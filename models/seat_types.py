from odoo import fields,models,api


class SeatTypes(models.Model):
    _name = "seat.types"
    _description = "Types of Seats(Business,Economy etc),Price,Availability Status"

    price = fields.Integer()
    ticket = fields.Selection(String="Ticket Types",selection=[('1','Business Class'),('2','Economy Class'),('3','First Class')])
    available_tickets = fields.Integer(default=60,compute="_compute_available_tickets")

    @api.depends("available_tickets")
    def _compute_available_tickets(self):
        for record in self:
            record.available_tickets = 60 - len(self.env['ticket.booking'].search([('ticket_type','=',record.ticket)]))