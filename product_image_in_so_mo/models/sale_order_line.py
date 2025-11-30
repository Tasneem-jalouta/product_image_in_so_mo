from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_image = fields.Image(string="Product Image", store=True)

    @api.model
    def create(self, vals):
        if not vals.get('product_image') and vals.get('product_id'):
            product = self.env['product.product'].browse(vals['product_id'])
            vals['product_image'] = product.image_128
        return super().create(vals)

    def write(self, vals):
        res = super().write(vals)
        if 'product_image' in vals or 'product_id' in vals:
            for line in self:
                mos = self.env['mrp.production'].search([
                    ('origin', '=', line.order_id.name),
                    ('product_id', '=', line.product_id.id)
                ])
                for mo in mos:
                    mo.product_image = line.product_image or line.product_id.image_128
        return res
