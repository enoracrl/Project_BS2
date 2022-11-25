<img src="https://upload.wikimedia.org/wikipedia/fr/thumb/6/6c/Logo_Universit%C3%A9_Rennes_1_.svg/1280px-Logo_Universit%C3%A9_Rennes_1_.svg.png" height="100px"/>
# PROJECT BS2

**UE BS2**

*Enora CORLER and Léa BEAULIEU - M2 BIS*

## Study of graphs of interactions

This project is dedicated to the study of graphs of interactions between proteins, by writting tools to manipulate these graphs, and to introduce into these graphs a notion of interaction between protein domains. We can use this code to also work with graph visualization with some additional modules such as matplotlib and networkx.


![alt text](https://github.com/enoracrl/Project_BS2/blob/ad7e867e07980f579b3b512e7c86ef483c7507a3/barabasi-albert_graph.png)

![alt text](https://github.com/enoracrl/Project_BS2/blob/efd063e27c90e9a6af51ae892363fc335a654ede/erdos-renyi_graph.png)

## Lauch

{% filename %}python interactome.py [-h] [-fo FILE_OUT] [-d D] [-min DMIN] [-max DMAX] [-p P] [-m M_MAX] filename protein degree{% endfilename %}

`positional arguments: '\n'
  filename              name of input graph of interaction file '\n'
  protein               name of the protein you want to study locally '\n'
  degree                degree that others proteins have too

optional arguments:
  -h, --help            show this help message and exit
  -fo FILE_OUT, --file_out FILE_OUT
                        name of output graph of interaction file cleaned
  -d D                  number of digits to round-off
  -min DMIN             minimum degree for the rank for histogram_degree
  -max DMAX             maximumx degree for the rank for histogram_degree
  -p P, --proba P       probability that a node is connected to another for
                        Erdös-Renyi
  -m M_MAX, --maximal_degree M_MAX
                        number of maximum nodes for the Barabasi-Albert graph`

You can test this program on some examples files that are in the *Examples/* folder, but you can also provides your own !

Make sure that you interaction file is readable (.txt format for example), not empty, with a couple of interactions per line separated by a tabulation or a space like that :

`6 '\n'
A B'\n'
A C'\n'
B D'\n'
D E'\n'
D F `

Don't worry if you forgot to put the number of interactions of your graph (first line) or you put interactions twice or homo-dimers : our programm will clean your file !

## Files 

Scripts :
* **tp.py** : python file containing the main functions of the first chapters 
* **test.py** : python file containing tests for our functions of the first chapters 
* **interactome.py** : python file containing the Interactome class with all our functions
* **test_interactome.py** : python file containing tests for our Interactome class
* **demo_with_interaction.py** : python file calling some of our methods with example files 

Additional files are put in ./Examples :
* **Human_HighQuality.txt** : a test file containing interactions (more complex : 27276 interactions) ;
* **toy_example.txt** : a test file containing interactions (simpler : only 6 interactions) ;
* **false_file_example-1.txt** to **false_file_example-4.txt** : files based on the *toy_example.txt* file which are not correctly written (empty file, wrong numbers of line/interactions/columns) ;
* **toy_example_to_clean.txt** : example file with homo-dimers and repetitions which is used in input to generate a cleaned file in output ;
* **toy_example_with_3_CC.txt** : example file based on toy_example.txt with 3 componected components.

## Credits 
* *Protein-protein interaction networks and graph theory* - **E. BECKER** (Bioinformatic master's degree courses)
* *Python 3.10.7 documentation* - (https://docs.python.org/3/)
* *Cours de Python* - **Patrick Fuchs and Pierre Poulain**
