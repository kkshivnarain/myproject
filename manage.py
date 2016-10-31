<<<<<<< HEAD
#!/usr/local/bin/python2.7
=======
#!/usr/bin/env python
>>>>>>> 01375511faeadc5485caff722ece85c561f19e85
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
