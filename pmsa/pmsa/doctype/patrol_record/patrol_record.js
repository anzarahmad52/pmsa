frappe.ui.form.on('Patrol Record', {
    refresh: function(frm) {
        // Example: Auto-fetch route checkpoints when route is selected
        frm.add_fetch('route', 'checkpoints', 'checkpoints');
    },
    route: function(frm) {
        if (frm.doc.route) {
            frappe.call({
                method: "frappe.client.get",
                args: {
                    doctype: "Patrol Route",
                    name: frm.doc.route
                },
                callback: function(r) {
                    if (r.message) {
                        frm.set_value("checkpoints", r.message.checkpoints);
                    }
                }
            });
        }
    }
});
