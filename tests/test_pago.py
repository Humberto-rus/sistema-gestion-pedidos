import pytest
from src.pago.pago import ProcesadorPago, PagoTarjeta, PagoPayPal


def test_pago_tarjeta_exitoso():
    estrategia = PagoTarjeta(numero_tarjeta="1234-5678-9012-3456")
    procesador = ProcesadorPago(estrategia)
    resultado = procesador.procesar(150.0)
    assert resultado["exito"] is True
    assert resultado["metodo"] == "Tarjeta de Crédito/Débito"


def test_pago_paypal_exitoso():
    estrategia = PagoPayPal(email="cliente@ejemplo.com")
    procesador = ProcesadorPago(estrategia)
    resultado = procesador.procesar(150.0)
    assert resultado["exito"] is True
    assert resultado["metodo"] == "PayPal"