# lists are like arrays in javascript
fruits = ['apple','orange','watermelon','grapefruit']

print(fruits)

print( fruits[2] )
# add 'pear' to the end of fruits
fruits.append('pear')

print(fruits)
# count how many times 'apple' appear in the list
print( fruits.count('apple') )

print( len(fruits) )

#delete an item from the list -> item with index 1 ('orange')
del fruits[1]
print( fruits )