from django.forms.formsets import formset_factory
from django.shortcuts import render
from .forms import PizzaForm, MultiplPizzaForm
from .models import Pizza


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_pizza_form = MultiplPizzaForm(request.POST)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            new_form = PizzaForm()
            message = f"Your {filled_form.cleaned_data['size']} pizza has been ordered successfully"
            return render(request, 'pizza/order.html', {'form': new_form, 'message': message, 'pizza_pk': created_pizza.pk, 'multiple_pizza_form': multiple_pizza_form})
        elif multiple_pizza_form.is_valid():
            return render(request, 'pizza/pizzas.html')
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form, 'multiple_pizza_form': multiple_pizza_form})


def pizzas(request):
    number_of_pizzas = 2
    multiple_pizza_form = MultiplPizzaForm(request.GET)
    if multiple_pizza_form.is_valid():
        number_of_pizzas = multiple_pizza_form.cleaned_data['size']
    MultipleForms = formset_factory(PizzaForm, extra=number_of_pizzas)
    form_set = MultipleForms()
    if request.method == 'POST':
        filled_form_set = MultipleForms(request.POST)
        if filled_form_set.is_valid():
            note = 'success'
            for form in filled_form_set:
                pizza = Pizza()
                pizza.topping1 = form.cleaned_data['topping1']
                pizza.topping2 = form.cleaned_data['topping2']
                pizza.size = form.cleaned_data['size']
                pizza.save()
        else:
            note = 'failed'
        return render(request, 'pizza/pizzas.html', {'formset': form_set, 'note': note})
    return render(request, 'pizza/pizzas.html', {'formset': form_set})


def edit(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    pizza_form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            note = 'Your pizza has been successfully updated'
        else:
            note = 'Sorry there\'s an error. Please try again :)'
        return render(request, 'pizza/edit_pizza.html', {'form': pizza_form, 'note': note})

    else:
        return render(request, 'pizza/edit_pizza.html', {'form': pizza_form})
