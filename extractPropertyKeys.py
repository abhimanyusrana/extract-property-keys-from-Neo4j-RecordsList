# inspects all records and extracts properties mentioned in them to ensure it
# gets all. Returns a set of property values.
# it takes input in form : 'WHATEVERHAPPENS-IN-THE-QUERY return n, keys(n)'
def getPropertySet(records):
  keySet=set()
  for x in records:
    for y in x[1]:
      keySet.add(y)
  return keySet
