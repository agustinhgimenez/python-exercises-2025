import pytest
from envio import Envio
from recargo import RecargoCategorico, RecargoSobrePeso , RecargoArbitrario
from impuesto import IVA, ImpuestoMulticategoria , ImpuestoAduanero , ImpuestoExtrano

# -------------------------
# E J E R C I C I O   1
# -------------------------
def test_ejercicio_1_envios_internacionales():
    a = Envio("Buenos Aires", "Argentina", "Utrecht", "Países Bajos", 2, 220, ["musica"])
    b = Envio("California", "Estados Unidos", "Miami", "Estados Unidos", 5, 1500, ["libros"])
    c = Envio("Lima", "Perú", "Santiago", "Chile", 1, 500, ["arte"])

    envios = [a, b, c]
    internacionales = [e for e in envios if e.es_internacional()]

    assert a.es_internacional() is True
    assert b.es_internacional() is False
    assert c.es_internacional() is True
    assert internacionales == [a, c]