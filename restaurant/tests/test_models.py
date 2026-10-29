from django.test import TestCase
from restaurant.models import Booking, Menu


class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

    def test_inventory_saved(self):
        item = Menu.objects.create(title="Greek Salad", price=12, inventory=25)
        self.assertEqual(Menu.objects.get(pk=item.pk).inventory, 25)


class BookingModelTest(TestCase):
    def test_booking_str(self):
        b = Booking.objects.create(
            name="Jane", no_of_guests=4, booking_date="2026-12-01T19:00:00Z"
        )
        self.assertEqual(str(b), "Jane")
