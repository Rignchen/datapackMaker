from os import listdir
from lib import choice

names = [i.removesuffix(".py") for i in listdir("script")]

script = listdir("script")[choice("Wich template do you want? ",names)]

