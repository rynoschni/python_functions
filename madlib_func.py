def madlib (name, subject):
    themadlib = "Your name is %s and your favorite subject is %s." % (name, subject)
    return themadlib

my_story = madlib("Ryan", "physics")
print(my_story)
