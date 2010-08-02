#!/usr/bin/env python

import sys
import os.path

# remove '.' from the path (you should use the project package to reference
# anything in here)
sys.path.pop(0)
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.dirname(PROJECT_ROOT))

DEFAULT_SETTINGS_MAP = {
    'runserver': 'sample_project.settings',
    'shell': 'sample_project.settings',
    'dbshell': 'sample_project.settings',
}
settings_specified = any([arg.startswith('--settings=') for arg in sys.argv])
if not settings_specified and len(sys.argv) >= 2:
    command = sys.argv[1]
    settings_module = DEFAULT_SETTINGS_MAP.get(command,
                                               'sample_project.settings')
    if settings_module:
        print 'NOTICE: using default settings module "%s" for command "%s"' % (settings_module, command)
        sys.argv.append('--settings=%s' % settings_module)

try:
    import sample_project.settings
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'local_settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

from django.core.management import execute_manager
if __name__ == "__main__":
    execute_manager(sample_project.settings)
