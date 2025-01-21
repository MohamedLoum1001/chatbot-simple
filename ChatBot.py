from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Données FAQ
faq = [
    {"question": "Quels sont les programmes disponibles ?", "answer": "Ynov Maroc propose des programmes en informatique, management, création digitale et plus encore."},
    {"question": "Quelle est la durée des programmes ?", "answer": "La durée varie selon le programme, mais les cycles Bachelor durent 3 ans et les cycles Mastère durent 2 ans."},
    {"question": "Quels sont les frais de scolarité ?", "answer": "Les frais de scolarité dépendent du programme choisi. Veuillez contacter le service administratif pour plus de détails."},
    {"question": "Comment s'inscrire ?", "answer": "Pour vous inscrire, remplissez le formulaire en ligne sur notre site web ou contactez directement notre service des admissions."},
    {"question": "Quels sont les critères d'admission ?", "answer": "Les critères incluent un dossier académique solide et un entretien individuel avec notre équipe des admissions."},
    {"question": "Y a-t-il des bourses disponibles ?", "answer": "Oui, Ynov Maroc propose des bourses basées sur le mérite et des critères sociaux."},
    {"question": "Bonjour", "answer": "Bonjour ! Comment puis-je vous aider aujourd'hui ?"},
    {"question": "Licence 1", "answer": "La Licence 1 est la première étape de votre parcours. Vous y apprendrez les bases de votre domaine choisi."},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faq', methods=['GET'])
def get_faq():
    return jsonify(faq)

if __name__ == "__main__":
    app.run(debug=True)
