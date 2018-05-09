from odoo.addons.website_portal.controllers import main

class website_account_mandatory_mod(main.website_account):

	MANDATORY_BILLING_FIELDS = ["name", "email", "street", "city", "country_id", "vat", "company_name"]
	OPTIONAL_BILLING_FIELDS = ["phone", "zipcode", "state_id"]


	_items_per_page = 20

