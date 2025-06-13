# sav2csv
# UPDATED TO USE Python3 and Pandas

Converts SPSS ".sav" files to CSV.

    usage: sav2csv [-h] [-f SAV_FILE] [-o OUTPUTDIRECTORY]

    Converts an spss "sav" data file to CSV

    optional arguments:
      -h, --help          show this help message and exit
      -f SAV_FILE         The .sav file to export. If omitted, a graphical file
                          chooser will be used.
      -o OUTPUTDIRECTORY  The output directory. Default is the current directory
                          if SAV_FILE was given, otherwise a file chooser will be
                          used as well.
