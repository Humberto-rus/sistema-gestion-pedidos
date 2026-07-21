from abc import ABC, abstractmethod


# Producto Base
class Pedido(ABC):
    def __init__(self, id_pedido: int, cliente: str):
        self.id_pedido = id_pedido
        self.cliente = cliente

    @abstractmethod
    def calcular_total(self, subtotal: float) -> float:
        pass

    @abstractmethod
    def obtener_tipo(self) -> str:
        pass


# Productos Concretos
class PedidoFisico(Pedido):
    def __init__(self, id_pedido: int, cliente: str, costo_envio: float):
        super().__init__(id_pedido, cliente)
        self.costo_envio = costo_envio

    def calcular_total(self, subtotal: float) -> float:
        return subtotal + self.costo_envio

    def obtener_tipo(self) -> str:
        return "Físico"


class PedidoDigital(Pedido):
    def __init__(self, id_pedido: int, cliente: str, enlace_descarga: str):
        super().__init__(id_pedido, cliente)
        self.enlace_descarga = enlace_descarga

    def calcular_total(self, subtotal: float) -> float:
        return subtotal

    def obtener_tipo(self) -> str:
        return "Digital"


# Creador Base (Factory)
class CreadorPedido(ABC):
    @abstractmethod
    def crear_pedido(self, **kwargs) -> Pedido:
        pass


# Creadores Concretos
class CreadorPedidoFisico(CreadorPedido):
    def crear_pedido(self, **kwargs) -> Pedido:
        return PedidoFisico(
            id_pedido=kwargs["id_pedido"],
            cliente=kwargs["cliente"],
            costo_envio=kwargs.get("costo_envio", 0.0)
        )


class CreadorPedidoDigital(CreadorPedido):
    def crear_pedido(self, **kwargs) -> Pedido:
        return PedidoDigital(
            id_pedido=kwargs["id_pedido"],
            cliente=kwargs["cliente"],
            enlace_descarga=kwargs.get("enlace_descarga", "")
        )