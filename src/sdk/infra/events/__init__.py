from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Type

import zope.event


@dataclass
class EventBase:
    """
    Defines the base class for the events scheme classes that will define
    how each event looks.

    To implement a handler see http://zopeevent.readthedocs.io/en/latest/classhandler.html
    or implement like this example:

    Implement custom handlers like this:

    from zope.event.classhandler import handler
    from my_custom_events import MyEventClass


    @handler(MyEventClass)
    def MyEventClassHandler(event: MyEventClass):
        print('In MyEventClassHandler()')
    """

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return self.__class__.__name__


def notify(event_lambda: Callable[[], Type[EventBase]]):
    """
    Calls the all of the registered handlers for the given event class type.

    Args:
        event_lambda (Callable[[], EventBase]): lambda: EventClass(*args, **kwargs) where EventClass is a subclass of EventBase.
    """

    # We create the instance here using the event lambda function to be able to control the call
    event_instance = event_lambda()

    zope.event.notify(event_instance)
