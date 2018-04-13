# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from core.tests import CommonTestClass
from testthetest.models import Books


class TestTheTest(CommonTestClass):
    def test_string_compare(self):
        self.assertEqual('1', '1')


class TestTheTestModel(TestCase):
    def test_book_and_author(self):
        """
        Book has an title and a author
        """
        print "===TEST==="

        main = Books.objects.get(title="main")
        self.assertEqual(getattr(main, 'main'), "mainauthor")
