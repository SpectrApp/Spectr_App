# from dadata import Dadata
from app import app
import json
from catboost import CatBoostRegressor
import pandas as pd
import os

'''
def get_info_by_address(address: str):
    token = app.config['DADATA_API_KEY']
    secret = app.config['DADATA_SECRET_KEY']
    dadata = Dadata(token, secret)
    try:
        result = dadata.clean("address", address)
    except:
        result = None

    address_data = result
    if (address_data is None or 'qc_geo' not in address_data or address_data['qc_geo'] > 1):
        return None
    return address_data
'''


def parse_realty_form(form):
    '''
    Parse user input from form to dict
    '''

    parsed_data = dict()
    parsed_data["floor"] = form.floor.data
    parsed_data["floors_count"] = form.floors_total.data
    parsed_data["rooms_count"] = form.rooms.data
    parsed_data["total_m2"] = form.area_total.data
    parsed_data["price_per_m2"] = form.price_per_m2.data
    parsed_data["year_of_construction"] = form.year.data
    parsed_data["living_m2"] = form.area_living.data
    parsed_data["kitchen_m2"] = form.area_kitchen.data
    parsed_data["district"] = form.city_district.data.lower()
    if form.metro.data is not None and len(form.metro.data) > 0:
        parsed_data["underground"] = form.metro.data.lower()
    else:
        parsed_data["underground"] = "unspecified"
    parsed_data["city"] = form.city.data.lower()
    # for key in parsed_data.keys():
    #    parsed_data[key] = [parsed_data[key],]
    return parsed_data


def get_price_prediction(data):
    '''
    Get prediction based on user data
    '''
    model = CatBoostRegressor()      # parameters not required.
    path_to_model = os.path.abspath(os.path.join(
        'app', 'static', 'models', 'model2.cbm'))
    model.load_model(path_to_model)
    try:
        df = pd.DataFrame(data, index=[0])
        result = round(model.predict(df)[0])
        
    except Exception as e:
        print("eee " + e.__str__())
        result = data
    return result
