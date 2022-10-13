from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create two D6.
die_1 = Die()
die_2 = Die()


# Make some rolls, and store results in a list.
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# for roll_num in range(100_000):
    # result = die_1.roll() * die_2.roll()
    # results.append(result)

# Analyze the results.
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]
# for value in range(2, max_result + 1):
    # frequency = results.count(value)
    # frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 6}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three(we multiplied them) D6 die 100000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_*_d6.html')
