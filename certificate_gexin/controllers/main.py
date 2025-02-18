# -*- coding: utf-8 -*-

from odoo.http import request, Controller, route


class CertificateController(Controller):

    @route('/validacion/certificado', type='http', auth='public', website=True)
    def validate_certificate(self, access_token, **kwargs):
        survey_user_input = request.env['survey.user_input'].sudo().search(
            [('access_token', '=', access_token)], limit=1)

        if survey_user_input:
            return request.render('certificate_gexin.certificate_validation_gexin', {
                'student_name': survey_user_input.partner_id.display_name or 'Desconocido',
                'certificate_valid': True,
                'completion_date': survey_user_input.end_datetime.strftime('%d/%m/%Y'),
                'survey_name': survey_user_input.survey_id.display_name,
            })
        else:
            return request.redirect('/404')
