from django.db import models
from django.utils.text import slugify

class Shop(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    sender_email = models.EmailField(blank=True, null=True)
    legal_business_name = models.CharField(max_length=255, blank=True, null=True)
    country_region = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    apartment_suite = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    pin_code = models.CharField(max_length=10, blank=True, null=True)
    timezone = models.CharField(max_length=100, blank=True, null=True)
    unit_system = models.CharField(max_length=50, blank=True, null=True)
    weight_unit = models.CharField(max_length=50, blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True)
    order_prefix = models.CharField(max_length=10, blank=True, null=True)
    order_suffix = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Shop, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shops'  # Update the table name in the database

class Shop_Categories(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=255, unique=True)  # External ID for API calls
    total_products = models.IntegerField(default=0)
    image_id = models.CharField(max_length=255, unique=True, null=True, blank=True)  # External image ID for API calls
    shop_id = models.CharField(max_length=255, unique=True)  # Internal unique shop ID

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Shop_Categories, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_categories'  # Update the table name in the database

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    total_products = models.IntegerField(default=0)
    total_earnings = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    shop = models.ForeignKey(Shop_Categories, on_delete=models.SET_NULL, null=True, blank=True, related_name='categories')  # Temporarily allow nulls
    shop_category_id = models.CharField(max_length=255, null=True, blank=True)  # Temporarily allow nulls

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        db_table = 'ecommerce_categories'
        unique_together = ('shop', 'shop_category_id')

    def get_hierarchy(self):
        hierarchy = [self.name]
        parent = self.parent
        while parent:
            hierarchy.insert(0, parent.name)
            parent = parent.parent
        return ' -> '.join(hierarchy)
