import flet as ft

def main(page: ft.Page):
  # page config
    page.title = 'Login Screen'
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False
    page.padding = 100
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

  # function called on click
    def btn_click(e):
        # verify if name and pass is not empty
        if all([name_input.value, pass_input.value]):
            dlg = ft.AlertDialog(
                title = ft.Text(f'Welcome {name_input.value}')
            )
            page.dialog = dlg
            dlg.open = True
            page.update()
        
    # user interface components
    page.appbar = ft.AppBar(title=ft.Text('Login Screen'), center_title=True)
    name_input = ft.TextField(
        label = 'Name', autofocus=True, hint_text='Type your name...'
    )
    pass_input = ft.TextField(
        label = 'Password', password=True, can_reveal_password=True
    )
    submit_btn = ft.ElevatedButton(
        text = 'Login', width=600, on_click=btn_click
    )
    page.update()
    page.add(name_input, pass_input, submit_btn)

ft.app(target=main)
