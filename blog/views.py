import datetime
from django.utils import timezone
import pytz
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Article, Writer
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ArticleCreationForm

# Create your views here.

# Index view
def index_view(request):

    article_in_last_30_days = Count(
        'article_writer', 
        filter=Q(article_writer__created_at__gt=timezone.now() - datetime.timedelta(days=30))
    )

    # count the articles of each writer and Filter articles from last 30 days
    writers_listing = Writer.objects.annotate(
        total_articles=Count('article_writer'), 
        article_in_30_days=article_in_last_30_days
    )

    context = {
        'writers_listing':writers_listing, 
    }

    return render (request, 'index.html', context)

# Artice Create view
@login_required(login_url='login')
def article_create_view(request):
   
    article_form = ArticleCreationForm(request.POST or None)

    # create new article
    if request.method == 'POST':
        if article_form.is_valid():
            title = request.POST.get('title')
            content = request.POST.get('content')
            article = Article.objects.create(title=title, content=content, written_by=request.user.writer)
            article.save()
            return redirect('/')
    else:
        article_form = ArticleCreationForm()

    context = {'article_form':article_form}
    
    return render(request, 'article-create.html', context)

# Artice Detail view
@login_required(login_url='login')
def article_detail_view(request, pk):
    
    # get specific article by id.
    article = get_object_or_404(Article, pk=pk)
    
    context = {
        'article':article,
    }

    return render(request, 'article-detail.html', context)

# Artice Edit view
@login_required(login_url='login')
def article_update_view(request, pk):
    # get specific article by id.
    article = get_object_or_404(Article, pk=pk)
    
    # get article owner
    article_writer = str(article.written_by)
    # get loggedin_user
    loggedin_user = str(request.user)

    article_form = ArticleCreationForm(request.POST or None, instance=article)
    
    # only allow the article owner to edit the article
    if (article_writer == loggedin_user):
        if request.method == 'POST':
            if article_form.is_valid():
                article_form.save()
                return redirect('/')
    else:
        return HttpResponse("You're not permitted to edit this article")
    
    context = {
        'article_form':article_form,
    }

    return render(request, 'article-update.html', context)

# Artice Approve view
@login_required(login_url='login')
def article_approve_view(request):
    
    all_articles = Article.objects.all()

    # check if looged in user is an editor
    user_is_editor = request.user.writer.is_editor
    
    if user_is_editor:
        if request.method == 'POST':
            # update the article status
            article_id = request.POST.get('id')
            article = Article.objects.get(id=article_id)
            
            if article.status == 'APPROVED':
                article.status = 'REJECTED'
            else:
                article.status = 'APPROVED'
            
            article.edited_by = request.user.writer
            
            article.save()
    else:
        return HttpResponse("You're not permitted to view this page")
    

    context = {
        'all_articles':all_articles,
    }

    return render(request, 'article-approve.html', context)


# Artice Edited view
@login_required(login_url='login')
def article_edited_view(request):
    
    # check if looged in user is an editor
    user_is_editor = request.user.writer.is_editor

    if user_is_editor:
        articles = request.user.writer.article_editor.all()
    else:
        return HttpResponse("You're not permitted to view this page")
    

    context = {
        'articles':articles,
    }

    return render(request, 'articles-edited.html', context)
    


