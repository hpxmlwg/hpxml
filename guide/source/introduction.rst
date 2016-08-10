.. include:: <isonum.txt>

Introduction to HPXML
#####################

The Need for Data Standardization
*********************************

In today’s residential energy efficiency market the electronic exchange of information and data is often characterized by a
lack of common terms, definitions, and two-way feedback systems (Figure 1). This limits the ability of decision-makers to
access, aggregate, share and use data for the design and implementation of energy efficiency programs. This also makes it
difficult for market actors to understand the drivers of variation in performance (e.g., of measures, home improvements
contractors, energy efficiency programs, and homes), identify investment opportunities, and precisely quantify and project
savings from energy efficiency investments. 

To facilitate communication and the exchange of information and data on residential building and energy performance, the
Building Performance Institute (BPI), a nonprofit standards setting organization, developed and published the HPXML Data
Dictionary and the HPXML Transfer Standard. 

The HPXML Data Dictionary defines terms related to the physical attributes and performance of buildings and measures. It
provides a common vocabulary for the residential energy efficiency industry and the data standard also defines several standard
datasets that can be used to describe specific use cases, for example, information collected during the completion of a whole
-house program. 

The HPXML Transfer Standard provides requirements for an extensible mark-up language (XML) data transfer protocol that can be
used to transfer information related to energy efficiency upgrades between different software systems. The transfer standard is
the companion standard to the HPXML data dictionary. Each of the data elements defined in the data dictionary can be
transferred using HPXML.


.. figure:: /images/existing_connections.png
    :figwidth: 4.5in
    :align: center

    Figure 1: Existing Market Conditions

.. figure:: /images/hpxml_connected_market.png
    :figwidth: 4.5in
    :align: center

    Figure 2: Connected Market

Value of HPXML
**************

HPXML allows home improvement contractors to easily exchange data with partnering businesses, energy efficiency programs, the real 
estate market and the financial sector. Many of the energy efficiency programs that have adopted HPXML, including the New York State 
Energy Research and Development Authority (NYSERDA), Energy Upgrade California, and Arizona Public Service (APS) have been able to 
reduce implementation costs through the automated validation of standardized data. For example, APS was able to decrease its 

While there are many uses for HPXML, we believe these can be framed as four categories:

    * Reduce program administrative and implementation costs. HPXML enables access to the same, well understood terms and data structures that are used for data retrieval, driving economies of scale in the administration, finance, and evaluation of energy efficiency programs. HPXML also enables the reuse of data and software for multiple purposes, which guards against software obsolesce and vendor lock-in, boosting innovation in software development. 
    * Support high quality research.
    * Support more precise savings calculations.
    * Make energy efficiency visible in the real estate transaction.

Standards Development
*********************

HPXML is developed by a working group of industry experts under the Building Performance Institute Data and Modeling Standards
Technical Committee. The HPXML working group is comprised of organizations and individuals from residential energy efficiency
programs, software development, government, and the nonprofit sector. Members are responsible developing and managing the HPXML Data
Dictionary and the HPXML Transfer Standard. The working group meets quarterly to discuss updates and vote on new version releases. 

HPXML is developed through a consensus-based approach and comments from all stakeholders are taken into account. If you are 
interested in joining the working group, contact hpxml@homeperformance.org. 

HPXML Compliance
****************

Compliance with HPXML requires that stakeholders use HPXML data in all cases in which an HPXML data element is sufficient to 
adequately represent the person, characteristic, concept or other home-related datum. Data can be “adequately represented” by HPXML 
if HPXML data elements, singly or in combination, provide a representation of the thing or person to be described that a) could 
reasonably be understood by other energy efficiency professionals, and b) does not result in significant loss of information or 
create significant risks of miscommunication.

For example, using a non-HPXML data element entitled “Number of Panes” to describe the number of layers of glass in a window would 
not be HPXML-compliant because the HPXML element “Number of Layers” could be used. In the context of a description of a window, this 
would be understood by energy efficiency professionals and would not result in miscommunication.

Software developers may test their tool's compliance with HPXML by uploading files to the HPXML validator. Example HPXML files are 
also available on Github. More information on the HPXML validator can be found in the section for Software Developers.

Alignment with Industry Standards
*********************************

To facilitate communication with a wide range of market actors in related industries, HPXML is aligned with the Department of 
Energy’s (DOE) Building Energy Data Exchange Specification (BEDES) and with the Real Estate Standards Organization's (RESO) Data 
Dictionary.

BEDES is a dictionary of terms, definitions, and field formats created to facilitate the exchange of information on building 
characteristics and energy use for the commercial, multifamily and residential industries. It is intended to be used in tools and 
activities that help stakeholders make energy investment decisions, track building performance, and implement energy-efficient 
policies and programs. Residential terms that appear both in BEDES and HPXML are aligned.

The Real Estate Standards Organization (RESO) Data Dictionary standardizes fields, enumerations, and definitions for hundreds of 
multiple listing services (MLS) nationwide. The RESO Dictionary contains a number of fields and enumerations that can be used to 
characterize energy-related improvements to the home. Because these fields are standardized and aligned with HPXML, realtors can 
provide homebuyers with access to consistent, comparable information about energy efficiency features in existing homes, which will 
make energy efficiency visibile in the real estate transaction.

Continued Growth
****************

The HPXML Data Dictionary is designed to grow with the industry. If you have recommendations for adding new or changing
existing data elements or enumerations, create a new issue on the Github repository or send an email to hpxml@homeperformance.org 
with the following information.

    * Name: Create a name for the data element or enumeration you feel best describes the term.
    * Definition: Write a comprehensive definition of the data element and include references if necessary.
    * Data Type: Include your recommended data type and maximum field length.
    * Enumerations: If your recommended field is a pick-list, please include enumerations. Enumerations may also need a definition.
    * Justification: Please provide a reason the data element is important to your energy efficiency program or market.
    * Duplication: Review the dictionary thoroughly to ensure you are not duplicating an already existing data element or enumeration. Concepts can be expressed in a number of ways and rather than adding additional data elements or enumerations, we can use this recommendation to better define existing elements.

How to Use the Implementation Guide
***********************************

The HPXML Implementation Guide was created by Home Performance with ENERGY STAR® to help program administrators and software 
developers integrate HPXML into their operations and products. This guide is divided into two sections: one section is tailored to 
program administrators and the other section is tailored to software developers. 

HPXML is periodically updated to reflect changes in the needs of the market and the stakeholders that adopt the standard. Whenever a 
new version of HXPML is released, the Guide will be updated to reflect changes to the data standard and how it is being used in the 
market.

For more information on HPXML, visit www.hpxmlonline.com. 
