# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spaceship(models.Models){
    
    _name = "spaceMission.spaceship"
    _description = "Spaceship"
    
    active = fields.Boolean(string = "Active", default = True)
    numOfPassengers = fields.Integer(string = "Number of Passengers")
    shipType = fields.Selection(string = "Type of Ship",selection = [("shipX","ShipX"),"shipY","ShipY")], copy = False)
    
    fuelType = fields.Selection(string = "Type of Fuel", selection = [("gas","Gas"),("diesel","Diesel")], copy = False)
    
    dimensions = fields.Char(string = "Dimensions(length x width x height)")
}
