import pickle
fruits=['apples', 'oranges', 'bananas']
x=7
y=3.14
nuts=['pecans', 'almond']
grades=[99,100,56,77,85]

with open('myData.pkl', 'wb') as f:
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(nuts,f)
    pickle.dump(grades,f)
    pickle.dump(fruits,f)
    pickle.dump(3,f) 
    
with open('myData.pkl', 'rb') as f2:
    a=pickle.load(f2)
    b=pickle.load(f2)
    c=pickle.load(f2)
    d=pickle.load(f2)
    e=pickle.load(f2)
    f=pickle.load(f2)
    
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

    
    