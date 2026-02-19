from django.contrib import admin
from .models import Product, ProductColorImage ,WarrantyRegistration ,WarrantyApproval

# Register your models here.
class ProductColorImageInline(admin.TabularInline):
    model = ProductColorImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductColorImageInline]

admin.site.register(Product, ProductAdmin)

class WarrantyApprovalInline(admin.StackedInline):
    model = WarrantyApproval
    can_delete = False
    max_num = 1   # only one approval allowed


@admin.register(WarrantyRegistration)
class WarrantyRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_name', 'serial_number', 'submitted_at', 'is_verified')
    list_filter = ('is_verified',)
    inlines = [WarrantyApprovalInline]


@admin.register(WarrantyApproval)
class WarrantyApprovalAdmin(admin.ModelAdmin):
    list_display = ('registration', 'approved', 'approved_at')