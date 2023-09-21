# from django.shortcuts import render
from django.http import HttpResponse
from .models import Type, Article, Contact, Booking

# Create your views here.

def index(request):
    articles  = Article.objects.filter(available=True)
    formatted_articles = ["<li>{}</li>".format(article.titel) for article in articles]
    message = """<ul>{}</ul>""".format("\n".join(formatted_articles))
    return HttpResponse(message)

def listing(request):
    articles  = Article.objects.filter(available=True)
    formatted_articles = ["<li>{}</li>".format(article.titel) for article in articles]
    message = """<ul>{}</ul>""".format("\n".join(formatted_articles))
    return HttpResponse(message)

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    types = " ".join([type.name for type in article.types.all()])
    message = "l'article {} est concue pour en plusieurs formats, notemment pour {}".format(article.titel, types)
    return HttpResponse(message)

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
    return HttpResponse(message)