from django import forms
from .models import Post, Comment, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    tags_field = forms.CharField(required=False, help_text="Comma-separated tags.", label='Tags')

        class Meta:
                model = Post
                        fields = ['title', 'content']

                            def save(self, commit=True, user=None):
                                    instance = super().save(commit=False)
                                            if user is not None:
                                                        instance.author = user
                                                                if commit:
                                                                            instance.save()
                                                                                        tags_text = self.cleaned_data.get('tags_field', '')
                                                                                                    if tags_text:
                                                                                                                    tags = [t.strip() for t in tags_text.split(',') if t.strip()]
                                                                                                                                    from .models import Tag
                                                                                                                                                    for tag_name in tags:
                                                                                                                                                                        tag_obj, _ = Tag.objects.get_or_create(name=tag_name)
                                                                                                                                                                                            instance.tags.add(tag_obj)
                                                                                                                                                                                                    return instance

                                                                                                                                                                                                    class CommentForm(forms.ModelForm):
                                                                                                                                                                                                        class Meta:
                                                                                                                                                                                                                model = Comment
                                                                                                                                                                                                                        fields = ['content']
                                                                                                                                                                                                                                widgets = {
                                                                                                                                                                                                                                            'content': forms.Textarea(attrs={'rows':3, 'placeholder':'Write a comment...'})
                                                                                                                                                                                                                                                    }

                                                                                                                                                                                                                                                    class UserRegisterForm(UserCreationForm):
                                                                                                                                                                                                                                                        email = forms.EmailField(required=True)

                                                                                                                                                                                                                                                            class Meta:
                                                                                                                                                                                                                                                                    model = User
                                                                                                                                                                                                                                                                            fields = ['username', 'email', 'password1', 'password2']

                                                                                                                                                                                                                                                                            class UserUpdateForm(forms.ModelForm):
                                                                                                                                                                                                                                                                                class Meta:
                                                                                                                                                                                                                                                                                        model = User
                                                                                                                                                                                                                                                                                                fields = ['username', 'email']

                                                                                                                                                                                                                                                                                                class ProfileUpdateForm(forms.ModelForm):
                                                                                                                                                                                                                                                                                                    class Meta:
                                                                                                                                                                                                                                                                                                            model = Profile
                                                                                                                                                                                                                                                                                                                    fields = ['bio', 'avatar']
                                                                                                                                                                                                                                                                                                                    