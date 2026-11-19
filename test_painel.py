from adaptador import AdaptadorImportado
from painel import precisa_de_alerta, texto_do_painel
from sensor_importado import ImportedSensor
from sensor_nacional import SensorNacional


def test_painel_mostra_o_sensor_nacional():
    assert texto_do_painel(SensorNacional(22.0)) == "22.0 graus"


def test_nacional_a_31_graus_pede_alerta():
    assert precisa_de_alerta(SensorNacional(31.0))


def test_painel_mostra_o_importado_em_celsius():
    assert texto_do_painel(AdaptadorImportado(ImportedSensor(95))) == "35.0 graus"


def test_importado_a_86_fahrenheit_nao_pede_alerta():
    assert not precisa_de_alerta(AdaptadorImportado(ImportedSensor(86)))