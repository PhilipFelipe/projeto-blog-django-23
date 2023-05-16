from blog.views import index
from django.urls import path

app_name = 'blog'

urlpatterns = [
    # blog:index
    path('', index, name='index')
]
