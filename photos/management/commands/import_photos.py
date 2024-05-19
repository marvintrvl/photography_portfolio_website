import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from photos.models import Photo, Category

class Command(BaseCommand):
    help = 'Import photos from predefined folders into corresponding categories'

    def handle(self, *args, **kwargs):
        base_path = 'C:/Users/menzm/Desktop/Studium/Photography_Website/photo_website/photos/static/ws_e'
        categories_folders = {
            'city-scapes': 'City scapes',
            'landscapes': 'Landscapes',
            'nature': 'Nature',
            'portraits': 'Portraits',
            'street-photography': 'Street photography',
            'drone-photography': 'Drone photography'
        }

        for folder, category_name in categories_folders.items():
            folder_path = os.path.join(base_path, folder)
            if not os.path.isdir(folder_path):
                self.stderr.write(self.style.ERROR(f'Folder {folder_path} does not exist'))
                continue

            category, created = Category.objects.get_or_create(name=category_name)

            for filename in os.listdir(folder_path):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    src_file_path = os.path.join(folder_path, filename)
                    dst_file_path = os.path.join(settings.MEDIA_ROOT, 'photos', filename)

                    # Create the destination directory if it doesn't exist
                    os.makedirs(os.path.dirname(dst_file_path), exist_ok=True)

                    # Copy the file to the destination directory
                    shutil.copy2(src_file_path, dst_file_path)

                    # Set the relative path for the image field
                    relative_path = os.path.join('photos', filename)

                    # Check if the photo already exists in the database
                    photo_exists = Photo.objects.filter(category=category, image=relative_path).exists()

                    if photo_exists:
                        self.stdout.write(self.style.WARNING(f'{filename} already exists in {category_name}'))
                    else:
                        Photo.objects.create(category=category, image=relative_path)
                        self.stdout.write(self.style.SUCCESS(f'Successfully added {filename} to {category_name}'))

        self.stdout.write(self.style.SUCCESS('All photos have been imported'))
