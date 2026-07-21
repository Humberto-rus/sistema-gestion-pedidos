from abc import ABC, abstractmethod


# Estrategia Base
class EstrategiaPago(ABC):
    @abstractmethod
    def pagar(self, monto: float) -> dict:
        pass


# Estrategia Concreta 1: Tarjeta
class PagoTarjeta(EstrategiaPago):
    def __init__(self, numero_tarjeta: str):
        self.numero_tarjeta = numero_tarjeta

    def pagar(self, monto: float) -> dict:
        return {
            "exito": True,
            "metodo": "Tarjeta de Crédito/Débito",
            "monto": monto,
            "detalle": f"Pago procesado con tarjeta finalizada en {self.numero_tarjeta[-4:]}"
        }


# Estrategia Concreta 2: PayPal
class PagoPayPal(EstrategiaPago):
    def __init__(self, email: str):
        self.email = email

    def pagar(self, monto: float) -> dict:
        return {
            "exito": True,
            "metodo": "PayPal",
            "monto": monto,
            "detalle": f"Pago procesado desde la cuenta {self.email}"
        }


# Contexto que utiliza la estrategia
class ProcesadorPago:
    def __init__(self, estrategia: EstrategiaPago):
        self._estrategia = estrategia

    def cambiar_estrategia(self, estrategia: EstrategiaPago):
        self._estrategia = estrategia

    def procesar(self, monto: float) -> dict:
        return self._estrategia.pagar(monto)