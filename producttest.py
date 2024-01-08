"""from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from django.views.generic.list import ListView

from products.models import Product, ProductCategory
from django.core.cache import cache


class ProductsListViewTests(TestCase, ListView):
    def setUp(self):
        self.category = ProductCategory.objects.create(name='Test Category')
        # Создание временного изображения для использования в тесте
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        self.product = Product.objects.create(name='Test Product', category=self.category, image=image, price=10.00)

    def test_products_list_view(self):
        # Проверка основного представления списка продуктов
        response = self.client.get(reverse('products:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertContains(response, 'U-STYLE CATALOG')
        self.assertIn('categories', response.context)
        self.assertEqual(len(response.context['categories']), 1)  # Проверка наличия категорий в контексте

    def test_filtered_products_list_view(self):
        # Проверка фильтрации по категориям
        url = reverse('products:index', kwargs={'category_id': self.category.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Добавьте утверждения для проверки, что продукты в ответе принадлежат указанной категории
        # Например, проверьте, что все продукты имеют category_id равный self.category.id

    def test_caching_categories(self):
        # Проверка кэширования категорий
        response = self.client.get(reverse('products:index'))
        self.assertEqual(response.status_code, 200)
        categories_in_context = response.context['categories']
        cached_categories = cache.get('categories')
        self.assertIsNotNone(categories_in_context)
        self.assertEqual(categories_in_context.count(), ProductCategory.objects.count())
        self.assertEqual(categories_in_context.count(), cached_categories.count())

    # def test_no_category_filter(self):
    #     # Проверка, что при отсутствии указания категории, возвращается весь список продуктов
    #     response = self.client.get(reverse('products:index'))
    #     products_count = Product.objects.count()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.context['categories']), products_count)

    # def test_empty_categories_cache(self):
    #     # Проверка наличия категорий в кэше при его очистке или первом запросе
    #     cache.clear()  # Очистить кэш перед тестом
    #     response = self.client.get(reverse('products:index'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('categories', response.context)
    #     self.assertEqual(len(response.context['categories']), ProductCategory.objects.count())
    #     cached_categories = cache.get('categories')
    #     self.assertIsNotNone(cached_categories)
    #     self.assertEqual(cached_categories.count(), ProductCategory.objects.count())

    # def test_pagination(self):
    #     # Проверка разбиения списка продуктов на страницы
    #     response = self.client.get(reverse('products:index'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'])
    #     self.assertTrue('paginator' in response.context)
    #     self.assertTrue('page_obj' in response.context)
    #
    # def test_invalid_category_filter(self):
    #     # Проверка обработки случая с недопустимым ID категории
    #     invalid_category_id = 9999
    #     url = reverse('products:index', kwargs={'category_id': invalid_category_id})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.context['object_list']), 0)  # Проверка, что возвращается пустой список

    # Добавьте больше тестовых методов для покрытия других кейсов использования
"""

# from django.test import TestCase
# from django.urls import reverse
# from .models import Product, ProductCategory
# from django.core.cache import cache
#
# class ProductsListViewTest(TestCase):
#
#     def setUp(self):
#         self.category = ProductCategory.objects.create(name='Test Category')
#         # Создаем продукты с изображениями
#         self.product1 = Product.objects.create(name='Product 1', category=self.category, price=10.0,
#                                                image='path/to/image1.jpg')
#         self.product2 = Product.objects.create(name='Product 2', category=self.category, price=15.0,
#                                                image='path/to/image2.jpg')
#         # Создаем продукты без изображений
#         self.product3 = Product.objects.create(name='Product 3', category=self.category, price=20.0)
#         self.product4 = Product.objects.create(name='Product 4', category=self.category, price=25.0)
#
#
#     def test_get_queryset_without_category_id(self):
#         response = self.client.get(reverse('products:index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertQuerysetEqual(response.context['object_list'], [repr(self.product1), repr(self.product2)])
#
#     def test_get_queryset_with_category_id(self):
#         response = self.client.get(reverse('products:category', kwargs={'category_id': self.category.id}))
#         self.assertEqual(response.status_code, 200)
#         self.assertQuerysetEqual(response.context['object_list'], [repr(self.product1), repr(self.product2)])
#
#     def test_get_context_data_categories_cached(self):
#         cache.set('categories', [self.category])
#         response = self.client.get(reverse('products:index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.context['categories']), 1)
#
#     def test_get_context_data_categories_not_cached(self):
#         response = self.client.get(reverse('products:index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.context['categories']), 1)
#
#     def test_product_image_exists(self):
#         # Получаем продукты, у которых есть изображения
#         products_with_images = Product.objects.exclude(image='')
#         for product in products_with_images:
#             # Проверяем, что изображение существует
#             if product.image and hasattr(product.image, 'url'):
#                 self.assertTrue(product.image.url != '')
#             else:
#                 # Обработка случая, когда изображение отсутствует
#                 self.fail(f"Product '{product.name}' has no associated image.")

# Создаёт категорию и продукты для проверки

"""from django.urls import reverse
from django.test import TestCase
from products.models import Product, ProductCategory


class ProductsFilterTest(TestCase):
    def setUp(self):
        # Создаем категории
        accessories_category = ProductCategory.objects.create(
            id=4,
            name='Accessories',
            description='Accessories description'
        )
        # Создаем продукты, принадлежащие категории Accessories
        Product.objects.create(
            id=24,
            name='Брелок символ СФУ',
            image='products.images/1_idtdwrP.png',
            price=100,
            quantity=16,
            category=accessories_category
        )
        Product.objects.create(
            id=25,
            name='Брелок символ СФУ_2',
            image='products.images/2_0SdVerR.png',
            price=100,
            quantity=41,
            category=accessories_category
        )
        # Создаем продукт, не принадлежащий категории Accessories
        Product.objects.create(
            id=26,
            name='Брелок символ СФУ',
            image='products.images/3_X3W0qhO.png',
            price=150,
            quantity=11,
            category=accessories_category
        )
        Product.objects.create(
            id=27,
            name='Брелок символ СФУ',
            image='products.images/4_GaGVvzz.png',
            price=110,
            quantity=15,
            category=accessories_category
        )

    def test_accessories_category_filter(self):
        # Переходим на страницу с продуктами
        response = self.client.get(reverse('products:index'))
        self.assertEqual(response.status_code, 200)

        # Фильтруем по категории Accessories
        response = self.client.get(
            reverse('products:category', kwargs={'category_id': 4}))  # Используйте нужный ID категории
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,
                            'Брелок символ СФУ')  # Проверяем, что продукты из категории отображаются на странице"""


# import requests
# import unittest
#
#
# class TestProductFilters(unittest.TestCase):
#
#     def test_filter_by_gifts_category(self):
#         category_id = 4
#         requests.get('http://127.0.0.1:8000')
#         requests.get('http://127.0.0.1:8000/products/')
#         response = requests.get(f'http://127.0.0.1:8000/products/category/{category_id}/')
#         response.raise_for_status()  # Проверяем успешный статус ответа
#         self.assertEqual(response.status_code, 200)
#
#         # Проверяем, что на список продуктов существует
#         product_card_text = "Брелок символ СФУ"  # Это может быть текст из карточки продукта
#         self.assertIn(product_card_text, response.text,
#                       f"На странице отсутствуют продукты для категории ID={category_id}")
#         print("Продукты доступны на странице для категории 'Gifts'")
#
#     def test_filter_by_Clothes_category(self):
#     category_id = 1
#     requests.get('http://127.0.0.1:8000')
#     requests.get('http://127.0.0.1:8000/products/')
#     response = requests.get(f'http://127.0.0.1:8000/products/category/{category_id}/')
#     response.raise_for_status()  # Проверяем успешный статус ответа
#     print(response.raise_for_status())  # none - ошибок нету
#     self.assertEqual(response.status_code, 200)
#
#     # Проверяем, что на список продуктов существует
#     product_card_text = "Брелок символ СФУ"  # Это может быть текст из карточки продукта
#     self.assertIn(product_card_text, response.text,
#                   f"На странице отсутствуют продукты для категории ID={category_id}")
#     print("Продукты доступны на странице для категории 'Gifts'")
#
#
# if __name__ == '__main__':
#     unittest.main()
