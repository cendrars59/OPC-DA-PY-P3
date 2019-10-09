# -*- coding: Utf-8 -*
from utils.filesManagement.import_items import build_list_from_file
from models.Item import Item


class ItemsList:

    def __init__(self):
        self.list = build_list_from_file()

    def dispatch_items_randomly(self, level):
        """
        Function to dispatch randomly each items
        :param level:
        :return:
        """
        for item in self.list:
            item.position = Item.define_random_position(item, level)

    def find_an_item_in_list(self, level):
        """
        function to find an item into the list
        :param level:
        :return:
        """
        for element in self.list:
            element.find_an_item(element, level)





