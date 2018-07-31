# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class CreateVendors(http.Controller):

    @http.route('/page/create_suppliers_portal.create_supplier', type='http', auth='user', website=True)
    def render_create_supplier_template(self):
        create_contacts_group = http.request.env.ref('base.group_partner_manager')
        current_user = request.env.user

        create_contacts_ids = []
        for user_partners in create_contacts_group.users:
            create_contacts_ids.append(user_partners.id)

        cancreate = False
        if current_user.id in create_contacts_ids:
            cancreate = True

        return http.request.render(
            'create_suppliers_portal.create_supplier',
            {
                'cancreate': cancreate,
            }
        )

    @http.route('/website/create_vendor', type='http', auth='user', website=True)
    def create_vendor(self, **kwargs):
        name = kwargs.get('name')
        vat = kwargs.get('vat')

        data_vendor = {
            'name': name,
            'vat': vat,
            'customer': False,
            'supplier': True
        }

        http.request.env['res.partner'].sudo().create(
            data_vendor
        )

        return http.request.redirect('/')