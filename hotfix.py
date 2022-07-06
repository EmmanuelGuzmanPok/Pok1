from odoo import fields, models


class QualityReferencePatron(models.Model):
    _name = "quality.reference.patron"
    _description = "quality reference patron"

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
    instrument_model_id = fields.Many2one('quality.instrument.model',
                                          string="Instrument Model")
    value = fields.Integer(string="Value")
