from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models



class AdressPlanes(models.Model):
    adress_UA = models.CharField(max_length=400)
    adress_RU = models.CharField(max_length=400)
    adress_EN = models.CharField(max_length=400)

    def __str__(self):
        return self.adress_RU

class LocationPlanes(models.Model):
    Location_UA = models.CharField(max_length=100)
    Location_RU = models.CharField(max_length=100)
    Location_EN = models.CharField(max_length=100)

    def __str__(self):
        return self.Location_RU


class CityPlanes(models.Model):
    city_standart_UA = models.CharField(max_length=30, unique=True)
    city_standart_RU = models.CharField(max_length=30, unique=True)
    city_standart_EN = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.city_standart_RU

class ContractorPlanes(models.Model):
    Contractor_UA = models.CharField(max_length=100)
    Contractor_RU = models.CharField(max_length=100, unique=True)
    Contractor_EN = models.CharField(max_length=100)

    def __str__(self):
        return self.Contractor_RU


class TypePlanes(models.Model):
    typeRU = models.CharField(max_length=40, unique=True)
    typeEN = models.CharField(max_length=40, unique=True)
    typeUA = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.typeRU

class FormatPlanes(models.Model):
    format = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.format

class SidePlanes(models.Model):
    side = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.side

class Totalplanes(models.Model):
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    doors = models.CharField(max_length=40)
    Self_number = models.CharField(max_length=40)
    Razom_number = models.IntegerField(unique=True)
    type = models.ForeignKey(TypePlanes, on_delete=models.CASCADE)
    format = models.ForeignKey(FormatPlanes, on_delete=models.CASCADE)
    OTS = models.CharField(max_length=20)
    GRP = models.CharField(max_length=20)
    adress = models.ForeignKey(AdressPlanes, on_delete=models.CASCADE)
    house = models.CharField(max_length=20)
    city_standart = models.ForeignKey(CityPlanes, on_delete=models.CASCADE)
    side = models.ForeignKey(SidePlanes, on_delete=models.CASCADE)
    loc = models.ForeignKey(LocationPlanes, on_delete=models.CASCADE)
    Contractor = models.ForeignKey(ContractorPlanes, on_delete=models.CASCADE)
    route = models.IntegerField()
    imagePhoto = models.ImageField(upload_to='OhhRazom/image/photo', default='OhhRazom/image/photo/1.jpg')
    imageShema = models.ImageField(upload_to='OhhRazom/image/shema', default='OhhRazom/image/shema/1.jpg')

    def __str__(self):
        return str(self.Razom_number) + " " + str(self.Self_number)

class Allagancy(models.Model):
    Agancy = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.Agancy

class Client(models.Model):
    client = models.CharField(max_length=50, unique=True)
    agancy = models.ForeignKey(Allagancy,on_delete=models.PROTECT)
    founder = models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
        return self.client

class Rk(models.Model):
    RK = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.RK

class Story(models.Model):
    rk = models.ForeignKey(Rk, on_delete=models.CASCADE)
    story = models.CharField(max_length=100)
    color = models.CharField(max_length=15, default="#191970")
    def __str__(self):
        return str(self.story)

class RkCompany(models.Model):
    rk = models.ForeignKey(Rk, on_delete=models.CASCADE)
    Razom_number = models.ForeignKey(Totalplanes, on_delete=models.CASCADE)
    Grade = models.IntegerField(null=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.rk) + " " + str(self.Razom_number) + " " + str(self.story)

class PermisionUsersClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

class ReachCity(models.Model):
    rk = models.ForeignKey(Rk, on_delete=models.CASCADE)
    city = models.ForeignKey(CityPlanes, on_delete=models.CASCADE)
    reach = models.CharField(max_length=40)
    frequency = models.CharField(max_length=20, default='0')
    period = models.CharField(max_length=20, default='0')
    def __str__(self):
        return str(self.city) + " " + str(self.rk)


class sm(models.Model):
    isnt = models.CharField(max_length=40)


