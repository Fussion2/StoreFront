from django.db import models

# Create your models here.

class Promotion(models.Model):
    description=models.CharField(max_length=225)
    discount=models.FloatField()
    



class Collection(models.Model):
    title=models.CharField(max_length=250)
    featured_product=models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')

class Product(models.Model):
    title=models.CharField( max_length=225)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions=models.ManyToManyField(Promotion)
    
    
class Customer(models.Model):
    membership_bronze='B'
    membership_silver='S'
    membership_gold='G'
    
    membership_choices=[
        (membership_bronze,'Bronze'),
        (membership_silver,'Silver'),
        (membership_gold,'Gold'),
    ]
     
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=224)
    birth_date=models.DateField(null=True)
    membership=models.CharField(choices=membership_choices, max_length=1, default=membership_bronze)

# class meta:
#     db_table='store_customer'
#     Indexe=[
#         models.Index(fields=['lastname','firstname'])
#     ]    
    
class Order(models.Model):
    paymentstatus_pending='P'
    payementstatus_failed='F'
    paymentstatus_complete='C'
    
    payment_choices=[
        (paymentstatus_pending,'Pending'),
        (payementstatus_failed,'Failed'),
        (paymentstatus_complete,'Complete'),
    ]
    
    Placed_At=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1,choices=payment_choices,default=paymentstatus_pending)
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)
    
    
    
class Order_item(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)
    
    
    
class Address(models.Model):
    street=models.CharField(max_length=225)
    city=models.CharField(max_length=225)
    # cascade ius used to delete customer add if customer is deleted
    # customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
    # one to many relation if customer have mutiple add
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    

class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    
class Cart_item(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    #  it keeps the value positive
    quantity=models.PositiveSmallIntegerField() 