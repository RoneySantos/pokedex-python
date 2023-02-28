from flask.globals import *
from models.pokemon import PokemonClass
from flask import Flask, render_template, jsonify
import requests
import json

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search_page", methods = ["GET", "post"])
def buscar():
    pokemon = PokemonClass(request.form["name_pokemon"].lower(),"","")
    try:
        res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.name}").text)
        result_number = res["id"]
        pokemon.number = result_number
        # Get photo
        result_photo = res["sprites"]
        result_photo = result_photo["front_default"]
        pokemon.photo = result_photo
    except:
        return "Pokemon not found"
    return render_template("index.html",
    name = pokemon.name,
    photo = pokemon.photo,
    number = pokemon.number
    
    )

if __name__=="__main__":
    app.run(debug=True)