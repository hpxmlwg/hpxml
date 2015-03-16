.. include:: <isonum.txt>

Introduction
############

An organized group of members of the home performance community with the support
of the private, utility, and public sectors, conceived of and developed the
Building Performance Institute's (BPI) BPI-2100 and BPI-2200 data standards
commonly referred to as ("HPXML"). To expedite its deployment into the market,
Home Performance with ENERGY STAR\ |reg| developed this HPXML Implementation Guide to
help program administrators and software developers integrate HPXML into their
operations and products. Simply put, HPXML is a set of common definitions for
the attributes of the systems in a home and the computing language that
facilitates the quick and easy transfer of home-related data between different
market actors. Without HPXML, home improvement contractors cannot easily
exchange data with partnering businesses, energy efficiency programs, the real
estate market, or the financial sector.

As conveyed in Figure 1 below, today there is a fragmented, siloed marketplace
where exchange of data occurs but with non-uniform definitions for metrics and a
lack of for two-way feedback systems. Figure 2 represents a market where HPXML
has been successfully integrated which facilitates the easy exchange of data
between and among different market actors.  While each market actor would have
specific uses for some data, other data could be shared creating more value for
residential energy efficiency as a whole ultimately translating into greater
energy savings from a more efficient marketplace.

.. todo::

    Figure 1: Existing Market Conditions

.. todo::

    Figure 2: Connected Market

It is the expectation of the U.S. Department of Energy that expanded use of
HPXML will achieve the following:

    * Reduce time and cost of collecting and transferring home and
      energy-related data;
    * Foster new and strengthen existing organizational relationships within
      the residential supply chain;
    * Increase the transparency of energy efficiency work tto facilitate deeper
      market penetration of energy efficiency products and services;
    * Enhance ability to quantify energy savings through standardized,
      data-rich EM&V methods;
    * Improve the quality assurance systems and practices needed to efficiently
      support, measure and verify energy performance.

Significant effort has gone into the development of HPXML and this
Implementation Guide, but the work is not complete.  HPXML is constantly being
improved and this Implementation Guide will benefit from the lessons learned by
different organizations integrating HPXML into their operations.  If you have
questions about HPXML or believe you can contribute to the overall success of
its deployment, please email us at homeperformance@energystar.gov.  HPXML was
developed and deployed through a collaborative process, and we intend to
continue in that spirit to expand its execution and improvement.  

.. _what-are-the-bpi-standards:

What are the BPI Data Standards?
********************************

The BPI data standards are designed to help collect and transfer
information about the characteristics of residential buildings and upgrade projects.
This data can be shared with any party involved in a home performance or
energy-efficiency program, including contractors, program administrators,
utilities, federal agencies, and others. In addition, HPXML allows home performance data 
to be seamlessly shared with the financial, real estate, insurance, and other 
appropriate industries. This creates a standardized way to
collect project information and to share that information to facilitate market
growth.

The two primary data standards, `BPI-2100`_ and `BPI-2200`_ are closely related and
are used together to implement HPXML:

`BPI-2100-S-2013`_: Standard for Home Performance-Related Data Transfer
    provides requirements for an extensible mark-up language (XML) standard
    data transfer protocol that can be used to transfer home
    performance-related data.

`BPI-2200-S-2013`_: Standard for Home Performance-Related Data Collection
    provides a standard vocabulary for describing terms related to
    buildings, energy consumption, and energy conservation measures. Each of
    the data elements defined in BPI-2200 can be transferred using HPXML via
    the methodology outlined in BPI-2100.    

BPI will be developing additional data collection standards, of which
`BPI-2101-S-2013`_ has been completed. Each of these standards specifies a set
of data elements to be collected at specific points during the implementation of
an energy efficiency program (e.g. the audit, project completion, etc.). While
HPXML is capable of transferring a wide variety of data elements, any one
program or jurisdiction will only need a small sub-set in most cases. To
facilitate adoption of the data standards and to reduce variation between
jurisdictions, which can be costly for software providers and contractors, BPI
WG-5 in coordination with stakeholders from across the industry have started
developing the following data collection standards:

`BPI-2101-S-2013`_: Standard Requirements for a Certificate of Completion for Residential Energy Efficiency Upgrades
    This standard identifies a set of data elements for certificates that
    document the completion of a whole-house energy upgrade (HEU) and
    individual energy conservation measures (ECMs). The set of data elements
    required for inclusion in the certificate will provide a clear,
    easy-to-understand description of the HEU or ECMs, including information
    about major energy-related improvements implemented and, if relevant,
    predicted energy savings or other performance indicators. The certificate
    is designed to be used as a reference document by real estate agents,
    appraisers, and other professionals during the home sale process, and can
    be uploaded into Multiple Listing Service (MLS) databases. Home Performance
    with ENERGY STAR's Certificate of Completion template, available to Program
    Sponsors, complies with BPI-2101 to assure consistency of data elements.

Draft: Standard for Home Energy Auditing Data Collection with Energy Modeling Tools
    This draft standard represents the minimum data necessary for energy
    modeling tools to capture during an energy audit and transfer by HPXML to
    home performance programs. The standard is designed to promote
    consistency between programs and facilitate cost efficiency in the
    implementation of HPXML through alignment to a standardized specification.

Draft: Standard for Home Energy Job Completion Data Collection with Energy Modeling Tools
    This draft standard represents the minimum required data necessary to be
    captured by energy modeling or other data collection tools during a home energy upgrade
    and transfer by HPXML to home performance programs. The standard is
    designed to promote consistency between programs and facilitate cost
    efficiency in the implementation of HPXML through alignment to a
    standardized specification.

The Role of BPI Working Group 5
*******************************

BPI Working Group 5 (BPI WG-5) is a volunteer effort with representation from
program administrators, implementers, software developers, and government
agencies. The group is an official Building Performance Institute committee
tasked with developing and maintaining standards related to the collection and
transfer of energy efficiency and home performance-related data.  BPI WG-5 is
responsible for maintaining the standards, and it works to ensure that the
standards can meet the needs of various market actors.  As a program
administrator, you may want to familiarize yourself with this group, as they
can serve as an invaluable resource to assist in the implementation of the BPI
data standards, facilitate changes in the standard, and answer questions about
the standards. To contact the BPI WG-5 or to get involved, email them at
hpxml@homeperformance.org.

Data Standards and the U.S. DOE's Building Energy Data Exchange Specification (BEDES)
*************************************************************************************

The BPI data standards were developed to serve the single family residential
sector (i.e. 1-4 unit buildings). Since the creation of HPXML, and with shared
objectives, the US Department of Energy has begun the development of the
`Building Energy Data Exchange Specification`_, referred to as BEDES (pronounced
"beads" or /bi:ds/). BEDES is a dictionary of terms, definitions, and field
formats which was created to help facilitate the exchange of information on
building characteristics and energy use. It is intended to be used in tools and
activities that help stakeholders make energy investment decisions, track
building performance, and implement energy-efficient policies and programs.

Since the initiation of the BEDES effort, BPI WG-5 and representatives from the
DOE have coordinated efforts to maintain interoperability between the
two standards.  The primary difference between the two efforts is one of scope,
as the BPI data standards are designed for single-family residences, while
BEDES is designed to include all building types — both commercial and
residential.

For more information on visit the `BEDES website <Building Energy Data Exchange Specification_>`_.

.. _BPI-2100: http://www.bpi.org/tools_downloads.aspx?selectedTypeID=1&selectedID=141
.. _BPI-2200: http://www.bpi.org/tools_downloads.aspx?selectedTypeID=1&selectedID=142
.. _BPI-2100-S-2013: `BPI-2100`_
.. _BPI-2200-S-2013: `BPI-2200`_
.. _BPI-2101: http://www.bpi.org/tools_downloads.aspx?selectedTypeID=1&selectedID=143
.. _BPI-2101-S-2013: `BPI-2101`_
.. _Building Energy Data Exchange Specification: http://energy.gov/eere/buildings/building-energy-data-exchange-specification-bedes