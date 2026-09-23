import unittest
from src.inventory import inventory, add_product, update_stock, remove_product, get_stock, inventory_value

class TestInventory(unittest.TestCase):
    def setUp(self):
        inventory.clear()
        add_product("P001", "Keyboard", 10, 750)
        add_product("P002", "Mouse", 20, 450)

    def test_add_and_stock(self):
        self.assertEqual(get_stock("P001"), 10)

    def test_update_stock(self):
        update_stock("P001", 15)
        self.assertEqual(get_stock("P001"), 15)

    def test_remove_product(self):
        remove_product("P002")
        self.assertNotIn("P002", inventory)

    def test_inventory_value(self):
        self.assertEqual(inventory_value(), 16500)

if __name__ == "__main__":
    unittest.main()
