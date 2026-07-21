from abc import ABC, abstractmethod
from typing import List


# Interfaz Observador
class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje: str):
        pass


# Observador Concreto 1: Email
class ObservadorEmail(Observador):
    def __init__(self, email: str):
        self.email = email
        self.historial: List[str] = []

    def actualizar(self, mensaje: str):
        registro = f"Email enviado a {self.email}: {mensaje}"
        self.historial.append(mensaje)


# Observador Concreto 2: SMS
class ObservadorSMS(Observador):
    def __init__(self, telefono: str):
        self.telefono = telefono
        self.historial: List[str] = []

    def actualizar(self, mensaje: str):
        registro = f"SMS enviado a {self.telefono}: {mensaje}"
        self.historial.append(mensaje)


# Sujeto (Observable)
class SujetoPedido:
    def __init__(self, id_pedido: int):
        self.id_pedido = id_pedido
        self.estado = "Pendiente"
        self._observadores: List[Observador] = []

    def suscribir(self, observador: Observador):
        if observador not in self._observadores:
            self._observadores.append(observador)

    def desuscribir(self, observador: Observador):
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar(self, mensaje: str):
        for observador in self._observadores:
            observador.actualizar(mensaje)

    def cambiar_estado(self, nuevo_estado: str):
        self.estado = nuevo_estado
        mensaje = f"Pedido {self.id_pedido} cambió su estado a: {nuevo_estado}"
        self.notificar(mensaje)