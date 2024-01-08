from django.test import TestCase
from users.models import User
from django.test import Client


# class LoginTestCase(TestCase):
#
#     def setUp(self):
#         # Создаем существующего пользователя для входа
#         self.username = 'asddsa'
#         self.password = 'tbbs1999'
#         self.user = User.objects.create_user(username=self.username, password=self.password)
#
#         # Создаем клиент для отправки запросов
#         self.client = Client()
#
#     def test_login_existing_user(self):
#         # Отправляем POST-запрос для входа пользователя
#         login = self.client.login(username=self.username, password=self.password)
#
#         # Проверяем успешность входа
#         self.assertTrue(login, "Не удалось войти в аккаунт")
#
#         # Получаем информацию о текущем пользователе
#         user = User.objects.get(username=self.username)
#         self.assertEqual(user.username, self.username, "Пользователь не совпадает")
