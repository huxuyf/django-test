from django import forms

class myform(forms.Form):
    user_name = forms.CharField(max_length=10,label='你的姓名',help_text='请输入您的姓名')
    age = forms.IntegerField(min_value=0,label='你的年龄',help_text='请输入您的年龄')
    address = forms.CharField(max_length=100,label='地址')
