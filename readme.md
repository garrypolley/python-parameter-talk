This is a short set of examples to show how Python parameters work. It has a
specific point of showing how kwargs work.

Showing the differences between:

* keyword argument vs keyword parameter
* argument defaults and behavior

## named_parameters.py

Just because have names does not mean you must specify them. These can
be viewed as positional parameters. Note, _all_ parameters are
position, however, some may have default values.

## named_parameters_default_value.py

If a default value is given to a parameter is not a _keyword_ argument.
It is just a parameter with a default value.  This means you do not
need to specify a value for the parameter.

## named_parameters_keyword_arguments.py

The order of keyword arguments is irrelevant.  As long as positional
arguments are satisfied first the ordering of the named parameters with
default values does not matter.

So when using _keyword_ _arguments_ the position of arguments does not matter.

## kwargs.py

A bit on how **kwargs work.  That **kwargs is a special "gobble" up the rest
of the keyword arguments.

## args.py

A bit on how *args work.  That *args is a special "gobble" up the rest of the
positional arguments.

## Default Values

Default values are not always the same.  Python keeps default values assigned
to parameters the same, respecting the rules of mutable data types.

Take a look at `fib.py`, `fib_cached.py`, and `fib_cached_broken.py`.

It's an example of why this behavior can be useful and why it works how
it does work.  Specifically the `known_values` being modified vs reassigned
effects how the default parameter works.  If the value is _reassigned_ it does
not effect the default parameter because the parameter **_is not modified_**.
When `known_values.append` is used the default parameter  **_is changed_**.
This because the actual value is modified.
