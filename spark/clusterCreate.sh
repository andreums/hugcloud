#!/bin/bash

gcloud dataproc clusters create clusterhugairbnb3 \
--region us-east1 \
--single-node \
--metadata 'PIP_PACKAGES=google-cloud==0.34.0 google-cloud-storage==1.19.1 google-cloud-firestore==1.6.0 google-cloud-error-reporting==0.33.0' 