import flet as ft

from views.home_view import HomeView
from views.cart_view import CartView
from views.profile_view import ProfileView


def main(page: ft.Page):
    """Example using only NavigationRail."""
    page.title = "Ejemplo NavigationRail"
    page.theme_mode = ft.ThemeMode.LIGHT

    current_view = ft.Container(expand=True)
    views = [HomeView(), CartView(), ProfileView()]
    current_view.content = views[0]

    def on_change(e: ft.ControlEvent):
        current_view.content = views[e.control.selected_index]
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationRailDestination(icon=ft.Icons.SHOPPING_CART, label="Cart"),
            ft.NavigationRailDestination(icon=ft.Icons.PERSON, label="Profile"),
        ],
        on_change=on_change,
    )

    page.add(ft.Row([rail, current_view], expand=True))


if __name__ == "__main__":
    ft.app(target=main)
