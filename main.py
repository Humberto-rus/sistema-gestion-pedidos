from src.config.configuracion import ConfiguracionSistema
from src.pedido.pedido import CreadorPedidoFisico, CreadorPedidoDigital
from src.descuento.descuento import DescuentoPorcentaje, EnvoltorioRegalo
from src.pago.pago import ProcesadorPago, PagoTarjeta
from src.notificacion.notificacion import SujetoPedido, ObservadorEmail, ObservadorSMS


def ejecutar_sistema():
    print("=" * 60)
    print(" 🛒 SISTEMA DE GESTIÓN DE PEDIDOS Y PAGOS ")
    print("=" * 60)

    # 1. Singleton: Cargar Configuración
    config = ConfiguracionSistema()
    print(f"\n[1] Configuración del sistema cargada (Modo: {config.modo})")

    # 2. Factory Method: Crear un pedido físico
    creador = CreadorPedidoFisico()
    pedido = creador.crear_pedido(
        id_pedido=101, cliente="Humberto", costo_envio=50.0
    )
    subtotal = 200.0
    total_base = pedido.calcular_total(subtotal)
    print(f"\n[2] Pedido {pedido.obtener_tipo()} creado para {pedido.cliente}")
    print(f"    Subtotal: ${subtotal:.2f} + Envío: $50.00 = Total Base: ${total_base:.2f}")

    # 3. Decorator: Aplicar descuento y envoltorio
    pedido_decorado = EnvoltorioRegalo(
        DescuentoPorcentaje(pedido, porcentaje=10), costo_regalo=20.0
    )
    total_final = pedido_decorado.calcular_total(subtotal)
    print(f"\n[3] Aplicando Decoradores:")
    print("    - Descuento del 10%")
    print("    - Envoltorio de regalo (+$20.00)")
    print(f"    Total con Descuentos y Adicionales: ${total_final:.2f}")

    # 4. Strategy: Procesar el Pago
    estrategia_pago = PagoTarjeta(numero_tarjeta="1234-5678-9012-3456")
    procesador = ProcesadorPago(estrategia_pago)
    resultado_pago = procesador.procesar(total_final)
    print(f"\n[4] Procesamiento de Pago:")
    print(f"    Método: {resultado_pago['metodo']}")
    print(f"    Estado: {'Exitoso' if resultado_pago['exito'] else 'Fallido'}")
    print(f"    Detalle: {resultado_pago['detalle']}")

    # 5. Observer: Notificar Cambio de Estado
    notificador = SujetoPedido(id_pedido=pedido.id_pedido)
    obs_email = ObservadorEmail(email="humberto@ejemplo.com")
    obs_sms = ObservadorSMS(telefono="+528441234567")

    notificador.suscribir(obs_email)
    notificador.suscribir(obs_sms)

    print(f"\n[5] Notificaciones de Estado:")
    notificador.cambiar_estado("Procesando Pago")
    notificador.cambiar_estado("Enviado")

    print("\n Historial de alertas enviadas al cliente:")
    for msj in obs_email.historial:
        print(f"    📧 [EMAIL] {msj}")
    for msj in obs_sms.historial:
        print(f"    📱 [SMS]   {msj}")

    print("\n" + "=" * 60)
    print(" ¡PROCESO COMPLETADO EXITOSAMENTE! ")
    print("=" * 60)


if __name__ == "__main__":
    ejecutar_sistema()