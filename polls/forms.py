from django import forms

class dataForm(forms.Form):
    csv_data = forms.FileField()