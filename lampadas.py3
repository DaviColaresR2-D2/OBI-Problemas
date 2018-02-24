# Você está de volta em seu hotel na Tailândia depois de um dia de mergulhos. O seu quarto tem duas lâmpadas. Vamos chamá-las de A e B.   #
# No hotel há dois interruptores, que chamaremos de I1 e I2. Ao apertar I1, a lâmpada A troca de estado, ou seja, acende se estiver       #
# apagada e apaga se estiver acesa. Se apertar I2, ambas as lâmpadas A e B trocam de estado.                                              #
# As lâmpadas inicialmente estão ambas apagadas. Seu amigo resolveu bolar um desaﬁo para você. Ele irá apertar os interruptores em uma    #
# certa sequência, e gostaria que você respondesse o estado ﬁnal das lâmpadas A e B.                                                      #
# Entrada                                                                                                                                 #
# A primeira linha contém um número N que representa quantas vezes seu amigo irá apertar algum interruptor. Na linha seguinte seguirão N  #
# números, que pode ser 1, se o interruptor I1 foi apertado, ou 2, se o interruptor I2 foi apertado.                                      #
# Saída                                                                                                                                   #
# Seu programa deve imprimir dois valores, em linhas separadas.                                                                           #
# Na primeira linha, imprima 1 se a lâmpada A estiver acesa no ﬁnal das operações e 0 caso contrário. Na segunda linha, imprima 1 se a    #
# lâmpada B estiver acesa no ﬁnal das operações e 0 caso contrário.                                                                       #
# Restrições • 1 ≤ N ≤ 105                                                                                                                #
# Informações sobre a pontuação                                                                                                           #
# • Em um conjunto de casos de teste equivalente a 20 pontos, N = 3.                                                                      #

# Primeiramente iremos pegar os valores digitados, o valor da quantidade de vezes que o interruptor será apertado não terá importância    #
# nesse modelo de resolução, então partiremos para os interruptores em si, pra isso usaremos uma lista "l", e esta posteriomente seguida  #
# do comando "split()" que irá dividir os valores ao longo da lista. A seguir usaremos o comando "count()" para que se descubra a         #
# quantidade de vezes que cada lãmpada foi acesa.                                                                                         #

N = input()
l = []
l = input().split(" ")
a1 = l.count("1")
b2 = l.count("2")
l1 = a1 + b2
l2 = b2


if l1 % 2 == 0:
  print(0)
else:
  print(1)
if l2 % 2 == 0:
  print(0)
else:
  print(1)
