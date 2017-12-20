from django import forms
from he import models
from django.forms import widgets as Fw
from django.forms import fields
import re

class UserInfoModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['username','password','email']

    def clean_password(self):
        password = self.cleaned_data['password']
        p = re.compile('^[a-zA-Z]\w{5,14}$')
        if p.match(password):
            return password
        else:
            raise forms.ValidationError('以字母开头5-15位密码',code='password_length_error')

    def clean_username(self):
        username = self.cleaned_data['username']
        p = len(username)
        if p>3:
            return username
        else:
            raise forms.ValidationError('用户名长度不能小于3位',code='username_len_error')


class LoginModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['username','password']


class EditModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['username','email']


class RegitserModelForm(forms.Form):
    username = fields.CharField(
        error_messages={'required':'用户名不能为空'}
    )
    password = fields.CharField(
        error_messages={'required': '密码不能为空'},
    )
    email = fields.EmailField(
        error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'}
    )


class PublicModelForm(forms.ModelForm):
    class Meta:
        model = models.Public
        exclude = ['add_time','run_time']



