from django import forms
from django.forms import ModelForm, ImageField, Form, CharField, PasswordInput
from .models import Product
from .models import User

class UserRegisterForm(forms.ModelForm):
    avatar = ImageField()
    password = CharField(max_length = 128, widget=PasswordInput)

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ("avatar", "username", "first_name", "last_name")




class UserLoginForm(Form):
    username = CharField(max_length=128)
    password = CharField(max_length=128, widget=PasswordInput)

class ProductCreateForm(forms.ModelForm):
    image = ImageField()
    class Meta:
        model= Product
        fields = "__all__"


class ProductUpdateForm(forms.ModelForm):
    image = ImageField()
    class Meta:
        model = Product
        fields = "__all__"