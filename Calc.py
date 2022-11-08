while 1:
    MODE=input("Please enter 1.Programmable, 2.Scientific\n")

    while MODE=='2':
        num1,operation,num2=input("Please enter the operation [num +,-,/,* num]\n").split(" ",3)

        if operation=='+':
            result=int(num1)+int(num2)

        elif operation=='-':
            result=int(num1)-int(num2)

        elif operation =='/':
            result=float(num1)/float(num2)

        elif operation =='*':
            result=int(num1)*int(num2)

        print(result)
        MODE=input("Continue in Scientific Mode? 2.Yes, 0.No\n")

    while MODE=='1':
        choice=input("1.To Convert Number,2.shift operation, 3.bitwise Operation\n")
        if choice=='1':
           input_type=input("Please enter the input number type, 0.Decimal...1.Binary...2.Octal...3.Hexadecimal\n");   
           if input_type=='0':
               number=input("Please enter number in Decimal form\n")
               number=int(number)
               print(bin(number))
               print(oct(number))
               print(hex(number))

           if input_type=='1':
               number=input("Please enter number in binary Form\n")
               decimal_integer=int(number,2)
               print(decimal_integer)
               print(oct(decimal_integer))
               print(hex(decimal_integer))

           if input_type=='2':
               number=input("Please enter number in octal Form\n")
               decimal_integer=int(number,8)
               print(decimal_integer)
               print(bin(decimal_integer))
               print(hex(decimal_integer))

           if input_type=='3':
               number=input("Please enter number in Hexadecimal Form\n")
               decimal_integer=int(number,16)
               print(decimal_integer)
               print(bin(decimal_integer))
               print(oct(decimal_integer))
        if choice=='2':
           choice,shifts=input("Please enter the operation 0.ShiftRight , 1.ShiftLeft and number of shifts\n").split(" ",2)
           if choice=='0':
               number=input("Enter number in binary Mode\n")
               number=int(number,2)
               number=number>>int(shifts)
               print(bin(number))
           if choice=='1':
               number=input("Enter number in binary Mode\n")
               number=int(number,2)
               number=number<<int(shifts)
               print(bin(number))
        if choice=='3':
            num1,operation,num2=input("Please enter num1-[|,&,^]-num2 with spaces in binary\n").split(" ",3)
            if operation =='|':
                print(int(num1)|int(num2))
            if operation=='&':
                print(int(num1)&int(num2))
            if operation=='^':
                print(int(num1)^int(num2))
        MODE=input("Continue in Programmable Mode? 1.Yes 0.No\n")
