'''
STUDENT CODE:
'''

from random import uniform, random

class MarkovModel:
    def __init__(self, probs=[], emissions=[]):
        assert type(probs) == list and type(emissions) is list
        self.p = probs
        self.e = emissions
        self.s = [1]*len(probs)     # Size of the data that goes into making

    '''
    Run markov model until endfunc returns anything other than False
    endfunc must be a function that takes a string (for last emission)
    and an int representing the number of iterations run.
	endfunc must return False to continue or anything else (True) to stop
    '''
    def run(self, endfunc):
        c = 0
        i = uniform(0, len(self.e))
        s = self.e[i]
        while(endfunc(s, c) == False):
            print(s)
            newi = random()
            newi = binsearch(self.p[i], newi)
            s = self.p[i][newi]
            i = newi
            c += 1

def train(mm, data):
    assert type(mm) is MarkovModel
    # assert type(data) is list
    indices = {}
    l = 0
    # Reset the hmm, just good practice.
    mm.e = []
    mm.p = []
    data = [(d.split(' ') + ['\n']) for d in data.split('\n')]
    prev = None
    for sent in data:
        for word in sent:
            if(indices.get(word) == None):
                indices[word] = l
                l += 1
                mm.e.append(word)
                mm.p.append([0] * l)
            if(indices.get(prev) != None):
                mm.p[indices[prev]][indices[word]] += 1
                mm.s[indices[prev]] += 1



'''
PROVIDED CODE:
'''

def endOnString(st, i, endstr="\n"):
    if(st == endstr):
        return True
    else:
        return False

def endAfterN(st, i, num=100):
    if(i == num):
        return True
    else:
        return False

# Parse Project Gutenberg csv
def dataFromNovel(filename):
    pass


def binsearch(l, val, j=0):
	assert type(l) is list
	if(len(l) < 1):
		return None
	elif(len(l) == 1):
		return j
	else:
		i = len(l) // 2
		if(val < l[i]):
			binsearch(l[:i], val, j)
		else:
			binsearch(l[i:], val, j+i)
