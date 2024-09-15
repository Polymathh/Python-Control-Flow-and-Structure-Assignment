#first teaser
def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = price * discount_percent / 100
        final_amount = price - discount_amount  
    else:
        final_amount = price   

    return final_amount
    

    #second teaser
    price = 3000
    discount_percent = 30 

def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = price * discount_percent / 100
        final_amount = price - discount_amount  
    else:
        final_amount = price   

    return final_amount

price = float(input("Enter the price: "))  
discount_percent = float(input("Enter the discount percentage: "))  


final_amount = calculate_discount(price, discount_percent)
   
print(f"Your final amount is:", final_amount)

