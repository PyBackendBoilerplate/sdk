from zope.event.classhandler import handler

from sdk.infra.events import EventBase


def register_infra_events_handlers() -> None:
    """
    To register the event handler callback functions, you just need to import them
    so by importing this module to call this function, you will have them all imported
    and registered by zope.event.
    """

    from sdk.infra.events.handlers import hooks


@handler(EventBase)
def EventBaseHandler(event: EventBase):
    """This will run for EVERY event (include custom events). """

    # Nothing to implement here at the moment...
    pass
