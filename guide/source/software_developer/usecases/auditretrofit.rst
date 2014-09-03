Audit-Retrofit
##############

The audit-retrofit use case covers two scenarios:

#. A baseline building with a proposed work scope 
#. A baseline building with a completed work scope

Both scenarios describe a pre- and post-retrofit building and the actions
(measures) that occur between the two states to make the difference. To achieve
this the HPXML document needs to have the following
:ref:`top level nodes <top-level-nodes>`:

* Contractor - who is proposing/doing the work
* Customer - home owner or resident
* Building x 2

   * Pre-retrofit
   * Post-retrofit (proposed or completed)
* Project - Description of measures and :doc:`references <../references>` of 
  affected elements in the pre- and post- buildings.
 
.. literalinclude:: example1.xml
   :language: xml
   :linenos:


