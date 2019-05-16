from load_yaml_config import load_yaml_config


class SVJObject(object):
    def __init__(self, config):
        self.config = config
        self.in_params = load_yaml_config(self.config)
        self.n_jobs = in_params['n_jobs']

    def gridpack_stage(self):
        self.process_type = self.in_params['process_type']
        self.m_med = self.in_params['m_med']
        self.n_events = self.in_params['n_events']
        self.m_d = self.in_params['m_d']
        self.r_inv = self.in_params['r_inv']

    def lhe_stage(self):
        self.model_name = self.in_params['model_name']
        self.total_events = self.in_params['total_events']
        self.split_lhe_file_path = self.in_params['lhe_file_path']

    def full_sim_stage(self):
        self.work_space = self.in_params['work_space']
        self.lhe_file_path = self.in_params['lhe_file_path']
        self.n_events = self.in_params['n_events']
        self.model_name = self.in_params['model_name']
        self.alpha_d = self.in_params['alpha_d']
        self.m_d = self.in_params['m_d']
        self.n_f = self.in_params['n_f']

# FINISH
