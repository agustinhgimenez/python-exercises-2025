# tests/test_banco.py
import pytest
from banco import Banco
from cuenta import Cuenta
from tarjeta import Tarjeta, DebitoEstrategia, CreditoBlanca, CreditoDorada


@pytest.fixture
def banco_y_cuenta_principal():
    banco = Banco()
    cuenta = Cuenta("38123456", monto_disponible=5000, deuda=0)
    banco.agregar_cuenta(cuenta)
    banco.agregar_tarjeta(Tarjeta("1234 5678 9012 3456", cuenta, DebitoEstrategia()))
    banco.agregar_tarjeta(Tarjeta("9012 3456 1234 5678", cuenta, CreditoBlanca()))
    banco.agregar_tarjeta(Tarjeta("1111 2222 3333 4444", cuenta, CreditoDorada()))
    return {"banco": banco, "cuenta": cuenta}


def test_consumo_debito(banco_y_cuenta_principal):
    banco = banco_y_cuenta_principal["banco"]
    cuenta = banco_y_cuenta_principal["cuenta"]
    banco.consumir("1234 5678 9012 3456", 300)
    assert cuenta.monto_disponible == 4700.0


def test_consumo_credito_blanca(banco_y_cuenta_principal):
    banco = banco_y_cuenta_principal["banco"]
    cuenta = banco_y_cuenta_principal["cuenta"]
    banco.consumir("9012 3456 1234 5678", 500)
    assert cuenta.deuda == 500.0


def test_consultar_saldo(banco_y_cuenta_principal):
    banco = banco_y_cuenta_principal["banco"]
    cuenta = banco_y_cuenta_principal["cuenta"]
    assert banco.consultar_saldo("38123456") == cuenta.monto_disponible


def test_consultar_deuda(banco_y_cuenta_principal):
    banco = banco_y_cuenta_principal["banco"]
    cuenta = banco_y_cuenta_principal["cuenta"]
    assert banco.consultar_deuda("38123456") == cuenta.deuda


def test_mejor_cliente(banco_y_cuenta_principal):
    banco = banco_y_cuenta_principal["banco"]
    cuenta = banco_y_cuenta_principal["cuenta"]
    banco.consumir("9012 3456 1234 5678", 500)
    assert banco.mejor_cliente() == cuenta.dni



def test_credito_blanca_supera_limite(banco_y_cuenta_principal):
    banco = banco_y_cuenta_principal["banco"]
    with pytest.raises(Exception, match="tope de deuda|tope de deuda de la tarjeta Blanca"):
        banco.consumir("9012 3456 1234 5678", 20_000)


def test_debito_con_devolucion_iva(banco_y_cuenta_principal):
    banco = banco_y_cuenta_principal["banco"]
    cuenta = banco_y_cuenta_principal["cuenta"]
    saldo_inicial = cuenta.monto_disponible
    banco.consumir("1234 5678 9012 3456", 4000)  # > 3000 => cobra 0.79 * 4000 = 3160
    assert cuenta.monto_disponible == pytest.approx(saldo_inicial - 3160, rel=1e-9)
