.. |hescore| replace:: Home Energy Score

|hescore|
#########

DOE's |hescore| rates a home's energy performance on a scale of 1 (least
efficient) to 10 (most efficient). The score is determined using the assessed
characteristics of the building that are either entered into a web interface by
a qualified assessor or submitted via software through a SOAP API. 

The API requires data inputs to be submitted in terms of the data model set forth by
|hescore|. Therefore, any users of the |hescore| API must translate their data
into the appropriate location and representation in the |hescore| input array. 

The |hescore| API provides the capability for an HPXML import. This receives an
HPXML file as input and translates the user-specified :ref:`building-node`
element (whether pre- or post-upgrade) into corresponding |hescore| inputs and
populates the |hescore| input array. 

By using this import capability, software developers can leverage their investment in HPXML to provide |hescore|
functionality at a minimum incremental development cost.

See :ref:`hescore-use-case-defn` for additional information.

|hescore| API
*************

For more information on how to use the |hescore| API, see the `API documentation
<https://developers.buildingsapi.lbl.gov/hescore>`_. The API method,
``submit_hpxml_inputs`` provides the HPXML import capability. 

Data elements required and translation details
**********************************************

The :ref:`datatool` includes |hescore|. It represents the minimum required data
fields for successful import. It is a good starting point. 

The HPXML import into |hescore| can accept a larger variety of data elements. The details of the translation and required HPXML elements
`are documented separately <http://hescore-hpxml.readthedocs.org/>`_.

Additionally, The translator has been  `released open source on GitHub
<https://github.com/NREL/hescore-hpxml>`_. Example HPXML files are available in
that repository.
