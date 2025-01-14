import tkinter as tk # The GUI application is created by importing the tkinter library.
from tkinter import messagebox # To show pop-up messages, import the messagebox module from tkinter.

class VendingMachine: # Constructor method to initialize the VendingMachine class
    def __init__(self): # Set the VendingMachine class properties to their initial values.
        # Initialize product data. Dictionaries method has been used in this
        self.products = {
            "Snacks": {
                "S111": {"name": "Sandwich - Meat Sandwich", "Rate": 7.00, "Stock": 5},
                "S222": {"name": "Chips - Original Lays Chips", "Rate": 2, "Stock": 7},
                "S333": {"name": "Chips - French Cheese Chips", "Rate": 4, "Stock": 0},  # Out of Stock
                "S444": {"name": "Seafood Sandwich", "Rate": 5.50, "Stock": 6},
                "S555": {"name": "Chicken Sandwich", "Rate": 4.99, "Stock": 2},
                "S666": {"name": "Cheese Sandwich", "Rate": 3, "Stock": 8},
                "S777": {"name": "Salmon Sandwich", "Rate": 8, "Stock": 4},
            },
            "Drinks": {
                "D111": {"name": "Hot Chocolate", "Rate": 4, "Stock": 7},
                "D222": {"name": "Green Tea", "Rate": 3.25, "Stock": 9},
                "D333": {"name": "Iced Tea", "Rate": 4.50, "Stock": 4},
                "D444": {"name": "Pepsi", "Rate": 5.00, "Stock": 2},
                "D555": {"name": "Mountain Dew", "Rate": 3.00, "Stock": 8},
                "D666": {"name": "Fanta", "Rate": 2.50, "Stock": 3},
                "D777": {"name": "Marinda", "Rate": 3.50, "Stock": 5},
            },
            "Biscuits": {
                "BB11": {"name": "Biscuits - Chocolate Chip", "Rate": 2, "Stock": 6},
                "BB22": {"name": "Biscuits - Oatmeal Raisin", "Rate": 2.50, "Stock": 8},
                "BB33": {"name": "Aparon", "Rate": 4.00, "Stock": 9},
                "BB44": {"name": "Apas", "Rate": 3.75, "Stock": 4},
                "BB55": {"name": "Broas", "Rate": 5.00, "Stock": 7}, 
            }
        }
        self.total_inserted = 0.0  # Total money inserted by the user
        self.root = tk.Tk() # Creating the main window of the application 
        self.root.title("🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🅼🆄🅷🆁🅴🅴🅼❜🆂 🆅🅴🅽🅳🅸🅽🅶 🅼🅰🅲🅷🅸🅽🅴") # Setting the title of the GUI application 
        self.root.configure(bg="#f0f8ff")  # Set background color
        self.create_gui() # this is used for Calling the method to create the GUI components. 

    def create_gui(self): #by the help of this code this will create the GUI components.
        # Main title label
        tk.Label(self.root, text="🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🅼🆄🅷🆁🅴🅴🅼❜🆂 🆅🅴🅽🅳🅸🅽🅶 🅼🅰🅲🅷🅸🅽🅴", font=("Arial", 16), bg="#f0f8ff").pack(pady=10)

        # Buttons for categories
        button_frame = tk.Frame(self.root, bg="#f0f8ff")
        button_frame.pack(pady=20) # this code is use to Add some space between the buttons and the main title heading.
        # these are the buttons for the products available 
        tk.Button(button_frame, text="Snacks", font=("Arial", 14), command=self.show_snacks_menu).grid(row=0, column=0, padx=20)
        tk.Button(button_frame, text="Drinks", font=("Arial", 14), command=self.show_drinks_menu).grid(row=0, column=1, padx=20)
        tk.Button(button_frame, text="Biscuits", font=("Arial", 14), command=self.show_biscuits_menu).grid(row=0, column=2, padx=20)

        # Input fields for product code and money and bg colour 
        self.input_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.input_frame.pack(pady=10)
        # Product code label and entry
        tk.Label(self.input_frame, text="Enter product code:", bg="#f0f8ff").grid(row=0, column=0)
        self.code_entry = tk.Entry(self.input_frame)
        self.code_entry.grid(row=0, column=1) # Entry field for product code

        tk.Label(self.input_frame, text="Insert money (AED):", bg="#f0f8ff").grid(row=1, column=0) # Label for money input
        self.money_entry = tk.Entry(self.input_frame)
        self.money_entry.grid(row=1, column=1) # Entry field for money by the help of this code the user can enter the money.

        tk.Button(self.input_frame, text="Purchase", command=self.purchase).grid(row=2, column=0, columnspan=2, pady=10) # Button of the purchasing the product 

        # Label for suggestions
        self.suggestion_label = tk.Label(self.root, text="", font=("Arial", 12), bg="#f0f8ff")
        self.suggestion_label.pack(pady=5)

    def show_snacks_menu(self):
        self.show_category_menu("Snacks", self.products["Snacks"])

    def show_drinks_menu(self):
        self.show_category_menu("Drinks", self.products["Drinks"])

    def show_biscuits_menu(self):
        self.show_category_menu("Biscuits", self.products["Biscuits"])

    def show_category_menu(self, category_name, items):
        # Display items in the selected category
        category_window = tk.Toplevel(self.root)
        category_window.title(f"{category_name} Menu")
        category_window.configure(bg="#f0f8ff")

        for code, product in items.items():
            label = f"{code}: {product['name']} - AED {product['Rate']} (Remaining: {product['Stock']})"
            tk.Label(category_window, text=label, bg="#f0f8ff").pack(anchor="w") # by the help of this code this will Display the product details in the window

    def purchase(self):
        # Process purchase based on the entered product code and money
        code = self.code_entry.get().upper()
        try:
            money = float(self.money_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount of money.") #by the help of this code this will show the error message if the correct value is not entered.
            return

        # Search for the product in all categories
        for category, items in self.products.items():
            if code in items:
                product = items[code]
                break
        else:
            messagebox.showerror("Error", "Invalid product code.") #by the help of this code this will Display error message if product code is not found
            return

        # Check stock availability
        if product['Stock'] == 0:
            messagebox.showinfo("Out of Stock", f"Sorry, {product['name']} is out of stock.") #by the help of this code the user will know if the product is out of stock
            return

        # Check if the money is sufficient
        if money < product['Rate']:
            messagebox.showinfo("Insufficient Funds", f"Insufficient funds. {product['name']} costs AED {product['Rate']}.")
            return

        # Process the purchase
        change = money - product['Rate']
        product['Stock'] -= 1
        self.total_inserted += product['Rate']
        # this will show the receipt of the product bought. 
        receipt = (
            f"Receipt:\n"
            f"Product: {product['name']}\n"
            f"Cost: AED {product['Rate']}\n"
            f"Change: AED {change:.2f}\n\n"
            f"{product['name']} has been dispensed.\n\n"
            f"Thank you for your purchase! Come again!"
        )

        # Display the receipt
        messagebox.showinfo("Purchase Successful", receipt)

        #by the help of this code this will Offer additional items based on category
        if product in self.products["Snacks"].values():
            self.offer_additional_item("Drinks", "Would you like to add a drink?")
        elif product in self.products["Drinks"].values():
            self.offer_additional_item("Biscuits", "Would you like to add a biscuit?")
        elif product in self.products["Biscuits"].values():
            self.offer_additional_item("Drinks", "Would you like to add a drink?")

    def offer_additional_item(self, category_name, message):
        # Ask the user if they want to add an additional item
        additional_items = [f"{code}: {item['name']} (AED {item['Rate']})" for code, item in self.products[category_name].items() if item['Stock'] > 0]

        if additional_items:
            response = messagebox.askyesno("Additional Item", message)
            if response:
                # Display available items in the selected category
                suggestion_window = tk.Toplevel(self.root)
                suggestion_window.title(f"{category_name} Suggestions")
                suggestion_window.configure(bg="#f0f8ff")

                tk.Label(suggestion_window, text=f"Available {category_name}:", font=("Arial", 14), bg="#f0f8ff").pack(pady=10)
                for item in additional_items:
                    tk.Label(suggestion_window, text=item, bg="#f0f8ff").pack(anchor="w") #this will show the available items in the selected category

if __name__ == "__main__": # this is the main function of the code
    VendingMachine().root.mainloop() # this will start the GUI of the vending machine

