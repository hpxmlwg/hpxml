.. include:: <isonum.txt>

Overview of HPXML
#################

The Need for Data Standardization
*********************************

In today’s existing homes market the electronic exchange of information on energy performance, energy conservation measures, and the physical and operational attributes of a home is often characterized by a lack of common terms, definitions, and two-way feedback systems (Figure 1). This limits the ability of decision-makers to access, aggregate, share and use data for the design and implementation of residential energy efficiency programs. This also makes it difficult for market actors to understand the drivers of variation in performance (e.g., of measures, contractors, programs, and homes), identify investment opportunities, analyze market trends, and project savings from energy efficiency investments. 

Data standards like the Home Performance Extensible Markup Language (HPXML) are a powerful solution to some of the most intractable problems facing the residential energy efficiency industry, for example, the high program delivery and administrative costs for programs and contractors. Data standards are crucial for ensuring that energy efficiency improvements in homes are properly valued in real estate transactions. Data standards are also crucial in enabling the quantification of the energy savings that result from energy efficiency upgrades, which in turn will allow for savings guarantees, low-cost consumer finance, and the sale of energy efficiency into energy, capacity and carbon markets. Finally, data standards are crucial for on-going research into the best methods for making homes energy efficient because the aggregation of standardized data supports comparability and comprehensive, ongoing analysis of program and contractor performance.


.. figure:: /images/existing_connections.png
    :figwidth: 3in
    :align: center

    Figure 1: Existing Market Conditions



.. figure:: /images/hpxml_connected_market.png
    :figwidth: 3in
    :align: center

    Figure 2: Connected Market



Value of HPXML
**************

HPXML is comprised of two Building Performance Institute (BPI) data standards that were published in 2013 to support a growing industry by facilitating communication and the exchange of information and data on residential building and energy performance. 

The HPXML Data Dictionary (BPI-2200) standardizes terms and field formats related to the physical attributes and performance of buildings and measures. It defines the data elements necessary to provide a general description of a whole house or single measure energy efficiency upgrade for reporting, rebate and basic quality assurance (QA) purposes. The standard also includes several smaller datasets that are being used to standardize reporting for specific use cases, for example, data required at the completion of a whole-house program (see next section for more information).

The HPXML Transfer Standard (BPI-2100) provides requirements for a standard extensible mark-up language (XML) data transfer protocol that can be used to transfer information and data between different software systems. The transfer standard is the companion standard to the HPXML data dictionary. Each of the data elements defined in the data dictionary can be transferred using HPXML.

Together, the data dictionary and transfer standard benefit a growing industry by:

    * Standardizing terminology and facilitating the collection of higher quality data as a means of tracking and quantifying work being completed across the residential energy efficiency industry;

    * Creating interoperability between software systems to allow the transfer of residential energy efficiency data across a diverse set of market actors, such as the real estate and financial sectors; and,

    * Improving industry efficiency by reducing the costs of data collection and exchange between market actors.

Programs that have adopted HPXML have been able to reduce costs by facilitating software solutions for automated reporting, project review, incentive processing, and quality assurance. Programs that have adopted these automated review and verification processes have seen accelerated project approval, reduced errors, and freed up staff time for other more valuable projects. For example, one year after implementing HPXML, Arizona Public Service's Home Performance with ENERGY STAR program acheived:

    * 50% increase in contractor satisfaction after the launch of an HPXML-based software encironment;
    * 31% decrease per project in contractor administrative labor following the implementation of a more streamlined online reporting, rebate approval, and QA process; and,
    * 50% decrease in quality assurance administrative labor following implementation of the new software environment.

Software vendors that have adopted HPXML are developing off-the-shelf solutions for programs and contractors, making it significantly cheaper and faster to adopt new software. Adoption of the national data standard can help programs avoid vendor lock-in and associated problems such as software obsolescence.

Data standards, like all other standards, are more valuable the more broadly they are used. Every time a program implements a data standard, transactional costs fall for firms already using the standard. Software vendors can provide a rich set of data about a whole-house upgrade to programs using HPXML at very little additional cost because they have already made the initial investment to design their software to support the data standards. For the energy efficiency industry to realize the full benefit of the BPI data standards, it is crucial that more programs and other users adopt the standards.

Alignment with Industry Standards
*********************************

To facilitate communication with a wide range of market actors in related industries, HPXML is aligned with the Department of Energy’s (DOE) Building Energy Data Exchange Specification (BEDES). BEDES is a taxonomy of terms, definitions, and field formats created to facilitate the exchange of information on building characteristics and energy use for the commercial, multifamily and residential industries.

HPXML is currently the most widely used implementation of BEDES. Users of residential BEDES terms may adopt the standard HPXML schema to transfer information and data between software systems. This has the benefit of increasing the cost-effective transfer of residential energy efficiency data across a diverse set of market actors.

HPXML is also aligned with the Real Estate Standards Organization's (RESO) Data Dictionary, which standardizes terms used in hundreds of multiple listing services (MLS) and other source providers nationwide so that information can be easily shared and understood in the real estate industry, and with the Appraisal Institute's Green and Energy Efficient Addendum, which standardizes the communication of high performing features for appraisers, lenders, agents, and homeowners. 

Programs that adopt HPXML can swiftly and easily generate a BPI-2101-compliant Home Performance Certificate (described in next section), Home Energy Score, or other scores and labels, to introduce information about a home's energy efficient features into real estate transactions through the auto-population of MLS.

Standards Development
*********************

HPXML has been developed, and is modified and maintained, by the stakeholders who use them, including organizations and individuals from residential energy efficiency programs, software development, government, and the nonprofit sector. HPXML is managed by a working group of industry experts under the Building Performance Institute (BPI) Data and Modeling Standards Technical Committee using an open and consensus based decision-making process set by the BPI. The working group meets quarterly to discuss updates and to vote on new versions of the standards. 

If you are interested in joining the working group, sign up through www.hpxmlonline.com. 

HPXML Compliance
****************

Stakeholders that wish to comply with the HPXML Data Dictionary and Transfer Standard shall use HPXML data in all cases in which an HPXML data element is sufficient to adequately represent the person, characteristic, concept or other home-related datum that is being described.

Data can be adequately represented by HPXML if HPXML data elements, singly or in combination, can be used to describe the person or thing in a way that a) could reasonably be understood by other energy efficiency professionals, and b) does not result in significant loss of information or create significant risks of miscommunication.

Software developers may validate their HPXML files against the schema and its datasets by uploading files to the HPXML Validator. Example HPXML files are also available on Github. 

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
