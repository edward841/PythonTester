# PythonTester

The goal of this project is to create a tool to help the programmer measure 
and visualize runtime of a Python3 program, as well as compare it with the 
runtime of previous versions.

Simply add the recordtime decorator to the function(s) you want to time and track.
When that function is evaluated, the recordtime decorator will measure the execution
time of the given function in CPU time (seconds) and save it to the given output CSV
file. It is possible to limit the number of data points it saves for any one input
and by default limits it to 10 points. You could specify a different limit or set
maximum=None to disable limiting data points.

## Data Organization

Using recordtime will create a csv file that it will save the data in, so that you can
view or process that data as you see fit. In a given file, the structure of the data 
is as follows:


| Version | 1 | | |
| --- | --- | --- | --- |
| Test | Input | R1 | R2 |
| 1 | A | x1 | x2 |  
| 2 | B | y1 | y2 |
| Version | 2 | | |
| Test | Input | R1 | R2 |
| 1 | A | a1 | a2 |  
| 2 | B | b1 | b2 |


Each version represents a different version of the program, the A and B are the input that 
the function was called with, and the values in columns R1 and R2 represent runtimes (x2 
is the runtime of the first version, the second time the function was run with input A).

## Implemented

The module for measuring and recording the runtime in a separate csv file

## Not yet implemented

The module that generates visuals
