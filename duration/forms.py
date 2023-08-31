from django import forms

class UserInfoForm(forms.Form):
    # name = forms.CharField(label="Name", max_length=100)
    # phone_number = forms.CharField(label="Phone Number")
    # email = forms.EmailField(label="Email Id")
    url_link = forms.URLField(label="URL Link")

