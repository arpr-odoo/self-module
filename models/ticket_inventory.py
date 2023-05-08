from odoo import fields,models,api


class TicketInventory(models.Model):
    _name = 'ticket.inventory'
    _description = 'Ticket Inventory'

    name = fields.Many2one('seat.types', required=True, ondelete='cascade')
    flight_id = fields.Many2one('flight.db', required=True, ondelete='cascade')
    price = fields.Float(required=True)
    quantity = fields.Integer(required=True, default=0)

    # TODO: Updating Number of tickets when it gets confirmed

