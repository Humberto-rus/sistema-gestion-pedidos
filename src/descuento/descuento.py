from src.pedido.pedido import Pedido


# Decorador Base
class DecoradorPedido(Pedido):
    def __init__(self, pedido: Pedido):
        super().__init__(pedido.id_pedido, pedido.cliente)
        self._pedido = pedido

    def calcular_total(self, subtotal: float) -> float:
        return self._pedido.calcular_total(subtotal)

    def obtener_tipo(self) -> str:
        return self._pedido.obtener_tipo()


# Decorador Concreto 1: Descuento Porcentual
class DescuentoPorcentaje(DecoradorPedido):
    def __init__(self, pedido: Pedido, porcentaje: float):
        super().__init__(pedido)
        self.porcentaje = porcentaje

    def calcular_total(self, subtotal: float) -> float:
        total_previo = self._pedido.calcular_total(subtotal)
        descuento = total_previo * (self.porcentaje / 100.0)
        return total_previo - descuento


# Decorador Concreto 2: Envoltorio de Regalo
class EnvoltorioRegalo(DecoradorPedido):
    def __init__(self, pedido: Pedido, costo_regalo: float = 20.0):
        super().__init__(pedido)
        self.costo_regalo = costo_regalo

    def calcular_total(self, subtotal: float) -> float:
        total_previo = self._pedido.calcular_total(subtotal)
        return total_previo + self.costo_regalo