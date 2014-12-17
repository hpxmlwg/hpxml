.. _auditretrofitusecase:

Audit-Retrofit
##############

The audit-retrofit use case covers two scenarios:

#. A baseline building with a proposed work scope 
#. A baseline building with a completed work scope

Both scenarios describe a pre- and post-retrofit building and the actions
(measures) that occur between the two states to make the difference. To achieve
this the HPXML document needs to have the
:ref:`top level nodes <top-level-nodes>` described as below. 

All xml examples are taken from the ``examples/audit.xml`` document. It contains
all of the required fields for an audit use case data transfer.

Contractor
**********

The ``Contractor`` elements should list the name of the contractor--the person
who is proposing and or completing the work. The company being represented and
an email address are also included.

.. literalinclude:: /../../examples/audit.xml
   :language: xml
   :lines: 13-33
   :emphasize-lines: 11-12,15

Customer
********

The customer is the homeowner or resident. The ``Customer`` element should
include their name and phone number as shown.

.. literalinclude:: /../../examples/audit.xml
   :language: xml 
   :lines: 34-47
   :emphasize-lines: 6-7,10

Building
********

There are two ``Building`` nodes in an Audit-Retrofit use case document: pre-
and post-retrofit. Each is a full description the house. For the audit use
case, the pre-retrofit condition is the house as audited and the post-retrofit
condition is the proposed work scope. For the retrofit use case, the
pre-retrofit building is the state of the house before any work was done and
the post-retrofit state is the final building state audit.

.. _preretro:

Pre-retrofit
============

The pre-retrofit ``Building`` element comes first in the document. It describes
the initial state of the building. It should have a ``ProjectStatus/EventType``
of ``audit``. 

.. literalinclude:: /../../examples/audit.xml
   :language: xml 
   :lines: 48-49,60-62,280
   :emphasize-lines: 4

Many items within the building require a unique ``SystemIdentifier`` element.
The ``id`` attribute is used to specify this id within the document (see
:ref:`id-idref`). 

For example, the water heater in the pre-retrofit building has an id of ``dhw1``.

.. literalinclude:: /../../examples/audit.xml
   :language: xml
   :lines: 222-228
   :emphasize-lines: 2

.. _postretro:
   
Post-retrofit
=============

The post-retrofit ``Building`` element appears second in the document. It
describes the "after" state of the building. In the audit use case, that means
the *proposed* state of the building after the retrofits. In the retrofit use
case, that means the *actual* audited state of the building after the work is
completed. The ``ProjectStatus/EventType`` element has a different value
depending on the use case:

.. table:: Post-retrofit Event Types
   
   ========  =======================================
   Use Case  Event Type
   ========  =======================================
   Audit     proposed workscope
   Retrofit  job completion testing/final inspection
   ========  =======================================

The post-retrofit building is mostly a duplicate of the pre-retrofit building
where components of the building that do not change remain the same. However,
each component in the post-retrofit building needs a unique identifier that is
different from the unique identifier in the pre-retrofit building. The
``sameas`` attribute of the ``SystemIdentifier`` element is used to link
identical elements in the pre- and post-retrofit buildings (see :ref:`sameas`).

Going back to the water heater example, the water heater in the post-retrofit
building has a different ``id`` than the identical water heater in the
pre-retrofit building, but it has a ``sameas`` attribute to link it back to the
pre-retrofit water heater and indicate it is indeed the same equipment.

.. literalinclude:: /../../examples/audit.xml
   :language: xml
   :lines: 455-461
   :emphasize-lines: 2

.. note::

   When a measure changes a component between a pre- and post-retrofit building,
   the ``SystemIdentifier/@sameas`` attribute is omitted because the measure
   references the relationship between components.

Project
*******

In this paradigm, the :ref:`preretro` and :ref:`postretro` building elements
describes the state of the building at points in time. The ``Project`` element
describes what was done or is to be done to get from one state to another. 

The ``ProjectSystemIdentifiers`` are used to reference the pre- and post-
building ids. The redundant ``BuildingID`` element should reference the post-
building.

.. literalinclude:: /../../examples/audit.xml
   :language: xml
   :lines: 566-571,588-589,610-612
   :emphasize-lines: 2,4-5

Energy Savings
==============

``EnergySavingsInfo`` is used to transmit either or both the estimated or
measured energy use and savings achieved in a retrofit. 

.. literalinclude:: /../../examples/audit.xml
   :language: xml
   :lines: 571-588

.. note::

   All percentages are expressed in the form of fractions. i.e. 10% => 0.1

Measures
========

The ``Measure`` element describes a piece of work done for a job. Each measure
references one or more replaced components in the pre-retrofit building and one
or more (usually one) installed components in the post-retrofit building. In
cases where a component was installed without replacing an existing comopnent
the ``ReplacedComponent`` can be omitted. Similarly if something was removed
and nothing was installed in its place ``InstalledComponent`` would be omitted.
The measure cost is also included.

From the example file, this measure

.. literalinclude:: /../../examples/audit.xml 
   :language: xml 
   :lines: 600-609 
   :emphasize-lines: 7,9

replaces this furnace in the pre-retrofit building

.. literalinclude:: /../../examples/audit.xml 
   :language: xml 
   :lines: 148-161 
   :emphasize-lines: 2

with this one.

.. literalinclude:: /../../examples/audit.xml 
   :language: xml 
   :lines: 381-394 
   :emphasize-lines: 2


