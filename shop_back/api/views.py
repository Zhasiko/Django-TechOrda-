from django.http.response import JsonResponse

from . import models

def get_products(request):
    products = models.Product.objects.all()
    product_names = [{'name': p.name} for p in products]

    return JsonResponse(product_names, safe=False)

def get_product(request, *args, **kwargs):
    product = models.Product.objects.get(id=int(kwargs['id']))
    product_info = {
        'id': product.id,
        'name': product.name,
        'amount': product.amount,
    }

    return JsonResponse(product_info, safe=False)

def get_categories(request):
    categories = models.Category.objects.all()
    category_names = [{'name': c.name} for c in categories]

    return JsonResponse(category_names, safe=False)

def get_category(request, *args, **kwargs):
    category = models.Category.objects.get(id=int(kwargs['id']))
    category_info = {
        'id' : category.id,
        'name': category.name,
    }

    return JsonResponse(category_info, safe=False)

def get_products_of_category(request, *args, **kwargs):
    category = models.Category.objects.get(id=int(kwargs['id']))
    products = category.products.all()
    product_names = [{'name': p.name,
                      'amount': p.amount} for p in products]
    category_products = {
        'id': category.id,
        'name': category.name,
        'products': product_names,
    }
    return JsonResponse(category_products, safe=False)