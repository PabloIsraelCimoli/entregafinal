from django.shortcuts import redirect, render
from .models import Post
# importar CommentForm
from .froms import CommentForm

# para usar frontpage.html
#importar model post


def frontpage(request):
    posts=Post.objects.all()
    return render(request, 'blog/frontpage.html',{'posts':posts})

# crear la nuevo view de post detail
#slug viene de model de la base de datos
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm
    return render(request, 'blog/post_detail.html',{'post':post, 'from': 'from'})
    
