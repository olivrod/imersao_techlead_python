import requests
from typing import Tuple, Any

def do_GET() -> Tuple[int, Any]:
    url = "https://assets.breatheco.de/apis/fake/sample/project1.php"
    response = requests.get(url)
    return response.status_code, response.json()

def main() -> None:
    status_get, data_get = do_GET()
    # print(status_get, data_get)
    print(f"Projeto: {data_get['name']}, Imagem: {data_get['images'][0]}")

if __name__ == "__main__":
    main()


# ?> python3 format_json.py
# Projeto: 'eLearning', Imagem: 'https://intra.42.fr?image=178'

# {
#     "name": "Coursera eLearning",
#     "thumb": "https://unsplash.it/450/320?image=178",
#     "description": "The coolest elarning site on the planet",
#     "images": [
#         "https://unsplash.it/450/320?image=178",
#         "https://unsplash.it/450/320?image=179",
#         "https://unsplash.it/450/320?image=180",
#         "https://unsplash.it/450/320?image=181",
#     ],
# }