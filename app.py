
from flask import Flask, request, render_template_string
from calculatrice import addition, soustraction, multiplication, division

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def accueil():
    resultat = None

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        operation = request.form["operation"]

        if operation == "addition":
            resultat = addition(a, b)
        elif operation == "soustraction":
            resultat = soustraction(a, b)
        elif operation == "multiplication":
            resultat = multiplication(a, b)
        elif operation == "division":
            resultat = "Division impossible" if b == 0 else division(a, b)

    return render_template_string("""
        <h1>Ma calculatrice CI/CD</h1>
        <form method="POST">
            <input type="number" step="any" name="a" required>
            <input type="number" step="any" name="b" required>
            <select name="operation">
                <option value="addition">Addition</option>
                <option value="soustraction">Soustraction</option>
                <option value="multiplication">Multiplication</option>
                <option value="division">Division</option>
            </select>
            <button type="submit">Calculer</button>
        </form>
        <h2>Résultat : {{ resultat if resultat is not none else "" }}</h2>
    """, resultat=resultat)

if __name__ == "__main__":
    app.run(debug=True)
