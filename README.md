#**CSC1034: Practical 2**

#### This package allows analysis and display of proteins from Uniprot. It has been done as a part of CSC1034 module.

## Languages and modules used in the project:
* Python (3.7.4)
* Biopython	(1.74)
* Matplotlib (3.1.1)
* Pytest (5.2.1)
* Pyparsing (2.4.2)

##Launch
This project can be accessed from my Project 2 repository on Gitlab (URL).
To edit it, you will need to fork and then clone it into your local environment in whatever IDE for Python you're using. 
Use Pipenv (e.g. `pipenv --python 3.7`) to create a Pipfile and a virtual environment.

##Functionalities
This project can be used to access the names of all proteins in a database, see the average length of their sequences or 
to create a bar chart of average protein lengths by taxa. To do this, either call a suitable function from uniplot.py file in the terminal or run the file itself, 
after specifying which function to call within it. The available functions are as follows:
1) To print the list of protein names use: uniplot.py 'list'
2) To calculate the average length of all proteins use: uniplot.py 'average'
3) To plot a bar chart depicting protein lengths by taxa use: uniplot.py 'plot_average_by_taxa'

E.g. running `pipenv run python uniplot.py plot_average_by_taxa`, in the terminal,
 will display something like this: 
 ![A bar chart](./resources/average_plot.jpg)
 
 ##Sources
 This Project is based on an outline and a tutorial 'How Receptive Are You?' by Philip Lord of Newcastle University.
 The tutorial can be accessed here: https://internal.cs.ncl.ac.uk/modules/2019-20/csc1034/part-1/project-2/csc1034-project-2_web.html

