from django.shortcuts import render

# Create your views here.
def index(request):
  header_str = 'Hello, Human'
  context = {
    'worldHeader': header_str
  }
  return render(request, 'index.html', context)

