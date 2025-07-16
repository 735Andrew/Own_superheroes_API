import requests as r
from typing import Tuple, Dict
import sqlalchemy as sa
from flask import request
from app import app, db
from app.models import Hero
from config import API_TOKEN


@app.route("/hero", methods=["POST"])
def add_hero() -> Tuple[Dict, int, Dict]:
    try:
        hero_name = request.get_json()["name"]
        URL = f"https://superheroapi.com/api/{API_TOKEN}/search/{hero_name}"
        response = r.get(URL).json()

        if response["response"] == "success":
            hero = db.session.scalar(sa.select(Hero).where(Hero.name == hero_name))

            if hero is None:
                data = response["results"][0]["powerstats"]
                hero = Hero(
                    name=hero_name,
                    intelligence=data["intelligence"],
                    strength=data["strength"],
                    speed=data["speed"],
                    power=data["power"],
                )
                db.session.add(hero)
                db.session.commit()

                return hero.to_dict(), 201, {"Content-Type": "application/json"}
            else:
                return (
                    {"error": "character with given name have been already added."},
                    409,
                    {"Content-Type": "application/json"},
                )
        else:
            return (
                {"error": response["error"]},
                404,
                {"Content-Type": "application/json"},
            )

    except Exception as e:
        return {"error": str(e)}, 400, {"Content-Type": "application/json"}


@app.route("/hero", methods=["GET"])
def explore_heroes() -> Tuple[str:Dict]:
    try:
        query_data = request.args.to_dict()  # Taking arguments from query string
        output_structure = {}

        for key, value in query_data.items():
            if key in ("name", "intelligence", "strength", "speed", "power"):
                if key == "name":
                    hero = db.session.scalar(sa.select(Hero).where(Hero.name == value))
                    if hero is not None:
                        return hero.to_dict(), 200, {"Content-Type": "application/json"}
                    else:
                        raise ValueError(
                            f"There is no hero with name '{value}' in your collection of superheroes."
                        )
                else:
                    if 0 <= int(value) <= 100:  # Preventing SQL Injection
                        query1 = sa.select(Hero).where(
                            sa.text(f"heroes.{key} > {value}")
                        )
                        query2 = sa.select(Hero).where(
                            sa.text(f"heroes.{key} < {value}")
                        )
                        query3 = sa.select(Hero).where(
                            sa.text(f"heroes.{key} = {value}")
                        )

                        output_structure[key] = {
                            f"Heroes with an ability level higher than {value}": [
                                hero.to_dict()
                                for hero in db.session.scalars(query1).fetchall()
                            ],
                            f"Heroes with an ability level lower than {value}": [
                                hero.to_dict()
                                for hero in db.session.scalars(query2).fetchall()
                            ],
                            f"Heroes with an ability level {value}": [
                                hero.to_dict()
                                for hero in db.session.scalars(query3).fetchall()
                            ],
                        }
                    else:
                        raise ValueError("Wrong data type for ability level.")

            else:
                return (
                    {"error": f"argument '{key}' is not supported."},
                    422,
                    {"Content-Type": "application/json"},
                )
        return output_structure, 200, {"Content-Type": "application/json"}

    except Exception as e:
        return {"error": str(e)}, 400, {"Content-Type": "application/json"}
