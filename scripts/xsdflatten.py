#!/usr/bin/env python
import sys
import re
import copy
from lxml import etree


def get_includes_from_file(filename):
    pattern = re.compile('(<xs:include schemaLocation)')
    lines = [line.strip() for line in open(filename).readlines()]
    includes = [line.split('=')[1].split('"')[1] for line in lines if pattern.match(line)]

    # sanity check
    for inc in includes:
        if not inc.endswith('.xsd'):
            raise 'Problem including %s in file %s' % (inc, filename)

    return includes


def get_includes_recurse(filename, include_set):
    includes = get_includes_from_file(filename)
    include_set.update(includes)
    for inc in includes:
        get_includes_recurse(inc, include_set)


def get_xml_tree_from_file(filename):
    tree = etree.parse(filename)
    return tree.getroot()


def remove_includes(root):
    # Find and remove the includes
    includes = root.findall('xs:include', root.nsmap)
    for inc in includes:
        root.remove(inc)
    return root


def flatten_file(filename, outfilename):
    include_set = set()
    get_includes_recurse(filename, include_set)

    # Get the main document
    root = get_xml_tree_from_file(filename)
    root = remove_includes(root)

    # Merge in the elements of the includes
    for inc_file in include_set:
        inc_root = get_xml_tree_from_file(inc_file)
        inc_root = remove_includes(inc_root)
        # root.append(etree.Comment('Imported from %s' % inc_file))
        for child in inc_root:
            root.append(copy.deepcopy(child))

    # Write to file
    with open(outfilename, 'wb') as f:
        f.write(etree.tostring(root, pretty_print=True))
    print(f'Wrote output file: {outfilename}.')


def main(filename, outfilename):
    flatten_file(filename, outfilename)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
