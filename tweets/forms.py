from django import forms

class TweetForm(forms.Form):
    text = forms.CharField(max_length=160,
                           widget=forms.Textarea(attrs={
                                            "rows": 1,
                                            "cols": 65})
                           )
    country = forms.CharField(widget=forms.HiddenInput(), required=False)

class SearchForm(forms.Form):
    query = forms.CharField(label="Enter a keyword"
                                  "to search for",
                            widget=forms.TextInput(attrs={
                                "size": 32,
                                "class": 'form-control'
                            }))