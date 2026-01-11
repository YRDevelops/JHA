from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def analyze_and_suggest(monthly_expense, yearly_income):

    yearly_expense = monthly_expense * 12
    yearly_savings = yearly_income - yearly_expense

    if yearly_savings < yearly_income * 0.2:
        expense_suggestion = "Your expenses are high. Try to save at least 20%."
    else:
        expense_suggestion = "Good saving habit! Keep it up."

    investment_amount = yearly_income * 0.15

    if investment_amount > 500000:
        investment_advice = "Invest in Mutual Funds + Index Funds."
    else:
        investment_advice = "Invest in PPF and ELSS."

    return {
        "yearly_expense": f"₹{yearly_expense:,.2f}",
        "yearly_savings_potential": f"₹{yearly_savings:,.2f}",
        "expense_suggestion": expense_suggestion,
        "investment_advice": investment_advice,
    }

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json

    result = analyze_and_suggest(
        float(data['monthlyExpense']),
        float(data['yearlyIncome'])
    )

    return jsonify(result)

if __name__ == "__main__":
    app.run()
