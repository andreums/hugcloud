import json
import os

from datetime import datetime
from random import randint

from google.cloud import firestore

db = firestore.Client()

def usuarios(request):
  request_json = request.get_json(silent=True)

  #print("REQUEST", request_json)
  

  if request_json and 'name' in request_json and 'email' in request_json and 'age' in request_json:
    name  = request_json['name']
    email = request_json['email']
    age   = request_json['age']

    doc_ref = db.collection('usuarios').document(email)
    doc_ref.set({
      'name'   : name,
      'email'  : email,
      'age'    : age,
      'created': datetime.utcnow().isoformat()
    }) 

    return json.dumps({'externalId': doc_ref.id})

  else:
    return 'Error 500'
