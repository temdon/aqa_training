__author__ = 'Artem Kolesnichenko'
__date__ = '18.10.2024'

import allure
import pytest

from app.main import Application


@pytest.mark.env
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

    client = Application()

    with allure.step('2 + 2 ==4'):
        add_result = client.add(2, 2)
        assert add_result == 4
