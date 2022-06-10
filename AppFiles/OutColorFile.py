import json
import os
from ..PlaceApp import PlaceBase


class WorkFiels:
    @staticmethod
    def colorFile(Key):
        path = os.path.join(PlaceBase.getPalce(), 'Files/Configfiels/ColorSite.json')
        with open(path) as ReadJson:
            try:
                data = json.load(ReadJson)
                return data[Key]
            except:
                pass

    @staticmethod
    def outToDB(file):
        path = os.path.join(PlaceBase.getPalce(), f'Files/DatatoDB/{file}.json')
        with open(path) as ReadJson:
            try:
                data = json.load(ReadJson)
                return data
            except:
                pass

