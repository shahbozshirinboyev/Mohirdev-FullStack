from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blog

# # Create your views here.
# def bloglistview(request):
#   blogs = Blog.objects.all()

#   context = {
#     "blogs": blogs,
#   }

#   return render(request, "home.html", context=context)

# def blogdetailview(request, id):
#   blog = get_object_or_404(Blog, id=id)
#   context = {
#     'blog': blog
#   }

#   # try:
#   #   blog = Blog.objects.get(id=id)
#   #   context = {
#   #     "blog": blog,
#   #   }
#   # except Blog.DoesNotExist:
#   #   raise Http404("No blog found")

#   return render(request, "blog_detail.html", context=context)
# # 10.37 sec

# Classlar yordamida view yaratish.

class Bloglistview(ListView):
  model = Blog
  template_name = "home.html"
  context_object_name = "blogs"

class BlogDetailView(DetailView):
  model = Blog
  template_name = "blog_detail.html"
  context_object_name = "blog"
