import unittest
import requests
from api_handler import APIHandler


class PokemonTests(unittest.TestCase):

    def setUp(self) -> None:
        self.api_handler = APIHandler()

    def test_default_pokemons(self):
        response = requests.get(self.api_handler.url + self.api_handler.pokemon_endpoint)
        response_body = response.json()
        size = len(response.content) / 1000
        roundtrip = response.elapsed.total_seconds() * 1000

        self.assertEqual(1154, response_body["count"])
        self.assertTrue(response_body)
        self.assertEqual(200, response.status_code)
        self.assertTrue(1000 > roundtrip)
        self.assertLess(size, 100)

    def test_get_pokemons_with_offset(self):
        params = {
            "offset": 20,
            "limit": 10
        }
        response_body = self.api_handler.get_pokemons(params=params)

        # self.assertTrue(response_body)
        # self.assertEqual(200, response.status_code)
        self.assertEqual(params["limit"], len(response_body["results"]))     # check limit param
        # self.assertRegex(response_body["results"][0]['url'], ".*\/21\/")    # check offset param
        self.assertRegex(response_body["results"][0]['url'], f"/{params['offset'] + 1}")
        # self.assertIn(f"/{params['offset'] + 1}", response_body["results"][0]['url'])

    def test_get_pokemon_shape_match_id_name(self):

        response_body = self.api_handler.get_pokemon_shape()
        self.assertEqual(response_body["count"], len(response_body["results"]))
        third_shape = response_body["results"][2]["name"]

        response_body = self.api_handler.get_pokemon_shape(name_or_id=third_shape)
        self.assertEqual(3, response_body["id"])

    def test_random_pokemon(self):
        response_body = self.api_handler.get_random_pokemon()
        name = response_body["name"]
        print(name)
        self.assertTrue(response_body["abilities"])
        self.assertGreater(len(response_body["abilities"]), 0)


if __name__ == '__main__':
    unittest.main()
