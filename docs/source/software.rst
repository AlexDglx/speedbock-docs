Software
========

.. _installation:

Installation
------------

Installing `speedbocktech` module:

.. tab-set::

    .. tab-item:: pip

      .. code-block:: console

            (.venv) $ pip install speedbocktech

    .. tab-item:: conda

      .. code-block:: console
            
            (.venv) $ conda install speedbocktech

.. note::
   The module is a wrapper for the speedbocktech c library.
   It is recommended creating a virtual environment before installing the package.

All sensors are accessible using the module's functions. The output result is generally a dictionary.


Sensors
-------
All sensors come pre-calibrated, it's possible to set your own calibration for your specific application.

.. note::
   Reverting to factory settings is possible at any moment. Add page to manual reset.
   

Environment
~~~~~~~~~~~


Enclosure
---------
Offsets
~~~~~~~

Routes
------
Create
~~~~~~

Export
~~~~~~

Downloading Files
-----------------
Format
~~~~~~

Custom Calibration
------------------

Pre-installed calibrations are stored in `/device/cal/factory` and cannot be deleted.
Store your custom calibrations in `/device/cal/custom` to override the factory calibrations.

Camera
~~~~~~

Proximity Sensor
~~~~~~~~~~~~~~~~

IMU
~~~

Temperature
~~~~~~~~~~~
