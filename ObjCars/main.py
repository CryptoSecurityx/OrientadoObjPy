from veiculo import Veiculo

novocarro = Veiculo('Audi','R8','black edition',600000,10)

print(novocarro.marca)
print(novocarro.modelo)
print(novocarro.cor)
print(novocarro.preco)
print(novocarro.tanque)

novocaminhao = Veiculo('Mercedez', 'naoimformado', 'prata', 250000,40)
print(novocaminhao.marca)
print(novocaminhao.modelo)
print(novocaminhao.cor)
print(novocaminhao.preco)
print(novocaminhao.tanque)

novocaminhao.abastecer(35)
print(novocaminhao.tanque)