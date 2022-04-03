import numpy as np

### Вычисления с помощью Numpy

### задание 1

a = np.array([[1,2,3,3,1],[6,8,11,10,7]])
print(a)
a = a.transpose()
mean_a = a.mean(axis=0)
print("Средние значения столбцов: {}".format(mean_a))

### задание 2

a_centered = a - mean_a
print(a_centered)

### задание 3

a_centered_sp = a_centered[:,0] @ a_centered[:,1]
print(a_centered_sp/(len(a_centered)-1))

### задание 4

print(np.cov(a.transpose()))
### в ковариацинной матрице мы получили элемент (0,1)=2.0, что равно значению элемента a_centered_sp/(len(a_centered)-1) вычесленному выше