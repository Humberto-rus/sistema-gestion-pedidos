import pytest
from src.notificacion.notificacion import SujetoPedido, ObservadorEmail, ObservadorSMS


def test_notificaciones_al_cambiar_estado():
    sujeto = SujetoPedido(id_pedido=101)
    
    email_obs = ObservadorEmail(email="cliente@ejemplo.com")
    sms_obs = ObservadorSMS(telefono="+528441234567")
    
    sujeto.suscribir(email_obs)
    sujeto.suscribir(sms_obs)
    
    # Cambiamos estado y verificamos historial de mensajes
    sujeto.cambiar_estado("Enviado")
    
    assert len(email_obs.historial) == 1
    assert "Pedido 101 cambió su estado a: Enviado" in email_obs.historial[0]
    
    assert len(sms_obs.historial) == 1
    assert "Pedido 101 cambió su estado a: Enviado" in sms_obs.historial[0]