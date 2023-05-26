
from datetime import datetime, date
from random import randrange


class Producto:
    cont_id=0
    def __init__(self, nombre, precio, categoria, cantidad, fechaCaducidad):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.cantidad = cantidad
        self.id = Producto.cont_id
        self.fechaCaducidad = fechaCaducidad
        Producto.cont_id+=1
        self.unidadesVendidas = 0

    def __str__(self):
        return f"ID: {self.id+1} --- Producto: {self.nombre} --- Categoria: {self.categoria} -- Precio: ${self.precio} --- Cantidad Disponible: {self.cantidad}"
    

    def contadorUnidadesVendidas(self,cantidad):
        if cantidad>self.cantidad:
            print("se excedio la cantidad de unidades existentes")
            return False
        else:    
            self.unidadesVendidas += cantidad
            self.cantidad -= cantidad
            return True
        


class Inventario:
    def __init__(self):
        self.listaProductos = []

    def mostrarInventario(self):
        print("Listado de productos")
        for producto in self.listaProductos:
            print(producto)

    def agg_producto(self, producto):
        self.listaProductos.append(producto)
        print(self.listaProductos)
        
    def eliminar_producto(self,articulo):
         for producto in self.listaProductos:
            if articulo.lower()==producto.nombre.lower():
                self.listaProductos.remove(producto)

    def pedir_reabastecimiento(self):
        for producto in self.listaProductos:
            if producto.cantidad<5:
                print(f"¡¡Se necesita un reabastecimiento de manera urgente!! del producto {producto.nombre}")


class Usuario:
    def __init__(self, nombreUser, id):
        self.nombreUser = nombreUser
        self.id = id

    def __str__(self):
        return f"ID: {self.id} --- Creador: {self.nombreUser}"

    def iniciarVenta(self):
        return f"Venta iniciada :V"

    def anadirReabastecimiento(self, inventario, articulo):
        for producto in inventario.listaProductos:
            if articulo.lower() == producto.nombre.lower():
                cantidad = int(input("Indique la cantidad de ingresos del producto: "))
                producto.cantidad += cantidad
    
                        
class Pedido:
    def __init__(self, id_pedido, estado):
        self.id_pedido = id_pedido
        self.estado = estado

    def __str__(self):
        return f"El pedido {self.id_pedido} se encuentra en estado {self.estado}"


class Detalle:
    def __init__(self, fecha, id_pedido, estado):
        self.fecha = fecha
        self.impuestos = 0
        self.valorCobrar = 0
        self.pedido = Pedido(id_pedido, estado)

    def mostrarPedido(self):
        print(self.pedido)


    def calcular_subtotal_and_impuesto(self, producto, cantidad):
        if producto.categoria == "Papeleria":
            valorSinImpuesto = producto.precio * cantidad
            self.impuestos = valorSinImpuesto * 0.16
            print(f"Subtotal: ${valorSinImpuesto}")
            print(f"Impuesto: ${self.impuestos}")
        elif producto.categoria == "Drogueria":
            valorSinImpuesto = producto.precio * cantidad
            self.impuestos = valorSinImpuesto * 0.12
            print(f"Subtotal: ${valorSinImpuesto}")
            print(f"Impuesto: ${self.impuestos}")
        elif producto.categoria == "Supermercado":
            valorSinImpuesto = producto.precio * cantidad
            self.impuestos = valorSinImpuesto * 0.04
            print(f"Subtotal: ${valorSinImpuesto}")
            print(f"Impuesto: ${self.impuestos}")


    def calcularValorCobrar(self, producto, cantidad):
         self.valorCobrar = (producto.precio*cantidad) + self.impuestos
         return self.valorCobrar



class Estadistico_Ventas:
    def __init__(self):
        self.totalVentas = 0
        self.promedioVenta = 0


    def __str__(self):
        return f"Total Vendido: ${self.totalVentas} -- Producto mas vendido: {self.productoMasVendido} -- Producto menos vendido: {self.productoMenosVendido}"
    
    def calcularTotalVentas(self, valor):
        self.totalVentas += valor.valorCobrar


    def productoMasVendido(self, inventario):
        i = 0
        mayor = 0
        for producto in inventario.listaProductos:
            if i == 0:
                mayor = producto.unidadesVendidas
                nameMayor = producto.nombre
            else: 
                if producto.unidadesVendidas > mayor:
                    mayor = producto.unidadesVendidas
                    nameMayor = producto.nombre
            i += 1
            
        print(f"El producto mas vendido es {nameMayor} con {mayor} unidades vendidas")
     

    def productoMenosVendido(self, inventario):
        i = 0
        menor = 0
        for producto in inventario.listaProductos:
            if i == 0:
                menor = producto.unidadesVendidas
                nameMenor = producto.nombre
            else:
                if producto.unidadesVendidas < menor:
                    menor = producto.unidadesVendidas
                    nameMenor = producto.nombre
            i += 1

        print(f"El producto con menos ventas es: {nameMenor} con {menor} unidades vendidas")

    def mostrarTotalVentas(self):
        print(f"Lo recaudado es: ${self.totalVentas}")

    def promedioVentas(self, inventario):
        contador = 0
        for producto in inventario.listaProductos:
            contador += producto.unidadesVendidas

        self.promedioVenta = self.totalVentas/contador

    def mostrarPromedioVentaProducto(self):
        return f"El promedio de unidad de venta por producto es: ${self.promedioVenta:.2f}"




class Empresa:
    def __init__(self, nombre, RUC):
        self.nombre = nombre
        self.RUC = RUC

    def __str__(self):
        return f"Empresa: {self.nombre} -- RUC: {self.RUC}"
    

class Menu():
    def __init__(self):
        self.opciones = ["1.Iniciar venta","2.Ver inventario","3.Agregar Producto ","4.cambiar producto", "5.Agregar existencias","6.Ver dinero acumulado","7.Ver unidad de dinero obtenido por unidad de producto","8.Mostrar producto mas vendido","9.Mostrar producto menos vendido","10.Salir"]
    

def menu_programa(show):
    while True:
        print("------- Menu ----------")
        for i in show.opciones:
            print(i)
        while True:
            opcion = int(input("Elija una opcion: "))
            if (0<opcion<=len(show.opciones)):
                break
            else:
                print("Vuelva a intentarlo")
        print()

        if opcion == 1:
            print(empresa)
            if len(inventario.listaProductos) == 0:
                print("No existe nada en inventario")
            else:
                fecha = datetime.now()
                id_pedido = randrange(0,100)
                estado = "Iniciado"
                detalle = Detalle(fecha, id_pedido, estado)
                usuario.iniciarVenta()
                print(f"Estado de la compra: {detalle.pedido.estado}")
                print("Contamos con los siguientes productos: ")
                for producto in inventario.listaProductos:
                    print(f"ID: {producto.id} --- Producto: {producto.nombre} --- Precio Unidad: ${producto.precio}")
                
                busqueda=input("¿Que producto desea vender?\nDigite: ")
                for producto in inventario.listaProductos:
                    if busqueda.lower()==producto.nombre.lower():
                        cantidad=int(input("Indique la cantidad: "))
                        valid=producto.contadorUnidadesVendidas(cantidad)
                        if valid == True:
                            detalle.calcular_subtotal_and_impuesto(producto,cantidad)
                            print(f"El valor a cobrar es: ${detalle.calcularValorCobrar(producto,cantidad)}")
                            estadistico.calcularTotalVentas(detalle)
                            estadistico.promedioVentas(inventario)
                            print(f"Fecha emision Factura: {detalle.fecha}")
                            detalle.pedido.estado = "Finalizado"
                            print(detalle.pedido)
                            print()
                        else:
                            print("Error: excede el numero de cantidades existentes")
            inventario.pedir_reabastecimiento()

        elif opcion == 2:
            inventario.mostrarInventario()

        elif opcion==3:
         agregar_prod(1+1,1)

        elif opcion == 4:
            producto=input("que elemento desea cambiar: ")
            inventario.eliminar_producto(producto)
            agregar_prod(1+1,i=1)

        elif opcion == 5:
            producto = input("Digite el producto a agregar existencias: ")
            usuario.anadirReabastecimiento(inventario, producto)

        elif opcion == 6:
            estadistico.mostrarTotalVentas()

        elif opcion == 7:
            print(estadistico.mostrarPromedioVentaProducto())
        
        elif opcion == 8:
            estadistico.productoMasVendido(inventario)

        elif opcion == 9:
            estadistico.productoMenosVendido(inventario)

        else:
            print("Gracias por usar el programa :)")
            break


            

def agregar_prod(c_pro,i):
 
    
    tipo_producto = ["Drogueria", "Papeleria", "Supermercado"]
    print("\tBienvenido\n--- Agregando productos ---")
    
    while i <c_pro:
        
        if i==0:
             nombre1=[]
             nombre = input(f"Ingrese nombre del producto : ")
        else:
            filtro=True
            
            while filtro:
                    repetidos=0
                    nombre = input(f"Ingrese nombre del producto : ")
                    for producto in inventario.listaProductos:
                        if nombre.lower()==producto.nombre.lower():
                            repetidos+=1
                    if repetidos>0:
                        print("no se deben repetir los nombres de los objetos")    
                    else:
                        filtro=False 
        precio = float(input(f"Ingrese el precio del {nombre}: $"))
        print("\tCategorías:")
        for j, tipo in enumerate(tipo_producto):
            print(f"{j+1}. {tipo}")
        while True:
            opcion = int(input("Indique la categoría: "))
            if 0 < opcion <= len(tipo_producto):
                categoria = tipo_producto[opcion-1]
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        cantidad = int(input("Indique la cantidad a agregar: "))


        producto = Producto(nombre, precio, categoria, cantidad,  "2023")
        inventario.agg_producto(producto)
        print("Producto agregado correctamente\n")
        i += 1
        
empresa = Empresa("Multicomercio", "1234567892001")
inventario = Inventario()
estadistico = Estadistico_Ventas()
usuario = Usuario("Cristian","2709")
    
print("\t---Welcome---")
cantidad = int(input("¿Cuántos elementos desean ingresar? "))

agregar_prod(cantidad,i=0)
menu = Menu() 
menu_programa(menu)


    

        

