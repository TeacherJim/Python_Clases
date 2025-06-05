import flet as ft

class ProfileView(ft.UserControl):
    """User profile screen."""

    def build(self) -> ft.Control:
        return ft.Column(
            [
                ft.Text("Perfil", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Información del usuario"),
            ]
        )


def profile_view() -> ft.Control:
    """Functional version of :class:`ProfileView`."""
    return ft.Column(
        [
            ft.Text("Perfil", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Información del usuario"),
        ]
    )
