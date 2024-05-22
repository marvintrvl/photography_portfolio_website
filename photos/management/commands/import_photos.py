import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from photos.models import Photo, Category, Subcategory

class Command(BaseCommand):
    help = 'Import photos from predefined folders into corresponding categories and subcategories'

    def handle(self, *args, **kwargs):
        base_path = os.path.join(settings.BASE_DIR, 'photos/static')

        for category_folder in os.listdir(base_path):
            category_path = os.path.join(base_path, category_folder)
            if os.path.isdir(category_path):
                category, created = Category.objects.get_or_create(name=category_folder)
                for subcategory_folder in os.listdir(category_path):
                    subcategory_path = os.path.join(category_path, subcategory_folder)
                    if os.path.isdir(subcategory_path):
                        subcategory, created = Subcategory.objects.get_or_create(name=subcategory_folder, category=category)
                        for filename in os.listdir(subcategory_path):
                            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                                src_file_path = os.path.join(subcategory_path, filename)
                                dst_file_path = os.path.join(settings.MEDIA_ROOT, 'photos', filename)
                                # Create the destination directory if it doesn't exist
                                os.makedirs(os.path.dirname(dst_file_path), exist_ok=True)
                                # Copy the file to the destination directory
                                shutil.copy2(src_file_path, dst_file_path)
                                # Set the relative path for the image field
                                relative_path = os.path.join('photos', filename)
                                # Check if the photo already exists in the database
                                photo_exists = Photo.objects.filter(subcategory=subcategory, image=relative_path).exists()
                                if photo_exists:
                                    self.stdout.write(self.style.WARNING(f'{filename} already exists in {subcategory.name}'))
                                else:
                                    Photo.objects.create(subcategory=subcategory, image=relative_path)
                                    self.stdout.write(self.style.SUCCESS(f'Successfully added {filename} to {subcategory.name}'))
        self.stdout.write(self.style.SUCCESS('All photos have been imported'))