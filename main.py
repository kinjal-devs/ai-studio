import flet as ft

BG = "#F5F1F7"
SURFACE = "#FFFCFF"
INK = "#292130"
MUTED = "#817687"
PLUM = "#493454"
VIOLET = "#80639A"
LILAC = "#E9DDF0"
PINK = "#E9C9D9"
BORDER = "#E8E0EA"

def main(page: ft.Page):
    page.title = "Mom's AI Studio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = BG
    page.padding = 0
    page.window_width = 430
    page.window_min_width = 320
    page.window_height = 900
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=PLUM, surface=SURFACE))
    page.fonts = {"Display": "https://fonts.googleapis.com/css2?family=DM+Serif+Display&display=swap"}

    content = ft.Column(expand=True, spacing=0, scroll=ft.ScrollMode.AUTO)

    def snack(message):
        page.snack_bar = ft.SnackBar(content=ft.Text(message), bgcolor=PLUM)
        page.snack_bar.open = True
        page.update()

    def text(value, size=14, color=INK, weight=None, font=None):
        return ft.Text(value, size=size, color=color, weight=weight, font_family=font)

    def pill(label, color=LILAC):
        return ft.Container(content=text(label, 11, PLUM, ft.FontWeight.W_600), bgcolor=color, padding=ft.padding.symmetric(horizontal=12, vertical=7), border_radius=30)

    def section_title(kicker, title, subtitle=None):
        items = [text(kicker.upper(), 10, VIOLET, ft.FontWeight.BOLD), text(title, 25, INK, font="Display")]
        if subtitle:
            items.append(text(subtitle, 13, MUTED))
        return ft.Column(items, spacing=5)

    def card(title, subtitle, icon, action, tint=LILAC):
        return ft.Container(
            content=ft.Row([
                ft.Container(content=ft.Icon(icon, color=PLUM, size=23), bgcolor=tint, width=48, height=48, border_radius=16, alignment=ft.alignment.center),
                ft.Column([text(title, 15, INK, ft.FontWeight.W_600), text(subtitle, 11, MUTED)], spacing=4, expand=True),
                ft.Icon(ft.Icons.CHEVRON_RIGHT, color=MUTED)
            ], spacing=12),
            bgcolor=SURFACE, padding=14, border=ft.border.all(1, BORDER), border_radius=20,
            on_click=action
        )

    def show_home():
        content.controls = [
            ft.Container(
                content=ft.Column([
                    ft.Row([ft.Column([text("MOM'S AI STUDIO", 10, "#E9DDF0", ft.FontWeight.BOLD), text("A little imagination\ngoes a long way.", 29, "#FFFFFF", font="Display")], spacing=7), ft.Container(content=ft.Icon(ft.Icons.AUTO_AWESOME, color="#FFFFFF", size=27), bgcolor="#FFFFFF22", padding=13, border_radius=18)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    text("Create beautiful moving moments from your ideas.", 13, "#E9DDF0"),
                    ft.Row([pill("YOUR CREATIVE SPACE", "#FFFFFF22"), text("✦  Made with love", 11, "#F5EAF7")], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                ], spacing=18),
                bgcolor=PLUM, padding=22, border_radius=26
            ),
            ft.Container(height=24),
            section_title("MAKE SOMETHING", "What would you like to create?"),
            ft.Container(height=12),
            card("Text to Video", "Turn a written idea into a video", ft.Icons.EDIT_NOTE, lambda e: show_create("Text to Video")),
            ft.Container(height=10),
            card("Image to Video", "Bring a favourite picture to life", ft.Icons.IMAGE_OUTLINED, lambda e: show_create("Image to Video"), PINK),
            ft.Container(height=25),
            section_title("FIND YOUR NEXT IDEA", "A little inspiration"),
            ft.Container(height=12),
            ft.Row([
                ft.Container(content=ft.Column([ft.Icon(ft.Icons.LANDSCAPE, color=PLUM, size=24), text("Cinematic\nnature", 13, INK, ft.FontWeight.W_600)], spacing=12), bgcolor="#E9E2EF", padding=15, border_radius=18, expand=True),
                ft.Container(content=ft.Column([ft.Icon(ft.Icons.AUTO_AWESOME, color=PLUM, size=24), text("Dreamlike\nscenes", 13, INK, ft.FontWeight.W_600)], spacing=12), bgcolor="#F0E2E8", padding=15, border_radius=18, expand=True),
            ], spacing=10),
            ft.Container(height=24),
            ft.Container(content=ft.Row([ft.Icon(ft.Icons.INFO_OUTLINE, color=VIOLET), ft.Column([text("Your creative workspace", 13, INK, ft.FontWeight.W_600), text("Connect a video provider when you're ready to generate.", 11, MUTED)], spacing=3, expand=True)], spacing=12), padding=15, bgcolor="#EEE8F1", border_radius=18)
        ]
        content.spacing = 0
        page.update()

    def show_create(mode="Text to Video"):
        mode_value = ft.Ref[ft.Dropdown]()
        prompt = ft.Ref[ft.TextField]()
        upload_note = ft.Ref[ft.Text]()
        content.controls = [
            section_title("CREATION STUDIO", "Make your idea move", "Shape the details of your next video."),
            ft.Container(height=18),
            ft.Container(content=ft.Row([ft.Container(content=text("Text to Video", 12, PLUM, ft.FontWeight.W_600), bgcolor="#E9DDF0" if mode=="Text to Video" else SURFACE, padding=11, border_radius=12, expand=True, alignment=ft.alignment.center, on_click=lambda e: show_create("Text to Video")), ft.Container(content=text("Image to Video", 12, PLUM, ft.FontWeight.W_600), bgcolor="#E9DDF0" if mode=="Image to Video" else SURFACE, padding=11, border_radius=12, expand=True, alignment=ft.alignment.center, on_click=lambda e: show_create("Image to Video"))], spacing=8), padding=5, bgcolor="#FFFFFF", border_radius=16),
            ft.Container(height=20),
            text("YOUR PROMPT", 10, VIOLET, ft.FontWeight.BOLD),
            ft.TextField(ref=prompt, multiline=True, min_lines=5, max_lines=7, hint_text="Describe the scene you imagine...\n\nExample: A quiet lavender field at golden hour, with a soft breeze moving through the flowers.", border_color=BORDER, focused_border_color=VIOLET, bgcolor=SURFACE, border_radius=16, text_size=13),
        ]
        if mode == "Image to Video":
            content.controls += [ft.Container(height=12), ft.OutlinedButton("Choose an image", icon=ft.Icons.ADD_PHOTO_ALTERNATE, on_click=lambda e: snack("Image upload will be enabled in the next build.")), ft.Text("Image upload is not connected yet.", ref=upload_note, size=11, color=MUTED)]
        content.controls += [
            ft.Container(height=18),
            text("VIDEO SETTINGS", 10, VIOLET, ft.FontWeight.BOLD),
            ft.Row([
                ft.Column([text("Aspect ratio", 11, MUTED), ft.Dropdown(width=145, value="9:16 · Portrait", options=[ft.dropdown.Option("9:16 · Portrait"), ft.dropdown.Option("16:9 · Landscape"), ft.dropdown.Option("1:1 · Square")], border_color=BORDER, text_size=12)], spacing=6, expand=True),
                ft.Column([text("Duration", 11, MUTED), ft.Dropdown(width=130, value="5 seconds", options=[ft.dropdown.Option("5 seconds"), ft.dropdown.Option("10 seconds"), ft.dropdown.Option("Provider default")], border_color=BORDER, text_size=12)], spacing=6)
            ], spacing=10),
            ft.Container(height=22),
            ft.FilledButton("Prepare my video  ✦", icon=ft.Icons.AUTO_AWESOME, on_click=lambda e: snack("Your prompt is ready. Connect a video-generation provider and API key in a future setup step to create real videos."), style=ft.ButtonStyle(bgcolor=PLUM, color="#FFFFFF", padding=18, shape=ft.RoundedRectangleBorder(radius=14)), width=float("inf")),
            ft.Container(height=10),
            text("No video is generated yet. This app will only show a real result after a provider is connected.", 10, MUTED),
        ]
        page.update()

    def show_explore():
        content.controls = [
            section_title("EXPLORE", "Ideas worth imagining", "A few directions to get your creativity flowing."),
            ft.Container(height=18),
            ft.TextField(hint_text="Search inspiration", prefix_icon=ft.Icons.SEARCH, border_color=BORDER, bgcolor=SURFACE, border_radius=14),
        ]
        ideas = [("Cinematic nature","Wide landscapes, gentle movement and golden light",ft.Icons.WB_SUNNY),("Dreamlike scenes","Surreal colours and floating, magical details",ft.Icons.AUTO_AWESOME),("Warm memories","Soft nostalgic moments and film-like tones",ft.Icons.FAVORITE_BORDER),("Modern motion","Clean shapes, bold transitions and fresh energy",ft.Icons.MOTION_PHOTOS_ON)]
        for title,desc,ic in ideas:
            content.controls += [ft.Container(height=10),card(title,desc,ic,lambda e,t=title: snack(f"{t} inspiration selected."))]
        page.update()

    def show_library():
        content.controls = [
            section_title("MY CREATIONS", "Your personal library", "The videos you create will live here."),
            ft.Container(height=30),
            ft.Container(content=ft.Column([ft.Container(content=ft.Icon(ft.Icons.VIDEO_LIBRARY_OUTLINED, size=38, color=VIOLET), bgcolor=LILAC, padding=22, border_radius=24), text("Your gallery is waiting", 18, INK, ft.FontWeight.W_600), text("Once a video provider is connected and you create something, your creations can appear here.", 12, MUTED)], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=12), padding=30, bgcolor=SURFACE, border=ft.border.all(1,BORDER), border_radius=22, alignment=ft.alignment.center),
            ft.Container(height=18),
            ft.FilledButton("Start creating", icon=ft.Icons.ADD, on_click=lambda e: show_create(), style=ft.ButtonStyle(bgcolor=PLUM,color="#FFFFFF"), width=float("inf"))
        ]
        page.update()

    def show_settings():
        content.controls = [
            section_title("PREFERENCES", "Settings & help", "Keep your creative space just the way you like it."),
            ft.Container(height=18),
            card("Generation provider","Provider connection is not set up",ft.Icons.CLOUD_OUTLINED,lambda e: snack("Provider setup will be added after choosing a supported video-generation service.")),
            ft.Container(height=10),
            card("Privacy & API keys","Keep your keys private and secure",ft.Icons.LOCK_OUTLINE,lambda e: snack("Never share or commit a real API key. Store it locally in your .env file.")),
            ft.Container(height=10),
            card("Help & guidance","Learn how to use the studio",ft.Icons.HELP_OUTLINE,lambda e: snack("Choose a creation mode, write a prompt, then connect a provider to generate.")),
            ft.Container(height=24),
            text("ABOUT",10,VIOLET,ft.FontWeight.BOLD),
            ft.Container(height=8),
            ft.Container(content=ft.Column([text("Mom's AI Studio",16,INK,ft.FontWeight.W_600),text("A thoughtful creative workspace, made with love.",12,MUTED),text("Version 0.1 · Early build",10,MUTED)],spacing=6),padding=17,bgcolor=SURFACE,border=ft.border.all(1,BORDER),border_radius=18)
        ]
        page.update()

    def navigate(e):
        idx = e.control.selected_index
        [show_home, show_create, show_explore, show_library, show_settings][idx]()

    page.add(ft.Container(content=ft.Column([
        ft.Container(content=ft.Row([ft.Column([text("MOM'S AI STUDIO",10,VIOLET,ft.FontWeight.BOLD),text("Create something lovely",16,INK,ft.FontWeight.W_600)],spacing=2),ft.Container(content=ft.Icon(ft.Icons.AUTO_AWESOME,color=PLUM),bgcolor=LILAC,padding=10,border_radius=14)],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),padding=ft.padding.only(left=20,right=20,top=17,bottom=12)),
        ft.Container(content=content,expand=True,padding=ft.padding.symmetric(horizontal=20,vertical=8)),
        ft.NavigationBar(destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME_OUTLINED,selected_icon=ft.Icons.HOME,label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD_CIRCLE_OUTLINE,label="Create"),
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE_OUTLINED,label="Explore"),
            ft.NavigationBarDestination(icon=ft.Icons.VIDEO_LIBRARY_OUTLINED,label="Library"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS_OUTLINED,label="Settings"),
        ],on_change=navigate,bgcolor=SURFACE,indicator_color=LILAC)
    ],spacing=0,expand=True),expand=True,bgcolor=BG))
    show_home()

ft.app(target=main)
