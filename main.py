from pichartTemplete import piChart
import  numpy as np
import  pandas as pd

question1 = 'How do you feel overall about distance education?'
question2 = ' Do you have access to a device for learning online?'
question3 = 'What device do you use for distance learning?'
question4 = 'How much time do you spend each day on an average on distance education?'
question5 = 'How effective has remote learning been for you?'
question6 = 'How helpful your [School or University] has been in offering you the resources to learn from home?'
question7 = ' Do you enjoy learning remotely?'
question8 = 'How helpful are your teachers while studying online?'
listQuestion = [question1,question2,question3,question4,question5,question6,question7,question8]
def questionOption(question):
    if question1 == question:
        return ['Excellent','Good','Average','Poor']
    if question2 == question:
        return ['Yes','Yes, but it doesn’t work well','No, I use others device']
    if question3 == question:
        return ['Laptop','Desktop','Tablet','Smartphone']
    if question4 == question:
        return ['1-3 hours','3-5 hours','5-7 hours','7+ hours']
    if question5 == question:
        return ['Extremely effective','Moderately effective','Slightly effective','Not at all effective']
    if question6 == question:
        return ['Extremely helpful','Moderately helpful','Slightly helpful','Not at all helpful']
    if question7 == question:
        return ['Yes, absolutely','Yes, but I would like to change a few things','No, there are quite a few challenges','No, not at all']
    if question8 == question:
        return ['Extremely helpful','Moderately helpful','Slightly helpful','Not at all helpful']
def getChart(question):
    data = pd.read_csv('Distance learning survey.csv')
    dataInNumpy = data[question].to_numpy()
    listlabels = questionOption(question)
    data = []
    for i in listlabels:
        data.append((len(np.where(dataInNumpy == i)[0])*100)/len(dataInNumpy))
    piChart(data =data, labels=listlabels,outputImage=question)

for i in listQuestion:
  getChart(i)