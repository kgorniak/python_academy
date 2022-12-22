import requests
from faker import Faker


class APIHandler:
    url = "https://pokeapi.co/api/v2"
    pokemon_endpoint = "/pokemon"
    pokemon_shape_endpoint = "/pokemon-shape"

    def get_pokemons(self, name_or_id="", params=None):
        response = requests.get(f"{self.url}{self.pokemon_endpoint}/{name_or_id}", params=params)
        response_body = response.json()
        return response_body

    def get_pokemon_shape(self, name_or_id="", params=None):
        response = requests.get(f"{self.url}{self.pokemon_shape_endpoint}/{name_or_id}", params=params)
        response_body = response.json()
        return response_body

    def get_random_pokemon(self, name_or_id="", params=None):
        faker = Faker()
        random_pokemon_id = faker.random_int(1, 905)
        response = requests.get(f"{self.url}{self.pokemon_endpoint}/{random_pokemon_id}", params=params)
        response_body = response.json()
        return response_body
