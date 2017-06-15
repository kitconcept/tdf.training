from Products.Five.browser import BrowserView
from plone import api
from plone.dexterity.browser.view import DefaultView
from tdf.extensionuploadcenter.eupproject import EUpProjectView


class ProjectListView(BrowserView):
    """ A list of projects
    """

    def projects(self):
        results = []
        brains = api.content.find(
            context=self.context,
            portal_type='tdf.extensionuploadcenter.eupproject')
        # http://docs.plone.org/develop/plone/searching_and_indexing/query.html
        # Low level call will be:
        # portal_catalog = api.portal.get_tool('portal_catalog')
        # brains = portal_catalog.searchResults(
        #              portal_type='tdf.extensionuploadcenter.eupproject'
        # )
        for brain in brains:
            # Beware of the getObject() method, only do that when it's required
            # if the date to retrieve is not stored as metadata in the catalog
            # project = brain.getObject()
            # basic data is stored as metadata:
            results.append({
                'title': brain.Title,
                'description': brain.Description,
                'url': brain.getURL(),
            })
        return results


class CustomEUpProjectView(EUpProjectView):
    """ Extended class for the customized view """

    def say_hallo(self):
        return "HALLO"
