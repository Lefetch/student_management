from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    student = fields.Boolean(string='Student', default=True)
    father_name = fields.Char(string='Father Name')
    surname = fields.Char(string='Surname')
    enrollment_number = fields.Char(
        string='Enrollment number',
        readonly=True,
        default=lambda self: _('New')
    )

    @api.model
    def create(self, vals):
        """i did override this method to allow to auto count the Enrollment number"""
        if vals.get('enrollment_number', _('New')) == _('New'):
            vals['enrollment_number'] = self.env['ir.sequence'].next_by_code('student.sequence') or _('New')
        return super(ResPartner, self).create(vals)





