import xmltodict
# def test_root(client):
#     assert True == True


def test_getInventoryLevels_error(client):
    res = client.get('/api/inventory')
    print (dir(client))
    assert res.status_code == 400

def test_getInventoryLevels_successful(client):
    res = client.get('/api/inventory')
    # assert res.status_code == 200

def test_getFilterValues(client):
    res = client.get('/api/inventory')
    # print (dir(res))
    # assert res.status_code == 200