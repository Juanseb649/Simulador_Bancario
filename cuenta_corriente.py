__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

from cliente import cliente

class cuentacorriente:
    """----------------------------------------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------------------------------------"""
    __saldo=0
    __depositos=0
    __retiros=0
    """----------------------------------------------------------------------------------------------
    #Metodo
    ----------------------------------------------------------------------------------------------"""
    __method__= "Dar saldo"
    __parameter__= "Ninguno"
    __return__="saldo de la cuenta"
    __description__="Metodo que me muestra el saldo de la cuenta"
    def DarSaldo(self):
        return self.__saldo
    """----------------------------------------------------------------------------------------------
    #Metodo
    ----------------------------------------------------------------------------------------------"""
    __method__= "retiros"
    __parameter__= "ninguno"
    __return__="retiros"
    __description__="Metodo que muestra cuando realizo un retiro"
    def retiros(self):
        return self.__retiros
    """#--------------------------------------------------------------------------------------------
    #Metodo
    -------------------------------------------------------------------------------------------------#"""
    __method__= "Depositos cuenta corriente"
    __parameter__= "Ninguno"
    __return__="Depositos"
    __description__="Metodo que me muestra cuando realizo un deposito en la cuenta corriente"
    def depositos(self):
        return self.__depositos
    """#--------------------------------------------------------------------------------------------
    #Metodo
    -------------------------------------------------------------------------------------------------#"""
    __method__= "Consignar saldo"
    __parameter__= "monto"
    __return__="ninguno"
    __description__="Metodo que permite consignar un monto a la cuenta corriente"
    def consignar_saldo(self,monto):
        self.__saldo=self.__saldo+monto
    """#--------------------------------------------------------------------------------------------
    #Metodo
    -------------------------------------------------------------------------------------------------#"""
    __method__= "Retirar saldo"
    __parameter__= "monto"
    __return__="ninguno"
    __description__="Metodo que permite retirar un monto a la cuenta corriente"
    def consignar_saldo(self,monto):
        self.__saldo=self.__saldo-monto


