import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


API_TOKEN = os.environ.get("API_TOKEN")

# Making opportunity to test API in sandbox with env variable
if os.environ.get("TESTS") == "True":
    DATABASE_URL = "sqlite:///:memory:"
else:
    DATABASE_URL = os.environ.get("POSTGRESQL_DATABASE_URL")
