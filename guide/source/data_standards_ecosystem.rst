Standard Datasets
########################

.. _standard-data-collection-tools:

Value of Standardized Data Collection
*************************************

The HPXML Data Dictionary includes requirements for four datasets that contain a subset of HPXML data elements. Each of these datasets specifies a number of data elements to be collected at specific points during the implementation of an energy efficiency program (e.g. the audit, project completion, etc.). While HPXML is capable of transferring a wide variety of data elements, any one program or jurisdiction will only need a small sub-set in most cases. 

The audit and upgrade datasets were identified by the working group to facilitate the transfer of project data from third-party energy modeling tools to a program management database. Home Energy Score and BPI-2101 reflect collaboration with existing programs.

he standard is designed to promote
    consistency between programs and facilitate cost efficiency in the
    implementation of HPXML through alignment to a standardized specification.


New standard datasets will be created as the need arises.

To facilitate adoption of the data standards and reduce variation between
jurisdictions, which can be costly for software providers and contractors

Audit
*****

The audit dataset is designed for use by Home Performance with ENERGY STAR® or other whole house programs that require auditors to submit energy audit results and a proposed workscope to the program for review. The audit dataset was established through a consensus process of three geographically diverse existing whole-house programs, and is intended to meet the needs of most programs. The dataset describes the baseline building with a proposed workscope. Required fields include data on the home’s existing characteristics, health and safety needs, recommended improvements, and savings predictions.

Programs that wish to adopt the audit dataset, may download the Data Selection Tool for guidance on the required data fields.

Software developers may visit the GitHub repository for an example of an HPXML audit file.

Upgrade
*******

The upgrade dataset is designed to facilitate the transfer of information on completed whole house retrofits from contractors to Home Performance with ENERGY STAR® or other whole house programs that require a completed workscope. The upgrade dataset describes the baseline building (e.g., the pre-upgrade condition of the home, with proposed measures) with a completed workscope (e.g., description of installed measures, with modeled or predicted energy savings). The upgrade dataset was established through a consensus process of three geographically diverse existing whole-house programs, and is intended to meet the needs of most programs. Programs that offer more diverse incentives may need to add HPXML data elements to meet program needs.

Programs that wish to adopt the upgrade dataset, may download the Data Selection Tool for guidance on the required data fields.

Software developers may visit the GitHub repository for an example of an HPXML upgrade file.

Home Energy Score
*****************

The Department of Energy’s Home Energy Score (HEScore) is similar to a miles-per-gallon rating that helps homeowners and homebuyers understand how much energy the home is expected to use. The score also provides information on how to make the home more energy efficient.

The Home Energy Score Translator was developed by the National Renewable Energy Laboratory (NREL) to generate HEScore inputs from HPXML files. The translator is available open source as a stand-alone script. It is also incorporated into the HEScore API. By using this translator, software developers can leverage their investment in HPXML to provide HEScore functionality with minimum development cost.

Certificate of Completion
*************************

BPI-2101-S-2013 Standard Requirements for a Certificate of Completion for Residential Energy Efficiency Upgrades is a BPI standard that identifies a subset of HPXML data elements for certificates that document the completion of an energy efficiency project, either whole-house or individual measures. BPI-2101 provides a clear, easy-to-understand description of the home energy upgrade, including predicted energy savings or other performance indicators, such as Home Energy Score, and is designed to be used as a reference document by real estate agents, appraisers, and other professionals during the home sale process. 

Types of Certificates

There are two types of certificates that can be issued in compliance with BPI-2101. The first is a Certificate of Efficiency Improvements, which provides information about the energy efficiency improvements installed. The second is a Certificate of Performance, which provides information about energy efficiency improvements installed plus quantitative information about a home’s performance, for example, a Home Energy Score or projected energy consumption.

These certificates can be formatted and branded by the programs that are implementing them. For example, Arizona Public Service and Salt River Project are currently issuing a Certificate of Efficiency Improvements to homeowners that complete the Home Performance with ENERGY STAR program. A sample certificate can be found here.

Alignment with Real Estate Standards

All of the HPXML data elements that can be used on BPI-2101 compliant certificates are aligned with the Real Estate Standards Organization (RESO) Data Dictionary and with the Appraisal Institute’s Residential Green and Energy Efficient Addendum. The RESO Data Dictionary standardizes the fields that are used in hundreds of MLS’ nationwide. Because BPI-2101 is aligned with the RESO standard, programs are able to provide homeowners with access to consistent, comparable information about the energy efficiency features in existing homes and to standardize the flow of information about a home’s energy efficient characteristics into property listings.

Future Updates

The Home Performance Coalition will be working with Elevate Energy, and other BPI Working Group 9 members in 2016 to update the Certificate of Completion to ensure its continued alignment with the new version of the RESO Data Dictionary (v.1.5).
