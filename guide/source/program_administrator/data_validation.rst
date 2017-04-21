.. _step5:

Step 5: Designing a Data Validation Process
###########################################

Designing a good system for data validation that automatically checks all submitted data is critical for ensuring high-quality data, maintaining contractor satisfaction, and streamlining quality assurance activities. The good news is that most of this work will be completed by your software vendor. However, you will want to undergo a thorough scoping exercise with your vendor to identify what types of validation checks you want your program software to complete. 

For example, a basic validation check ensures that all data is present and in the right format. More advanced validation checks can ensure that data falls within an acceptable range for program compliance purposes or to guide quality assurance. You may be able to automate quality assurance review on health and safety results to ensure all standards are being met. If not met, a user can be warned and intervene on the project.

If done correctly, a good validation system can speed up your process and significantly reduce cost. If done too hastily, it can increase frustration within your contractor base or yield lower-quality data.

Your data validation systems should align with your business objectives. For example, if you are using HPXML for a rebate program, you will want to validate that:

    * All files are in the correct HPXML format
    * Data points required for rebate eligibility screening are collected
    * All rebate eligibility rules are met
    * Health and safety standards have been followed

Your program will probably have specific requirements that you are trying to validate against. As you develop your validation system share the requirements with prospective third-party software vendors. These software vendors will likely include these same requirements in their software validation protocols to warn contractors when a requirement has not been met. This is an important benefit of using a national data standard.

Once validation rules have been set, it is equally important to ensure that the user’s experience is optimized to minimize frustration and clearly communicate validation errors. If a contractor is not receiving clear validation error messaging and cannot resolve the issue during the upload process, this can lead to a large number of phone calls and a higher technical assistance requirement resulting in greater cost to the program. If the process is not managed properly, you can burn out your users and create contractor dissatisfaction. This, of course, is not an observation exclusive to HPXML, but a best practice in any software implementation in general.

.. _toolbox:

HPXML Toolbox
*************

To assist in validation, the National Renewable Energy Lanoratory (NREL) has created an `HPXML Toolbox`_ that includes
an HPXML schema validator, dataset validator, data dictionary, a collapsable tree view of HPXML,
and a web API that can be incorportated into software workflows. The tool is
useful to both software developers to test their implementation against the
known datasets. It is also helpful for program administrators to see what data
is in an HPXML file and what additional data would be required to meet any of
the use cases.

.. _HPXML Toolbox: https://hpxml.nrel.gov/

Phasing of Validation
*********************

As you prepare your rollout schedule, consider implementing a phased validation system roll out. If you clearly define the scope of each phase and roll it out following a regimented schedule, you can greatly assist the market in adapting to the new system, while giving you the opportunity to improve the data quality and functionality of your system over time. For example, if you are running a whole home program with incentives or rebates, here are some phases to consider:

Phase 1 – File Validation and Minimum Data Requirements
=======================================================

In this phase, you will want to verify that the uploaded HPXML file is in the correct structure and minimum data points required are present and in the correct format. This will allow you to get to market quickly and begin to test your systems. You will still need a person to review the files to ensure that the data provided meets the technical requirements of your rebate program. For example, you will validate that all required insulation data points are present, but review the installed R-value to make sure that it meets your program requirements. You will also want to add a check to ensure that no health and safety problems exist.

Phase 2 – Advanced Data Validation and Automated QA
===================================================

Over time, you can begin to layer in engineering assumptions that provide automated QA or guided QA. For example, you can add a validation check to see if installed measures are consistent with standard building practices. This way, if you receive a file that claims to have an attic with R-100, a QA advisor is triggered to review the project.

By using this type of validation system, you can significantly reduce your labor requirements for reviewing submitted files because you can focus your labor on probable errors or problem areas. In some cases, you may be able to get to auto-approval on a selected number of projects.

.. note::

    Over time, you can add even more sophisticated systems. If you launch with a very complex validation system, there is a high likelihood that many of the initial project submissions will fail as the market is still adapting to the new program environment. If you take a phased approach, you can ease this tension and coordinate with the market to facilitate high-quality data transactions while reducing admin costs.  
