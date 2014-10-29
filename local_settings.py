
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "8e4fab34-bd3d-4d99-8053-f15b6c4d91e58c46b114-77b7-4c46-b421-7422c3eb5bb8bdb29368-cbf5-4a79-8986-d59a2c5def78"
NEVERCACHE_KEY = "66db02b9-27f6-47cb-9992-25ff45a88601e08b6968-7ba0-46ff-87de-873d6c4dbfd5d8e59d53-1a89-46de-8b13-8039aec60f1d"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
