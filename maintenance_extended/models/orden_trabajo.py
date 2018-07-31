"""
* Created by gonzalezoscar on 31/07/18
* expenses
"""

# -*- coding: utf-8 -*-
from odoo import api, fields, models


class OrdenTrabajo(models.Model):
    _name = 'ops4g.orden_trabajo'

    name = fields.Char(
        string=""
    )

    descripcion = fields.Char(
        string="Descripción",
        required=True,
    )

    responsable = fields.Many2one(
        'res.users',
        string="Responsable",
        required=True,
    )

    responsable_supervision = fields.Many2one(
        'res.users',
        string="Responsable de supervisión",
    )

    costo_horas_hombre = fields.Float(
        string="Costo horas hombre",
        compute="get_costo_horashombre",
    )

    costo_recursos = fields.Float(
        string="Costo recursos",
    )

    costo_total = fields.Float(
        string="Costo total"
    )

    tareas_ids = fields.One2many(
        'ops4g.tareas',
        'orden_trabajo_id',
        string="Tareas",
    )

    @api.one
    @api.depends('tareas_ids')
    def get_costo_horashombre(self):
        for record in self:
            if len(record.tareas_ids) > 0:
                costo_horas_hombre = 0
                print("\n ***************Iniciando")
                for tarea in record.tareas_ids:
                    costo_horas_hombre += tarea.importe
                record.costo_horas_hombre = costo_horas_hombre