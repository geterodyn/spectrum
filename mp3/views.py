from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from mp3.forms import UploadFileForm

from mp3.processing import uploaded_file_handle

# Create your views here.

def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data = uploaded_file_handle(request.FILES['mp3_file'])
            return render(request, 'mp3/upload.html', {'form': form, 'data': data})
    else:
        form = UploadFileForm()
    return render(request, 'mp3/upload.html', {'form': form})