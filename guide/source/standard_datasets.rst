.. _benefits-of-adopting-standard-datasets:

Standard HPXML Datasets
#######################

One of the areas in which data standardization holds the greatest promise is in data collection and reporting. If different programs all agree to collect the same (or very similar) data for the same use cases, such as the data reported by the contractor when the initial audit is conducted or the final job and test-out results are reported, information technology costs could be reduced tremendously across the country because software vendors would be able to use the same reporting template, with only minor modifications, for multiple programs. Standard datasets will also greatly facilitate cross-program comparability, support research efforts and accurate quantification of savings for other uses.

As part of the effort to implement the data standards, Home Performance Coalition, chair of the HPXML working group, led the development of three standard datasets, for the audit, project completion, and the Home Performance Certificate (BPI-2101-S-2013), which creates a bridge between the energy efficiency and real estate industries. The National Renewable Energy Laboratory (NREL) developed the Home Energy Score Translator, which allows software vendors to generate HEScore inputs from HPXML files. 

Each of the datasets specify a number of required data elements that can be collected at specific points during the implementation of a residential energy efficiency program. The audit and upgrade datasets were created to facilitate the transfer of project data from third-party energy modeling tools to a program management database. Home Energy Score and the Home Performance Certificate reflect collaboration with existing programs and standards.

The next section of the Implementation Guide explains how programs and implementers can use the Data Selection Tool to determine their HPXML data needs based on the minimum data requirements of the HPXML datasets.

The remainder of this section describes current HPXML datasets. Development of standard datasets associated with other use cases, particularly evaluation, measurement, and verification (EM&V), is an important additional priority because it will generate additional cost savings and promote program adoption of the standards. New datasets will be published as they are identified. 

Audit
*****

The audit dataset is designed for use by Home Performance with ENERGY STAR or other whole-house programs that require auditors to submit energy audit results and a proposed work scope to the program for review.

The audit dataset was established through a consensus process of three geographically diverse existing whole-house programs, and is intended to meet the needs of most programs. The dataset describes the baseline building with a proposed work scope. Required fields include data on the home's existing characteristics, health and safety needs, recommended improvements, and savings predictions.

Programs that wish to adopt the audit dataset, may download the Data Selection Tool for guidance on the required data fields. Software developers may visit the GitHub repository for an example of an HPXML audit file.

Upgrade
*******

The upgrade dataset is designed to facilitate the transfer of information on completed whole house retrofits from contractors to Home Performance with ENERGY STAR or other whole house programs.

The upgrade dataset describes the baseline building (e.g., the pre-upgrade condition of the home, with proposed measures) with a completed work scope (e.g., description of installed measures, with modeled or predicted energy savings). The upgrade dataset was established through a consensus process of three geographically diverse existing whole-house programs, and is intended to meet the needs of most programs. Programs that offer more diverse incentives may need to add HPXML data elements to meet program needs.

Programs that wish to adopt the upgrade dataset, may download the Data Selection Tool for guidance on the required data fields. Software developers may visit the GitHub repository for an example of an HPXML upgrade file.

Home Energy Score
*****************

The Department of Energy’s Home Energy Score (HEScore) is similar to a miles-per-gallon rating that helps homeowners and homebuyers understand how much energy the home is expected to use. The HEScore also provides information on how to make the home more energy efficient.

The Home Energy Score Translator was developed by the NREL to generate HEScore inputs from HPXML files. The translator is available open source as a stand-alone script. It is also incorporated into the HEScore API. By using this translator, software developers can leverage their investment in HPXML to provide HEScore functionality with minimum development cost.

Home Performance Certificate
****************************

BPI-2101-S-2013 Standard Requirements for a Certificate of Completion for Residential Energy Efficiency Upgrades is a BPI standard that identifies a subset of HPXML data elements for certificates that document the completion of an energy efficiency project, either whole-house or individual measures. 

A BPI-2101 compliant certificate is designed to be used as a reference document by real estate agents, appraisers, and other professionals during the home sale process. The certificate provides a clear, easy-to-understand description of the home energy upgrade, including predicted energy savings or other performance indicators, such as Home Energy Score.

There are two types of certificates that can be issued in compliance with BPI-2101. The first is a Certificate of Efficiency Improvements, which provides information about the energy efficiency improvements installed. The second is a Certificate of Performance, which provides information about energy efficiency improvements installed plus quantitative information about a home’s performance, for example, a Home Energy Score or projected energy consumption.

These certificates can be formatted and branded by the programs that are implementing them. For example, Arizona Public Service and Salt River Project are currently issuing a Certificate of Efficiency Improvements to homeowners that complete the Home Performance with ENERGY STAR program. A sample certificate can be found on www.hpxmlonline.com/hpxml-datasets/bpi-2101. 

All of the HPXML data elements that can be used on BPI-2101 compliant certificates are aligned with the Real Estate Standards Organization (RESO) Data Dictionary and with the Appraisal Institute’s Residential Green and Energy Efficient Addendum. The RESO Data Dictionary standardizes the fields that are used in hundreds of MLS’ nationwide. Because BPI-2101 is aligned with the RESO standard, programs are able to provide homeowners with access to consistent, comparable information about the energy efficiency features in existing homes and to standardize the flow of information about a home’s energy efficient characteristics into property listings.

The Home Performance Coalition will be working with Elevate Energy, and other BPI Working Group 9 members, in 2017 to update the alignment of the standard with the new versions of the RESO data dictionary and Appraisal Institute’s Residential Green and Energy Efficient Addendum. 
