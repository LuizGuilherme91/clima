"""O codigo que veio de fora, de outro fabricante. Nao e' nosso: aqui ninguem mexe.

Ele fala outra lingua: o metodo se chama read_fahrenheit, e a leitura vem em graus Fahrenheit.
"""


class ImportedSensor:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def read_fahrenheit(self):
        return self.fahrenheit