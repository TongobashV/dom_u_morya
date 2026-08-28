from django import forms

class HousesFilterForms(forms.Form):
    min_price = forms.IntegerField(label="від", required=False)
    max_price = forms.IntegerField(label="до", required=False)
    query = forms.CharField(label="опис", required=False)
    ordering = forms.ChoiceField(label="сортування", required=False, choices=[
        ("name", "за алфавітом"),
        ("price", "дешеві зверху"),
        ("-price", "дорожчі зверху")
    ])
