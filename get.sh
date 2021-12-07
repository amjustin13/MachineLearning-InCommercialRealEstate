#!/bin/bash
pip install gdown
gdown https://drive.google.com/drive/folders/1clmb7pAAfWyVyjdFbaJYxTMeeHpbAunm?usp=sharing  -O /srv/testserver/modelFolder --folder
git clone https://github.com/EC528-ML-RealEstate/ML-Services.git
mv modelFolder ML-Services
cd ML-Services
docker build -t webapp-build:latest .
docker run --name $1 -d webapp-build
docker exec -it $1 python app.py
