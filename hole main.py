import flet as ft
def main(page: ft.Page)
    page.title = "simple flet app"
    page.add(ft.Text "hola flet")
    txt.number = ft.TextField(value="0")
    def incrementar(0):
        txt.number.value = str(int (txt.number.value) +1)
        page.update(ft.ElevatedButton("incrementar", on_click=incrementar))
        page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))
        
ft.app(main):
    