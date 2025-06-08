import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.START

    tasks = ft.Column()
    task_input = ft.TextField(label="Digite uma tarefa", width=300)
  
    def add_task(e):
        if task_input.value.strip() != "":
            tasks.controls.append(ft.Text(f"• {task_input.value.strip()}"))
            task_input.value = ""
            page.update()
            task_input.focus()


    add_button = ft.ElevatedButton(text="Adicionar", on_click=add_task)

    page.add(
        ft.Row([task_input, add_button], spacing=10),
        tasks
    )

ft.app(target=main)
