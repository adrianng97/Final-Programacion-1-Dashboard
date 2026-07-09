"""
Dashboard de Análisis de Ventas e Inventario.
Módulo principal que procesa los datos y genera reportes visuales.
"""
import matplotlib.pyplot as plt
from colorama import init, Fore, Style
import analisis_stock

# Inicializar colorama para la consola
init(autoreset=True)

def mostrar_alertas(inventario):
    """Imprime en consola alertas en rojo si falta stock usando colorama."""
    print(Fore.CYAN + Style.BRIGHT + "\n--- ALERTAS DE INVENTARIO ---")
    
    for producto in inventario:
        punto_pedido = analisis_stock.calcular_punto_pedido(
            producto['ventas_diarias'], 
            producto['demora_prov']
        )
        
        if analisis_stock.verificar_stock(producto['stock'], punto_pedido):
            print(Fore.RED + f"¡ALERTA! Reponer {producto['nombre']}. Stock actual: {producto['stock']} (Mínimo: {punto_pedido})")
        else:
            print(Fore.GREEN + f"Stock OK: {producto['nombre']}")

def generar_grafico_ventas(inventario):
    """Genera un gráfico de barras con los productos más vendidos usando matplotlib."""
    # Extraemos los nombres y proyectamos las ventas a 30 días automáticamente
    nombres = [p['nombre'] for p in inventario]
    ventas_totales = [p['ventas_diarias'] * 30 for p in inventario] 

    plt.bar(nombres, ventas_totales, color='skyblue')
    plt.title('Proyección de Ventas Mensuales por Producto')
    plt.xlabel('Productos')
    plt.ylabel('Unidades Vendidas (Proyección a 30 días)')
    plt.show()

def main():
    """Función principal que ejecuta el dashboard."""
    # Lista de diccionarios con los datos de los productos
    datos_inventario = [
        {'nombre': 'Teclado Mecánico', 'stock': 12, 'ventas_diarias': 2, 'demora_prov': 5},
        {'nombre': 'Mouse Óptico', 'stock': 4, 'ventas_diarias': 3, 'demora_prov': 3},
        {'nombre': 'Monitor 24', 'stock': 20, 'ventas_diarias': 1, 'demora_prov': 7},
        {'nombre': 'Memoria RAM', 'stock': 25, 'ventas_diarias': 2, 'demora_prov': 7}
    ]
    
    mostrar_alertas(datos_inventario)
    generar_grafico_ventas(datos_inventario)

if __name__ == "__main__":
    main()
    