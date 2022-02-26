import sys
from queue import PriorityQueue
import collections
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

class Order(object):
    oid = ''
    price = -1
    quantity = -1
    timestamp = -1

    def __init__(self, oid, price, quantity, timestamp):
        self.oid = oid
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp

    def __str__(self):
        # Quantity @ Price # OrderID
        return str(self.quantity) + '@' + str(self.price) + "#" + str(self.oid)

class BuyOrder(Order):

    def __lt__(self, other):
        if self.price > other.price:
            return True
        elif self.price == other.price:
            if self.timestamp < other.timestamp:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        if self.price == other.price and self.timestamp == other.timestamp:
            return True
        else:
            return False

class SellOrder(Order):

    def __lt__(self, other):
        if self.price < other.price:
            return True
        elif self.price == other.price:
            if self.timestamp < other.timestamp:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        if self.price == other.price and self.timestamp == other.timestamp:
            return True
        else:
            return False

# test data

if __name__ == "__main__":
    q = PriorityQueue()
    priorities = [(3, 2), (3, 1), (1, 2), (1, 1), (2, 1), (2, 2)]


    # 通过OrderedDict类创建的字典是有序的
    dic = collections.OrderedDict()

    for i in range(len(priorities)):
        dic[i] = SellOrder(i, priorities[i][0], i * 2 ,priorities[i][1])
        # q.put(SellOrder(i, priorities[i][0], i *2 ,priorities[i][1]))

    # print(dic)
    print(sorted(dic.items(), key=lambda x: x[1]))

    # while not q.empty():
    #     data = q.get()
    #     print(data.price, data.timestamp)