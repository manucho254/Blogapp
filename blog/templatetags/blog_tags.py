from django import template
from ..models import Blog

register = template.Library()

@register.simple_tag
def total_posts():
    model = Blog
    return (object.entry_title())

@register.inclusion_tag('myapp/blog/latest_posts.html')
def show_latest_posts(count=8):
    latest = Blog.objects.all()
    latest_posts = latest.entry_pic.order_by('-entry_date')[:count]
    return {'latest_posts': latest_posts}