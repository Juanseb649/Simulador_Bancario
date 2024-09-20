__author__ = "Juan Sebastian Ibarra Salas"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "juan.ibarra@campusucc.edu.co"

#----------------------------------------------------------------
# Importaciones
#----------------------------------------------------------------

from Cuenta_de_ahorros import Cuentadeahorros
from cuenta_corriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    __cedula = ''
    __nombre = ''
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Asociaciones
    #----------------------------------------------------------------
    
    __cuentaAhorros=Cuentadeahorros()
    __cuentaCorriente=CuentaCorriente()
    __cdt=CDT()
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    __method__ = "DepositarCuentaCorriente"
    __parameter__ = "Monto"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite depositar en la cuenta corriente"
    def DepositarCuentaCorriente(self, monto):
        # Aqui inicia mi codigo
        self.__cuentaCorriente.ConsignarSaldo(monto)
    
    __method__ = "CalcularSaldoTotal"
    __parameter__ = "Ninguno"
    __returns__ = "Saldo total de todas las cuentas"
    __Description__ = "Metodo que permite calcular el saldo total actual en todas las cuentas"
    def CalcularSaldoTotal(self):
        # Aqui inicia mi codigo
        # Metodo 1
        # total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        # return total
        # Metodo 2
        return self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
    
    __method__ = "PasarAhorroACorriente"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "Metodo que permite pasar saldo de la cuenta de ahorrros a la cuenta corriente"
    def PasarAhorroACorriente(self):
        # Aqui inicia mi codigo
        saldoAhorros = self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarSaldo(saldoAhorros)
        self.__cuentaCorriente.ConsignarSaldo(saldoAhorros)
    
    __method__ = "Ahorros"
    __parameter__ = "Monto"
    __returns__ = ""
    __Description__ = "Metodo que permite pasar mis ahorros en la cuenta corriente a la cuenta de ahorros"
    def ahorrar (self,monto):   
        monto = self.__cuentaAhorros__.darsaldo()
        self. __cuentaCorriente (monto)
        self.__cuentaAhorros (monto)
    
    __method__ = "Retiro Ahorro"
    __parameter__ = "monto"
    __returns__ = ""
    __Description__ = "Metodo que permite retirar un monto de mi saldo"
    def retirar (self,monto):
        self.__cuentaAhorros.RetirarSaldo(monto)
    
    __method__ = "Retiro total"
    __parameter__ = ""
    __returns__ = ""
    __Description__ = "Retira el valor existente en la cuenta de ahorro y cuenta corriente"
    def retirar (self):
        self.__cuentaAhorros.RetirarSaldo(self.__cuentaAhorros.DarSaldo)
    
    __method__ = "Duplicar Ahorro "
    __parameter__ = ""
    __returns__ = ""
    __Description__ = "Duplica la cantidad de dinero que hay en la cuenta de ahorros"
    def duplicar (self):
        self.__cuentaAhorros.ConsignarSaldo (self.__cuentaAhorros.darsaldo())
    
    __method__ = "Dar saldo corriente"
    __parameter__ = ""
    __returns__ = "saldo"
    __Description__ = "retorna el saldo que hay en la cuenta corriente"
    def darsaldocorriente (self):
        return self.__cuentaCorriente.DarSaldo()