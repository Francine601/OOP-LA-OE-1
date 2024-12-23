class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_phone_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")

    def modify_phone_info(self, brand=None, model=None, price=None):
        if brand:
            self.brand = brand
        if model:
            self.model = model
        if price:
            self.price = price

    def delete_phone_attribute(self, attribute):
        if attribute == 'brand':
            self.brand = None
            print("Brand has been deleted.")
        elif attribute == 'model':
            self.model = None
            print("Model has been deleted.")
        elif attribute == 'price':
            self.price = None
            print("Price has been deleted.")
        else:
            print(f"{attribute} not found.")

phone_list = []

def main_menu():
    while True:
        print("\nPhone Manager Menu:")
        print("1. Add Phone")
        print("2. Modify Phone")
        print("3. Delete Phone Attribute")
        print("4. Delete Phone")
        print("5. View All Phones")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            brand = input("Enter phone brand: ")
            model = input("Enter phone model: ")
            price = input("Enter phone price: ")
            phone = Phone(brand, model, price)
            phone_list.append(phone)
            print("Phone added successfully.")
        
        elif choice == "2":
            if not phone_list:
                print("No phones to modify.")
                continue
            index = int(input(f"Enter phone index (0 to {len(phone_list)-1}): "))
            if 0 <= index < len(phone_list):
                brand = input("Enter new brand (leave blank to skip): ")
                model = input("Enter new model (leave blank to skip): ")
                price = input("Enter new price (leave blank to skip): ")
                phone_list[index].modify_phone_info(brand, model, price)
                print("Phone modified successfully.")
            else:
                print("Invalid index.")
        
        elif choice == "3":
            if not phone_list:
                print("No phones to modify.")
                continue
            index = int(input(f"Enter phone index (0 to {len(phone_list)-1}): "))
            if 0 <= index < len(phone_list):
                attribute = input("Enter attribute to delete (brand/model/price): ")
                phone_list[index].delete_phone_attribute(attribute)
            else:
                print("Invalid index.")
        
        elif choice == "4":
            if not phone_list:
                print("No phones to delete.")
                continue
            index = int(input(f"Enter phone index (0 to {len(phone_list)-1}): "))
            if 0 <= index < len(phone_list):
                del phone_list[index]
                print("Phone deleted successfully.")
            else:
                print("Invalid index.")
        
        elif choice == "5":
            if not phone_list:
                print("No phones to display.")
                continue
            for i, phone in range(phone_list):
                print(f"\nPhone {i}:")
                phone.display_phone_info()

        elif choice == "6":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
    