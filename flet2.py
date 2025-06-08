import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.START

    nome = ft.TextField(label="Nome", width=400)
    email = ft.TextField(label="Email", width=400)
    mensagem = ft.TextField(label="Mensagem", multiline=True, width=400, height=150)
    confirmacao = ft.Text(value="", color="green")

    def enviar_formulario(e):
        if nome.value and email.value and mensagem.value:
            confirmacao.value = "Formulário enviado com sucesso!"
            nome.value = ""
            email.value = ""
            mensagem.value = ""
        else:
            confirmacao.value = "Por favor, preencha todos os campos."
            confirmacao.color = "red"
        page.update()

    enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_formulario)

    page.add(
        ft.Text("Formulário de Contato", size=24, weight="bold"),
        nome,
        email,
        mensagem,
        enviar,
        confirmacao
    )

ft.app(target=main)
