from django.http import HttpResponse

def catalog(request):
	site_name = "Modern Musician"
	response_html = u"<html><body>Welcome to %s.</body></html>" % site_name
	return HttpResponse(response_html)

from django.shortcuts import render
def file_not_found_404(request):
    return render(request, '404.html',{page_title:'age Not Found'})