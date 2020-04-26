import json
import os

from datetime import datetime
from random import randint

from google.cloud import firestore

db = firestore.Client()

# string resource_id = 1;   // identificador inmueble
#  string resource_name = 2; // direccion del immueble
#  string category_id = 3;   // clase de inmueble
#  string provider_id = 4;   // persona que ofrece el el inmueble en alquiler
#  bool promotion = 5; 

def recursos2(request):
  request_json = request.get_json(silent=True)

  #print("REQUEST", request_json)
  

  if request_json and 'resourceId' in request_json \
    and 'resourceName' in request_json \
    and 'categoryId' in request_json \
    and 'providerId' in request_json \
    and 'promotion' in request_json:

    resourceId  = request_json['resourceId']
    resourceName= request_json['resourceName']
    categoryId  = request_json['categoryId']
    providerId  = request_json['providerId']
    promotion   = request_json['promotion']

    doc_ref = db.collection('recursos').document(resourceId)
    doc_ref.set({
      'resource_id': resourceId,
      'resource_name': resourceName,
      'category_id': categoryId,
      'providerId': providerId,
      'promotion': promotion,
      'created': datetime.utcnow().isoformat()
    }) 

    return json.dumps({'externalId': doc_ref.id})

  else:
    return 'Error 500'
