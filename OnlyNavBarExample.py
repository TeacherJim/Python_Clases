import flet as ft

from views.home_view import home_view
from views.cart_view import cart_view
from views.profile_view import profile_view


def main(page: ft.Page):
    """Example using only NavigationBar."""
    page.title = "Ejemplo NavigationBar"
    page.theme_mode = ft.ThemeMode.LIGHT

    current_view = ft.Container(expand=True)
    views = [home_view, cart_view, profile_view]
    current_view.content = views[0]()

    def on_change(e: ft.ControlEvent):
        current_view.content = views[e.control.selected_index]()
        page.update()

    nav = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SHOPPING_CART, label="Cart"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile"),
        ],
        on_change=on_change,
    )

    page.add(ft.Column([nav, current_view], expand=True))


if __name__ == "__main__":
    ft.app(target=main)
