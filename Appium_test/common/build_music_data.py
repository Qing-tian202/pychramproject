import json
from tools import BASE_PATH

def build_music_data():
    with open(BASE_PATH / 'datas/test_music.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)

        return json_data