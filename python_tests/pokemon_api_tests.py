import unittest
import requests


class PokemonTests(unittest.TestCase):

    def setUp(self) -> None:
        self.url = "https://pokeapi.co/api/v2"
        self.pokemon_endpoint = "/pokemon"

    def test_default_pokemons(self):
        response = requests.get(self.url + self.pokemon_endpoint)
        response_body = response.json()
        size = len(response.content) / 1000
        roundtrip = response.elapsed.total_seconds() * 1000

        self.assertEqual(1154, response_body["count"])
        self.assertTrue(response_body)
        self.assertEqual(200, response.status_code)
        self.assertTrue(1000 > roundtrip)
        self.assertLess(size, 100)


if __name__ == '__main__':
    unittest.main()
