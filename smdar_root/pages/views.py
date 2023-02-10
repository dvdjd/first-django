from django.shortcuts import render
# from django.http import HttpResponse
from . models import Page

# Create your views here.
def index (request, pagename) :
    # return HttpResponse("<h1>Hello Django Python</h1>")
    # return render(request, 'pages/page.html')
    
	pagename = '/' + pagename
	pg = Page.objects.get(permalink=pagename)
	context = {
		'title': pg.title,
		'content': pg.bodytext,
		'last_updated': pg.update_date
	}
	# assert False (set to True to test the view)
	return render(request, 'pages/page.html', context)

def login (request) :
    # return HttpResponse("<h1>Hello Django Python</h1>")
    return render(request, 'pages/login.html')
