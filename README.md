
This is a Reproducible Research Package utilizing [BART Ridership data](https://www.bart.gov/about/reports/ridership) that investigates the effects of COVID-19 on commute trips in Downtown San Francisco and Berkeley. This repository contains an installable package, `project_tools`, which contains relevant functions stored in `utils.py` and test cases in `/test`. Our analysis is comprised of four notebooks: `Mapping_Ridership.ipynb`, `Analysis_of_Ridership_of_Stations_with_Different_Land_Use.ipynb`, `Ridership_Standard_Deviation_Analysis.ipynb`, and `Modeling_Post_Covid_Ridership_Using_Pre_Covid_Data.ipynb`. The main analyses are compiled into a primary notebook `main.ipynb`. 

# Analysis
* `Mapping_Ridership.ipynb`: Interactive maps showing the ridership of particular stations.
* `Analysis_of_Ridership_of_Stations_with_Different_Land_Use.ipynb`: Finding ridership patterns before and after pandemic regarding various land use conditions.
* `Modeling_Post_Covid_Ridership_Using_Pre_Covid_Data.ipynb`: Machine learning model on predicting post-COVID ridership using pre-COVID ridership data.
* `Ridership_Standard_Deviation_Analysis.ipynb`: Identifying stations with high ridership variance.

# Installation

To install the package, please follow the command listed below on your terminal:\

* Create the bartproject environment: make env
* Install the project_tools module, navigate to the project_tools file and enter: pip install .
* Remove any previous figure or data files from the project directory: make clean
* Execute Jupyter Notebooks and create the figures and data: make all

# Testing and Automation

To test the data, enter the following commands in your terminal:\

* Activate the environment: conda activate bartproject
* Run all tests for the functions: pytest project_tools

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s23/project-Group23.git/HEAD?labpath=main.ipynb)

Link to the JupyterBook: https://ucb-stat-159-s23.github.io/project-Group23/
