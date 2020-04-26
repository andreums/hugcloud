#!/bin/bash

gcloud dataproc jobs submit pyspark 41top10.py \
 --cluster clusterhugairbnb3 \
 --region us-east1 \
 --files=helpers.py