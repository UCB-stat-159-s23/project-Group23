.ONESHELL:
SHELL = /bin/bash


#env - creates and configures the environment.
.PHONY : env
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate notebook
	conda install ipykernel
	python -m ipykernel install --user --name bartproject --display-name "Bart Project Kernel"
	
	
#html - build the JupyterBook normally
.PHONY : html	
html :
	jupyter-book build .
	
	
#all - run all jupyter notebooks
.PHONY : all
all:
	conda activate bartproject
	jupyter execute *.ipynb
	
	
#clean - clean up the figures and _build folders.
.PHONY : clean
clean :
	rm -rf figures/*
	rm -rf _build/*