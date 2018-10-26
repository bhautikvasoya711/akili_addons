# -*- coding: utf-8 -*-
from odoo import  fields, models


class Company(models.Model):
    _inherit = "res.company"

    enable_feature = fields.Boolean(string='Enable Feature',)
    website_description = fields.Html(string='Website term description',)
