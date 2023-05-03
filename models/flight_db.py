from odoo import models,fields,api


class FlightDB(models.Model):
    _name = "flight.db"
    _description = "Flight Ticket Booking System"

    flight_id = fields.Integer()
    d_airport = fields.Char()
    d_time = fields.Datetime()
    a_airport = fields.Char()
    a_time = fields.Datetime()
    duration = fields.Float(compute="_compute_duration")
    
    _sql_constraints = [('unique_flight_id','unique(flight_id)','Flight ID must be Unique...')]
    
    @api.depends("d_time","a_time")
    def _compute_duration(self):
        for record in self:
            if(record.a_time and record.d_time):
                diff = record.a_time - record.d_time
                print(diff.days)
                days,seconds = diff.days, diff.seconds
                travel_hours = days*24 + seconds/3600
                record.duration = travel_hours
            else:
                record.duration = 0