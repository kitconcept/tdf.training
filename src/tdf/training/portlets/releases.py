# -*- coding: utf-8 -*-
from plone import api
from zope.interface import implements
from zope import schema

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from tdf.training import _


class IReleasesPortlet(IPortletDataProvider):

    count = schema.Int(title=_(u'Number of items to display'),
                       description=_(u'How many items to list.'),
                       required=True,
                       default=5)


class Assignment(base.Assignment):
    implements(IReleasesPortlet)

    count = 5

    title = _(u'label_releases_portlet', default=u'Releases portlet')

    def __init__(self, count=5):
        self.count = count


class Renderer(base.Renderer):
    """Actions portlet renderer."""

    render = ViewPageTemplateFile('releases.pt')

    def all_releases(self):
        """Get a list of all releases, ordered by version, starting with the latest.
        """

        catalog = api.portal.get_tool(name='portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        res = catalog.searchResults(
            portal_type=('tdf.extensionuploadcenter.euprelease', 'tdf.extensionuploadcenter.eupreleaselink'),
            path=current_path,
            sort_on='Date',
            sort_order='reverse',
            limit=self.data.count)
        return [r.getObject() for r in res]


class AddForm(base.AddForm):
    """Portlet add form.
    This is registered in configure.zcml. The schema attribute tells
    plone.autoform which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    schema = IReleasesPortlet
    label = _(u'heading_add_actions_portlet',
              default=u'Add actions portlet')
    description = _(u'help_add_actions_portlet',
                    default=u'An action portlet displays actions from a category')

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The schema attribute tells
    plone.autoform which fields to display.
    """
    schema = IReleasesPortlet
