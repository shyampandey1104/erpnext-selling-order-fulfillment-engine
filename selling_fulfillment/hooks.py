# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "selling_fulfillment"
app_title = "Erpnext Selling Order Fulfillment Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Selling Order Fulfillment Engine - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/selling_fulfillment/css/selling_fulfillment.bundle.css"
app_include_js = "/assets/selling_fulfillment/js/selling_fulfillment.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Selling Order Fulfillment Engine Entry": {
        "validate": "selling_fulfillment.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "selling_fulfillment.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "selling_fulfillment.tasks.hourly_sync"
    ],
    "daily": [
        "selling_fulfillment.tasks.daily_reconciliation"
    ],
    "weekly": [
        "selling_fulfillment.tasks.weekly_digest"
    ]
}
