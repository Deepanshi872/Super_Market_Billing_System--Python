products= {"Apple":30, "Chips": 20, "Mango":87, "Coke":45, "Pulses": 100, "Rice": 123, "Channa":348}

while True:
    cart = {}
    amount= 0
    Name= input("Enter your name:")
    Phone_number= input("Enter phone number:")

    while True:
        Quantity= float(input("Enter quantity here:"))
        while True:
            Product_name= input("Enter product name:").title()
            if Product_name not in products.keys():
                print("enter correct spelling")
            else:
                break
        amount += products[Product_name]*Quantity
        cart[Product_name] = products[Product_name], "x", Quantity
        repeat_item= input("Do you want to add more item:").lower()
        if repeat_item=="no":
            break
    discount= 0
    if amount <=500:
        discount= 0.05
        act_amount= amount-amount*discount

    elif amount <=1000:
        discount= 0.07
        act_amount= amount-amount*discount

    elif amount <=5000:
        discount= 0.15
        act_amount= amount-amount*discount

    else:
        discount= 0.20
        act_amount= amount-amount*discount

    print("-"*30)
    print("Customer Name:", Name)
    print("Customer Phone number:", Phone_number)
    for i,j in cart.items():
        p,x,q = j
        print(i, ":", p,x,q)
    print("Total bill:", amount)
    print("Discount applied:", discount*100, "%off")
    print("Final amount:", act_amount)
    print("-"*30)

    next_person= input("Is their new person in line?").lower()
    if next_person=="no":
        break


