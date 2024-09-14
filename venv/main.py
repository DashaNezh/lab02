def sieve_of_eratosthenes(n):
    # Инициализируем список для отметки составных чисел
    primes = [True] * (n + 1)  # Изначально считаем все числа простыми
    p = 2  # Начинаем с 2 — первого простого числа

    # Убираем кратные числа до корня из n
    while p * p <= n:
        # Если число не было помечено как составное
        if primes[p]:
            # Убираем все кратные числа p, начиная с p^2
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    # Собираем список простых чисел
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

# Пример использования
N = int(input("Введите число N: "))
primes = sieve_of_eratosthenes(N)
print(f"Простые числа до {N}: {primes}")
