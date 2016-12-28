# Objective: To generate simple phrases
# Expand to generate more complex phrases.

from random import randint

nouns = [
	"man",
	"woman",
	"boy",
	"girl"
]

verbs = [
	"laughs",
	"fights",
	"cries",
	"runs"
]

a = randint(0, 3)
b = randint(0, 3)

print ("The " + nouns[a] + " " + verbs[b])