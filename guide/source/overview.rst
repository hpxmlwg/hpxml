.. include:: <isonum.txt>

Overview
########

The Need for Data Standardization
*********************************

In today’s existing homes market the electronic exchange of information on energy performance, energy conservation measures, and the physical and operational attributes of a home is often characterized by a lack of common terms, definitions, and two-way feedback systems (Figure 1). This limits the ability of decision-makers to access, aggregate, share and use data for the design and implementation of residential energy efficiency programs. This also makes it difficult for market actors to understand the drivers of variation in performance (e.g., of measures, contractors, programs, and homes), identify investment opportunities, analyze market trends, and project savings from energy efficiency investments. 

Data standards like the Home Performance Extensible Markup Language (HPXML) make it easier and quicker to exchange information and data on residential building and energy performance. 


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

HPXML is comprised of two Building Performance Institute (BPI) data standards that were published in 2013 to support a growing industry by facilitating communication and the exchange of information and data on residential building and energy performance.

The HPXML Data Dictionary (BPI-2200) standardizes terms and field formats related to the physical attributes and performance of buildings and measures. It defines the data elements necessary to provide a general description of a whole house or single measure energy efficiency upgrade for reporting, rebate and basic quality assurance (QA) purposes. The standard also includes several standard datasets that can be used to describe specific use cases, for example, information collected during the completion of a whole-house program (see next section for more information).

The HPXML Transfer Standard (BPI-2100) provides requirements for a standard extensible mark-up language (XML) data transfer protocol that can be used to transfer information and data between different software systems. The transfer standard is the companion standard to the HPXML data dictionary. Each of the data elements defined in the data dictionary can be transferred using HPXML.

Together, the data dictionary and transfer standard benefit a growing industry by:

    * Standardizing terminology and facilitating the collection of higher quality data as a means of tracking and quantifying the work being completed across the residential energy efficiency industry;

    * Creating interoperability between software systems to allow the transfer of residential energy efficiency data across a diverse set of market actors; and,

    * Improving industry efficiency by reducing the costs of data collection and exchange between market actors.

As the number of stakeholders using HPXML increases, the costs of collecting and sharing information will decrease, enabling programs and other stakeholders to deliver better information to decision-makers at a lower cost. The ability to aggregate, share and use building and energy performance data will create new opportunities in the valuation of energy efficiency.

Benefits
********

Adoption of HPXML is voluntary, but there are significant benefits for those who adopt the data standards, including:

    * Reduced Costs - HPXML can help programs and contractors reduce costs significantly by facilitating off-the-shelf software solutions for automated reporting, project review, incentive processing, and quality assurance. Programs that have adopted these automated review and verification processes have been able to accelerate project approval, reduce errors, and free up staff time for more valuable projects. Having a standard data format also means software developers do not have to re-invent the wheel for their clients, making it cheaper and faster for programs to adopt new software, and void vendor lock-in and associated problems such as software obsolescence.

    * Increased Interoperability - HPXML is aligned with the Department of Energy's Building Energy Data Exchange Specification (BEDES) and with the Real Estate Standards Organization's Data Dictionary. This alignment makes it possible for industry stakeholders to cost-effectively exchange information within and across sectors, for example, between programs and the real estate industry or financial sector. Programs using HPXML can also generate a Home Energy Score through the Department of Energy’s HPXML-compliant Application Program Interface (API). 

    * High Quality Research and Improved Analytics - The aggregation of standardized data supports comparability and enables cost-effective research on the benefits of residential energy upgrades. With HPXML, programs can complete comprehensive, ongoing analysis of program and contractor performance, and identify participation and performance trends over time.

Standards Development
*********************

HPXML is managed by a working group of industry experts under the Building Performance Institute Data and Modeling Standards Technical Committee. The HPXML working group is comprised of organizations and individuals from residential energy efficiency programs, software development, government, and the nonprofit sector. Members are responsible developing and managing the HPXML Data Dictionary and the Transfer Standard. The working group meets quarterly to discuss updates and vote on new versions of the standards. 

If you are interested in joining the working group, sign up through the HPXML website. 

HPXML Compliance
****************

Stakeholders that wish to comply with the HPXML Data Dictionary and Transfer Standard shall use HPXML data in all cases in which an HPXML data element is sufficient to adequately represent the person, characteristic, concept or other home-related datum that is being described.

Data can be adequately represented by HPXML if HPXML data elements, singly or in combination, can be used to describe the person or thing in a way that a) could reasonably be understood by other energy efficiency professionals, and b) does not result in significant loss of information or create significant risks of miscommunication.

Software developers may validate their HPXML files against the schema and its datasets by uploading files to the HPXML validator. Example HPXML files are available on Github. 

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

The HPXML Implementation Guide helps program administrators and software developers integrate HPXML into their operations and products. This guide is divided into two sections that are tailored to specific audiences. 

    * The Program Administrator Guide discusses the benefits of HPXML adoption and walks administrators through the process of goal setting, identifying data needs, data validation, testing, and quality management.
    
    * The Software Developer Guide provides developers with information on versioning, document structure, XML element references, and use case validation. The section also provides links to sample HPXML files.

HPXML is periodically updated to reflect changes in the needs of the market and the stakeholders that adopt the standard. Whenever a 
new version of HXPML is released, the Guide will be updated to reflect changes to the data standard and how it is being used in the 
market.

For more information on HPXML, visit www.hpxmlonline.com. 
