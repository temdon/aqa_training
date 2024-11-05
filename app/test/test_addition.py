__author__ = 'Artem Kolesnichenko'
__date__ = '18.10.2024'

import allure
import pytest

from app.main import Application


@pytest.mark.vm
@allure.title('Test addition')
@allure.link(url='', name='Test description')
@pytest.mark.parametrize('val_1', [1, 2, 3])
@pytest.mark.parametrize('val_2', [4, 5])
def test_addition(val_1, val_2):
    """Test addition.

    **Command example**::

        2 + 2

    Setup:
        - None

    Test Body:
        - {val_1} + {val_2} = {exp_result}

    Teardown:
        - None
    """

    client = Application()

    exp_result = val_1 + val_2
    with allure.step(f'{val_1} + {val_2} == {exp_result}'):
        add_result = client.add(val_1, val_2)
        assert add_result == exp_result
