import math

def newton_method(f, df, x0, eps=1e-6, max_iter=100):
    """
    Решает уравнение f(x)=0 методом Ньютона (касательных).
    
    Параметры:
    f: функция f(x)
    df: производная функции f'(x)
    x0: начальное приближение
    eps: точность
    max_iter: максимальное число итераций
    
    Возвращает:
    x: найденный корень
    n: количество итераций
    """
    print("Метод касательных (Ньютона):")
    print(f"{'n':<3} {'x_n':<12} {'f(x_n)':<12} {'f\'(x_n)':<12} {'x_{n+1}':<12} {'|Δx|':<12}")
    print("-" * 65)
    
    x = x0
    for n in range(max_iter):
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-12:
            print("Производная близка к нулю!")
            break
            
        x_new = x - fx / dfx
        delta = abs(x_new - x)
        
        print(f"{n:<3} {x:<12.6f} {fx:<12.6f} {dfx:<12.6f} {x_new:<12.6f} {delta:<12.6f}")
        
        if delta < eps:
            return x_new, n+1
        x = x_new
    
    return x, max_iter

def chord_method(f, a, b, eps=1e-6, max_iter=100):
    """
    Решает уравнение f(x)=0 методом хорд.
    
    Параметры:
    f: функция f(x)
    a, b: границы интервала [a, b]
    eps: точность
    max_iter: максимальное число итераций
    
    Возвращает:
    x: найденный корень
    n: количество итераций
    """
    print("\nМетод хорд:")
    print(f"{'n':<3} {'a':<12} {'b':<12} {'f(a)':<12} {'f(b)':<12} {'x_new':<12} {'|Δx|':<12}")
    print("-" * 80)
    
    fa, fb = f(a), f(b)
    x_prev = b
    
    for n in range(max_iter):
        x = a - (fa * (b - a)) / (fb - fa)
        fx = f(x)
        delta = abs(x - x_prev)
        
        print(f"{n:<3} {a:<12.6f} {b:<12.6f} {fa:<12.6f} {fb:<12.6f} {x:<12.6f} {delta:<12.6f}")
        
        if abs(fx) < eps or delta < eps:
            return x, n+1
        
        if fa * fx < 0:
            b, fb = x, fx
        else:
            a, fa = x, fx
            
        x_prev = x
    
    return x, max_iter

def combined_method(f, df, a, b, eps=1e-6, max_iter=100):
    """
    Решает уравнение f(x)=0 комбинированным методом хорд и касательных.
    
    Параметры:
    f: функция f(x)
    df: производная функции f'(x)
    a, b: границы интервала [a, b]
    eps: точность
    max_iter: максимальное число итераций
    
    Возвращает:
    (a + b) / 2: среднее значение последних приближений
    n: количество итераций
    """
    print("\nКомбинированный метод хорд и касательных:")
    print(f"{'n':<3} {'a_n':<12} {'b_n':<12} {'f(a_n)':<12} {'f(b_n)':<12} {'|a_n - b_n|':<12}")
    print("-" * 65)
    
    for n in range(max_iter):
        # Метод хорд (для a)
        a_new = a - (f(a) * (b - a)) / (f(b) - f(a))
        # Метод Ньютона (для b)
        b_new = b - f(b) / df(b)
        
        delta = abs(b_new - a_new)
        
        print(f"{n:<3} {a:<12.6f} {b:<12.6f} {f(a):<12.6f} {f(b):<12.6f} {delta:<12.6f}")
        
        a, b = a_new, b_new
        
        if delta < eps:
            return (a + b) / 2, n+1
    
    return (a + b) / 2, max_iter

def main():
    """Основная функция для демонстрации всех методов"""
    print("РЕШЕНИЕ УРАВНЕНИЙ ПРИБЛИЖЕННЫМИ МЕТОДАМИ")
    print("=" * 50)
    
    # Пример: 2x - 5ln(x) - 3 = 0
    def f(x):
        return 2*x - 5*math.log(x) - 3
    
    def df(x):
        return 2 - 5/x
    
    # Параметры
    a, b = 0.5, 1.0
    eps = 1e-6
    
    print(f"Уравнение: 2x - 5ln(x) - 3 = 0")
    print(f"Отрезок: [{a}, {b}]")
    print(f"Точность: {eps}")
    print()
    
    # Метод касательных
    root_newton, iter_newton = newton_method(f, df, x0=b, eps=eps)
    print(f"\nРезультат метода касательных: x = {root_newton:.6f} (итераций: {iter_newton})")
    
    # Метод хорд
    root_chord, iter_chord = chord_method(f, a, b, eps=eps)
    print(f"Результат метода хорд: x = {root_chord:.6f} (итераций: {iter_chord})")
    
    # Комбинированный метод
    root_combined, iter_combined = combined_method(f, df, a, b, eps=eps)
    print(f"Результат комбинированного метода: x = {root_combined:.6f} (итераций: {iter_combined})")
    
    print("\n" + "=" * 50)
    print("СРАВНЕНИЕ МЕТОДОВ:")
    print(f"Метод касательных: {iter_newton} итераций")
    print(f"Метод хорд: {iter_chord} итераций") 
    print(f"Комбинированный метод: {iter_combined} итераций")

if __name__ == "__main__":
    main()