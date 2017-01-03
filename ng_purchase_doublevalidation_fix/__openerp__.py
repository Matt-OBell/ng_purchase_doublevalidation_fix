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

{
    "name" : "Purchase Double Validation Fix",
    "version" : "1.0",
    "depends" : ["purchase_double_validation"],
    "author" : "Mattobell",
    "website" : "http://www.mattobell.com",
    "description": """
This module allow you to specify double validation of purchase amount on company form.
    """,
    "category" : "Purchase Management",
    "sequence": 32,
    "update_xml" : [
        "ng_purchase_doublevalidation_fix_view.xml",
    ],
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
