from django.views.generic import ListView
from .models import Photo, Category
from django.shortcuts import render, get_object_or_404

def base_view(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'photos/base.html', context)

class IndexView(ListView):
    model = Photo
    template_name = 'photos/index.html'
    context_object_name = 'recent_photos'
    ordering = ['-id']
    paginate_by = 10

def category_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    photos = category.photos.all()
    context = {
        'category': category,
        'photos': photos,
        'category_name': category.name,  # Add this line
        'category_photos': photos,  # Add this line
    }
    return render(request, 'photos/categories.html', context)