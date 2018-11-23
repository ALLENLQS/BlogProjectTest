#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : ALLEN
# @Time    : 2018/11/2 20:40
# @File    : forms.py
# @Software: PyCharm

from django import forms
from ckeditor_uploader.fields import RichTextUploadingFormField

class CommentForm(forms.Form):
    content = RichTextUploadingFormField(label="")

from app01.models import Comment
class CommentForm_aboutModel(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {
            "content":""
        }
    def clean_content(self):
        """
        form表单自定义校验的函数名称必须是clean_加上字段名称
        校验content，函数名称就叫做clean_content
        :return:
        """
        data = self.cleaned_data.get("content") #获取提交的值
        if "allen" in data:
            raise forms.ValidationError("don't speek allen") #这个错误类型是form表单类定义好的，
                                                            # 这里引发的错误，会放到errors当中
        else:
            return data