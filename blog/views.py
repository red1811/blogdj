from django.shortcuts import render, redirect
from .models import Post, Comments
from django.utils import timezone
from .forms import PostForm, CommentForm
# Create your views here.


def for_base(request):
    return render(request, 'blog/base.html', {'user': request.user})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    user = request.user
    return render(request, 'blog/post_list.html', {'posts': posts, 'user': user})


def make_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_done')
        else:
            return redirect('make_post')
    else:
        form = PostForm()
        return render(request, 'blog/make_post.html', {'form': form})


def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comments.objects.filter(post=post)
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            return redirect('post_details', pk=pk)
    else:
        form = CommentForm()
        return render(request, 'blog/post_detail.html', {'post': post,
                                                         'user': request.user,
                                                         'form': form,
                                                         'comments': comments})


def draft_posts(request):
    posts = Post.objects.filter(published_date=None).order_by('-created_date')
    return render(request, 'blog/drafts.html', {'posts': posts, 'user': request.user})


def publish_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.published_date = timezone.now()
    post.save()

    return redirect('post_details', pk=post.pk)


def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            postl = form.save(commit=False)
            postl.author = request.user
            postl.save()

            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/edit.html', {'form': form, 'post': post})


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')


def post_done_view(request):
    return render(request, 'blog/post_done.html')


def delete_comment(request, pk):
    comment = Comments.objects.get(pk=pk)
    post = Post.objects.get(pk=comment.post.pk)
    comment.delete()
    return redirect('post_details', pk=post.pk)


def move_to_draft(request, pk):
    post = Post.objects.get(pk=pk)
    post.published_date = None
    post.save()
    return redirect('post_done')


def add_like(request, pk):
    post = Post.objects.get(pk=pk)
    post.like += 1
    post.like_activated_author.append(request.user.username)
    post.save()

    return redirect('post_details', pk=pk)


def remove_like(request, pk):
    post = Post.objects.get(pk=pk)
    post.like -= 1
    post.like_activated_author.remove(request.user.username)
    post.save()

    return redirect('post_details', pk=pk)


def add_like_to_comment(request, pk):
    comment = Comments.objects.get(post=Post.objects.get(pk=pk))
    comment.like += 1
    comment.like_activated_author.append(request.user.username)
    comment.save()

    return redirect('post_details', pk=pk)


def remove_like_from_comment(request, pk):
    comment = Comments.objects.get(post=Post.objects.get(pk=pk))
    comment.like -= 1
    comment.like_activated_author.remove(request.user.username)
    comment.save()

    return redirect('post_details', pk=pk)


def post_likes(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_likes.html', {'post': post})


def comment_likes(request, pk):
    comment = Comments.objects.get(post=Post.objects.get(pk=pk))
    return render(request, 'blog/comment_likes.html', {'comment': comment})