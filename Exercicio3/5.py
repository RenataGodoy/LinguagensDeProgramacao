# Solicita um número N e exibe os N primeiros termos da sequência de Fibonacci
n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
fib1, fib2 = 0, 1
print("Sequência de Fibonacci:")
for _ in range(n):
    print(fib1, end=" ")
    fib1, fib2 = fib2, fib1 + fib2
print()
