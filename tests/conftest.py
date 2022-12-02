import pytest
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    # app.config.update({
    #     "TESTING": True,
    # })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

# @pytest.fixture()
# def client():
#     app = create_app()
#     # app.config.update({"TESTING" : True})
#     return app.test_client()

# @pytest.fixture()
# def client():
#     app = create_app()
#     yield app.test_client()


# @pytest.fixture()
# def client():
#     app = create_app()
#     app.testing = True
#     yield app.test_client()



# @pytest.fixture()
# def client():
#     app = create_app
#     app.testing = True
#     yield app.test_client()

