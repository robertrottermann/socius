from datetime import datetime, date, timedelta
from odoo import http,api,fields,models
import datetime
from odoo.http import request
# from odoo.addons.portal.controllers.portal import Websitedetail

class Websitedetail(http.Controller):
    @http.route(['/page/content1'], type='http', auth="public", website=True, csrf=False)
    def content(self,**kw):
        print("Homepage",kw)
        data = []
        # data1 = []
        details = request.env['backend.model'].browse(int(kw['id']))
        for i in details:
            # data.append(i)
            # print(data)
            # data = {'heading': i.name, 'content': i.comment, 'img': i.data_file, 'id': i.id}
            # print(data)
            data.append(i)
        return request.render('climate_website.content_one',  {'data':data})