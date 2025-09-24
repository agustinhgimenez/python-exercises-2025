from banco import Banco
from cuenta import Cuenta
from tarjeta import Tarjeta, DebitoEstrategia, CreditoBlanca, CreditoDorada

b = Banco()
cu = Cuenta("38123456", monto_disponible=5000, deuda=0)
b.agregar_cuenta(cu)

t_deb = Tarjeta("1234 5678 9012 3456", cu, DebitoEstrategia())
t_cre_bla = Tarjeta("9012 3456 1234 5678", cu, CreditoBlanca())
t_cre_dor = Tarjeta("1111 2222 3333 4444", cu, CreditoDorada())

b.agregar_tarjeta(t_deb)
b.agregar_tarjeta(t_cre_bla)
b.agregar_tarjeta(t_cre_dor)

b.consumir("1234 5678 9012 3456", 300)     # débito
b.consumir("9012 3456 1234 5678", 500)     # crédito blanca
print(b.consultar_saldo("38123456"))       # 4700.0
print(b.consultar_deuda("38123456"))       # 500.0
print(b.mejor_cliente())                   # "38123456"
