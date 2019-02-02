from collections import defaultdict, namedtuple, Counter, deque

# NAMED TUPLE
# A namedtuple is a convenient way to define a class without methods
User = namedtuple('User', 'name role')
user = User(name='john', role='coder')
print(user.name, user.role)

# DEFAULT DICT
# useful for building up a nested data structure when keys 
# might not already exist in the dict. 
# defaultdict takes a datatype that is the default type for a 
# key that doesn't exist yet. 
scores = [('dana', 10), ('john', 10), ('charlie', 11)]
scores_dict = defaultdict(int)
for name, score in scores:
	scores_dict[name] = score
print(scores_dict)


scores = [('dana', 10), ('dana', 10), ('dana', 11), ('dana', 10), ('john', 10), ('charlie', 11)]
scores_dict = defaultdict(set)
for name, score in scores:
	scores_dict[name].add(score)
print(scores_dict)


# COUNTER
words = "hello hello, is anybody there? Nobody is there!".split(" ")
count = Counter(words).most_common(3)
print(count)

# DEQUES
# double ended queue.
# lists in python are great but some operations, 
# like delete and insert can get slow when 
# your list grows.
# If you need to add/remove at both ends, consider a DEQUE

# inserting/deleting into the middle of a deque
# is quicker than in a plain list. 