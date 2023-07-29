from rest_framework import serializers
from ..models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'barang_id', 'barang_name', 'tanggal', 'jumlah', 'harga']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
