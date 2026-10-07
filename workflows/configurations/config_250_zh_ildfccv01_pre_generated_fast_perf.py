from hep_workflows import AnalysisConfiguration, configurations
from glob import glob
from os import environ, path as osp
from os.path import expandvars

def glob_exp(x, **kwargs):
    return glob(expandvars(x), **kwargs)

# The following configuration runs the ILD@FCC

class Config_250_zh_ildfccv01_pre_generated_fast_perf(AnalysisConfiguration):
    tag = '250-zh-ildfccv01-pg-fast-perf'
    sqrt_s = 250

    def __init__(self):
        self.task_kwargs:dict[str, dict] = {
            # configure FastSimSGV
            'FastSimSGV': {
                'geometry_file': expandvars('$HEP_WORKFLOWS_PLUGIN_ROOT/workflows/resources/sgv/sgv_geo_ildfcc_v1.inp')
            }
        }
    
    def sgv_inputs(self, fast_sim_task):
        input_files = []
        base = '$ILC_PROD_PATH/mc-2020/generated/250-SetA/higgs'
        
        for mask in ['Pe2e2h']:
            input_files += glob_exp(f'{base}/*{mask}*.slcio')
        
        input_files.sort()

        # check the SGV steering file for more info 
        input_options = [{
            'global_steering.MAXEV': 999999,
            'global_generation_steering.CMS_ENE': self.sqrt_s,
            'external_read_generation_steering.GENERATOR_INPUT_TYPE': 'LCIO',
            'external_read_generation_steering.INPUT_FILENAMES': 'input.slcio', # do not change
            'analysis_steering.CALO_TREATMENT': 'PERF'
        }] * len(input_files)
        
        return input_files, input_options

configurations.add(Config_250_zh_ildfccv01_pre_generated_fast_perf())