
# putting all of our code in 1 file is not practical
# we would end up having 1 million lines of code in 1 file
# hard to maintain and very messy
# easy to have variable names collision

# module is the idea of separating our code into smaller, manageable chunk
# everything in a module stays inside a module, unless we import it
# whenever we want to use a component eg function inside a module, we just need to import it
# We also refer modules as libraries

# the random module that we've been using is a perfect example
# the functions are contained within the module, without polluting the global scope



from quotes import inspire, count

quote = inspire()
print(quote)



