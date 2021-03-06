from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# Homepage
def home(request):
    return render(request, 'home.html', {})

# GET Todos los posts.
def posts(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'posts.html', {'posts' : posts })

    ## COMO SE TRADUCE LO DE ARRIBA EN SQL?
    ## SELECT * FROM Post WHERE publish_date <= DATETIME.NOW() ORDER BY publish_date

# GET Todos los posts usando Class View.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

# GET Un post por medio de su id (o Primary Key).
class PostDetailView(DetailView):
      model = Post
      template_name = 'post_detail.html'

#POST Crear un nuevo post
class PostCreateView(CreateView):
      model = Post
      form_class = PostForm
      template_name = 'post_new.html'
      #fields = '__all__'

#POST Actualizar un nuevo post
class PostUpdateView(UpdateView):
      model = Post
      form_class = PostForm
      template_name = 'post_update.html'
      #fields = ['title', 'text']

class PostDeleteView(DeleteView):
      model = Post
      form_class = PostForm
      template_name = 'post_delete.html'
      success_url = reverse_lazy('landing')
      #fields = ['title', 'text']
