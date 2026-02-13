# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_book = {}

for _ in range(n):
    entry = input().split()
    name = entry[0]
    number = entry[1]
    phone_book[name] = number

try:
    while True:
        query = input()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
except EOFError:
    pass
