.. _step3:

Step 3: Identify Your Data Needs
################################

.. contents::

BPI-2200 defines a long list of data elements, many of which you may not need
for your project. To determine which data points that you need, it is important
to start with the responses that you came up with in Step 1. The goal of this
exercise is to identify the minimum data collection requirements you need to
meet your project goals. This means identifying what must be collected in the
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

BPI is completing development of standard data sets for use cases (1), (2), (3),
(4) and (5) above, and will develop standard data sets for the other use cases
in the future. 

The standard audit and retrofit data sets are data collection and transfer
requirements that were created by existing HPXML adopters to facilitate the
transfer of project data from third-party energy modeling tools to a program
management database. As a collaboration between Home Performance programs in
Arizona, California, New York, Vermont, and Virginia, the standard use cases
are well suited for a wide range of program types, climate zones, and
implementation models.

Although these standards are being developed for Home Performance with ENERGY
STAR or whole house programs, they they can be used by other types of programs
as well. 

Even if you are not implementing a whole home program, these use cases are still
a great place to start as numerous software vendors are already able to
transfer the data required in these use cases. Any subset of data within these
use cases will be easy to implement for existing HPXML-compliant tools. 

The standard use cases also represent the required fields that implementation
partners have agreed to transfer to date. These data points have been
identified by the BPI WG-5 as sufficient and achievable as data collection
requirements for third-party energy modeling tools. The BPI data standards
support the collection and transfer of additional data points beyond these use
cases. However, additional data may require substantive changes on behalf of
the software vendors. Program administrators should  recognize the financial
impacts of custom data collection requests and consider providing financial
assistance to software vendors to meet any customization requests, as
appropriate.  

Before reviewing the standard use cases, there are several best practices to
consider.

Data Selection Best Practices
*****************************

Be Transparent with Stakeholders
================================

Especially with your contractors and software
vendors. By identifying your program needs early in the processes, stakeholders
can make you aware of potential challenges that may arise later.

Be Aware of Data Collection Burden
==================================

When selecting data requirements, programs tend to err on the side of more data
being better. It is important to remember that every data point required by the
program, costs contractor time and money to collect.  Similarly software
vendors not only incur costs to code to custom data point, but some data point
might significantly outside the scope of data that modeling tool needs to
collect to effective complete a energy simulation. So try to collect only what
you really needed and if you have data points that are unique to your program,
it may make sense to collect those data points directly in your program
management system or through an alternate data collection method. 

Leverage data choices made by other program sponsors
====================================================

HPXML is easily extensible and therefore can be customized to the very specific
needs of a program.  But program sponsors need to remember that they are not
the only member of the data management system.  When a program is using a data
specification to collect data, too much customization for a program pushes the
development costs of automation of the data collection process for that
specific program onto other parties (software tool vendors and service
providers).  Working with HPXML is best executed in coordination with other
program sponsors to minimize the number of program specific  data fields
required.  This will reduce costs for tool vendors, speed up the software
approval process, and make more tools available, for your program area,
increasing competition.

Schedule Updates to Data Requirements
=====================================

Software developers tend to work in phases to control releases of their
software. It is important to set a specification that software vendors need to
meet and schedule regular updates once or twice a year. Constantly changing the
requirements as you find issues can generate frustration, add costs, and create
challenges in software versioning control. Be as regimented as you can with a
scheduled iterative process.

Recognize the Diverse Uses for Your Data
========================================

Make sure that you are identifying all uses in the planning phase, so you can
try to reduce the need to make significant  changes to the data requirements
later on.  This can include uses such as:

* Quality assurance
* Verification of incentive eligibility or financing
* Marketing
* Measurement and evaluation
* Energy efficiency planning
* Real estate valuation

Adopting all of these best practices should assist you in establishing a
streamlined data selection process.

.. _datatool:

Standard Data Set Reviewing Tool
********************************

To assist program administrators in reviewing the standard use cases, we have
developed a data set reviewing tool that helps identify what data points are
currently required by these use cases.  Remember, if you don't see a data point
you're looking for in the use cases, it can be added to meet your program's
needs.

The Standard Data Set Reviewing Tool is available here

Understanding the HPXML Data Structure
**************************************

In the reviewing tool you will notice the following descriptors for each data
point:

Data Category 
    A general description of the information at the building characteristic
    or contact information level. Note: Insulation has several data categories,
    depending on the insulating plane. For example, are you referring to
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

Setting the Data Requirement Level for Your Program
***************************************************

As the program administrator, your main task in this step is to determine the
data element "requirement level."  In each of the use cases, you will find
three requirement levels:

Required
    It is mandatory to collect and transfer this data point with every
    project. This usually is driven by rebate qualifications or quality
    assurance requirements.
Required if Present   
    It is mandatory to collect and transfer if the condition exists in the
    house, but the condition might not be there in every case. For example,
    combustion safety is required only if gas appliance exists in the home.
Optional
    Not required by your program.

The :ref:`datatool` will allow you to see the minimum required fields that have
been agreed upon by BPI WG-5. In addition, you can use the Home Energy Score
and BPI – 2101 compliant toggles. By activating these toggles, you can see
which fields would be required if you wanted to complete a Home Energy Score or
fill out a BPI-2101 real estate certificate.

The fields that are grayed out are optional and represent fields that are
relevant in many jurisdictions, but not required. You can choose to make
optional fields required in your jurisdiction. However, it is important to note
that not all software products on the market collect every possible data point.
By making some of these data points "required" it may restrict which products
are eligible to participate or require you to provide financial assistance to
software vendors to code their software to to this requirement.  So it is
important to communicate with potential software vendors and make sure to
collect their feedback on which fields you require for your jurisdiction. BPI
WG -5 can help facilitate that conversation in a constructive environment.

Some programs with a large number of measurement-specific rebates are choosing
to use the optional feature in a different way. Your program can use a minimum
standard that is required for every home. However, if the contractor or
software vendor wants to participate in the full spectrum of rebates, they can
choose to send "optional" fields that trigger a rebate payment. This allow a
diverse set of software products and contractor business models to participate,
without having to be able to do everything the program may able to offer. If
you want to choose this path, it will be important to provide clear
specifications on which "optional" fields will trigger which rebate payments.

Definitions for Standard Data Sets
**********************************

Audit Use Case
==============

The audit use case is designed for Home Performance with ENERGY STAR or whole
house programs that complete comprehensive energy audits. This use case allows
auditors to submit their audit results and proposed scope of work for an
eligibility review from the program. Required fields are established to help
identify the home's existing characteristics, health and safety needs,
recommended improvements, and associated savings predictions. 

An example of an audit use case HPXML file can be found on the
`HPXML GitHub repository <https://github.com/hpxmlwg/hpxml/tree/hpxmlguide/examples>`_
and more technical description of the audit and retrofit use case can be found
in the software developer guide at :ref:`auditretrofitusecase`.

Retrofit Use Case
=================

The retrofit use case is designed to facilitate the transfer of complete home
performance with ENERGY STAR or whole house retrofit projects. This includes
the pre-retrofit condition of the home and a description of the installed
measures, as well as associated predicted savings. Required fields are
established to complete a full quality assurance review of all installed
measures and determine rebate or financing eligibility. The minimum
requirements reflect those most common between all of the HPXML programs so
far. Programs that offer more diverse rebates may need to consider changing
"optional" fields to "required" in order to meet program needs.

The retrofit use case HPXML file is very similar to the audit use case. The
differences are detailed in :ref:`auditretrofitusecase`. 

Other Use Cases
===============

The standard use cases provided as a part of this guide are two primary use
cases that have been developed to date.  We are also developing standard use
cases that identify the data points need for both BPI-2101 certificate of
completion and the required data points to complete a DOE's HESorce. Each use
case only uses a fraction of the HPXML standards. Over time, more use cases
will be developed to meet market needs.

A full list of HPXML data elements that can currently be incorporated into use
cases is available in the
`online schema documentation <http://hpxmlwg.github.io/hpxml/schemadoc/hpxml-2.0.0/index.html>`_.

How to Add Data Elements
************************

As you review the data sets and identify the fields that are required for your
implementation, it is not uncommon to identify a data point you require that
are not in one of the use cases or the HPXML standards as a whole. If this is
the case, BPI WG-5 can assist in adding the new data element and in identifying
how to incorporate them into the standard.   In some cases this might include
added new elements to the standard to account for data points that could be
applicable across many jurisdictions.  However, if the data point is truly
unique to your program, WG-5 has also introduced "measure codes" that allow us
to assign a code for a specific measure in a specific program.  This created
added flexibility without needing to modify the standards in all cases.

To submit a new data element for consideration, you can use the WG-5 github
account.  This way all members can see your recommendations and address them
immediately.  Follow the steps below to submit additional requests if needed:

#. If you have not already, sign up for a user account on
   `GitHub <https://github.com>`_.
#. Go to the
   `HPXML GitHub issues page <https://github.com/hpxmlwg/hpxml/issues/>`_.
#. Click "New Issue"
#. Fill out the form to ask your question or make your request. No need to assign a person or milestone.
#. Check the appropriate labels: probably "docs" and "enhancement" or "bug".
#. Click "Submit New Issue".

Once you have defined the use case you need for your jurisdiction and have
identified all required fields, you are ready to proceed to the next step. 
Remember, this can be an iterative process. It is good to do your due diligence
in the planning process. However, even the best implementation plans will need
to be modified as you get the program to market and start running a large
number of homes through it. Make sure to schedule opportunities later in your
implementation to check in on data requirements and adjust as needed.



