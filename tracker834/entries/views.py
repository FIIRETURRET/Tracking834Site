from django.shortcuts import render, get_object_or_404

import csv, io
from .models import Query
from django.core import serializers
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required


# Create your views here.

def index(request):
    query_list = Query.objects.order_by('-queryName')
    context = {
        'query_list': query_list,
    }
    return render(request, 'entries/index.html', context)
    
    
def detail(request, query_id):
    query = get_object_or_404(Query, pk=query_id)
    data = serializers.serialize( "python", Query.objects.all() )
    return render(request, 'entries/detail.html', {'query': query, 'data': data})
    
    
def export_entries_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="entries.csv"'

    writer = csv.writer(response)
    writer.writerow(['Folder Name', 'Sub Folder Name'])

    entries = Query.objects.all().values_list('folderName', 'subfolder')
    for entry in entries:
        writer.writerow(entry)

    return response
    
# Makes it so only super users can access this    
@permission_required('admin.can_add_log_entry')
def csv_upload(request):
    template = 'entries/csv_upload.html'
    
    prompt = {
        'order': 'order of CVS should be'
    }
    
    if request.method=="GET":
        return render(request, template, prompt)
    
    # Get the file
    csv_file = request.FILES['file']
    
    # Check to see if the file uploaded is .csv
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a .csv file')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    # Skip the header
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, create = Query.objects.update_or_create(
            queryName = column[3],
        )
    context = {}
    return render(request, template, context)