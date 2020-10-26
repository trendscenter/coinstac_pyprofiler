# python_profiler
Profile your python code (includes code running using coinstac-simulator). This primarily uses pyinstrument profiler, but can also be extended to include other python profilers

## Prerequisites
    Python 3.6+
    Other packages listed in Requirements.txt
    
# Usage
NOTE: The code currently implements profiling based on pyinstrument profiler. Other profilier (such as cprofile) can be included based on requirements. 
## First way: 
Use the following line above the method definition which needs to be profiled.

```python
@profile(type="pyinstrument", output_file_prefix=output_file_prefix)
```

Decorator class to profile any method.
Note: 'output_file_prefix' should include its (absolute) directory path


## Second way: 
Create object of Profile class in custom_profiler.py and use start() and stop() methods to control profiling. 


# Merging multiple profile output files
Merges the json profiler output files generated using pyinstrument profiling and saves merged output.

## Use-case:
For a computation in coinstac-simulator, some computation has many iterations and every iteration of python call generates a separate profile json output file. All such json files can be merged separately for each client/remote using this call.

## Example
An example usage is included in examples/profiler_usage.py which demonstrates how to use the above mentioned profiling methods and also merging multiple profile output files.

Happy profiling!!
