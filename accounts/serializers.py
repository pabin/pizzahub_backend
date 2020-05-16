from rest_framework import serializers
from datetime import timedelta
from django.utils import timezone

from inventory.serializers import ShoppingCartSerializer
from .models import *


class UserSerializer(serializers.ModelSerializer):
    valid_cart = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'valid_cart', 'username', 'user_image', 'address', 'contact', 'first_name', 'last_name', 'last_login']
        depth = 1

    def get_valid_cart(self, obj):
        time_now = timezone.now()
        valid_cart = obj.carts.filter(validity__gte=time_now, is_active=True)

        if valid_cart:
            return ShoppingCartSerializer(valid_cart[0]).data
        return None