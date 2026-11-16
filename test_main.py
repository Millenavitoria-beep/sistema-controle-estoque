
import unittest

from main import (
    estoque,
    cadastrar_produto,
    registrar_entrada,
    registrar_saida
)


class TestSistemaEstoque(unittest.TestCase):

    def setUp(self):
        estoque.clear()

    def test_cadastrar_produto(self):
        resultado = cadastrar_produto("Arroz", 10, 25.0)

        self.assertTrue(resultado)
        self.assertEqual(estoque["Arroz"]["quantidade"], 10)

    def test_registrar_entrada(self):
        cadastrar_produto("Feijao", 5, 8.0)

        resultado = registrar_entrada("Feijao", 3)

        self.assertTrue(resultado)
        self.assertEqual(estoque["Feijao"]["quantidade"], 8)

    def test_registrar_saida(self):
        cadastrar_produto("Leite", 10, 5.5)

        resultado = registrar_saida("Leite", 2)

        self.assertTrue(resultado)
        self.assertEqual(estoque["Leite"]["quantidade"], 8)

    def test_saida_maior_que_estoque(self):
        cadastrar_produto("Cafe", 5, 15.0)

        resultado = registrar_saida("Cafe", 10)

        self.assertFalse(resultado)
        self.assertEqual(estoque["Cafe"]["quantidade"], 5)


if __name__ == "__main__":
    unittest.main()
