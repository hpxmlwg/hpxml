.. include:: <isonum.txt>

Overview of HPXML
#################

What is HPXML?
**************

In today’s existing homes market, the electronic exchange of information on energy performance, energy conservation measures, and the physical and operational attributes of a home is often characterized by a lack of common terms, definitions, and two-way feedback systems. This limits the ability of decision-makers to access, aggregate, share and use data for the design and implementation of residential energy efficiency programs. This also makes it difficult for market actors to understand the drivers of variation in performance (e.g., of measures, contractors, programs, and homes), identify investment opportunities, analyze market trends, and project savings from energy efficiency investments.

.. figure:: /images/existing_connections.png
    :figwidth: 3in
    :align: center

    Figure 1: Existing Market Conditions

Open data standards, like HPXML, are a powerful solution to some of the most intractable problems facing the residential energy efficiency industry. Data standards are crucial in enabling the quantification of energy savings that result from energy efficiency upgrades that in turn allow for savings guarantees, low-cost consumer finance, and the sale of energy efficiency into energy, capacity, and carbon markets. Data standards are crucial for ensuring that energy efficiency improvements in homes are properly valued in real estate transactions. Finally, data standards are crucial for supporting ongoing research into the best methods for making homes energy efficient because the aggregation of standardized data supports comparability and comprehensive analysis of program and contractor performance.

.. figure:: /images/hpxml_connected_market.png
    :figwidth: 3in
    :align: center

    Figure 2: Connected Market

HPXML is comprised of two BPI data standards that were published in 2013 to support a growing industry by facilitating communication and the exchange of information and data on residential building and energy performance. The purpose of HPXML is to:

    * Standardize terminology and facilitate the collection of higher quality data as a means of tracking and quantifying work being completed across the residential energy efficiency industry;
    * Create interoperability between software systems to allow the transfer of residential energy efficiency data across a diverse set of market actors, such as the real estate and financial sectors; and,
    * Improve industry efficiency by reducing the costs of data collection and exchange between market actors.

The HPXML Data Dictionary (BPI-2200) standardizes terms and data formats related to the physical attributes and performance of buildings and measures. It defines the data elements necessary to provide a general description of a whole house or single measure energy efficiency upgrade for reporting, rebate and basic quality assurance (QA) purposes. The standard includes several smaller datasets that are being used to standardize data collection and reporting for specific use cases, for example, data required at the completion of a whole-house program (see section on Standard HPXML Datasets).

The HPXML Transfer Standard (BPI-2100) provides requirements for a standard extensible mark-up language (XML) data transfer protocol that can be used to transfer information and data between different software systems. The transfer standard is the companion standard to the HPXML data dictionary. Each of the data elements defined in the data dictionary can be transferred using HPXML.

Data standards, like other standards, are more valuable the more broadly they are used. Every time a program implements a data standard, transactional costs fall for firms already using the standard. Software vendors can provide a rich set of data about a whole-house upgrade to programs using HPXML at very little additional cost because they have already made the initial investment to design their software to support the data standards. For the energy efficiency industry to realize the full benefit of the BPI data standards, it is crucial that more programs and other users adopt the standards.

Aligned with Industry Standards
*******************************

HPXML is the most widely used implementation of the Department of Energy’s (DOE) Building Energy Data Exchange Specification (BEDES). BEDES is a dictionary of terms, definitions, and data formats created to facilitate the exchange of information on building characteristics and energy use for the commercial, multifamily and residential industries.

HPXML is also aligned with the Real Estate Standards Organization's (RESO) Data Dictionary, which standardizes terms used in Multiple Listing Services (MLS) and other source providers nationwide so that information can be easily shared and understood in the real estate industry.

The benefit of having HPXML aligned with the RESO Data Dictionary and with BEDES is to increase interoperability across sectors and industries. Home energy efficiency information, including score and labels, can be transferred to MLS databases. 

Management and Version Control
******************************

HPXML Working Group
===================

HPXML has been developed, and is modified and maintained, by the stakeholders who use it, including organizations and individuals from residential energy efficiency programs, software development, government, home performance contracting, and the nonprofit sector. 

The Home Performance Coalition (HPC) chairs a national working group of industry experts with oversight from the BPI Data and Modeling Standards Technical Committee using an open and consensus based decision-making process set by BPI. The working group meets quarterly to discuss updates and to vote on new versions of the standards.

Membership and participation in the HPXML working group is voluntary and open to all organizations and individuals interested in HPXML.

The HPXML Working Group can be a valuable resource for program administrators, implementers and software developers that are interested in adopting HPXML.

Versioning
==========

The HPXML schema follows the `Semantic Versioning 2.0 specification <http://semver.org/>`_. The version numbers follow a pattern of Major, Minor, and Patch (e.g., 4.2.0). The major version number is incremented when the schemas are changed in a manner that is incompatible with previous versions. Examples of changes that require a major version change include renaming elements, removing elements, moving elements, and removing enumerations.

The minor version number is incremented when the schemas are changed in a manner that is backwards compatible with previous versions that share the same major version. In other words, a document created in a previous version of the schema will also validate against the new schema. Examples of changes that require a minor version change include adding elements, adding enumerations, and changing the annotation in the schema for an element. 

Technical documentation can be found at https://www.hpxmlonline.com/.

HPXML Compliance
****************

Stakeholders that wish to comply with the HPXML Data Dictionary and Transfer Standard shall use HPXML data in all cases in which an HPXML data element is sufficient to adequately represent the person, characteristic, concept or other home-related datum that is being described.

Data can be adequately represented by HPXML if HPXML data elements, singularly or in combination, can be used to describe the person or thing in a way that:

    1. Could reasonably be understood by other energy efficiency professionals; and,
    2. Does not result in significant loss of information or create significant risks of miscommunication.
    
Software developers may validate their HPXML files against the schema and its datasets by uploading files to the `HPXML Validator <https://hpxml.nrel.gov/validator/>`_. Sample HPXML files are `available on Github <https://github.com/hpxmlwg/hpxml/tree/master/examples>`_. 

Continued Growth
****************

When reviewing the datasets that are required for your implementation, it is possible to identify a data point you require that is not in one of the pre-defined datasets or in HPXML. If this is the case, the HPXML working group can assist in adding the new data element and in identifying how to incorporate it into the standard.

See :ref:`how_to_add_data_elements` for details.
