from django import forms

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'Paypal')
)

class CheckoutForm(forms.Form):
    address = forms.CharField(widget = forms.TextInput(attrs = {
        "placeholder": 'Address',
        "class": 'stext-111 cl8 plh3 size-111 p-lr-15'
    }))
    state = forms.CharField(widget = forms.TextInput(attrs = {
        "placeholder": 'State',
        "class": 'stext-111 cl8 plh3 size-111 p-lr-15'
    }))
    city = forms.CharField(widget = forms.TextInput(attrs = {
        "placeholder": 'City',
        "class": 'stext-111 cl8 plh3 size-111 p-lr-15'
    }))
    pincode = forms.CharField(widget = forms.TextInput(attrs = {
        "placeholder": 'Pincode',
        "class": 'stext-111 cl8 plh3 size-111 p-lr-15'
    }))

    payment_option = forms.ChoiceField(choices = PAYMENT_CHOICES, widget = forms.Select(attrs = {
        "class": 'rs1-select2 rs2-select2 bor8 bg0 m-b-12 m-t-9',
        "class": 'js-select2'
    }))