"""O adaptador: faz o sensor importado falar a lingua do painel.

Por fora, ele tem o que o painel espera: temperatura(), em graus Celsius.
Por dentro, ele pergunta ao sensor importado, na lingua dele, e converte a resposta.
"""


class AdaptadorImportado:
    def __init__(self, importado):
        self.importado = importado

    def temperatura(self):
        fahrenheit = self.importado.read_fahrenheit()
        return (fahrenheit - 32) * 5 / 9