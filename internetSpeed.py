import flet as ft
import speedtest
from time import sleep


def main(page: ft.Page):
    page.title = "Internet Speed Test"
    page.theme_mode = 'dart'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_bgcolor = 'blue'
    page.padding = 20
    page.bgcolor = "black"

    # enab scroll in the page
    page.auto_scroll = True

    # config the fonts
    page.fonts = {
        "RoosterPersonalUse": "fonts/RoosterPersonalUse-3z8d8.ttf",
        "SourceCodePro-BlackItalic": "fonts/SourceCodePro-BlackItalic.ttf",
        "SourceCodePro-Bold": "fonts/SourceCodePro-Bold.ttf"
    }
    # initializinf speed test
    # Don't name your file speedtest.py. It will causean big confusion
    st = speedtest.Speedtest()

    # the heading of the app
    appTitle = ft.Row(
        controls=[
            ft.Text("Internet", font_family="RoosterPersonalUse",
                    style="displayLarge", color="#ff3300"),
            ft.Text("Speed", font_family="RoosterPersonalUse",
                    style="displayLarge", color="#ffff00"),

        ],
        alignment='center',
    )
    # termi lines
    line_01 = ft.Text(value="> Press start...",
                      font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_02 = ft.Text(value="",
                      font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_03 = ft.Text(value="",
                      font_family="SourceCodePro-BlackItalic", color="#1aff1a")

    # Progress bar
    progress_bar_01 = ft.ProgressBar(
        width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text_01 = ft.Text(
        value=" ", font_family="SourceCodePro-Bold", opacity=0)
    progress_row_01 = ft.Row([progress_text_01, progress_bar_01])

    line_04 = ft.Text(value="",
                      font_family="SourceCodePro-Bold", color="#ffff00")
    line_05 = ft.Text(value="",
                      font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    progress_bar_02 = ft.ProgressBar(
        width=400, color="#0080ff", bgcolor="#eeeeee", opacity=0)
    progress_text_02 = ft.Text(
        value=" ", font_family="SourceCodePro-Bold", opacity=0)
    progress_row_02 = ft.Row([progress_text_02, progress_bar_02])

    line_06 = ft.Text(value="",
                      font_family="SourceCodePro-BlackItalic", color="#1aff1a")
    line_07 = ft.Text(value="",
                      font_family="SourceCodePro-Bold", color="#1aff1a")
    line_08 = ft.Text(value="",
                      font_family="SourceCodePro-BlackItalic", color="#ffffff")
    termilText = ft.Column(
        [line_01, line_02,
         line_03, progress_row_01, line_04,
         line_05, line_06, progress_row_02,
         line_07, line_08]
    )

    # The container to display internet infos
    getSpeedContainer = ft.Container(
        content=termilText,
        width=200,
        height=100,
        bgcolor="#4d4d4d",
        border_radius=35,
        animate=ft.animation.Animation(1000, "bounceOut")
    )

    # Terminal animation fonction
    def animate_getSpeedContainer(e):
        progress_row_01.opacity = 0
        progress_bar_01.opacity = 0
        progress_bar_02.opacity = 0
        progress_row_02.opacity = 0
        progress_bar_02.value = None
        progress_bar_01.value = None
        line_01.value = ""
        line_02.value = ""
        line_03.value = ""
        line_04.value = ""
        line_05.value = ""
        line_06.value = ""
        line_07.value = ""
        line_08.value = ""

        getSpeedContainer.update()
        getSpeedContainer.width = 700
        getSpeedContainer.height = 400
        line_01.value = "> calculing download speed, please wait..."
        getSpeedContainer.update()
        sleep(2)

        ideal_server = st.get_best_server()  # find the best server and connect
        city = ideal_server['name']
        country = ideal_server['country']
        cc = ideal_server['cc']
        line_02.value = f">Finding the best possible server in {city},{country}({
            cc})"
        getSpeedContainer.update()
        sleep(4)

        line_03.value = "> Connexion stablished , status OK"
        progress_row_01.opacity = 1
        progress_bar_01.opacity = 1
        getSpeedContainer.update()

        download_speed = st.download()/1024/1024
        progress_bar_01.value = 1
        line_04.value = f"> The download speed is {
            str(round(download_speed, 2))}Mbps"
        getSpeedContainer.update()

        line_05.value = "> Calculating upload speed, please wait..."
        getSpeedContainer.update()
        sleep(2)
        line_06.value = "> Executing upload script, hold on..."
        progress_row_02.opacity = 1
        progress_bar_02.opacity = 1
        getSpeedContainer.update()
        upload_speed = st.upload()/1024/1024
        progress_bar_02.value = 1
        line_07.value = f"The upload speed is {
            str(round(upload_speed, 2))}Mbps"
        getSpeedContainer.update()
        sleep(2)
        line_08.value = ">completed successfully\n\n >>"
        "App Developped by SouleCode"
        getSpeedContainer.update()

    # Page components
    page.add(
        appTitle,
        getSpeedContainer,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED,
                      on_click=animate_getSpeedContainer,
                      icon_color="#1aff1a", icon_size=50,
                      ),
    )


ft.app(target=main, assets_dir="assets")
