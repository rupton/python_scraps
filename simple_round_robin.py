desinations = {}

desinations[0] = 'server 01'
desinations[1] = 'server 02'
desinations[2] = 'server 03'

for req in range(1000):
    n = req % 3
    destination = desinations.get(n, 'Unknown')
    print(f"Request {req} is being routed to {destination}")