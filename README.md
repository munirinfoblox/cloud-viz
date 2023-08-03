## Introduction
This is a tool written in Python that generates architectural diagram of a cloud environment or a kubernetes cluster or part of it.
This tool requires to be fed into the information from the cloud and then it can generate the diagram.

## Setup python environment
`python3 -m venv env`
`source env/bin/activate`
`pip install --upgrade pip && pip install -r requirements.txt`

## Generate Diagram of an AWS account
* Run the `steampipe` application and query the appropriate objects and attributes that you want to visualize
* Convert that SQL result to appropriate `yaml` or `json` to feed into the diagram generator.
* Run the diagram generator with the following command

  ```python generator.py```