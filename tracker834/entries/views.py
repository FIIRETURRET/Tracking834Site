from django.shortcuts import render, get_object_or_404

import csv
from .models import Query
from django.core import serializers
from django.http import HttpResponse


# Create your views here.

def index(request):
    query_list = Query.objects.order_by('-queryName')[:10]
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