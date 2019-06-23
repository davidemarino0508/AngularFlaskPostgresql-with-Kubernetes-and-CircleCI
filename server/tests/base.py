"""Base Unit Test Case"""
import sys
sys.path.append('..')

import unittest
from ..main.api import create_app_blueprint
from ..main import db
from . import config_name

class BaseTestCase(unittest.TestCase):
    """A base class for test setup"""

    def create_app(self):
        # create a new instance of app
        app = create_app_blueprint(config_name)
        return app

    def setUp(self):
        """ setup method for unittest, called before each test function"""
        # create a new instance of app
        app = self.create_app()
        # to make request to my application
        self.client = app.test_client(self)
        # to use (current_app, g, url_for)
        self.context = app.app_context()
        self.request_context = app.test_request_context()
        db.create_all()
        db.session.commit()

    def tearDown(self):
        """Called after each test function"""
        db.session.remove()
        db.drop_all()
