
import unittest
from main import estoque, cadastrar_produto


class TestEstoque(unittest.TestCase):

    def setUp(self):
        estoque.clear()

    def test_cadastrar_produto(self):
        estoque["Arroz"] = {
            "quantidade": 10,
            "preco": 25.0
        }

        self.assertIn("Arroz", estoque)
        self.assertEqual(estoque["Arroz"]["quantidade"], 10)
        self.assertEqual(estoque["Arroz"]["preco"], 25.0)


if __name__ == "__main__":
    unittest.main()
