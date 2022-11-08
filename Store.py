store={
    "Apples":[40,15],
    "Banana":[30,10],
    "Cherry":[70,5]
    }



while True:
    MODE=input("Please enter 1.Owner, 2.Customer \n")
    bill =0
    while MODE=='2':
        choice=input("1.To Show menu, 2.Buy Products, 3.Pay the Bill \n")
        if choice=='1':
            for keys, value in store.items():
                print(keys,value[1],'EGP')

        while(choice=='2'):
            fruit,number=input("Please enter Fruit and amount\n").split(" ",2)
            bill=(store[fruit][1]*int(number))+bill
            store[fruit][0]-=int(number)
            choice=input("Anything Else? 2.Buy Products, 3.Pay the Bill \n")

        if choice=='3':
            print(bill)

        MODE=input("Do you want to continue in Customer Mode 2.Yes..0.No \n")

    while MODE=='1':
        choice=input("1.Add New Products, 2.Show Products, 3.Change Cost \n")
        if choice=='1':
            new_fruit,amount,cost=input("Please enter New fruit, Ammout and Cost with spaces between \n").split(" ",3)
            store.update({new_fruit:[int(amount),int(cost)]})
        if choice=='2':
            print(store)
        if choice=='3':
            fruit,new_cost=input("Please choose which product and its new Price \n").split(" ",2)
            store[fruit][1]=int(new_cost)

        MODE=input("Do you want to continue in Owner Mode 1.Yes..0.No \n")