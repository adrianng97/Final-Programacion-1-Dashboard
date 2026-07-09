"""
Módulo para el análisis matemático de inventario.
Cumple con PEP 257 detallando el propósito de cada función.
"""

def calcular_punto_pedido(ventas_diarias, dias_demora_proveedor, stock_seguridad=5):
    """
    Calcula el punto de pedido de un producto.
    
    Args:
        ventas_diarias (float): Promedio de unidades vendidas por día.
        dias_demora_proveedor (int): Días que tarda el proveedor en reponer.
        stock_seguridad (int): Unidades de resguardo (por defecto 5).
        
    Returns:
        float: Cantidad mínima en stock antes de realizar un nuevo pedido.
    """
    return (ventas_diarias * dias_demora_proveedor) + stock_seguridad

def verificar_stock(stock_actual, punto_pedido):
    """
    Evalúa si el stock actual está por debajo del límite seguro.
    
    Args:
        stock_actual (float): Cantidad de unidades disponibles.
        punto_pedido (float): Límite mínimo aceptable.
        
    Returns:
        bool: True si se necesita reponer, False caso contrario.
    """
    return stock_actual <= punto_pedido