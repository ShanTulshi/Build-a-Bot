'''
STUDENT CODE:
'''

from random import uniform, random
from sample import *

class MarkovModel:
    def __init__(self, probs=[], emissions=[]):
        assert type(probs) is list and type(emissions) is list
        assert len(probs) == len(emissions)
        self.p = probs
        self.e = emissions
        self.indices = {}

    '''
    Run markov model until endfunc returns anything other than False
    endfunc must be a function that takes a string (for last emission)
    and an int representing the number of iterations run.
	endfunc must return False to continue or anything else (True) to stop
    '''
    def run(self, endfunc):
        c = 0
        i = int(uniform(0, len(self.e)))
        word = self.e[i]
        while(endfunc(word, c) == False):
            print(word, end=' ')
            newi = random()
            newi = search(self.p[i], newi)
            word = self.e[newi]
            i = newi
            c += 1
        print()

def train(mm, data):
    assert type(mm) is MarkovModel
    l = 0
    # Reset the hmm, just good practice.
    mm.e = []
    mm.p = []
    mm.indices = {}

    data = [(d.split(' ') + ['\n']) for d in data]
    prev = None
    for sent in data:
        for word in sent:
            if(mm.indices.get(word) == None):
                mm.indices[word] = l
                l += 1
                mm.e.append(word)
    mm.p = [([0] * len(mm.e)) for i in range(len(mm.e))]
    for sent in data:
        for word in sent:
            if(mm.indices.get(prev) != None):
                mm.p[mm.indices[prev]][mm.indices[word]] += 1
            prev = word
    # Divide everything by sum to get probabilities out of 1
    for i in range(len(mm.p)):
        denom = sum(mm.p[i])
        for j in range(len(mm.p[i])):
            # Plus-one smoothing, for variety
            mm.p[i][j] = (mm.p[i][j] + 1) / (denom + len(mm.p[i]))
            if(j > 1):
                mm.p[i][j] += mm.p[j][j-1]


'''
PROVIDED CODE:
'''

def endOnString(st, i, endstr="\n"):
    if(endstr in st):
        return True
    else:
        return False

def endAfterN(st, i, n=100):
    if(i == n):
        return True
    else:
        return False

# Parse Project Gutenberg csv
def dataFromNovel(filename):
    f = open(filename)
    data = []
    for line in f:
        # Remove extraneous lines
        if(len(line) > 3):
            # Add everything but the first char (") and the last 2 ("\n).
            data.append(line[1:-2])
    return data


def search(l, val, j=0):
	assert type(l) is list
	if(len(l) <= 1):
		return j
	else:
		i = len(l) // 2
		if(val < l[i]):
			return search(l[:i], val, j)
		else:
			return search(l[i:], val, j+i)
