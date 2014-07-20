import MapReduce
import sys

"""
Relational Join using MapReduce
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(order_id, record):
    # key: word
    # value: list of occurrence counts
    for v in record:
      if v[0]=='order':
        for j in record:
          if j[0]=='line_item':
            mr.emit((v + j))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
