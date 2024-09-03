import frappe
from frappe.model.document import Document

class Checkpoint(Document):
    pass

def create_default_checkpoints():
    default_checkpoints = [
        {"checkpoint_name": "Checkpoint 1", "location": "Location 1"},
        {"checkpoint_name": "Checkpoint 2", "location": "Location 2"},
        {"checkpoint_name": "Checkpoint 3", "location": "Location 3"}
    ]
    
    for checkpoint in default_checkpoints:
        if not frappe.db.exists("Checkpoint", checkpoint["checkpoint_name"]):
            doc = frappe.get_doc({
                "doctype": "Checkpoint",
                "checkpoint_name": checkpoint["checkpoint_name"],
                "location": checkpoint["location"]
            })
            doc.insert(ignore_permissions=True)
            frappe.db.commit()
