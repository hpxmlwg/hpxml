Audit-Upgrade
#############

.. contents::

The audit and upgrade datasets cover two scenarios:

#. A baseline building with a proposed work scope (see :ref:`audit-use-case-defn`)
#. A baseline building with a completed work scope (see :ref:`upgrade-use-case-defn`)

Both datasets describe a pre- and post-upgrade building and actions (or upgrades) that occur during both states. To accurately describe these scenarios, the HPXML document needs to have the
:ref:`top level nodes <top-level-nodes>` as described below. 

All XML examples are taken from the ``examples/audit.xml`` document. It contains
all of the required fields defined in the Audit dataset.

Contractor
**********

The ``Contractor`` elements should identify the name of the contractor (the person
who is proposing and or completing the work), company and the email address.

.. literalinclude:: /../../examples/audit.xml
   :language: xml
   :lines: 12-32
   :dedent: 2
   :emphasize-lines: 11-12,15

Customer
********

The customer is the homeowner or resident. The ``Customer`` element should
include the customer's name and phone number.

.. literalinclude:: /../../examples/audit.xml
   :language: xml 
   :dedent: 2
   :start-at: <Customer>
   :end-at: </Customer>
   :emphasize-lines: 6-7,10

Building
********

There are two ``Building`` nodes in the Audit and Upgrade document: pre-
and post-upgrade. Each document includes a full description the house. The pre-upgrade condition of the house in the Audit dataset is the house prior to any work being completed on it (existing condition). The post-upgrade
condition of the house describes the proposed work scope, usually completed by the contractor. 

The pre-upgrade condition of the house in the Upgrade dataset is the state of the house prior to the completion of any work (existing condition). The post-upgrade condition of the house state describes the building after work has been completed.

.. _preupgrade:

Pre-upgrade
===========

The pre-upgrade ``Building`` element comes first in the document. It describes
the initial state of the building (prior to work being completed). It should have a ``ProjectStatus/EventType``
of ``audit``. 

.. literalinclude:: /../../examples/audit.xml
   :language: xml 
   :dedent: 2
   :lines: 47-48,59-61,302
   :emphasize-lines: 4

Many items within the building require a unique ``SystemIdentifier`` element.
The ``id`` attribute is used to specify this ID within the document (see
:ref:`id-idref`). 

For example, the water heater in the pre-upgrade building has an id of ``dhw1``.

.. literalinclude:: /../../examples/audit.xml
   :language: xml
   :dedent: 10
   :lines: 244-250
   :emphasize-lines: 2

.. _postupgrade:
   
Post-upgrade
============

The post-upgrade ``Building`` element appears second in the document. It
describes the "after" state of the building. In the audit dataset, that means
the *proposed* improvements to the building (e.g., what the building would look like after proposed work has been completed). In the upgrade dataset, that means the *actual* condition of the building after the work is
completed. The ``ProjectStatus/EventType`` element has a different value
depending on the scenario:

.. table:: Post-upgrade Event Types
   
   ========  =======================================
   Use Case  Event Type
   ========  =======================================
   Audit     proposed workscope
   Upgrade   job completion testing/final inspection
   ========  =======================================

The post-upgrade building is mostly a duplicate of the pre-upgrade building; components of the building that do not change remain the same. However, each component in the post-upgrade building needs a unique identifier that is
different from the unique identifier in the pre-upgrade building. The
``retrofit_id`` attribute of the ``SystemIdentifier`` element is used to link
identical elements in the pre- and post-upgrade buildings (see :ref:`retrofit_id`).

Going back to the water heater example, the water heater in the post-upgrade
building has a different ``id`` than the identical water heater in the
pre-upgrade building, but it has a ``retrofit_id`` attribute to link it back to the
pre-upgrade water heater and indicate it is indeed the same equipment.

.. literalinclude:: /../../examples/audit.xml
   :language: xml
   :dedent: 10
   :lines: 500-506
   :emphasize-lines: 2

.. note::

   When a measure changes a component between a pre- and post-upgrade building,
   the ``SystemIdentifier/@retrofit_id`` attribute is omitted because the measure
   references the relationship between components.

Project
*******

In this paradigm, the :ref:`preupgrade` and :ref:`postupgrade` building elements
describe the state of the building at points in time. The ``Project`` element
describes what was done, or is planning to be done, to the building to get from one scenario to another. 

``PreBuildingID`` and ``PostBuildingID`` are used to reference the pre- and post-
building ids, respectively.

.. literalinclude:: /../../examples/audit.xml
   :language: xml
   :dedent: 2
   :lines: 611-618,664-665
   :emphasize-lines: 2-4

Energy Savings
==============

``EnergySavingsInfo`` is used to transfer either or both the estimated or
measured energy use and savings achieved in an upgrade. 

.. literalinclude:: /../../examples/audit.xml
   :language: xml
   :dedent: 6
   :start-at: <EnergySavingsInfo>
   :end-at: </EnergySavingsInfo>

.. note::

   All percentages are expressed in the form of fractions (i.e., 10% => 0.1)

Measures
========

The ``Measure`` element describes work completed for a job. Each measure
references one or more replaced components in the pre-upgrade building and one
or more (usually one) installed components in the post-upgrade building. 

In cases where a measure was installed without replacing an existing measure or component,
the ``ReplacedComponent`` can be omitted. Similarly, if a component was removed
and nothing was installed in its place, ``InstalledComponent`` would be omitted.
The measure cost is also included in these files.

From the example file below, this measure replaces this furnace in the pre-upgrade building with this one.

.. literalinclude:: /../../examples/audit.xml 
   :language: xml
   :dedent: 8
   :lines: 651-662
   :emphasize-lines: 7,10


.. literalinclude:: /../../examples/audit.xml 
   :language: xml 
   :dedent: 12
   :lines: 170-183 
   :emphasize-lines: 2


.. literalinclude:: /../../examples/audit.xml 
   :language: xml
   :dedent: 12
   :lines: 426-439
   :emphasize-lines: 2


