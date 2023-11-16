from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_name',
            'post_text',
            'author',
            'category',
        ]
        labels = {
            'post_name': 'Заголовок',
            'post_text': 'Текст',
            'author': 'Автор',
            'category': 'Категория',
        }


    def clean(self):
        cleaned_data = super().clean()
        post_text = cleaned_data.get('post_text')
        if post_text is not None and len(post_text) < 30:
            raise ValidationError({
                'post_text': "Текст поста не может быть менее 30 символов."
            })

        post_name = cleaned_data.get("name")
        if post_name == post_text:
            raise ValidationError(
                "Текст поста не должен быть идентичным названию."
            )
        return cleaned_data
