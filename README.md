# Create python package

##  Create package directory structure
```
SamplePackage/
    SamplePackage/
        __init__.py
    setup.py
```

## Define setup file
`setup.py` is the build script for setuptools. It tells setuptools about your package (such as the name and version) as well as which code files to include.

## define __init__ file
When you import your package, methods or variable from this file will be exported.  

## Load module using pip
`pip install .`

## Test module
Open python terminal 

```
$python3
```

Run following commands
```
import SamplePackage as sp
sp.getCarName()
sp.getPersonName()
```
