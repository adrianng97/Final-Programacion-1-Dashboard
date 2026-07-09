# Dashboard de Análisis de Ventas e Inventario

## Descripción y Funcionalidad
Este proyecto es una herramienta de automatización diseñada para la gerencia de comercios minoristas o distribuidoras. Su función principal es procesar un historial de ventas, calcular qué artículos tienen mayor rotación y emitir alertas tempranas cuando el stock de un producto se encuentra por debajo del mínimo recomendado.

El programa está modularizado para separar la lógica de presentación de la lógica de negocio. Utiliza un módulo propio (`analisis_stock.py`) para los cálculos matemáticos del "punto de pedido" y módulos externos (`matplotlib` y `colorama`) para la visualización de datos y alertas en consola.

## Requisitos del Sistema
* **Python:** Versión 3.x instalada en el sistema.
* **Sistema Operativo:** Compatible con Windows, Linux o macOS.

## Instalación y Configuración del Entorno Virtual (venv)
Para garantizar las buenas prácticas de desarrollo colaborativo y no generar conflictos con las librerías globales del sistema operativo, este proyecto utiliza un entorno virtual (`venv`). Siga estas instrucciones para ejecutarlo localmente:

**1. Clonar el repositorio o descargar los archivos:**
Abra una terminal y ubíquese en la carpeta donde desea guardar el proyecto.

**2. Crear el entorno virtual:**
Ejecute el siguiente comando para crear un entorno aislado:
```bash
python -m venv venv
```

## Ejemplos de uso

Para ejecutar el dashboard, simplemente corra el archivo principal desde su terminal (asegúrese de tener el entorno virtual activado): python main.py

Resultados esperados:

Consola: Se imprimirá un reporte codificado por colores. Los productos con stock suficiente aparecerán en verde, mientras que aquellos cuyo stock esté por debajo del punto de pedido calculado emitirán una alerta roja.

Interfaz Gráfica: Se abrirá automáticamente una ventana emergente mostrando un gráfico de barras (generado con matplotlib) que proyecta las ventas mensuales de cada producto.

## Buenas prácticas

PEP 8: El código fuente respeta las convenciones de estilo de Python para asegurar la máxima legibilidad.

PEP 257 (Docstrings): Todas las funciones y módulos cuentan con documentación interna utilizando docstrings para explicar sus argumentos y retornos.

Modularización: La lógica matemática se encuentra aislada en el módulo analisis_stock.py, separando las responsabilidades y facilitando el mantenimiento del código (aplicando el principio "Simple es mejor que complejo" del Zen de Python).
