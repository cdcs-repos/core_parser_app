""" Tests for XSDParser - element
"""
from os.path import join, dirname, abspath
from lxml import etree

from unittest.case import TestCase

from tests.test_utils import DataHandler
from core_parser_app.tools.parser.parser import XSDParser
from xml_utils.commons.constants import LXML_SCHEMA_NAMESPACE, SCHEMA_NAMESPACE

# FIXME: use django finder
RESOURCES_PATH = join(dirname(abspath(__file__)), '..', 'data')

# FIXME: tests about html content were removed


class ParserGenerateElementTestSuite(TestCase):

    def setUp(self):
        element_data = join(RESOURCES_PATH, 'parser', 'element')
        self.element_data_handler = DataHandler(element_data)

        # set default namespace
        self.namespace = LXML_SCHEMA_NAMESPACE
        self.namespaces = {'xs': SCHEMA_NAMESPACE}

        # get an instance of the XSDParser
        self.parser = XSDParser()

    def test_create_simple_type_basic(self):
        xsd_files = join('simple_type', 'basic')
        xsd_tree = self.element_data_handler.get_xsd(xsd_files)
        xsd_element = xsd_tree.xpath('/xs:schema/xs:element',
                                     namespaces=self.namespaces)[0]

        # generate result dict
        result_dict = self.parser.generate_element(xsd_element, xsd_tree,
                                                   full_path='')

        # Load expected dictionary and compare with result
        expected_dict = self.element_data_handler.get_json(xsd_files)
        self.assertDictEqual(expected_dict, result_dict)

    def test_create_simple_type_unbounded(self):
        xsd_files = join('simple_type', 'unbounded')
        xsd_tree = self.element_data_handler.get_xsd(xsd_files)
        xsd_element = xsd_tree.xpath('/xs:schema/xs:complexType/xs:sequence/xs:element',
                                     namespaces=self.namespaces)[0]

        # generate result dict
        result_dict = self.parser.generate_element(xsd_element, xsd_tree,
                                                   full_path='')

        # Load expected dictionary and compare with result
        expected_dict = self.element_data_handler.get_json(xsd_files)
        self.assertDictEqual(expected_dict, result_dict)


class ParserReloadElementTestSuite(TestCase):

    def setUp(self):
        # Init data path
        element_data = join(RESOURCES_PATH, 'parser', 'element')
        self.element_data_handler = DataHandler(element_data)

        # Set default namespace
        self.namespace = LXML_SCHEMA_NAMESPACE
        self.namespaces = {'xs': SCHEMA_NAMESPACE}

        # Get an instance of the XSDParser with editing enabled
        self.parser = XSDParser()
        self.parser.editing = True

    def test_reload_simple_type_basic(self):
        xsd_files = join('simple_type', 'basic')
        xsd_tree = self.element_data_handler.get_xsd(xsd_files)
        xsd_element = xsd_tree.xpath('/xs:schema/xs:element',
                                     namespaces=self.namespaces)[0]

        xml_tree = self.element_data_handler.get_xml(xsd_files)
        xml_data = etree.tostring(xml_tree)
        edit_data_tree = etree.XML(str(xml_data.encode('utf-8')))

        # generate result dict
        result_dict = self.parser.generate_element(
            xsd_element, xsd_tree, full_path='',
            edit_data_tree=edit_data_tree
        )

        # Load expected dictionary and compare with result
        expected_dict = self.element_data_handler.get_json(xsd_files+".reload")
        self.assertDictEqual(expected_dict, result_dict)

    def test_reload_simple_type_unbounded(self):
        xsd_files = join('simple_type', 'unbounded')
        xsd_tree = self.element_data_handler.get_xsd(xsd_files)
        xsd_element = xsd_tree.xpath('/xs:schema/xs:complexType/xs:sequence/xs:element',
                                     namespaces=self.namespaces)[0]

        xml_tree = self.element_data_handler.get_xml(xsd_files)
        xml_data = etree.tostring(xml_tree)
        edit_data_tree = etree.XML(str(xml_data.encode('utf-8')))

        # generate result dict
        result_dict = self.parser.generate_element(
            xsd_element, xsd_tree, full_path='/root',
            edit_data_tree=edit_data_tree
        )

        # Load expected dictionary and compare with result
        expected_dict = self.element_data_handler.get_json(xsd_files+".reload")
        self.assertDictEqual(expected_dict, result_dict)

