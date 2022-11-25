"""Object interactome which allows to manipulate graphs, and to introduce into these graphs a
notion of interaction between protein domains.

Usage: Visualization and manipulation of graphs

"""

__authors__ = ("Enora CORLER", "Léa BEAULIEU")
__contact__ = ("enora.corler@etudiant.univ-rennes1.fr", "lea.beaulieu@etudiant.univ-rennes1.fr")
__date__ = "25/11/2022"

'''
Importation of necessary modules :
    - numpy : used to create matrix
    - itertools : allows to implement a various number of iterators
    - os : allows to manipulate files
    - argparse : 
'''

import itertools
import argparse
import os
import numpy as np

class Interactome :
    '''
    A class to explore the interactome.

    Methods :
        We read the file for a reasonable number of times to construct the object,
        and then manipulate the data structure as we want
    '''
    def __init__(self, file, fileout=None) :
        '''
        Construct all the necessary attributes for the interactome object. We also
        verify if our file is correctly formarted ;
            if not, we clean it.
        Args :
            a tabulate file, .txt format
            a name of an output file, .txt format
        Attributes :
            int_list : the list of all interactions
            int_dic : a dictionnary that regroups all the interactions
            self.matrix : the adjacency matrix of the interactions
        Parameters :
            int_list : the list of all interactions
            int_dic : a dictionnary that regroups all the interactions
            self.matrix : the adjacency matrix of the interaction
        Output :
            fileout : a tabulate file based on the input file, cleaned from
                all repetitions/homo-dimers ;
            CC_of_[file].txt : a tabulate file with :
                    - one lign by connected component ;
                    - the lenght of it is the first element of the line ;
                    - the list of all vertices that composes the connected component.
        '''
        if file is None :
            raise ValueError("Please put your graph of interactions in input as a file !")
        file_name, file_extension = os.path.splitext(file)
        self.file = file
        self.matrix = []
        int_dict = {}
        int_list = []
        text = []
        number_interactions = ""
        with open(file, 'r', encoding="utf-8") as file_reader :
            text = [line.split() for line in file_reader]
            if text != [] :
                number_interactions = text[0][0]
                for line in text[1:] :
                    # removing lines with a number of cols > 2
                    if len(line) % 2 == 0:
                        int_list.append(tuple(line))
                        int1, int2 = line
                        if int1 not in int_dict :
                            int_dict[int1] = [int2]
                        else :
                            int_dict[int1].append(int2)
                        if int2 not in int_dict :
                            int_dict[int2] = [int1]
                        else :
                            int_dict[int2].append(int1)
        # verifying if the interactome is clean
        count = sum([len(elem) for elem in text[1:]])
        cleaned = False
        if number_interactions.isnumeric() is True :
            if len(text[1:]) == int(number_interactions) and count % 2 == 0 :
                # if the file is not empty, with a correct number of interactions/lines/columns
                cleaned = True
        if cleaned is False :
            # cleaning interactome
            for i in range(1, len(int_list)-1):
                if int_list[i][0] == int_list[i][1]:
                    del int_list[i]  # removing homo-dimers
            clean_text = list(l for l, _ in itertools.groupby(int_list))
            for i in clean_text:
                for j in reversed(clean_text):
                    if i == tuple(reversed(j)) :
                        clean_text.remove(j)  # removing duplicates
            # modifying initial number of interactions by the newest value
            clean_text.insert(0,str(len(clean_text)))
            # we write into a new tabulated file the modifications
            if fileout is None :
                fileout = file_name+"_cleaned"+file_extension
            with open(fileout, "w+", encoding="utf-8") as file_writer:
                file_writer.write(clean_text[0]+"\n")
                for i in clean_text[1:]:
                    file_writer.write(str(i[0]) + "\t" + str(i[1])+"\n")
            cleaned = True
        self.int_list = int_list
        self.int_dict = int_dict
        self.file_name = file_name
        self.file_extension = file_extension

    # ACCESSEURS
    def get_int_list(self) -> list :
        '''
        Return the instance variable of the list of interactions.
        '''
        return self.int_list

    def get_int_dict(self) -> dict :
        '''
        Return the instance variable of the dictionnary of interactions.
        '''
        return self.int_dict

    def get_mat(self) -> np.ndarray :
        '''
        Return the instance variable of the matrix of interactions
        '''
        self.matrix = self.read_interaction_file_mat()[1]
        return self.matrix

    # METHODS OF THE CLASS

    def read_interaction_file_mat(self) -> tuple :
        '''
        Return an adjacency matrix that show 1 every time there is an interaction between
        two vertices. Also return a list that contains all vertices in the order of the matrix.

        Output :
            proteins : a list with all proteins in the order of the matrix
            matrix : a matrix (np.ndarrays())
        '''
        proteins = list(self.int_dict.keys())
        matrix = np.zeros((len(proteins), len(proteins)), dtype=int)
        for key, values in self.int_dict.items():
            for value in values:
                matrix[proteins.index(key), proteins.index(value)] = 1
        return proteins, matrix

    def read_interaction_file(self) -> tuple :
        '''
        Return a triplet, the first element is the interaction dictionnary, the second
        one is the interaction list, the third one the matrix, and the last one is the
        ordered list of vertices.

        Output :
            d_int, l_int, l_som, m_int : dict(), list(), list() and a matrix (np.ndarrays())
        '''
        return (self.get_int_dict(), self.get_int_list(), self.read_interaction_file_mat()[0],
                self.get_mat())

    def count_vertices(self) -> int :
        '''
        Return the number of vertices by counting the numbers of keys of the
        interaction dictionnary (= the number of vertices).

        Output :
            number_of_vertices : an int (number of vertices)
        '''
        number_of_vertices = len(self.get_int_dict().keys())
        return number_of_vertices

    def count_edges(self) -> int :
        '''
        Return the number of edges (the number of interactions of our file).
        Output :
            number_of_edges : an int (number of edges)
        '''
        number_of_edges = len(self.get_int_list())
        return number_of_edges

    def get_degree(self, prot:str) -> int :
        '''
        Return the protein degree (all the interaction of a protein).

        Args :
            prot : the name of a protein existing in the file
        Output :
            protein_degree : an int (number of vertices that are linked to the protein)
        '''
        if prot not in self.get_int_dict() :
            raise ValueError("This protein is not in this graph")
        protein_degree = len(self.get_int_dict()[prot])
        return protein_degree

    def get_max_degree(self) -> tuple :
        '''
        Return the maximum degree (maximum number of interactions) of a given graph, and the protein
            associated to.
        Output :
            proteins : a str (name of the protein(s) that have the maximum degree) ;
            max_degree : an int (maximum degree of the file).
        '''
        max_degree = max(len(item) for item in self.get_int_dict().values())
        protein = tuple(key for key, values in self.get_int_dict().items()
                        if len(values) == max_degree)
        return protein, max_degree

    def get_ave_degree(self, digits:int=4) -> float :
        '''
        Return the mean degree of a given graph of interactions.
        Output :
            mean_degree : an float (mean degree of the graph), with 4 digits.
        '''
        sum_degree = 0
        for prot in self.get_int_dict() :
            sum_degree += len(self.get_int_dict()[prot])
        count_prot = len(self.get_int_dict())
        mean_degree = round(sum_degree/count_prot, digits)
        return mean_degree

    def count_degree(self, deg:int=4) -> int :
        '''
        Return the number of proteins that have the same degree as the one in the argument.
        Args :
            deg : the degree (int) we want to explore.
        Output :
            same_degree_prot : an int (number of proteins that have the same degree).
        '''
        if deg < 0 :
            raise ValueError("You must choose a positive int degree")
        same_degree_prot = 0
        for prot in self.get_int_dict() :
            if len(self.get_int_dict()[prot]) == deg :
                same_degree_prot += 1
        return same_degree_prot

    def histogram_degree(self, dmin:int, dmax:int) -> None :
        '''
        Print for a given range [dmin, dmax] the number of proteins that have the degree d by using
            a dictionnary to save in memory the key (= degree) and the values
            (= number of interactions).
        Args :
            dmin : the minimum degree of the range (int) ;
            dmax : the maximum degree of the range (int).
        Output :
            print histogram_degree() : print a "*" for every proteins that have the degree "nb_deg".
        '''
        count_prot = 0
        deg_int = {}
        for deg in range(dmin, dmax+1):
            if deg not in deg_int :
                deg_int[deg] = self.count_degree(deg)
            else:
                count_prot += self.count_degree(deg)
        for nb_deg, nb_prot in deg_int.items():
            print(str(nb_deg), nb_prot*"*", sep=" ")

    def density(self, digits:int=4) -> float :
        '''
        Return the density of the interactome.
        Output :
            density : a float (number of total edges / maximal number of edges that the interactome
            could have)
        '''
        max_edges = self.count_vertices()*(self.count_vertices()-1)/2   # n*(n-1)/2
        density = round(self.count_edges() / max_edges, digits)              # edges / max_edges
        return density

    def clustering(self, prot:str, digits:int=4) -> float :
        '''
        Return the local clustering coefficient, which is the number of interactions (degree) of
            all the neighbours of a given node divided by the maximum number of interactions
            (degree) it could have.
        Args :
            prot : a given node which we want to know the associated local clustering coefficient
        Output :
            coeff_clustering : a float (number of edges of the protein neighbors / maximal
            number of edges that it could have)
        '''
        # maximum degree of the neighbours of the protein prot
        max_degree_prot = self.get_degree(prot)*(self.get_degree(prot)-1)/2
        list_prot = [prot]
        if max_degree_prot == 0:  # 0 divided by anything equals to 0
            coeff_clustering = float(0)
        else:
            count = 0
            for i in self.get_int_dict()[prot]:
                for j in self.get_int_dict()[i]:
                    if j in self.get_int_dict()[prot] and j not in list_prot :
                        count+=1
                        list_prot.append(j)
            if count > 0: # to delete the input protein from our calculation
                count -= 1
            coeff_clustering = round(count/max_degree_prot, digits)
        return coeff_clustering

    def graph_er(self, proba:float) -> list:
        '''
        Generating Erdös-Rényi random graphs G(n, p) where n is the number of vertices,
        and p is the probability of a edge to be present.
        Args :
            p : a probability (float) of a node is connected to another one (presence of an edge)
        Output :
            g : a random graph (list of tuples) with n nodes and m vertices
         '''
        edges = self.count_edges()
        nodes = list(range(1, edges + 1))
        graph = []
        for i in nodes :
            for j in nodes :
                if i < j:
                    if np.random.binomial(1, proba) == 1:
                        graph.append((str(i), str(j)))
        return graph

    def graph_ba(self, m_max) -> list :
        '''
        Generating Barabasi-Alfred random graph, with m_0 edges in initialization which will be
            increased to m_max edges at the end. The probability that a new edge (s) is
            connected with an pre-existing edge (i) is given by this formula :
                            p(a_si = 1) = k_i / Sum(k_j)
                        where k_i is the degree of the edge i
        Args :
            n_max : maximum number of nodes to create in our graph
        Output :
            g : a random graph (list of tuples) with n nodes and m vertices
        '''
        m_init = self.count_vertices()
        nodes = self.read_interaction_file_mat()[0]
        sum_degrees = 0
        graph = self.get_int_list() #pre-existing graph based on the list of interactions
        for prot in nodes :
            sum_degrees += self.get_degree(prot)
        if m_init < 2 or sum_degrees < 0 :
            raise ValueError
        count = m_init
        while count < m_max :
            deg = 0
            nodes.append(count) #we add a new node
            self.get_int_dict()[count] = []
            for prot in nodes : # for every node in our graph
                # proability of interaction between a pre-existing node and a new one
                proba = self.get_degree(prot)/sum_degrees
                if np.random.binomial(1, proba) == 1:
                    # adding an edge between the new node and a pre-existing one
                    graph.append((prot, str(nodes[-1])))
                    self.get_int_dict()[count] = [nodes[-1]]
                    deg += 1
                sum_degrees += deg
            count +=1
        return graph

    def find_cc(self) -> list :
        '''
        Return all connected nodes. We check if a specific node is connected to another one.
        Output :
            connected_nodes : a list (of all nodes that are connected)
        '''
        cc_list = []
        for node in self.get_int_dict() :
            node_added = False
            for edge in self.get_int_dict()[node] :
                for i in range(len(cc_list)) :
                    if edge in cc_list[i] :
                        if node not in cc_list[i] :
                            cc_list[i].append(str(node))
                            node_added = True
            if node_added is False :
                cc_list.append([str(node)])
        return cc_list

    def count_cc(self) -> int:
        '''
        Return the count of connected components for a given graph.
        Output :
            count_CC : an int which correpond to the number of connected components in our graph
        '''
        count_cc = len(self.find_cc())
        return count_cc

    def write_cc(self) :
        '''
        Return an output file that contains the different connected components.
        Output :
            connected_components.txt : a tabulate file with
            - one lign by connected components
            - the lenght of it is the first element of the line
            - the list of all vertices that composes the connected component.
        '''
        file_cc = self.file_name+"_CC"+self.file_extension
        with open(file_cc, "w+", encoding="utf-8") as file_writer:
            for i in range(self.count_cc()):
                file_writer.write(str(len(self.find_cc()[i]))
                                  + '\t'
                                  + ' '.join(self.find_cc()[i])
                                  + '\n')

    def extract_cc(self, prot:str) -> list :
        '''
        Return all the vertices of the connected component for the protein given in input.
        Args :
            prot : vertice we want to know the connected component which it belongs
        Output :
            self.find_CC : a list (vertices of the connected component for the protein)
        '''
        for i in range(len(self.find_cc())) :
            if prot in self.find_cc()[i] :
                cc_prot = self.find_cc()[i]
        return cc_prot

    def compute_cc(self) -> list :
        '''
        Return for every protein in the connected component, the number of the connected
            component it is involved in.
        Output :
            lcc : a list (number of connected components for every vertices of the
            connected component)
        '''
        lcc = []
        for i in range(len(self.find_cc())) :
            for _ in range(len(self.find_cc()[i])) :
                lcc.append(i+1)
        return lcc

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(
                    prog = 'interactome.py',
                    description = 'Visualization and manipulation of graphs')
    parser.add_argument('filename',
                        help="name of input graph of interaction file",
                        type=str)
    parser.add_argument('-fo', '--file_out',
                        help="name of output graph of interaction file cleaned",
                        type=str,
                        dest='file_out',
                        default=None)
    parser.add_argument('protein',
                        help="name of the protein you want to study locally",
                        type=str)
    parser.add_argument('degree',
                        help="degree that others proteins have too",
                        type=int)
    parser.add_argument('-d',
                        help="number of digits to round-off",
                        dest='d',
                        type=int,
                        default=4)
    parser.add_argument('-min',
                        help="minimum degree for the rank for histogram_degree",
                        type=int,
                        dest='dmin',
                        default=1)
    parser.add_argument('-max',
                        help="maximumx degree for the rank for histogram_degree",
                        type=int,
                        dest='dmax',
                        default=3)
    parser.add_argument('-p', '--proba',
                        help="probability that a node is connected to another for Erdös-Renyi",
                        dest='p',
                        type=float,
                        default=0.5)
    parser.add_argument('-m', '--maximal_degree',
                        help="number of maximum nodes for the Barabasi-Albert graph",
                        dest='m_max',
                        type=int,
                        default=15)
    args = parser.parse_args()
    res = Interactome(args.filename, args.file_out)
    res.get_degree(args.protein)
    res.get_ave_degree(args.d)
    res.count_degree(args.degree)
    res.histogram_degree(args.dmin, args.dmax)
    res.clustering(args.protein, args.d)
    res.density(args.d)
    res.graph_ER(args.p)
    res.graph_BA(args.m_max)
    res.extract_cc(args.protein)
    