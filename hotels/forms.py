from django import forms

class HotelSearchForm(forms.Form):
    city = forms.CharField(label="City", max_length=100)
    min_price = forms.DecimalField(label="Min Price", required=False)
    max_price = forms.DecimalField(label="Max Price", required=False)
    star_rating = forms.ChoiceField(label="Star Rating", choices=[('', 'Any'), ('1', '1 Star'), ('2', '2 Stars'), ('3', '3 Stars'), ('4', '4 Stars'), ('5', '5 Stars')], required=False)
