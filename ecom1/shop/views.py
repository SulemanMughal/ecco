from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from cart.forms import CartAddProductForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from .forms import *
from django.db.models import Q

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    product = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'product':product,
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)



def home(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    product = Product.objects.all()
    banner = Product.objects.filter(banner2=True)[0:3]
    banner1 = Product.objects.filter(banner1=True)[0]
    hot_item = Product.objects.filter(hot_item=True)
    on_sale = Product.objects.filter(on_sale=True)


    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'product':product,
        'banner':banner,
        'banner1':banner1,
        'hot_item':hot_item,
        'on_sale':on_sale
    }
    return render(request, 'shop/product/home.html', context)



def contact(request):
    form=contactForm()
    if request.method=='POST':
        current_site = get_current_site(request)
        form=contactForm(request.POST, request.FILES)
        if form.is_valid():
            message = render_to_string('shop/product/email.html', {
                'user':request.POST['Name'], 'domain':current_site.domain,
                'email':request.POST['Email'],'subject':request.POST['Subject'],
                'message':request.POST['Message']
            ,
            })
            mail_subject = 'You have got a contact'
            to_email = 'dawarsardar786@gmail.com'
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            form.save()
            return redirect('shop:product_list')
    context = {
        'form':form,
    }
    return render(request,'shop/product/contact.html',context)


def search(request):

    query = request.GET.get('query', None)
    query1 = request.GET.get('query1', None)
    result = (query1.split('-'))
    value1 =(result[0][1:])
    value2 =(result[1][2:])

    query2 = request.GET.get('query2', None)
    if query2== 'on':
        query2=True
    else:
        query2=False
    print(query2)
    categories = Category.objects.all()
    product = Product.objects.all()
    products = Product.objects.all()
    if query is not None:
        products = products.filter(
            Q(category__name__icontains=query) |
            Q(name__icontains=query) |
            Q(price__icontains=query) 
    

        )
    if query1 is not None:
        products = products.filter(
            Q(price__gte=value1) &
            Q(price__lte=value2) &
            Q(fast_available__exact=query2) 
            
    

        )
    context = {

        'query':query,
        'products': products,
        'product': product,
        'categories': categories,

     
    }

    return render(request, 'shop/product/list.html', context)