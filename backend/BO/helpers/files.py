from django.core.files.storage import FileSystemStorage
from django.conf import settings

def save_image(binary_file, image_name):
  
    with open(binary_file, "rb") as outstream:
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save(image_name, outstream)

  # Create a FileSystemStorage object.
#   storage = FileSystemStorage(location=settings.MEDIA_ROOT)

  # Save the image file.
#   filename = storage.save(image_name, binary_file)

  # Return the path to the saved image file.
    return f"{settings.MEDIA_URL}/{image_name}"