# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "selling_fulfillment"
app_title = "Erpnext Selling Order Fulfillment Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Selling Order Fulfillment Engine for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/selling_fulfillment/css/selling_fulfillment.bundle.css"
app_include_js = "/assets/selling_fulfillment/js/selling_fulfillment.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "selling_fulfillment.engine.on_document_submit",
        "on_cancel": "selling_fulfillment.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "selling_fulfillment.engine.daily_scheduled_sync"
    ]
}
