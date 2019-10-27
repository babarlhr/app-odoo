# -*- coding: utf-8 -*-

# Created on 2018-10-12
# author: 广州尚鹏，https://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

# Odoo在线中文用户手册（长期更新）
# https://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# https://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# https://www.sunpop.cn/odoo10_developer_document_offline/
# description:

from odoo import api, SUPERUSER_ID, _


def pre_init_hook(cr):
    pass
    # cr.execute("")

def post_init_hook(cr, registry):
    try:
        #
        sql = "UPDATE res_partner SET customer = TRUE WHERE customer_rank >= 1;"
        cr.execute(sql)
        sql = "UPDATE res_partner SET supplier = TRUE WHERE supplier_rank >= 1"
        cr.execute(sql)
    except Exception as e:
        pass
    pass
    # cr.execute("")

def uninstall_hook(cr, registry):
    pass
    # cr.execute("")

