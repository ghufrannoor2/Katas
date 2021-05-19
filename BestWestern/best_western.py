# -*- coding: utf-8 -*-
import enum
from abc import ABC, abstractmethod

class BestWestern(object):

    def __init__(self, items):
        self.items = items
        self._item_type = ItemTypes.REGULAR
        self._is_item_on_sale = False
        self._is_item_past_sell_in = False
    
    def _classify_item(self, item):
        negative_diminishment_items = ["Aged Cheese", "Conference Tickets"]
        precious_items = ["Platinum Surfboard"]

        if item.name in negative_diminishment_items:
            self._item_type = ItemTypes.NEGATIVE_DIMINISHMENT

        if item.name == "Conference Tickets":
            self._item_type = ItemTypes.CONFERENCE_TICKETS

        if item.name in precious_items:
            self._item_type = ItemTypes.PRECIOUS
        
        if "On Sale" in item.name:
            self._is_item_on_sale = True
        
        if item.sell_in <= 0:
            self._is_item_past_sell_in = True
    
    def update_items(self):
        for item in self.items:
            self._classify_item(item)
            if self._item_type == ItemTypes.REGULAR:
                item_updater = ItemUpdaterRegular(item, self._is_item_on_sale, self._is_item_past_sell_in)
            elif self._item_type == ItemTypes.NEGATIVE_DIMINISHMENT:
                item_updater = ItemUpdaterNegativeDiminishment(item, self._is_item_on_sale, self._is_item_past_sell_in)
            elif self._item_type == ItemTypes.CONFERENCE_TICKETS:
                item_updater = ItemUpdaterConferenceTickets(item, self._is_item_on_sale, self._is_item_past_sell_in)
            else:
                item_updater = ItemUpdaterPrecious(item, self._is_item_on_sale, self._is_item_past_sell_in)
        item_updater.update_item()
                

class ItemTypes(enum.Enum):
    REGULAR = 1
    NEGATIVE_DIMINISHMENT = 2
    CONFERENCE_TICKETS = 3
    PRECIOUS = 4


class QualityUpdateInterface(ABC):
    @abstractmethod
    def update_item(self, item):
        pass


class ItemUpdaterRegular(QualityUpdateInterface):
    def __init__(self, item, is_item_on_sale, is_item_past_sell_in):
        self._item = item
        self._is_item_on_sale = is_item_on_sale
        self._is_item_past_sell_in = is_item_past_sell_in

    def _calculate_diminishment_prefactor(self):
        self._diminishment = 1

    def _calculate_diminishment(self):
        self._calculate_diminishment_prefactor()
        
        if self._is_item_on_sale:
            self._diminishment = self._diminishment * 2

        if self._is_item_past_sell_in:
            self._diminishment = self._diminishment * 2
    
    def _update_quality(self):
        self._calculate_diminishment()
        self._item.quality = self._item.quality - self._diminishment
        
        # Handle negative item quality that may have occurred
        if self._item.quality < 0:
            self._item.quality = 0
        
        # Handle overflow item quality that may have occurred
        if self._item.quality > 50 and self._item.quality != 80:
            self._item.quality = 50

    def _update_sell_in(self):
        self._item.sell_in = self._item.sell_in - 1
    
    def update_item(self):
        self._update_quality()
        self._update_sell_in()


class ItemUpdaterNegativeDiminishment(ItemUpdaterRegular):
    def _calculate_diminishment_prefactor(self):
        self._diminishment = -1


class ItemUpdaterConferenceTickets(ItemUpdaterRegular):
    def _calculate_diminishment_prefactor(self):
        self._diminishment = -1
        if self._item.sell_in <= 5:
            self._diminishment = -3
        elif self._item.sell_in <= 10:
            self._diminishment = -2
        if self._item.sell_in <= 0:
            self._diminishment = self._item.quality


class ItemUpdaterPrecious(ItemUpdaterRegular):
    def _calculate_diminishment_prefactor(self):
        self._diminishment = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
