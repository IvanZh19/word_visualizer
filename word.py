import networkx as nx
import matplotlib.pyplot as plt

def test_edge(word1, word2):
    """returns True if word1 and word2 can be linked"""
    diffs = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diffs += 1
    return diffs == 1

def prompt_word(wordset):
    """prompts user until a word from wordset is received."""
    word = ''
    while word not in wordset:
        word = input('Enter a word:')
    return word

class WordGraph:
    """
    Represents the space of words explored in a word ladder game.
    """
    def __init__(self, start, end):
        """
        start and end are the target strings to connect.
        """
        self.start = start
        self.end = end
        self.start_blob = {start}
        self.end_blob = {end}
        self.nodes = {start, end}
        self.edges = set() # assuming not trivial start==end case

    def display_insides(self):
        """
        Displays the internal values of the WordGraph, for debugging.
        """
        print(self.start)
        print(self.end)
        print(self.start_blob)
        print(self.end_blob)
        print(self.nodes)
        print(self.edges)


    def display(self):
        """
        Displays the state of the WordGraph.
        """
        new_G = nx.Graph()
        new_G.add_nodes_from(self.nodes)
        new_G.add_edges_from(self.edges)
        nx.draw(new_G, with_labels=True)
        plt.pause(.1)
        plt.clf()

    def add_word(self, candidate):
        """
        Adds the candidate word to the WordGraph, with any applicable connections.
        """
        for word in self.nodes:
            if test_edge(word, candidate):
                self.edges.add((word, candidate))
                if word in self.start_blob:
                    self.start_blob.add(candidate)
                elif word in self.end_blob:
                    self.end_blob.add(candidate)
        self.nodes.add(candidate)

    def check_done(self, candidate):
        """
        Returns True if the candidate word connects start and end, False otherwise
        """
        return candidate in self.start_blob and candidate in self.end_blob

if __name__=="__main__":
    start = input('Enter the starting word:')
    end = input('Enter the ending word:')
    assert len(start) == len(end), 'Impossible start and end pair'
    assert len(start) in {4,5,6}, 'Not supported word length'
    # consider using pickle to save and load wordset.
    wordset = set()
    with open(f'wordset_{len(start)}.txt','r') as f:
        for line in f:
            wordset.add(line[:-1]) # exclude \n

    word_graph = WordGraph(start, end)
    done = False
    while not done:
        new_word = prompt_word(wordset)
        word_graph.add_word(new_word)
        word_graph.display()
        done = word_graph.check_done(new_word)
    done = False
    while not done:
        word_graph.display()
        done = input('Game complete! Enter 1 to quit: ') != 1

"""code used to generate 4,5,6 length word files"""

# wordset_4 = set()
# wordset_5 = set()
# wordset_6 = set()

# with open('wordlist-20210729.txt', 'r') as file:
#     # the raw file has quotation marks and \n
#     for line in file:
#         word = line[1:-2]
#         if len(word) == 4:
#             wordset_4.add(word)
#         elif len(word) == 5:
#             wordset_5.add(word)
#         elif len(word) == 6:
#             wordset_6.add(word)

# with open('wordset_4.txt', 'a') as f:
#     for word in wordset_4:
#         f.write(word+'\n')

# with open('wordset_5.txt', 'a') as f:
#     for word in wordset_5:
#         f.write(word+'\n')

# with open('wordset_6.txt', 'a') as f:
#     for word in wordset_6:
#         f.write(word+'\n')
