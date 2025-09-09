import pytest
from peaje import Peaje, FormaDePago, Auto, Moto, Camion, AutoElectrico, Gubernamental
from peaje.vehiculos import Vehiculo

#TESTING
class TestPeaje:
    def testConstructorPeaje(self):
        peaje = Peaje("Panamericana")
        assert isinstance(peaje,Peaje)

class TestFormaDePago:
    def testConstructorFormaDePago(self):
        formadepago=FormaDePago(0.5)
        assert isinstance(formadepago,FormaDePago)

class TestVehiculo:
    def testConstructorVehiculo(self):
        vehiculo=Vehiculo("AU 773 NA","efectivo")
        assert isinstance(vehiculo,Vehiculo)

class TestAuto:
    def testConstructorAuto(self):
        auto=Auto("AU 773 NA","sube")
        assert isinstance(auto,Auto)

class TestMoto:
    def testConstructorMoto(self):
        moto=Moto("AU 773 NA","telepase")
        assert isinstance(moto,Moto)

class TestAutoElectrico:
    def testConstructorAutoElectrico(self):
        autoelectrico=AutoElectrico("AU 773 NA","telepase")
        assert isinstance(autoelectrico,AutoElectrico)

class TestCamion:
    def testConstructorCamion(self):
        camion=Camion("AU 773 NA","efectivo",3)
        assert isinstance(camion,Camion)

class TestGubernamental:
    def testConstructorGubernamental(self):
        gubernamental=Gubernamental("AU 773 NA","efectivo")
        assert isinstance(gubernamental,Gubernamental)

