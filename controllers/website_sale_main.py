from odoo.addons.website_sale.controllers import main


main.PPG = 8
main.PPR = 2

class website_sale_mandatory_mod(main.WebsiteSale):
	
	def _get_mandatory_billing_fields(self):
		return ["name", "email", "street", "city", "country_id", "zip", "company_name", "vat"]
		
	def _get_mandatory_shipping_fields(self):
		return ["name", "street", "city", "country_id", "zip", "company_name", "vat"]