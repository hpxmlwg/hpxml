Introduction
########################

.. benefits-of-adopting-standard-datasets:

The HPXML Data Dictionary contains over 800 data points. However, program administrators may only need to collect a subset of the HPXML data for specific use cases (i.e., during the administration of a whole home program or to make energy efficiency visible in real estate transactions).

To facilitate the implementation of HPXML, the data standard includes several standard datasets that can be adopted by programs and software tools. The "audit" and "upgrade" datasets are designed to facilitate the transfer of project data from third-party energy modeling tools to a program management database. The Home Performance Certificate and Home Energy Score Translator can be used to document home energy improvements and performance for the residential real estate and appraisal industries. 

By adopting these datasets, programs and developers can implement HPXML more quickly and cost-effectively. 


The HPXML Data Dictionary includes minimum data requirements for four use cases that were identified to reduce data variation between jurisdictions implementing energy efficiency programs, including whole-house and single measure programs. Each of the use cases include corresponding datasets that specify a number of data elements that can be collected at specific points during the implementation of an energy efficiency program (e.g., the energy audit). The audit and upgrade datasets were created to facilitate the transfer of project data from third-party energy modeling tools to a program management database. Home Energy Score and the Certificate of Completion (BPI-2101) reflect collaboration with existing programs and standards.

By adopting the audit and upgrade datasets, energy efficiency programs can implement HPXML more quickly and cost-effectively, and reduce the data collection burden on contractors working in multiple jurisdictions. Data variation among programs also imposes costs on software developers because significant development work is needed to meet the program's data needs. Software tools may also leverage their investment in HPXML to offer Home Energy Score functionality and off-the-shelf software solutions for organizations implementing energy efficiency programs. This guards the program industry against software obsolesce and vendor lock-in, and also greatly reduces the variation in data collection requirements across jurisdictions.

When programs adopt HPXML-compliant software, program administrators can get out of the software development business by adopting off-the-shelf solutions that require little customization. This guards against software obsolesce and vendor lock-in, and boosts innovation in software development.  

Below is a description of the current HPXML datasets. Home Performance Coalition, which chairs the HPXML working group, continues to work with industry partners, including regulators, program evaluators, implementers, and utilities to advance data standardization in the industry, including standardized measure definitions, reporting and program evaluation requirements. New datasets will be published as they are identified. 

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

The Home Energy Score Translator was developed by the National Renewable Energy Laboratory (NREL) to generate HEScore inputs from HPXML files. The translator is open source and available as a stand-alone script. It is also incorporated into the HEScore API. By using this translator, software developers can leverage their investment in HPXML to provide HEScore functionality with minimum development cost.

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
