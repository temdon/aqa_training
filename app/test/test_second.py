__author__ = 'Artem Kolesnichenko'
__date__ = '18.10.2024'

import allure
import pytest


@pytest.mark.
@allure.title('')
@allure.link(url='', name='Test description')
def test_second():
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
        pass
