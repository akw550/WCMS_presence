
from django.shortcuts import render, redirect
from posts.models import Posts, PostsForm
from django.views import View

# # Create your views here.
# def new(request):
#     form = PostsForm()
#     data = Posts.objects.all()
#     if request.method == 'POST':
#         form = PostsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     return render(request, 'new.html', {'title' : 'Add New Post', 'form': form, 'rows': data})


def new(request):
    return render(request, "new.html" ,{'title': 'new page title'})