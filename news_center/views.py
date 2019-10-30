from django.shortcuts import render
from django.utils import timezone
from .models import New

# Create your views here.
def news_list(request):
    news = New.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news_list.html', {'news':news})