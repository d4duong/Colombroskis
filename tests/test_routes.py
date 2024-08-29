# TODO: Write tests for each route to ensure they render correctly and handle input as expected
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Coding Adventure Game!" in response.data
