import math

def newton_method(f, df, x0, eps=1e-6, max_iter=100):
    """Метод касательных"""
    x = x0
    for n in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-12:
            break
        x_new = x - fx / dfx
        if abs(x_new - x) < eps:
            return x_new, n+1
        x = x_new
    return x, max_iter

def chord_method(f, a, b, eps=1e-6, max_iter=100):
    """Метод хорд"""
    fa, fb = f(a), f(b)
    x_prev = b
    for n in range(max_iter):
        x = a - (fa * (b - a)) / (fb - fa)
        fx = f(x)
        delta = abs(x - x_prev)
        if abs(fx) < eps or delta < eps:
            return x, n+1
        if fa * fx < 0:
            b, fb = x, fx
        else:
            a, fa = x, fx
        x_prev = x
    return x, max_iter

def combined_method(f, df, a, b, eps=1e-6, max_iter=100):
    """Комбинированный метод"""
    for n in range(max_iter):
        x_chord = a - (f(a) * (b - a)) / (f(b) - f(a))
        x_newton = b - f(b) / df(b)
        a, b = x_chord, x_newton
        if abs(b - a) < eps:
            return (a + b) / 2, n+1
    return (a + b) / 2, max_iter

def f(x):
    return 2 * math.log10(x + 7) - 5 * math.sin(x)

def df(x):
    return (2 / ((x + 7) * math.log(10))) - 5 * math.cos(x)

# Параметры 
a, b = 2.7, 2.8
x0 = 2.75  # начальное приближение

print("ЗАДАНИЕ 7a: 2 lg(x + 7) - 5 sin(x) = 0")
print("Интервал: (2.7; 2.8)")
print()

# Запуск методов
root_newton, iter_newton = newton_method(f, df, x0)
root_chord, iter_chord = chord_method(f, a, b)
root_combined, iter_combined = combined_method(f, df, a, b)

print("РЕЗУЛЬТАТЫ:")
print(f"Метод касательных:  x = {root_newton:.6f} (итераций: {iter_newton})")
print(f"Метод хорд:         x = {root_chord:.6f} (итераций: {iter_chord})")
print(f"Комбинированный:    x = {root_combined:.6f} (итераций: {iter_combined})")

# Проверка
print(f"\nПроверка: f({root_newton:.6f}) = {f(root_newton):.2e}")