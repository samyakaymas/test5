from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm,Form
from .models import User
from django.apps import apps
Chapter = apps.get_model('theoryTag', 'Chapter')
Subject = apps.get_model('theoryTag', 'Subject')
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=254, required=True)
    chapter = forms.ModelChoiceField(queryset=Chapter.objects.all())
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'subject', 'chapter')

class SignInForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

class PasswordForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'] = forms.ChoiceField(choices=tuple([(user.pk,user.username) for user in User.objects.order_by('username')]),required=True)
        self.fields['password1'] = forms.CharField(widget=forms.PasswordInput)
        self.fields['password2'] = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        super(PasswordForm,self).clean()
        form_data = self.cleaned_data
        if form_data['password1'] != form_data['password2']:
            self._errors["password2"] = self.error_class(["Password do not match"])
            del form_data['password2']
        return form_data

class PermissionForm(Form):
    CHOICES = [("","")]
    CHOICES_ = [(user.pk,user.username) for user in get_user_model().objects.all()]
    CHOICES.extend(CHOICES_)
    CHOICES = tuple(CHOICES)
    username = forms.ChoiceField(choices=CHOICES,required=True)
    can_add_theory = forms.BooleanField(required=False)
    can_edit_theory = forms.BooleanField(required=False)
    can_see_theory = forms.BooleanField(required=False)
    can_add_tag = forms.BooleanField(required=False)
    can_see_tag = forms.BooleanField(required=False)
    can_add_cross = forms.BooleanField(required=False)
    can_see_cross = forms.BooleanField(required=False)