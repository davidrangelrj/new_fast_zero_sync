from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero_new.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (afirma)
    assert response.json() == {'message': 'Ola mundo!'}
