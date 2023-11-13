from typing import Union

from fastapi import FastAPI

app = FastAPI()

account_balance = 1000  # Başlangıç bakiyesi

@app.get("/balance")
def get_balance():
    return {"balance": account_balance}

@app.post("/deposit/{amount}")
def deposit(amount: float):
    global account_balance
    account_balance += amount
    return {"message": f"Deposit successful. New balance: {account_balance}"}

@app.post("/withdraw/{amount}")
def withdraw(amount: float):
    global account_balance
    if amount > account_balance:
        return {"error": "Insufficient funds"}
    else:
        account_balance -= amount
        return {"message": f"Withdrawal successful. New balance: {account_balance}"}