update-submodules:
	git submodule update --recursive

download-mot-weights:
	./external/FastMOT/scripts/download_models.sh
