from django.shortcuts import render,redirect
from cart.models import Cart,Account,Order
from shop.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_to_cart(request,p):
    product=Product.objects.get(pname=p)
    user=request.user
    try:
        cart=Cart.objects.get(user=user,product=product)
        if(cart.quantity<cart.product.stock):
            cart.quantity+=1
            cart.save()
    except Cart.DoesNotExist:
        cart=Cart.objects.create(product=product,user=user,quantity=1)
        cart.save()
    return redirect('cart:cart_view')

def cart_view(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    total=0
    for i in cart:
        total+=(i.quantity * i.product.price)
    return render(request,'cartview.html',{'cart':cart,'total':total})

def cart_remove(request,p):
    product=Product.objects.get(pname=p)
    user=request.user
    try:
        cart=Cart.objects.get(user=user,product=product)
        if(cart.quantity>1):
            cart.quantity-=1
            cart.save()

        else:
            cart.delete()

    except:
        pass
    return redirect('cart:cart_view')




def full_remove(request,p):
    product=Product.objects.get(pname=p)
    user=request.user
    try:
        cart=Cart.objects.get(user=user, product=product)
        cart.delete()

    except:
        pass
    return redirect('cart:cart_view')


@login_required
def order_form(request):
    if(request.method=="POST"):
        a=request.POST['a']
        ph=request.POST['ph']
        an=request.POST['an']
        user=request.user
        cart=Cart.objects.filter(user=user)
        total=0
        for i in cart:
            total+=i.quantity*i.product.price

        acct=Account.objects.get(acctnumber=an)
        if(acct.balance>total):
            acct.balance=acct.balance-total
            acct.save()

            for i in cart:
                o=Order.objects.create(user=user,product=i.product,phone=ph,address=a,noofitems=i.quantity,order_status="paid")
                o.save()

                i.product.stock=i.product.stock-i.quantity
                i.product.save()
            cart.delete()
            msg="Order Placed Successfully"
            return render(request,'orderconfirm.html',{'msg':msg})
        else:
            msg="Unable to place order due to Insufficient Account Balance"
            return render(request,'orderconfirm.html',{'msg':msg})

    return render(request,'orderform.html')


@login_required
def your_orders(request):
    user=request.user
    order=Order.objects.filter(user=user)
    for i in order:
        username=i.user.username

    return render(request,'yourorders.html',{'order':order,'username':username})