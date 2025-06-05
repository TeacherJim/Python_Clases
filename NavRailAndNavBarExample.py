import flet as ft

def main(page: ft.Page):
    page.title = "Mini Amazon - Navegación"
    page.theme_mode = ft.ThemeMode.LIGHT

    label = ft.Text("¡Bienvenido a Mini Amazon!")

    def on_navigation_change(e):
        opciones = ["Home", "Cart", "Profile"]
        seleccion = opciones[e.control.selected_index]
        label.value = f"Ahora estás en: {seleccion}"
        page.update()

    nav = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SHOPPING_CART, label="Cart"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile")
        ],
        on_change=on_navigation_change
    )

    rail = ft.NavigationRail(
        selected_index=0,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationRailDestination(icon=ft.Icons.SHOPPING_CART, label="Cart"),
            ft.NavigationRailDestination(icon=ft.Icons.PERSON, label="Profile")
        ],
        on_change=on_navigation_change
    )

    page.add(
        ft.Row([
            rail,
            ft.Column([
                nav,
                label
            ])
        ])
    )

ft.app(target=main)
