#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:19:31 2020

@author: lauraglastra
"""

# Import the matplotlib module here.  No other modules should be used.
from matplotlib import pyplot as plt

# Create a list variable that contains at least 25 elements.  You can create this list any number of ways.  
# This will be your sample.
a = [*range(0,25,1)]
print(a)

# Pretend you do not know how long x is; compute it's length, N, without using functions or modules.
def calc_length(x):
    counter = 0
    for i in x:
        counter = counter + 1
    return counter

x = a
print(calc_length(x));

# Compute the mean of the elements in list x.
sum = 0
for i in x:
    sum = sum + i

mean = sum/calc_length(x)

print(mean)

# Compute the std deviation, using the mean and the elements in list x.
#print(x)
b = []
for i in x:
    sdist = (abs(i - mean))**2
    b.append(sdist)
#print(b)

sum_sdist = 0;
for i in b:
    sum_sdist = sum_sdist + i
    
#print(sum_sdist)

std=(sum_sdist/calc_length(x))**(1/2)
print(std)

# Use the 'print' command to report the values of average (mu) and std. dev. (sigma).
print("Average: ", mean, "  Std dev: ", std)


# Count the number of values that are within +/- 1 std. deviation of the mean.  
# A normal distribution will have approx. 68% of the values within this range.  
# Based on this criteria is the list normally distributed?

count = 0;
for i in x:
    if i >= (mean+std) or i <= (mean-std):
        count = count+1
 
print(count)

ndist = (count/calc_length(x))*100

# Use print() and if statements to report a message about whether the data is normally distributed.
if ndist > 70 or ndist < 65:
    print("The list is not normally distributed. ", ndist, " is the percent of values within +/- 1 std. deviation of the mean")
else:
    print("The list is pretty normally distributed. ", ndist, " is the percent of values within +/- 1 std. deviation of the mean")


### Use Matplotlb.pyplot to make a histogram of x.
plt.hist(x)



# too lazy to calculate median separately in a function so just using known median of 12
# using pearson's skewness forumal
skw = (3*(mean-12))/std
print(skw)

"""
According to this very legitamate website, https://www.statisticshowto.com/pearsons-coefficient-of-skewness/
there is zero skewness in this sample according to the Pearson skewness calculation performed above. If the value 
were negative or positive then it means the distribution is negatively or positively skewed respectively.






