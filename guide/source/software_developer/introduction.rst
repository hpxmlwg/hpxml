Introduction
############

This section of the Implementation Guide is designed to outline the technical details of implementing HPXML. HPXML is
an expansive standard data format based on extensible markup language (XML) and maintained by the Building
Performance Institute's HPXML working group. For more information on HPXML, visit http://www.hpxmlonline.com. 

The HPXML format is defined by a set of XML Schema (XSD) documents that outline
all the acceptable data elements, their structure, and relation to one another.
The schema itself is very flexible. Almost none of the elements are required,
which allows for any level of detail in home performance data to be transmitted
in the format. This level of flexibility is very useful but it also can be
dangerous for the software developer. Two developers could each create an
implementation that would represent their data in valid HPXML, but would be divergent. The purpose of this guide is to document the assumptions that are not codified in the schema that are necessary to write and interpret HPXML documents
across platforms.

Standard Datasets
*****************

In order to better utilize the standard and have consistency across the HPXML workging group has created :doc:`/standard_datasets` that define what data elements are required for a pre-defined set of typical use cases. While most programs will have their own specific data needs to be supported by HPXML these can serve a useful starting point to enable interoperability between existing systems already in the marketplace. 

The majority of the assumptions and recommendations in this Guide come from the set of
pilot implementations in the :doc:`Audit-Upgrade Standard Dataset
</software_developer/usecases/auditupgrade>`. This guide primarily documents
lessons learned from those pilots. As other datasets are created, this
guide will continue to be updated.

HPXML Working Group
*******************

One of the best resources you will have available to you as you develop to HPXML
is the HPXML Working Group. Many of the current
developers are working group members. They have a lot of experience in getting HPXML working and
can help you avoid costly pitfalls.

To join the working group, send an email to hpxml@homeperformance.org.

GitHub
******

The HPXML schemas, example files, and this guide are all `maintained on GitHub
<https://github.com/hpxmlwg/hpxml>`_. You will always be able to find the latest
version of the schemas there. Additionally as the schemas evolve over time you
can be connected to and influence that process. 

