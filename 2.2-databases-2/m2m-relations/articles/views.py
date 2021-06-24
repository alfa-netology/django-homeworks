from django.shortcuts import render

from articles.models import Article, Scope


def articles_list(request):
    template = 'articles/news.html'
    articles = list()

    data = Article.objects.all().order_by('-published_at')
    for item in data:        
        scope = Scope.objects.filter(article=item).all().order_by('-is_main', 'tag')

        articles.append({
           'title': item.title,
           'text': item.text,
           'image': item.image,
           'scope': scope,
        })

    context = {'articles': articles}
    
    return render(request, template, context)
