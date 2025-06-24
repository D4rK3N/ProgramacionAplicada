print(end="\n")
animals = {'cat', 'dog', 'goldfish', 'canary', 'cat'}
print(animals) 


even_numbers = {2, 4, 6, 8, 10}
big_numbers = {6, 7, 8, 9, 10}
print(end="\n")
print(big_numbers - even_numbers)
print(big_numbers | even_numbers)
print(big_numbers & even_numbers)


print(end="\n")
print(animals)
print(sorted(animals))


print(end="\n")
print(list(range(10)))
print(list(range(1, 11)))
print(list(range(1, 11, 2)))


animals = ['cat', 'dog', 'goldfish', 'canary', 'cat']

animals_set = set(animals)
animals_unique_list = list(animals_set)
animals_unique_tuple = tuple(animals_unique_list)
print(end="\n")
print (animals_set)
print (animals_unique_list)
print (animals_unique_tuple)


marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }

colours = list(marbles)
counts = tuple(marbles.values()) 
marbles_set = set(marbles.items())

print(end="\n")
print (colours)
print (counts)
print (marbles_set)


dictado=dict([(1, 2), (3, 4)])
print(end="\n")
print(dictado)


s = "abracadabra"
print("\n")
print(len(s))
print(s.index("a"))
print(s[0])
print(s[3:5])

print("\n")
print('h' in 'abcd') 


print('ab' in 'abcd') 


print(['a', 'b'] in ['a', 'b', 'c', 'd'])


print("\n")
abc_list = list("abracadabra")
print(abc_list)

print("\n")
l = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']
s = "".join(l)
print(s)


animals = ('cat', 'dog', 'fish')
print("\n")
print(" ".join(animals))
print(",".join(animals))
print(", ".join(animals))
print("cat    dog fish\n".split())
print("cat|dog|fish".split("|"))
print("cat, dog, fish".split(", "))
print("cat, dog, fish".split(", ", 2))


my_table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]
print("\n")
print(my_table[0][0])
my_table[0][0] = 42
print(my_table)


my_2d_list = [
    [0],
    [1, 2, 3, 4],
    [5, 6],
]
print("\n")
print(my_2d_list)


my_3d_list = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
]
print("\n")
print(my_3d_list[0][0][0])