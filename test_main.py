from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)


@pytest.mark.parametrize('param', [
    ('ninetales')
])
def test_read_main(param):
    """
    Test service api rest
    """
    response = client.get(f"/pokemon/{param}")
    assert response.status_code == 200
    assert response.json() == {'id': [38],
                                'name': ['vulpix'],
                                'detail': {'pokeslot': [1],
                                'poketype': ['fire'],
                                'pokeversion': ['red-blue'],
                                'base_happiness': [70],
                                'capture_rate': [75],
                                'color': ['yellow'],
                                'v_egg_groups': ['ground']},
                                'list_evolution': ['ninetales'],
                                'evolution': '',
                                'prevolution': 'vulpix'}
