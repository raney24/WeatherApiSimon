## Scope

A website that displays the current forecast of a city/state. The website also displays future forecasts.

## Features

- User can enter a city/state
- Display current and future forecast for the location 

## Steps

- Get familiar with APIs
- Research weather APIs
- Figure out what stack we want to write in
- Implement API into stack
  - Recieve data from API
  - Call API with specific city
  - Manipulate/Gather all data for forecast
 - Gather user input
 - Display forecast based on user input

## Instructions

1. Run flask server
> $env:FLASK_APP="hello.py"
> flask run

2. Run flask server with debug mode
> $env:FLASK_APP="hello.py"
> $env:FLASK_DEBUG=1
> python -m flask run