import requests

BASE_URL = "http://localhost:8000"

def test_get_version():
    response = requests.get(f"{BASE_URL}/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_check_prime_2():
    response = requests.get(f"{BASE_URL}/check_prime/2")
    assert response.status_code == 200
    assert response.json() == {"number": 2, "is_prime": True}

def test_check_prime_3():
    response = requests.get(f"{BASE_URL}/check_prime/3")
    assert response.status_code == 200
    assert response.json() == {"number": 3, "is_prime": True}

def test_check_prime_4():
    response = requests.get(f"{BASE_URL}/check_prime/4")
    assert response.status_code == 200
    assert response.json() == {"number": 4, "is_prime": False}

def test_check_prime_0():
    response = requests.get(f"{BASE_URL}/check_prime/0")
    assert response.status_code == 200
    assert response.json() == {"number": 0, "is_prime": False}

def test_check_prime_negative():
    response = requests.get(f"{BASE_URL}/check_prime/-5")
    assert response.status_code == 200
    assert response.json() == {"number": -5, "is_prime": False}

def test_check_prime_large():
    response = requests.get(f"{BASE_URL}/check_prime/97")
    assert response.status_code == 200
    assert response.json() == {"number": 97, "is_prime": True}

def test_check_prime_non_integer():
    response = requests.get(f"{BASE_URL}/check_prime/1.5")
    assert response.status_code == 422  # Validation error

def test_check_prime_string():
    response = requests.get(f"{BASE_URL}/check_prime/abc")
    assert response.status_code == 422  # Validation error

def test_check_prime_boundary():
    response = requests.get(f"{BASE_URL}/check_prime/1")
    assert response.status_code == 200
    assert response.json() == {"number": 1, "is_prime": False}
