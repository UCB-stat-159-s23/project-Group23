.ONESHELL:
SHELL = /bin/bash


#env - creates and configures the environment.
.PHONY : env
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate notebook
	conda install ipykernel
	python -m ipykernel install --user --name make-env --display-name "Project Kernel"