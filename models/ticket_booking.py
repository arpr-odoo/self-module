import random
import string
from odoo import api, exceptions, models,fields


class TicketBooking(models.Model):
    states = [('new','New'),('confirm','Confirmed'),('cancel','Canceled')]
    _name = "ticket.booking"
    _description = "Data of Customer which have booked ticket"

    name = fields.Char(required=True)
    phone = fields.Char(required=True)
    email = fields.Char()
    dob = fields.Date(string="Date of Birth",required=True)
    gender = fields.Selection(string="Gender",selection=[('m','Male'),('f','Female'),('o','Others')])
    passport_id = fields.Char(string="Passport Number", required=True)
    address = fields.Text()
    status = fields.Selection(string="Status",selection=states,default=states[0][0])

    flight_data = fields.Many2one("flight.db")
    flight_id = fields.Char(related="flight_data.flight_id")
    d_airport = fields.Char(related="flight_data.d_airport")
    d_time = fields.Datetime(related="flight_data.d_time")
    a_airport = fields.Char(related="flight_data.a_airport")
    a_time = fields.Datetime(related="flight_data.a_time")
    duration = fields.Float(related="flight_data.duration")

    ticket_data = fields.Many2one("seat.types")
    # ticket_id = fields.Char(compute="generateTicket")
    ticket_type_id = fields.Char(related="ticket_data.name")

    ticket_inventory_id = fields.Many2one('ticket.inventory', string='Ticket Inventory')
    price = fields.Float(related="ticket_inventory_id.price")
    quantity = fields.Integer(related="ticket_inventory_id.quantity")

    _sql_constraints = [('unique_passport_id','unique(passport_id)','Passport ID must be unique...')]


    @api.depends("ticket_data")
    def generateTicket(self):
        if(self.ticket_data):
            self.ticket_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
        else:
            self.ticket_id = ""

    def confirm_action(self):
        if(self.status=='cancel'):
            raise exceptions.UserError("Canceled Ticket can't Buy again...")
        else:
            self.status = 'confirm'
        return True

    def cancel_action(self):
        self.status = 'cancel'
        return True