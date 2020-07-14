'''
Word Latters
--------------
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed a a time.

Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and that they are not the same
'''

'''
start: hit
end: cog

hit -> hot -> hog -> cog
hit => hot -> cot -> cog
'''

'''
start: sail
end: boat

sail -> tail -> toil -> coil -> coal -> coat -> boat
sail -> bail -> boil -> boll -> bolt -> boat
'''
from utils import Queue


def find_latters(begin_word, end_word):
    visited = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        vert = path[-1]
        if vert not in visited:
            visited.add(vert)
            if vert == end_word:
                return path
            for next_v in get_neighbors(vert):
                path_copy = list(path)
                path_copy.append(next_v)
                q.enqueue(path_copy)
    return None

#  reads all words from the file and adds them to a set
dictionary = set()
with open('words.txt') as f:
    for line in f:
        word = line.strip()
        dictionary.add(word)
import string
letters = list(string.ascii_lowercase)

def get_neighbors(word):
    neighbors = []
    string_word = list(word)  #['w', 'o', 'r', 'd']

    for i in range(len(string_word)):
        for letter in letters:
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)

            if w == word:
                continue
        
            if w in dictionary:
                neighbors.append(w)
    return neighbors


print(find_latters('sail', 'boat'))
print(find_latters('hit', 'cog'))