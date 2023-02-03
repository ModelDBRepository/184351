'''
Defines a class, Neuron473465774, of neurons from Allen Brain Institute's model 473465774

A demo is available by running:

    python -i mosinit.py
'''
class Neuron473465774:
    def __init__(self, name="Neuron473465774", x=0, y=0, z=0):
        '''Instantiate Neuron473465774.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron473465774_instance is used instead
        '''
               
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Pvalb-IRES-Cre_Ai14_IVSCC_-172096.04.02.01_471781218_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
 
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron473465774_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im_v2', u'K_T', u'Kd', u'Kv2like', u'Kv3_1', u'NaV', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 80.33
            sec.e_pas = -92.1046676636
        
        for sec in self.axon:
            sec.cm = 1.22
            sec.g_pas = 0.000983985162724
        for sec in self.dend:
            sec.cm = 1.22
            sec.g_pas = 2.00484449065e-06
        for sec in self.soma:
            sec.cm = 1.22
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Ih = 2.23256e-05
            sec.gbar_NaV = 0.027629
            sec.gbar_Kd = 0.000113507
            sec.gbar_Kv2like = 0.054829
            sec.gbar_Kv3_1 = 0.850178
            sec.gbar_K_T = 0.000502729
            sec.gbar_Im_v2 = 0.00228453
            sec.gbar_SK = 0.00035096
            sec.gbar_Ca_HVA = 2.2976e-06
            sec.gbar_Ca_LVA = 0.00350418
            sec.gamma_CaDynamics = 0.013685
            sec.decay_CaDynamics = 50.7555
            sec.g_pas = 1.63222e-06
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

