def test_create_pet():

    response = client.post(
        "/pets",
        json={
            "name": "Rex",
            "species": "dog",
            "breed": "Labrador",
            "age": 5,
            "owner_id": 1
        }
    )

    assert response.status_code == 200