# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import tdf.training


class TdfTrainingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=tdf.training)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tdf.training:default')


TDF_TRAINING_FIXTURE = TdfTrainingLayer()


TDF_TRAINING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TDF_TRAINING_FIXTURE,),
    name='TdfTrainingLayer:IntegrationTesting'
)


TDF_TRAINING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TDF_TRAINING_FIXTURE,),
    name='TdfTrainingLayer:FunctionalTesting'
)


TDF_TRAINING_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TDF_TRAINING_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='TdfTrainingLayer:AcceptanceTesting'
)
