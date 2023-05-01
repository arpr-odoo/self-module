from . import flight_db
from odoo import api, models,fields


class TicketBooking(models.Model):
    states = [('new','New'),('confirm','Confirmed'),('cancel','Canceled')]
    _name = "ticket.booking"
    _description = "Data of Customer which have booked ticket"

    name = fields.Char(required=True)
    phone = fields.Integer(required=True)
    email = fields.Char()
    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection(string="Gender",selection=[('m','Male'),('f','Female'),('o','Others')])
    passport_id = fields.Char(string="Passport Number", required=True)
    address = fields.Text()
    status = fields.Selection(string="Status",selection=states,default=states[0][0])

    # TODO:  make relation of this model to flight_db,seat type, flight type

    flight_id = fields.Many2one("flight.db")
    d_airport = fields.Char(related="flight_id.d_airport")
    d_time = fields.Datetime(related="flight_id.d_time")
    a_airport = fields.Char(related="flight_id.a_airport")
    a_time = fields.Datetime(related="flight_id.a_time")
    duration = fields.Float(related="flight_id.duration")

