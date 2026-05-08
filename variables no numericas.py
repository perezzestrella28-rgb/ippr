class Pedido:
    def __init__(self, nombre_usuario, cantidad_de_pizzas, esta_pagado, direccion_envio, precio_total):
        self.nombre_usuario = nombre_usuario
        self.cantidad_de_pizzas = cantidad_de_pizzas
        self.esta_pagado = esta_pagado
        self.direccion_envio = direccion_envio
        self.precio_total = precio_total
 
    def resumen(self):
        return (f"\nPedido de {self.nombre_usuario}: "
                f"{self.cantidad_de_pizzas} pizzas, "
                f"total ${self.precio_total:.2f}, "
                f"pagado: {self.esta_pagado}, "
                f"envío a: {self.direccion_envio}")
 
 
# Pedir datos al usuario
nombre = input("Nombre del usuario: ")
cantidad = int(input("Cantidad de pizzas: "))
pagado = input("¿Está pagado? (True/False): ") == "True"
direccion = input("Dirección de envío: ")
precio = float(input("Precio total: "))
 
# Crear objeto y mostrar resultado
pedido1 = Pedido(nombre, cantidad, pagado, direccion, precio)
print(pedido1.resumen())
