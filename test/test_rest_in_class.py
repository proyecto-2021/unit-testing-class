import os
import pytest
from app import create_app, db


@pytest.fixture(scope='module')
def client():
    # arrange
    filename = '/tmp/fresh_test.db'
    db_path = 'sqlite:///' + filename

    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': db_path})
    with app.test_client() as test_client:
        with app.app_context():
            db.create_all()
            yield test_client

    # cleanup
    os.remove(filename)


def test_post_new_user(client):
    # arrange
    user = {'username': 'user1', 'email': 'user1@example.com'}
    # act
    resp = client.post('/users', json=user)
    # assert
    assert resp.status_code == 200
    assert 'id' in resp.json.keys()
    assert resp.json['username'] == 'user1'
    assert resp.json['email'] == 'user1@example.com'


def test_user_raul_exists_after_post(client):
    # arrange
    name = 'raul'
    mail = f'{name}@example.com'
    user = {'username': name, 'email': mail}
    # act
    client.post('/users', json=user)
    resp = client.get(f'/users/{name}')
    # assert
    assert resp.status_code == 200
    assert 'id' in resp.json.keys()
    assert resp.json['username'] == name
    assert resp.json['email'] == mail


def test_user_pedro_exists_after_post(client):
    # arrange
    name = 'pedro'
    mail = f'{name}@gmail.com'
    user = {'username': name, 'email': mail}
    # act
    client.post('/users', json=user)
    resp = client.get(f'/users/{name}')
    # assert
    assert resp.status_code == 200
    assert 'id' in resp.json.keys()
    assert resp.json['username'] == name
    assert resp.json['email'] == mail


@pytest.mark.parametrize("name, mail",
    [('juan', 'juan@hotmail.com'), ('jose', 'jose@gmail.com'), ('user3', 'user3@gmail.com')])
def test_user_exists_after_post(client, name, mail):
    # arrange
    user = {'username': name, 'email': mail}
    # act
    client.post('/users', json=user)
    resp = client.get(f'/users/{name}')
    # assert
    assert resp.status_code == 200
    assert 'id' in resp.json.keys()
    assert resp.json['username'] == name
    assert resp.json['email'] == mail

