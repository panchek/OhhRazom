import json
import os
from ..PlaceApp import PlaceBase
import traceback

class WorkFile:
    @staticmethod
    def outLenguage(file):
        path = os.path.join(PlaceBase.getPalce(), f'Files/Configfiels/{file}.json')
        try:
            with open(path, encoding="utf-8") as ReadJson:
                data = json.load(ReadJson)
                return data
        except Exception as e:
            return traceback.format_exc()