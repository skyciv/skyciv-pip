# The SkyCiv Pip Package

This package provides helpful tools to create objects and interact with the SkyCiv API. These components can be used to quickly construct models by providing code completion, parameter information and examples.

>***Note: We strongly recommend using VSCode and the Pylance plugin for VSCode. Pylance is still in preview mode and requires some polishing however, it will help provide intellisense options as seen in the image below.***

<div style="text-align: center;">
    <img style="max-width: 100%" src="https://github.com/skyciv/skyciv-pip/raw/master/img/intellisense.png"/>
</div>

----

## Documentation

The SkyCiv API documentation can be found here: https://skyciv.com/api/v3/

The Python Pip package documentation is a work in progress but for now, you can refer to the [JavaScript package docs](https://skyciv.com/api/v3/docs/packages/#npm---javascript) which are not exactly the same but very similar. The main difference being that methods use `snake_case` in python rather than `camelCase` in JavaScript.

For example, `sections.loadCustomFromLibrary()` in the NPM package would translate to `sections.load_custom_from_library()` for the Pip package.

----

## Install

```
pip3 install skyciv
```

----

## Example

The recommended use of this package is by using the `Model()` and `ApiObject()` classes.

```py
import skyciv

# Create an instance of the Model class
model = skyciv.Model("metric")

# Nodes
model.nodes.add(0, 0, 0)
model.nodes.add(0, 0.5, 0)
model.nodes.add(0, 1, 0)
model.nodes.add(0.5, 1, 0)
model.nodes.add(0.5, 0.5, 0)
model.nodes.add(1, 0.6, 0)
model.nodes.add(1, 0.1, 0)
model.nodes.add(1.5, 0.1, 0)
model.nodes.add(1.5, 0.6, 0)
model.nodes.add(1.5, 0, 0)
model.nodes.add(1.5, -0.4, 0)
model.nodes.add(1, -0.6, 0)
model.nodes.add(2, 0, 0)
model.nodes.add(2, 0.7, 0)
model.nodes.add(2, 1, 0)
model.nodes.add(1.7, 0.7, 0)
model.nodes.add(2.3, 0.7, 0)
model.nodes.add(2.5, 1, 0)
model.nodes.add(2.5, 0.5, 0)
model.nodes.add(2.5, 0, 0)
model.nodes.add(3, 0.5, 0)
model.nodes.add(3, 0, 0)
model.nodes.add(3.3, 0.5, 0)
model.nodes.add(3.3, 0.14, 0)
model.nodes.add(3.7, 0.14, 0)
model.nodes.add(3.7, 0.5, 0)
model.nodes.add(4, 0.5, 0)
model.nodes.add(4, 0.4, 0)
model.nodes.add(4, 0, 0)
model.nodes.add(4.5, 0.5, 0)
model.nodes.add(4.5, 0, 0)
model.nodes.add(-0.5, 0, 0)
model.nodes.add(3.3, 0, 0)
model.nodes.add(3.7, 0, 0)
model.nodes.add(4.9, 0, 0)

# Members
model.members.add(1, 2, 1)
model.members.add(2, 3, 1)
model.members.add(3, 4, 1)
model.members.add(4, 5, 1)
model.members.add(5, 2, 1)
model.members.add(6, 7, 1)
model.members.add(7, 8, 1)
model.members.add(8, 9, 1)
model.members.add(8, 10, 1)
model.members.add(10, 11, 1)
model.members.add(11, 12, 1)
model.members.add(15, 14, 1)
model.members.add(14, 13, 1)
model.members.add(16, 14, 1)
model.members.add(14, 17, 1)
model.members.add(18, 19, 1)
model.members.add(19, 20, 1)
model.members.add(19, 21, 1)
model.members.add(21, 22, 1)
model.members.add(24, 25, 1)
model.members.add(25, 26, 1)
model.members.add(26, 23, 1)
model.members.add(23, 24, 1)
model.members.add(27, 28, 1)
model.members.add(28, 29, 1)
model.members.add(28, 30, 1)
model.members.add(30, 31, 1)
model.members.add(32, 1, 2)
model.members.add(1, 10, 2)
model.members.add(10, 13, 2)
model.members.add(13, 20, 2)
model.members.add(20, 22, 2)
model.members.add(22, 33, 2)
model.members.add(33, 34, 2)
model.members.add(34, 29, 2)
model.members.add(29, 31, 2)
model.members.add(31, 35, 2)
model.members.add(24, 33, None, "FFFfff", "FFFfff", "rigid")
model.members.add(25, 34, None, "FFFfff", "FFFfff", "rigid")

# Plates
model.plates.add([5, 4, 3, 2], 12, 1, is_meshed=True)

# Meshed plate
model.meshed_plates.add(1, 5, 4, 3, 2)

# Sections
model.sections.add_library_section(
    skyciv.sections.Australian_Steel_300_Grade_CHS_Grade_350_101_6x3_2_CHS, 1)
model.sections.add_library_section(
    skyciv.sections.Australian_Steel_300_Grade_Universal_beams_150_UB_14_0, 1)

# Material
model.materials.add("Structural Steel")
# or : model.materials.addCustom("Custom Steel", 7850, 210000, 0.29, 300, 440, "steel")

# Supports
model.supports.add(32, "FFFFRR")
model.supports.add(35, "FFFFRR")

# Settlements
model.settlements.add(35, ty=-10)

# Add point load
model.point_loads.add("m", member=3, position=30.4, y_mag=-5, load_group="LG1")
model.point_loads.add("n", node=13, y_mag=1.6, load_group="LG1")
model.point_loads.add("n", node=12, y_mag=-3.7, load_group="LG1")

# Add moment
model.moments.add("n", node=12, y_mag=0.3, load_group="LG1")
model.moments.add("m", member=16, position=0, x_mag=-0.1, load_group="LG1")

# Add distributed load
model.distributed_loads.add(32, y_mag_A=-10, y_mag_B=-2, position_B=100, load_group="LG1")

# Pressure
model.pressures.add(1, "global", 0, 0, 0.1, "LG1")

# Area load
model.area_loads.add("one_way", [23, 24, 25, 26], 1.3, "Z", column_direction=[23, 26], LG="LG1")

# Selfweight
model.self_weight.add(y=-1, LG="SW1")

# Make a load combination
model.load_combinations.add("SW1 + LG1", {"SW1": 1, "LG1": 1})

# Create an API Object
ao = skyciv.ApiObject()

# Set auth
ao.auth.username = "YOUR_SKYCIV_USERNAME"
ao.auth.key = "YOUR_SKYCIV_API_KEY"

# Set functions
ao.functions.add("S3D.session.start", {"keep_open": True})
ao.functions.add("S3D.model.set", {"s3d_model": model})
# Uncomment the next line to run a solve as well.
# ao.functions.add("S3D.model.solve", {"analysis_type": "linear"})
ao.functions.add("S3D.file.save", {"name": "package-debut", "path": "api/PIP/"})

res = ao.request()

print(res["response"])
```

Now, we can even view the model in [S3D](https://platform.skyciv.com/structural).
<div style="text-align: center;">
    <img style="max-width: 100%" src="https://github.com/skyciv/skyciv-pip/raw/master/img/result-in-s3d.png"/>
</div>

----

## Sections Database

Section library paths for all sections can be found in the `skyciv.sections` object.

For example:

By typing something like this: `skyciv.sections.aus300150ub`.

<div style="text-align: center;">
    <img style="max-width: 100%" src="https://github.com/skyciv/skyciv-pip/raw/master/img/sections-autocomplete.png"/>
</div>

Intellisense will offer the closest sections which you can select with autocompletion. Resulting in the path shown below.

```py
path = skyciv.sections.Australian_Steel_300_Grade_Universal_beams_150_UB_14_0

# path is now equal to:
["Australian", "Steel (300 Grade)", "Universal beams", "150 UB 14.0"]
```

Although it does not look great, this way, auto completion will ensure the string arrays are correct.

----

## Global Methods

### `skyciv.request(api_object, options?)`
Make a request to the SkyCiv API.

```py
skyciv_response = skyciv.request(api_object, options)
# Do something with the response
```

#### Options (optional dictionary)

* *version* - _2 | 3_ (Defaults to 3)
* *http_or_https* - _http | https_ (Defaults to https)

```py
options = {
    "http_or_https": "http",
    "version": 3,
}
```

----

## Manually building the API Object
Visit the [API docs](https://skyciv.com/api/v3/docs/getting-started) for instructions on how to create an instance of the SkyCiv API object.

----

## Changelog

| Version  | Breaking          | Description     |
| :---     | :---              | :---            |
| 1.1.3    | Breaks `model.self_weight`. | • `Model().set` method now can now accept a downloaded JSON model from platform.skyciv.com/structural.<br/>• Fixed self_weight data structure.<br/>• `Functions` and `Function` class now defaults `args` to an empty object.|
| 1.1.2    | false             | • Typos.<br/>• Improved in-code docs.<br/>• Fixed Canadian bridging channel lookup in `skyciv.sections`.<br/>• The `request()` method of the `ApiObject()` will now automatically store the `last_session_id` to the `auth.session_id` property of the `ApiObject` instance. |
| 1.1.1    | false             | • README.md patch. |
| 1.1.0    | false             | • Added 37 new classes including the `ApiObject()` and `Model()` classes. |
| 1.0.4    | false             | • Package will now only use dumps on input if `api_object` is not a string. |
| 1.0.3    | false             | • Fixed options dictionary to be optional. |
| 1.0.2    | false             | • Updated readme. |
| 1.0.1    | false             | • Changed `skyciv.request()`. to print msg if SkyCiv returns error rather than throw an exception. |
| 1.0.0    | -                 | Initial release. |