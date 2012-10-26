import os
import subprocess

from mindpoolsite import meta
from mindpoolsite.scripts import base


class StopDaemon(base.Script):
    """
    """
    def run(self):
        pidFile = "twistd.pid"
        print "Stopping %s services ..." % meta.libraryName
        if not os.path.exists(pidFile):
            print "Could not find the server's PID file ..."
            print "Aborting."
        else:
            pid = open(pidFile).read()
            subprocess.call(["kill", pid])
            print "Stopped."
