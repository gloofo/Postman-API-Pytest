from src.modules import *

def fake():
    fake = Faker()
    return fake

def data():
    with open("src/endpoints.yaml","r") as file:
        getData = yaml.load(file, Loader=yaml.FullLoader)
    return getData

