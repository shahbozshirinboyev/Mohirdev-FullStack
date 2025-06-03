from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def bloglistview(request):
  blogs = Blog.objects.all()

  context = {
    "blogs": blogs,
  }

  return render(request, "home.html", context=context)

def blogdetailview(request, id):
  blog = get_object_or_404(Blog, id=id)
  context = {
    'blog': blog
  }

  # try:
  #   blog = Blog.objects.get(id=id)
  #   context = {
  #     "blog": blog,
  #   }
  # except Blog.DoesNotExist:
  #   raise Http404("No blog found")

  return render(request, "blog_detail.html", context=context)
# 10.37 sec