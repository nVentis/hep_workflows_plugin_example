# hep_workflows_plugin_example

This repository shows how to use hep_workflows for your own analyses.

## Setup

Create an `.env` file in this directory with the following variables: 

1. one of `SH_ENVIRONMENT_FILE/K4H_NIGHTLY/K4H_RELEASE`:

    - `K4H_NIGHTLY`: a specific key4hep nightly version; run `source /cvmfs/sw-nightlies.hsf.org/key4hep/setup.sh --list-releases` for a list. `LATEST` is also an allowed value
    - `K4H_RELEASE`: a specific key4hep release version; run `source /cvmfs/sw-nightlies.hsf.org/key4hep/setup.sh --list-releases` for a list. `LATEST` is also an allowed value
    - `SH_ENVIRONMENT_FILE`: absolute path to a shell file that sources your environment; in this case we require that it is based on key4hep (by checking that `KEY4HEP_STACK` is defined)

2. `PYTHON_ENVIRONMENT_PATH`: absolute path to a python virtual environment (i.e. the directory containing a `bin` directory).
3. `DATA_PATH`: absolute path to a writable directory (preferably with loads of space :))

Make sure the Python environment is set up using the Python executable provided by the key4hep stack you're using. If you have not yet set it up, load the key4hep stack first, then run `python -m venv anavenv && echo "PYTHON_ENVIRONMENT_PATH=\"$(pwd)/anavenv\""`. This will create a virtual environment with name `anavenv` and print a line `PYTHON_ENVIRONMENT_PATH="<some value>"` that you can paste into your `.env` file.

You should now have two lines in your `.env` file. Continue in a new shell.

To install the software dependencies, run `source workflows/setup.sh && pip install -r requirements.txt`

## Examples

The following examples illustrate how to use `hep_workflows` and `AnalysisConfigurations` to run common tasks around event generation, simulation, reconstruction and analysis in a straightforward manner.

### SGV fast simulation of 250 GeV ZH samples with ILD@FCCv01

This example shows how to run SGV fast simulation using a custom detector geometry on pre-generated ILC MC truth samples at 250 GeV COM energy. The sample base path (the directory including the ILC mc-2020 and other MC productions) is assumed to be located at `ILC_PROD_PATH`; add this path to your `.env` file.

An example configuration is included in `workflows/configurations/config_250_zh_ildfccv01_pre_generated_fast_perf.py`. It shows how to change parameters of SGV such as the geometry file, input files and calorimeter simulation. 

In a clean shell, running `source workflows/setup.sh` and then `law run FastSimSGV --tag=250-zh-ildfccv01-pg-fast-perf` should schedule the job submission

### Event generation and SGV fast simulation with ILD@ILC at 550 GeV

TODO

For now, examples can be found in the ZHH analysis repository here: https://github.com/ILDAnaSoft/ZHH/blob/main/workflows/analysis/configurations.py .

### Event generation and full simulation and reconstruction with ILD@ILC at 500 GeV

TODO

For now, this example can be found here: https://github.com/nVentis/hep-workflows/blob/main/hep_workflows/tests/test_e500_zh_full.py