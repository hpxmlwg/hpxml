from lxml import etree
import pathlib

here = pathlib.Path(__file__).resolve().parent


def test_schema():
    # Checks that the schema is valid xsd
    xmlschema_doc = etree.parse(str(here / '..' / 'schemas' / 'HPXML.xsd'))
    xmlschema = etree.XMLSchema(xmlschema_doc)  # noqa: F841
