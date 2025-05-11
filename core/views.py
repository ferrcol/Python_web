from django.shortcuts import render, HttpResponse

html_base = """
    <h1>First web page</h1>
    <ul>
        <li><a href="/">Main</a></li>
        <li><a href="/about/">about</a></li>
        <li><a href="/portfolio/">portfolio</a></li>
        <li><a href="/contact/">contact</a></li>
    </ul>
"""

# Create your views here.
def home(request):
    return HttpResponse(html_base+"<h1>First web test</h1><h2>Test1</h2>")

def about(request):
    return HttpResponse(html_base+"<h1>About test</h1><h2>Test2</h2>")

def portfolio(request):
    return HttpResponse(html_base+"<h1>portfolio web test</h1><h2>Test2</h2>")

def contact(request):
    return HttpResponse(html_base+"<h1>contact web test</h1><h2>Test2</h2>")
