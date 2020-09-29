palavra_secreta = {
    0: " ",
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z",
}

print("Cada numero se refere a letra a sua direita !!!", palavra_secreta)
try:
    mensagem = []

    while True:
        mensagem.append(
            int(input("Escreva seu código em numeros! Digite uma letra para encerrar: ")))
except:
    print(mensagem)
traducao = []
for a in mensagem:
    traducao.append(palavra_secreta[a])
print("A mensagem é : ", "".join(traducao).upper())
