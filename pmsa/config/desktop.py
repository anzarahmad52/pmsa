from frappe import _

def get_data():
    return [
        {
            "module_name": "PMSA",
            "category": "Modules",
            "label": _("PMSA"),
            "color": "#1abc9c",
            "icon": "octicon octicon-file-directory",
            "type": "module",
            "description": _("Patrol Management System App"),
        }
    ]