from __future__ import unicode_literals

import unittest

from django.http import HttpRequest
from django.template import Template
from django.template.context import RequestContext
from django.test.client import RequestFactory

from crumbs.templatetags.breadcrumb_tags import render_breadcrumbs

class CrumbsTestCase(unittest.TestCase):
    def test_render_without_request(self):
        render_breadcrumbs({})

    def test_render_with_request(self):
        render_breadcrumbs({'request': ''})

    def test_render_with_request_and_crumbs(self):
        context = {}
        context['request'] = HttpRequest() 
        context['request'].breadcrumbs = []
        context['request'].breadcrumbs.append(('Test1', '/'))
        context['request'].breadcrumbs.append(('Test2', '/'))
        render_breadcrumbs(context)

    def test_add_without_request(self):
        render_breadcrumbs({})

    def test_add_with_request(self):
        render_breadcrumbs({'request': ''})

    def test_add_with_request_and_crumbs(self):
        context = {}
        context['request'] = HttpRequest()
        context['request'].breadcrumbs = []
        context['request'].breadcrumbs.append(('Test1', '/'))
        context['request'].breadcrumbs.append(('Test2', '/'))
        render_breadcrumbs(context)

    def test_add_name_no_args(self):
        template = Template("{% load breadcrumb_tags %}{% add_crumb 'List' 'list_view' %}")
        request = RequestFactory().get('/')
        context = RequestContext(request)
        result = template.render(context)
        self.assertEqual(result, '')
        self.assertEqual(request.breadcrumbs, [('List', '/list_view/')])

    def test_add_absolute_no_args(self):
        template = Template("{% load breadcrumb_tags %}{% add_crumb 'Home' '/home/' %}")
        request = RequestFactory().get('/')
        context = RequestContext(request)
        result = template.render(context)
        self.assertEqual(result, '')
        self.assertEqual(request.breadcrumbs, [('Home', '/home/')])

    def test_add_kwargs(self):
        template = Template("{% load breadcrumb_tags %}{% add_crumb crumb='Home' url='/home/' %}")
        request = RequestFactory().get('/')
        context = RequestContext(request)
        result = template.render(context)
        self.assertEqual(result, '')
        self.assertEqual(request.breadcrumbs, [('Home', '/home/')])

    def test_add_with_args(self):
        template = Template("{% load breadcrumb_tags %}{% add_crumb 'Details' 'detail_view' 44 %}")
        request = RequestFactory().get('/')
        context = RequestContext(request)
        result = template.render(context)
        self.assertEqual(result, '')
        self.assertEqual(request.breadcrumbs, [('Details', '/detail_view/44/')])
