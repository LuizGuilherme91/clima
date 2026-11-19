from adaptador import AdaptadorImportado
from painel import precisa_de_alerta, texto_do_painel
from sensor_importado import ImportedSensor
from sensor_nacional import SensorNacional

sala = SensorNacional(22.0)
quintal = AdaptadorImportado(ImportedSensor(95))

print(texto_do_painel(sala))
print(texto_do_painel(quintal))
print(precisa_de_alerta(quintal))