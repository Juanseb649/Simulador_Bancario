__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

from cliente import cliente

class Cuentadeahorros:

# Aqui inicia la declaracion de la clase

    """----------------------------------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------------------------------"""
    interes_mensual = 0
    saldo = 0
    """----------------------------------------------------------------------------------------------
    # Metodo
    ----------------------------------------------------------------------------------------------"""
    __method__= "Consignar valor"
    __parameter__= "nuevo valor"
    __return__="Valor"
    __description__="Metodo que muestra valor a consignar"
    def consignar_valor(self,nuevovalor):
        self.saldo = nuevovalor
    """----------------------------------------------------------------------------------------------
    # Metodo
    ----------------------------------------------------------------------------------------------"""
    __method__= "Mostrar el saldo "
    __parameter__= "ninguno"
    __return__="Saldo"
    __description__="Metodo que muestra el saldo en cuenta"
    def dar_saldo(self):
        return self.saldo
    """----------------------------------------------------------------------------------------------
    # Metodo
    ----------------------------------------------------------------------------------------------"""
    __method__= "Retirar valor"
    __parameter__= "Retirar el valor y mostrar el monto en la cuenta"
    __return__="Saldo de la cuenta"
    __description__="Metodo que muestra el monto en cuenta"
    def retirar_valor(self,monto):
        self.saldo = monto
    """----------------------------------------------------------------------------------------------
    # Metodo
    ----------------------------------------------------------------------------------------------"""
    __method__= "Dar interes mensual"
    __parameter__= "ninguno"
    __return__="intereses"
    __description__="Mostrar el interes mensual"
    def dar_interes_mensual(self):
        return self.interes
    """----------------------------------------------------------------------------------------------
    # Metodo
    ----------------------------------------------------------------------------------------------"""
    __method__= "Actualizar saldo por mes"
    __parameter__= "ninguno"
    __return__="saldo"
    __description__="metodo que actualiza el saldo"
    def actualizar_Saldo_por_paso_mes(self):
        return self.saldo
