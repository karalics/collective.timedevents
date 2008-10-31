"""
    Time based events
    
    http://www.twinapex.com

"""

__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__copyright__ = "Copyright 2008 Twinapex Research"
__license__ = "GPL"
__docformat__ = "epytext"

# Python imports
import logging

# Zope imports
import zope
from DateTime import DateTime
from zope.component import adapter

# Local imports
from interfaces import ITickEvent

class TickEvent(object):
    """This class implements the ITickEvent interface.
    """
    zope.interface.implements(ITickEvent)

    def __init__(self, date_time, next_tick):
        self.date_time = DateTime(date_time)
        self.next_tick = DateTime(next_tick)


@adapter(ITickEvent)
def tick_logger(tick_event):
    """This function is a handler for the ITickEvent. Its purpose is to log all
       ticks.
    """
    l = logging.getLogger('timedevents')
    l.info('(%s) TICK detected.' % tick_event.date_time.ISO())


