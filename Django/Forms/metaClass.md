# Meta Class

- The Meta class of Models and ModelForms can be thought of as something similar to a class or function decorator
- Meta class is simply an inner class.
- In Django, the use of Meta class is simply to provide metadata to the ModelForm class.
- The Meta class is referenced during the construction of the form/object instance before the class definition itself.
- You could try to do the same work by overriding the class __init__ function, but 1) that would be a lot of extra work to replicate something already being done for you by the Meta class, and 2) any such implementation is unlikely to be as efficient or clean as the Meta class.
- It is different from metaclass of a Class in Python.

## metadata of a ModelForm

Any information that is “not a form Field” can be considered as metadata. Django provides sensible defaults to all fields. But if you want to override the default behavior of fields, you can define the corresponding meta options. Some meta options are compulsory.For example:

- model: Model class to use for creating Form
- fields: list to fields to include in the Form
- exclude: list of fields to exclude from the Form
- widgets: a dictionary of field-widget pairs

And so on, there are many more meta options you can define inside Meta class.

## Why Meta class is used to define the meta information? Why not simply define them as class attributes?

It was more of a design decision to use Meta. You can access the contents of inner class from Outer class. It provides a cleaner API and keeps fields (which are the crux of any form) and the form configuration options separate.

In general, inner class are avoided in Python and they don’t provide any huge advantage but do cause some minor inconveniences.
