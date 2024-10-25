__author__ = 'Artem Kolesnichenko'
__date__ = '18.10.2024'

import allure
import pytest

from app.main import Application


@pytest.mark.vm
@allure.title('Test addition')
@allure.link(url='', name='Test description')
@pytest.mark.parametrize('val_1, val_2, exp_result', [
    pytest.param(1, 2, 3, marks=pytest.mark.hw),
    (2, 2, 4)
])
def test_addition(val_1, val_2, exp_result):
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

    with allure.step(f'{val_1} + {val_2} == {exp_result}'):
        'test value : {}'.format(val_1)
        add_result = client.add(val_1, val_2)
        assert add_result == exp_result
