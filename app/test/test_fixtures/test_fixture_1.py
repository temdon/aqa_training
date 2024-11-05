__author__ = 'Artem Kolesnichenko'
__date__ = '01.11.2024'

import allure
import pytest


@allure.title('')
@allure.link(url='', name='Test description')
@pytest.mark.parametrize('get_bucket, exp_obj_name', [('our_bucket', 'my_object')], indirect=['get_bucket'])
def test_fixture_1(put_object, get_bucket, exp_obj_name):
    """None

    **Command example**::

        # TODO

    Setup:
        - Put object to the bucket

    Test Body:
        - Get object
        - Verify result

    Teardown:
        - None
    """

    with allure.step('Get object'):
        print('Get object')

    with allure.step('Resuil is correct'):
        print('Verify object')
