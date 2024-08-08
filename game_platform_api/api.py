import logging
import requests
from models import Room, Game
from utils import setup_logging

# Инициализация логирования
setup_logging()

# Получаем логгер для использования в этом модуле
logger = logging.getLogger(__name__)

class GamePlatformApi:
    def __init__(self, API_URL='http://127.0.0.1:8000/api/'):
        self.API_URL = API_URL

    def __make_request(self, method, endpoint, token=None, data=None):
        url = f'{self.API_URL}{endpoint}'
        headers = self.__get_headers(token) if token else {}
        
        response = requests.request(method, url, headers=headers, json=data)
        logger.info(f"Request {method} {url} returned status {response.status_code}")
        if response.status_code in [200, 201]:
            return response.json()
        else:
            logger.error(f"Request {method} {url} failed with status {response.status_code}: {response.text}")
            response.raise_for_status()
    
    def __get_headers(self, token):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }


    def room_create(self, wallet_address: str, payload: list[str], bet):
        data = {
            'wallet_address': wallet_address,
            'name_room': payload[3],
        }
        #room = Room(room_id=room_data['id'], creator=User(room_data['creator']['username'], 
        #                                                  room_data['creator']['id']), payload=room_data['payload'])
        return self.__make_request('POST', 'rooms/create-room/', data=data)


    def get_rooms(self, token: str) -> list:
        rooms_data = self.__make_request('GET', 'rooms/', token)
        
        return rooms_data
    
    def thimbles_game_create(self, player: str, payload, bet) -> dict:
        
        data = {
            'room_id': payload[3],
            'bet': float(bet),
            'choice': int(payload[4]),
            'player_wallet': player

        }
        try:
            res = self.__make_request('POST', 'games/create-game/', data=data)
        except Exception as e:
            return 'no'
        return res
    def get_my_rooms(self, wallet_address: str):
        data = {
            'wallet_address': wallet_address
        }
        rooms_json = self.__make_request('GET', 'rooms/my-rooms/', data=data)
        rooms = []
        for room_json in rooms_json:
            room = Room(room_json['creator_wallet'], room_json['name'], room_json['id'])
            rooms.append(room)
        return rooms

    def get_games_in_room(self, room_id: int):
        data = {
            'room_id': room_id
        }
        games_json = self.__make_request('GET', 'games/games-in-room/', data=data)
        games = []
        for game_json in games_json:
            game = Game(
                game_id=game_json['id'],
                room_id=game_json['room_id'],
                player=game_json['player'],
                choice=game_json['choice'],
                bet=game_json['bet'],
                winner=game_json['winner'],
                disc=game_json['disc']
            )
            games.append(game)
        return games

    def get_my_games(self, wallet: str):
        data = {
            "player_wallet": wallet
        }
        games_json = self.__make_request('GET', 'games/my-games/', data=data)
        games = []
        for game_json in games_json:
            game = Game(
                game_id=game_json['id'],
                room_id=game_json['room_id'],
                player=game_json['player'],
                choice=game_json['choice'],
                bet=game_json['bet'],
                winner=game_json['winner'],
                disc=game_json['disc']
            )
            games.append(game)
        return games