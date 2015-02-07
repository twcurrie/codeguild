def greeting(name):
    greeting_string = "Class, this is {0}\nSay \"Hello\" to {0}\n\"Hello {0}!\"\n"
    return greeting_string.format(name)

def print_greeting(name):
    print greeting(name)
    return None

names = ['t','r','e']

for name in names:
    print_greeting(name)
