.. _step3:

Step 3: Identify Data Needs
################################

.. todo::

    CAROLINE SHOULD REVIEW THIS SECTION FOR TONE ONCE REVISED

.. contents::

BPI-2200 defines a long list of data elements, many of which may not be needed
for your project. To determine which data points are needed, it is important
to start with the responses received in Step 1. The goal of this
exercise is to identify the minimum data collection requirements needed to
meet project goals. This means identifying what must be collected in the
field, what must be transferred to your program management system, and what you
are transferring/reporting to others, when applicable. The good news is that
BPI WG-5 has coordinated with multiple programs across the country to develop
standard use cases that can serve as a great starting point for most programs.

Standard Data Sets Developed by BPI WG-5
****************************************

When exporting or importing data with third-party data systems, it is important
to develop a concise set of data requirements. As stated above, the BPI data
standards are capable of describing and transferring a large universe of data,
only a portion of which is needed for any one use case. To facilitate
efficiencies between programs, BPI is in the process of developing standard
data sets, each of which is associated with a specific use case. Use cases
(defined here as a set of interactions designed to achieve a specific function
within an energy efficiency program) that BPI WG-5 has identified as
particularly important for energy-efficiency programs include:

#. Reporting on the baseline conditions of a home and proposed improvements
#. Reporting on the improvements to the home compared to baseline conditions
#. Reporting on health and safety testing
#. Reviewing a contractor's work as part of a QA process
#. Reporting a home's energy efficiency assets to the parties in real estate transactions
#. Reporting data on program activity to DOE and other agencies

The standard audit and upgrade data sets are data collection and transfer
requirements that were created by existing HPXML adopters to facilitate the
transfer of project data from third-party energy modeling tools to a program
management database. As a collaboration between Home Performance with ENERGY STAR programs in
Arizona, California, New York, Vermont, and Virginia, the standard use cases
are well suited for a wide range of program types, climate zones, and
implementation models.

Although these standards are being developed for Home Performance with ENERGY
STAR or whole house programs, they can be used by other types of programs
as well. 

Even if implementation is not for a whole home program, these use cases are still
a great place to start, as several software vendors are already able to
transfer the data required in these use cases. Any subset of data within these
use cases will be easy to implement for existing HPXML-compliant tools. 

Standard use cases also represent the required fields that implementation
partners have agreed to transfer to date. These data points have been
identified by the BPI WG-5 as sufficient and achievable as data collection
requirements for third-party energy modeling tools. The BPI data standards
support the collection and transfer of additional data points beyond these use
cases. However, additional data may require software vendors to make substantive changes. Program administrators should recognize the financial
impacts of custom data collection requests and consider providing financial
assistance to software vendors to meet any customization requests, as
appropriate.  

Before reviewing the standard use cases, there are several best practices to
consider.

Data Selection Best Practices
*****************************

Be Transparent with Stakeholders
================================

It is especially important to be transparent with your contractors and software
vendors. By identifying your program needs early in the process, stakeholders
can make you aware of potential challenges that may arise later.

Be Aware of Data Collection Burden
==================================

When selecting data requirements, all programs collect a prudent amount of data for program compliance and measurement and verification of results.  When choosing what data points are mandatory for your programs, it is important to remember that every data point collected has a costs contractors to collect.  Similarly, software
vendors not only incur costs to code to custom data points, but some data points
might fall significantly outside the scope of data that a modeling tools need to
collect to effectively complete an energy simulation.  Thus, it is important to collaborative with your evaluators, contractors and software vendors to identify data sets that are consistent to that being done in other programs across the country and meet the need of the program as cost efficiently as possible.   

Leverage data choices made by other Program Sponsors
====================================================

HPXML is easily extensible and therefore can be customized to the specific
needs of a program.  That said, Program Sponsors should first look at the data sets being implemented by other program around the country. When a program is using a
specification to collect data, too much customization can push significant development costs of automation of the data collection process for that specific program onto other parties (software tool vendors and service
providers).  To streamline implementation and best leverage efforts from other programs it is best to coordination with other
Program Sponsors to minimize the number of program-specific data fields
required in your jurisdiction.  This can help reduce costs for tool vendors, speed up the software
approval process, and make more tools available for program areas.

Schedule Updates to Data Requirements
=====================================

Software developers tend to work in phases to control releases of their
software. It is important to specify that software vendors need to
meet and schedule regular updates once or twice a year. Constantly changing the
requirements as issues are found can generate frustration, add costs, and create
challenges in software version control. Be as regimented as possible with a
scheduled iterative process.

Recognize the Diverse Uses for Your Data
========================================

Be sure to identify all uses in the planning phase
to reduce the need to make significant changes to the data requirements
later.  This can include uses such as:

* Quality assurance
* Verification of energy savings, incentive eligibility or financing
* Marketing
* Measurement and evaluation
* Energy efficiency planning
* Real estate valuation

Adopting all of these best practices will assist in establishing a
streamlined data selection process.

.. _datatool:

Standard Data Set Reviewing Tool
********************************

To assist program administrators in reviewing the standard use cases,
a data set reviewing tool was developed that helps identify what data points are
currently required by these use cases.  Remember, if a data point
is not in the use cases, it can be added to meet the program's
needs.

The Standard Data Set Reviewing Tool is available here

.. todo::

    Need to include the Excel spreadsheet tool.

Understanding the HPXML Data Structure
**************************************

In the reviewing tool, notice the following descriptors for each data
point:

Data Category 
    A general description of the information at the building characteristic
    or contact information level. Note: Insulation has several data categories,
    depending on the insulating plane. For example, referencing
    insulation installed on the attic floor "Attic Floor Insulation" or on the
    bottom of the roof deck "Attic Roof Insulation."
Data Element 
    A specific data point or descriptor within that data category. For
    example, insulation material type or R-value.
Data Type 
    How the data should be provided. For example, as a number, text,
    enumeration, etc.
Definition
    A written description of the data point and what it means.

It is important to note that, in most cases, there are several data points
needed to describe any one building characteristic. For example, if you require
blower door testing in your program, you will require "Air Infiltration"
information. In this case, there are three data points that are required to
describe an air leakage measurement, such as 2000 CFM\ :sub:`50`:

    "Building Air Leakage" = 2000

    "Building Air Leakage Unit" = CFM

    "House Pressure" = 50  

This also provides flexibility to receive the same data in multiple formats. For
example, air leakage could be represented in CFM50, ACH or ACH50.

Setting the Program's Data Requirement Level
********************************************

The program administrator's main task in this step is to determine the
data element "requirement level."  In each of the use cases, there are
three requirement levels:

Required
    It is mandatory to collect and transfer this data point with every
    project. This usually is driven by rebate qualifications or quality
    assurance requirements.
Required if Present   
    It is mandatory to collect and transfer if the condition exists in the
    house, but the condition might not be there in every case. For example,
    combustion safety is required only if a gas appliance exists in the home.
Optional
    Not required.

The :ref:`datatool` will allow you to see the minimum required fields that have
been agreed upon by BPI WG-5. In addition, you can use the Home Energy Score
and BPI – 2101 requirement toggles. By activating these toggles, you can see
which fields would be required if you wanted to complete a Home Energy Score or
fill out a BPI-2101 Home Performance Certificate of Completion.

The grayed out fields are optional and represent fields that are
relevant in many programs, but not required. You can choose to make
optional fields required in your program. However, it is important to note
that not all software products on the market collect every possible data point.
Making some of these data points "required" may restrict which products
are eligible to participate, or may require you to pay software vendors to code their software for this requirement.  So it is
important to communicate with potential software vendors and make sure to
collect their feedback on which fields you require for your program before determining your final data requirements. BPI
WG-5 can help facilitate that conversation in a constructive environment.

Some programs with a large number of measure-specific rebates are choosing
to identify data points as "optional" to allow flexibility in implementation. Your program can use a minimum
data collection standard that is required for every home. However, if the contractor or
software vendor wants to participate in the full spectrum of rebates, they can
choose to send "optional" fields that trigger a rebate payment. This allows a
diverse set of software products and contractor business models to participate,
without mandating that every software and contractor support the full spectrum of rebates your program portfolio may offer. If you want to choose this path, it will be important to provide clear
specifications on which "optional" fields will trigger which rebate payments.

Definitions for Standard Data Sets
**********************************

Audit Use Case
==============

The audit use case is designed for Home Performance with ENERGY STAR or whole
house programs that require energy audits. This use case allows
auditors to submit their audit results and proposed scope of work for an
eligibility review from the program. Required fields are established to help
identify the home's existing characteristics, health and safety needs,
recommended improvements, and associated savings predictions. 

An example of an audit use case HPXML file can be found on the
`HPXML GitHub repository <https://github.com/hpxmlwg/hpxml/tree/hpxmlguide/examples>`_
and more technical description of the audit and upgrade use case can be found
in the software developer guide at :doc:`/software_developer/usecases/auditupgrade`.

Upgrade Use Case
================

The upgrade use case is designed to facilitate the transfer of completed home
performance with ENERGY STAR or whole house upgrade projects. This includes
the pre-upgrade condition of the home and a description of the installed
measures, as well as associated predicted savings. Required fields are
established to complete a full quality assurance review of all installed
measures and determine rebate or financing eligibility. The minimum
requirements reflect those most common between all of the HPXML-compliant programs so
far. Programs that offer more diverse rebates may need to consider changing
"optional" fields to "required" in order to meet program needs.

The upgrade use case HPXML file is very similar to the audit use case. The
differences are detailed in :doc:`/software_developer/usecases/auditupgrade`. 

Home Energy Score Use Cases
===========================

The Home Energy Score use case defines the minimum data set required by the DOE's Home Energy Score tool, in order to properly generate the 1 to 10 score.  These data point are clearly identified in the data selection tool.  Programs interested in generating a Home Energy Score, will need to make sure that their HPXML software tool are collecting this minimum dataset. 

In order to generate the score, your program software team will also need to integrate with the DOE's Home Energy Score API. HPXML can be transferred through the API and generate a Home Energy Scores in real time. For more information on integration with the Home Energy Score API, see :doc:`/software_developer/usecases/hescore` in the software developer guide. 

Other Use Cases
===============

The standard use cases provided as a part of this guide are two primary use
cases that have been developed to date.  Standard use
cases that identify the data points needed for both BPI-2101 certificate of
completion is in development. Each use case only uses a fraction of the data points that the HPXML standard can support. Over time, more use cases will be developed to meet market needs.

A full list of HPXML data elements that can currently be incorporated into use
cases is available in the
`online schema documentation <http://hpxmlwg.github.io/hpxml/schemadoc/hpxml-2.0.0/index.html>`_.

How to Add Data Elements
************************

As you review the data sets and identify the fields that are required for
implementation, it is possible to identify a data point you require that
is not in one of the pre-defined use cases or the HPXML standards as a whole. If this is
the case, BPI WG-5 can assist in adding the new data element and in identifying
how to incorporate it into the standard. In some cases this might include
adding new elements to the standard to account for data points that could be
applicable across many programs.  However, if the data point is truly
unique to your program, WG-5 has also introduced "measure codes" that allow
a code to be assigned for a specific measure in a specific program.  This creates
added flexibility without needing to modify the standards in all cases.

To submit a new data element for consideration, you can use the WG-5 github
account.  This way all members can see your recommendations and address them
immediately.  Follow the steps below to submit additional requests if needed:

#. Sign up for a user account on
   `GitHub <https://github.com>`_.
#. Go to the
   `HPXML GitHub issues page <https://github.com/hpxmlwg/hpxml/issues/>`_.
#. Click "New Issue"
#. Fill out the form to ask a question or make a request. No need to assign a person, milestone, or label.
#. Click "Submit New Issue".

Once you have defined the use case needed for your program and have
identified all required fields, you are ready to proceed to the next step. 
Remember, this can be an iterative process. It is good to do due diligence
in the planning process. However, even the best implementation plans will need
to be modified as the program goes to market and a large
number of homes start running through it. 

.. note::

    Make sure to schedule opportunities later in your
    implementation to check in on data requirements and adjust as needed.
