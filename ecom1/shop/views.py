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
    banner = Product.objects.filter(banner2=True)
    trending = Product.objects.filter(trending=True)


    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'product':product,
        'banner':banner,
        'trending':trending
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
    categories = Category.objects.all()
    product = Product.objects.all()
    products = Product.objects.all()
    if query is not None:
        products = products.filter(
            Q(category__name__icontains=query) |
            Q(name__icontains=query) |
            Q(price__icontains=query) 
    

        )
   
    context = {

        'query':query,
        'products': products,
        'product': product,
        'categories': categories,

     
    }

    return render(request, 'shop/product/list.html', context)