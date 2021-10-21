import os
import pytest
from app import create_app, db
from users.daos.user_dao import add_user, get_user_by_name


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
    n = 'admin'
    m = 'admin@example.com'
    # act
    add_user(n, m)
    # assert
    stored_user = get_user_by_name(n)
    assert stored_user.username == 'admin'

'''
def test_insert_user_jose(client):
    # arrange
    n = 'jose'
    m = 'jose@example.com'
    # act
    add_user(n, m)
    # assert
    stored_user = get_user_by_name(n)
    assert stored_user.username == 'jose'
'''


def test_insert_user_twice(client):
    # arrange
    n = 'raul'
    m = 'raul@example.com'
    # act
    add_user(n, m)
    # assert
    with pytest.raises(ValueError, match=r"User with name raul already in the DB"):
        add_user(n, 'raul@anothermail.com')




