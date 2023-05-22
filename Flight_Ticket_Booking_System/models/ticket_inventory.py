from odoo import fields,models,api


class TicketInventory(models.Model):
    _name = 'ticket.inventory'
    _description = 'Ticket Inventory'


    name = fields.Many2one('seat.types')
    flight_id = fields.Many2one('flight.db')
    price = fields.Float(required=True)
    quantity = fields.Integer()


    ticket_booking_id = fields.One2many("ticket.booking","ticket_inventory_id")

    # seat_ids = fields.One2many('ticket.inventory', 'name', string='Ticket Inventories')
    seat_count = fields.Integer(compute="_compute_seat_count")


    @api.depends("ticket_booking_id")
    def _compute_seat_count(self):
        # print(self.ticket_booking_id)
        self.seat_count = len(self.ticket_booking_id)
        # if(self.ticket_booking_id)
        # self.seat_count = len(self.ticket_booking_id)

    def tickets_of_flight_action(self):
        return {
            'type':'ir.actions.act_window',
            'name':('tickets'),
            'res_model':'ticket.booking',
            'view_type':'list',
            'view_mode':'list',
            'domain':[('id','in',self.ticket_booking_id.ids)]
        }
