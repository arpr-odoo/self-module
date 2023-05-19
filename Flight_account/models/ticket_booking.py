from odoo import api,fields,models,Command


class TicketBooking(models.Model):
    _inherit = 'ticket.booking'

    def confirm_action(self):
        self.env['account.move'].create({
            'move_type':'out_invoice',
            "invoice_line_ids":[
                Command.create({
                    "name":"Base Flight Charges",
                    "quantity":1,
                    "price_unit":self.price*0.80
                }),
                Command.create({
                    "name":"convenience fees",
                    "quantity":1,
                    "price_unit":500
                }),
            ]
        })
        return super().confirm_action()