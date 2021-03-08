from datetime import datetime, timedelta
import requests
import sys


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
            next_date = get_next_due_date(plans['start_date'], plans['installment_frequency'])
            return plans['id'], plans['amount_to_pay'], next_date
    return None


def remaining_amount(payment_plan_id, amount_to_pay, payments):
    for payment in payments:
        if payment['payment_plan_id'] == payment_plan_id:
            amount_to_pay = amount_to_pay - payment['amount']
    return round(amount_to_pay, 2)


def get_next_due_date(start, frequency):
    weekday = datetime.strptime(start, '%Y-%m-%d')
    now = datetime.utcnow()
    days_ahead = weekday.weekday() - now.weekday()
    if days_ahead <= 0:
        if frequency == 'WEEKLY':
            days_ahead += 7
        else:
            days_ahead += 14
    due_date = datetime.now() + timedelta(days=days_ahead)
    return due_date.date().isoformat()


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

        # get remaining amount and due date
        if payment_plan:
            debt_dict['is_in_payment_plan'] = True
            debt_dict['remaining_amount'] = remaining_amount(payment_plan[0], payment_plan[1], payments)
            if debt_dict['remaining_amount'] > 0:
                debt_dict['next_payment_due_date'] = payment_plan[2]
            else:
                debt_dict['next_payment_due_date'] = None
        else:
            debt_dict['is_in_payment_plan'] = False
            debt_dict['remaining_amount'] = debt['amount']
            debt_dict['next_payment_due_date'] = None

        output_json.append(debt_dict)
    return output_json


def output_json():
    json = create_json()
    for json_line in json:
        sys.stderr.write("{} \n".format(json_line))


output_json()
