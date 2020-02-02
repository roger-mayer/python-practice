# lists!

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])  # trek
print(bicycles[0].title())  # Trek
print(bicycles[-1])  # last in list (specialized)

message = f"My first bicycle was a {bicycles[3].title()}."
print(message)

bicycles[3] = 'state'  # reassign
print(bicycles)

bicycles.append('specialized')  # add to list
print(bicycles)

bicycles.insert(2, 'huffy')  # insert into list
print(bicycles)

bicycles.pop()  # remove last item
print(bicycles)

bicycles.pop(2)  # remove at index
print(bicycles)

bicycles.remove('redline')  # remove based on value
print(bicycles)

for bike in bicycles:
    print(f'{bike.title()} is a bicycle')

