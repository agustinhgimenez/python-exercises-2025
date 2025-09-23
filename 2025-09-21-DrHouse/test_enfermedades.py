# test_enfermedades.py
import pytest
from persona import Persona
from enfermedades import Enfermedad, EnfermedadInfecciosa, EnfermedadAutoinmune, EnfermedadMixta
# ------------------------
# Fixtures reutilizables
# ------------------------
@pytest.fixture
def persona_base():
    # Persona del enunciado: 36°C y 3.000.000 células
    return Persona(temperatura=36.0, cantidad_celulas=3_000_000)

@pytest.fixture
def malaria():
    # Malaria: infecciosa, 5000 células amenazadas
    return Enfermedad("Malaria", 5000, EnfermedadInfecciosa())

@pytest.fixture
def lupus():
    # Lupus: autoinmune, 10000 células amenazadas
    return Enfermedad("Lupus", 10000, EnfermedadAutoinmune())


class TestEnfermedades:
    """Suite de pruebas para los 4 puntos del enunciado."""

    # ---------------- PUNTO 1 ----------------
    def test_punto1_vivir_un_dia(self, persona_base, malaria, lupus):
        p = persona_base
        p.contraer(malaria)
        p.contraer(lupus)

        p.vivir_un_dia()

        # Temperatura: 36 + (5000/1000) = 41.0
        assert p.temperatura == pytest.approx(41.0)
        # Autoinmune resta 10000 células
        assert p.cantidad_celulas == 2_990_000
        # Infecciosa duplica la amenaza
        assert malaria.celulas_amenazadas == 10_000
        # Autoinmune no cambia su propia amenaza
        assert lupus.celulas_amenazadas == 10_000

    # ---------------- PUNTO 2 ----------------
    def test_punto2_atenuar_y_esta_sana(self, persona_base, malaria, lupus):
        p = persona_base
        p.contraer(malaria)
        p.contraer(lupus)
        p.vivir_un_dia()  # malaria=10000, lupus=10000

        malaria.atenuar(5000)  # -> 5000
        lupus.atenuar(500)     # -> 9500

        assert malaria.celulas_amenazadas == 5_000
        assert lupus.celulas_amenazadas == 9_500
        assert p.esta_sana() is False

    # ---------------- PUNTO 3 ----------------
    def test_punto3_medicamento(self, persona_base, malaria, lupus):
        p = persona_base
        p.contraer(malaria)
        p.contraer(lupus)
        p.vivir_un_dia()          # malaria=10000, lupus=10000

        malaria.atenuar(5000)     # -> 5000
        lupus.atenuar(500)        # -> 9500

        p.recibir_medicamento(300)  # 300*15 = 4500

        assert malaria.celulas_amenazadas == 500      # 5000-4500
        assert lupus.celulas_amenazadas == 5_000      # 9500-4500
        assert p.esta_sana() is False

    # ---------------- PUNTO 4 (teórico) ----------------
    def test_punto4_enfermedad_mixta(self):
        p = Persona(temperatura=36.0, cantidad_celulas=3_000_000)
        mixta = Enfermedad("Mixta", 4000, EnfermedadMixta())

        p.contraer(mixta)
        p.vivir_un_dia()

        # Infecciosa: +4.0 °C y duplica 4000 -> 8000
        assert p.temperatura == pytest.approx(40.0)
        assert mixta.celulas_amenazadas == 8000
        # Autoinmune: resta 8000 al cuerpo
        assert p.cantidad_celulas == 3_000_000 - 8_000


class TestEnfermedadesExtras:
    """Casos borde y utilitarios del modelo."""

    def test_atenuar_no_deja_negativo(self):
        e = Enfermedad("Test", 1000, EnfermedadInfecciosa())
        e.atenuar(5000)
        assert e.celulas_amenazadas == 0
        assert e.esta_curada() is True

    def test_eliminar_curadas(self):
        p = Persona(temperatura=36.0, cantidad_celulas=3_000_000)
        e1 = Enfermedad("A", 100, EnfermedadInfecciosa())
        e2 = Enfermedad("B", 50,  EnfermedadAutoinmune())

        p.contraer(e1)
        p.contraer(e2)
        e2.atenuar(10_000)  # curada

        p.eliminar_curadas()
        assert len(p.enfermedades) == 1
        assert p.enfermedades[0].nombre == "A"
