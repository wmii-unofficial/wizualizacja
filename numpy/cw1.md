
**Zadanie 1**

_Za pomocą funkcji arange stwórz tablicę Numpy składającą się 20 kolejnych wielokrotności liczby 2_


```python
import numpy as np #przyda się właściwie zawsze, stąd na początku
#w przypadku braku definicji zapraszam na http://wmii.uwm.edu.pl/~kropiak/wd/6_Biblioteka%20Numpy%201.pdf
```


```python
arr = np.arange(2, 2*21, 2)
arr
```




    array([ 2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34,
           36, 38, 40])



**Zadanie 2**

_Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int64_


```python
arr2 = np.random.randn(5)*10
arr2i = np.array(arr2, dtype='int64')
arr2, arr2i
```




    (array([ 7.93967188,  6.96147026, -5.90763086, -0.55270008,  9.10507197]),
     array([ 7,  6, -5,  0,  9]))



**Zadanie 3**

Napisz funkcję, którabędzie:
- przyjmowała jeden parametr‘n’w postaci liczby całkowitej
- zwracała tablicę Numpy o wymiarach n x n kolejnych liczb całkowitych poczynając od 1


```python
def magic_array(n):
    return np.arange(1,n*n+1).reshape(n,n)

magic_array(10)
```




    array([[  1,   2,   3,   4,   5,   6,   7,   8,   9,  10],
           [ 11,  12,  13,  14,  15,  16,  17,  18,  19,  20],
           [ 21,  22,  23,  24,  25,  26,  27,  28,  29,  30],
           [ 31,  32,  33,  34,  35,  36,  37,  38,  39,  40],
           [ 41,  42,  43,  44,  45,  46,  47,  48,  49,  50],
           [ 51,  52,  53,  54,  55,  56,  57,  58,  59,  60],
           [ 61,  62,  63,  64,  65,  66,  67,  68,  69,  70],
           [ 71,  72,  73,  74,  75,  76,  77,  78,  79,  80],
           [ 81,  82,  83,  84,  85,  86,  87,  88,  89,  90],
           [ 91,  92,  93,  94,  95,  96,  97,  98,  99, 100]])




```python
#zadanie 4
def numbers(n,m):
    return np.logspace(base=n, start=1, stop=m, num=m, dtype='int64')

numbers(2,4)
```




    array([ 2,  4,  8, 16])




```python
#zadanie 5
def reversed_eye(n):
    m = np.arange(n,0,-1)
    return np.eye(n)*m

reversed_eye(3)
```




    array([[3., 0., 0.],
           [0., 2., 0.],
           [0., 0., 1.]])




```python
#zadanie 6
wykreslanka = np.empty((5,5), dtype='U1')
wykreslanka[2,:] = list('kotek')
wykreslanka[:,2] = list('tutej')
slowo = 'metot' #totem
for i in range(5):
    wykreslanka[i,i] = list(slowo)[i] 
wykreslanka
```




    array([['m', '', 't', '', ''],
           ['', 'e', 'u', '', ''],
           ['k', 'o', 't', 'e', 'k'],
           ['', '', 'e', 'o', ''],
           ['', '', 'j', '', 't']], dtype='<U1')




```python
#zadanie 7
def magic(n):
    arr = np.eye(n,dtype='int64')*2
    for i in range(1,n):
        v = np.ones(n-i,dtype='int64')*2*(i+1)
        arr += np.diag(v, k=i) + np.diag(v, k=-i) 
    return arr

magic(3)
```




    array([[2, 4, 6],
           [4, 2, 4],
           [6, 4, 2]])




```python
#zadanie 8
def dziel(arr, kierunek):
        if kierunek=='poziomo' and arr.shape[0]%2==1:
            return []
        elif kierunek=='pionowo' and arr.shape[1]%2==1:
            return []
        
        if kierunek=='pionowo':
            return arr[:,0:arr.shape[1]//2], arr[:,arr.shape[1]//2:]
        elif kierunek=='poziomo':
            return arr[0:arr.shape[0]//2,:], arr[arr.shape[0]//2:,:]

arr = np.arange(16).reshape(2,8)
dziel(arr, 'pionowo')
```




    (array([[ 0,  1,  2,  3],
            [ 8,  9, 10, 11]]), array([[ 4,  5,  6,  7],
            [12, 13, 14, 15]]))




```python
#zadanie 9
def fibonacci_arr(n):
    arr = np.ones(2,dtype='int64')
    for i in range(n*n-2):
        arr = np.append(arr, np.sum(arr[-2:]))
    return arr.reshape(n,n)

fibonacci_arr(5)
```




    array([[    1,     1,     2,     3,     5],
           [    8,    13,    21,    34,    55],
           [   89,   144,   233,   377,   610],
           [  987,  1597,  2584,  4181,  6765],
           [10946, 17711, 28657, 46368, 75025]])




```python

```
