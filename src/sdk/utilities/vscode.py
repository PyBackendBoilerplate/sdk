"""Code snippet to allow docker debugging in vscode

Taken originally from https://github.com/adriencaccia/vscode-flask-debug

Typical usage example:

from sdk.utilities.vscode import initialize_flask_server_debugger_if_needed

if __name__ == '__main__':
    initialize_flask_server_debugger_if_needed()

    print('Hello, World!')

"""

from sdk.config import ConfigBase


# TODO: run only on vscode if possible
def initialize_flask_server_debugger_if_needed(port: int = 10001):
    """
    Waits for VS Code debugger to attach on 0.0.0.0:port.

    Args:
        port (int, optional): Port number for VS Code to use when attaching the debugger. Defaults to 10001.
    """

    if ConfigBase().active_env.vscode_debug_mode is True:
        import multiprocessing
        """
            In debug mode Flask uses a first Process (pid 1) to start child processes that handle connections.
            If the main process isn't filtered out from the debugging, the debugging port is taken and subsequent
            child processes can't use the same port and are attributed a random port which prevents connections.
        """
        if multiprocessing.current_process().pid > 1:

            import debugpy

            debugpy.listen(('0.0.0.0', port))
            print('~#~ VS Code debugger can now be attached, press F5 in VS Code ~#~', flush=True)
            debugpy.wait_for_client()
            print('~#~ VS Code debugger attached, enjoy debugging ~#~', flush=True)
