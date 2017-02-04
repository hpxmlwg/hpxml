Development Tools
#################

Data Selection Tool
*******************

A :ref:`datatool` has been developed to help program administrators select the data points they are requiring to collect for specific use cases. The data selection tool is a spreadsheet with the required and optional data points selected by working group members for specific use cases, including Audit, Upgrade, Home Energy Score, and Home Performance Certificate. A detailed desccription of these use cases and the corresponding standard HPXML datasets can be found in section :ref:'

In the spreadsheeet, data points required by a dataset will be in black color instead of light grey. Elements that are optional are highlighted in red.

The standard datasets provide a complete list of data elements required to either provide or process.

HPXML Toolbox
*************

To facilitate the adoption of the HPXML standard use cases, NREL has developed
the `HPXML Toolbox`_. The toolbox provides a schema validator plus use case
validator. Submitting an HPXML file will perform the following steps:

#. Validation of the file against HPXML schema and determination of schema version.
#. Validation against each of the standard use cases including output describing
   any missing elements required to meet a particular use case. 
#. Display of HPXML file in collapsable tree form.

The validation functionality is available as a `website`_ for testing and
viewing individual files, or as a `web service API`_ that allows the validation
to be called as part of a software workflow. 

.. _website: https://hpxml.nrel.gov/validator/
.. _web service API: https://hpxml.nrel.gov/api/
.. _HPXML Toolbox: https://hpxml.nrel.gov
