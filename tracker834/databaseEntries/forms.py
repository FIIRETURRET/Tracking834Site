from django import forms
from .models import Database


class NewDatabaseForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={ "style": "height: 300px",
                    "height": 100,
                    "cols": 100,
            }
        ),
        max_length=10000,
        #help_text='The max length of the text is 10000.',
    )

    class Meta:
        model = Database
        fields = "__all__"