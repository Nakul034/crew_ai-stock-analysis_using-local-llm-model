from flask import Flask, render_template, request
from main import FinancialCrew

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        company = request.form['company']
        

        # Here you can call the FinancialCrew class with the gathered data
        financial_crew = FinancialCrew(company)
        result = financial_crew.run()

        return render_template('result.html', result=result)

    return render_template('index1.html')

if __name__ == "__main__":
    app.run(debug=True)
