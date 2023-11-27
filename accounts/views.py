from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.forms import inlineformset_factory

# Create your views here.
from .models import Product
from .models import Customer
from .models import Order
from .forms import OrderForm
from .filters import OrderFilter


def home(request):
    #   return HttpResponse('Home Page')

    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = Order.objects.count()
    orders_delivered= Order.objects.filter(status = 'delivered').count()
    orders_pending = Order.objects.filter(status='Pending').count()

    context = {
                 "orders": orders,
                 "customers": customers,
                 "total_orders": total_orders,
                 "orders_delivered": orders_delivered, 
                 "orders_pending": orders_pending,
              }

    return render(request, "dashboard.html", context)


def contact(request):
    #    return HttpResponse('Contact Page')
    return render(request, 'contact.html')


def customers(request, pk_id):
    #    return HttpResponse('Customers Page')
    customer = Customer.objects.get(id=pk_id)
    orders = customer.order_set.all()

    #adding the filter
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
                "customer": customer,
                "orders": orders,
                "myFilter": myFilter,
              }

    return render(request, "customers.html", context)


def products(request):
    #    return HttpResponse('Products Page')
    products = Product.objects.all()

    # we will pass the products dataset to the
    # view. To pass this variable we use a dictionary
    # the key name we use here, will be the name we use
    # in the template to refer to the data
    return render(request, "products.html", {'products': products})

"""
    def createOrder(request):
        form = OrderForm()
        context = {'form': form}


        if request.method == 'POST':
            form = OrderForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('/')


        return render(request, 'order_form.html', context)
"""

def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=pk)
#   formSet = OrderFormSet(instance=customer)
    formSet = OrderFormSet(queryset=Order.objects.none(), instance=customer)
 
    #form = OrderForm(initial={"customer": customer,})
    context = {'formSet': formSet}


    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formSet = OrderFormSet(request.POST, instance=customer)

        if formSet.is_valid():
            formSet.save()
            return redirect('/')


    return render(request, 'order_form.html', context)


def updateOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context = {'form': form}

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')


    return render(request, 'order_form.html', context)



def deleteOrder (request, pk):

    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'order': order,}
    return render(request, 'delete_order.html', context)


def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
