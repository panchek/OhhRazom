import random

from django.contrib.auth.models import User

from ..models import Client

class EnterInSystem:
    @staticmethod
    def createUser(idClient):
        dictAlfabet = {
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h',
            '9': 'i',
            '10': 'j',
            '11': 'k',
            '12': 'l',
            '13': 'm',
            '14': 'n',
            '15': 'o',
            '16': 'p',
            '17': 'q',
            '18': 'r',
            '19': 's',
            '20': 't',
            '21': 'u',
            '22': 'v',
            '23': 'w',
            '24': 'x',
            '25': 'y',
            '26': 'z'
        }

        strOut = ""
        for i in range(10):
            tmp = random.randint(1, 100)
            if tmp % 2 == 0 :
                strOut+= str(random.randint(1, 9))
            else:
                cur = random.randint(1, 26)
                strOut+= dictAlfabet[str(cur)]
        while True:
            randomClient = str(random.randint(100, 500))
            InfClient = Client.objects.get(id=int(idClient))
            LoginOut = str(InfClient.client) + randomClient
            try:
                User.objects.get(username=LoginOut)
            except:
                break
        return {
            "Login" : LoginOut,
            "Password": strOut
        }
