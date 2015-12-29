#WebGUI daemon written for dashservcmd.

from daemon import runner

class webgui:

    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5

    def start(self):


app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
