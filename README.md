Andrawpick
----------
A simple script to pick Android drawables from a folder and put them into your project.

Usage
-----
Positional arguments

    src                   Source res folder path.

Optional arguments

    -h, --help            show this help message and exit
    -d DEST, --dest DEST  Destination res folder path.
    -f FILE, --file FILE  Filename regex.
    -s SIZES [SIZES ...], --sizes SIZES [SIZES ...] Sizes you want (mdpi, hdpi etc..)

A real life example :) I needed to pick all ic_traffic_white icons from material-design-icons package:

    $ andrawpick material-design-icons-1.0.0/maps/ -f ic_traffic_white --sizes hdpi mdpi

