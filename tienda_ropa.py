# Clase General
class Producto:
    def __init__(self, nombre, precio, stock):
        # Ponemos en privado a las variables
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
    
    # Encapsulación:
    # Decorador para el getter y setter de ´__nombre´
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    # Decorador para el getter y setter de ´__precio´
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("Valor no válido. Debe ser positivo.")
    
    # Decorador para el getter y setter de ´__stock´
    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            print("Valor no válido. Debe ser positivo.")
    
    def mostrar_info(self):
        return f'{self.nombre}, Precio: {self.precio}, Cantidad: {self.stock}'

# Clase Intermedia
class Ropa(Producto):
    def __init__(self, nombre, precio, stock, talla, tela):
        # Herencia:
        super().__init__(nombre, precio, stock)
        
        self.__talla = talla
        self.__tela = tela
        
    # Decorador para el getter y setter de ´__talla´
    @property
    def talla(self):
        return self.__talla
    
    @talla.setter
    def talla(self, nueva_talla):
        # Validacion para las tallas
        tallas = ["XS","S","M", "L","XL","XXL"]        
        nueva_talla = nueva_talla.upper()
        if nueva_talla in tallas:
            self.__talla = nueva_talla
        else:
            print("Valor no válido. Debe ser XS, S, M, L, XL o XXL")
    
    # Decorador para el getter y setter de ´__tela´
    @property
    def tela(self):
        return self.__tela
    
    @tela.setter
    def tela(self, nueva_tela):
        # Validacion para las telas
        telas = ["algodon","seda","lino","sintetica","poliester","cuero"]
        nueva_tela = nueva_tela.lower()
        if nueva_tela in telas:
            self.__tela = nueva_tela
        else:
            print("Valore no válido. Debe ser algodon, seda, lino, sintetica, poliester o cuero")
    
    def mostrar_info(self):
        return f'{super().mostrar_info()}, Talla: {self.talla} y Tipo de tela: {self.tela}'
    
# Clases especificas
class Camisa(Ropa):
    def __init__(self, nombre, precio, stock, talla, tela, tipo_camisa):
        super().__init__(nombre, precio, stock, talla, tela)

        self.__tipo_camisa = tipo_camisa
        
    @property
    def tipo_camisa(self):
        return self.__tipo_camisa
    @tipo_camisa.setter
    def tipo_camisa(self, nuevo_tipo_camisa):
        self.__tipo_camisa = nuevo_tipo_camisa
    
    def mostrar_info(self):
        return f'{super().mostrar_info()}, Tipo de camisa: {self.tipo_camisa}'

class Pantalon(Ropa):
    def __init__(self, nombre, precio, stock, talla, tela, tipo_pantalon):
        super().__init__(nombre, precio, stock, talla, tela)
        
        self.__tipo_pantalon = tipo_pantalon
    
    @property
    def tipo_pantalon(self):
        return self.__tipo_pantalon
    @tipo_pantalon.setter
    def tipo_pantalon(self, nuevo_tipo_pantalon):
        self.__tipo_pantalon = nuevo_tipo_pantalon
    
    def mostrar_info(self):
        return f'{super().mostrar_info()}, Tipo de pantalon: {self.tipo_pantalon}'

class Zapato(Ropa):
    def __init__(self, nombre, precio, stock, talla, material, tipo_zapato):
        super().__init__(nombre, precio, stock, talla, material)

        self.__tipo_zapato = tipo_zapato
    
    @property
    def tipo_zapato(self):
        return self.__tipo_zapato
    @tipo_zapato.setter
    def tipo_zapato(self, nuevo_tipo_zapato):
        self.__tipo_zapato = nuevo_tipo_zapato
        
    def mostrar_info(self):
        return f'{super().mostrar_info()}, Tipo de zapato: {self.tipo_zapato}'

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito está vacío.")
        else:
            print("\n--- Carrito de Compras ---")
            for producto in self.productos:
                print(producto.mostrar_info())
            print("\n")
class Tienda:
    def __init__(self):
        self.carrito = Carrito()
    
    def mostrar_productos(self, productos):
        print("\n---Menu de productos---")
        
        for i, producto in enumerate(productos):
            print(f"{i + 1}. {producto.mostrar_info()}")
        print("0. Finalizar compra\n")
    
    def seleccionar_productos(self, productos):
        while True:
            self.mostrar_productos(productos)
            opcion = input("Selecciona el número del producto que deseas comprar (0 para finalizar): ")

            if opcion == '0':
                break
            elif opcion.isdigit() and 1 <= int(opcion) <= len(productos):
                producto = productos[int(opcion) - 1]
                self.carrito.agregar_producto(producto)
                print(f"Agregaste al carrito: {producto.mostrar_info()}")
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
    
    def mostrar_resumen(self):
        monto_total = 0
        print("\n--- Resumen de la Compra ---")
        for producto in self.carrito.productos:
            print(f'{producto.nombre} - Precio: {producto.precio}')
            monto_total += producto.precio
        
        print(f'Monto a pagar: {monto_total}')
    
    def menu_principal(self, productos):
        while True:
            print("Menu Principal")
            print("1. Ver Productos.")
            print("2. Ver Carrito.")
            print("3. Finalizar Compras.")
            print("4. Salir.")
            
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                self.seleccionar_productos(productos)
            elif opcion == "2":
                self.carrito.mostrar_carrito()
            elif opcion == "3":
                self.mostrar_resumen()
                print("Gracias por su compra!")
                break
            elif opcion == "4":
                print("Gracias por su visita!")
                break
            else:
                print("Opcion invalida. Trate de nuevo.")

# Crear lista de productos
productos = [
    Camisa("Camisa Hombre", 65000, 10, "XL", "algodon", "casual"),
    Camisa("Camisa Mujer", 70000, 5, "M", "seda", "formal"),
    Pantalon("Pantalón Hombre", 85000, 15, "L", "lino", "chino"),
    Pantalon("Pantalón Mujer", 80000, 8, "S", "poliester", "de vestir")
]

mi_Tienda = Tienda()
mi_Tienda.menu_principal(productos)