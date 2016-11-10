
from pyinotify import *
import os, os.path

flags = IN_CLOSE_WRITE| IN_CREATE | IN_Q_OVERFLOW
dirs = {}
base = '/log/lighttpd/cache/images/icon/u241'
base = 'tmp'


class UpdateParentDir(ProcessEvent):
    def process_IN_CLOSE_WRITE(self, event):
        print 'modify', event.pathname
        mtime = os.path.getmtime(event.pathname)
        p = event.path
        while p.startswith(base):
            m = os.path.getmtime(p)
            if m < mtime:
                print 'update', p
                os.utime(p, (mtime, mtime))
            elif m > mtime:
                mtime = m
            p = os.path.dirname(p)

    process_IN_MODIFY = process_IN_CLOSE_WRITE

    def process_IN_Q_OVERFLOW(self, event):
        print 'over flow'
        max_queued_events.value *= 2

    def process_default(self, event):
        pass


wm = WatchManager()
notifier = Notifier(wm, UpdateParentDir())
dirs.update(wm.add_watch(base, flags, rec=True, auto_add=True))

notifier.loop()