import flet as ft
# DİKKAT: Veritabanı ve Bcrypt kütüphanelerini kaldırdık!
# import mysql.connector  <-- SİLDİK
# import bcrypt           <-- SİLDİK

def main(page: ft.Page):
    page.title = "Rehber Test"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    lbl_info = ft.Text("PATRON! EKRAN GELDİ!", size=30, weight="bold", color="green", text_align="center")
    lbl_sub = ft.Text("Sorun veritabanı kütüphanesindeymiş.", size=16, color="black")

    def button_click(e):
        lbl_info.value = "Buton da Çalışıyor!"
        lbl_info.color = "blue"
        page.update()

    btn_test = ft.ElevatedButton("Tıkla Bana", on_click=button_click, height=50, width=200)

    # İkonları da 'hazır' ikonlardan seçtik ki internet yavaşsa bile görünsün
    page.add(
        ft.Icon(ft.icons.CHECK_CIRCLE, size=100, color="green"),
        ft.Container(height=20),
        lbl_info,
        lbl_sub,
        ft.Container(height=20),
        btn_test
    )

ft.app(target=main)
