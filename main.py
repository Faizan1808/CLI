def main():

    try:
        # Cart List
        Mycart = []
        infile = open("MyCart.txt", "r")
        line = infile.readline()
        while line:
            Mycart.append(line.rstrip("\n").split(","))
            line = infile.readline()

        infile.close()
    except FileNotFoundError:
        print("the <MyCart.txt> file is not found")

        print("New Product List!")
        Mycart = []

    choice = 0
    while choice != 5:

        print("Add Products To Cart")
        print("1) Add Product")
        print("2) Lookup a Product")
        print("3) Display Products")
        print("4) Delete product")
        print("5) Quit")

        choice = int(input())

        if choice == 1:
            print("Adding a Product")
            nItem = input("Enter the name of the product: ")
            nprice = input("Enter the price: ")
            ndetails = input("Enter product details: ")

            Mycart.append([nItem, nprice, ndetails])

        elif choice == 2:
            print("Looking up for a Product...")
            keyword = input("Enter Search Product: ")
            for cart in Mycart:
                if keyword in cart:
                    print(cart)

        elif choice == 3:
            print("Displaying all Product...")
            for i in range(len(Mycart)):
                print(Mycart[i])

        elif choice == 4:
            print("Deleting the product...")
            nItem = input("Enter the name of the product: ")
            nprice = input("Enter the price: ")
            ndetails = input("Enter product details: ")

            Mycart.remove([nItem, nprice, ndetails])

        elif choice == 5:
            print("Quitting Program....!")
    print("Program Terminatted!")

    # saving to external txt file
    outfile = open("MyCart.txt", "w")
    for cart in Mycart:
        outfile.write(",".join(cart) + "\n")
    outfile.close()


if __name__ == "__main__":
    main()
