# -*- coding: utf-8 -*-
# import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
from sqlalchemy.dialects.postgresql import JSONB

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# Ниже описание модели

# Класс Растение
class Plant(Base):
    __tablename__ = 'plants'

    mainclass_id  = db.Column(db.Integer, db.ForeignKey("mainclasses.id"), nullable=False)
    species_id    = db.Column(db.Integer, db.ForeignKey("species.id"), nullable=False)
    name_rus = db.Column(db.String(128), nullable=False)
    name_lat = db.Column(db.String(128), nullable=False)
    properties    = db.Column(JSONB, nullable=True)

    # New instance instantiation procedure
    def __init__(self, mainclass_id, species_id, name_rus, name_lat, properties):
        self.mainclass_id  = mainclass_id
        self.species_id    = species_id
        self.name_rus = name_rus
        self.name_lat = name_lat
        self.properties = properties

    def __repr__(self):
        return '<Plant %s>' % (self.name_rus)

# Класс "Главный класс"
class Mainclass(Base):
    __tablename__ = 'mainclasses'

    name_rus = db.Column(db.String(128), nullable=False)
    name_lat = db.Column(db.String(128), nullable=False)

    # New instance instantiation procedure
    def __init__(self, name_rus, name_lat):
        self.name_rus = name_rus
        self.name_lat = name_lat

    def __repr__(self):
        return '<Mainclass %s>' % (self.name_rus)

# Класс Вид
class Specie(Base):
    __tablename__ = 'species'

    genus_id  = db.Column(db.Integer, db.ForeignKey("genuses.id"), nullable=False)
    name_rus = db.Column(db.String(128), nullable=False)
    name_lat = db.Column(db.String(128), nullable=False)

    # New instance instantiation procedure
    def __init__(self, genus_id, name_rus, name_lat):
        self.genus_id  = genus_id
        self.name_rus = name_rus
        self.name_lat = name_lat

    def __repr__(self):
        return '<User %r>' % (self.name)

# Класс Род
class Genus(Base):
    __tablename__ = 'genuses'

    family_id  = db.Column(db.Integer, db.ForeignKey("families.id"), nullable=False)
    name_rus = db.Column(db.String(128), nullable=False)
    name_lat = db.Column(db.String(128), nullable=False)

    # New instance instantiation procedure
    def __init__(self, family_id, name_rus, name_lat):
        self.family_id  = family_id
        self.name_rus = name_rus
        self.name_lat = name_lat

    def __repr__(self):
        return '<User %r>' % (self.name)

# Класс Семейство
class Family(Base):
    __tablename__ = 'families'

    lifeform_id  = db.Column(db.Integer, db.ForeignKey("lifeforms.id"), nullable=False)
    name_rus = db.Column(db.String(128), nullable=False)
    name_lat = db.Column(db.String(128), nullable=False)

    # New instance instantiation procedure
    def __init__(self, lifeform_id, name_rus, name_lat):
        self.lifeform_id  = lifeform_id
        self.name_rus = name_rus
        self.name_lat = name_lat

    def __repr__(self):
        return '<User %r>' % (self.name)

# Класс Жизненная форма
class Lifeform(Base):
    __tablename__ = 'lifeforms'

    name_rus = db.Column(db.String(128), nullable=False)
    name_lat = db.Column(db.String(128), nullable=False)

    # New instance instantiation procedure
    def __init__(self, name_rus, name_lat):
        self.name_rus = name_rus
        self.name_lat = name_lat

    def __repr__(self):
        return '<User %r>' % (self.name)