from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from allauth.account.forms import SignupForm
from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError
from datetime import date
from .models import UserProfile

PAYMENT_CHOICES = (
    # ('S', 'Stripe'),
    ('P', 'Card'),
    ('C', 'Cash')
)       


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    phone_number = forms.CharField(required=True,max_length=10)

    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    phone_number = forms.CharField(required=True)

    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    phone_number = forms.CharField(max_length=10 )
    date_of_birth = forms.DateTimeField()
   
    
    def save(self, request):
        UserProfile.user = super(CustomSignupForm, self).save(request)
        UserProfile.user.first_name = self.cleaned_data['first_name']
        UserProfile.user.last_name = self.cleaned_data['last_name']
        UserProfile.user.phone_number = self.cleaned_data['phone_number']
        UserProfile.user.date_of_birth = self.cleaned_data['date_of_birth']
        
        
        
        UserProfile.user.save()
        return  UserProfile.user

class RestrictEmailAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        RestrictedList = ['Your restricted list goes here.']
        if email in RestrictedList:
            raise ValidationError('You are restricted from registering.\
                                                  Please contact admin.')
        return email

class UsernameMaxAdapter(DefaultAccountAdapter):
    def clean_username(self, username):
        if len(username) > 'Your Max Size':
            raise ValidationError('Please enter a username value\
                                      less than the current one')
         
        # For other default validations.
        return DefaultAccountAdapter.clean_username(self, username)
