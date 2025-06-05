import flet as ft



def build_cart_view() -> ft.Control:
        return ft.Column(
            [
                ft.Text("Carrito", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Aquí van los productos agregados"),
            ]
        )


