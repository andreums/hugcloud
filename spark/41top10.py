import sys
import os
import json
from datetime import datetime
from os.path import expanduser



from google.cloud import storage
from google.cloud import firestore

home = expanduser("~")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = home+"/credentials.json"


# from pyspark import SparkContext
# from pyspark.sql import SQLContext, Row
# from helpers import item_fields, parse_item
# from pyspark.sql import Row
# from pyspark.sql import SparkSession
# from pyspark.sql.types import *


# sc = SparkContext('local', 'airbnb')
# sq = SQLContext(sc)
# spark = SparkSession.builder.master("local").appName("SQL").getOrCreate()

db = firestore.Client()
storage_client = storage.Client()

datos  = []  
blobs  = storage_client.list_blobs("mibucketandreums",prefix="airbnb")

categories  = []

mPath = home+"/categories.json"

with open(mPath, 'r') as jsonFile:
    categories = json.load(jsonFile)

i = 0
for blob in blobs:
    if (i>20):
        break
    datos.append(json.loads(blob.download_as_string()))
    i+=1

for evento in datos:
    resourceId = evento.get("resourceId")
    doc_ref = db.collection('recursos').document(resourceId)
    recurso = doc_ref.get().to_dict()
    evento["category"]     = (recurso.get("category_id"))
    evento["resourceName"] = (recurso.get("resource_name"))
    evento["resourceId"] = (recurso.get("resource_id"))


    print(evento)
    

# datosJson = (json.dumps(datos))
# df = spark.createDataFrame(list(map(lambda x: Row(words=x), datos)))

# fila = df.map(lambda r: ((r.resourceId, r.category), r.r))
# scoreAndLabels = predicciones \
#         .map(lambda r: ((r.user, r.product), r.rating)) \
#         .join(ratingsTuple) \
#         .map(lambda tup: tup[1])

