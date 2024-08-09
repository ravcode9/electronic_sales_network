from django.contrib import admin
from .models import NetworkNode, Product, ContactInfo


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели ContactInfo.
    """
    list_display = ('email', 'country', 'city', 'street', 'house_number')
    search_fields = ('email', 'city')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели Product.
    """
    list_display = ('name', 'model', 'release_date')
    search_fields = ('name', 'model')


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели NetworkNode.
    """
    list_display = ('name', 'display_contact_info',
                    'debt', 'created_at', 'level', 'supplier_link')
    list_filter = ('contact_info__city', 'level')
    actions = ['clear_debt']

    def display_contact_info(self, obj):
        """
        Отображение контактной информации в виде строки.
        """
        return ', '.join([f'{info.email}, {info.city}, {info.street},'
                          f' {info.house_number}'
                          for info in obj.contact_info.all()])
    display_contact_info.short_description = 'Contact Info'

    def supplier_link(self, obj):
        """
        Создание ссылки на поставщика.
        """
        if obj.supplier:
            return (f'<a href="/admin/network/networknode/'
                    f'{obj.supplier.id}/">{obj.supplier.name}</a>')
        return "No Supplier"
    supplier_link.allow_tags = True
    supplier_link.short_description = 'Supplier'

    def clear_debt(self, request, queryset):
        """
        Очистка задолженности перед поставщиком.
        """
        queryset.update(debt=0)
    clear_debt.short_description = 'Очистить задолженность перед поставщиком'
