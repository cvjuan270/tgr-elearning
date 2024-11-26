from odoo.http import request

from odoo.addons.portal.controllers import portal


class CustomerPortal(portal.CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        partner = request.env.user.partner_id
        slideChanelParner = request.env["slide.channel.partner"]
        if "slide_channel_count" in counters:
            values["slide_channel_count"] = (
                slideChanelParner.sudo().search_count([("partner_id", "=", partner.id)])
            ) or 0
        return values
