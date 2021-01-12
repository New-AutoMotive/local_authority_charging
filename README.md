# Local authority charging devices

This repository contains the codes necessary to investigate the uptake of public charging devices as well as EVs at local authority level. 

## Requirements

To run the analysis contained in this repository it is necessary to install Anaconda (download here: https://www.anaconda.com/products/individual), and follow the step by step guide outlined below. 

## Anaconda environment
Firstly, open the Anaconda prompt and navigate to where the `local_authority_charging` folder is stored on your local drive using the command\
\
`cd path/to/file`\
\
Then, to create and activate a specific environment for the project, run the following commands\
\
`conda create -y --name environment_name_you_like python=3.8` \
`conda activate environment_name_you_like`

## Required packages 
The `requirements.txt file` contains the list of the required packages to run the analysis. The file can be edited to include new packages which need to be included.
To install all the required packages, make sure the `environment_name_you_like` environment is running in the `local_authority_charging` folder. If not, repeat the above commands in the Anaconda prompt\
\
`cd path/to/file`.\
`conda activate environment_name_you_like`\
\
Then, install the packages by running\
\
`pip install -r requirements.txt`\
\
You will require ArcGIS for Python before processing the notebooks. To install this, run\
\
`conda install -c esri arcgis=1.8.3`\
\

## Jupyter Notebook 
To set the `environment_name_you_like` environment on your Jupyter Notebook, install `ipykernel` by typing in the Anaconda prompt\
 \
`conda install -c anaconda ipykernel`\
 \
Followed by\
 \
`python -m ipykernel install --user --name=environment_name_you_like`\
 \
Finally, in the Anaconda prompt running the `environment_name_you_like` environment in the `local_authority_charging` folder, type\
 \
`jupyter notebook`\
 \
And run the `EV and charging devices uptake.ipynb` Jupyter Notebook 
