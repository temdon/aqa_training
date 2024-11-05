__author__ = 'Artem Kolesnichenko'
__email__ = 'artem.kolesnichenko@objectfirst.com'
__date__ = '01.11.2024'

import pytest


@pytest.fixture(params=['versioning', 'non-versioning'])
def get_bucket(request):
    fixture_parameter = request.param
    print(f'Bucket: {fixture_parameter}')

    return fixture_parameter


@pytest.fixture
def put_object(register_se, get_bucket):
    bucket = get_bucket
    print(f'Object put to the bucket to bucket {bucket}')

    yield

    print('Delete object from bucket')


@pytest.fixture
def register_se(get_bucket):
    bucket = get_bucket
    print(f'Registering SE on  bucket {bucket}')

    yield

    print('Unregistering SE')
