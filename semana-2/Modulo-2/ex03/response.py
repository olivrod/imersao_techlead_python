import sys
import requests
from requests.exceptions import RequestException

def main() -> None:
    if len(sys.argv) != 2:
        print("Comando necessita de um parametro: python3 response.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        print(f"{response.status_code} {response.reason}")
    except RequestException as e:
        print(f"Error: {type(e).__name__}")
        sys.exit(1)
    except Exception as e:
        print(f"{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


# ?> python3 response.py https://www.google.com
# 200 OK
# ?> python3 response.py https://42.fr/unknown
# 404 Not Found
# ?> python3 response.py https://invalidaddress
# Error: ConnectError