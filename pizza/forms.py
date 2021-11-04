from django import forms


class PizzaForm(forms.Form):
    SIZE_CHOICES = [('Large', 'Large'),
                    ('Medium', 'Medium'),
                    ('Small', 'Small')]
    topping1 = forms.CharField(label='topping 1', max_length=200)
    topping2 = forms.CharField(label='topping 2', max_length=200)
    size = forms.ChoiceField(label='size', choices=SIZE_CHOICES)
