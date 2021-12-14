from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null = True)
    address = models.CharField(max_length=400, null = True)
    email = models.CharField(max_length=200, null = True)
    date_created = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return self.name

##

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

##

class Product(models.Model):
    CATEGORY = (
                ('Sadan', 'Sadan'),
                ('SUV', 'SUV'),
                )
    name = models.CharField(max_length=200)
    price = models.FloatField(null = True)
    category = models.CharField(max_length=200, null = True, choices = CATEGORY)
    description = models.CharField(max_length=200, null = True, blank = True)
    date_created =  models.DateTimeField(auto_now_add= True)
    tags = models.ManyToManyField(Tag)
    link= models.CharField(max_length=200, null = True, blank = True)

    def __str__(self):
        return self.name

##

class Order(models.Model):
    STATUS = (
                ('Unavailable' , 'Unavailable'),
                ('On Test Drive', 'On Test Drive'),
                ('Delivered', 'Delivered'),
             )
    customer = models.ForeignKey(Customer, null = True , on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, null = True , on_delete = models.SET_NULL)
    date_created =  models.DateTimeField(auto_now_add= True)
    status = models.CharField(max_length = 200, null = True, choices = STATUS)
    note = models.CharField(max_length = 1000, null = True)

    def __str__(self):
        return self.product.name
