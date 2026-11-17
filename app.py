
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "estoque-chave-2026"

estoque = {}


@app.route("/")
def inicio():
    return render_template("index.html", estoque=estoque)


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get("nome", "").strip()

    try:
        quantidade = int(request.form.get("quantidade", 0))
        preco = float(request.form.get("preco", 0))
    except ValueError:
        flash("Informe valores válidos.")
        return redirect(url_for("inicio"))

    if not nome or nome in estoque or quantidade < 0 or preco < 0:
        flash("Não foi possível cadastrar o produto.")
    else:
        estoque[nome] = {
            "quantidade": quantidade,
            "preco": preco
        }
        flash("Produto cadastrado com sucesso!")

    return redirect(url_for("inicio"))


@app.route("/entrada", methods=["POST"])
def entrada():
    nome = request.form.get("nome", "").strip()

    try:
        quantidade = int(request.form.get("quantidade", 0))
    except ValueError:
        quantidade = 0

    if nome not in estoque or quantidade <= 0:
        flash("Não foi possível registrar a entrada.")
    else:
        estoque[nome]["quantidade"] += quantidade
        flash("Entrada registrada com sucesso!")

    return redirect(url_for("inicio"))


@app.route("/saida", methods=["POST"])
def saida():
    nome = request.form.get("nome", "").strip()

    try:
        quantidade = int(request.form.get("quantidade", 0))
    except ValueError:
        quantidade = 0

    if (nome not in estoque or quantidade <= 0
            or quantidade > estoque[nome]["quantidade"]):
        flash("Não foi possível registrar a saída.")
    else:
        estoque[nome]["quantidade"] -= quantidade
        flash("Saída registrada com sucesso!")

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run()
