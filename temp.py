# coding=utf-8
import os
from restAuth import settings

print os.environ  # словарь переменных окружения. Изменяемый (можно добавлять и удалять переменные окружения).

print os.getcwd() #текущая рабочая директория.
template_name = 'net/php'
print os.path.join(settings.BASE_DIR, 'static', template_name,'vbv')
print os.path.join(os.getcwd(),'vasa','1.txt')
print os.path.dirname(os.getcwd())
print os.path.dirname(os.path.abspath(__file__))
print os.path.dirname(__file__)