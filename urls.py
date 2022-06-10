from django.urls import path

from .CommandRK import CommandWork
from .views import *
from .viewsAdmin import *
from .viewsSetting import *
from .viewsFilters import *
from .ViewsCurrentRK import *
from .ChangeLenguage import *
from .AdminDo import *
from .viewSettingBody import *
from .viewRegister import *
from .viewsDeleteUser import *
from .viewClient import *
from .ClientDo import *
from .viewOutDoors import *
from .WorkBodyOutDoors import *
from .viewsData import *

urlpatterns = [
    path('', EnterView.as_view(), name='Enter'),
    path('update/doors/', UpdateDoorsPage.as_view(), name='UpdateDoorsGo'),
    path('ChangeLenguage', ChangeLengEnterPage.as_view()),
    path('Autentificate/', NavigationPermision.as_view(), name="Autentificate"),
    path('admin/setting/', SettingAdmin.as_view(), name="setting"),
    path('admin/', Admin.as_view(), name ='Admin'),
    path('admin/<str:flag>', WorkAdminPage.as_view()),
    path('account/exit/', LogOut.as_view(), name='Logut'),
    path('filter/<str:type>', Filter.as_view()),
    path('admin/setting/<str:utils>', SettingUtils.as_view()),
    path('admin/setting/<str:utils>/<str:RK>', ThisRK.as_view()),
    path('admin/rk/setting/', WorkCurrentRK.as_view(), name='CurrentRK'),
    path('change/lenguage/set/', Lenguage.as_view(), name='ChangeLenguage'),
    path('admin/rk/setting/<str:utils>', CommandWork.as_view()),
    path('admin/setting/account/create/', TransmitSetting.as_view()),
    path('account/register/', RegisterPage.as_view(), name='Register'),
    path('account/register/back', BackToSetting.as_view()),
    path('admin/setting/account/delete/<int:idUser>', DeleteUser.as_view()),
    path('client/', ClientPage.as_view(), name='Client'),
    path('client/<str:flag>', WorkClientPage.as_view()),
    path('client/Grade/<str:point>',PassPoint.as_view()),
    path('admin/mark/<str:action>', AsyincDelete.as_view()),
    path('admin/export/Excel', ExportExcelAdmin.as_view()),
    path('client/export/Excel/<str:colorHead>', ExportExcelClient.as_view()),
    path('admin/out_doors/', OutDoorsPage.as_view(), name='outdoors'),
    path('config/ChangeLenguage', ChangeLenguageOut.as_view()),
    path('admin/out_doors/<str:flag>/<str:x>/<str:y>/<str:zoom>', WorkBodyOutDoors.as_view()),
    path('InputToDb/Finall/', ImportDBFinall.as_view()),
    path('InputToDb/City/', ImportDBCity.as_view()),
    path('InputToDb/Side/', ImportDBSide.as_view(), name='Side'),
    path('InputToDb/Format/', ImportDBFormat.as_view(), name='Format'),
    path('InputToDb/Type/', ImportDBType.as_view(), name='Type'),
    path('InputToDb/Contactor/', ImportDBContactor.as_view(), name='Contactor'),
    path('InputToDb/adress/', ImportDBadress.as_view()),
    path('InputToDb/loc/', ImportDBloc.as_view()),
    path('Change/Img/in/', FixProblem.as_view()),
]

"""
"""