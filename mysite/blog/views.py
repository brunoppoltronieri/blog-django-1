from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post

def post_list(request): 
    context = {
        'posts':  Post.objects.all()
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    context = {
        'post':  Post.objects.get(pk=pk)
    }
    return render(request, 'blog/post_detail.html', context)

def post_new(request):
    # from IPython import embed; embed()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('post_detail', post.pk)
    else:     
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('post_detail', post.pk)
    else:     
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
