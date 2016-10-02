import sys

balance = 42
annual_interestRate = 0.2
monthly_payment_rate = 0.04

monthly_interest = annual_interestRate / 12
monthly_payment = current_balance * monthly_payment_rate
monthly_unpaid_balance = current_balance - monthly_payment
updated_balance = monthly_unpaid_balance + (monthly_interest * monthly_unpaid_balance)

