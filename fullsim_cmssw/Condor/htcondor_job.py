from cmssw_info import CmsswInfo
import os


class HTCondorJob(object):
    """ Store all the info required to write a HTCondor job file """
    def __init__(self, work_space, gen_frag, lhe_base, model, n_events, year, queue=1, seed=None):
        self.work_space = work_space
        self.gen_frag = gen_frag
        self.lhe_base = lhe_base
        self.model = model
        self.n_events = n_events
        self.year = year
        self.queue = queue
        self.seed = seed

        self.this_dir = os.path.dirname(os.path.realpath(__file__))

        self.disk = 50000 * self.n_events  # kB
        self.runtime = 288 * self.n_events  # seconds. 8 hours/100 events
        self.memory = 5000  # MB

        if 'soolin' in os.environ['HOSTNAME'] or self.lhe_base.startswith('root://'):
            self.grid_proxy = "use_x509userproxy = true"
        else:
            self.grid_proxy = ""

        self.cmssw_info = CmsswInfo(year)
        if self.cmssw_info.gensim['arch'].startswith('slc6'):
            self.job_os = 'SLCern6'
        else:
            self.job_os = 'CentOS7'

        self.write_submission_script()

    def write_submission_script(self):
        """ Write the HTCondor submission script for sample generation """

        body = """# HTCondor submission script
Universe = vanilla
cmd      = {this_dir}/runFullSim_condor_{year}.sh
args     = {work_space} {gen_frag} {lhe_base}_$(Process).lhe {model} {n_events:.0f} $(Process) {cmssw_gensim} {cmssw_aod} {cmssw_nano}
Log      = {work_space}/logs/{model}/condor_job_$(Process).log
Output   = {work_space}/logs/{model}/condor_job_$(Process).out
Error    = {work_space}/logs/{model}/condor_job_$(Process).error
should_transfer_files   = YES
when_to_transfer_output = ON_EXIT_OR_EVICT
{grid_proxy}
# Resource requests (disk storage in kB, memory in MB)
request_cpus = 1
# Disk request size determined by n_events
request_disk = {disk}
request_memory = {memory}
# Max runtime (seconds) determined by n_events
+MaxRuntime = {runtime}
# Require SLC6 machines if needed as CMSSW_7_1_X can't run on SLC7/CentOS7
Requirements = (OpSysAndVer == "{os}")
batch_name = {model}
# Number of instances of job to run
queue {queue}
""".format(this_dir=self.this_dir,
           work_space=self.work_space,
           gen_frag=self.gen_frag,
           lhe_base=self.lhe_base,
           model=self.model,
           n_events=self.n_events,
           disk=self.disk,
           runtime=self.runtime,
           grid_proxy=self.grid_proxy,
           queue=self.queue,
           os=self.job_os,
           year=self.year,
           memory=self.memory,
           cmssw_gensim=self.cmssw_info.gensim['version'],
           cmssw_aod=self.cmssw_info.aod['version'],
           cmssw_nano=self.cmssw_info.nano['version'])

        self.job_file = os.path.join(self.work_space, 'submission_scripts', self.model, 'condor_submission_all.job')
        # Edit submission script file name and body if writing individual files
        if self.seed is not None:
            self.job_file = self.job_file.replace('all.job', '{}.job'.format(self.seed))
            body = body.replace('$(Process)', str(self.seed))

        with open(self.job_file, 'w') as f:
            f.write(body)
