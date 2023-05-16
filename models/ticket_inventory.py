from odoo import fields,models,api


class TicketInventory(models.Model):
    _name = 'ticket.inventory'
    _description = 'Ticket Inventory'


    name = fields.Many2one('seat.types')
    flight_id = fields.Many2one('flight.db')
    price = fields.Float(required=True)
    quantity = fields.Integer()


    ticket_booking_id = fields.One2many("ticket.booking","ticket_inventory_id")


