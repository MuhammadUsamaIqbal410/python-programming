# Applying filter to extract the specific liength length words
words = ["good", "curious", "moody", "goofy", "attractive", "bad",]

def sepcific_length(x):
    return len(x)>5
filtered = list(filter(sepcific_length, words))
print(filtered)

# Contrarily

filtered = list(filter(lambda x : len(x)>5, words))
print(filtered)

