# 6. Create a dictionary called people that has another dictionary
# for each Bob (age 22), Carol (age 47) and Justin (age 14)
# with their name and age.

#NOW LOOP THROUGH AND PRINT NAMES AND VALUES
people = {
    "bob" : { "age":22},
    "carol" : { "age":47},
    "ted" : { "age":14},
}

for index, person in people.items():
    print index, person["age"]

#JSON STYLE - LIST OF DICTS AKA ARRAY OR OBJECTS
people = [
    { "name": "bob", "age":22},
    { "name": "carol", "age":47},
    { "name": "ted", "age":14},
]

for person in people:
    print person["name"], person["age"]

#EFFICIENT STYLE - LIST OF LISTS AKA ARRAY OF ARRAYS
#NOTE: No clue is given that the second field is an age.
people = [
    ["bob",22],
    ["carol",47],
    ["ted",14],
]

# WITH EXTRA CR LF CARRIAGE RETURN LINE FEED
for person in people:
    for field in person:
        print field

# NOW WITH NO WITH EXTRA CR LF CARRIAGE RETURN LINE FEED AS BEFORE

for person in people:
    print person[0], person[1]
