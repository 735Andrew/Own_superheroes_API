from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


API_TOKEN = os.environ.get("API_TOKEN")
POSTGRESQL_DATABASE_URL = os.environ.get("POSTGRESQL_DATABASE_URL")
SQLITE_DATABASE_URL = "sqlite:///" + os.path.join(basedir, "app.db")  # todo change db
