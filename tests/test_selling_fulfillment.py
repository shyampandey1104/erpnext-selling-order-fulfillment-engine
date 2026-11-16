import unittest
from selling_fulfillment.engine import ERPNextSellingOrderEngine, VolumePricingRule, SalesOrderItem

class TestSellingEngine(unittest.TestCase):
    def test_volume_discount_rule(self):
        engine = ERPNextSellingOrderEngine()
        rules = [
            VolumePricingRule(1.0, 9.0, discount_pct=0.0),
            VolumePricingRule(10.0, 49.0, discount_pct=10.0),
            VolumePricingRule(50.0, 999.0, discount_pct=20.0)
        ]
        rate_small = engine.apply_pricing_rules(5.0, 100.0, rules)
        self.assertEqual(rate_small, 100.0)

        rate_bulk = engine.apply_pricing_rules(20.0, 100.0, rules)
        self.assertEqual(rate_bulk, 90.0)

    def test_pick_list_allocation(self):
        engine = ERPNextSellingOrderEngine()
        items = [SalesOrderItem("SKU-LAPTOP", 5.0, 60000.0)]
        stock = {"SKU-LAPTOP": 10.0}
        pick = engine.generate_pick_list(items, stock)
        self.assertTrue(pick[0].is_stock_available)
        self.assertEqual(pick[0].qty_allocated, 5.0)

if __name__ == "__main__":
    unittest.main()
