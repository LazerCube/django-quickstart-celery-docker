# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig

class CoreConfig(AppConfig):
    name = 'modules.core'

    def ready(self):
        pass