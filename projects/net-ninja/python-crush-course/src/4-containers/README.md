# [Python Crash Course #4 - Containers - YouTube](https://youtu.be/pJJ2uLB1_Zo?list=PL4cUxeGkcC9goeb7U1FXFdNszWetCmhfB "Python Crash Course #4 - Containers - YouTube")

Storing a single value in a variable is easy

```python
user_name = 'Bob'
all_users = ?
```

Python has several datatypes for that:  
A list a tuple, a dictionary a set

```python
Tuple = ('bob', 123, 'Lisa', ('another', ('list')))
```

```python
List = ['bob', 123, 'Lisa', ('another', ('list'))]
```

() or [] and then comma separated values

A tuple cannot change (immutable) while you can change the calues of a list

```python
Set = {1, 2, 3, 'test'}
```
Every entry in set is unique

```python
Dictionary = {'name':'Bob', 123:'test', 'Lisa': (1, 2, 3)}
```
Key:value pairs instead of single entries

## Indexing

```python
['Lisa', 'Bob', 'Alex', 'Anna', 'John']
#  0       1       2       3       4
```

```python
['Lisa', 'Bob', 'Alex', 'Anna', 'John'][1]
#          ^
```

## Slicing

```python
['Lisa', 'Bob', 'Alex', 'Anna', 'John']
#  0       1       2       3       4
```

```python
['Lisa', 'Bob', 'Alex', 'Anna', 'John'][1:4:2]
#        [<----------------->]
```

## Exercise

Create a list = (1,2,3,4,5,6,7,8,9,10)  
Create a new list: 8, 6, 4, 2
