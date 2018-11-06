## Dell test case.
Write client-server application.
Use case: application which is used in car centers to store information
about sold cars. At first application will be used in a single car center then
all centers in town/city/world will use it to store information. It should be
possible to retrieve info about any sold car by serialNumber.
Clients pass to server an Object “Car” with following attributes:

```
"ownerName" type="string"
"serialNumber" type="uint64"
"modelYear" type="uint64"
"code" type="string"
"vehicleCode" type="string"
"engine"
    "capacity" type="uint16"
    "numCylinders" type="uint8"
    "maxRpm" type="uint16"
    "manufacturerCode" type="char"
"fuelFigures"
    "speed" type="uint16"
    "mpg" type="float"
    "usageDescription" type="string"
"performanceFigures"
    "octaneRating" type="uint16"
"acceleration"
    "mph" type="uint16"
    "seconds" type="float"
    "manufacturer" type="string"
    "model" type="string"
    "activationCode" type="string"
```

Server saves the information persistently.