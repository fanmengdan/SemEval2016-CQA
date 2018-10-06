# SemEval preprocess
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

file = open("SemEval2016-Task3-CQA-QL-dev.xml","r")
soup = BeautifulSoup(file,"html5lib")
file.close()

file = open("SemEval2016-Task3-CQA-QL-train-part1.xml","r")
soup1 = BeautifulSoup(file,"html5lib")
file.close()

file = open("SemEval2016-Task3-CQA-QL-train-part2.xml","r")
soup2 = BeautifulSoup(file,"html5lib")
file.close()

# store the features
PairFeature = []
NQ = 0
NPair = 0

# dev part
for thread in soup.find_all('thread'):
    # store Q info.
    tempQ = []
    Q = thread.find_all('relquestion')[0]
    tempQ.append(Q['relq_date'])
    tempQ.append(Q['relq_id'])
    tempQ.append(Q['relq_userid'])
    if str(Q.relqsubject.string):
        tempQ.append(str(Q.relqsubject.string))
    else:
        tempQ.append(',')
    if str(Q.relqbody.string):
        tempQ.append(str(Q.relqbody.string))
    else:
        tempQ.append(",")
    tempQ.append(str(len(thread.find_all('relcomment'))))

    # add A info.
    for A in thread.find_all('relcomment'):
        temp = []
        temp += tempQ
        temp.append(A['relc_date'])
        temp.append(A['relc_id'])
        temp.append(A['relc_userid'])
        if str(A.relctext.string):
            temp.append(str(A.relctext.string))
        else:
            temp.append(",")
        if str(A['relc_relevance2relq'])=="Good":
            temp.append("1")
        else:
            temp.append("0")
        PairFeature.append(temp)
print "Dev dinish!"

for thread in soup1.find_all('thread'):
    # store Q info.
    tempQ = []
    Q = thread.find_all('relquestion')[0]
    tempQ.append(Q['relq_date'])
    tempQ.append(Q['relq_id'])
    tempQ.append(Q['relq_userid'])
    if str(Q.relqsubject.string):
        tempQ.append(str(Q.relqsubject.string))
    else:
        tempQ.append(',')
    if str(Q.relqbody.string):
        tempQ.append(str(Q.relqbody.string))
    else:
        tempQ.append(",")
    tempQ.append(str(len(thread.find_all('relcomment'))))

    # add A info.
    for A in thread.find_all('relcomment'):
        temp = []
        temp += tempQ
        temp.append(A['relc_date'])
        temp.append(A['relc_id'])
        temp.append(A['relc_userid'])
        if str(A.relctext.string):
            temp.append(str(A.relctext.string))
        else:
            temp.append(",")
        if str(A['relc_relevance2relq'])=="Good":
            temp.append("1")
        else:
            temp.append("0")
        PairFeature.append(temp)
print "Part1 finish!"

for thread in soup2.find_all('thread'):
    # store Q info.
    tempQ = []
    Q = thread.find_all('relquestion')[0]
    tempQ.append(Q['relq_date'])
    tempQ.append(Q['relq_id'])
    tempQ.append(Q['relq_userid'])
    if str(Q.relqsubject.string):
        tempQ.append(str(Q.relqsubject.string))
    else:
        tempQ.append(',')
    if str(Q.relqbody.string):
        tempQ.append(str(Q.relqbody.string))
    else:
        tempQ.append(",")
    tempQ.append(str(len(thread.find_all('relcomment'))))

    # add A info.
    for A in thread.find_all('relcomment'):
        temp = []
        temp += tempQ
        temp.append(A['relc_date'])
        temp.append(A['relc_id'])
        temp.append(A['relc_userid'])
        if str(A.relctext.string):
            temp.append(str(A.relctext.string))
        else:
            temp.append(",")
        if str(A['relc_relevance2relq'])=="Good":
            temp.append("1")
        else:
            temp.append("0")
        PairFeature.append(temp)
print "Part2 finish!"

NQ = len(soup.find_all('thread'))+len(soup1.find_all('thread'))+len(soup2.find_all('thread'))
NPair = len(PairFeature)

print "# of Question is: ", NQ
print "# of Pairs is: ", NPair

file = open("PairOriginal.tsv","w")
file.write("Q_time\tQ_id\tQ_user\tQ_subject\tQ_body\tQ_#A\tA_time\tA_id\tA_user\tA_body\tCredible\n")
for pair in PairFeature:
    file.write("\t".join(pair)+'\n')
file.close()
print "jobs done!"
