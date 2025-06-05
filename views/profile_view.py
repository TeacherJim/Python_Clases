import flet as ft

def build_profile_view() -> ft.Control:
        return ft.Column(
            [
                ft.Text("Perfil", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Información del usuario"),
            ]
        )

