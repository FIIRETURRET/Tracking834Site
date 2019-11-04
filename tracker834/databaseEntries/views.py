from django.shortcuts import render, get_object_or_404, redirect


from .models import Database
from .forms import NewDatabaseForm

from django.core import serializers
from django.contrib.auth.decorators import permission_required, login_required



# Create your views here.

@login_required
def index(request):
    database_list = Database.objects.order_by('-data')
    context = {
        'database_list': database_list,
    }
    return render(request, 'databaseEntries/index.html', context)

@login_required
def detail(request, database_id):
    if request.method == "POST":
        if request.POST.get('data'):
            database = get_object_or_404(Database, pk=database_id)
            database.data = request.POST.get('data')
            database.whereFound = request.POST.get('whereFound')
            database.description = request.POST.get('description')
            database.goodLink = request.POST.get('goodLink')
            database.needed = request.POST.get('needed')
            database.notes = request.POST.get('notes')
            database.save()
            return redirect('databases:index')
    else:
        database = get_object_or_404(Database, pk=database_id)
        data = serializers.serialize( "python", Database.objects.all().order_by('-pk') )
        return render(request, 'databaseEntries/detail.html', {'database': database, 'data': data})

@login_required
def new_database(request):
    if request.method == 'POST':
        form = NewDatabaseForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            return redirect('databases:index')
    else:
        form = NewDatabaseForm()
    return render(request, 'databaseEntries/new_database.html', {'form': form})