import os
import pytest
from app import create_app, db


@pytest.fixture(scope='module')
def client():
    # arrange
    filename = '/tmp/fresh_test.db'
    db_path = 'sqlite:///' + filename

    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': db_path})
    with app.test_client() as cli:
        with app.app_context():
            db.create_all()
            yield cli

    # cleanup
    os.remove(filename)


def test_insert_admin_user(client):
    # arrange
    user_dict = {'username': 'admin', 'email': 'admin@example.com'}
    # act
    r = client.post('/users', json=user_dict)
    # assert
    assert r.status_code == 200
    assert r.json == {'id': 1, 'username': 'admin', 'email': 'admin@example.com'}


def test_insert_and_get_user(client):
    # arrange
    username = 'newuser'
    user_dict = {'username': username, 'email': f'{username}@example.com'}
    client.post('/users', json=user_dict)
    # act
    res = client.get(f'/users/{username}')

    # assert
    assert res.status_code == 200
    assert res.json == {'id': 2, 'username': username, 'email': f'{username}@example.com'}


@pytest.mark.parametrize("username", ['name1', 'name2', 'name3'])
def test_insert_and_get_user_param(client, username):
    # arrange
    user_dict = {'username': username, 'email': f'{username}@example.com'}
    client.post('/users', json=user_dict)
    # act
    res = client.get(f'/users/{username}')

    # assert
    assert res.status_code == 200
    assert res.json['username'] == username
    assert res.json['email'] == f'{username}@example.com'
