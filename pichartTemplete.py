import matplotlib.pyplot as plt
import os

class piChart:
    lables = []
    data = []
    outputImage = str
    def __init__(self,labels,data,outputImage):
        self.lables = labels
        self.data = data
        self.outputImage = outputImage
        self.showChart()

    def showChart(self):
            colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
            fig = plt.figure()
            ax = fig.add_axes([0, 0, 1, 1])
            ax.axis('equal')
            plt.title('title')
            try:
             plt.pie(self.data, autopct='%1.2f%%', colors=colors, explode=(0.05, 0.05, 0.05, 0.05))
            except:
                plt.pie(self.data, autopct='%1.2f%%', colors=colors,)
            centre_circle = plt.Circle((0, 0), 0.80, fc='white')
            fig = plt.gcf()
            fig.gca().add_artist(centre_circle)
            plt.legend(self.lables, title=self.outputImage,
                       loc="upper right",
                       )
            if not os.path.exists('./chart/'):
                os.mkdir('./chart/')
            plt.savefig('./chart/' + self.outputImage)
