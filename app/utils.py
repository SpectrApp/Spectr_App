from dadata import Dadata
from app import app
import json

def get_info_by_address(address : str):
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