# statistics is another built-in module. It helps out with statistic functions like the mean of a list, like with mean(scores) here.
import statistics

scores = [4, 4, 3, 6, 1, 2, 8, 4]
mean = statistics.mean(scores)
print(f"Mean score is {mean}")

# We're able to use multiple different modules in the same file by adding a comma between the modules we're importing.

import statistics, math

diameters = [9, 7, 4, 6]
result = statistics.mean(diameters)
print(f"Mean diameter is {result}")

print("Value of pi is: ")
print(math.pi)

# Sometimes we want to use just parts of a module and not the whole functionality, like here where we only need the value for pi from math.

import math

print("Value of pi is: ")
print(math.pi)

# In that case, we can use the keyword from to extract only the funtionality we care about, like here with from math import pi.

from math import pi

print("Value of pi is: ")
print(pi)

# When we use from, we don't need to add the name of the module anymore. Like here we use mean isntead of statistics.mean .

from statistics import mean

test_scores = [33, 7, 4, 6]
result = mean(test_scores)
print(f"Mean result is {result}")
      
# Q. What's the statistics module for?
# A. It provides methods to help with common statistical calculations.

# Q. How do we import multiple modules?
# A. By placing a comma between the modules we're importing.

# Q. What does the form keyword do when importing modules?
# A. It allows us to import parts of a module's functionality.

# What happens when we use the from keyword to import certain functionality?
# A. We no longer need to use the module's name in our code when using functionality.

# Complete the code by importing two modules.

import statistics, math

active_time = [2, 2, 4, 5]
result = statistics.mean(active_time)
print(f"Mean is {result}")

# Import the pi functionality from the math module.

from math import pi

print(pi)

# Use the mean functionality from the imported statistics module.

from statistics import mean

ages = [22, 26, 18, 35]
result = mean(ages)
print(result)

