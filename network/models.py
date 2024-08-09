from django.core.exceptions import ValidationError
from django.db import models


class ContactInfo(models.Model):
    """
    Модель для хранения контактной информации.
    """
    email = models.EmailField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.city}, {self.street}, {self.house_number}'


class Product(models.Model):
    """
    Модель для хранения информации о продукте.
    """
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return f'{self.name} ({self.model})'


class NetworkNode(models.Model):
    """
    Модель для хранения информации о звене сети.
    """
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=255)
    contact_info = models.ManyToManyField(
        ContactInfo, related_name='network_nodes', blank=True)
    products = models.ManyToManyField(
        Product, related_name='network_nodes', blank=True)
    supplier = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True,
        blank=True, related_name='supplied_nodes')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=0)

    def __str__(self):
        return self.name

    def clean(self):
        """
        Валидация модели перед сохранением.
        """
        if self.level == 0 and self.supplier is not None:
            raise ValidationError("Завод не может иметь поставщика.")
        if (self.level == 1 and self.supplier
                is not None and self.supplier.level != 0):
            raise ValidationError(
                "Розничная сеть может иметь"
                " только завод в качестве поставщика.")
        if (self.level == 2 and self.supplier
                is not None and self.supplier.level not in [0, 1]):
            raise ValidationError(
                "Индивидуальный предприниматель может иметь"
                " поставщикам либо завод, либо розничную сеть.")

    def save(self, *args, **kwargs):
        """
        Переопределение метода save для вызова валидации.
        """
        self.clean()
        super().save(*args, **kwargs)
