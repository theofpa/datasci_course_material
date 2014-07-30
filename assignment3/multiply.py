import MapReduce
import sys

"""
Matrix Multiplication in Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# sample
# ["a", 4, 2, 96]
# ["a", 4, 3, 27]
# ["b", 0, 0, 63]
# ["b", 0, 1, 18]

def mapper(record):
    matrix = record[0]
    if matrix=='a':
        for i in range(5):
            pos=(record[1],i)
            mr.emit_intermediate(pos,record)
    elif matrix=='b':
        for i in range(5):
            pos=(i,record[2])
            mr.emit_intermediate(pos,record)

def reducer(pos, record):
    a = {}
    b = {}
    for r in record:
        if r[0]=='a':
            a[r[2]]=r[3]
        elif r[0]=='b':
            b[r[1]]=r[3]
    total=0
    for i in range(5):
        try:
            total+=a[i]*b[i]
        except:
            continue
    mr.emit((pos[0],pos[1],total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
