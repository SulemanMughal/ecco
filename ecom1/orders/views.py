from django.shortcuts import render,redirect
from .models import *
from .forms import OrderCreateForm
from cart.cart import Cart
from django.conf import settings

########################### STRIPE #############################

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

############################# BRAINTREE #############################
import braintree
braintree.Configuration.configure(braintree.Environment.Sandbox,
 merchant_id=settings.BRAINTREE_MERCHANT_ID,
 public_key=settings.BRAINTREE_PUBLIC_KEY,
 private_key=settings.BRAINTREE_PRIVATE_KEY)




#####################################################################


def order_create(request):
    key=settings.STRIPE_PUBLISHABLE_KEY
    cart = Cart(request)
    print(cart.get_total_price())
    order=None
    if request.method == 'POST':
     
        form = OrderCreateForm(request.POST)
        if form.is_valid():
          
  
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                   
                )
            cart.clear()
        #     charge = stripe.Charge.create(
        #     amount=int(cart.get_total_price())*100,
        #     currency='usd',
        #     description=('Payment for Order id {} '.format(order.id)),
        #     source=request.POST['stripeToken']
        # )
            
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form,'key':key})

def charge(request,id,slug): # new
    idorder=Order.objects.get(id=id)
    key=settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
    
        charge = stripe.Charge.create(
            amount=slug,
            currency='usd',
            description=(idorder.first_name + idorder.last_name),
            source=request.POST['stripeToken']
        )
        return render(request, 'orders/order/created.html', {'order': idorder,})

    return render(request, 'charge.html',{'key':key,'order': idorder,'total':slug})

################### paypal ##########################
# from django.urls import reverse
# def view_that_asks_for_money(request):

#     # What you want the button to do.
#     paypal_dict = {
#         "business": "receiver_email@example.com",
#         "amount": "10000000.00",
#         "item_name": "name of the item",
#         "invoice": "unique-invoice-id",
#         # "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
#         # "return": request.build_absolute_uri(reverse('your-return-view')),
#         # "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
#         "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
#     }

#     # Create the instance.
#     form = PayPalPaymentsForm(initial=paypal_dict)
#     context = {"form": form}
#     return render(request, "payment.html", context)

########################### Braintree ###########################################

# def checkout_page(request):
#     #generate all other required data that you may need on the #checkout page and add them to context.

#     # if settings.BRAINTREE_PRODUCTION:
#     #     braintree_env = braintree.Environment.Production
#     # else:
#     braintree_env = braintree.Environment.Sandbox

#     # Configure Braintree
#     braintree.Configuration.configure(
#         braintree_env,
#         merchant_id=settings.BRAINTREE_MERCHANT_ID,
#         public_key=settings.BRAINTREE_PUBLIC_KEY,
#         private_key=settings.BRAINTREE_PRIVATE_KEY,
#     )
 
#     try:
#         braintree_client_token = braintree.ClientToken.generate({ "customer_id": user.id })
#     except:
#         braintree_client_token = braintree.ClientToken.generate({})

#     context = {'braintree_client_token': braintree_client_token}
#     return render(request, 'checkout.html', context)


# def payment(request):
#     nonce_from_the_client = request.POST['paymentMethodNonce']
#     customer_kwargs = {
#         "first_name": request.user.first_name,
#         "last_name": request.user.last_name,
#         "email": request.user.email,
#     }
#     customer_create = braintree.Customer.create(customer_kwargs)
#     customer_id = customer_create.customer.id
#     result = braintree.Transaction.sale({
#         "amount": "10.00",
#         "payment_method_nonce": nonce_from_the_client,
#         "options": {
#             "submit_for_settlement": True
#         }
#     })
#     print(result)
#     return HttpResponse('Ok')



################### paypal ##########################
# from django.urls import reverse
# def view_that_asks_for_money(request):

#     # What you want the button to do.
#     paypal_dict = {
#         "business": "receiver_email@example.com",
#         "amount": "10000000.00",
#         "item_name": "name of the item",
#         "invoice": "unique-invoice-id",
#         # "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
#         # "return": request.build_absolute_uri(reverse('your-return-view')),
#         # "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
#         "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
#     }

#     # Create the instance.
#     form = PayPalPaymentsForm(initial=paypal_dict)
#     context = {"form": form}
#     return render(request, "payment.html", context)

########################### Braintree ###########################################

# def checkout_page(request):
#     #generate all other required data that you may need on the #checkout page and add them to context.

#     # if settings.BRAINTREE_PRODUCTION:
#     #     braintree_env = braintree.Environment.Production
#     # else:
#     braintree_env = braintree.Environment.Sandbox

#     # Configure Braintree
#     braintree.Configuration.configure(
#         braintree_env,
#         merchant_id=settings.BRAINTREE_MERCHANT_ID,
#         public_key=settings.BRAINTREE_PUBLIC_KEY,
#         private_key=settings.BRAINTREE_PRIVATE_KEY,
#     )
 
#     try:
#         braintree_client_token = braintree.ClientToken.generate({ "customer_id": user.id })
#     except:
#         braintree_client_token = braintree.ClientToken.generate({})

#     context = {'braintree_client_token': braintree_client_token}
#     return render(request, 'checkout.html', context)


# def payment(request):
#     nonce_from_the_client = request.POST['paymentMethodNonce']
#     customer_kwargs = {
#         "first_name": request.user.first_name,
#         "last_name": request.user.last_name,
#         "email": request.user.email,
#     }
#     customer_create = braintree.Customer.create(customer_kwargs)
#     customer_id = customer_create.customer.id
#     result = braintree.Transaction.sale({
#         "amount": "10.00",
#         "payment_method_nonce": nonce_from_the_client,
#         "options": {
#             "submit_for_settlement": True
#         }
#     })
#     print(result)
#     return HttpResponse('Ok')


