from war import War


if __name__ == "__main__":
    war = War(3, 1)
    war.generate()
    from storage import Storage
    print(Storage.armies)
