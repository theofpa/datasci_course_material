import MapReduce
import sys

"""
Invert index
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    recordtype = record[0]
    order_id = record[1]
    data = []
    if recordtype=='order':
      for i in range(2,9):
        data.append(record[i])
        mr.emit_intermediate(recordtype, order_id, data)

def reducer(recordtype, order_id, data):
    # key: word
    # value: list of occurrence counts
    total = []
    for v in data:
      if v not in total:
        total.append(v)
    mr.emit((order_id, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
