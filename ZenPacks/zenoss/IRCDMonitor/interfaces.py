###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
from Products.Zuul.interfaces import IRRDDataSourceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IIRCDMonitorDataSourceInfo(IRRDDataSourceInfo):
    cycletime = schema.Int(title=_t(u'Cycle Time (seconds)'))
    hostname = schema.Text(title=_t(u'Host Name'),
                           group=_t(u'IRC'))
    warning_num = schema.Int(title=_t(u'Warning Count'),
                             group=_t(u'IRC'))
    port = schema.Int(title=_t(u'Port'),
                      group=_t(u'IRC'))
    critical_num = schema.Int(title=_t(u'Critical Count'),
                              group=_t(u'IRC'))
