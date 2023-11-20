from flask import Flask, redirect, render_template, request, url_for
import repositorio

app = Flask(__name__)

# Ao obter dados do servidor, a máquina do cliente usa um GET
# Ao enviar dados para o servidor, a máquina do cliente usa um POST

#Rota que retorna os personagens
@app.route("/")
def exibir_personagens():
    lista_personagens = repositorio.retornar_personagens()
    return render_template('index.html', personagens = lista_personagens)

#Esta rota cria, atualiza, exclui e salva um personagem no template cadastro.html e renderiza os dados na página index.html
@app.route("/personagem/<int:id>", methods=['GET', 'POST'])
def exibir_personagem(id):

    if request.method == 'POST':
        #Excluíndo ou salvando um personagem
        if "excluir" in request.form:
           repositorio.remover_personagem(id)
           return redirect(url_for('exibir_personagens'))
        elif "salvar" in request.form: 
            id = request.form["id"]
            nome = request.form["nome"]
            descricao = request.form["descricao"]
            casa = request.form["casa"]
            imagem = request.form["imagem"]

            #Atualizando ou criando um novo personagem
            dados_retornados = repositorio.retornar_personagem(id)
            if dados_retornados:
               repositorio.atualizar_personagem(id = id, nome = nome, descricao = descricao, casa = casa, imagem = imagem)
            else:
               repositorio.criar_personagem(nome = nome, descricao = descricao, casa = casa, imagem = imagem)
          
            return redirect(url_for('exibir_personagens'))
    else:
    
     id, nome, descricao, casa, imagem = repositorio.retornar_personagem(id)
     
    return render_template('cadastro.html', id = id, nome = nome, descricao = descricao, casa = casa, imagem = imagem)

app.run(debug=True)
