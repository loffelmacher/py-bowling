import pytest
from app import create_app


@pytest.fixture
def app():
    test_app = create_app('testing')
    return test_app.test_client()


def test_empty_data_error(app):
    res = app.post('/api/v1/valuation', data={})
    assert res.is_json is True
    assert res.status_code == 400
    assert 'Bad Request' in res.json['error']
    assert res.json['message'] == 'Empty data'
