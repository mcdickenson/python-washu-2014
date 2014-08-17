# pip install pollster
from pollster import Pollster 

pollster = Pollster()

# current estimate of president's job approval
chart = pollster.charts(topic='obama-job-approval')[0]
chart.estimates

example_topics = ['2012-gop-primary', '2012-senate', '2012-governor', '2012-president', '2012-house']

# list charts about Texas
pollster.charts(state='TX')

# calculate margin between Obama and Romney from poll
poll = pollster.polls(chart='2012-general-election-romney-vs-obama')[0]
question = [ x['subpopulations'][0] for x in poll.questions if x['chart'] == '2012-general-election-romney-vs-obama'][0]
obama = [x for x in question['responses'] if x['choice'] == 'Obama'][0]
romney = [x for x in question['responses'] if x['choice'] == 'Romney'][0]
print obama['value'] - romney['value']

# check methodology in recent polls about the house 
chart = pollster.chart(slug='us-health-bill')
print [[x.pollster, x.method] for x in chart.polls()]

# TODO: compare favorability of Democratic and Republican parties from a recent poll
# use info at http://elections.huffingtonpost.com/pollster/api/charts