.. include:: <isonum.txt>

.. _benefits-of-adopting-standard-datasets:

Standard HPXML Datasets
#######################

One of the areas in which data standardization holds the greatest promise is in data collection and reporting. If different energy efficiency programs all agree to collect the same (or very similar) data for the same use cases, such as the data reported by the contractor when the initial audit is conducted or the final job and test-out results are reported, information technology (IT) costs could be reduced significantly across the country. 

Software vendors would be able to use the same reporting template, with only minor modifications, for multiple programs. Standard datasets would also greatly facilitate cross-program comparability as well as support research efforts and accurate quantification of savings for other uses.

HPXML includes four standard datasets that program administrators can adopt to standardize data collection and reporting for various use cases, including:

    * Transfer of project data from third-party energy modeling or data collection tools to a program management database; and
    * Export energy efficiency project data, including the DOE’s Home Energy Score, to local MLS.

Each of the datasets specifies a number of required data elements that can be collected at specific points during the implementation of a residential energy efficiency program. Below is a summary of the datasets, followed by a discussion in the next section of the benefits of adopting data standards.

.. _audit-use-case-defn:

Audit
*****

The audit dataset is designed for use by Home Performance with ENERGY STAR® or other whole-house programs that require auditors to submit energy audit results and a proposed workscope to the program for review. The dataset describes the baseline building with a proposed work scope. Required fields include data on the home’s existing characteristics, health and safety needs, recommended improvements, and savings predictions.

The audit dataset was established through a consensus process of three geographically diverse existing whole-house programs, and is intended to meet the needs of most programs.

Programs that wish to adopt the audit dataset may download the `Data Selection Tool <http://www.hpxmlonline.com/tools-resources/data-selection-tool/>`_ for guidance on the required data fields. Software developers may visit Github for an example of an HPXML audit file.

.. _upgrade-use-case-defn:

Upgrade
*******

The upgrade dataset is designed to facilitate the transfer of information on completed whole house retrofits from contractors to Home Performance with ENERGY STAR |reg| or other whole house programs.

The upgrade dataset describes the baseline building (e.g., the pre-upgrade condition of the home, with proposed measures) with a completed work scope (e.g., description of installed measures, with modeled or predicted energy savings). The upgrade dataset was established through a consensus process of three geographically diverse existing whole-house programs, and is intended to meet the needs of most programs. Programs that offer more diverse incentives may need to add HPXML data elements to meet program needs.

Programs that wish to adopt the upgrade dataset may download the Data Selection Tool for guidance on the required data fields. Software developers may visit Github for an example of an HPXML upgrade file.

.. _hescore-use-case-defn:

Home Energy Score
*****************

The Home Energy Score (HEScore) is similar to a miles-per-gallon rating that helps homeowners and homebuyers understand how much energy the home is expected to use. The HEScore also provides information on how to make the home more energy efficient.

The `Home Energy Score Translator <https://github.com/NREL/hescore-hpxml>`_ was developed by the National Renewable Energy Laboratory (NREL) to generate HEScore inputs from HPXML files. The translator is available open source as a stand-alone script. It is also incorporated into the HEScore API. By using this translator, software developers can leverage their investment in HPXML to provide HEScore functionality with minimum development cost.

.. _bpi2101-use-case-defn:

Home Performance Certificate
****************************

The Home Performance Certificate (BPI-2101-S-2013 Standard Requirements for a Certificate of Completion for Residential Energy Efficiency Upgrades) is a nationally recognized protocol that creates a bridge between the energy efficiency, real estate, and appraisal industries. The standard identifies a standard set of data elements for certificates that document the completion of a whole-house energy upgrade (HEU) and individual energy conservation measures (ECMs). A certificate that complies with the requirements of the standard can be branded and issued by home energy upgrade programs or by entities implementing nationally recognized third-party quality assurance (QA) programs. 

The set of data elements required for inclusion in the certificate provides a clear, easy-to-understand description of the HEU or ECMs, including information about major energy-related improvements implemented, and, if relevant, predicted energy savings or other performance indicators. The certificate can be designed to be used as a reference document by real estate agents, appraisers, and other professionals during the home sale process. The certificate may be attached to an MLS listing sheet and shown to the buyer and buyer’s agent as a demonstration of the home’s relative energy efficiency, which may increase the home’s market value. The certificate may also be used by appraisers and underwriters as a source of information about characteristics of a home related to energy consumption and energy savings.

The information in a BPI-2101-compliant certificate is aligned with the Real Estate Standards Organization’s Data Dictionary, which specifies a standard vocabulary for MLS systems. This alignment allows information from a BPI-2101-compliant certificate to be more easily transferred to MLS systems. The information is also designed to align with data fields included on the Appraisal Institute’s Residential Green and Energy Efficiency Addendum (AI Addendum). The AI Addendum is an attachment that appraisers can voluntarily elect to include in their residential appraisal to comply with Uniform Standards of Professional Appraisal Practice (USPAP) when completing a high-performance home assignment.

The scope of the standard does not include the appearance of a certificate. The certificate’s sponsor may choose a certificate design that best meets its programmatic needs. 

Arizona Public Service and Salt River Project currently are issuing the certificate to homeowners that complete the Home Performance with ENERGY STAR |reg| program. 

Future HPXML Datasets
*********************

The development of standard datasets associated with other use cases, particularly evaluation, measurement, and verification (EM&V), is an important additional priority because it will generate additional cost savings and promote program adoption of the standards. New datasets will be published as they are identified.
