# copy a list to a new one
list = [ 1,2,3,4,5 ]
newList = list
list.reverse()
# using = the newList will also be reversed
print( list )
print( newList )
# using copy you create an independent list
anotherList = list.copy()
list.reverse()
print( list )
print( anotherList )