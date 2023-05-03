from . import flight_db
from odoo import api, exceptions, models,fields


class TicketBooking(models.Model):
    states = [('new','New'),('confirm','Confirmed'),('cancel','Canceled')]
    _name = "ticket.booking"
    _description = "Data of Customer which have booked ticket"

    name = fields.Char(required=True)
    phone = fields.Char(required=True)
    email = fields.Char()
    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection(string="Gender",selection=[('m','Male'),('f','Female'),('o','Others')])
    passport_id = fields.Char(string="Passport Number", required=True)
    address = fields.Text()
    status = fields.Selection(string="Status",selection=states,default=states[0][0])

    flight_id = fields.Many2one("flight.db")
    d_airport = fields.Char(related="flight_id.d_airport")
    d_time = fields.Datetime(related="flight_id.d_time")
    a_airport = fields.Char(related="flight_id.a_airport")
    a_time = fields.Datetime(related="flight_id.a_time")
    duration = fields.Float(related="flight_id.duration")

    seat_id = fields.Many2one("seat.types")
    ticket_type = fields.Selection(related="seat_id.ticket")
    available_tickets = fields.Integer(related="seat_id.available_tickets")

    _sql_constraints = [('unique_passport_id','unique(passport_id)','Passport ID must be unique...')]

    def confirm_action(self):
        if(self.status=='cancel'):
            raise exceptions.UserError("Canceled Ticket can't Buy again...")
        else:
            self.status = 'confirm'
        return True

    def cancel_action(self):
        self.status = 'cancel'
        return True