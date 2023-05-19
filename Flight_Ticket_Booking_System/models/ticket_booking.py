from odoo import api, exceptions, models,fields


class TicketBooking(models.Model):
    states = [('new','New'),('confirm','Confirmed'),('cancel','Canceled')]
    _name = "ticket.booking"
    _description = "Data of Customer which have booked ticket"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True,tracking=True)
    phone = fields.Char(required=True)
    email = fields.Char()
    dob = fields.Date(string="Date of Birth",required=True)
    gender = fields.Selection(string="Gender",selection=[('m','Male'),('f','Female'),('o','Others')])
    passport_id = fields.Char(string="Passport Number", required=True,tracking=True)
    address = fields.Text()
    status = fields.Selection(string="Status",selection=states,default=states[0][0],tracking=True)


    # getting flight details from flight_db model
    flight_data = fields.Many2one("flight.db",required=True)
    flight_id = fields.Char(related="flight_data.flight_id")
    d_airport = fields.Char(related="flight_data.d_airport")
    d_time = fields.Datetime(related="flight_data.d_time")
    a_airport = fields.Char(related="flight_data.a_airport")
    a_time = fields.Datetime(related="flight_data.a_time")
    duration = fields.Float(related="flight_data.duration")

    # getting ticket details from ticket_inventory
    ticket_inventory_id = fields.Many2one('ticket.inventory', string='Ticket Inventory',required=True)
    price = fields.Float(related="ticket_inventory_id.price")
    quantity = fields.Integer(related="ticket_inventory_id.quantity")
    _sql_constraints = [('unique_passport_id','unique(passport_id)','Passport ID must be unique...')]
        
        
    def confirm_action(self):
        self.ticket_inventory_id.quantity -= 1
        self.status = 'confirm'
        # print(self.ticket_inventory_id.flight_id['name'])
        # print()
        # print(self.flight_data['name'])
        return True

    def cancel_action(self):
        self.ticket_inventory_id.quantity += 1
        self.status = 'cancel'
        return True


    # for getting ticket types corrensponding to the flight
    @api.depends("")
    def get_ticket_types(self):
        pass