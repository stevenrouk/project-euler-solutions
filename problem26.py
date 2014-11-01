""" This is the python script used to solve Problem 26 on Project Euler. """

from decimal import getcontext, Decimal
import re

PRECISION = 5000
getcontext().prec = PRECISION

# Create the list l which will hold all of the divisions 1/x, from x = 1 to 999.
l = []

# Use the Decimal library to find the decimal approximations of 1/x to a precision of 5000 decimal places.
for x in range(1,1000):
  l.append( str( Decimal(1) / Decimal(x) ) )

# This function checks for repeating patterns in a string.
def repetitions(s):
  r = re.compile(r"(.+?)\1+")
  for match in r.finditer(s):
    yield (match.group(1), len(match.group(0)) / len(match.group(1)))

anslist = []

for x in l:
  anslist.append(list(repetitions(x)))

biglist = []

for x in range(len(anslist)):
  for i in anslist[x]:
    biglist.append([x, long(i[0]) ] )

maxlen = 0

trueans = []

for x in biglist:
  if len(str(x[1])) > maxlen:
    maxlen = len(str(x[1]))
    trueans.append(x)

print trueans[len(trueans)-1][0] + 1
