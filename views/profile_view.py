import flet as ft

    def build(self) -> ft.Control:
        return ft.Column(
            [
                ft.Text("Perfil", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Información del usuario"),
            ]
        )

