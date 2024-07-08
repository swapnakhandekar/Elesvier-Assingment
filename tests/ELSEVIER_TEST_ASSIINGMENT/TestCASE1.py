

import requests
import pytest

# Constants
API_KEY = "82a01f82-5904-4ddd-9bd8-66dcdde64a9b"  # api key to access
BASE_URL = "https://api.elsevierpure.com/ws/api"  # url for website

# Fixtures
@pytest.fixture(scope="module")
def headers():
    return {
        "accept": "application/json",
        "api-key": API_KEY,
        "Content-Type": "application/json"
    }

@pytest.fixture(scope="module")
def create_external_organization(headers):
    url = f"{BASE_URL}/external-organizations"
    data_to_send = {
        "name": {"en_US": "External Organization by Swapna"}
    }
    api_response = requests.put(url, headers=headers, json=data_to_send)
    assert api_response.status_code == 201
    return api_response.json()

# Tests
def test_create_external_organization(create_external_organization):
    organization = create_external_organization
    assert "uuid" in organization
    assert organization["name"]["en_US"] == "External Organization by Swapna"

def test_retrieve_external_organization(headers, create_external_organization):
    uuid = create_external_organization["uuid"]
    url = f"{BASE_URL}/external-organizations/{uuid}"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

    print(response.status_code)

    organization = response.json()
    assert organization["uuid"] == uuid
    assert organization["name"]["en_US"] == "External Organization by Swapna"
    print(organization["name"]["en_US"])

def test_create_external_organization_with_optional_fields(headers):
    url = f"{BASE_URL}/external-organizations"
    payload = {
        "name": {"en_US": "My external organization with optional fields"}
    }
    response = requests.put(url, headers=headers, json=payload)
    assert response.status_code == 201

    organization = response.json()
    assert "uuid" in organization
    assert organization["name"]["en_US"] == "My external organization with optional fields"
    print(organization["name"]["en_US"])

