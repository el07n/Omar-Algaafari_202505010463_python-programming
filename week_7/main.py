from food_order import calculate_total


def main():
    try:
        price = float(input("Price (RM): "))
        quantity = int(input("Quantity: "))

        total = calculate_total(price, quantity)

        if total == "invalid price":
            print("invalid price")
        elif total == "invalid quantity":
            print("invalid quantity")
        else:
            print(f"Total Payment = RM {total:.2f}")

    except ValueError:
        print("invalid input")


if __name__ == "__main__":
    main()