from fpdf import FPDF

class ReceiptCalculator:
    def __init__(self):
        self.items = []
        self.tax_rate = 0.07  # 7% tax rate
        self.discount_rate = 0.10  # 10% discount rate

    def add_item(self, name, price, quantity):
        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def calculate_totals(self):
        subtotal = sum(item['price'] * item['quantity'] for item in self.items)
        tax = subtotal * self.tax_rate
        discount = subtotal * self.discount_rate
        total = subtotal + tax - discount
        return subtotal, tax, discount, total

    def generate_receipt(self):
        subtotal, tax, discount, total = self.calculate_totals()
        receipt_lines = ["RECEIPT", "="*40]
        for item in self.items:
            line = f"{item['name']:<20} {item['quantity']:>3} x ${item['price']:>6.2f} = ${item['price'] * item['quantity']:>6.2f}"
            receipt_lines.append(line)
        receipt_lines.append("=" * 40)
        receipt_lines.append(f"Subtotal: ${subtotal:>6.2f}")
        receipt_lines.append(f"Tax (7%): ${tax:>6.2f}")
        receipt_lines.append(f"Discount (10%): ${discount:>6.2f}")
        receipt_lines.append(f"Total: ${total:>6.2f}")
        return "\n".join(receipt_lines)

    def display_receipt(self):
        receipt = self.generate_receipt()
        print(receipt)

    def save_receipt_text(self, filename="receipt.txt"):
        receipt = self.generate_receipt()
        with open(filename, "w") as file:
            file.write(receipt)
        print(f"Receipt saved to {filename}")

    def save_receipt_pdf(self, filename="receipt.pdf"):
        receipt = self.generate_receipt()
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Add header
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, 'RECEIPT', ln=True, align='C')
        pdf.set_font("Arial", size=12)
        pdf.ln(10)
        
        # Add item details
        pdf.set_font("Arial", size=12)
        for line in receipt.split("\n"):
            pdf.cell(200, 10, txt=line, ln=True, align='L')
        
        # Add footer
        pdf.ln(10)
        pdf.set_font("Arial", 'I', 12)
        pdf.cell(200, 10, 'Thank you for shopping with us! Visit Again...!!!', ln=True, align='C')
        
        pdf.output(filename)
        print(f"Receipt saved to {filename}")

def main():
    calculator = ReceiptCalculator()

    while True:
        print("Enter item details:")
        name = input("Enter Item Name: ")
        price = float(input("Enter Price of Item: "))
        quantity = int(input("Enter Quantity of Item: "))

        calculator.add_item(name, price, quantity)

        more_items = input("Add another item? (yes/no): ").strip().lower()
        if more_items != 'yes':
            break

    calculator.display_receipt()
    calculator.save_receipt_text()
    calculator.save_receipt_pdf()

if __name__ == "__main__":
    main()