from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

questions = [
    "1. Is there a need to remove supply chain (SC) intermediaries from transaction?",
    "2. Are parties working with digital assets, notarized/tokenized assets?",
    "3. Is there a need to create a permanent authoritative record of digital assets or data?",
    "4. Are there multiple parties?",
    "5. Are all parties known?",
    "6. Is there a need for a trusted third-party or for parties to trust each other?",
    "7. Is an audit trail of activity (transactions & users) important?",
    "8. Are there contractual relationships or value exchange to be managed?",
    "9. Are the parties' interests well-aligned?",
    "10. Are there conditions under which transaction needs to be automatically executed (e.g., based on milestone achieved)?",
    "11. Is there a need for a self-executing contract?",
    "12. Is there a need for a decentralized network?",
    "13. Is there a need to be able to control functionality?",
    "14. Should transaction be public?"
]

@app.route('/', methods=['GET'])
def home():
    session['current_question_index'] = 0 
    return render_template('home.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    global current_question_index
    
    if request.method == 'POST':
        answer = request.form.get('answer')

        if current_question_index < 4:
            if answer == 'yes':
                current_question_index += 1
                return render_template('index.html', question=questions[current_question_index])
            elif answer == 'no':
                return render_template('end.html')

        elif 4 <= current_question_index <= 5:
            if answer == 'no':
                current_question_index += 1
                return render_template('index.html', question=questions[current_question_index])
            elif answer == 'yes':
                return render_template('end.html')

        elif current_question_index == 6 or current_question_index == 7:
            if answer == 'yes':
                current_question_index += 1
                return render_template('index.html', question=questions[current_question_index])
            elif answer == 'no':
                return render_template('end.html')
              
        elif current_question_index == 8:
            if answer == 'no':
                current_question_index += 1
                return render_template('index.html', question=questions[current_question_index])
            elif answer == 'yes':
                return render_template('end.html')

        elif 9 <= current_question_index <= 11:
            if answer == 'yes':
                current_question_index += 1
                return render_template('index.html', question=questions[current_question_index])
            elif answer == 'no':
                return render_template('end.html')
              
        elif current_question_index == 12:
            if answer == 'yes':
                return render_template('solution_1.html')
            elif answer == 'no':
                current_question_index += 1
                return render_template('index.html', question=questions[current_question_index])
              
        elif current_question_index == 13:
            if answer == 'yes':
                return render_template('solution_2.html')
            elif answer == 'no':
                return render_template('solution_1.html')

    current_question_index = 0


    return render_template('index.html', question=questions[current_question_index])

if __name__ == '__main__':
    app.run(debug=True)
