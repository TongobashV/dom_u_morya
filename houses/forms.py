from django import forms

class HousesFilterForms(forms.Form):
    min_price = forms.IntegerField(label="от", required=False)
    max_price = forms.IntegerField(label="до", required=False)
    query = forms.CharField(label="описание", required=False)