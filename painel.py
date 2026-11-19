"""Antes: o painel aprendeu a falar com o sensor importado -- em cada lugar que pergunta a temperatura.

Funciona, mas o painel agora conhece o codigo de fora: o nome dele, o metodo dele e a conta da unidade.
E cada funcao nova que perguntar a temperatura vai precisar do mesmo if.
"""
from sensor_importado import ImportedSensor


def texto_do_painel(sensor):
    if isinstance(sensor, ImportedSensor):
        celsius = (sensor.read_fahrenheit() - 32) * 5 / 9
    else:
        celsius = sensor.temperatura()
    return str(celsius) + " graus"


def precisa_de_alerta(sensor):
    if isinstance(sensor, ImportedSensor):
        celsius = (sensor.read_fahrenheit() - 32) * 5 / 9
    else:
        celsius = sensor.temperatura()
    return celsius > 30