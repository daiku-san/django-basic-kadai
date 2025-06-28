from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    
    # Productクラスの中に、__str__メソッドを定義することで、オブジェクトの文字列表現を返す
    def __str__(self):
        return self.name

    # 新規作成や編集後に、詳細ページにリダイレクトするためのURLを返す
    def get_absolute_url(self):
        return reverse('list')