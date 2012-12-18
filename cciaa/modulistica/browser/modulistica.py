# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter

from cciaa.modulistica import modulisticaMessageFactory as _

class ModulisticaView(BrowserView):
    """View for seeing the files in the folder"""

    IMG_TAG = """<img src="%s" alt="%s" title="%s" />"""

    def getDocumentContentOf(self, doc_id):
        """given an id, load from this folder a page"""
        context = self.context
        page = getattr(context, doc_id)
        body = '<a name="section-'+ doc_id +'"></a>' + page.getText()
        return body
    
    def generateImgTag(self, icon, alt="", title=""):
        """Given an icon, generate one from (X)HTML to be used in the view"""
        src = icon
        if not src:
            # Can happens for some values of icon_visibility in site_properties
            return alt
        return self.IMG_TAG % (src, alt, title)
    
    def safe_unicode(self, value):
        if isinstance(value, unicode):
            return value
        elif isinstance(value, str):
            try:
                return unicode(value, 'utf-8')
            except UnicodeDecodeError:
                return unicode(value, 'utf-8', 'ignore')
        return str(value)
    
    def getDownloadMessage(self, title, type):
        """'download' or 'goto'"""
        if type=='download':
            return _('download_message',
                     default=u'Download the file ${title}',
                     mapping={'title': self.safe_unicode(title)})
        elif type=='goto':
            return _('goto_message',
                     default=u'Go to link ${title}',
                     mapping={'title': self.safe_unicode(title)})            
        return None
    
    def generateColumns(self,related_items,num_rel):
        """Generate table columns"""
        var = related_items - num_rel
        stringa = ""
        for i in range(0, var):
            stringa += "<td class=\"col3\"/>"
        return stringa

    def count_related_items(self,items):
        """ return how many related items a file has, limited to 2"""
        max = 0
        for item in items:
            if item.portal_type=='File':
                if len(item.getRawRelatedItems) > max:
                    max = len(item.getRawRelatedItems)
            if max > 2:
                return 2
        return max
    
    def getColumns(self):
        return self.context.getField('columns').get(self.context)
    
    def getTitles(self,items):
        """Generate the table header with titles given in the folder new field"""
        stringa =""
        num_related = self.count_related_items(items) + 2
        columns = self.getColumns()
        
        if columns:
            if len(columns) > num_related:
                titles = columns[:num_related]
            else:
                titles = columns
        
            for title in titles:
                stringa += '<th class="nosort" scope="col">' + title + "</th>" 
            if len(titles) < num_related :
                for i in range(num_related-len(titles)):
                    stringa += "<th>" "</th>"
        return """<tr class="headingModuli">%s</tr>""" % stringa

    def isRemote(self, url):
        """Check if the given URL is remote or not
        only HTTP or HTTPS can be remote URLs 
        """
        if not url.lower().startswith("http"):
            return False 
        portal_url = getToolByName(self.context, 'portal_url')()
        return not url.startswith(portal_url)

    def getExternalLinkMessage(self):
        return _(u'External link') 

    def isAnon(self):
        return getToolByName(self.context, 'portal_membership').isAnonymousUser()

    def member(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        return portal_state.member()

