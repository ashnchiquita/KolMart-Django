from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    REQUIRED_FIELDS = [username, email, password]

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barang_id = models.CharField(max_length=255)
    barang_name = models.CharField(max_length=255)
    tanggal = models.DateField(auto_now_add=True)
    jumlah = models.IntegerField()
    harga = models.IntegerField()

    REQUIRED_FIELDS = [user, barang_id, barang_name, tanggal, jumlah, harga]
