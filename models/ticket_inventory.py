from odoo import fields,models,api


class TicketInventory(models.Model):
    _name = 'ticket.inventory'
    _description = 'Ticket Inventory'


    name = fields.Many2one('seat.types', required=True)
    flight_id = fields.Many2one('flight.db', required=True)
    price = fields.Float(required=True)
    quantity = fields.Integer()

    # TODO: Updating Number of tickets when it gets confirmed

    ticket_booking_id = fields.One2many("ticket.booking","ticket_inventory_id")
    # ticket_status = fields.Selection(related="ticket_booking_id.status")

    # tickets_remain = fields.Integer(compute="_compute_remain")


