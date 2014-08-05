"""Lab 2: Classes and Inheritance
Demonstrating the Median Voter Theorem""" 

import random 

# background: 
# http://en.wikipedia.org/wiki/Median_voter_theorem
# http://en.wikipedia.org/wiki/Jefferson_(Pacific_state)
# http://www.youtube.com/watch?v=31FFTx6AKmU

class Individual(object):
  def __init__(self, ideology):
    self.ideology = ideology

class Voter(Individual):
  def __init__(self, ideology): 
    Individual.__init__(self, ideology)
  # TODO: have a voter tell you their ideology


class Candidate(Individual):
  def __init__(self, ideology, party): 
    Individual.__init__(self, ideology)
    self.party = party 
    self.numerator = 1
    self.denominator = 1

  def __repr__(self):
    return "%s party" % self.party 

  def report_ideology(self):
    return self.ideology 

  def update_ideology(self, ballot):
    return self.ideology 
    # TODO:  make this method work! 


class Polity(object):
  def __init__(self):
    self.voters = []
    self.candidates = []

  # TODO: have a polity print count of candidates and voters

  def populate(self, count):
    for i in range(count):
      ideol = random.betavariate(5,5)
      voter = Voter(ideol) 
      self.voters.append(voter)

  def nominate(self, cand):
    self.candidates.append(cand)

  def election(self):
    counts = [0] * len(self.candidates) 
    ballots = dict(zip(self.candidates, counts))
    for voter in self.voters: 
      minDiff = min(range(len(self.candidates)), key = lambda i: abs(voter.ideology - self.candidates[i].ideology))
      choice = self.candidates[minDiff]
      ballots[choice] += 1 
    return ballots 

  def get_winner(self, ballots):
    winner = max(ballots, key=ballots.get)
    return winner 

  def report_candidate_ideologies(self):
    for candidate in self.candidates:
      print candidate, ":", candidate.report_ideology()

  def update_candidate_ideologies(self, ballot):
    return 
    # TODO: call the update_ideology method for each candidate


def print_winner(winner):
  print "And the winner is... the %s!" % winner

def election(polity):
  result = jefferson.election() 
  print result 
  winner = jefferson.get_winner(result)
  print_winner(winner)
  # TODO: make this part work 
  print "OLD IDEOLOGIES:"
  jefferson.report_candidate_ideologies()
  print "NEW IDEOLOGIES:"
  jefferson.update_candidate_ideologies(result)
  jefferson.report_candidate_ideologies()
  print "\n"
  return winner 

# Make candidates
sensible = Candidate(.55, "sensible")
silly = Candidate(.45, "silly")
slightly_silly = Candidate(.4, "slightly silly")
# TODO: initialize very silly party with ideology .1
#       and a stone dead party with ideology .01 

print sensible, silly, slightly_silly

# Create and populate polity
jefferson = Polity()
jefferson.populate(100)

# Nominate candidates
jefferson.nominate(sensible)
jefferson.nominate(silly)
jefferson.nominate(slightly_silly)
# don't forget to nominate your new candidates! 

print jefferson 

# Have an election 
winner = election(jefferson)

# TODO: keep holding elections until the sensible party loses 

### Suggested task order ###
### 1. implement missing print methods in Voter and Polity
### 2. initialize candidates from other parties
### 3. nominate your new candidates
### 4. implement update_ideology() in the Candidate class 
### 5. implement update_candidate_ideologies() in the Polity class
### 6. implement the loop described immediately above 

# Hint: my completed code is only 10 lines longer than this file