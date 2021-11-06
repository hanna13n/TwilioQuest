import sys
order_of_succession = sys.argv
order_of_succession.pop(0)
for i, j in enumerate(order_of_succession, 1):
    print(f"{i}.{j}")
