# -*- coding: utf-8 -*-
import unittest

from best_western import Item, BestWestern


class BestWesternTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        best_western = BestWestern(items)
        best_western.update_items()
        self.assertEqual("foo", items[0].name)
    
    # Check that normal item quality decreases by one each day before sell-in date
    def test_one_day_value_decrease_before_sell_in(self):
        items = [Item("Juice", 5, 10)]
        best_western = BestWestern(items)
        best_western.update_items()
        self.assertEqual(9, items[0].quality)

    def test_one_day_value_decrease_past_sell_in(self):
        items = [Item("Juice", 0, 10)]
        best_western = BestWestern(items)
        best_western.update_items()
        self.assertEqual(8, items[0].quality)
    
    def test_two_day_value_decrease_past_sell_in(self):
        items = [Item("Juice", 0, 10)]
        best_western = BestWestern(items)
        best_western.update_items()
        best_western.update_items()
        self.assertEqual(6, items[0].quality)
    
    def test_aged_cheese_one_day_value_increase_before_sell_in(self):
        items = [Item("Aged Cheese", 5, 10)]
        best_western = BestWestern(items)
        best_western.update_items()
        self.assertEqual(11, items[0].quality)

    def test_aged_cheese_one_day_value_increase_after_sell_in(self):
        items = [Item("Aged Cheese", 0, 10)]
        best_western = BestWestern(items)
        best_western.update_items()
        self.assertEqual(12, items[0].quality)
    
    def test_aged_cheese_two_day_value_increase_after_sell_in(self):
        items = [Item("Aged Cheese", 0, 10)]
        best_western = BestWestern(items)
        best_western.update_items()
        best_western.update_items()
        self.assertEqual(14, items[0].quality)
    
    def test_aged_cheese_max_quality(self):
        items = [Item("Aged Cheese", 3, 50)]
        best_western = BestWestern(items)
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        self.assertEqual(50, items[0].quality)
    
    def test_platinum_surfboard(self):
        items = [Item("Platinum Surfboard", 5, 80)]
        best_western = BestWestern(items)
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        self.assertEqual(80, items[0].quality)
    
    def test_conference_tickets_more_than_ten_days_value_increase(self):
        items = [Item("Conference Tickets", 16, 20)]
        best_western = BestWestern(items)
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        self.assertEqual(25, items[0].quality)
    
    def test_conference_tickets_ten_days_or_less_but_more_than_five_days_value_increase(self):
        items = [Item("Conference Tickets", 11, 20)]
        best_western = BestWestern(items)
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        self.assertEqual(29, items[0].quality)
    
    def test_conference_tickets_five_days_or_less_value_increase(self):
        items = [Item("Conference Tickets", 6, 20)]
        best_western = BestWestern(items)
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        self.assertEqual(34, items[0].quality)
    
    def test_conference_tickets_past_sell_zero_value(self):
        items = [Item("Conference Tickets", 6, 20)]
        best_western = BestWestern(items)
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        best_western.update_items()
        self.assertEqual(0, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
