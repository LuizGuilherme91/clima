from adaptador import AdaptadorImportado
from sensor_importado import ImportedSensor


def test_212_fahrenheit_sao_100_celsius():
    assert AdaptadorImportado(ImportedSensor(212)).temperatura() == 100.0


def test_32_fahrenheit_sao_0_celsius():
    assert AdaptadorImportado(ImportedSensor(32)).temperatura() == 0.0