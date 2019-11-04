from django import forms
from .models import Query


class NewQueryForm(forms.ModelForm):

    conversionStartDate = forms.DateField(
        widget = forms.SelectDateWidget(

        ),
        label = 'Conversion Start Date'
    )

    conversionCompletionDate = forms.DateField(
        widget = forms.SelectDateWidget(

        ),
        label = 'Conversion Completion Date'
    )

    convertYN = forms.NullBooleanField(required=False, label='Query Converted')

    folderName = forms.CharField(label='Folder Name')
    subfolder = forms.CharField(label='Sub-folder')
    subfolder2 = forms.CharField(label='Sub-folder-2')
    queryUsedFor = forms.CharField(label='Query-Used-For')
    queryName = forms.CharField(label='Query Name')
    files = forms.CharField(label='Files')
    assignedTo = forms.CharField(label='Assigned To')
    newNameInBI = forms.CharField(label='New Name in BI')

    class Meta:
        model = Query
        fields = "__all__"