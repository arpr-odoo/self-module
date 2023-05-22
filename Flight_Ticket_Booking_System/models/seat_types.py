from odoo import fields,models,api


class SeatTypes(models.Model):
    _name = "seat.types"
    _description = "Types of Seats(Business,Economy etc),Price,Availability Status"

    name = fields.Char(required=True)
    description = fields.Char()

