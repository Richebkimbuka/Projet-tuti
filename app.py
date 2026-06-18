from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)


def generer_mot_de_passe(
    longueur=16,
    majuscules=True,
    minuscules=True,
    chiffres=True,
    symboles=True
):
    caracteres = ""

    if majuscules:
        caracteres += string.ascii_uppercase

    if minuscules:
        caracteres += string.ascii_lowercase

    if chiffres:
        caracteres += string.digits

    if symboles:
        caracteres += "!@#$%^&*()_+-=[]{}"

    if not caracteres:
        return ""

    return "".join(
        secrets.choice(caracteres)
        for _ in range(longueur)
    )


@app.route("/", methods=["GET", "POST"])
def index():

    mot_de_passe = ""
    longueur = 16

    if request.method == "POST":

        longueur = int(
            request.form.get("longueur", 16)
        )

        mot_de_passe = generer_mot_de_passe(
            longueur=longueur,
            majuscules="majuscules" in request.form,
            minuscules="minuscules" in request.form,
            chiffres="chiffres" in request.form,
            symboles="symboles" in request.form
        )

    return render_template(
        "index.html",
        mot_de_passe=mot_de_passe,
        longueur=longueur
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )