webcam ?= /dev/video2

update-submodules:
	git submodule update --recursive

download-mot-weights:
	./external/FastMOT/scripts/download_models.sh

build:
	cd external/FastMOT && \
	docker build -t fastmot:latest . --build-arg TRT_IMAGE_VERSION=21.05
	docker run --gpus all --rm -v ./external/FastMOT:/usr/src/app/FastMOT -e TZ=$(cat /etc/timezone) fastmot:latest /bin/bash -c "cd fastmot/plugins && make"

run:
	xhost local:root
	docker run --gpus all --rm -v ./external/FastMOT:/usr/src/app/FastMOT --device=$(webcam):/dev/video0:rwm -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix${DISPLAY} -e TZ=$(cat /etc/timezone) fastmot:latest /bin/bash -c "python3 app.py --input-uri /dev/video0 --mot --show"
