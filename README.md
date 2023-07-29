# KolMart - Monolith Django Ecommerce Web
An ecommerce web application made by Chiquita Ahsanunnisa (13521129) to fulfill Seleksi 3 Programming Laboratory 2023 tasks.

# Author
Chiquita Ahsanunnisa (13521129)

# Tech Stack
- Python @3.10.5
- Pip @23.1.2
- Django @3.1.7
- Django Rest Framework @3.12.4
- Django Environ @0.4.5
- PyJWT @2.0.1

# How To Run
## Migration Command
1. Run `python manage.py makemigrations api`
2. Run `python manage.py migrate`

## Seeding Command
1. Create a json file: `./api/fixtures/initial_data.json`
2. Put seed data inside that file
3. Run `python manage.py initdata`

## Via Docker

## Local
1. Run `pip install -r requirements.txt`
2. Create `.env` folder inside ./kolmart directory
3. Put your JWT secret key (`JWT_SECRET`), single service account username (`SS_USERNAME`), single service account password (`SS_PASSWORD`), single service api URL (`SS_API_URL`) in `.env` file
4. Run migration command and if needed, run seeding command
5. Run `python manage.py runserver`

# Endpoints
- POST `/api/login`
- POST `/api/logout`
- GET `/api/order`
- GET `/api/product/:id`
- POST `/api/product/:id`
- POST `/api/register`
- GET `/api/self`
- GET `/api/store`

# Bonuses Done

## B03 - Single Service Implementation
Single service implemented using TypeScript with string typing, no `as` and `any` keywoard, and runtime type checking.

## B05 - Lighthouse
1. Login (`/login`) with average score 95.5

2. Register (`/register`) with average score 95.5

3. Store (`/store`) with average score 97.5

4. Product (`/store/{product_id}`) with average score 96.25

5. Cart (`/cart`) with average score 98

6. Orders (`/order`) with average score 98

## B06 - Responsive Layout
KolMart frontend is built responsive.
## B07 - API Documentation
API documentation for single service can be accessed [here](http://deploy.com). API documentation for monolith can be accessed [here](http://deploy.com).

## B11 - Additional Features
1. Logout
2. Cart

## B12 - FE Admin Bug Fix
- fix: change replace query to set query in barang filter (#3)
