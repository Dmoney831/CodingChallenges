# import datetime
from datetime import datetime
from collections import defaultdict

def weekly_aggregation(ts):
    result = defaultdict(list)
    for t1 in ts:
        t1_date = datetime.strptime(t1, "%Y-%m-%d")
        week = t1_date.isocalendar()[1]
        result[week].append(t1)
    return list(result.values())



ts = [
    '2019-01-01', 
    '2019-01-02',
    '2019-01-08', 
    '2019-02-01', 
    '2019-02-02',
    '2019-02-05',
]
print(weekly_aggregation(ts))