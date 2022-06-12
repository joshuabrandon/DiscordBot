# Import
from datetime import datetime as dt
import pytz
import requests
import pandas as pd
import sys

# Read in and store Steam API key
api_file = open("SteamKey.txt","r")
api_key = api_file.readline()
api_file.close()

# Player Steam IDs
player_id = {
    "Bleu": 76561198014939291
    ,"Karnoff": 76561198025251571
    ,"luppidd": 76561198094922857
    ,"andyman14": 76561198202137419
    ,"Lavving": 76561197983942380
    ,"Mrak": 76561198073209374
}

player_names = list(player_id.keys())

def get_steam_game(player_name):
    steam_id = player_id.get(player_name)
    output = ""
    
    if steam_id != None:
        url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={}&steamids={}".format(api_key,steam_id)
        response_raw = requests.get(url).json()
        response_granular = response_raw['response']['players'][0]

        steam_name = response_granular["personaname"]

        game_name = response_granular.get("gameextrainfo")
        game_status = None

        if game_name != None:
            game_status = 1
            output = "{} (also known as {}) is currently playing {} on Steam!".format(player_name,steam_name,game_name)
        else:
            game_status = 0
            game_name = "No active game"
            output = "{} (also known as {}) is not playing anything on Steam right now.".format(player_name,steam_name,game_name)
    else:
        #output = "I have no idea who this is. Try one of these names: {}".format(sorted(list(player_id.keys()), key=str.lower))
        output = "I have no idea who this is. Try one of these names: {}".format(', '.join(player_names))
        
    
    return output