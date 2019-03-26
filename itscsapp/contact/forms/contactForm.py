from django import forms
from itscsapp.contact.models.contact import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'subject', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-md-6 col-sm-6 col-xs-12 contact-input-spac form-group',
                                           'placeholder': 'Nombre', 'id': 'f1'}),
            'phone_number': forms.TextInput(attrs={'class': 'col-md-6 col-sm-6 col-xs-12 contact-input-spac form-group',
                                                   'placeholder': 'Numero Telefonico', 'id': 'f2'}),
            'subject': forms.TextInput(attrs={'class': 'col-md-6 col-sm-6 col-xs-12 contact-input-spac form-group',
                                              'placeholder': 'Asunto', 'id': 'f3'}),
            'email': forms.EmailInput(attrs={'class': 'col-md-6 col-sm-6 col-xs-12 contact-input-spac form-group',
                                             'placeholder': 'Email', 'id': 'f4'}),
            'message': forms.Textarea(attrs={'class': 'col-md-12 col-sm-12 col-xs-12 contact-input-spac form-group',
                                             'placeholder': 'Mensaje', 'id': 'f5'}),
        }
        labels = {
            'name': '', 'phone_number': '', 'subject': '', 'email': '', 'message': ''
        }
