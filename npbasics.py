Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
print(np.__version__)
1.23.5
arr=np.array([1,2,3])
print(arr)
[1 2 3]
print(arr[2])
3
a=np.array([[1,2,3],[4,5,6]])
print(a)
[[1 2 3]
 [4 5 6]]
print(a.ndim)
2
print(arr.ndim)
1
print(type(arr))
<class 'numpy.ndarray'>
a=np.array(['apple','ball','cat'])
print(a)
['apple' 'ball' 'cat']
print(a.dtype())
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(a.dtype())
TypeError: 'numpy.dtype[str_]' object is not callable
print(a.dtype)
<U5
print(type(a))
<class 'numpy.ndarray'>
print(a[2])
cat
print(a[2[1]])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(a[2[1]])
TypeError: 'int' object is not subscriptable
b=a[2]
print(b[2])
t
k=np.array(['a','b','c'],dtype='S2')
print(k)
[b'a' b'b' b'c']
k=np.array(['a','b','c'],dtype='U2')
print(k)
['a' 'b' 'c']
p=k.astype(i)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    p=k.astype(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
p=k.astype('i')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    p=k.astype('i')
ValueError: invalid literal for int() with base 10: 'a'
p=arr.astype(int)
print(p)
[1 2 3]
print(p.dtype)
int32
arr = np.array([[-1, 2, 0, 4],
				[4, -0.5, 6, 0],
				[2.6, 0, 7, 8],
				[3, -7, 4, 2.0]])
print(arr.ndim)
SyntaxError: multiple statements found while compiling a single statement
arr = np.array([[-1, 2, 0, 4],[4, -0.5, 6, 0],[2.6, 0, 7, 8],[3, -7, 4, 2.0]])
print(arr.ndim)
2
print(arr[2,1:4])
[0. 7. 8.]
print(a[1,3])
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(a[1,3])
IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed
print(a[1,1:2])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(a[1,1:2])
IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed
a=np.array([1,2,3,4,5])
print(a+2)
[3 4 5 6 7]
print(a-3)
[-2 -1  0  1  2]
print(a*3)
[ 3  6  9 12 15]
print(a**2)
[ 1  4  9 16 25]
print(a.dot)
<built-in method dot of numpy.ndarray object at 0x00000189AE600570>
b=np.array([[1,5,7],[6,2,3],[6,7,9]])
print(b)
[[1 5 7]
 [6 2 3]
 [6 7 9]]
print(b.T)
[[1 6 6]
 [5 2 7]
 [7 3 9]]
print(a.T)
[1 2 3 4 5]
print(a.max())
5
print(b.max(axis=0))
[6 7 9]
print(b.max(axis=1))
[7 6 9]
print(b.max(axis=2))
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(b.max(axis=2))
  File "C:\Users\Lavanya\AppData\Roaming\Python\Python310\site-packages\numpy\core\_methods.py", line 40, in _amax
    return umr_maximum(a, axis, None, out, keepdims, initial, where)
numpy.AxisError: axis 2 is out of bounds for array of dimension 2
c=np.array([[[1,2,3],[4,5,6]],[6,7,8],[11,22,33]])

Warning (from warnings module):
  File "<pyshell#49>", line 1
VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
c=np.array([[[1,2,3],[4,5,6]],[[6,7,8],[11,22,33]]])
print(c)
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 6  7  8]
  [11 22 33]]]
print(c.ndim)
3
print(c.dtype)
int32

print(c.,max(axis=2))
SyntaxError: invalid syntax
print(c.max(axis=2))
[[ 3  6]
 [ 8 33]]
print(c.min(axis=1))
[[1 2 3]
 [6 7 8]]
print(c.min(axis=0))
[[1 2 3]
 [4 5 6]]
print(b.min(axis=1))
[1 2 6]
print(b)
[[1 5 7]
 [6 2 3]
 [6 7 9]]
print(b.min(axis=0))
[1 2 3]
print(c.sum(axis=0))
[[ 7  9 11]
 [15 27 39]]
d=np.array([[[[1,2,3],[4,5,6]],[[7,8,9]]],[[11,22,33]]])
print(d)
[list([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]]) list([[11, 22, 33]])]
print(d.ndim)
1
d=np.array([[[1,2,3],[4,5,6]]])
print(d)
[[[1 2 3]
  [4 5 6]]]
print(d.ndim)
3
e=np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]],[[[4,5,6],[7,8,9]],[[1,2,3],[4,5,6]]]])
print(e)
[[[[1 2 3]
   [4 5 6]]

  [[7 8 9]
   [1 2 3]]]


 [[[4 5 6]
   [7 8 9]]

  [[1 2 3]
   [4 5 6]]]]
print(e.ndim)
4
print(e.dtype)
int32
print(e.max(axis=0))
[[[4 5 6]
  [7 8 9]]

 [[7 8 9]
  [4 5 6]]]
print(e.min(axis=1))
[[[1 2 3]
  [1 2 3]]

 [[1 2 3]
  [4 5 6]]]
print(e.sum(axis=2))
[[[ 5  7  9]
  [ 8 10 12]]

 [[11 13 15]
  [ 5  7  9]]]
print(e.sum(axis=3))
[[[ 6 15]
  [24  6]]

 [[15 24]
  [ 6 15]]]
print(e.max(axis=4))
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print(e.max(axis=4))
  File "C:\Users\Lavanya\AppData\Roaming\Python\Python310\site-packages\numpy\core\_methods.py", line 40, in _amax
    return umr_maximum(a, axis, None, out, keepdims, initial, where)
numpy.AxisError: axis 4 is out of bounds for array of dimension 4
print(a.dot(b))
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print(a.dot(b))
ValueError: shapes (5,) and (3,3) not aligned: 5 (dim 0) != 3 (dim 0)
print(b)
[[1 5 7]
 [6 2 3]
 [6 7 9]]
print(a)
[1 2 3 4 5]
>>> f=np.array([[1,2,3],[4,5,6]])
>>> print(f)
[[1 2 3]
 [4 5 6]]
>>> print(e.dot(f))
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print(e.dot(f))
ValueError: shapes (2,2,2,3) and (2,3) not aligned: 3 (dim 3) != 2 (dim 0)
>>> print(b.dot(f))
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    print(b.dot(f))
ValueError: shapes (3,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)
>>> f=np.array([[1,2,3],[4,5,6],[6,7,8]])
>>> print(b.dot(f))
[[ 63  76  89]
 [ 32  43  54]
 [ 88 110 132]]
>>> print(f)
[[1 2 3]
 [4 5 6]
 [6 7 8]]
>>> print(np.add(a))
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    print(np.add(a))
TypeError: add() takes from 2 to 3 positional arguments but 1 were given
>>> print(np.add(a,2))
[3 4 5 6 7]
>>> print(np.multiply(b,f))
[[ 1 10 21]
 [24 10 18]
 [36 49 72]]
>>> print(np.sin(a))
[ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427]
>>> print(np.sqrt(b))
[[1.         2.23606798 2.64575131]
 [2.44948974 1.41421356 1.73205081]
 [2.44948974 2.64575131 3.        ]]
