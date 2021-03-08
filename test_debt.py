import unittest

from debt import remaining_amount, get_next_due_date, get_payment_plan


class TestDebt(unittest.TestCase):
    def test_amount(self):
        payments = [
            {
                "amount": 1,
                "date": "2020-09-29",
                "payment_plan_id": 0
            },
            {
                "amount": 1,
                "date": "2020-10-29",
                "payment_plan_id": 0
            },
            {
                "amount": 1,
                "date": "2020-10-29",
                "payment_plan_id": 2
            },
            {
                "amount": 50,
                "date": "2020-10-29",
                "payment_plan_id": 1
            }]
        amount = remaining_amount(0, 10, payments)
        self.assertEqual(amount, 8)
        amount = remaining_amount(1, 200, payments)
        self.assertEqual(amount, 150)

    def test_due_date(self):
        due_date = get_next_due_date("2020-09-28", "WEEKLY")
        self.assertEqual(due_date, '2021-03-08')
        due_date = get_next_due_date("2020-09-28", "BI-WEEKLY")
        self.assertEqual(due_date, '2021-03-15')

    def test_payment_plan(self):
        payment_plans = [{
            "amount_to_pay": 12345,
            "debt_id": 0,
            "id": 0,
            "installment_amount": 51.25,
            "installment_frequency": "WEEKLY",
            "start_date": "2000-01-02"
            },
            {
            "amount_to_pay": 12,
            "debt_id": 1,
            "id": 1,
            "installment_amount": 2,
            "installment_frequency": "BI-WEEKLY",
            "start_date": "2020-01-02"
            }]
        plans = get_payment_plan(payment_plans, 0)
        self.assertEqual(plans[0], 0)
        self.assertEqual(plans[1], 12345)
        self.assertEqual(plans[2], '2021-03-14')
        plans = get_payment_plan(payment_plans, 1)
        self.assertEqual(plans[0], 1)
        self.assertEqual(plans[1], 12)
        self.assertEqual(plans[2], '2021-03-18')
