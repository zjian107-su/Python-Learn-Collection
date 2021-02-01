import pygal
from die import Die

# create two D6 dices
die_1 = Die()
die_2 = Die()

# throw a dice and save the result in a result
results = []
for roll_num in range(1000000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# analysis
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualiztaion
hist = pygal.Bar()

hist.title = "Results of multiplying two D6 dice. (1,000,000 rolls)"
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8',
#  '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_labels = list(range(1, max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_visual.svg')

print(frequencies)
