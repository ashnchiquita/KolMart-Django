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

## Run Command
1. Run `pip install -r requirements.txt`
2. Create `.env` folder inside `./kolmart` directory
3. Put your JWT secret key (`JWT_SECRET`), single service account username (`SS_USERNAME`), single service account password (`SS_PASSWORD`), single service api URL (`SS_API_URL`) in `.env` file
4. Run migration command and if needed, run seeding command
5. Run `python manage.py runserver`
6. App will run at `http://localhost:8000`

# Endpoints
- POST `/api/login`
- POST `/api/logout`
- GET `/api/order`
- GET, POST `/api/product/:id`
- POST `/api/register`
- GET `/api/self`
- GET `/api/store`

# Bonuses Done

## B03 - Single Service Implementation
Single service implemented using TypeScript with string typing, no `as` and `any` keywoard, and runtime type checking.

## B05 - Lighthouse
1. Login (`/login`) with average score 95.5
![Screen Shot 2023-07-29 at 19 09 15](https://github.com/ashnchiquita/KolMart-Django/assets/88751131/165beebf-ad55-4e90-9c1d-9f727c91be48)

3. Register (`/register`) with average score 95.5
![Screen Shot 2023-07-29 at 19 08 09](https://github.com/ashnchiquita/KolMart-Django/assets/88751131/071da31e-a0da-490b-8671-da5cebec7fb7)

5. Store (`/store`) with average score 97.5
![Screen Shot 2023-07-29 at 19 09 55](https://github.com/ashnchiquita/KolMart-Django/assets/88751131/42e2520b-0f29-4d47-ad4a-3c32b684b413)

6. Product (`/product/{product_id}`) with average score 96.25
![Screen Shot 2023-07-29 at 19 10 37](https://github.com/ashnchiquita/KolMart-Django/assets/88751131/4352c3eb-4e7d-458f-9a05-12b5b2c09219)

8. Cart (`/cart`) with average score 98\
![Screen Shot 2023-07-29 at 19 14 24](https://github.com/ashnchiquita/KolMart-Django/assets/88751131/d557cd3b-0922-47f6-8033-27e89364ff89)

9. Orders (`/order`) with average score 98\
![Screen Shot 2023-07-29 at 19 15 11](https://github.com/ashnchiquita/KolMart-Django/assets/88751131/aaf71197-6e6d-4104-afc6-72976b760d68)

## B06 - Responsive Layout
KolMart frontend is built responsive.

## B07 - API Documentation
API documentation for single service can be accessed [here](https://app.swaggerhub.com/apis/16521248/ohl_single_service/1). API documentation for monolith can be accessed [here](https://app.swaggerhub.com/apis/16521248/ohl_monolith/1).

## B11 - Additional Features
1. Logout
2. Cart

## B12 - FE Admin Bug Fix
- fix: change replace query to set query in barang filter (#3)
