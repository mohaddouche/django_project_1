from django.shortcuts import render
from django.http import HttpResponse
from .models import Type, Article, Contact, Booking
from django.template import loader

# Create your views here.

def index(request):
    articles  = Article.objects.filter(available=True)
    template = loader.get_template('store/index.html')
    context = {'articles': articles}
    return render(request, 'store/index.html', context)

def listing(request):
    articles  = Article.objects.filter(available=True)
    context = {
        'articles': articles
    }
    return render(request, 'store/listing.html', context)


def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    types_name = " ".join([type.name for type in article.types.all()])
    context = {
        'article_title': article.titel,
        'types_name': types_name,
        'article_id' : article.id,
        'thumbnail': article.picture
    }
    return render(request, 'store/detail.html', context)

def search(request):
    query = request.GET.get('query')

    if not query : 
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(titel__icontains=query)

        if not articles.exists():
            message = "Nous n'avons trouvé aucun résultat !"
        else:
            articles = ["<li>{}</li>".format(article.titel) for article in articles]
            message = """Nous avon trouvé les articles correspondant à votre requete ! Les voici : 
            <ul>{}</ul>""".format("</li><li>".join(articles))
    title = "Résulats pour la requete %s"%query
    context = {
        'articles': articles,
        'title': title
    }
    return render(request, 'store/search.html', context)