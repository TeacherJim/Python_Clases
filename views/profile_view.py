import flet as ft


def profile_view() -> ft.Column:
    """User profile screen."""

    return ft.Column(
        [
            ft.Text("Perfil", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Información del usuario"),
        ]
    )
