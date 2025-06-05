import flet as ft

from views.home_view import HomeView
from views.cart_view import CartView
from views.profile_view import ProfileView


def main(page: ft.Page):
    """Example using NavigationRail and NavigationBar."""
    page.title = "Mini Amazon - Navegación"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Container to show the current view
    current_view = ft.Container(expand=True)

    # Instantiate views created in separate modules
    views = [HomeView(), CartView(), ProfileView()]
    current_view.content = views[0]  # start on Home

    def on_navigation_change(e: ft.ControlEvent):
        """Callback to switch visible view."""
        current_view.content = views[e.control.selected_index]
        page.update()

    nav = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SHOPPING_CART, label="Cart"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile"),
        ],
        on_change=on_navigation_change,
    )

    rail = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationRailDestination(icon=ft.Icons.SHOPPING_CART, label="Cart"),
            ft.NavigationRailDestination(icon=ft.Icons.PERSON, label="Profile"),
        ],
        on_change=on_navigation_change,
    )

    # Layout with NavigationRail on the left and NavigationBar on top
    page.add(
        ft.Row(
            [
                rail,
                ft.Column(
                    [
                        nav,
                        current_view,
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
