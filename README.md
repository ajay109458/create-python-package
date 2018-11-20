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

## Create a package 
```
python setup.py sdist
```

It creates a tar package, eg. SamplePackage-0.1.tar.gz

## Upload package to test pypi repository

Note: Install twine package using pip
```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

## Upload package to pypi repository
```
twine upload dist/*
```

### Install module 
```
pip install SamplePackage
```
