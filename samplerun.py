from hmm_sol import *
from twitter_api import get_tweets

m = MarkovModel()
d = get_tweets('SarcasticRover')
train(m, d)
m.run(endOnString)
