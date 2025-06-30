Versioning
##########

The HPXML schemas follow the `Semantic Versioning v2.0 <http://semver.org/>`_
specification. The version numbers follow a pattern of :ref:`major-version`.
:ref:`minor-version`. :ref:`patch-version` (i.e. 4.2.0). 

The first element of ``HPXML.xsd`` will indicate the version of the schema via
the ``version`` attribute. Note that when referencing a version, the patch
number is assumed to be zero if it is omitted. 

.. code-block:: xml

   <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="http://hpxmlonline.com/2023/09"
    targetNamespace="http://hpxmlonline.com/2023/09" elementFormDefault="qualified" version="4.2"> 

Additionally, starting with version 2.0, the version of the schema used is
required in the ``schemaVersion`` attribute on the root element of every
document. 

.. code-block:: xml

   <HPXML xmlns="http://hpxmlonline.com/2023/09" schemaVersion="4.2">
    
.. _major-version:

Major
*****

The major version number is incremented when the schemas are changed in a manner
which is incompatible with previous versions. Examples of changes which
necessitate a major version change include:

   * Renaming elements 
   * Removing elements 
   * Moving elements 
   * Removing enumerations

A different xml namespace is used for each major revision. Starting with version
2.0, the namespaces follow the pattern where the year and month are when the major version number was changed.

::

   http://hpxmlonline.com/[Year]/[Month]

.. _minor-version:

Minor
*****

The minor version number is incremented when the schemas are changed in a manner
that is backwards compatible with previous versions that share the same
:ref:`major-version` version. Backwards compatible in the context of HPXML
means that given the schema changes, a document created in a previous version
of the schema will also validate against the new schema. Example of changes
which necessitate a minor version change include:

   * Adding elements
   * Adding enumerations
   * Changing the annotation in the schema for an element

.. warning::

   Based on the definition of backwards compatibility, adding enumerations 
   is a non-breaking change. However, it can be breaking for receiving systems 
   if they are not expecting the change. The working group will provide warning 
   when new enumerations are added so that receivers have an opportunity to 
   respond by updating support. 

.. _patch-version:

Patch
*****

A patch version number is incremented when a backwards compatible change (as
described in :ref:`minor-version`) is made to address a bug.
