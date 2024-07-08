import requests

# Constants
API_KEY = "82a01f82-5904-4ddd-9bd8-66dcdde64a9b"
BASE_URL = "https://api.elsevierpure.com/ws/api"

# Helper functions
def create_external_organization(headers):
    url = f"{BASE_URL}/external-organizations"
    payload = {
        "name": {"en_US": "External Organization By Swapna"},
        "Birth-day": 29101994

    }
    response = requests.put(url, headers=headers, json=payload)
    print(response.json()["name"]["en_US"])
    if response.status_code == 201:
        return response.json()
    else:
        return None

def retrieve_external_organization(headers, uuid):
    url = f"{BASE_URL}/external-organizations/{uuid}"
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def create_external_organization_with_optional_fields(headers):
    url = f"{BASE_URL}/external-organizations"
    payload = {
        "name": {"en_US": "My external organization with optional fields"},
        "workflow": {'step': 'forApproval', 'description': {'en_US': 'For not approval', 'da_DK': 'Til godkendelse', 'nl_NL': 'Ter goedkeuring'}}
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 201:
        return response.json()
    else:
        return None
#
# # Tests
# def test_create_external_organization():
#     headers = {
#         "accept": "application/json",
#         "api-key": API_KEY,
#         "Content-Type": "application/json"
#     }
#     organization = create_external_organization(headers)
#     assert organization is not None
#     assert "uuid" in organization
#     assert organization["name"]["en_US"] == "My external organization"
#
# def test_retrieve_external_organization():
#     headers = {
#         "accept": "application/json",
#         "api-key": API_KEY,
#         "Content-Type": "application/json"
#     }
#     organization = create_external_organization(headers)
#     assert organization is not None
#     uuid = organization["uuid"]
#     retrieved_organization = retrieve_external_organization(headers, uuid)
#     assert retrieved_organization is not None
#     assert retrieved_organization["uuid"] == uuid
#     assert retrieved_organization["name"]["en_US"] == "My external organization"
#
# def test_create_external_organization_with_optional_fields():
#     headers = {
#         "accept": "application/json",
#         "api-key": API_KEY,
#         "Content-Type": "application/json"
#     }
#     organization = create_external_organization_with_optional_fields(headers)
#     assert organization is not None
#     assert "uuid" in organization
#     assert organization["name"]["en_US"] == "My external organization with optional fields"
#     # assert organization["description"]["en_US"] == "An optional description"

# Run the tests
# test_create_external_organization()
# test_retrieve_external_organization()
# test_create_external_organization_with_optional_fields()
created_Data = create_external_organization(headers={
        "accept": "application/json",
        "api-key": API_KEY,
        "Content-Type": "application/json"
    })

print(created_Data[")

Retrieve_Data = retrieve_external_organization(headers={
        "accept": "application/json",
        "api-key": API_KEY,
        "Content-Type": "application/json"
    }, uuid= created_Data["uuid"])

print(Retrieve_Data["name"])


print(created_Data.items())

optional_field = create_external_organization_with_optional_fields(headers={
        "accept": "application/json",
        "api-key": API_KEY,
        "Content-Type": "application/json"
    })
print(optional_field["workflow"])