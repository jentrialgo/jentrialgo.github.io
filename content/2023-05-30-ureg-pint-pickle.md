Title: Reading units from a pickle file with Pint
Date: 2023-05-30 12:00
Category: Pylance, Python, Pint
Tags: Pylance, Python, Pint

I have a Python package called cloudmodel that uses Pint to define units and adds some to
the default registry. When I read a pickle file that use these units, I get an error:


    int.errors.UndefinedUnitError: 'usd' is not defined in the unit registry

The way to fix it is to set the application registry to the one used by cloudmodel:

```python
from cloudmodel.unified.units import ureg
from pint import set_application_registry

set_application_registry(ureg)
```
