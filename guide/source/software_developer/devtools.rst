Development Tools
#################

Data Selection Tool
*******************

Program administrators are being instructed to use the :ref:`datatool` to
determine and communicate the intersection of :doc:`usecases/index` they're
interested in as well as any additional elements to collect and require.
Elements beyond established use cases are highlighted in red. In the
spreadsheeet, elements required by a use case will be more prominent (black font
color instead of light grey). Elements required in addition to specified use
cases will be highlighted in red. All together, it should provide a complete
list of data elements required to either provide or process.

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
