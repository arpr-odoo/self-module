{
    'name': "Flight Ticket Booking System",
    'version': '1.0',
    'depends': ['base'],
    'author': "Arth Prajapati",
    'category': 'Ticket Booking',
    'description': """
    Flight Ticket Booking System
    """,
    'application': True,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/seat_types_view.xml',
        'views/flight_db_views.xml',
        'views/ticket_booking.xml',
        'views/ticket_menus.xml',
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
}