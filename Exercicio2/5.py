# Solicita três lados e verifica se formam um triângulo válido
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os lados formam um triângulo válido.")
else:
    print("Os lados não formam um triângulo válido.")