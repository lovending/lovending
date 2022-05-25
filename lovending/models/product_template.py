from odoo import models, fields
import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_brand_id = fields.Many2one(
        "product.brand", string="SAL", help="Selecciona la marca del producto"
    )
    product_manufacturer_id = fields.Many2one(
        "product.manufacturer", string="Fabricante", help="Selecciona el fabricante"
    )