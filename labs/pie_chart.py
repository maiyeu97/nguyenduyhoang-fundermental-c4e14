from matplotlib import pyplot

labels = ['MAC','PC','lINUX']
colors = ['red','blue','yellow']
data = [2, 20 ,1]

pyplot.pie(data, labels=labels, colors=colors)
pyplot.axis('equal')
pyplot.show()
