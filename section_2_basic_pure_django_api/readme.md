# Section 2. Web APIs

> 기본 장고를 활용하여 웹 API 만들기

- [Github repo](https://github.com/pymike00/The-Complete-Guide-To-DRF-and-VueJS/tree/master/02-WEB-APIs/First_API_Django/onlinestore)
## 배운점

- models.py
```python
from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,
                                     on_delete=models.CASCADE,
                                     related_name="products")
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField()
    shipping_cost = models.FloatField()
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
```

-  views.py
```python
from django.http import JsonResponse
from .models import Manufacturer, Product


def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())}  # .values("pk", "name")
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        response = JsonResponse(
            {"error": {"code": 404, "message": "product not found!"}}, status=404
        )
    else:
        data = {
            "product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name,
                "description": product.description,
                "photo": product.photo.url,
                "price": product.price,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity,
            }
        }
        response = JsonResponse(data)
    return response


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.filter(active=True)
    data = {"manufacturers": list(manufacturers.values())}
    response = JsonResponse(data)
    return response


def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
    except Manufacturer.DoesNotExist:
        response = JsonResponse(
            {"error": {"code": 404, "message": "manufacturer not found!"}}, status=404
        )
    else:
        manufacturer_products = manufacturer.products.all()
        data = {
            "manufacturer": {
                "name": manufacturer.name,
                "location": manufacturer.location,
                "active": manufacturer.active,
                "products": list(manufacturer_products.values()),
            }
        }
        response = JsonResponse(data)
    return response
```



- `values()` 메소드를 이용하여 쿼리셋을 일일이 들여다 볼 필요가 없다.

- related_name을 이용하여 ForeignKey로 연결된 테이블에서 역방향으로 바로 조회가 가능하다.
    - 일대다 : Manufacturer - Product(ForeignKey-manufacturer)
    - `manufacturer.products.all()`

