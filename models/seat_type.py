from odoo import fields,models


class SeatTypes(models.Model):
    _name = "seat.types"
    _description = "Types of Seats(Business,Economy etc),Price,Availability Status"

    price = fields.Integer()
    ticket = fields.Selection(String="Ticket Types",selection=[('1','Business Class','2','Economy Class')])
    available_tickets = fields.Integer()