"""
MIT License

Copyright (c) 2022 UnB

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


def question_1() -> None:
    n = input()

    print(n)
    print(n * 2)
    print(n, n)
    print(f"2{n}")
    print(f"[{n}]")


def question_2() -> None:
    x = input()
    y = input()
    z = input()

    print(x + y + z)
    print(x)
    print(y + y)
    print(z, z, z)
    print(f"X == {x}, Y == {y}, Z == {z}")
    print(f"X != {y}, Y != {x}, Z == {z}")


def question_3() -> None:
    def imprimeAPC() -> None:
        print(r"    _    ____   ____ ")
        print(r"   / \  |  _ \ / ___|")
        print(r"  / _ \ | |_) | |    ")
        print(r" / ___ \|  __/| |___ ")
        print(r"/_/   \_\_|    \____|")


def question_4() -> None:
    import math

    x, y = map(int, input().split())
    print(math.pow(x, y))


def question_5() -> None:
    import math

    def powAPC(x: int, y: int) -> None:
        print(math.pow(x, y))


def question_6() -> None:
    def converte(fahrenheit: int) -> None:
        print((fahrenheit - 32) * 5 / 9)


def question_7() -> None:
    def converte(celsius: int) -> None:
        print((celsius * 9 / 5) + 32)


def question_8() -> None:
    du, dudu, edu = map(float, input().split())
    total = du + dudu + edu

    print(f"{(du * 1.1):.2f} {(dudu * 1.1):.2f} {(edu * 1.1):.2f} {total:.2f}")
    print(f"{(total * 1.1):.2f}")


def question_9() -> None:
    raio = float(input())

    PI = 3.14159

    diametro = 2 * raio
    area = PI * (raio**2)
    perimetro = 2 * PI * raio

    print(format(diametro, ".2f"))
    print(format(area, ".2f"))
    print(format(perimetro, ".2f"))


def question_10() -> None:
    dia, mes, ano = input().split("/")

    print(f"{dia}-{mes}-{ano}")
    print(f"{mes}-{dia}-{ano}")
    print(f"{ano}/{mes}/{dia}")


def question_11() -> None:
    def maiorAB(a: int, b: int) -> None:
        print(max(a, b))

    for _ in range(5):
        maiorAB(*map(int, input().split()))


def question_12() -> None:
    def trocarAB(a: int, b: int) -> None:
        print(b, a)

    for _ in range(5):
        trocarAB(*map(int, input().split()))


def question_13() -> None:
    def age(dias: int) -> None:
        anos, resto = divmod(dias, 360)
        meses, dias = divmod(resto, 30)

        print(f"{anos} ano(s), {meses} mes(es) e {dias} dia(s)")

    for n in map(int, input().split()):
        age(n)


def question_14() -> None:
    def age(dias: int) -> None:
        anos, resto = divmod(dias, 360)
        meses, dias = divmod(resto, 30)

        print(anos, meses, dias)

    for n in map(int, input().split()):
        age(n)


def question_15() -> None:
    def peso_ideal(altura: float) -> None:
        print(72.7 * altura - 58, 62.1 * altura - 44.7)

    peso_ideal(float(input()))


def question_16() -> None:
    horas, minutos, segundos = map(int, input().split(":"))
    tempo = segundos + (minutos * 60) + (horas * 3600)
    print(f"La se foram {tempo} segundos que nao voltam mais...")


def question_17() -> None:
    def binario(n: int) -> None:
        print(bin(n))

    for _ in range(5):
        binario(int(input()))


def question_18() -> None:
    def hexadecimal(n: int) -> None:
        print(hex(n))

    for _ in range(5):
        hexadecimal(int(input()))


# TODO: Question 19
# TODO: Question 20


def question_21() -> None:
    n1, n2, n3 = map(float, input().split())
    p1, p2, p3 = map(int, input().split())

    resultado = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3)
    print(format(resultado, ".6f"))


def question_22() -> None:
    def sucessor(n: int) -> None:
        print(n + 1)


def question_23() -> None:
    def antecessor(n: int) -> None:
        print(n - 1)


def question_24() -> None:
    def concatenar(a: str, b: str) -> None:
        print(a + b)

    def repetir(string: str, num: str) -> None:
        print(string * int(num))

    def ambos(a: str, b: str, num: str) -> None:
        print((a + b) * int(num))

    a, b, c = input().split()

    concatenar(a, b)
    repetir(a, c)
    ambos(a, b, c)
