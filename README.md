### Hotel Price Comparison Website

This is a Django-based hotel price comparison website that scrapes hotel prices from Booking.com and Agoda. Users can search for hotels by city, price range, and star rating, compare prices, and bookmark hotels for future reference.

# Features

1. User authentication (signup/login/logout)

2. Search hotels by city, price range, and star rating

S3. crape hotel data from Booking.com and Agoda using Scrapy

4. Display results with price comparison

5. Bookmark hotels for later viewing

# Installation Guide

# Prerequisites

Ensure you have the following installed:

 - Python 3.8+

 - PostgreSQL

 - Django

 - Scrapy

# Step 1: Clone the Repository

```bash
    git clone https://github.com/sajidZ-904/Hotel_Price_Comparison.git
    cd Hotel_Price_Comparison
```

# Step 2: Create a Virtual Environment

```bash
    python3 -m venv virtualenv
    source virtualenv/bin/activate  # On Windows use: venv\Scripts\activate
```

# Step 3: Install Dependencies

```bash
    pip install -r requirements.txt
```

# Step 4: Configure the Database

Edit ```hotel_compare/settings.py``` to set up PostgreSQL:

```bash
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Run migrations

```bash
    python manage.py migrate
```

# Step 5: Run the scrapers:

```bash
    cd hotel_scraper
    scrapy crawl booking
    scrapy crawl agoda
```

# Step 6: Run the server

```bash
    cd ..
    python manage.py runserver
```

Open ```http://127.0.0.1:8000/`` in your browser. Check the following APIs:

 - Login/Register: ```http://127.0.0.1:8000/accounts/login/```
 - Hotel Search: ```http://127.0.0.1:8000/hotels/search/```
 - Bookmarks: ```http://127.0.0.1:8000/hotels/bookmarks/```

### How to Use

1. **Register/Login**: Create an account and log in.

2. **Search Hotels**: Enter a city, price range, and star rating.

3. **Compare Prices**: View hotel listings with prices from Booking.com and Agoda.

4. **Bookmark Hotels**: Click on the bookmark button to save a hotel.

5. **View Bookmarks**: Access saved hotels on the bookmark page.

### Database Setup (PostgreSQL)

1. Create a PostgreSQL database:

```bash
    sudo -u postgres psql
    CREATE DATABASE hotel_db;
    CREATE USER your_user WITH PASSWORD 'your_password';
    ALTER ROLE your_user SET client_encoding TO 'utf8';
    ALTER ROLE your_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE your_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE hotel_db TO your_user;
    \q
```

2. Update ```hotel/compare/settings.py``` with the correct database credentials.

3. Run migrations:

```bash
    python manage.py migrate
```

### Deployment

For deploying on a production server:

1. Set up **Gunicorn**

2. Configure **Nginx** for reverse proxy

3. Use **PostgreSQL** instead of SQLite

Enable **HTTPS** with **Let's Encrypt**

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License

MIT License