from SamplePackage import firstmodule
from SamplePackage import secondmodule

def getCarDetails():
    car = firstmodule.Car()
    return car.getCarName()

def getPersonDetails():
    person = secondmodule.Person();
    return person.getPersonName()