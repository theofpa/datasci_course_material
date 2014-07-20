import MapReduce
import sys

"""
Trim nucleotide example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    seqid = record[0]
    nucleotide = record[1]
    mr.emit_intermediate(nucleotide[:-10], 1)

def reducer(nucleotide, ncount):
    # key: word
    # value: list of occurrence counts
    mr.emit((nucleotide))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
