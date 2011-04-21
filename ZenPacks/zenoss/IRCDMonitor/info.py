###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.template import RRDDataSourceInfo
from ZenPacks.zenoss.IRCDMonitor.interfaces import IIRCDMonitorDataSourceInfo


class IRCDMonitorDataSourceInfo(RRDDataSourceInfo):
    implements(IIRCDMonitorDataSourceInfo)
    cycletime = ProxyProperty('cycletime')
    hostname = ProxyProperty('hostname')
    port = ProxyProperty('port')
    warning_num = ProxyProperty('warning_num')
    critical_num = ProxyProperty('critical_num')

    @property
    def testable(self):
        """
        We can NOT test this datsource against a specific device
        """
        return False
