# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
a = "aaaaabbbbccc"
my_counter = Counter(a) # Counter({"a": 5, "b": 4, "c": 3})
my_counter.most_common(2) # [("a", 5),("b", 4)] returns list with tuples
my_counter.most_common(1)[0][0] # most common, first tuple in list, first element = a
list(my_counter.elements()) # ["a", "a", "a", "a", "a", "b", "b", "b", "b", "c", "c", "c"]

from collections import namedtuple
Point = namedtuple("Point", "x,y")
pt = Point(1, -4) # Point(x=1, y=-4), pt.x and pt.y to access values of the class

from collections import OrderedDict
#dictionary but remembers the order, Python 3.7+ supports that natively, no reason to use on new Python versions

from collections import defaultdict
d = defaultdict(int)
d["a"] = 1
d["b"] = 2
# d["a"] is 1, d["b"] is 2, d["everything else"] is 0(default int value)

from collections import deque
d = deque()
d.append(1)
d.append(2)
print(d) # deque([1, 2])
d.appendleft(3) # deque([3, 1, 2])
d.pop() # deque([3, 1]), removes last item
d.popleft() # deque([1]), removes first item
d.clear()
d.extend(4,5,6) # appends elements on the right (1,4,5,6)
d.extendleft(4,5,6) # extends on the left (6,5,4,1), reverse order
d.rotate(1) # 6541 becomes 1654, all to the right, last goes to first place, -1 for left rotation