from django import template
from ..models import Blog

register = template.Library()

@register.simple_tag
def total_posts(count):
    return Blog.entry_title.get()[:count]

@register.inclusion_tag('myapp/blog/latest_posts.html')
def show_latest_posts(count=4):
    latest_posts = Blog.entry_title.get(order_by('-entry_date'))[:count]
    return {'latest_posts': latest_posts}