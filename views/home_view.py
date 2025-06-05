import flet as ft

class HomeView(ft.UserControl):
    """Simple home screen."""

    def build(self) -> ft.Control:
        return ft.Column(
            [
                ft.Text("Home", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Bienvenido a la tienda de ejemplo"),
            ]
        )
