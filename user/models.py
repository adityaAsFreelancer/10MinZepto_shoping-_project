from django.db import models

# Create your models here.
class category(models.Model):
    cname=models.CharField(max_length=200,null=True)
    cpic=models.ImageField(upload_to='static/category',null=True)
    cdate=models.DateField(max_length=30,null=True)
    def __str__(self):
        return self.cname
class slider(models.Model):
    spic=models.ImageField(upload_to='static/slider',null=True)
    sdate=models.DateField(null=True)
class subcategory(models.Model):
    category_name=models.ForeignKey(category,on_delete=models.CASCADE)
    subcategory_name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.subcategory_name
class mproduct(models.Model):
    pcategory=models.ForeignKey(category,on_delete=models.CASCADE)
    psubcategory=models.ForeignKey(subcategory,on_delete=models.CASCADE)
    price=models.IntegerField(null=True)
    ppic=models.ImageField(upload_to='static/myproduct',null=True)
    total_discount=models.IntegerField(null=True)
    product_quantity=models.CharField(max_length=200,null=True)
    discount_price=models.IntegerField(null=True)
    pdate=models.DateField(null=True)
class register(models.Model):
    sname=models.CharField(max_length=200,null=True)
    semail=models.CharField(max_length=200,primary_key=True)
    smobile=models.IntegerField(null=True)
    spassword=models.CharField(max_length=200,null=True)
    profile=models.ImageField(upload_to='static/register',null=True)
    saddress=models.TextField()
    def __str__(self):
        return self.sname
class contactus(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=150,null=True)
    mobile=models.IntegerField(null=True)
    message=models.TextField(null=True)
    def __str__(self):
        return self.name
class faculty(models.Model):
    fname=models.CharField(max_length=200,null=True)
    fpic=models.ImageField(upload_to='static/faculty',null=True)
    finformation=models.TextField(null=True)
    def __str__(self):
        return self.fname
class of_slider(models.Model):
    of_pic=models.ImageField(upload_to='static/offer_pic',null=True)
    of_date=models.DateField(null=True)
class cart(models.Model):
    userid=models.CharField(max_length=200,null=True)
    product_name=models.CharField(max_length=200,null=True)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    total_price=models.FloatField(null=True)
    product_picture=models.CharField(max_length=300,null=True)
    pw=models.CharField(max_length=200,null=True)
    added_date=models.DateField()
class myorder(models.Model):
    userid=models.CharField(max_length=200,null=True)
    product_name=models.CharField(max_length=200,null=True)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    total_price=models.FloatField(null=True)
    product_picture=models.CharField(max_length=300,null=True)
    pw=models.CharField(max_length=200,null=True)
    order_date=models.DateField(null=True)
    status=models.CharField(max_length=200,null=True)

