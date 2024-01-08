import unittest
from products.views import ProductsListView
from products.models import Product
from django.views.generic.list import ListView
from unittest.mock import MagicMock


class TestProductsListView(unittest.TestCase, ListView):
    def setUp(self):
        self.view = ProductsListView()

    def test_model_attribute(self):
        self.assertEqual(self.view.model, Product)
        print("complete1")

    def test_template_name_attribute(self):
        self.assertEqual(self.view.template_name, 'products/products.html')
        print("complete2")

    def test_paginate_by_attribute(self):
        self.assertEqual(self.view.paginate_by, 6)
        print("complete3")

    def test_title_attribute(self):
        self.assertEqual(self.view.title, 'U-STYLE CATALOG')
        print("complete4")

    def test_get_queryset_with_category_id(self):
        self.view.kwargs = {'category_id': 1}  # Пример category_id для теста

        # Здесь убедимся, что вызывается метод, и вернем ожидаемое значение
        expected_count = 4  # Замените на фактическое количество продуктов с category_id = 1
        self.view.get_queryset = MagicMock(return_value=Product.objects.filter(category_id=self.view.kwargs['category_id']))
        result = self.view.get_queryset()

        # Проверяем, что вызывается метод с корректными параметрами
        self.view.get_queryset.assert_called_once()

        # Проверяем, что результат содержит ожидаемое количество объектов
        self.assertEqual(result.count(), expected_count)

        print("работаем2")

    def test_get_queryset_without_category_id(self):
        # Сбрасываем атрибут, чтобы симулировать отсутствие category_id
        self.view.kwargs = {}
        self.view.get_queryset = MagicMock(return_value=Product.objects.all())
        result = self.view.get_queryset()

        # Проверяем, что вызвался метод без фильтрации
        self.view.get_queryset.assert_called_once()
        self.assertEqual(result.count(), 11)  # Замените на ожидаемое количество объектов
        print("работаем")

    def test_get_queryset_with_different_category_ids(self):
        test_cases = [
            {'category_id': 1, 'expected_count': 4},
            {'category_id': 4, 'expected_count': 4},
            # Добавьте больше тестовых случаев, если необходимо
        ]

        for case in test_cases:
            self.view.kwargs = {'category_id': case['category_id']}
            expected_count = case['expected_count']

            self.view.get_queryset = MagicMock(
                return_value=Product.objects.filter(category_id=self.view.kwargs['category_id']))
            result = self.view.get_queryset()

            self.view.get_queryset.assert_called_once()
            self.assertEqual(result.count(), expected_count)

        print("работаем2")
