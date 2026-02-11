def main():
    COST = 100
    accept_coins = [5, 20, 50, 25]
    print("Amount Due: 100")

    while True:
        inserted_coin = int(input("Insert a coin: "))

        if inserted_coin in accept_coins:
            COST -= inserted_coin

        if COST < 0:
            print(f"Change Owed: {-COST}")
            break
        elif COST == 0:
            print("Change Owed: 0")
            break
        else:
            print(f"Amount Due: {COST}")

if __name__ == "__main__":
    main()