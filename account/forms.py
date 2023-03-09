from django import forms

from account.models import Profile


class ProfileForm(forms.ModelForm):

    blog_about = forms.CharField(
        widget=forms.Textarea(attrs={'style': 'width:100%'})
    )

    class Meta:
        model = Profile
        fields = ('blog_about', 'avatar',)
