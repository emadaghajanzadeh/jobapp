from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

# We have a form which is a ModelForm (we are converting an already existing model to a form)
# We have a class Meta within which we specify which model this form links to
class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        # Which fields of that model you are going to use?
        # fields = ['first_name', 'last_name', 'email']
        # Or alternatively:
        fields = '__all__'
        # exclude = ("first_name",)
        # Also, here you can see the list of all conversion from model to form: https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#field-types
        # Defning customized labels for fileds to be shown to users:
        labels = {
            'first_name': _('Enter first name'),
            'last_name': _('Enter last name'),
            'email': _('Enter email')
        }
        # Defining help texts:
        # help_texts = {
        #     'first_name': _("Enter characters only")
        # }
        # As well, customizing errors:
        error_messages = {
            'first_name':{
                'required': _("You cannot move forward without first name")
            },
        }



# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError("Invalid Last Name!1")
#     return value

# class SubscribeForm(forms.Form):
#     # Tip1: you can use different valiadtors as arguments.
#     first_name = forms.CharField(max_length=100, required=False, label="Enter your first name please!")
#     last_name = forms.CharField(max_length=100, validators=[validate_comma])
#     email = forms.EmailField(max_length=100)
#     # For custom validation, you should always use this format: clean_{attribute}: clean_first_name
#     # However this function is only specified for the field (first_name)
#     # So you can use validator to define some standards and apply them to all other fields.
#     def clean_first_name(self):
#         data = self.cleaned_data['first_name']
#         if "," in data:
#             raise forms.ValidationError("Invalid First Name!")
#         return data
