from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.conf import settings
from  . models import Document
from  aws.forms import DocumentForm

def home(request):
    return render(request, 'aws/base.html', {})

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = DocumentForm()
    return render(request, 'aws/model_form_upload.html', {'form': form})
