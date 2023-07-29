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
1. Login (`/login`) with average score 95.5\
![Screen Shot 2023-07-29 at 19 09 15](https://github.com/ashnchiquita/KolMart-Django/assets/88751131/a901dac8-d97f-4290-817e-e4b39c782484)

2. Register (`/register`) with average score 95.5\
![Screen Shot 2023-07-29 at 19 08 09](https://github.com/ashnchiquita/KolMart-Django/assets/88751131/0f0f5c4c-1262-47cc-9f49-ba3cc6f25b04)

3. Store (`/store`) with average score 97.5\
![Screen Shot 2023-07-29 at 19 09 55](https://github.com/ashnchiquita/KolMart-Django/assets/88751131/4ed93136-9316-4d14-bbb5-09135777e55f)

4. Product (`/product/{product_id}`) with average score 96.25\
![Screen Shot 2023-07-29 at 19 10 37](https://github.com/ashnchiquita/KolMart-Django/assets/88751131/9b52bb56-b31d-44d3-bcc4-ac66cf546d61)

5. Cart (`/cart`) with average score 98\
![Screen Shot 2023-07-29 at 19 14 24](https://github.com/ashnchiquita/KolMart-Django/assets/88751131/c44f7b90-4151-4b8e-aef2-8a98abcb105d)

6. Orders (`/order`) with average score 98\
![Screen Shot 2023-07-29 at 19 15 11](https://github.com/ashnchiquita/KolMart-Django/assets/88751131/a7c92aa7-3672-4844-bc16-c65411461484)

## B06 - Responsive Layout
KolMart frontend is built responsive.

## B07 - API Documentation
API documentation for single service can be accessed [here](https://app.swaggerhub.com/apis/16521248/ohl_single_service/1). API documentation for monolith can be accessed [here](https://app.swaggerhub.com/apis/16521248/ohl_monolith/1).

## B11 - Additional Features
1. Logout
2. Cart

## B12 - FE Admin Bug Fix
- fix: change replace query to set query in barang filter (#3)
