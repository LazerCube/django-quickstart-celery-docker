# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from celery import shared_task

@shared_task()
def on_chord_error(request, exc, traceback):
    print('Task {0!r} raised error: {1!r}'.format(request.id, exc))
