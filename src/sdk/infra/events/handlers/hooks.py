from zope.event.classhandler import handler

from sdk.infra.events.hooks import AppCreationDoneHook, HookEventBase


@handler(HookEventBase)
def HookEventBaseHandler(event: HookEventBase):
    """This will run for EVERY hook event (include custom events). """

    # Nothing to implement here at the moment...
    pass


@handler(AppCreationDoneHook)
def AppCreationDoneHookHandler(event: AppCreationDoneHook):
    # Nothing to implement here at the moment...
    pass
