#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
for i in sorted(new_dict):
        print("{}: {}".format(i, new_dict[i]))

print("--")
for i in sorted(a_dictionary):
    print("{}: {}".format(i, a_dictionary[i]))

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
for i in sorted(new_dict):
    print("{}: {}".format(i, new_dict[i]))

print("--")
for i in sorted(a_dictionary):
    print("{}: {}".format(i, a_dictionary[i]))