import flet as ft


def home_view() -> ft.Column:
    """Simple home screen."""

    return ft.Column(
        [
            ft.Text("Home", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Bienvenido a la tienda de ejemplo"),
        ]
    )
