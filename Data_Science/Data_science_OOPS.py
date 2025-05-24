

# Create a list of tuples, each representing the name, age, and position of a
# player on a basketball team.
team = [
    ('Marta', 20, 'center'),
    ('Ana', 22, 'point guard'),
    ('Gabi', 22, 'shooting guard'),
    ('Luz', 21, 'power forward'),
    ('Lorena', 19, 'small forward'),
    ]

# Create a function to extract and names and positions from the team list and
# format them to be printed. Returns a list.
def players_position(players):
    result = []

    for name, age, position in players:
        result.append('Name: {:>19} \nPosition: {:>15}\n'.format(name,position))

    return result

for player in players_position(team):
    print(player)

# Nested loops can produce the different combinations of pips (dots) in
# a set of dominoes.
for left in range(7):
    for right in range(left, 7):
        #print(left, right)
        print(f'[{left}|{right}]', end = " ")
        #print("A")

    print('\n')


# Create a list of dominoes, with each domino reprented as a tuple.
dominoes = []
for left in range(7):
    for right in range(left,7):
        dominoes.append((left, right))

print(dominoes)

print(dominoes[4][1])

# You can use a for loop to sum the pips on each domino and append
# the sum to a new list.
pips_from_loop = []
for domino in dominoes:
    pips_from_loop.append(domino[0] + domino[1])
print(pips_from_loop)

# A list comprehension produces the same result with less code.
pips_from_loop_comp = [domino[0] + domino[1] for domino in dominoes]
print(pips_from_loop == pips_from_loop_comp)

cities = ['Paris', 'Lagos', 'Mumbai']
countries = ['France', 'Nigeria', 'India']
places = zip(cities, countries)

print(places)
print(list(places))

scientists = [('Nikola', 'Tesla'), ('Charles', 'Darwin'), ('Marie', 'Curie')]
given_names, surnames = zip(*scientists)
print(given_names)
print(surnames)

letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print(index, letter)

letters = ['a', 'b', 'c']
for index, letter in enumerate(letters, 2):
   print(index, letter)

#List Comprehension
#my_list = [expression for element in iterable if condition]
numbers = [1, 2, 3, 4, 5]
num_list = [x + 10 for x in numbers]
print(num_list)

#my_list = [expression for element in iterable if condition]
words = ['Emotan', 'Amina', 'Ibeno', 'Sankwala']
new_list = [(word[0], word[-1]) for word in words if len(word) > 5]
print(new_list)

