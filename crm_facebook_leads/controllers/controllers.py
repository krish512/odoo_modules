# -*- coding: utf-8 -*-
# from odoo import http


# class CrmFacebookLeads(http.Controller):
#     @http.route('/crm_facebook_leads/crm_facebook_leads', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_facebook_leads/crm_facebook_leads/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_facebook_leads.listing', {
#             'root': '/crm_facebook_leads/crm_facebook_leads',
#             'objects': http.request.env['crm_facebook_leads.crm_facebook_leads'].search([]),
#         })

#     @http.route('/crm_facebook_leads/crm_facebook_leads/objects/<model("crm_facebook_leads.crm_facebook_leads"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_facebook_leads.object', {
#             'object': obj
#         })

