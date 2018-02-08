from django import forms

class ComplaintForm(forms.Form):
    title = forms.CharField(label='title',
                            max_length=100,
                            help_text="kya problem hai?"
                            )
    complaint = forms.CharField(label='complaint',
                                max_length=3000,
                                widget=forms.Textarea(attrs={'size': '40'})
                                )