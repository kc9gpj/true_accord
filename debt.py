import requests


def get_debts():
    response = requests.get('https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/debts')
    return response.json()

def get_payment_plans():
    response = requests.get('https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/payment_plans')
    return response.json()

def get_payments():
    response = requests.get('https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/payments')
    return response.json()

def get_payment_plan(payment_plans, debt_id):
    for plans in payment_plans:
        if debt_id == plans['debt_id']:
            return plans['id'], plans['amount_to_pay']
    return None

def remaining_amount(payment_plan_id, amount_to_pay, payments, debt_id):
    for payment in payments:
        if payment['payment_plan_id'] == payment['payment_plan_id']:     
            amount_to_pay = amount_to_pay - payment['amount']
        return amount_to_pay

def create_json():
    output_json = []
    debts = get_debts()
    payment_plans = get_payment_plans()
    payments = get_payments()

    for debt in debts:
        debt_dict = {}
        debt_dict['debt_id'] = debt['id']
        debt_dict['debt_amount'] = debt['amount']

        # get payment plan
        payment_plan = get_payment_plan(payment_plans, debt['id'])

        # get remaining amount
        if payment_plan:
            debt_dict['is_in_payment_plan'] = True
            debt_dict['remaining_amount'] = remaining_amount(payment_plan[0], payment_plan[1],  \
                 payments, debt['id'])
        else:
            debt_dict['is_in_payment_plan'] = False
            debt_dict['remaining_amount'] = debt['amount']
        
        print(debt_dict)



create_json()


# to do:
# - remaining_amount field
# - next_payment_due_date
