import flet as ft



def build_home_view() -> ft.Control:
        return ft.Column(
            [
                ft.Text("Home", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Bienvenido a la tienda de ejemplo"),
            ]
        )

