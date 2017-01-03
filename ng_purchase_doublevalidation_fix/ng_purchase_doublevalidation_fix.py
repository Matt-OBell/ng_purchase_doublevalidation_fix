# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Mattobell (<http://www.mattobell.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from osv import osv, fields

from openerp.addons.base_status.base_stage import base_stage
import crm
from datetime import datetime
from operator import itemgetter
from openerp.osv import fields, osv, orm
import time
from openerp import SUPERUSER_ID
from openerp import tools
from openerp.tools.translate import _
from openerp.tools import html2plaintext

from base.res.res_partner import format_address


from osv import osv, fields

import netsvc
import pooler
from osv import fields, osv, orm
from tools.translate import _

class purchase_config_settings(osv.osv_memory):
    _inherit = 'purchase.config.settings'
    _columns = {
        'limit_amount': fields.integer('limit to require a second approval',required=True,
            help="Amount after which validation of purchase is required."),
    }
    _defaults = {
        'limit_amount': 5000,
    }

    def get_default_limit_amount(self, cr, uid, fields, context=None):
        print "SSSSSSSSSSSSSSSSSSSSSSSSSSSS"
        user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
        ir_model_data = self.pool.get('ir.model.data')
        transition = ir_model_data.get_object(cr, uid, 'purchase_double_validation', 'trans_confirmed_double_lt')
        field, value = transition.condition.split('<', 1)
        return {'limit_amount': int(user.company_id.limit_amount)}

    def set_limit_amount(self, cr, uid, ids, context=None):
        print "SSSSSSSSSSDDDDDDDDDDDDDD"
        user = self.pool.get('res.users').browse(cr, uid, uid, context=context)
        ir_model_data = self.pool.get('ir.model.data')
        config = self.browse(cr, uid, ids[0], context)
        waiting = ir_model_data.get_object(cr, uid, 'purchase_double_validation', 'trans_confirmed_double_gt')
        waiting.write({'condition': 'amount_total >= %s' % user.company_id.limit_amount})
        confirm = ir_model_data.get_object(cr, uid, 'purchase_double_validation', 'trans_confirmed_double_lt')
        confirm.write({'condition': 'amount_total < %s' % user.company_id.limit_amount})

class Company(osv.osv):
    _inherit = 'res.company'
    _columns = {
        'limit_amount': fields.integer('Purchase Double Approval Limit',required=False,
            help="Amount after which validation of purchase is required."),
    }
    _defaults = {
        'limit_amount': 5000,
    }

Company()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
