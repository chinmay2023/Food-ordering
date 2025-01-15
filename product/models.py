from django.db import models
import uuid
# Create your models here.

#   DRY => Dot NOT repeat yourself


class BaseModel(models.Model):
      uid = models.Model (default = uuid.uuid4, editable = False, primary_key = True)   
      created_at = models.DateField(auto_created= True)
      update_at = models.DateField(auto_created= True)

      class Meta:
          abstract = True

class Product(models.Model):
  product_name = models.CharField(max_length=100)
  product_slug = models.SlugField(unique= True)
  product_description = models.TextField()
  product_price = models.IntegerField(default=0)
  product_demo_price = models.IntegerField(default=0)
  quantity = models.CharField(null=True , blank= True)


class ProductMetaInformation(BaseModel):
    product = models.OneToOneField(Product, on_delete= models.CASCADE)
    quantity = models.CharField(null=True , blank= True)
    product_measuring = models.CharField(max_length= 100 , choices=(("KG", "KG"), ("ML", "ML") , ("L" , "L")))
     
   


class ProductImages(models.Model):
     product_images = models.ImageField(upload_to="product")
 
