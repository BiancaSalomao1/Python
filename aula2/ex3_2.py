def gerar_curriculo_html(nome, endereco, telefone, email, escolaridade, experiencia):
    html = f"""
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currículo de {nome}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f4f4f4;
            }}
            .curriculo {{

            }}
        </style>
    </head>
    <body>
        <div class="curriculo">
            <h1>Currículo de {nome}</h1>
            <p><strong>Endereço:</strong> {endereco}</p>
            <p><strong>Telefone:</strong> {telefone}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Escolaridade:</strong> {escolaridade}</p>
            <p><strong>Experiência Profissional:</strong> {experiencia}</p>
        </div>
    </body>
    </html>
    """
    return html


def main():
    nome = input("Digite seu nome: ")
    endereco = input("Digite seu endereço: ")
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu email: ")
    escolaridade = input("Digite sua escolaridade: ")
    experiencia = input("Digite sua experiência profissional: ")

    curriculo_html = gerar_curriculo_html(nome, endereco, telefone, email, escolaridade, experiencia)
    
    with open("curriculo.html", "w") as file:
        file.write(curriculo_html)

    print("Currículo gerado com sucesso! Verifique o arquivo 'curriculo.html'.")


main()