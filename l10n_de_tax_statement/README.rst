.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=========================
German Tax Statement
=========================

This module provides you with the Tax Statement in German format.

Installation
============

* This module depends from module account_tax_balance available at https://github.com/OCA/account-financial-reporting.
* This module also depends from module date_range that is supported as of postgresql 9.2 or later versions.

Configuration
=============

This module depends on the tax tags (eg.: 81, 86, 89, 91, 61...) as prescribed by the german tax laws.

If the default Odoo German chart of accounts is installed (module l10n_de) then these tags are automatically present in the database.
If this is the case, go to menu: Invoicing -> Configuration -> Accounting -> German Tax Tags, and check that the tags are correctly set; click Apply to confirm.

If a non-standard chart of accounts is installed, you have to manually create the tax tags and properly set them into the tax definition.
After that, go to go to menu: Invoicing -> Configuration -> Accounting -> German Tax Tags, and manually set the tags in the configuration form; click Apply to confirm.

Usage
=====

#. Verify that you have enough permits. You need to belong at least to the Accountant group.
#. Go to the menu: Invoicing -> Reports > Taxes Balance > DE Tax Statement
#. Create a statement, providing a name and specifying start date and end date
#. Press the Update button to calculate the report: the report lines will be displayed in the tab Statement
#. Eventually you have to manually enter the Tax amounts of lines in Edit mode, click on the amount of the line to be able to change it)
#. Press the Post button to set the status of the statement to Posted; the statements set to this state cannot be modified anymore
#. If you need to recalculate or modify or delete a statement already set to Posted status you need first to set it back to Draft status: press the button Reset to Draft
#. If you need to print the report in PDF, open a statement form and click: Print -> DE Tax Statement



Known issues / Roadmap
======================

* Exporting formats not yet available
* Including in the report being created, not only the data filtered by the selected date range, but also all the old data that was not included in the previous tax declarations (work in progress...)


Credits
=======

Contributors
------------
* Thorsten Vocks <thorsten.vocks@openbig.org>
* Andrea Stirpe <a.stirpe@onestein.nl>
* Antonio Esposito <a.esposito@onestein.nl>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is not yet maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org or the corresponding github repository. 
