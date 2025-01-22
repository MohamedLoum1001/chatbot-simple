from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Données FAQ
faq = [
    {
        "question": "Bonjour",
        "answer": "Bonjour ! Je suis le chatbot de Ynov Maroc. Tu peux cliquer sur les 3 questions ?",
        "follow_up": [
            {
                "question": "Comment se passe votre journée ?",
                "answer": "Merci de demander ! Ma journée se passe bien.",
            },
            {
                "question": "Avez-vous des questions sur nos programmes ?",
                "answer": "Oui, nous avons plusieurs programmes disponibles.",
            },
            {
                "question": "Souhaitez-vous plus d'informations sur l'admission ?",
                "answer": "Bien sûr ! Les informations sur l'admission peuvent être trouvées sur notre site web.",
            }
        ]
    },
    {
        "question": "Quels sont les programmes disponibles ?",
        "answer": "Ynov Maroc propose des programmes en informatique, management, création digitale et plus encore.",
        "follow_up": [
            {
                "question": "Avez-vous une préférence pour un domaine spécifique ?",
                "answer": "Nous avons plusieurs domaines. Que préférez-vous ?",
            },
            {
                "question": "Voulez-vous des détails sur le programme en informatique ?",
                "answer": "Le programme en informatique couvre le développement web, la programmation, et bien plus.",
            },
            {
                "question": "Êtes-vous intéressé par les programmes de création digitale ?",
                "answer": "Oui, nos programmes de création digitale sont très populaires.",
            }
        ]
    },
    {
        "question": "Quelle est la durée des programmes ?",
        "answer": "La durée varie selon le programme, mais les cycles Bachelor durent 3 ans et les cycles Mastère durent 2 ans.",
        "follow_up": [
            {
                "question": "Souhaitez-vous des détails sur un programme spécifique ?",
                "answer": "Bien sûr, dites-moi sur quel programme vous voulez plus d'informations.",
            },
            {
                "question": "Avez-vous des questions sur le processus d'inscription ?",
                "answer": "Le processus d'inscription est simple. Nous vous guiderons.",
            },
            {
                "question": "Voulez-vous en savoir plus sur les cours proposés ?",
                "answer": "Nous avons une variété de cours dans chaque programme.",
            }
        ]
    },
    {
        "question": "Quels sont les frais de scolarité ?",
        "answer": "Les frais de scolarité dépendent du programme choisi. Veuillez contacter le service administratif pour plus de détails.",
        "follow_up": [
            {
                "question": "Souhaitez-vous savoir comment financer vos études ?",
                "answer": "Nous proposons des options de financement et des bourses.",
            },
            {
                "question": "Avez-vous des questions sur les bourses disponibles ?",
                "answer": "Oui, nous avons plusieurs bourses basées sur le mérite.",
            },
            {
                "question": "Voulez-vous des informations sur les paiements échelonnés ?",
                "answer": "Oui, vous pouvez choisir un plan de paiement échelonné.",
            }
        ]
    },
    {
        "question": "Comment s'inscrire ?",
        "answer": "Pour vous inscrire, remplissez le formulaire en ligne sur notre site web ou contactez directement notre service des admissions.",
        "follow_up": [
            {
                "question": "Avez-vous déjà visité notre site web ?",
                "answer": "Si non, je vous recommande de le faire pour plus d'informations.",
            },
            {
                "question": "Souhaitez-vous des informations sur les délais d'inscription ?",
                "answer": "Les délais d'inscription sont disponibles sur notre site.",
            },
            {
                "question": "Avez-vous des questions sur le processus de sélection ?",
                "answer": "Nous avons un processus de sélection rigoureux basé sur votre dossier.",
            }
        ]
    },
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faq', methods=['GET'])
def get_faq():
    return jsonify(faq)

if __name__ == "__main__":
    app.run(debug=True)
