"""O sensor que o painel ja' conhece: mede em graus Celsius."""


class SensorNacional:
    def __init__(self, celsius):
        self.celsius = celsius      # a leitura (fixa: e' o sensor de mentira da aula)

    def temperatura(self):
        return self.celsius