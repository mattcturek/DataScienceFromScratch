from matplotlib import pyplot as plt

#  Line Charts
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title("Nominal GDP")

plt.ylabel("Billions of $")
plt.show()


#  Bar Charts
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

#  Plot Bars with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")

#  Label X-Axis with Movie NAmes at Bar Centers
plt.xticks(range(len(movies)), movies)

plt.show()


#  Bar Chart that can be used as a histogram as well

from collections import Counter
grades = [83, 95, 91, 87, 70, 0, 85, 82,  100, 67, 73, 77, 0]

#  Bucket grades be decile, but put 100 in with the 90s
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],
        histogram.values(),
        10,
        edgecolor=(0, 0, 0))
plt.axis([-5, 105, 0 ,5])

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()


#  Misleading Bar-Histogram chart by not starting the Y-Axis at 0
mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of tikmes I heard someone say 'data science'")

#  If you don'tn do this, matplotlib will label the x-axis 0, 1
#  and then add a +2.013e3 off in the corner (bad matplotlib)!
plt.ticklabel_format(useOffset=False)

#  Misleading the Y-Axis Only shows the part above 500
plt.axis([2016.5, 2018.5, 0, 550])
plt.title("Look athe the 'Huge Increase!'")
plt.show()


#  Line Charts, they are good at showing trends
variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

#  We can make multiple calls to plt.plot
#  to show multiple series on the same chart
plt.plot(xs, variance, 'g-', label='variance')    #  green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2')      #  red dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error')   #  blue dotted line

#  Because we've assigned labels to each series,
#  we can get a legend for free (loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("Model Complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.show()


#  Scatterplots is the right choice for visualizing the relationship between
#  between two paried sets of data
friends = [ 70,  65,  72,  63,  71,  64,  60,  64,  67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

#  Label Each Point
for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label,
                     xy=(friend_count, minute_count),
                     xytext=(5, -5),
                     textcoords='offset points')

plt.title("Daily Minutes vs Number of Friends")
plt.xlabel("# of Friends")
plt.ylabel("daily minutes spent on site")
plt.show()