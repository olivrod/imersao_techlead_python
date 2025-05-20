import requests
from typing import Tuple, Any

def do_GET() -> Tuple[int, Any]:
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    return response.status_code, response.json()

def do_POST() -> Tuple[int, Any]:
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(url, json=payload)
    return response.status_code, response.json()

def main() -> None:
    status_get, data_get = do_GET()
    print(status_get, data_get)

    status_post, data_post = do_POST()
    print(status_post, data_post)

if __name__ == "__main__":
    main()
