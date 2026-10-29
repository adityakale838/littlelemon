Little Lemon Back-End Capstone

SETUP
1. python -m venv venv  &&  activate it
2. pip install -r requirements.txt
3. Create a MySQL database named littlelemon and set USER/PASSWORD in LittleLemon/settings.py
4. python manage.py makemigrations restaurant
5. python manage.py migrate
6. python manage.py runserver
7. Tests: python manage.py test

API PATHS TO TEST (base http://127.0.0.1:8000)

Static page
GET    /

Registration and authentication
POST   /auth/users/                 body: username, email, password
POST   /auth/token/login/           body: username, password -> returns auth_token
GET    /auth/users/me/              header: Authorization: Token <token>

Menu
GET    /restaurant/menu/            list all items
POST   /restaurant/menu/            create item (token required)
GET    /restaurant/menu/1           single item
PUT    /restaurant/menu/1           update item (token required)
DELETE /restaurant/menu/1           delete item (token required)

Table bookings (token required)
GET    /restaurant/booking/tables/        list bookings
POST   /restaurant/booking/tables/        body: name, no_of_guests, booking_date
GET    /restaurant/booking/tables/1
PUT    /restaurant/booking/tables/1
DELETE /restaurant/booking/tables/1

Sample menu body:    {"title": "Greek Salad", "price": "12.50", "inventory": 20}
Sample booking body: {"name": "Jane", "no_of_guests": 4, "booking_date": "2026-12-01T19:00:00Z"}# littlelemon
