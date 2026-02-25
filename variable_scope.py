#L --> E --> G --> B 


print(__file__)

delivery_partner = "Big Basket" #G

def hotel():
    dish = "idly" #E
    cost =  20 #E

    def checkout():
        quantity = 5 #L
        print(f"the order is {dish}")
        print(f"price {cost}")
        print(f"total quantity {quantity}")
        print(f"total price{quantity*cost}, {delivery_partner}")
    
    checkout()

hotel()