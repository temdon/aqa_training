__author__ = 'Artem Kolesnichenko'
__email__ = 'artem.kolesnichenko@objectfirst.com'
__date__ = '16.10.2024'

import random


class Application:
    def add(self, a: int, b: int) -> int:
        """Return summ of parameters"""
        return a + b

    def get_items_random_order(self) -> tuple:
        items = ('one', 'two', 'three')
        result_list = []
        cnt = 0
        while cnt < len(items):
            netx_item = random.choice(items)
            if netx_item not in result_list:
                result_list.append(netx_item)
                cnt += 1

        return tuple(result_list)
