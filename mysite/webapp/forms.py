from django import forms


class SentForm(forms.Form):
    name = forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }
        )

    )
    email = forms.EmailField(
        label='Enter Your Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Email'
            }
        )

    )
    subject = forms.CharField(
        label='Enter Your subject',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your subject'
            }
        )
    )
    message = forms.CharField(
        label='Enter Your Massage',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your massage'
            }
        )
    )

    file = forms.FileField()
