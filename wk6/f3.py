"""
create a function that converts
    celcius to farenheit

create a function that converts
    farenheit to celcius

create a function that's called checkout
    item_to_purchase, cost_of_item, payment_method, amount_paid
        
        item to purchase is a string
        cost of item is a float
        payment method is a basestring
        amount paid is a float
        
        inside of the method: only accept cash, debit, visa
        ensure that amount paid is greater or equal to cost of item

"""
def celcius_to_fahrenheit(temperature: float)->float:
    return temperature * (9/5) + 32
    # return temperature * 1.8 + 32

print(celcius_to_fahrenheit(-13))

def farenheit_to_celcius(temperature: float) -> float:
    return (temperature - 32) / 1.8


def checkout(item_to_purchase: str, 
cost_of_item: float, payment_method:str, amount_paid:float)->str:
    if isinstance(item_to_purchase, str) and isinstance(cost_of_item, float) \
    and isinstance(payment_method, str) and isinstance(amount_paid, float):
        
        if payment_method.lower() in "visa,debit,cash".split(",") and amount_paid>=cost_of_item:
            return f"You have successfully paid for {item_to_purchase}. " \
            f"${amount_paid} was paid via {payment_method}"
        else:
            return "invalid payment method or insufficient funds"
        
    return "Error with request"


result = checkout(item_to_purchase="shoes", payment_method="debit", 
amount_paid=100.0, cost_of_item=100.0)
print(result)
result = checkout(item_to_purchase="shoes", payment_method="debit", 
amount_paid=10.0, cost_of_item=100.0)
print(result)



