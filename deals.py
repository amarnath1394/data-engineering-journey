deals = [
    {"name": "Deal A", "vertical": "BFS", "amount": 1200000, "stage": "Won"},
    {"name": "Deal B", "vertical": "INS", "amount": 800000, "stage": "Open"},
    {"name": "Deal C", "vertical": "BFS", "amount": 500000, "stage": "Lost"},
     {"name": "Deal D", "vertical": "BFS", "amount": 500000, "stage": "Lost"},
    {"name": "Deal E", "vertical": "INS", "amount": 500000, "stage": "Won"},
     {"name": "Deal F", "vertical": "BFS", "amount": 500000, "stage": "Lost"},
     {"name": "Deal G", "vertical": "OI", "amount": 500000, "stage": "Lost"},

]

total_by_vertical = {}
for deal in deals:
    vertical=deal["vertical"]
    if vertical not in total_by_vertical:
        total_by_vertical[vertical]=0
        total_by_vertical[vertical] += deal["amount"]
print(total_by_vertical)
