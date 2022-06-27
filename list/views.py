import json
from django.shortcuts import render
import requests as HTTP_Client
import random
import os
from dotenv import load_dotenv

load_dotenv()

valid = os.environ['apikey']


def index(request):
    return render(request, 'list/index.html')


def neogeo(request):
    summary = f'https://api.rawg.io/api/platforms/12?key={valid}'
    games = f'https://api.rawg.io/api/games?key={valid}&platforms=12'
    API_response1 = HTTP_Client.get(summary)
    neogeosummary = API_response1.json()
    description = neogeosummary['description']
    game_count = neogeosummary['games_count']
    API_response2 = HTTP_Client.get(games)
    game_list = []

    for i in range(1):
        rangame = random.randint(1, 16)
        nggames = API_response2.json()
        games = nggames['results'][rangame]['name']
        game_list.append(games)
    return render(request, 'list/neogeo.html', {'info': description, 'game': game_list, 'amount': game_count})


def snes(request):
    summary = f'https://api.rawg.io/api/platforms/79?key={valid}'
    games = f'https://api.rawg.io/api/games?key={valid}&platforms=79'
    API_response3 = HTTP_Client.get(summary)
    jsonsummary = API_response3.json()
    description = jsonsummary['description']
    snes_count = jsonsummary['games_count']
    API_response4 = HTTP_Client.get(games)
    snes_game_list = []

    for x in range(1):
        randgame = random.randint(1, 16)
        newgame = API_response4.json()
        snesgame = newgame['results'][randgame]['name']
        snes_game_list.append(snesgame)
    return render(request, 'list/snes.html', {'info': description, 'game': snes_game_list, 'amount': snes_count})
