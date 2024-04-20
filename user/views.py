from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime
from django.db import connection

# Create your views here.
def home(request):
    ofdata=of_slider.objects.all().order_by('id')
    cdata=category.objects.all().order_by('-id')
    sdata=slider.objects.all().order_by('-id')
    pdata=mproduct.objects.all().order_by('-id')[0:8]
    opdata=mproduct.objects.all().filter(total_discount__gte=20).order_by('-id')[0:8]
    md={'cdata':cdata,'sdata':sdata,'pdata':pdata,'ofdata':ofdata,'opdata':opdata}
    return render(request,'user/index.html',md)
def about(request):
    fdata=faculty.objects.all().order_by('-id')[0:7]
    fd={'fdata':fdata}
    return render(request,'user/aboutus.html',fd)
def contact(request):
    if request.method=='POST':
        a=request.POST.get('name')
        e=request.POST.get('email')
        m1=request.POST.get('mob')
        m2=request.POST.get('message')
        x=contactus(name=a,email=e,mobile=m1,message=m2).save()
        return HttpResponse("<script>alert('Thanks you for contact');location.href='/user/contact'</script>")
    return render(request,'user/contactus.html')
def signup(request):
    if request.method=='POST':
        sname=request.POST.get('name')
        semail=request.POST.get('email')
        smobile=request.POST.get('mob')
        spassword=request.POST.get('pass')
        saddress=request.POST.get('address')
        profile=request.FILES['spic']
        x=register.objects.all().filter(semail=semail).count()
        if x==1:
            return HttpResponse("<script>alert('you are already registerd');location.href='/user/signup/'</script>")
        else:
            register(sname=sname,semail=semail,smobile=smobile,spassword=spassword,saddress=saddress,profile=profile).save()
            return HttpResponse("<script>alert('you are registerd successfully');location.href='/user/signup/'</script>")
           
    return render(request,'user/signup.html')
def signin(request):
    if request.method=='POST':
        semail=request.POST.get('email')
        spassword=request.POST.get("passwd")
        x=register.objects.all().filter(semail=semail,spassword=spassword).count()
        if x==1:
            y=register.objects.all().filter(semail=semail,spassword=spassword)
            request.session['user']=semail
            request.session['userpic']=str(y[0].profile)
            request.session['username']=str(y[0].sname)
            return HttpResponse("<script>alert('Login successful');location.href='/user/home/'</script>")
        else:
            return HttpResponse("<script>alert('Your username or password is incorrect');location.href='/user/signin/'</script>")
    return render(request,'user/signin.html')
def product(request):
    subdata=subcategory.objects.all().order_by('-id')
    scatid=request.GET.get('pid')
    catid=request.GET.get('cid')
    ofid=request.GET.get('oid')
    if scatid is not None:
        pdata=mproduct.objects.all().filter(psubcategory=scatid).order_by('-id')
    elif catid is not None:
        pdata=mproduct.objects.all().filter(pcategory=catid)
    else:
        pdata=mproduct.objects.all().order_by('id').order_by('-id')
    pd={"subdata":subdata,"pdata":pdata}
    return render(request,'user/product.html',pd)
def signout(request):
    if request.session.get('user'):
        del request.session['user']
        del request.session['userpic']
        return HttpResponse("<script>location.href='/user/home/'</script>")
    return render (request,'user/signout.html')
def myprofile(request):
    user=request.session.get('user')
    if request.method=='POST':
        sname=request.POST.get('name')
        smobile=request.POST.get('mobile')
        spassword=request.POST.get('pass')
        saddress=request.POST.get('address')
        pic=request.FILES['fu']
        register(sname=sname,semail=user,smobile=smobile,spassword=spassword,saddress=saddress,profile=pic).save()
        return HttpResponse("<script>alert('your profile is updated successful');location.href='/user/myprofile/'</script>")
    rdata=""
    if user:
        rdata=register.objects.all().filter(semail=user)
    md={"rdata":rdata}
    return render (request,'user/myprofile.html',md)
def mycart(request):
    user=request.session.get('user')
    if user:
        qt=int(request.GET.get('qt'))
        pname=request.GET.get('pname')
        ppic=request.GET.get('ppic')
        pw=request.GET.get('pw')
        price=int(request.GET.get('price'))
        total_price=qt*price
        if qt>0:
            cart(userid=user,product_name=pname,quantity=qt,price=price,total_price=total_price,product_picture=ppic,pw=pw,added_date=datetime.now().date()).save()
            cartitems=cart.objects.filter(userid=user).count()
            request.session['cartitems']=cartitems
            return HttpResponse("<script>alert('your item is added in cart');location.href='/user/cartitems/'</script>")
        else:
            return HttpResponse("<script>alert('Please increase your cart items');location.href='/user/product/'</script>")
    return render(request,'user/mycart.html')
def indexcart(request):
    user=request.session.get('user')
    if user:
        qt=int(request.GET.get('qt'))
        pname=request.GET.get('pname')
        ppic=request.GET.get('ppic')
        pw=request.GET.get('pw')
        price=int(request.GET.get('price'))
        total_price=qt*price
        if qt>0:
            cart(userid=user,product_name=pname,quantity=qt,price=price,total_price=total_price,product_picture=ppic,pw=pw,added_date=datetime.now().date()).save()
            cartitems=cart.objects.filter(userid=user).count()
            request.session['cartitems']=cartitems
            return HttpResponse("<script>alert('your item is added in cart');location.href='/user/cartitems/'</script>")
        else:
            return HttpResponse("<script>alert('Please increase your cart items');location.href='/user/home/'</script>")
    return render(request,'user/indexcart.html')
def cartitems(request):
    user=request.session.get('user')
    cid=request.GET.get('cid')
    cartdata=""
    if user:
        cartdata=cart.objects.filter(userid=user)
        if cid is not None:
            cart.objects.filter(id=cid).delete()
            cartitems=cart.objects.filter(userid=user).count()
            request.session['cartitems']=cartitems
            return HttpResponse("<script>alert('your card items is remove successfully');location.href='/user/cartitems/'</script>")
    cd={"cartdata":cartdata}
    return render(request,'user/cartitems.html',cd)
def myorders(request):
    user=request.session.get('user')
    msg=request.GET.get('msg')
    if msg is not None:
        cursor=connection.cursor()
        cursor.execute("insert into user_myorder(product_name,quantity,price,total_price,product_picture,pw,userid,status,order_date) select product_name,quantity,price,total_price,product_picture,pw,'"+str(user)+"','pending','"+str(datetime.now().date())+"' from user_cart where userid='"+str(user)+"'")
        cart.objects.filter(userid=user).delete()
        cartitems=cart.objects.filter(userid=user).count()
        request.session['cartitems']=cartitems
        return HttpResponse("<script>alert('your order has placed successful');location.href='/user/orderitem/'</script>")
    return render(request,'user/order.html')
def orderitems(request):
    oid=request.GET.get('oid')
    user=request.session.get('user')
    pdata=myorder.objects.filter(userid=user,status="pending")
    adata=myorder.objects.filter(userid=user,status="accepted")
    ddata=myorder.objects.filter(userid=user,status="deliverd")
    if oid is not None:
        myorder.objects.filter(id=oid)
        myorder.objects.filter(userid=user).delete()
        return HttpResponse("<script>alert('your order is cancel successfully');location.href='/user/orderitem/'</script>")
    od={"pdata":pdata,"adata":adata,"ddata":ddata}
    return render(request,'user/orderitem.html',od)