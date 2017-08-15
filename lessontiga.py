'''
list, tuples, dictionaries

'''

a_list = ['hello', '5', 'lol'] # lists starts w/ 0, 1, 2, 3 etc.
a_tuple = ('hello', '5', 'lol')
a_dictionaries = {'greeting':'hello', 'number':'5', 'laugh':'lol'}

a_list_of_list = [['hello'],[5,'lol']] # list of lists 

print (a_list[2])
print (a_list_of_list[1][1]) # printing list of lists ----> whut?? O_O
print (a_dictionaries['greeting'])
#=====================================================
# finding hello

name_var = 'hello' in a_list
print (name_var)

#=====================================================
# for loops
#=====================================================
'''
len : find length of variable

'''

for i in range(len(a_list)):
	print (a_list[i])

# multiple assignment 'trick'

random1, random2, random3 = a_list

#=====================================================
# Basic list fns

a_list.append('add more')
a_list.index('lol')
sorted_a_list = a_list.sort() # sort by Uppercase first


print (a_list.sort())	

#=====================================================
# debugging tips
#=====================================================

print (type(a_list))


# Basic error handling

try:
	nonexistent_func()
except Exception:
	print (Exception)