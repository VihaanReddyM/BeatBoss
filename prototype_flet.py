import flet as ft
from dab_api import DabAPI
import threading

def main(page: ft.Page):
    page.title = "DAB Music - Flet Prototype"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#020202"
    page.padding = 0
    page.spacing = 0
    page.window_width = 1300
    page.window_height = 850

    # Fonts
    page.fonts = {
        "Segoe UI": "https://github.com/google/fonts/raw/main/apache/robotocondensed/static/RobotoCondensed-Bold.ttf"
    }

    # Glass Style Utility
    def glass_layer(width=None, height=None, radius=20, blur=20, opacity=0.05):
        return ft.Container(
            width=width,
            height=height,
            border_radius=radius,
            bgcolor=ft.Colors.with_opacity(opacity, ft.Colors.WHITE),
            blur=ft.Blur(blur, blur, ft.BlurStyle.OUTER),
            border=ft.Border.all(0.5, ft.Colors.with_opacity(0.1, ft.Colors.WHITE)),
        )

    # Sidebar Navigation Item
    def nav_item(icon, text, selected=False):
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon, color=ft.Colors.GREEN if selected else ft.Colors.WHITE_70, size=20),
                ft.Text(text, color=ft.Colors.WHITE if selected else ft.Colors.WHITE_70, weight="bold", size=14)
            ], alignment=ft.MainAxisAlignment.START),
            padding=ft.Padding(left=20, top=12, right=0, bottom=12),
            border_radius=10,
            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.GREEN) if selected else ft.Colors.TRANSPARENT,
            on_hover=lambda e: setattr(e.control, "bgcolor", ft.Colors.with_opacity(0.1, ft.Colors.WHITE) if e.data == "true" and not selected else (ft.Colors.with_opacity(0.1, ft.Colors.GREEN) if selected else ft.Colors.TRANSPARENT)) or page.update()
        )

    # 1. Sidebar
    sidebar = ft.Container(
        width=260,
        height=page.window_height,
        padding=20,
        bgcolor="#0A0A0A",
        content=ft.Column([
            ft.Row([
                ft.Icon(ft.Icons.MUSIC_NOTE, color=ft.Colors.GREEN, size=32),
                ft.Text("DAB", size=24, weight="bold")
            ], alignment=ft.MainAxisAlignment.START),
            ft.Container(height=40),
            nav_item(ft.Icons.HOME, "Home", True),
            nav_item(ft.Icons.SEARCH, "Search"),
            nav_item(ft.Icons.LIBRARY_MUSIC, "Library"),
            ft.Divider(height=40, color=ft.Colors.WHITE_10),
            nav_item(ft.Icons.ADD_BOX, "Create Playlist"),
            nav_item(ft.Icons.FAVORITE, "Favorites"),
            nav_item(ft.Icons.MONITOR, "Monitor"),
        ])
    )

    # 2. Main Dashboard (Floating Card)
    search_bar = ft.TextField(
        hint_text="Search tracks, artists...",
        prefix_icon=ft.Icons.SEARCH,
        border_radius=25,
        bgcolor="#121212",
        border_color=ft.Colors.TRANSPARENT,
        focused_border_color=ft.Colors.GREEN,
        height=45,
        content_padding=10,
        expand=True
    )

    import_btn = ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.IMPORT_EXPORT, size=18, color=ft.Colors.BLACK),
            ft.Text("IMPORT", weight="bold", color=ft.Colors.BLACK)
        ]),
        bgcolor=ft.Colors.GREEN,
        padding=ft.Padding(left=20, top=10, right=20, bottom=10),
        border_radius=25,
        on_click=lambda _: None
    )

    main_content = ft.Container(
        expand=True,
        bgcolor="#020202",
        padding=ft.Padding(left=40, top=30, right=40, bottom=0),
        content=ft.Column([
            ft.Row([search_bar, ft.Container(width=20), import_btn]),
            ft.Container(height=40),
            ft.Text("Discover Modernity", size=48, weight="bold"),
            ft.Text("Welcome back, Explorer", color=ft.Colors.WHITE_30, size=18),
            ft.Container(height=30),
            # Placeholder for track grid
            ft.GridView(
                expand=True,
                runs_count=5,
                max_extent=250,
                child_aspect_ratio=0.8,
                spacing=20,
                run_spacing=20,
            )
        ])
    )

    # 3. Player Bar (Glass)
    player_bar = ft.Container(
        height=100,
        bgcolor=ft.Colors.with_opacity(0.8, "#0A0A0A"),
        blur=ft.Blur(20, 20),
        border=ft.Border(top=ft.BorderSide(0.5, ft.Colors.WHITE_10)),
        padding=ft.Padding(left=30, top=0, right=30, bottom=0),
        content=ft.Row([
            # Track Info
            ft.Row([
                ft.Container(width=60, height=60, bgcolor="#1A1A1A", border_radius=10),
                ft.Column([
                    ft.Text("No Track", size=14, weight="bold"),
                    ft.Text("Start your journey", size=12, color=ft.Colors.WHITE_30)
                ], spacing=2)
            ], spacing=15),
            
            # Controls
            ft.Column([
                ft.Row([
                    ft.IconButton(ft.Icons.SHUFFLE, icon_size=18, icon_color=ft.Colors.WHITE_30),
                    ft.IconButton(ft.Icons.SKIP_PREVIOUS, icon_size=24, icon_color=ft.Colors.WHITE),
                    ft.IconButton(ft.Icons.PLAY_CIRCLE_FILL, icon_size=48, icon_color=ft.Colors.WHITE),
                    ft.IconButton(ft.Icons.SKIP_NEXT, icon_size=24, icon_color=ft.Colors.WHITE),
                    ft.IconButton(ft.Icons.REPEAT, icon_size=18, icon_color=ft.Colors.WHITE_30),
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.Text("0:00", size=11, color=ft.Colors.WHITE_30),
                    ft.Slider(min=0, max=100, expand=True, active_color=ft.Colors.GREEN, inactive_color=ft.Colors.WHITE_10),
                    ft.Text("0:00", size=11, color=ft.Colors.WHITE_30),
                ], width=600)
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=0),
            
            # Utils
            ft.Row([
                ft.IconButton(ft.Icons.LYRICS, icon_size=20, icon_color=ft.Colors.WHITE_30),
                ft.IconButton(ft.Icons.VOLUME_UP, icon_size=20, icon_color=ft.Colors.WHITE_30),
                ft.Slider(width=100, value=80, min=0, max=100, active_color=ft.Colors.GREEN),
            ])
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )

    layout = ft.Column([
        ft.Row([sidebar, main_content], expand=True, spacing=0),
        player_bar
    ], expand=True, spacing=0)

    page.add(layout)

if __name__ == "__main__":
    ft.app(target=main)
