from django.shortcuts import render, get_object_or_404

from .models import Entry834

# Create your views here.

def index(request):
    entries_list = Entry834.objects.order_by('-testDate')[:10]
    context = {
        'entries_list': entries_list,
    }
    return render(request, 'entries/index.html', context)
    
    
def detail(request, entry_id):
    entry = get_object_or_404(Entry834, pk=entry_id)
    return render(request, 'entries/detail.html', {'entry': entry})