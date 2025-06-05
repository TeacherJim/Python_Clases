import flet as ft

class CartView(ft.UserControl):
    """Shopping cart screen."""

    def build(self) -> ft.Control:
        return ft.Column(
            [
                ft.Text("Carrito", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Aquí van los productos agregados"),
            ]
        )
