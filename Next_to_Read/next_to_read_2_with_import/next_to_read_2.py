import bookLists
import random

series = bookLists.bookSeriesList

bookSelected = random.randint(1, len(series))
print("Next book series to read is number {} - {} ".format(bookSelected+1, series[bookSelected]))
