'''
Leia 3 valores (A, B e C) representando as medidas de um triângulo. Mostrar se tais medidas formam um triângulo ou não.
Lembre-se que o valor de cada lado deve ser menor que a soma dos outros 2 lados e deve ser maior que o valor absoluto da
diferença entre os outros 2 lados.

'''


class Triangulo:
    def __init__(self):
        """
        Cria um objeto com tres lados
        """
        self.lado_a = -1
        self.lado_b = -1
        self.lado_c = -1

    def set_lado_a(self):
        """
        Solicita o lado A
        """
        self.lado_a = float(input('Insira a medida para o lado A :\n'))

    def set_lado_b(self):
        """
        Solicita o lado B
        """
        self.lado_b = float(input('Insira a medida para o lado B :\n'))

    def set_lado_c(self):
        """
        Solicita o lado C
        """
        self.lado_c = float(input('Insira a medida para o lado C :\n'))

    def checar_triangulo(self):
        """
        Checa se é possivel fazer um triangulo com os lados informados.
        :return: retorna se é possivel ou nao formar um triangulo.
        """
        lados = sorted([self.lado_a, self.lado_b, self.lado_c])
        if lados[0] + lados[1] > lados[2]:
            return print('É possivel formar um triangulo.')
        else:
            return print('Não é possivel formar um triangulo.')


t = Triangulo()
t.set_lado_a()
t.set_lado_b()
t.set_lado_c()
t.checar_triangulo()

