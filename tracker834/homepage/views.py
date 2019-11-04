from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.
@login_required
def index(request):
    context = { }
    return render(request, 'homepage/index.html', context)