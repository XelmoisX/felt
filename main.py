import flet as ft

# Lista de productos de ejemplo
productos = [
    {"nombre": "Manzana", "precio": 10, "imagen": "https://cdn-Icons-png.flaticon.com/512/415/415733.png"},
    {"nombre": "Pan", "precio": 15, "imagen": "https://cdn-Icons-png.flaticon.com/512/2907/2907018.png"},
    {"nombre": "Leche", "precio": 20, "imagen": "https://cdn-Icons-png.flaticon.com/512/2910/2910763.png"},
]

# Carrito de compras
carrito = []

# Función para mostrar pantalla de productos
def pantalla_productos(page: ft.Page):
    page.clean()
    
    productos_list = ft.ListView(
        spacing=10,
        expand=True
    )
    
    for p in productos:
        productos_list.controls.append(
            ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Image(src=p["imagen"], width=60, height=60),
                            ft.Text(f"{p['nombre']} - ${p['precio']}", size=18),
                            ft.IconButton(
                                icon=ft.Icons.ADD_SHOPPING_CART,
                                on_click=lambda e, prod=p: agregar_carrito(prod, page),
                                tooltip="Agregar al carrito"
                            )
                        ]
                    )
                )
            )
        )
    
    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text("Productos BravoVa", size=30, weight=ft.FontWeight.BOLD),
                ft.ElevatedButton("Ver Carrito", on_click=lambda e: pantalla_carrito(page))
            ]
        ),
        productos_list
    )

# Función para agregar producto al carrito con animación
def agregar_carrito(prod, page):
    carrito.append(prod)
    page.snack_bar = ft.SnackBar(
        ft.Text(f"{prod['nombre']} agregado al carrito ✅"),
        open=True,
        duration=1500
    )
    page.update()

# Función para mostrar pantalla de carrito
def pantalla_carrito(page: ft.Page):
    page.clean()
    
    carrito_list = ft.ListView(spacing=10, expand=True)
    total = 0
    for i, p in enumerate(carrito):
        total += p["precio"]
        carrito_list.controls.append(
            ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(f"{p['nombre']} - ${p['precio']}", size=18),
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                on_click=lambda e, index=i: eliminar_carrito(index, page),
                                tooltip="Eliminar"
                            )
                        ]
                    )
                )
            )
        )
    
    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text("Carrito de Compras", size=30, weight=ft.FontWeight.BOLD),
                ft.ElevatedButton("Volver", on_click=lambda e: pantalla_productos(page))
            ]
        ),
        carrito_list,
        ft.Container(
            alignment=ft.alignment.center_right,
            padding=10,
            content=ft.Text(f"Total: ${total}", size=20, weight=ft.FontWeight.BOLD)
        )
    )

# Función para eliminar un producto del carrito con animación
def eliminar_carrito(index, page):
    carrito.pop(index)
    page.snack_bar = ft.SnackBar(
        ft.Text("Producto eliminado 🗑️"),
        open=True,
        duration=1000
    )
    pantalla_carrito(page)

# Pantalla principal
def main(page: ft.Page):
    page.title = "BravoVa Lite"
    page.window_width = 400
    page.window_height = 700
    page.scroll = "auto"
    pantalla_productos(page)

ft.app(target=main)
