__author__ = 'Artem Kolesnichenko'
__date__ = '18.10.2024'

import allure
import pytest


@pytest.mark.
@allure.title('')
@allure.link(url='', name='Test description')
def test_first():
    """None

    **Command example**::

        # TODO

    Setup:
        - None

    Test Body:
        - None

    Teardown:
        - None
    """

    with allure.step('Title'):
        a_list = [1, 2, 3]
        next()
