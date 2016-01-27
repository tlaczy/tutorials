Observation processing using GAWK and Octave
===========================================

    :Authors: **Zoltan Siki** <siki.zoltan@epito.bme.hu>
    :Version: 1.0

Preface
-------

GNU AWK (named after the creators Aho, Kernighan, and Weinberger) is a 
Unix/Linux programable text utility what is compiled for Windows platforms, too.
The GAWK program syntax is similiar to C language.

GNU Octave is an open source high-level interpreted language, primarily 
intended for numerical computations. The syntax of the Octave program is 
quite similiar to Matlab, you can easy port programs between GNU Octave and
Matlab.

Samples mostly concern on observation data/file processing.

Samples were tested on Linux but should run on a Windows box, too.
Octave .m files may need some editing to run with Maplab. We some up some
incompatibilities between Octave and Matlab in the following table.

+--------------------------+---------------------+---------------------+
| **Operation**            | **Octave**          | **Matlab**          |
|                          |                     |                     |
+==========================+=====================+=====================+
| Denial                   | !                   | ~                   |
|                          | *or*                |                     |
|                          | ~                   |                     |
|                          |                     |                     |
+--------------------------+---------------------+---------------------+
| Not equal                | !=                  | ~=                  |
|                          | *or*                |                     |
|                          |                     |                     |
|                          | ~=                  |                     |
|                          |                     |                     |
+--------------------------+---------------------+---------------------+
| Increment                | i++                 | i = i + 1           |
|                          | *or*                |                     |
|                          | i += 1              |                     |
|                          | *or*                |                     |
|                          | i = i + 1           |                     |
|                          |                     |                     |
+--------------------------+---------------------+---------------------+
| Power                    | ^                   | ^                   |
|                          | *or*                |                     |
|                          | **                  |                     |
|                          |                     |                     |
+--------------------------+---------------------+---------------------+
| Standard output          | printf('Hello')     | fprintf('Hello')    |
|                          | *or*                |                     |
|                          | fprintf('Hello')    |                     |
|                          |                     |                     |
+--------------------------+---------------------+---------------------+
| String constants         | "Hello"             | 'Hello'             |
|                          | *or*                |                     |
|                          | 'Hello'             |                     |
|                          |                     |                     |
+--------------------------+---------------------+---------------------+
| String search            | index(str, sample)  | strfind(str, sample)|
|                          | *or*                |                     |
|                          | strfind(str, sample)|                     |
|                          | *or*                |                     |
|                          | findstr(str, sample)|                     |
|                          |                     |                     |
+--------------------------+---------------------+---------------------+
| End of code block        | end                 | end                 |
|                          | *or*                |                     |
|                          | endif               |                     |
|                          | endwhile            |                     |
|                          | endfunction         |                     |
|                          |                     |                     |
+--------------------------+---------------------+---------------------+
| Comment                  | #                   | %                   |
|                          | *or*                |                     |
|                          | %                   |                     |
|                          |                     |                     |
+--------------------------+---------------------+---------------------+
| Comment block            | %{                  | %{                  |
|                          | ...                 | ...                 |
|                          | %}                  | %}                  |
|                          | *or*                |                     |
|                          | #{                  |                     |
|                          | ...                 |                     |
|                          | #}                  |                     |
|                          |                     |                     |
+--------------------------+---------------------+---------------------+
| Line continuation        | ...                 | ...                 |
| (at the end of line)     | *or*                |                     |
|                          | \                   |                     |
|                          |                     |                     |
+--------------------------+---------------------+---------------------+

IF you would like to use a script in Matlab, too use Octave with the
*--traditional* command line switch. This way you will get warnings in case of
Maplab incompatible structures.

*Knowlage covered*

*   using pipelines, redirecting standard input and output (Unix/DOS)
*   using simple text processing utilities (grep, gawk, etc.)
*   using file input/output
*   using variables, expressions, decision control (conditional statement, loops), functions
*   using regular expressions
*   extending Octave/Matlab knowlage
*   vectorization

.. toctree::
    :maxdepth: 2

    leica_gsi
    leica_dna03
    gpx
    nmea
    monitoring_data
    prism
    lidar
    one_point
    level_net
    propagation_of_error
    coord_list
    mnea_stat
    polinom
    pseudo_inverz