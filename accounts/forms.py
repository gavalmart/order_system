from django.forms import ModelForm

#now add the model from the app that will be used to bring the data
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        