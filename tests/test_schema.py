from lxml import etree
import pathlib
import pytest

here = pathlib.Path(__file__).resolve().parent
example_files = list((here.parent / 'examples').glob('*.xml'))
example_files.extend((here.parent / 'guide').glob('**/*.xml'))


def test_schema():
    # Checks that the schema is valid xsd
    xmlschema_doc = etree.parse(str(here / '..' / 'schemas' / 'HPXML.xsd'))
    xmlschema = etree.XMLSchema(xmlschema_doc)  # noqa: F841


@pytest.mark.parametrize('filename', example_files, ids=lambda x: x.stem)
def test_example_file(filename):
    xmlschema_doc = etree.parse(str(here / '..' / 'schemas' / 'HPXML.xsd'))
    xmlschema = etree.XMLSchema(xmlschema_doc)
    doc = etree.parse(str(filename))
    if str(filename).endswith('invalid.xml'):
        assert not xmlschema.validate(doc)
    else:
        assert xmlschema.validate(doc)
