import matplotlib.pyplot as pyplot
labels = ('Python', 'Java', 'Scala', 'C++')
sizes = [40, 30, 25, 5]
pyplot.pie(sizes,
           labels=labels, autopct= '%1.f%%',startangle=0, counterclock= True)
pyplot.show()
