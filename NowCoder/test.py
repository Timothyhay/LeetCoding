# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections
import sys
from queue import PriorityQueue


# Order Class
class Order(object):
    oid = ''
    price = -1
    quantity = -1
    timestamp = -1
    otype = ''
    display = -1

    def __init__(self, oid, price, quantity, total_quantity, otype, timestamp):
        self.oid = oid
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp
        self.otype = otype
        self.total_quantity = total_quantity

    def __str__(self):
        # Quantity @ Price # OrderID
        if self.otype == "ICE":
            return str(self.quantity) + '(' + str(self.total_quantity) + ')@' + str(self.price) + "#" + str(self.oid)
        else:
            return str(self.quantity) + '@' + str(self.price) + "#" + str(self.oid)


# Hashmap can find cancel_orders in O(1), also remains the order(priority) of input with OrderedDict
buy_orders = collections.OrderedDict()
sell_orders = collections.OrderedDict()


# So BuyOrder and SellOrder extend the Order with different __cmp__ functions to use in priority queue
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


# Actions
# Submit
def submit(side, otype, oid, price, quantity, display, timestamp):
    crt_traded = 0
    # Match: (newly come) buy_price >= sell_price (with 1st priority)
    if side == 'B':
        sell_orders_list = sorted(sell_orders.items(), key=lambda x: x[1])
        # Add to the queue when empty
        if len(sell_orders_list) == 0:
            if otype == "LO":
                # __init__(self, oid, price, quantity, total_quantity, otype, timestamp):
                buy_orders[oid] = BuyOrder(oid, price, quantity, -1, otype, timestamp)
            return 0

        if otype == "LO" or otype == "IOC" or otype == "FOK":
            # Highest Priority sell_order instance = sell_orders_list[0][1]
            crt_sell_orders_quantity = sell_orders_list[0][1].quantity
            crt_sell_orders_price = sell_orders_list[0][1].price
            crt_sell_orders_id = sell_orders_list[0][1].oid
            # Sorted list pointer, use it to avoid sorting original hashmap
            ptr = 0
            # For FOK: Check if can be executed fully
            if otype == "FOK" and quantity < crt_sell_orders_quantity:
                return 0

            # Not Matched
            if price < crt_sell_orders_price:
                if otype == "LO":
                    # __init__(self, oid, price, quantity, total_quantity, otype, timestamp):
                    buy_orders[oid] = BuyOrder(oid, price, quantity, -1, otype, timestamp)
                return 0
            # Matched
            elif price >= crt_sell_orders_price:
                while quantity >= crt_sell_orders_quantity:
                    if price >= crt_sell_orders_price:
                        quantity -= crt_sell_orders_quantity
                        crt_traded += crt_sell_orders_quantity * crt_sell_orders_price

                        # Update the priority queue
                        sell_orders.pop(crt_sell_orders_id)
                        ptr += 1
                        # sell_orders_list = sorted(sell_orders.items(), key=lambda x: x[1])
                        if ptr == len(sell_orders_list):
                            break
                        crt_sell_orders_quantity = sell_orders_list[ptr][1].quantity
                        crt_sell_orders_price = sell_orders_list[ptr][1].price
                        crt_sell_orders_id = sell_orders_list[ptr][1].oid
                # Add with remaining quantity
                if quantity != 0:
                    if otype == "LO":
                        # __init__(self, oid, price, quantity, total_quantity, otype, timestamp):
                        buy_orders[oid] = BuyOrder(oid, price, quantity, -1, otype, timestamp)
                    elif otype == "IOC":
                        sell_orders[crt_sell_orders_id].quantity -= quantity
                        crt_traded += quantity * crt_sell_orders_price
                return crt_traded
        # Market Order
        elif otype == "MO":
            crt_sell_orders_quantity = sell_orders_list[0][1].quantity
            crt_sell_orders_price = sell_orders_list[0][1].price
            crt_sell_orders_id = sell_orders_list[0][1].oid
            # Sorted list pointer, use it to avoid sorting original hashmap
            ptr = 0
            empty_queue = False
            while quantity >= crt_sell_orders_quantity:
                quantity -= crt_sell_orders_quantity
                crt_traded += crt_sell_orders_quantity * crt_sell_orders_price

                # Update the priority queue
                sell_orders.pop(crt_sell_orders_id)
                # sell_orders_list = sorted(sell_orders.items(), key=lambda x: x[1])
                ptr += 1
                if ptr == len(sell_orders_list):
                    empty_queue = True
                    break

                crt_sell_orders_quantity = sell_orders_list[ptr][1].quantity
                crt_sell_orders_price = sell_orders_list[ptr][1].price
                crt_sell_orders_id = sell_orders_list[ptr][1].oid
            if empty_queue == False and quantity != 0:
                sell_orders[crt_sell_orders_id].quantity -= quantity
                crt_traded += quantity * crt_sell_orders_price
            return crt_traded
    elif side == 'S':
        buy_orders_list = sorted(buy_orders.items(), key=lambda x: x[1])
        if len(buy_orders_list) == 0:
            if otype == "LO":
                sell_orders[oid] = SellOrder(oid, price, quantity, timestamp)
            return 0
        # Limit and Immediate-or-Cancel Order
        if otype == "LO" or otype == "IOC" or otype == "FOK":
            # Highest Priority buy_order instance = buy_orders_list[0][1]
            crt_buy_orders_quantity = buy_orders_list[0][1].quantity
            crt_buy_orders_price = buy_orders_list[0][1].price
            crt_buy_orders_id = buy_orders_list[0][1].oid
            # Sorted list pointer, use it to avoid sorting original hashmap
            ptr = 0

            # For FOK: Check if can be executed fully
            if otype == "FOK" and quantity < crt_buy_orders_quantity:
                return 0

            # Not Matched
            if crt_buy_orders_price < price:
                # __init__(self, oid, price, quantity, total_quantity, otype, timestamp):
                if otype == "LO":
                    sell_orders[oid] = SellOrder(oid, price, quantity, -1, otype, timestamp)
                return 0
            # Matched
            elif crt_buy_orders_price >= price:
                while quantity >= crt_buy_orders_quantity:
                    if price >= crt_buy_orders_price:
                        quantity -= crt_buy_orders_quantity
                        crt_traded += crt_buy_orders_quantity * crt_buy_orders_price

                        # Update the priority queue
                        buy_orders.pop(crt_buy_orders_id)
                        ptr += 1
                        # buy_orders_list = sorted(buy_orders.items(), key=lambda x: x[1])
                        if len(buy_orders_list) == ptr:
                            break
                        crt_buy_orders_quantity = buy_orders_list[ptr][1].quantity
                        crt_buy_orders_price = buy_orders_list[ptr][1].price
                        crt_buy_orders_id = buy_orders_list[ptr][1].oid
                # Add with remaining quantity
                if quantity != 0:
                    if otype == "LO":
                        # __init__(self, oid, price, quantity, total_quantity, otype, timestamp):
                        sell_orders[oid] = SellOrder(oid, price, quantity, -1, otype, timestamp)
                    elif otype == "IOC":
                        buy_orders[crt_buy_orders_id].quantity -= quantity
                        crt_traded += quantity * crt_buy_orders_price
                return crt_traded

        # Market Order
        elif otype == "MO":
            crt_buy_orders_quantity = buy_orders_list[0][1].quantity
            crt_buy_orders_id = buy_orders_list[0][1].oid
            crt_buy_orders_price = buy_orders_list[0][1].price
            # Sorted list pointer, use it to avoid sorting original hashmap
            ptr = 0
            empty_queue = False
            while quantity >= crt_buy_orders_quantity:
                quantity -= crt_buy_orders_quantity
                crt_traded += crt_buy_orders_quantity * crt_buy_orders_price

                # Update the priority queue
                buy_orders.pop(crt_buy_orders_id)
                ptr += 1
                # buy_orders_list = sorted(buy_orders.items(), key=lambda x: x[1])
                if len(buy_orders_list) == ptr:
                    empty_queue = True
                    break
                crt_buy_orders_quantity = buy_orders_list[ptr][1].quantity
                crt_buy_orders_price = buy_orders_list[ptr][1].price
                crt_buy_orders_id = buy_orders_list[ptr][1].oid
            if empty_queue == False and quantity != 0:
                buy_orders[crt_buy_orders_id].quantity -= quantity
                crt_traded += quantity * crt_buy_orders_price
            return crt_traded
    else:
        pass


# Cancel
def cancel(oid):
    if oid in buy_orders:
        buy_orders.pop(oid)
    elif oid in sell_orders:
        sell_orders.pop(oid)


# Cancel/Replace Limit Order
def update(oid, quantity, price, timestamp):
    if oid in buy_orders:
        if buy_orders[oid].otype != "LO":
            return
        # When only quantity decrease, timestamp remains the same
        if price == buy_orders[oid].price and quantity <= buy_orders[oid].quantity:
            buy_orders[oid].quantity = quantity
        else:
            # old_order = buy_orders.pop(oid)
            #  __init__(self, oid, price, quantity, display, otype, timestamp):
            buy_orders[oid] = BuyOrder(oid, price, quantity, -1, "LO", timestamp)

    elif oid in sell_orders:
        if sell_orders[oid].otype != "LO":
            return
        # When only quantity decrease, timestamp remains the same
        if price == sell_orders[oid].price and quantity <= sell_orders[oid].quantity:
            sell_orders[oid].quantity = quantity
        else:
            # old_order = sell_orders.pop(oid)
            #  __init__(self, oid, price, quantity, display, otype, timestamp):
            sell_orders[oid] = SellOrder(oid, price, quantity, -1, "LO", timestamp)


# Travers OB
def travers_OB():
    print("B:", end='')
    for key, order in sorted(buy_orders.items(), key=lambda x: x[1]):
        # print(' ' + order.quantity + '@' + order.price + '#' + key)
        print(' ' + str(order), end='')
    print("\nS:", end='')
    for key, order in sorted(sell_orders.items(), key=lambda x: x[1]):
        print(' ' + str(order), end='')


for timestamp, line in enumerate(sys.stdin):
    details = line.split()

    if line == 'END':
        break
    action_type = details[0]

    if action_type == "SUB":
        order_type, side, order_id, quantity = details[1], details[2], details[3], int(details[4])
        if order_type == "MO":
            price = -1
        else:
            price = int(details[5])
        if order_type == "ICE":
            total_quantity = int(details[5])
        else:
            total_quantity = -1
        #  __init__(self, oid, price, quantity, -1, otype, timestamp):
        # For ICE: (self, oid, price, display_size, total_quantity, otype, timestamp):
        # (quantity = display_size, and the real total_quantity = total_quantity)
        print(submit(side, order_type, order_id, price, quantity, total_quantity, timestamp))
    elif action_type == "CXL":
        cancel(details[1])
    elif action_type == "CRP":
        update(order_id, quantity, price, timestamp)

travers_OB()
