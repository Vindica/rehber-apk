import flet as ft
import mysql.connector
import bcrypt

# --- IP ADRESİ AYARI ---
# Telefonda çalışması için buraya bilgisayarının IPv4 adresini yazmalısın.
# CMD -> ipconfig yazarak bulabilirsin.
DB_CONFIG = {'user': 'root', 'password': '1234', 'host': '192.168.1.133', 'database': 'rehberdb'} 

def main(page: ft.Page):
    page.title = "Rehber Mobil"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "adaptive"

    lbl_title = ft.Text("Rehber Giriş", size=32, weight="bold", color="blue")
    
    txt_username = ft.TextField(label="Kullanıcı Adı", width=280, icon=ft.icons.PERSON)
    txt_password = ft.TextField(label="Şifre", password=True, can_reveal_password=True, width=280, icon=ft.icons.LOCK)

    def login_click(e):
        if not txt_username.value or not txt_password.value:
            page.snack_bar = ft.SnackBar(ft.Text("Alanları doldur PATRON!"), open=True); page.update(); return

        btn_login.text = "Kontrol ediliyor..."; btn_login.disabled = True; page.update()
        
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username=%s", (txt_username.value,))
            response = cursor.fetchone()
            conn.close()

            if response and bcrypt.checkpw(txt_password.value.encode(), response[0].encode() if isinstance(response[0], str) else response[0]):
                page.snack_bar = ft.SnackBar(ft.Text("Giriş Başarılı! Hoşgeldin."), bgcolor="green", open=True)
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Hatalı bilgiler!"), bgcolor="red", open=True)
        except Exception as err:
            page.snack_bar = ft.SnackBar(ft.Text(f"Bağlantı Hatası: {err}"), bgcolor="red", open=True)
        finally:
            btn_login.text = "Giriş Yap"; btn_login.disabled = False; page.update()

    btn_login = ft.ElevatedButton("Giriş Yap", width=280, height=50, on_click=login_click)

    page.add(ft.Icon(ft.icons.TRAVEL_EXPLORE, size=100, color="blue"), lbl_title, txt_username, txt_password, btn_login)

ft.app(target=main)