from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField(min_length=4,max_length=100,help_text='Your Name')
    email=forms.EmailField(min_length=6,max_length=60,help_text='email',validators=EmailValidator(message='Enter a valid email address'))
    subject=forms.CharField(min_length=8,max_length=200,help_text='subject')
    msg=forms.Textarea(min_length=8,max_length=200,help_text='subject')