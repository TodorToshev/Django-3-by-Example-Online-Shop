from django import forms
<<<<<<< Updated upstream
from django.utils.translation import gettext_lazy as _

=======
from django.utils.translation import ugettext_lazy as _
>>>>>>> Stashed changes
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label=_('Quantity'))
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)