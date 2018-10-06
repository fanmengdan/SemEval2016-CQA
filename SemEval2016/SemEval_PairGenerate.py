import pandas as pd
from datetime import datetime

data = pd.read_csv("PairOriginal.tsv",sep='\t', lineterminator='\n', dtype= 'str')

DATA_DUMP_DAY = datetime(2018, 7, 18, 0, 0, 0, 0)

def get_age(creation_date):
    the_date, the_date2 = creation_date.split(" ")
    year, month, day = the_date.split("-")
    hour, minute, second = the_date2.split(":")
    cdate = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), 0)
    delta = DATA_DUMP_DAY - cdate
    return delta.days*24*3600+delta.seconds
data = data[data['Credible'].isin(['0','1'])]
print data
data['Q_time'] = data['Q_time'].apply(lambda x: get_age(x))
data['A_time'] = data['A_time'].apply(lambda x: get_age(x))
data['QASpan'] = data['Q_time'] - data['A_time']
print "QASpan done!"

data['#Title'] = data['Q_subject'].apply(lambda x: len(x.split(' ')))
data['#QWords'] = data['Q_body'].apply(lambda x: len(x.split(' ')))
data['#QSentence.'] = data['Q_body'].apply(lambda x: len(x.split('.')))
data['#QSentence,'] = data['Q_body'].apply(lambda x: len(x.split(',')))
data['#QSentence;'] = data['Q_body'].apply(lambda x: len(x.split(';')))
print "Q semantic done!"

data['#AWords'] = data['Q_body'].apply(lambda x: len(x.split(' ')))
data['#ASentence.'] = data['A_body'].apply(lambda x: len(x.split('.')))
data['#ASentence,'] = data['A_body'].apply(lambda x: len(x.split(',')))
data['#ASentence;'] = data['A_body'].apply(lambda x: len(x.split(';')))
print "A semantic done!"

temp_dict = dict()
for i,j in data.groupby('Q_id'):
    temp_dict[i] = len(j)
data['Q_#A'] = data['Q_id'].apply(lambda x: temp_dict[i])
data["PairId"] = [i for i in range(len(data))]
print "index done!"

data = data[['PairId','QASpan','Q_id','Q_user','Q_#A','A_id','A_user','#Title','#QWords','#QSentence.','#QSentence,','#QSentence;','#AWords','#ASentence.','#ASentence,','#ASentence;','Credible']]
data.to_csv("New_SemEval.csv")
