# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from testthetest.models import Books


class CommonTestClass(TestCase):
    def __init__(self, *args, **kwargs):
        super(CommonTestClass, self).__init__(*args, **kwargs)

    def setUp(self):
        print "===MAINSETUP==="

        Books.objects.create(title="main", author="mainauthor")

    def tearDown(self):
        print "===MAINTEARDOWN==="

        Books.objects.all().delete()