import pygal
from die import Die

# create a D6
die = Die()

# throw a dice and save the result in a result
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# analysis
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualiztaion
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)
