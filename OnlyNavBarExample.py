import flet as ft

from views.home_view import HomeView
from views.cart_view import CartView
from views.profile_view import ProfileView


def main(page: ft.Page):
    """Example using only NavigationBar."""
    page.title = "Ejemplo NavigationBar"
    page.theme_mode = ft.ThemeMode.LIGHT

    current_view = ft.Container(expand=True)
    views = [HomeView(), CartView(), ProfileView()]
    current_view.content = views[0]

    def on_change(e: ft.ControlEvent):
        current_view.content = views[e.control.selected_index]
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
