<img src="https://upload.wikimedia.org/wikipedia/fr/thumb/6/6c/Logo_Universit%C3%A9_Rennes_1_.svg/1280px-Logo_Universit%C3%A9_Rennes_1_.svg.png" height="100px"/>


# PROJECT BS2

## Study of graphs of interactions

**UE BS2**

*Enora CORLER and Léa BEAULIEU - M2 BIS*


This project is dedicated to the study of graphs of interactions between proteins, by writting tools to manipulate these graphs, and to introduce into these graphs a notion of interaction between protein domains.

Scripts :
* **tp.py** : python file containing the main functions
* **test.py** : python file containing tests for our functions

Additional files are put in ./Examples :
**Human_HighQuality.txt** : a test file containing interactions (more complex : 27276 interactions) ;
* **toy_example.txt** : a test file containing interactions (simpler : only 6 interactions) ;
* **false_file_example-1.txt** to **false_file_example-4.txt** : files based on the *toy_example.txt* file which are not correctly written (empty file, wrong numbers of line/interactions/columns) ;
* **toy_example_to_clean.txt** : example file with homo-dimers and repetitions which is used in input to generate a cleaned file in output ;
* **toy_example_with_3_CC.txt** : example file based on toy_example.txt with 3 componected components.

## Credits 

* *Protein-protein interaction networks and graph theory* - **E. BECKER** (Bioinformatic master's degree courses)
* *Python 3.10.7 documentation* - https://docs.python.org/3/
* *Cours de Python* - **Patrick Fuchs and Pierre Poulain**
