# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from tdf.training.testing import TDF_TRAINING_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that tdf.training is properly installed."""

    layer = TDF_TRAINING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if tdf.training is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'tdf.training'))

    def test_browserlayer(self):
        """Test that ITdfTrainingLayer is registered."""
        from tdf.training.interfaces import (
            ITdfTrainingLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ITdfTrainingLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TDF_TRAINING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['tdf.training'])

    def test_product_uninstalled(self):
        """Test if tdf.training is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'tdf.training'))

    def test_browserlayer_removed(self):
        """Test that ITdfTrainingLayer is removed."""
        from tdf.training.interfaces import \
            ITdfTrainingLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           ITdfTrainingLayer,
           utils.registered_layers())
