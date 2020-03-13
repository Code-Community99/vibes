import numpy as np 
import matplotlib.pyplot as plt

x=np.arange(32).reshape(16,2)
print(x)

new=x.reshape(8,4)
print(new)

print(new.shape)#prints the array size


#a new array
interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")]
for x in interests:
	print(x)
#print(interests)

def data_scientists_who_like(target_interest):
	print([user_id for user_id, user_interest in interests if user_interest == target_interest])

data_scientists_who_like(interests)


#list cpmprehesion

pair= [(x,y) for x in range(100)for y in range(100)]#prints the number 100 times starting from (0,0)....(99,99)

print(pair)



#graphs
#defined data to plot
#line graph

years = [1959, 1969, 1979, 1989, 1999, 2009, 2019]
population = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line graph, years on x-axis, gdp on y-axis
plt.plot(years, population, color='green', marker='o', linestyle='solid')
# add a title
plt.title("Census Visualization for Kenyan Economy")
# add a label to the y-axis
plt.ylabel("population in `0000")
#plt.show()




#bar graph

Age_group = ["0 to 12", "13 to 18", "19 to 30", "31 to 50", "51 to .."]
percentage_population = [17, 21, 34, 12, 6]
#0.1 is bar size
x_value = [i + 0.1 for i, _ in enumerate(percentage_population)]

plt.bar(x_value, Age_group)
plt.ylabel("Percentage Age Group")
plt.title("Age Group")
#plt.show()




variance=[1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared =[256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error =[x + y for x, y in zip(variance, bias_squared)]
xs = [i for i,_ in enumerate(variance)]



# we can make multiple calls to plt.plot
# to show multiple series on the same chart
plt.plot(xs, variance,
'g-', label='variance')
# green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2')
# red dot-dashed line
plt.plot(xs, total_error, 'b:', label='total error') # blue dotted line
# because we've assigned labels to each series
# we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()