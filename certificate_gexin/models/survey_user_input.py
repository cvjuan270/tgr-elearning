from odoo import models, fields
from odoo.http import request


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    def get_formatted_duration(self):
        if self.slide_id:
            hours = int(self.slide_id.completion_time)
            minutes = int((self.slide_id.completion_time - hours) * 60)
            return f"{hours}:{minutes:02d}"
        return False
