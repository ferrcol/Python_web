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
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    return render(request, "core/portfolio.html")

def contact(request):
    return render(request, "core/contact.html")
