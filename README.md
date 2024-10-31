Tienda de Ropa - Sistema de Gestión de Carrito de Compras
Este proyecto implementa un sistema de gestión de productos y carrito de compras para una tienda de ropa. La aplicación permite visualizar productos disponibles, agregar artículos al carrito, ver los productos seleccionados y finalizar la compra con un resumen del total a pagar.

Estructura del Código
El sistema está compuesto por las siguientes clases:

Producto: Representa los detalles generales de cualquier producto de la tienda (nombre, precio y stock).
Ropa: Hereda de Producto e incorpora atributos específicos para artículos de ropa, como talla y tela.
Camisa, Pantalon, Zapato: Heredan de Ropa y representan tipos específicos de productos. Cada uno de ellos incluye atributos adicionales como tipo_camisa, tipo_pantalon o tipo_zapato.
Carrito: Gestiona los productos agregados al carrito de compras y permite visualizar los artículos seleccionados.
Tienda: Gestiona el flujo principal del programa, permitiendo al usuario navegar por las opciones de la tienda, seleccionar productos y ver el resumen de su compra.

Cómo Ejecutar el Código
Para ejecutar el sistema de compras de la tienda de ropa, sigue estos pasos:

Asegúrate de tener Python 3 instalado en tu sistema.

Guarda el código en un archivo, por ejemplo tienda.py.

En la terminal, navega a la ubicación del archivo y ejecuta el siguiente comando:

python tienda.py