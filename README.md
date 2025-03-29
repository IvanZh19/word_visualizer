# word_visualizer

This is a short script I wrote to help me play [Word Ladder](https://en.wikipedia.org/wiki/Word_ladder). To play it, I like [this website](https://wordwormdormdork.com/).
The script relies on NetworkX and Matplotlib, and the words used are thanks to the open-source [Wordnik Wordlist](https://github.com/wordnik/wordlist). It supports words that are 4, 5, or 6 characters long, and I've also included the corresponding sets of words as raw text files.

Just run `word.py`, enter your starting and ending words, and start guessing!

I used it to get an optimal path between NEXT and HEIR! Spoilers:

![graph of my attempt](images\next_heir_graph.png)

![next, neat, heat, hear, heir](images\next_heir.png)
