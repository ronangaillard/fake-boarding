# Fake boarding pass generator

## How to use ?
To run the server : 
`python server.py`

Before you should run 
`pip install flask treeopoem` to install dependencies

And manually install Ghostscript on Mac OSX and Linux
`apt-get install ghostscript` or
`brew install ghostscript`

## TODO
* Improve parsing
  * Put names in capital letters
  * Choose date in calendar (and default date is the current day date)
  * Choose airport in a list containing all airport names
  * Same for carriers
  * Enable default values (for check-in number, passenger status,...)
* Scan exisiting bar codes
* Improve general UI

## Known bugs

