# -*- coding: UTF-8 -*-
# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
# from app.mod_auth.forms import LoginForm

# Import module models (i.e. User)
from app.mod_gendata.models import *

import latin_names

import random


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_gendata = Blueprint('gendata', __name__, url_prefix='/gendata')

# Заполняемые сущности
entities_tuple = (
    (Lifeform, 10),
    (Family, 10),
    (Genus, 10),
    (Specie, 10),
    (Plant, 5)
)

def gen_name(lan):
    if lan == "lat":
        return random.sample(latin_names.latin_names,1)[0]
    if lan == "rus":
        return random.sample(latin_names.russian_names,1)[0]

def add_entities(entity_index, parent_id):
    entity_class = entities_tuple[entity_index][0]
    for count in range(entities_tuple[entity_index][1]):
        if entity_index == 0:
            obj = entity_class(gen_name("rus"), gen_name("lat"))
        elif entity_index < 4:
            obj = entity_class(parent_id, gen_name("rus"), gen_name("lat"))
        elif entity_index == 4:
            obj = entity_class(1, parent_id, gen_name("rus"), gen_name("lat"), '{}')
        db.session.add(obj)
        db.session.flush()
        db.session.refresh(obj)
        print obj.id
        if entity_index < len(entities_tuple) - 1:
            add_entities(entity_index+1, obj.id)

@mod_gendata.route('/generate/', methods=['GET'])
def generate_data():
    add_entities(0, None)
    db.session.commit()
    return render_template("gendata/generate.html")
