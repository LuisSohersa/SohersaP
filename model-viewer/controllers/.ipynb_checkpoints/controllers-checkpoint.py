# -*- coding: utf-8 -*-
from odoo import http

class Site(http.Controller):
    @http.route('/model', website="true", auth='public')
    def index(self, **kw):
        return http.request.render('model-viewer.index',{})
#     @http.route('/model-viewer/model-viewer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('model-viewer.listing', {
#             'root': '/model-viewer/model-viewer',
#             'objects': http.request.env['model-viewer.model-viewer'].search([]),
#         })

#     @http.route('/model-viewer/model-viewer/objects/<model("model-viewer.model-viewer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('model-viewer.object', {
#             'object': obj
#         })
