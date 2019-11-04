from django.shortcuts import render, get_object_or_404, redirect

import datetime
import csv, io
from .models import Query
from .forms import NewQueryForm
from django.core import serializers
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required


# Create your views here.

@login_required
def index(request):
    query_list = Query.objects.order_by('-queryName')
    context = {
        'query_list': query_list,
    }
    return render(request, 'entries/index.html', context)

@login_required
def detail(request, query_id):
    if request.method == "POST":
        if request.POST.get('queryName'):
            query = get_object_or_404(Query, pk=query_id)
            query.queryName = request.POST.get('queryName')
            query.folderName = request.POST.get('folderName')
            query.subfolder = request.POST.get('subfolder')
            query.subfolder2 = request.POST.get('subfolder2')
            query.queryUsedFor = request.POST.get('queryUsedFor')
            query.files = request.POST.get('files')
            query.convertYN =request.POST.get('convertYN')
            query.conversionStartDate = request.POST.get('conversionStartDate')
            query.assignedTo = request.POST.get('assignedTo')
            query.conversionCompletionDate = request.POST.get('conversionCompletionDate')
            query.newNameInBI = request.POST.get('newNameInBI')
            query.save()
            return redirect('entries:index')
    else:
        query = get_object_or_404(Query, pk=query_id)
        data = serializers.serialize( "python", Query.objects.all())
        return render(request, 'entries/detail.html', {'query': query, 'data': data})

@login_required
def new_query(request):
    if request.method == 'POST':
        form = NewQueryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            return redirect('entries:index')
    else:
        form = NewQueryForm()
    return render(request, 'entries/new_query.html', {'form': form})

@login_required
def export_entries_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="entries.csv"'

    writer = csv.writer(response)
    writer.writerow(['Folder Name', 'Sub folder/Sub folder2', 'Query used for', 'Query Name',
                        'Files', 'Convert Y/N', 'Conversion Start Date', 'Assigned to',
                        'Conversion Completion Date', 'New Name in BI'])

    entries = Query.objects.all().values_list('folderName', 'subfolder', 'queryUsedFor', 'queryName',
                        'files', 'convertYN', 'conversionStartDate', 'assignedTo',
                        'conversionCompletionDate', 'newNameInBI')
    for entry in entries:
        writer.writerow(entry)

    return response


@login_required
# Makes it so only super users can access this
@permission_required('admin.can_add_log_entry')
def csv_upload(request):
    template = 'entries/csv_upload.html'

    prompt = {
        'order': 'order of CVS should be Folder Name | Sub Folder Name | Query Used For | Query Name | Files | Convert(y/n) | Conversion Start Date | Assigned to | Conversion Complete Date | New Name In BI'
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
        if column[5] == "True" or column[5] == "true":
            convertYN = True
        else:
            convertYN = False
        if column[6] != "":
            try:
                conversionStartDate = datetime.datetime.strptime(column[6], "%d/%m/%Y").strftime("%Y-%m-%d")
            except ValueError:
                conversionStartDate = None

        else:
            conversionStartDate = None
        if column[8] != "":
            try:
                conversionCompletionDate = datetime.datetime.strptime(column[8], "%d/%m/%Y").strftime("%Y-%m-%d")
            except ValueError:
                conversionStartDate = None
        else:
            conversionCompletionDate = None

        Query.objects.update_or_create(
            # filter on the unique value of 'queryName'
            queryName = column[3],
            # update these fields, or create a new object with these values
            defaults={
                'folderName': column[0],
                'subfolder': column[1],
                'queryUsedFor': column[2],
                'files': column[4],
                'convertYN': convertYN,
                'conversionStartDate': conversionStartDate,
                'assignedTo': column[7],
                'conversionCompletionDate': conversionCompletionDate,
                'newNameInBI': column[9],
            }
        )
    context = {}
    return render(request, template, context)