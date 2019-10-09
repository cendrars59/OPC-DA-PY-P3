import models.Item
from parameters import itemsParams


def build_list_from_file():
    items_list = []
    for key, value in itemsParams.items.items():
        temp_item = models.Item.Item(value['name'], value['icon'])
        items_list.append(temp_item)
    return items_list

