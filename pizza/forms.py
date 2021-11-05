from django import forms
from .models import Pizza

# class PizzaForm(forms.Form):
#     SIZE_CHOICES = [('Large', 'Large'),
#                     ('Medium', 'Medium'),
#                     ('Small', 'Small')]
#     topping1 = forms.CharField(label='topping 1', max_length=200)
#     topping2 = forms.CharField(label='topping 2', max_length=200)
#     size = forms.ChoiceField(label='size', choices=SIZE_CHOICES)


class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}


class MultiplPizzaForm(forms.Form):
    size = forms.IntegerField(min_value=2, max_value=6)
    # class Meta:
    #     model = Pizza
