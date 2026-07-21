import pytest
from src.pedido.pedido import CreadorPedidoFisico
from src.descuento.descuento import DescuentoPorcentaje, EnvoltorioRegalo


def test_descuento_porcentaje():
    creador = CreadorPedidoFisico()
    pedido = creador.crear_pedido(
        id_pedido=1, cliente="Juan Perez", costo_envio=50.0
    )
    # Total base = 100 subtotal + 50 envio = 150
    # 10% de descuento sobre 150 = 135
    pedido_con_descuento = DescuentoPorcentaje(pedido, porcentaje=10)
    assert pedido_con_descuento.calcular_total(100.0) == 135.0


def test_decoradores_combinados():
    creador = CreadorPedidoFisico()
    pedido = creador.crear_pedido(
        id_pedido=1, cliente="Juan Perez", costo_envio=50.0
    )
    # Total base = 150
    # Descuento 10% = 135
    # Envoltorio regalo = +20 -> Total = 155
    pedido_decorado = EnvoltorioRegalo(
        DescuentoPorcentaje(pedido, porcentaje=10), costo_regalo=20.0
    )
    assert pedido_decorado.calcular_total(100.0) == 155.0