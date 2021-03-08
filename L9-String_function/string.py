# the \ character means escape, to prevent the string from closing
# source: https://www.reddit.com/r/AskReddit/comments/dxosj/what_word_or_phrase_did_you_totally_misunderstand/c13pbyc/
# text = "When I was young my father said to me: \"Knowledge is Power....Francis Bacon\" I understood it as \"Knowledge is power, France is Bacon\". For more than a decade I wondered over the meaning of the second part and what was the surreal linkage between the two? If I said the quote to someone, \"Knowledge is power, France is Bacon\" they nodded knowingly. Or someone might say, \"Knowledge is power\" and I'd finish the quote \"France is Bacon\" and they wouldn't look at me like I'd said something very odd but thoughtfully agree. I did ask a teacher what did \"Knowledge is power, France is bacon\" mean and got a full 10 minute explanation of the Knowledge is power bit but nothing on \"France is bacon\". When I prompted further explanation by saying \"France is Bacon?\" in a questioning tone I just got a \"yes\". at 12 I didn't have the confidence to press it further. I just accepted it as something I'd never understand. It wasn't until years later I saw it written down that the penny dropped."

text = 'And I say heyayayeyay.'

# lower case
print(text.lower())


# # upper case
# print(text.upper())

# split the text by " ": it will return a list
split = text.split(" ")

print(split)

# join an array by a string object
glue = " "
join = glue.join(split)
join = " ".join(split)

# replace
replace = text.replace('say', 'call')
print(replace)

# format
text3 = "My name is {0}, I'm learning {1}"
print(text3.format('Shiny', "Python"))

text3 = "My name is {1}, I'm learning {0}"
print(text3.format('Shiny', "Python"))


text4 = "My name is {name}, I'm learning {topic}"
print(text4.format(name='Crazy', topic="Python"))

 