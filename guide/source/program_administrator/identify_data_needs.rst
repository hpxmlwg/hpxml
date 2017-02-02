.. _step3:

Step 3: Identify Data Needs
###########################

.. contents::

One of the areas in which data standardization holds the greatest promise is in data collection and reporting. If different programs all agree to collect the same (or very similar) data for the same use cases, such as the data reported by the contractor when the initial audit is conducted or the final job and test-out results are reported, information technology costs could be reduced tremendously across the country because software vendors would be able to use the same reporting template, with only minor modifications, for multiple programs. Standard datasets will also greatly facilitate cross-program comparability, support research efforts and accurate quantification of savings for other uses.

BPI-2200 defines a long list of data elements, many of which may not be needed
for your project. To determine which data points are needed, start with the
responses you developed in :doc:`implementation_goals`. The goal of this
exercise is to identify the minimum data collection requirements needed to meet
project goals. This means identifying what must be collected in the field, what
must be transferred to your program management system, and what you are
transferring/reporting to others, when applicable. The good news is that BPI
WG-5 has coordinated with multiple programs across the country to develop
standard use cases that can serve as a great starting point for most programs.

Standard Data Sets Developed by BPI WG-5
****************************************

When exporting or importing data with third-party data systems, it is important
to develop a concise set of data requirements. As stated above, HPXML is capable of describing and transferring a large universe of data, but only a portion of data may be needed for any one use case (defined as a set of interactions designed to achieve a specific function within an energy efficiency program). For example,

#. Reporting on the baseline conditions of a home and proposed improvements
#. Reporting on the improvements to the home compared to baseline conditions
#. Reporting on health and safety testing
#. Reviewing a contractor's work as part of a QA process
#. Reporting a home's energy efficiency assets to the parties in real estate transactions
#. Reporting data on program activity to DOE and other agencies

The standard Audit and Upgrade datasets are data collection and transfer
requirements that were created by existing HPXML adopters to facilitate the
transfer of project data from third-party energy modeling tools to a program
management database. As a collaboration between Home Performance with ENERGY
STAR programs in Arizona, California, New York, Vermont, and Virginia, the
standard datasets are well suited for a wide range of program types, climate
zones, and implementation models.

Although these datasets were initially developed for Home Performance with ENERGY
STAR or whole house programs, they can be used by other types of programs as
well, such as weatherization or single measure programs.

Even if implementation is not for a whole home program, these datasets are
still a great place to start because software vendors are already able to
transfer the data required in these use cases. Any subset of data within these
use cases will be easy to implement for existing HPXML-compliant tools. 

Standard use cases also represent the required fields that implementation
partners have agreed to transfer to date. These data points have been identified
by the BPI WG-5 as sufficient and achievable as data collection requirements for
third-party energy modeling tools. The BPI data standards support the collection
and transfer of additional data points beyond these use cases. However,
additional data may require software vendors to make substantive changes to
their software. Program administrators should recognize the financial impacts of
custom data collection requests and consider providing financial assistance to
software vendors to meet any customization requests, as appropriate.  

Before reviewing the standard use cases, there are several best practices to
consider.

Data Selection Best Practices
*****************************

Be Transparent with Stakeholders
================================

Transparency with your contractors and software vendors throughout the process
will help guide programmatic decisions and prevent challenges down the road.
This is particularly true for the data selection process as  stakeholders can
bring attention to potential challenges that need resolution.  For example, a
program may request a specific data point that is not typically collected by
most software products.  If vendors can identify this need early on, a
resolution can be reached in the planning phase and not delay the project later
on.

Be Sensitive to Data Collection Burden
======================================

When selecting data requirements, programs should collect just enough data for
program compliance and measurement and verification of results. As a guiding
principle, Home Performance with ENERGY STAR recommends that programs employ
administrative procedures that minimize the burden of participation for
contractors and homeowners. When choosing what data points are mandatory for
your programs, it is important to recognize that every data point collected has
a cost to contractors to collect. Collaborate  with evaluators, contractors and
software vendors to explore solutions that meet the need of the program as cost
efficiently as possible.

Leverage data choices made by other Program Administrators
==========================================================

HPXML is easily extensible and therefore can be customized to the specific needs
of a program. That said, program administrator should look at the data sets
being implemented by other programs around the country as many software company
are already exporting and importing these standard data sets. When a program is
using unique data requirements, the associated customization can push
significant development costs for that specific program onto other parties, like
software tool vendors and service providers. To streamline implementation and
best leverage efforts from other programs it is encouraged to coordinate with
other program administrators to minimize the number of program-specific data
fields required in your jurisdiction. This guide provides a HPXML data selection
tool below to easily facilitate this coordination.

Schedule Updates to Data Requirements
=====================================

Software developers tend to work in phases to control releases of their
software. To avoid additional costs or confusion, try scheduling regular updates
once or twice a year and communicate future changes as early as possible. This
will help with version control and create more manageable process for software
vendors and your implementation team.

Adopting these best practices will assist in establishing a streamlined data
selection process.

.. _datatool:

HPXML Data Selection Tool
*************************

To assist program administrators in reviewing the standard use cases that are
being implemented by other programs, a data selection tool  is available to help
identify what data points are currently required in these use cases and helps
programs select and communicate the requirements for the program. The HPXML Data
Selection Tool is a "living document", so if a programs identifies data points
that are not in the use cases, WG-5 can assist in added them to the tool and
thus meet the program's needs.

   * Download: :download:`HPXML Data Selection Tool <hpxml_data_selection_tool.xlsx>`

The attached instructional video will provide a walkthrough of the HPXML data
selection tool.  Using the tool programs can quickly select the data required
for HPXML program implementation.  Programs can then forward the tool to the
implementation team, trade allies and software providers, giving them clear
guidance on the requirements  for HPXML Implementation with your program.

.. raw:: html

    <iframe width="640" height="360" src="https://www.youtube.com/embed/vmfU1ytzMfc" frameborder="0" allowfullscreen></iframe>

.. raw:: latex

    \par\href{https://youtu.be/vmfU1ytzMfc}{YouTube: HPXML Data Selection Tool Tutorial}\par

Additional details about the data structure and standard data sets are provided
in the sections below.

Understanding the HPXML Data Structure
**************************************

In the reviewing tool, notice the following descriptors for each data
point:

Data Category 
    A general description of the information at the building characteristic or
    contact information level. Note: Insulation has several data categories,
    depending on the insulating plane. For example, referencing insulation
    installed on the attic floor "Attic Floor Insulation" or on the bottom of
    the roof deck "Attic Roof Insulation."
Data Element 
    A specific data point or descriptor within that data category. For example,
    insulation material type or R-value.
Data Type 
    How the data should be provided. For example, as a number, text,
    enumeration, etc.
Definition
    A written description of the data point and what it means. As the name of
    the data point is not always clear, this provides a narrative explanation of
    what each data point describes.

In most cases, there are several data points needed to describe any one building
characteristic. For example, if you require blower door testing in your program,
you will require "Air Infiltration" information. In this case, there are three
data points that are required to describe an air leakage measurement, such as
2000 CFM\ :sub:`50`:

    "Building Air Leakage" = 2000

    "Building Air Leakage Unit" = CFM

    "House Pressure" = 50  

This also provides flexibility to receive the same data in multiple formats. For
example, air leakage could be represented in CFM50, ACH or ACH50.

Setting the Program's Data Requirement Level
********************************************

The program administrator's main task in this step is to determine the data
element "requirement level." This sets the minimum requirements for software
tools to participate in your program.  In each of the use cases, there are two
requirement levels:

Required
    All software must collect this data point and transfer it any time it exists
    in a home. This usually is driven by rebate qualifications or quality
    assurance requirements.
Optional
    Not required.

The :ref:`datatool` will allow you to see the minimum required fields that have
been agreed upon by BPI WG-5 for audit and retrofit use cases. In addition, you
can use the Home Energy Score and BPI – 2101 requirement toggles. By activating
these toggles, you can see which fields would be required if you wanted to
complete a Home Energy Score or to fill out a `BPI-2101 Home Performance
Certificate of Completion`_.

.. _BPI-2101 Home Performance Certificate of Completion: http://www.bpi.org/tools_downloads.aspx?selectedTypeID=1&selectedID=143

The grayed out fields are optional and represent fields that are relevant in
many programs, but not required in the standard use cases. You can choose to
make optional fields required in your program. However, not all software
products on the market collect every possible data point. Making some of these
data points "required" may restrict which products are eligible to participate,
or may require you to pay software vendors to code their software for this
requirement. Communication with potential software vendors is key and consider
their feedback on which fields you require for your program before determining
your final data requirements. BPI WG-5 can help facilitate that conversation in
a constructive environment.

Some programs with a large number of measure-specific rebates are choosing to
identify data points as "optional" to allow flexibility in implementation. Your
program can use a minimum data collection standard that is required for every
home. However, if the contractor or software vendor wants to participate in the
full spectrum of rebates, they can choose to send "optional" fields that trigger
a rebate payment. This allows a diverse set of software products and contractor
business models to participate, without mandating that every software and
contractor support the full spectrum of rebates your program portfolio may
offer. If you want to choose this path, it will be important to provide clear
specifications on which "optional" fields will trigger which rebate payments.

Defining Use Cases
******************

The standard use cases provided as a part of this guide are the primary use
cases that have been developed to date. Each use case only uses a fraction of
the data points that the HPXML standard can support. Over time, more use cases
will be developed to meet market needs.

.. _audit-use-case-defn:

Audit Use Case
==============

The audit use case is designed for Home Performance with ENERGY STAR or whole
house programs that require energy assessments. This use case allows auditors to
submit their audit results and proposed scope of work for an eligibility review
from the program. Required fields are established to help identify the home's
existing characteristics, health and safety needs, recommended improvements, and
associated savings predictions. 

An example of an audit use case HPXML file can be found on the `HPXML GitHub
repository`_ and more technical description of the audit and upgrade use case
can be found in the software developer guide at
:doc:`/software_developer/usecases/auditupgrade`.

.. _HPXML GitHub repository: https://github.com/hpxmlwg/hpxml/tree/hpxmlguide/examples

.. _upgrade-use-case-defn:

Upgrade Use Case
================

The upgrade use case is designed to facilitate the transfer of completed whole
house upgrade projects, such as Home Performance with ENERGY STAR or
Weatherization programs. This includes the pre-upgrade condition of the home and
a description of the installed measures, as well as associated predicted
savings. Required fields are established to complete a full quality assurance
review of all installed measures and determine rebate or financing eligibility.
The minimum requirements reflect those most common between all of the
HPXML-compliant programs so far. Programs that offer more diverse rebates may
need to consider changing "optional" fields to "required" in order to meet
program needs.

The upgrade use case HPXML file is very similar to the audit use case. The
differences are detailed in :doc:`/software_developer/usecases/auditupgrade`. 

.. _hescore-use-case-defn:

Home Energy Score Use Case
==========================

The Home Energy Score use case defines the minimum data set required by the
DOE's Home Energy Score tool, in order to properly generate the 1 to 10 score. 
These data point are clearly identified in the data selection tool.  Programs
interested in generating a Home Energy Score, will need to make sure that their
HPXML software tool are collecting this minimum dataset. 

In order to generate the score, your program software team will also need to
integrate with the DOE's Home Energy Score API. HPXML can be transferred through
the API and generate a Home Energy Score in real time. For more information on
integration with the Home Energy Score API, see
:doc:`/software_developer/usecases/hescore` in the software developer guide. 

A full list of HPXML data elements that can currently be incorporated into use
cases is available in the `online schema documentation`_.

.. _online schema documentation: http://hpxmlwg.github.io/hpxml/schemadoc/hpxml-2.2.0/index.html

.. _bpi2101-use-case-defn:

BPI – 2101 Certificate of Completion Use Case
=============================================

The Certificate of Completion use case is designed to ensure that the value of
energy efficiency improvements is visible in the real estate transaction.
Studies suggest that buyers will pay higher prices for efficient homes – but
only if they know that the homes are efficient. Programs have traditionally had
difficulty in getting information about energy efficiency improvements into the
real estate transaction. The Certificate of Completion use case provides a
standardized framework for programs to collect and assemble data about a home
that features energy efficiency improvements ranging from a single installation
to a whole-house upgrade. The standard data set in this use case is aligned with
both the Appraisal Institute's Green and Energy Efficient Addendum and the Real
Estate Transaction Standard, allowing data from a trusted third party (a Home
Performance with ENERGY STAR or other efficiency program) to flow seamlessly to
appraisers and real estate (MLS) databases.

.. note::

    The BPI – 2101 Certificate of Completion Use Case is designed to be highly
    flexible and inclusive of a wide range of technologies.  When implementing
    this use case, most contractors and software vendors will not support the
    full spectrum of technology to import to your program.  However being able
    to capture the full spectrum of data point and export to other third
    parties, will give your program the widest range of options for interacting
    with the real estate industry.


How to Add Data Elements
************************

When reviewing the data sets that are required for your implementation, it is
possible to identify a data point you require that is not in one of the
pre-defined use cases or the HPXML standards. If this is the case, BPI WG-5 can
assist in adding the new data element and in identifying how to incorporate it
into the standard. In some cases this might include adding new elements to the
standard to account for data points that could be applicable across many
programs.  However, if the data point is truly unique to your program, WG-5 has
also introduced "measure codes" that allow a code to be assigned for a specific
measure in a specific program.  This creates added flexibility without needing
to modify the standards in all cases.

To submit a new data element for consideration, you can use the WG-5 `GitHub`_
account.  This way all members can see your recommendations and address them
immediately.  Follow the steps below to submit additional requests if needed:

  #. Sign up for a user account on `GitHub`_.
  #. Go to the `HPXML GitHub issues page`_.
  #. Click "New Issue"
  #. Fill out the form to ask a question or make a request. No need to assign a
     person, milestone, or label.
  #. Click "Submit New Issue".

.. _GitHub: https://github.com
.. _HPXML GitHub issues page: https://github.com/hpxmlwg/hpxml/issues/

Once you have defined the use case needed for your program and have identified
all required fields, you are ready to proceed to the next step. Remember, this
can be an iterative process. It is good to do due diligence in the planning
process. However, even the best implementation plans may need to be modified as
the program goes to market and a large number of homes start running through it. 

.. note::

    Schedule opportunities later in your implementation to check in on data
    requirements and adjust as needed.
