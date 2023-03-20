import pickle
list = ['a', 'b', 'c']
with open('list.txt', 'wb') as f:
    pickle.dump(list, f)
with open('list.txt', 'rb') as file:
    data = pickle.load(file)
    
print(data)