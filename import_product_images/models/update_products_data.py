# encoding: utf-8
# Created by Oscar Gonzalez at 10/08/18
# Created to expenses
from odoo import api, fields, models


class UpdateProductsData(models.Model):
    _name = 's4g.products_data'

    name = fields.Char(
        string="Nombre",
        required=True,
    )

    codigo = fields.Char(
        string="Código"
    )

    clave = fields.Char(
        string="Clave"
    )

    precio = fields.Float(
        string="Precio"
    )

    codigo_sat = fields.Char(
        string="Código SAT"
    )