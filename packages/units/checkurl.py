import requests

def read_payloads(file_path):
    try:
        with open(file_path, 'r') as file:
            payloads = file.read().splitlines()
        return payloads
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading payload file '{file_path}': {e}")
        return []

def check_url(base_url, payload):
    test_url = f"{base_url}/{payload}"
    try:
        response = requests.get(test_url)
        if response.status_code == 200:
            print(f"[+] Payload successful: {test_url}")
            return True
        else:
            print(f"[-] Payload failed: {test_url}")
            return False
    except requests.RequestException as e:
        print(f"Error requesting URL '{test_url}': {e}")
        return False
