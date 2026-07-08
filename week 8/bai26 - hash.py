def order_independent_hash(set_items): return sum(hash(x) for x in set_items)
print(order_independent_hash({1, 2}) == order_independent_hash({2, 1}))