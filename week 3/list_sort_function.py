# using custom function to sort a list
# function to return length of a word
def letters( word ) :
  return len(word)

# list
list = ['flower','cloud','sun','grass']
# sort the list using the custom function
list.sort( key=letters )
# ordered by the length of each word ascending
print( list )
# do it in reverse order
list.sort( key=letters, reverse=True )
print( list )