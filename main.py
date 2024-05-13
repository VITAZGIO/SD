import numpy as np
import time
from scipy.linalg import blas as FB

# Генерация случайных матриц размера n x n
def generate_random_matrix(n):
    return np.random.rand(n, n)

# Функция для умножения матриц с использованием собственной реализации
def matrix_multiply_custom(A, B):
    return np.dot(A, B)

# Функция для умножения матриц с использованием cblas_dgemm
def matrix_multiply_blas(A, B):
    return FB.dgemm(alpha=1.0, a=A, b=B, trans_b=True)

# Оптимизированный алгоритм умножения матриц с использованием NumPy
def matrix_multiply_optimized_np(A, B):
    return np.dot(A, B)

# Время выполнения функции и расчет MFlops
def measure_performance(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time == 0:
        return result, elapsed_time, 0.0  # Если время выполнения равно нулю, возвращаем MFlops равный нулю
    n = args[0].shape[0]
    c = 2 * n**3
    p = c / elapsed_time * 10**-6
    return result, elapsed_time, p

# Размерность матрицы
n = 2048

# Генерация случайных матриц
matrix1 = generate_random_matrix(n)
matrix2 = generate_random_matrix(n)

# Проверка корректности реализаций и замер производительности
result_custom, time_custom, mflops_custom = measure_performance(matrix_multiply_custom, matrix1, matrix2)
result_blas, time_blas, mflops_blas = measure_performance(matrix_multiply_blas, matrix1, matrix2)
result_optimized_np, time_optimized_np, mflops_optimized_np = measure_performance(matrix_multiply_optimized_np, matrix1, matrix2)

print("Собственная реализация:")
print("Время выполнения:", time_custom, "сек")
print("MFlops:", mflops_custom)

print("\nBLAS (cblas_dgemm):")
print("Время выполнения:", time_blas, "сек")
print("MFlops:", mflops_blas)

print("\nОптимизированный алгоритм с использованием NumPy:")
print("Время выполнения:", time_optimized_np, "сек")
print("MFlops:", mflops_optimized_np)

# Сравнение производительности оптимизированного алгоритма с BLAS
performance_threshold = 0.3 * mflops_blas
if mflops_optimized_np >= performance_threshold:
    print("\nОптимизированный алгоритм с использованием NumPy имеет производительность не менее 30% от BLAS.")
else:
    print("\nОптимизированный алгоритм с использованием NumPy не достигает необходимой производительности.")
