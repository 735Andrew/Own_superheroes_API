import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Hero(db.Model):
    __tablename__ = "heroes"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), unique=True)
    intelligence: so.Mapped[int] = so.mapped_column(sa.Integer())
    strength: so.Mapped[int] = so.mapped_column(sa.Integer())
    speed: so.Mapped[int] = so.mapped_column(sa.Integer())
    power: so.Mapped[int] = so.mapped_column(sa.Integer())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "intelligence": self.intelligence,
            "strength": self.strength,
            "speed": self.speed,
            "power": self.power,
        }
