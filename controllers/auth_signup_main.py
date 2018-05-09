import logging
import werkzeug

from odoo import http, _
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.addons.web.controllers.main import ensure_db, Home
from odoo.http import request
from odoo import tools
from odoo.tools.translate import _

from odoo.fields import Date

_logger = logging.getLogger(__name__)

from odoo.addons.auth_signup.controllers import main

class signup_mod(main.AuthSignupHome):

	def do_signup(self, qcontext):
		""" Shared helper that creates a res.partner out of a token """
		values = { key: qcontext.get(key) for key in ('login', 'name', 'password','company_name') }
		values.update({'zip': values.pop('zipcode', '')})
		assert values.values(), "The form was not properly filled in."
		assert values.get('password') == qcontext.get('confirm_password'), "Passwords do not match; please retype them."
		supported_langs = [lang['code'] for lang in request.env['res.lang'].sudo().search_read([], ['code'])]
		if request.lang in supported_langs:
			values['lang'] = request.lang
		self._signup_with_values(qcontext.get('token'), values)
		request.env.cr.commit()



