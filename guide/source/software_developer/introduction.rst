Introduction
############

..todo:: 

    SHOULDN'T THERE BE SOME INTRODUCTION TO PROGRAMS, INCLUDING HPWES, FOR THIS AUDIENCE? WOULDN'T IT MATTER TO THEM TO KNOW FOR WHAT THE DATA WILL BE PRIMARILY (INITIALLY) USED? SIMILARLY, PERHAPS THERE IS A NEED FOR THIS TYPE OF INTRO TO THE SOFTWARE DEVELOPMENT COMMUNITY ON THE PROGRAM ADMIN GUIDE.

This software developer guide is designed to outline the technical details of
getting a Home Performance XML (HPXML) implementation up and running. HPXML is
an expansive standard data format based on XML and maintained by the Building
Performance Institute's Working Group 5 (BPI WG-5). For more information on the
BPI data standards and their relation to HPXML see
:ref:`what-are-the-bpi-standards`. 

The HPXML format is defined by a set of XML Schema (xsd) documents that outline
all the acceptable data elements, their structure, and relation to one another.
The schema itself is very flexible. Almost none of the elements are required,
which allows for any level of detail in home performance data to be transmitted
in the format. This level of flexibility is very useful but it also can be
dangerous for the software developer. Two developers could each create an
implementation that would represent their data in valid HPXML, but would be very
divergent. The purpose of this guide is to document the assumptions that are not
codified in the schema that are necessary to write and interpret HPXML documents
across platforms.

The majority of the assumptions and recommendations here come from the set of
pilot implementations in the :doc:`Audit-Upgrade Use Case
</software_developer/usecases/auditupgrade>`. This guide primarily documents
lessons learned from those pilots. As other use cases present themselves, this
guide will be augmented appropriately.

BPI Working Group 5
*******************

One of the best resources you will have available to you as you develop to HPXML
is BPI Working Group 5 (a.k.a. HPXML Working Group). Many of the current
developers are there. They have a lot of experience in getting HPXML working and
can help you avoid costly pitfalls.

To join the working group send an email to hpxml@homeperformance.org.

GitHub
******

The HPXML schemas, example files, and this guide are all `maintained on GitHub
<https://github.com/hpxmlwg/hpxml>`_. You will always be able to find the latest
version of the schemas there. Additionally as the schemas evolve over time you
can be connected to and influence that process. 


