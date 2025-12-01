from odoo import models, fields, api

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    product_image = fields.Image(string="Product Image", store=True)

    @api.model
    def create(self, vals):
        if not vals.get('product_image') and vals.get('product_id'):
            product_id = vals['product_id']

            image = False
            if vals.get('origin'):
                sol = self.env['sale.order.line'].search([
                    ('order_id.name', '=', vals['origin']),
                    ('product_id', '=', product_id)
                ], limit=1)
                if sol and sol.product_image:
                    image = sol.product_image

            if not image:
                product = self.env['product.product'].browse(product_id)
                image = product.image_1920

            vals['product_image'] = image

        return super().create(vals)

    def write(self, vals):
        res = super().write(vals)

        if 'product_id' in vals and 'product_image' not in vals:
            for mo in self:
                image = False

                if mo.origin:
                    sol = self.env['sale.order.line'].search([
                        ('order_id.name', '=', mo.origin),
                        ('product_id', '=', mo.product_id.id)
                    ], limit=1)
                    if sol and sol.product_image:
                        image = sol.product_image

                if not image:
                    image = mo.product_id.image_1920

                mo.product_image = image

        return res
