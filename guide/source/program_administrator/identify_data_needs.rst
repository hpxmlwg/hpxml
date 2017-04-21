.. include:: <isonum.txt>

.. _step3:

Step 3: Identify Data Needs
###########################

One of the areas in which data standardization holds the greatest promise is in data collection and reporting. If different programs all agree to collect the same (or very similar) data for the same use cases, such as the data reported by the contractor when the initial audit is conducted, or the final job and test-out results are reported, information technology costs could be reduced significantly across the country because software vendors would be able to use the same reporting template, with only minor modifications, for multiple programs. Adopting the HPXML standard datasets also will greatly facilitate cross-program comparability, and support research efforts and the accurate quantification of savings for other uses.

HPXML defines a long list of data elements, many of which may not be needed for your project. To determine which data points are needed, we recommend using the standard datasets described in :doc:`/standard_datasets` as a starting point, while considering the goals you identified in :ref:`step1`. Even though the Audit and Upgrade datasets were initially established for whole-house programs, many of the data points are relevant to other types of residential programs, for example, weatherization or single-measure programs. Also, many software vendors are already able to transfer the data required in these datasets. Any subset of data within these datasets will be easy to implement for existing HPXML-compliant tools.

The goal of this exercise is to identify the minimum data collection requirements needed to meet project goals. This means identifying what must be collected in the field, what must be transferred to your program management system, and what you are transferring and reporting to others, where applicable.

The BPI data standards support the collection and transfer of additional data points beyond these datasets. However, additional data may require software vendors to make substantive changes to their software. Program administrators should recognize the financial impacts of custom data collection requests and consider providing financial assistance to software vendors to meet any customization requests, as appropriate.

Data Selection Best Practices
*****************************

When exporting or importing data from third-party data systems, it is important to develop a concise set of data requirements. As stated above, HPXML is capable of describing and transferring a large universe of data, but only a portion of data may be needed for a particular use case. Examples of use cases include:

  * Reporting on the baseline conditions of a home and proposed improvements
  * Reporting on the improvements to the home compared to baseline conditions
  * Reporting on health and safety testing
  * Reviewing a contractor's work as part of a QA process
  * Reporting a home's energy efficiency assets to the parties in real estate transactions
  * Reporting data on program activity to DOE and other agencies

Before reviewing the standard datasets, there are several best practices to consider.

Be Transparent with Stakeholders
================================

Transparency with your contractors and software vendors throughout the process will help guide programmatic decisions and prevent challenges down the road. This is particularly true for the data selection process as stakeholders can bring attention to potential challenges that need resolution. For example, a program may request a specific data point that is not typically collected by most software products. If vendors can identify this need early on, a resolution can be reached in the planning phase and not delay the project later on.

Be Sensitive to Data Collection Burden
======================================

When selecting data requirements, programs should collect just enough data for program compliance, and measurement and verification of results. As a guiding principle, Home Performance with ENERGY STAR\ |reg| recommends that programs employ administrative procedures that minimize the burden of participation for contractors and homeowners. When choosing mandatory data points for your program, it is important to recognize that every data point collected has a collection cost to contractors. Collaborate with evaluators, contractors, and software vendors to explore solutions that meet the need of the program as cost efficiently as possible.

Leverage Data Choices Made by Other Program Administrators
==========================================================

HPXML is easily extensible and therefore can be customized to the specific needs of a program. However, program administrators should look at the standard datasets being implemented by other programs around the country as many software vendors are already exporting and importing these standard datasets. When a program is using unique data requirements, the associated customization can push significant development costs for that specific program onto other parties, like software vendors and service providers. To streamline implementation and best leverage efforts from other programs, it is encouraged to coordinate with other program administrators to minimize the number of program-specific data fields required in your jurisdiction. This guide provides an HPXML data selection tool below to easily facilitate this coordination.

Schedule Updates to Data Requirements
=====================================

Software developers tend to work in phases to control releases of their software. To avoid additional costs or confusion, try scheduling regular updates once or twice a year and communicate future changes as early as possible. This will help with version control and create a more manageable process for software vendors and your implementation team.

Adopting these best practices will assist in establishing a streamlined data selection process.

.. _datatool:

HPXML Data Selection Tool
*************************

To assist program administrators in reviewing the standard datasets that are being implemented by other programs, a data selection tool is available to help identify the required data points. The tool also helps programs select and communicate the requirements for the program to contractors, trade allies, and other stakeholders. The HPXML Data Selection Tool is a "living document" so if a program identifies data points that are not in the datasets, the HPXML working group can assist in adding them to the tool to meet the program’s needs.

   * Download: :download:`HPXML Data Selection Tool <hpxml_data_selection_tool.xlsx>`

The attached instructional video provides a walkthrough of the HPXML data selection tool. By using the tool, programs can quickly select the data required for HPXML program implementation. Programs can then forward the tool to the implementation team, trade allies and software providers, giving them clear guidance on the requirements for HPXML Implementation with your program.

.. raw:: html

    <iframe width="640" height="360" src="https://www.youtube.com/embed/vmfU1ytzMfc" frameborder="0" allowfullscreen></iframe>

.. raw:: latex

    \par\href{https://youtu.be/vmfU1ytzMfc}{YouTube: HPXML Data Selection Tool Tutorial}\par

Additional details about the data structure and standard datasets are provided in the sections below.

Understanding the HPXML Data Structure
**************************************

In the reviewing tool, notice the following descriptors for each data
point:

  * Data Category - A general description of the information at the building characteristic or contact information level. Note: Insulation has several data categories, depending on the insulating plane. For example, referencing insulation installed on the attic floor "Attic Floor Insulation" or on the bottom of the roof deck "Attic Roof Insulation."

  * Data Element - A specific data point or descriptor within that data category. For example, insulation material type or R-value.

  * Data Type - How the data should be provided, for example, as a number, text, enumeration, etc.

  * Definition - A written description of the data point and what it means. Because the name of the data point is not always clear, this provides a narrative explanation of what each data point describes.

In most cases, there are several data points needed to describe any one building characteristic. For example, if you require blower door testing in your program, you will require "Air Infiltration" information. In this case, there are three data points that are required to describe an air leakage measurement, such as 2000 CFM\ :sub:`50`:

    "Building Air Leakage" = 2000

    "Building Air Leakage Unit" = CFM

    "House Pressure" = 50  

This provides flexibility to receive the same data in multiple formats. For example, air leakage could be represented in CFM\ :sub:`50`, ACH or ACH\ :sub:`50`.

Setting the Program's Data Requirement Level
********************************************

The program administrator's main task in this step is to determine the data element "requirement level." This sets the minimum requirements for software tools to participate in your program. In each of the standard datasets, there are two requirement levels:

  * Required - All software must collect this data point and transfer it any time it exists in a home. This usually is driven by rebate qualifications or quality assurance requirements.

  * Optional - Not required.

The :ref:`datatool` will allow you to see the minimum required fields that have been agreed upon by the HPXML Working Group for the audit and upgrade datasets. In addition, you can use the Home Energy Score and Home Performance Certificate requirement toggles. By activating these toggles, you can see which fields would be required if you wanted to complete a Home Energy Score or to comply with the Home Performance Certificate standard.

The grayed-out fields are optional and represent fields that are relevant in many programs, but not required in the standard datasets. You can choose to make optional fields required in your program. However, not all software products on the market collect every possible data point. Making some of these data points "required" may restrict which products are eligible to participate in your program, or may require you to pay software vendors to code their software for this requirement. Communication with potential software vendors is important. Consider their feedback on required fields before determining your final data requirements. The HPXML Working Group can help facilitate that conversation in a constructive manner.

Some programs with a large number of measure-specific rebates are choosing to identify data points as "optional" to allow flexibility in implementation. Your program can use a minimum data collection standard that is required for every home. However, if the contractor or software vendor wants to participate in the full spectrum of rebates, they can choose to send "optional" fields that trigger a rebate payment. This allows a diverse set of software products and contractor business models to participate, without mandating that every software and contractor support the full spectrum of rebates your program portfolio may offer. If you want to choose this path, it will be important to provide clear specifications on which "optional" fields will trigger which rebate payments.

.. _how_to_add_data_elements:

How to Add Data Elements
************************

When reviewing the datasets that are required for your implementation, it is possible to identify a data point you require that is not in one of the pre-defined datasets or in HPXML. If this is the case, the HPXML working group can assist in adding the new data element and in identifying how to incorporate it into the standard.

In some cases, this might include adding new elements to the standard to account for data points that could be applicable across many programs. To submit a new data element for consideration, you can use the working group’s `GitHub`_ account. This way, all members can see your recommendation and address it immediately. You can also email your request to hpxml@homeperformance.org.

Follow the steps below to submit requests:

  #. Sign up for a user account on `GitHub`_.
  #. Go to the `HPXML GitHub issues page`_.
  #. Click "New Issue"
  #. Fill out the form to ask a question or make a request. No need to assign a
     person, milestone, or label.
  #. Click "Submit New Issue".

.. _GitHub: https://github.com
.. _HPXML GitHub issues page: https://github.com/hpxmlwg/hpxml/issues/

Please include the following information in your request:

  * Name - Create a name for the data element or enumeration you feel best describes the term.

  * Definition - Write a comprehensive definition of the data element and include references if necessary.

  * Data Type - Include your recommended data type and maximum field length.

  * Enumerations - If your recommended field is a pick-list, please include enumerations. Enumerations may also need a definition.

  * Justification - Please provide a reason the data element is important to your energy efficiency program or market.

  * Duplication - Review the dictionary thoroughly to ensure you are not duplicating an already existing data element or enumeration. Concepts can be expressed in a number of ways and rather than adding additional data elements or enumerations, we can use this recommendation to better define existing elements.

Once you have defined the dataset needed for your program and have identified all required fields, you are ready to proceed to the next step. Remember, this can be an iterative process. It is good to do due diligence in the planning process. However, even the best implementation plans may need to be modified as the program goes to market and a large number of homes start running through it.

.. note::

    Schedule opportunities later in your implementation to check in on data
    requirements and adjust as needed.
