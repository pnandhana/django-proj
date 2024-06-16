from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import UploadFileForm
from .models import Certificate

def index(request):
    return render(request, 'index.html')

def upload_template(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle uploaded file here (e.g., save to media directory)
            uploaded_file = form.cleaned_data['file']
            # Example: save file to media directory
            with open('media/' + uploaded_file.name, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            return HttpResponse('File uploaded successfully!')
    else:
        form = UploadFileForm()
    return render(request, 'upload_template.html', {'form': form})

def generate_certificates(request):
    if request.method == 'POST':
        # Assuming you have a model named Certificate
        # Logic to generate certificates based on uploaded file or data
        # Example: create a certificate and save it
        certificate = Certificate(name='John Doe', template='media/template.pdf')
        certificate.save()
        return HttpResponse('Certificates generated!')
    else:
        # Render a form or page to upload data for generating certificates
        return render(request, 'generate_certificates.html')

def upload_excel(request):
    if request.method == 'POST':
        # Handle the uploaded file here
        uploaded_file = request.FILES['excel_file']
        # Process the file as needed
        return HttpResponse('File uploaded successfully!')
    return render(request, 'upload_excel.html')
