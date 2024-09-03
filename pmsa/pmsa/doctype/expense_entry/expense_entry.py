import frappe
from frappe.model.document import Document

class ExpenseEntry(Document):
    def on_submit(self):
        self.make_gl_entry()

    def make_gl_entry(self):
        gl_entry = frappe.new_doc("GL Entry")
        gl_entry.posting_date = self.expense_date
        gl_entry.account = self.account
        gl_entry.debit = self.amount
        gl_entry.credit = 0
        gl_entry.voucher_type = "Expense Entry"
        gl_entry.voucher_no = self.name
        gl_entry.insert()
        gl_entry.submit()
