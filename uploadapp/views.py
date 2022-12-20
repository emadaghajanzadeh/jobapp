from django.shortcuts import render
from uploadapp.forms import UploadForm

# Create your views here.

def upload_image(request):
    form = UploadForm()
    return render(request, 'uploadapp/add_image.html', {'form': form})
