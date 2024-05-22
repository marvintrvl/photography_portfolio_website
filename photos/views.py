from django.views.generic import ListView
from .models import Photo, Category, Subcategory
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

def subcategory_view(request, category_name, subcategory_name):
    category = get_object_or_404(Category, name=category_name)
    subcategory = get_object_or_404(Subcategory, name=subcategory_name, category=category)
    photos = subcategory.photos.all()
    context = {
        'category': category,
        'subcategory': subcategory,
        'photos': photos,
        'category_name': category.name,
        'subcategory_name': subcategory.name,
    }
    return render(request, 'photos/categories.html', context)