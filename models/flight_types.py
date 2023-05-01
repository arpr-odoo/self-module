from odoo import fields,models


class FlightTypes(models.Model):
    _name = "flight.types"
    _description = "Type of Flight(Domestic, Internation)"

    
    # flight_type = fields.Selection(string="Flight Name",selection=[('air-india','Air India'),('indigo','IndiGO'),('go-air','GoAir')])
    
    flight_types = fields.Char(string="Flight Name")