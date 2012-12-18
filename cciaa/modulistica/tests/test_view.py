# -*- coding: utf-8 -*-

from cciaa.modulistica.tests.base import TestCase
import re

class TestView(TestCase):

    def afterSetUp(self):
        self.setRoles(('Manager', ))
        portal = self.portal
        portal.invokeFactory(type_name="Folder", id="modulistica")
        m = getattr(portal, 'modulistica')
        m.edit(title="Modulistica")
        m.manage_addProperty('layout', 'cciaa_modulistica_view', 'string')
        
    def getModulistica(self):
        return self.portal.modulistica

    def test_addFile(self):
        m = self.getModulistica()
        m.invokeFactory(type_name='File', id='f1')
        f1 = getattr(m, 'f1')
        f1.edit(title='File 1', file='Lorem ipsum')
        self.assertTrue('Download the file File 1' in m())

    def test_addFileWithUnicodeName(self):
        m = self.getModulistica()
        m.invokeFactory(type_name='File', id='f1')
        f1 = getattr(m, 'f1')
        f1.edit(title='File ùno', file='Lorem ipsum')
        self.assertTrue(u'Download the file File ùno' in m())

    def test_addInternalLink(self):
        m = self.getModulistica()
        m.invokeFactory(type_name='Link', id='l1')
        l1 = getattr(m, 'l1')
        l1.edit(title='Link 1', remoteUrl=self.portal['news'].absolute_url())
        result = m()
        self.assertTrue('Visita Link 1' in result)
        self.assertFalse('ollegamento esterno' in result)
        
    def test_addExternalLinkNoDescr(self):
        """When external link has no descr, show only the tip text"""
        m = self.getModulistica()
        m.invokeFactory(type_name='Link', id='l1')
        l1 = getattr(m, 'l1')
        l1.edit(title='Link 1', remoteUrl='http://www.plone.org/')
        result = m()
        self.assertTrue('Visita Link 1' in result)
        self.assertEquals(len(re.findall('xternal link',result)), 1)

    def test_addExternalLinkWithDescr(self):
        """When external link has also descr, show tip text and description with additional text"""
        m = self.getModulistica()
        m.invokeFactory(type_name='Link', id='l1')
        l1 = getattr(m, 'l1')
        l1.edit(title='Link 1', remoteUrl='http://www.plone.org/', description="Go to plone.org")
        result = m()
        self.assertTrue('Visita Link 1' in result)
        self.assertEquals(len(re.findall('xternal link',result)), 2)

    def test_noHTTPExternalLink(self):
        """All links that don't starts with HTTP(s) are not external"""
        m = self.getModulistica()
        m.invokeFactory(type_name='Link', id='l1')
        l1 = getattr(m, 'l1')
        l1.edit(title='Link 1', remoteUrl='mailto:plone-devel@plone.org', description="Write to plone")
        result = m()
        self.assertTrue('Visita Link 1' in result)
        self.assertFalse('external link' in result)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestView))
    return suite
