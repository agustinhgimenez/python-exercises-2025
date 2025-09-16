# test_lavadero.py
import pytest

from vehiculo import Vehiculo
from ciudad import Ciudad
from lavaderos import LavaderoArtesanal, LavaderoAutomatico
from bandadas import Bandada, OtraAve, Paloma, Gaviota
from formacion import FormacionV, FormacionW


# ---------- helpers ----------
def crear_bandada_V():
    """2 gaviotas (30, 20), 1 paloma (300), 1 cotorra, 2 loros, en formación V."""
    g1, g2 = Gaviota(30), Gaviota(20)
    p1 = Paloma(300)
    c1, l1, l2 = OtraAve(), OtraAve(), OtraAve()
    b = Bandada(FormacionV())
    b.bandada.extend([g1, g2, p1, c1, l1, l2])
    return b, (g1, g2, p1, c1, l1, l2)


# ---------- tests a–f ----------

def test_a_paloma_gorda():
    """a) Una paloma gorda (500) pasa por el auto → +150 de suciedad"""
    auto = Vehiculo(0)
    paloma_g = Paloma(500)
    paloma_g.ensuciar(auto)
    assert auto.suciedad == pytest.approx(150.0)


def test_b_bandada_V_suma_390_sobre_150_previo():
    """
    b) La bandada en V pasa por el auto.
       Aportes: G1(90) + G2(60) + P1(90) + 3 aves * 50 = 390
       Partiendo de 150 (paloma gorda previa) => 540 total
    """
    auto = Vehiculo(0)
    Paloma(500).ensuciar(auto)  # deja 150
    bandada, _ = crear_bandada_V()
    bandada.ensuciar(auto)      # +390
    assert auto.suciedad == pytest.approx(540.0)


def test_c_ceniza_volcanica_suma_100_a_todos():
    """c) Ceniza volcánica 100 mm suma +100 a todos los vehículos en la ciudad."""
    BA = Ciudad("Buenos Aires")
    auto1, auto2 = Vehiculo(0), Vehiculo(0)
    BA.vehiculos.append(auto1)
    BA.vehiculos.append(auto2)

    BA.ensuciarConCeniza(100)
    assert auto1.suciedad == pytest.approx(100.0)
    assert auto2.suciedad == pytest.approx(100.0)


def test_d_lavar_en_SmallLav_con_640_de_suciedad():
    """
    d) Con 640 de suciedad:
       precio SmallLav (3 emp) = 10 * 3 * round(640/5) = 3840, y auto queda limpio.
       Cómo armamos 640: 150 (paloma 500) + 390 (bandada V) + 100 (ceniza) = 640
    """
    auto = Vehiculo(0)
    # 150
    Paloma(500).ensuciar(auto)
    # +390
    bandada, _ = crear_bandada_V()
    bandada.ensuciar(auto)
    # +100
    BA = Ciudad("Buenos Aires")
    BA.vehiculos.append(auto)
    BA.ensuciarConCeniza(100)

    assert auto.suciedad == pytest.approx(640.0)

    small = LavaderoArtesanal(3)
    assert small.calcularPrecio(auto) == pytest.approx(3840.0)
    small.lavar(auto)
    assert auto.suciedad == pytest.approx(0.0)


def test_e_cambiar_a_W_y_pasar_de_nuevo_total_707_1():
    """
    e) Después de una pasada previa en V (paloma pasa de 300→210),
       cambiamos a W y pasamos 2 veces:
       1ra: 90 + 60 + 63 + 150 = 363
       2da: 90 + 60 + 44.1 + 150 = 344.1
       Total ≈ 707.1 sobre auto limpio.
    """
    # mismas aves para conservar el peso de la paloma tras V
    auto = Vehiculo(0)
    bandada_V, (g1, g2, p1, c1, l1, l2) = crear_bandada_V()
    bandada_V.ensuciar(auto)   # paloma 300 -> 210
    auto.limpiar()             # dejamos el auto limpio, aves quedan modificadas

    bandada_W = Bandada(FormacionW())
    bandada_W.bandada.extend([g1, g2, p1, c1, l1, l2])
    bandada_W.ensuciar(auto)

    assert auto.suciedad == pytest.approx(707.1, rel=1e-4)


def test_f_encontrar_lavadero_mas_barato_y_lavar():
    """
    f) Con auto2=100 de suciedad:
       - Artesanal 3 emp → 600
       - Artesanal 2 emp → 400  (más barato)
       - Automático → 1000
    """
    BA = Ciudad("Buenos Aires")
    auto2 = Vehiculo(100)
    BA.vehiculos.append(auto2)

    small = LavaderoArtesanal(3)
    smaller = LavaderoArtesanal(2)
    fast = LavaderoAutomatico()  # 1000 fijo
    BA.lavaderos.extend([small, smaller, fast])

    elegido = BA.encontrarLavaderoEconomico(auto2)
    assert elegido.calcularPrecio(auto2) == pytest.approx(400.0)

    elegido.lavar(auto2)
    assert auto2.suciedad == pytest.approx(0.0)
