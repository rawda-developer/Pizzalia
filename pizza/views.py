from django.shortcuts import render
from .forms import PizzaForm


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            message = f"Your {filled_form.cleaned_data['size']} pizza has been ordered successfully"
        else:
            message = "Sorry there's an error in the order. Please try again :)"
        new_form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': new_form, 'message': message})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'form': form})
