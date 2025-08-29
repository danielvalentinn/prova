import flet as ft

def main(page: ft.Page):
    # Formato típico de celular (portrait)
    page.window_width = 360
    page.window_height = 640
    page.window_resizable = False  # Impede que o usuário redimensione
    page.bgcolor = ft.Colors.GREY_100

    # Campos de login
    login_username = ft.TextField(
        bgcolor=ft.Colors.GREY_100,
        hint_text='@email.com',
        width=300,
        prefix_icon=ft.Icons.EMAIL,
        border_radius=10,
        border_color=ft.Colors.GREY_400,
        label='Email'
    )

    login_password = ft.TextField(
        hint_text='Password',
        can_reveal_password=True,
        password=True,
        bgcolor=ft.Colors.GREY_100,
        border_radius=10,
        width=300,
        prefix_icon=ft.Icons.KEY,
        border_color=ft.Colors.GREY_400,
        label='Senha'
    )

    botao_google = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Image(
                    src="img/google.png",  # seu arquivo
                    width=24,
                    height=24
                ),
                ft.Text("Logar com o Google", size=14)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        width=300,
        bgcolor=ft.Colors.GREY_200,
        color=ft.Colors.BLACK,
        elevation=0,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )

    botao_apple = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Image(
                    src="img/apple.png",  # seu arquivo
                    width=20,
                    height=20
                ),
                ft.Text("Logar com a Apple", size=14)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        width=300,
        bgcolor=ft.Colors.GREY_200,
        color=ft.Colors.BLACK,
        elevation=0,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )

    botao_login = ft.ElevatedButton(
        text='Fazer Login',
        width=100,
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE,
        elevation=0,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),

    )

    criesuaconta = ft.Text(
    spans=[
        ft.TextSpan(text="Crie sua conta com e-mail "),
        ft.TextSpan(
            text="aqui",
            style=ft.TextStyle(
                color=ft.Colors.BLUE,
            ),
        ),
    ],
    text_align=ft.TextAlign.CENTER
)

    # Coluna centralizada
    coluna_login = ft.Column(
        [
            ft.Text(value='LOGIN', size=22, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
            login_username,
            login_password,
            botao_google,
            botao_apple,
            botao_login,
            criesuaconta
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    # Container para centralizar verticalmente
    container_central = ft.Container(
        content=coluna_login,
        alignment=ft.alignment.center,
        expand=True,
        padding=20
    )

    page.add(container_central)

ft.app(target=main)