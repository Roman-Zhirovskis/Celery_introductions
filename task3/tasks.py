from __future__ import absolute_import, unicode_literals

from django.core.management import call_command

from celery import shared_task

import sys


@shared_task
def bkup():
    sys.stdout = open("db.json", "w")
    call_command("dumpdata", "task3")
