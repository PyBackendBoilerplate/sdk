""" Defines an hooking system for system events.

This module defines the available hooks you can dynamically register.
"""

from dataclasses import dataclass

from sdk.infra.events import EventBase


@dataclass
class HookEventBase(EventBase):
    """
    Defines a hook base class.

    Args:
        EventBase ([type]): A hook is basically a more specialized event.
    """

    def __init__(self, *args, **kwargs):

        super(HookEventBase, self).__init__(*args, **kwargs)


@dataclass
class AppCreationDoneHook(HookEventBase):
    pass
