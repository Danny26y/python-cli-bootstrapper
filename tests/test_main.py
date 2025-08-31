import requests
import json

# Base URL of your API
BASE_URL = "http://localhost:8000"


def test_api():
    """Test the API endpoints"""

    # 1. Test root endpoint
    print("1. Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Response: {response.json()}\n")

    # 2. Test templates endpoint
    print("2. Getting available templates...")
    response = requests.get(f"{BASE_URL}/templates")
    print(f"Templates: {json.dumps(response.json(), indent=2)}\n")

    # 3. Create a FastAPI project
    print("3. Creating a FastAPI project...")
    project_data = {
        "name": "my_fastapi_app",
        "git_init": True,
        "use_venv": False,
        "license_type": "MIT",
        "template": "fastapi"
    }

    response = requests.post(
        f"{BASE_URL}/create",
        json=project_data
    )

    if response.status_code == 200:
        print(f"Project created: {json.dumps(response.json(), indent=2)}\n")
    else:
        print(f"Error: {response.text}\n")

    # 4. Create and download a Flask project
    print("4. Creating and downloading a Flask project...")
    project_data = {
        "name": "my_flask_app",
        "git_init": False,
        "use_venv": True,
        "license_type": "Apache",
        "template": "flask"
    }

    response = requests.post(
        f"{BASE_URL}/create-and-download",
        json=project_data
    )

    if response.status_code == 200:
        # Save the ZIP file
        with open("my_flask_app.zip", "wb") as f:
            f.write(response.content)
        print("Project downloaded as my_flask_app.zip\n")
    else:
        print(f"Error: {response.text}\n")

    # 5. Test health check
    print("5. Testing health check...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Health: {response.json()}\n")


if __name__ == "__main__":
    test_api()
#Test cases go here
