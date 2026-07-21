import pytest
from src.pedido.pedido import CreadorPedidoFisico, CreadorPedidoDigital


def test_creacion_pedido_fisico():
    creador = CreadorPedidoFisico()
    pedido = creador.crear_pedido(
        id_pedido=1, cliente="Juan Perez", costo_envio=50.0
    )
    assert pedido.calcular_total(100.0) == 150.0
    assert pedido.obtener_tipo() == "Físico"


def test_creacion_pedido_digital():
    creador = CreadorPedidoDigital()
    pedido = creador.crear_pedido(
        id_pedido=2, cliente="Maria Gomez", enlace_descarga="http://link.com"
    )
    assert pedido.calcular_total(100.0) == 100.0
    assert pedido.obtener_tipo() == "Digital"