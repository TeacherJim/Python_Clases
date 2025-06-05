import flet as ft


def cart_view() -> ft.Column:
    """Shopping cart screen."""

    return ft.Column(
        [
            ft.Text("Carrito", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Aquí van los productos agregados"),
        ]
    )
