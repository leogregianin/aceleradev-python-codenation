from main import SellersRancking
import unittest


class SellersRanckingTests(unittest.TestCase):
    def test_best_seller(self):
        sellers = [
            {"name": "Joaquina", "store": 2, "value": 1200.00},
            {"name": "Pedro", "store": 2, "value": 120.00},
            {"name": "Maria", "store": 1, "value": 450.00},
            {"name": "Fernanda", "store": 1, "value": 4000.00},
            {"name": "Patricia", "store": 1, "value": 100.00},
        ]
        rancking = SellersRancking()
        self.assertEqual(rancking.best_seller(sellers), ["Fernanda"])

    def test_rancking_list(self):
        sellers = [
            {"name": "Joaquina", "store": 2, "value": 1200.00},
            {"name": "Pedro", "store": 2, "value": 120.00},
            {"name": "Maria", "store": 1, "value": 450.00},
            {"name": "Fernanda", "store": 1, "value": 4000.00},
            {"name": "Patricia", "store": 1, "value": 100.00},
        ]
        rancking = SellersRancking()
        self.assertEqual(len(rancking.rancking_list(sellers)), 5)

    def test_best_seller_store(self):
        sellers = [
            {"name": "Joaquina", "store": 2, "value": 1200.00},
            {"name": "Pedro", "store": 2, "value": 120.00},
            {"name": "Maria", "store": 1, "value": 450.00},
            {"name": "Fernanda", "store": 1, "value": 4000.00},
            {"name": "Patricia", "store": 1, "value": 100.00},
        ]
        rancking = SellersRancking()
        self.assertEqual(len(rancking.best_seller_store(sellers, 1)), 1)

    def test_sales_goals(self):
        sellers = [
            {"name": "Joana", "store": 2, "value": 1200.00},
            {"name": "Pedro", "store": 2, "value": 120.00},
            {"name": "Maria", "store": 1, "value": 450.00},
        ]
        rancking = SellersRancking()
        self.assertEqual(len(rancking.sales_goals(sellers)), 2)

if __name__ == '__main__':
    unittest.main()
