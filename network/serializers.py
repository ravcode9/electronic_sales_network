from rest_framework import serializers
from .models import NetworkNode, Product, ContactInfo


class ContactInfoSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели ContactInfo.
    """
    class Meta:
        model = ContactInfo
        fields = ['email', 'country', 'city', 'street', 'house_number']


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'model', 'release_date']


class NetworkNodeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели NetworkNode.
    """
    contact_info = ContactInfoSerializer(many=True, read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    supplier = serializers.PrimaryKeyRelatedField(
        queryset=NetworkNode.objects.all(), required=False, allow_null=True)

    class Meta:
        model = NetworkNode
        fields = ['id', 'name', 'contact_info', 'products',
                  'supplier', 'debt', 'created_at', 'level']
        read_only_fields = ['debt', 'created_at']


class NetworkNodeUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления модели NetworkNode.
    """
    contact_info = serializers.PrimaryKeyRelatedField(
        queryset=ContactInfo.objects.all(), many=True, required=False)

    class Meta:
        model = NetworkNode
        fields = ['name', 'contact_info', 'products',
                  'supplier', 'level', 'debt',]
        read_only_fields = ['debt']
