from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(APITestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pasta", price=15, inventory=40)

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")
        expected = MenuSerializer(Menu.objects.all(), many=True).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected)

    def test_single_item(self):
        item = Menu.objects.first()
        response = self.client.get(f"/restaurant/menu/{item.pk}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], item.title)

    def test_create_requires_login(self):
        data = {"title": "Soup", "price": "6.50", "inventory": 10}
        self.assertEqual(self.client.post("/restaurant/menu/", data).status_code, 401)


class AuthAndBookingTest(APITestCase):
    def test_booking_requires_token(self):
        self.assertEqual(self.client.get("/restaurant/booking/tables/").status_code, 401)

    def test_register_login_and_book(self):
        reg = self.client.post(
            "/auth/users/",
            {"username": "jane", "password": "Str0ng!pass99", "email": "j@example.com"},
        )
        self.assertEqual(reg.status_code, 201)
        login = self.client.post(
            "/auth/token/login/", {"username": "jane", "password": "Str0ng!pass99"}
        )
        self.assertEqual(login.status_code, 200)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + login.data["auth_token"])
        booking = self.client.post(
            "/restaurant/booking/tables/",
            {"name": "Jane", "no_of_guests": 2, "booking_date": "2026-12-01T19:00:00Z"},
        )
        self.assertEqual(booking.status_code, 201)
        self.assertEqual(len(self.client.get("/restaurant/booking/tables/").data), 1)


class HomePageTest(APITestCase):
    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Little Lemon")
