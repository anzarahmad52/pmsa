import frappe
from frappe.model.document import Document

class PatrolRecord(Document):
    def on_submit(self):
        self.create_stock_entry()

    def create_stock_entry(self):
        stock_entry = frappe.new_doc("Stock Entry")
        stock_entry.purpose = "Material Transfer"
        stock_entry.from_warehouse = "Tanker - PMSA"
        stock_entry.to_warehouse = "Pump Storage - PMSA"
        stock_entry.append("items", {
            "item_code": "Patrol",
            "qty": 100,  # Replace with actual quantity from the patrol record
            "uom": "Liters"
        })
        stock_entry.insert()
        stock_entry.submit()
        self.stock_entry = stock_entry.name
        frappe.msgprint(f"Stock Entry {stock_entry.name} created and linked with Patrol Record {self.name}.")
        self.save()
def create_sales_order(self):
    sales_order = frappe.new_doc("Sales Order")
    sales_order.customer = "Customer Name"  # Replace with actual customer
    sales_order.append("items", {
        "item_code": "Patrol",
        "qty": 100,  # Replace with actual quantity from the patrol record
        "rate": 100,  # Replace with the selling rate
        "warehouse": "Pump Storage - PMSA"
    })
    sales_order.insert()
    sales_order.submit()
    self.sales_order = sales_order.name
    frappe.msgprint(f"Sales Order {sales_order.name} created and linked with Patrol Record {self.name}.")
    self.save()