import random

bookLists = open('bookLists.txt').read().splitlines()
listCount = len(bookLists)
bookSelected = random.randint(1, listCount)

print("Next book series to read is number {} - {} ".format(bookSelected+1, bookLists[bookSelected]))
