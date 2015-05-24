from api.endpoints import AllegroEndpoints
from credentials import API_KEY, LOGIN, PASSWORD


if __name__ == '__main__':
    api = AllegroEndpoints(API_KEY, LOGIN, PASSWORD)
