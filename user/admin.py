from django.contrib import admin
from .models import *

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display=('id','cname','cpic','cdate')
admin.site.register(category,categoryAdmin)
class sliderAdmin(admin.ModelAdmin):
    list_display=('id','spic','sdate')
admin.site.register(slider,sliderAdmin)
class subcategoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name','subcategory_name')
admin.site.register(subcategory,subcategoryAdmin)
class mproductAdmin(admin.ModelAdmin):
    list_display=('id','pcategory','psubcategory','ppic','price','total_discount','discount_price','pdate','product_quantity')
admin.site.register(mproduct,mproductAdmin)
class registerAdmin(admin.ModelAdmin):
    list_display=('sname','semail','smobile','profile','spassword','saddress')
admin.site.register(register,registerAdmin)
class contactusAdmin(admin.ModelAdmin):
    list_display=('id','name','email','mobile','message')
admin.site.register(contactus,contactusAdmin)
class facultyAdmin(admin.ModelAdmin):
    list_display=('id','fname','fpic','finformation')
admin.site.register(faculty,facultyAdmin)
class of_sliderAdmin(admin.ModelAdmin):
    list_display=('id','of_pic','of_date')
admin.site.register(of_slider,of_sliderAdmin)
class cartAdmin(admin.ModelAdmin):
    list_display=('id','userid','product_name','quantity','price','total_price','product_picture','pw','added_date')
admin.site.register(cart,cartAdmin)
class myorderAdmin(admin.ModelAdmin):
    list_display=('id','userid','product_name','quantity','price','total_price','product_picture','pw','order_date','status')
admin.site.register(myorder,myorderAdmin)
    