class Senator():
  def __init__(self, name):
    self.name = name
    self.bills_voted_on = []

  def vote(self, bill, choice):
    print self.name + " votes " + choice + " on " + bill.title
    bill.votes[choice].append(self.name)
    self.bills_voted_on.append(bill)

class Bill():
  def __init__(self, title):
    self.title = title
    self.votes = {"yes" : [], "no" : [], "abstain" : []}
    self.passed = None

  def result(self):
    if len(self.votes["yes"]) > len(self.votes["no"]):
      self.passed = True
    else:
      self.passed = False
    return self.passed

jane = Senator("Jane")
jack = Senator("Jack")
environment = Bill("Environmental Protection")
jane.vote(environment, "yes")
jack.vote(environment, "no")
environment.result()
print environment.votes
print environment.passed
print jack.bills_voted_on[0].passed

