def test_create_client(client):

    response = client.post(
        "/clients",
        json={
            "name": "Deivid",
            "email": "deivid@email.com",
            "phone": "11999999999"
        }
    )

    assert response.status_code == 201