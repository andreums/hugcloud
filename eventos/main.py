import json
import os


from datetime import datetime

from google.cloud import storage


storage_client = storage.Client()

# string event_id = 1;
#  google.protobuf.Timestamp event_time = 2;
#  google.protobuf.Timestamp process_time = 3;
#  string resource_id = 4;   // identificador inmueble
#  string user_id = 5;       // identificador del usuario
#  string country_code = 6;  // ISO3166
#  google.protobuf.Duration duration = 7;
#double item_price = 8;

def eventos(request):
  request_json = request.get_json(silent=True)  


  if request_json and 'eventId' in request_json \
    and 'eventTime' in request_json \
    and 'processTime' in request_json \
    and 'resourceId' in request_json \
    and 'userId' in request_json \
    and 'countryCode' in request_json \
    and 'duration' in request_json:

    payloadAsString = json.dumps(request_json)

    eventId   = request_json['eventId']
    eventTime = request_json['eventTime']
    processTime = request_json['processTime']
    resourceId = request_json['resourceId']
    userId  = request_json['userId']
    countryCode  = request_json['countryCode']
    duration   = request_json['duration']

    bucket_name = os.getenv('BUCKET_NAME')
    bucket = storage_client.bucket(bucket_name)

    new_blob = bucket.blob(f'airbnb/event-'+str(eventId)+'.json')
    new_blob.upload_from_string(payloadAsString)

    return json.dumps({'externalId': 'airbnb/event-'+str(eventId)+'.json'})

  else:
    return 'Error 500'
