coupling_orders.pyo                                                                                 0000644 0276724 0002567 00000000753 13234357560 013326  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc        	   @   sq   d  d l  m Z m Z e d d d d d d � Z e d d d d d d	 d
 d	 � Z e d d d d d d � Z d S(   i����(   t
   all_orderst   CouplingOrdert   namet   DMVt   expansion_orderi   t	   hierarchyt   QCDic   i   t   perturbative_expansiont   QEDN(   t   object_libraryR    R   R   R   R   (    (    (    sO   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/coupling_orders.pyt   <module>   s   		                     couplings.py                                                                                        0000644 0276724 0002567 00000030115 13234357560 011747  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     # This file was automatically created by FeynRules 2.4.46
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Thu 27 Oct 2016 23:02:25


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '-G',
                 order = {'QCD':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'G',
                 order = {'QCD':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*G**2)',
                 order = {'QCD':2})

GC_14 = Coupling(name = 'GC_14',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_15 = Coupling(name = 'GC_15',
                 value = 'complex(0,1)*gAd11',
                 order = {'DMV':1})

GC_16 = Coupling(name = 'GC_16',
                 value = 'complex(0,1)*gAd22',
                 order = {'DMV':1})

GC_17 = Coupling(name = 'GC_17',
                 value = 'complex(0,1)*gAd31',
                 order = {'DMV':1})

GC_18 = Coupling(name = 'GC_18',
                 value = 'complex(0,1)*gAd33',
                 order = {'DMV':1})

GC_19 = Coupling(name = 'GC_19',
                 value = 'complex(0,1)*gAl11',
                 order = {'DMV':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'complex(0,1)*gAl22',
                 order = {'DMV':1})

GC_21 = Coupling(name = 'GC_21',
                 value = 'complex(0,1)*gAl33',
                 order = {'DMV':1})

GC_22 = Coupling(name = 'GC_22',
                 value = 'complex(0,1)*gAu11',
                 order = {'DMV':1})

GC_23 = Coupling(name = 'GC_23',
                 value = 'complex(0,1)*gAu22',
                 order = {'DMV':1})

GC_24 = Coupling(name = 'GC_24',
                 value = 'complex(0,1)*gAu31',
                 order = {'DMV':1})

GC_25 = Coupling(name = 'GC_25',
                 value = 'complex(0,1)*gAu33',
                 order = {'DMV':1})

GC_26 = Coupling(name = 'GC_26',
                 value = 'complex(0,1)*gAXd',
                 order = {'DMV':1})

GC_27 = Coupling(name = 'GC_27',
                 value = 'complex(0,1)*gnu11',
                 order = {'DMV':1})

GC_28 = Coupling(name = 'GC_28',
                 value = 'complex(0,1)*gnu22',
                 order = {'DMV':1})

GC_29 = Coupling(name = 'GC_29',
                 value = 'complex(0,1)*gnu33',
                 order = {'DMV':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = 'complex(0,1)*gVd11',
                 order = {'DMV':1})

GC_31 = Coupling(name = 'GC_31',
                 value = 'complex(0,1)*gVd22',
                 order = {'DMV':1})

GC_32 = Coupling(name = 'GC_32',
                 value = 'complex(0,1)*gVd31',
                 order = {'DMV':1})

GC_33 = Coupling(name = 'GC_33',
                 value = 'complex(0,1)*gVd33',
                 order = {'DMV':1})

GC_34 = Coupling(name = 'GC_34',
                 value = 'complex(0,1)*gVl11',
                 order = {'DMV':1})

GC_35 = Coupling(name = 'GC_35',
                 value = 'complex(0,1)*gVl22',
                 order = {'DMV':1})

GC_36 = Coupling(name = 'GC_36',
                 value = 'complex(0,1)*gVl33',
                 order = {'DMV':1})

GC_37 = Coupling(name = 'GC_37',
                 value = 'complex(0,1)*gVu11',
                 order = {'DMV':1})

GC_38 = Coupling(name = 'GC_38',
                 value = 'complex(0,1)*gVu22',
                 order = {'DMV':1})

GC_39 = Coupling(name = 'GC_39',
                 value = 'complex(0,1)*gVu31',
                 order = {'DMV':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = 'complex(0,1)*gVu33',
                 order = {'DMV':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '-(complex(0,1)*gVXc)/2.',
                 order = {'DMV':1})

GC_42 = Coupling(name = 'GC_42',
                 value = 'complex(0,1)*gVXd',
                 order = {'DMV':1})

GC_43 = Coupling(name = 'GC_43',
                 value = 'I1a33',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-I2a33',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = 'I3a33',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-I4a33',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-2*complex(0,1)*lam',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '-4*complex(0,1)*lam',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '-ee/(2.*sw)',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-((cw*ee*complex(0,1))/sw)',
                 order = {'QED':1})

GC_6 = Coupling(name = 'GC_6',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-ee**2/(2.*sw)',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '-(ee**2*complex(0,1))/(2.*sw)',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = 'ee**2/(2.*sw)',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(cw*ee)/(2.*sw) - (ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_7 = Coupling(name = 'GC_7',
                value = '-ee**2/(2.*cw)',
                order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                 order = {'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '-(ee**2*vev)/(2.*cw)',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '(ee**2*vev)/(2.*cw)',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-2*complex(0,1)*lam*vev',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-6*complex(0,1)*lam*vev',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-(ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-(ee**2*complex(0,1)*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '(ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '-(ee**2*vev)/(2.*sw)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(ee**2*vev)/(2.*sw)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-(ee**2*complex(0,1)*vev)/2. - (cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '-(yb/cmath.sqrt(2))',
                 order = {'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = 'ee**2/(2.*cw)',
                order = {'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = 'yb/cmath.sqrt(2)',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = 'yt/cmath.sqrt(2)',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '-ytau',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = 'ytau',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '-(ytau/cmath.sqrt(2))',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

                                                                                                                                                                                                                                                                                                                                                                                                                                                   couplings.pyo                                                                                       0000644 0276724 0002567 00000021170 13234357560 012127  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc        	   @   s6  d  d l  m Z m Z d  d l m Z m Z m Z m Z m Z m	 Z	 m
 Z
 m Z e d d d d d i d d	 6� Z e d d
 d d d i d d 6� Z e d d d d d i d d 6� Z e d d d d d i d d 6� Z e d d d d d i d d 6� Z e d d d d d i d d 6� Z e d d d d d i d d 6� Z e d d d d d i d d 6� Z e d d d d d i d d 6� Z e d d d d d i d d 6� Z e d d d d  d i d d 6� Z e d d! d d" d i d d	 6� Z e d d# d d$ d i d d 6� Z e d d% d d& d i d d 6� Z e d d' d d( d i d d 6� Z e d d) d d* d i d d 6� Z e d d+ d d, d i d d 6� Z e d d- d d. d i d d 6� Z e d d/ d d0 d i d d 6� Z e d d1 d d2 d i d d 6� Z e d d3 d d4 d i d d 6� Z  e d d5 d d6 d i d d 6� Z! e d d7 d d8 d i d d	 6� Z" e d d9 d d: d i d d 6� Z# e d d; d d< d i d d 6� Z$ e d d= d d> d i d d 6� Z% e d d? d d@ d i d d 6� Z& e d dA d dB d i d d 6� Z' e d dC d dD d i d d 6� Z( e d dE d dF d i d d 6� Z) e d dG d dH d i d d 6� Z* e d dI d dJ d i d d 6� Z+ e d dK d dL d i d d 6� Z, e d dM d dN d i d d	 6� Z- e d dO d dP d i d d 6� Z. e d dQ d dR d i d d 6� Z/ e d dS d dT d i d d 6� Z0 e d dU d dV d i d d	 6� Z1 e d dW d dX d i d d	 6� Z2 e d dY d dZ d i d d	 6� Z3 e d d[ d d\ d i d d	 6� Z4 e d d] d d^ d i d d	 6� Z5 e d d_ d d` d i d d	 6� Z6 e d da d db d i d d	 6� Z7 e d dc d dd d i d d	 6� Z8 e d de d df d i d d	 6� Z9 e d dg d dh d i d d	 6� Z: e d di d dj d i d d	 6� Z; e d dk d dl d i d d	 6� Z< e d dm d dn d i d d	 6� Z= e d do d dp d i d d	 6� Z> e d dq d dr d i d d	 6� Z? e d ds d dt d i d d	 6� Z@ e d du d dv d i d d	 6� ZA e d dw d dx d i d d	 6� ZB e d dy d dz d i d d	 6� ZC e d d{ d d| d i d d	 6� ZD e d d} d d~ d i d d	 6� ZE e d d d d� d i d d	 6� ZF e d d� d d� d i d d	 6� ZG e d d� d d� d i d d	 6� ZH e d d� d d� d i d d	 6� ZI e d d� d d� d i d d	 6� ZJ e d d� d d� d i d d	 6� ZK e d d� d d� d i d d	 6� ZL e d d� d d� d i d d	 6� ZM e d d� d d� d i d d	 6� ZN e d d� d d� d i d d	 6� ZO e d d� d d� d i d d	 6� ZP e d d� d d� d i d d	 6� ZQ e d d� d d� d i d d	 6� ZR e d d� d d� d i d d	 6� ZS e d d� d d� d i d d	 6� ZT e d d� d d� d i d d	 6� ZU e d d� d d� d i d d	 6� ZV e d d� d d� d i d d	 6� ZW e d d� d d� d i d d	 6� ZX e d d� d d� d i d d	 6� ZY e d d� d d� d i d d	 6� ZZ e d d� d d� d i d d	 6� Z[ e d d� d d� d i d d	 6� Z\ e d d� d d� d i d d	 6� Z] e d d� d d� d i d d	 6� Z^ e d d� d d� d i d d	 6� Z_ e d d� d d� d i d d	 6� Z` e d d� d d� d i d d	 6� Za e d d� d d� d i d d	 6� Zb e d d� d d� d i d d	 6� Zc e d d� d d� d i d d	 6� Zd e d d� d d� d i d d	 6� Ze e d d� d d� d i d d	 6� Zf e d d� d d� d i d d	 6� Zg e d d� d d� d i d d	 6� Zh e d d� d d� d i d d	 6� Zi e d d� d d� d i d d	 6� Zj e d d� d d� d i d d	 6� Zk e d d� d d� d i d d	 6� Zl d� S(�   i����(   t   all_couplingst   Coupling(   t   complexconjugatet   ret   imt   csct   sect   acsct   asect   cott   namet   GC_1t   values   -(ee*complex(0,1))/3.t   orderi   t   QEDt   GC_10s   -Gt   QCDt   GC_11s   complex(0,1)*Gt   GC_12t   Gt   GC_13s   -(complex(0,1)*G**2)i   t   GC_14s   complex(0,1)*G**2t   GC_15s   complex(0,1)*gAd11t   DMVt   GC_16s   complex(0,1)*gAd22t   GC_17s   complex(0,1)*gAd31t   GC_18s   complex(0,1)*gAd33t   GC_19s   complex(0,1)*gAl11t   GC_2s   (2*ee*complex(0,1))/3.t   GC_20s   complex(0,1)*gAl22t   GC_21s   complex(0,1)*gAl33t   GC_22s   complex(0,1)*gAu11t   GC_23s   complex(0,1)*gAu22t   GC_24s   complex(0,1)*gAu31t   GC_25s   complex(0,1)*gAu33t   GC_26s   complex(0,1)*gAXdt   GC_27s   complex(0,1)*gnu11t   GC_28s   complex(0,1)*gnu22t   GC_29s   complex(0,1)*gnu33t   GC_3s   -(ee*complex(0,1))t   GC_30s   complex(0,1)*gVd11t   GC_31s   complex(0,1)*gVd22t   GC_32s   complex(0,1)*gVd31t   GC_33s   complex(0,1)*gVd33t   GC_34s   complex(0,1)*gVl11t   GC_35s   complex(0,1)*gVl22t   GC_36s   complex(0,1)*gVl33t   GC_37s   complex(0,1)*gVu11t   GC_38s   complex(0,1)*gVu22t   GC_39s   complex(0,1)*gVu31t   GC_4s   ee*complex(0,1)t   GC_40s   complex(0,1)*gVu33t   GC_41s   -(complex(0,1)*gVXc)/2.t   GC_42s   complex(0,1)*gVXdt   GC_43t   I1a33t   GC_44s   -I2a33t   GC_45t   I3a33t   GC_46s   -I4a33t   GC_47s   -2*complex(0,1)*lamt   GC_48s   -4*complex(0,1)*lamt   GC_49s   -6*complex(0,1)*lamt   GC_5s   ee**2*complex(0,1)t   GC_50s   (ee**2*complex(0,1))/(2.*sw**2)t   GC_51s   -((ee**2*complex(0,1))/sw**2)t   GC_52s    (cw**2*ee**2*complex(0,1))/sw**2t   GC_53s   -ee/(2.*sw)t   GC_54s   -(ee*complex(0,1))/(2.*sw)t   GC_55s   (ee*complex(0,1))/(2.*sw)t   GC_56s$   (ee*complex(0,1))/(sw*cmath.sqrt(2))t   GC_57s   -(cw*ee*complex(0,1))/(2.*sw)t   GC_58s   (cw*ee*complex(0,1))/(2.*sw)t   GC_59s   -((cw*ee*complex(0,1))/sw)t   GC_6s   2*ee**2*complex(0,1)t   GC_60s   (cw*ee*complex(0,1))/swt   GC_61s   -ee**2/(2.*sw)t   GC_62s   -(ee**2*complex(0,1))/(2.*sw)t   GC_63s   ee**2/(2.*sw)t   GC_64s   (-2*cw*ee**2*complex(0,1))/swt   GC_65s   -(ee*complex(0,1)*sw)/(6.*cw)t   GC_66s   (ee*complex(0,1)*sw)/(2.*cw)t   GC_67s"   -(cw*ee)/(2.*sw) - (ee*sw)/(2.*cw)t   GC_68s<   -(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)t   GC_69s;   (cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)t   GC_7s   -ee**2/(2.*cw)t   GC_70s7   (cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cwt   GC_71se   -(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)t   GC_72sb   ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)t   GC_73s   -(ee**2*vev)/(2.*cw)t   GC_74s   (ee**2*vev)/(2.*cw)t   GC_75s   -2*complex(0,1)*lam*vevt   GC_76s   -6*complex(0,1)*lam*vevt   GC_77s   -(ee**2*vev)/(4.*sw**2)t   GC_78s$   -(ee**2*complex(0,1)*vev)/(4.*sw**2)t   GC_79s#   (ee**2*complex(0,1)*vev)/(2.*sw**2)t   GC_8s   (ee**2*complex(0,1))/(2.*cw)t   GC_80s   (ee**2*vev)/(4.*sw**2)t   GC_81s   -(ee**2*vev)/(2.*sw)t   GC_82s   (ee**2*vev)/(2.*sw)t   GC_83s0   -(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)t   GC_84s/   (ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)t   GC_85s0   -(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)t   GC_86s/   (ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)t   GC_87st   -(ee**2*complex(0,1)*vev)/2. - (cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)t   GC_88sn   ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)t   GC_89s   -(yb/cmath.sqrt(2))t   GC_9s   ee**2/(2.*cw)t   GC_90s"   -((complex(0,1)*yb)/cmath.sqrt(2))t   GC_91s   yb/cmath.sqrt(2)t   GC_92s"   -((complex(0,1)*yt)/cmath.sqrt(2))t   GC_93s   yt/cmath.sqrt(2)t   GC_94s   -ytaut   GC_95t   ytaut   GC_96s   -(ytau/cmath.sqrt(2))t   GC_97s$   -((complex(0,1)*ytau)/cmath.sqrt(2))N(m   t   object_libraryR    R   t   function_libraryR   R   R   R   R   R   R   R	   R   R   R   R   R   R   R   R   R   R   R   R   R   R   R   R    R!   R"   R#   R$   R%   R&   R'   R(   R)   R*   R+   R,   R-   R.   R/   R0   R1   R2   R3   R4   R5   R6   R8   R9   R;   R<   R=   R>   R?   R@   RA   RB   RC   RD   RE   RF   RG   RH   RI   RJ   RK   RL   RM   RN   RO   RP   RQ   RR   RS   RT   RU   RV   RW   RX   RY   RZ   R[   R\   R]   R^   R_   R`   Ra   Rb   Rc   Rd   Re   Rf   Rg   Rh   Ri   Rj   Rk   Rl   Rm   Rn   Ro   Rp   Rq   Rs   Rt   (    (    (    sI   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/couplings.pyt   <module>   sH  :                                                                                                                                                                                                                                                                                                                                                                                                        CT_couplings.py                                                                                     0000644 0276724 0002567 00000135632 13234357560 012347  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     # This file was automatically created by FeynRules 2.4.46
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Thu 27 Oct 2016 23:02:25


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



R2GC_100_1 = Coupling(name = 'R2GC_100_1',
                      value = '(complex(0,1)*G**2*gAu22)/(6.*cmath.pi**2)',
                      order = {'DMV':1,'QCD':2})

R2GC_101_2 = Coupling(name = 'R2GC_101_2',
                      value = '-(complex(0,1)*G**2*gVu22)/(6.*cmath.pi**2)',
                      order = {'DMV':1,'QCD':2})

R2GC_102_3 = Coupling(name = 'R2GC_102_3',
                      value = '-(cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw)',
                      order = {'QCD':2,'QED':1})

R2GC_103_4 = Coupling(name = 'R2GC_103_4',
                      value = '(ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)',
                      order = {'QCD':2,'QED':1})

R2GC_104_5 = Coupling(name = 'R2GC_104_5',
                      value = '(complex(0,1)*G**2)/(12.*cmath.pi**2)',
                      order = {'QCD':2})

R2GC_105_6 = Coupling(name = 'R2GC_105_6',
                      value = '(complex(0,1)*G**2*gAd11)/(6.*cmath.pi**2)',
                      order = {'DMV':1,'QCD':2})

R2GC_106_7 = Coupling(name = 'R2GC_106_7',
                      value = '-(complex(0,1)*G**2*gVd11)/(6.*cmath.pi**2)',
                      order = {'DMV':1,'QCD':2})

R2GC_107_8 = Coupling(name = 'R2GC_107_8',
                      value = '(cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw)',
                      order = {'QCD':2,'QED':1})

R2GC_110_9 = Coupling(name = 'R2GC_110_9',
                      value = '(complex(0,1)*G**2*gAd22)/(6.*cmath.pi**2)',
                      order = {'DMV':1,'QCD':2})

R2GC_111_10 = Coupling(name = 'R2GC_111_10',
                       value = '-(complex(0,1)*G**2*gVd22)/(6.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2})

R2GC_115_11 = Coupling(name = 'R2GC_115_11',
                       value = '(complex(0,1)*G**2*gAu11)/(6.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2})

R2GC_116_12 = Coupling(name = 'R2GC_116_12',
                       value = '-(complex(0,1)*G**2*gVu11)/(6.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2})

R2GC_119_13 = Coupling(name = 'R2GC_119_13',
                       value = '-(complex(0,1)*G**2*MB**2)/(8.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_119_14 = Coupling(name = 'R2GC_119_14',
                       value = '-(complex(0,1)*G**2*MT**2)/(8.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_120_15 = Coupling(name = 'R2GC_120_15',
                       value = '-(complex(0,1)*G**2*MB*yb)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_120_16 = Coupling(name = 'R2GC_120_16',
                       value = '-(complex(0,1)*G**2*MT*yt)/(8.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_121_17 = Coupling(name = 'R2GC_121_17',
                       value = '-(complex(0,1)*G**2*yb**2)/(16.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_121_18 = Coupling(name = 'R2GC_121_18',
                       value = '-(complex(0,1)*G**2*yt**2)/(16.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_122_19 = Coupling(name = 'R2GC_122_19',
                       value = '(complex(0,1)*G**2)/(48.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_123_20 = Coupling(name = 'R2GC_123_20',
                       value = '(ee**2*complex(0,1)*G**2)/(216.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_123_21 = Coupling(name = 'R2GC_123_21',
                       value = '(ee**2*complex(0,1)*G**2)/(54.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_124_22 = Coupling(name = 'R2GC_124_22',
                       value = '-(ee*complex(0,1)*G**3)/(144.*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_124_23 = Coupling(name = 'R2GC_124_23',
                       value = '(ee*complex(0,1)*G**3)/(72.*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_125_24 = Coupling(name = 'R2GC_125_24',
                       value = '-(G**2*gAd33)/(12.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2})

R2GC_125_25 = Coupling(name = 'R2GC_125_25',
                       value = '-(G**2*gAu22)/(12.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2})

R2GC_125_26 = Coupling(name = 'R2GC_125_26',
                       value = '-(G**2*gAd11)/(12.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2})

R2GC_125_27 = Coupling(name = 'R2GC_125_27',
                       value = '-(G**2*gAd22)/(12.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2})

R2GC_125_28 = Coupling(name = 'R2GC_125_28',
                       value = '-(G**2*gAu33)/(12.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2})

R2GC_125_29 = Coupling(name = 'R2GC_125_29',
                       value = '-(G**2*gAu11)/(12.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2})

R2GC_126_30 = Coupling(name = 'R2GC_126_30',
                       value = '-(complex(0,1)*G**3*gAd33)/(16.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':3})

R2GC_126_31 = Coupling(name = 'R2GC_126_31',
                       value = '-(complex(0,1)*G**3*gAu22)/(16.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':3})

R2GC_126_32 = Coupling(name = 'R2GC_126_32',
                       value = '-(complex(0,1)*G**3*gAd11)/(16.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':3})

R2GC_126_33 = Coupling(name = 'R2GC_126_33',
                       value = '-(complex(0,1)*G**3*gAd22)/(16.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':3})

R2GC_126_34 = Coupling(name = 'R2GC_126_34',
                       value = '-(complex(0,1)*G**3*gAu33)/(16.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':3})

R2GC_126_35 = Coupling(name = 'R2GC_126_35',
                       value = '-(complex(0,1)*G**3*gAu11)/(16.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':3})

R2GC_127_36 = Coupling(name = 'R2GC_127_36',
                       value = '-(ee*complex(0,1)*G**2*gVd33)/(72.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2,'QED':1})

R2GC_127_37 = Coupling(name = 'R2GC_127_37',
                       value = '(ee*complex(0,1)*G**2*gVu22)/(36.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2,'QED':1})

R2GC_127_38 = Coupling(name = 'R2GC_127_38',
                       value = '-(ee*complex(0,1)*G**2*gVd11)/(72.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2,'QED':1})

R2GC_127_39 = Coupling(name = 'R2GC_127_39',
                       value = '-(ee*complex(0,1)*G**2*gVd22)/(72.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2,'QED':1})

R2GC_127_40 = Coupling(name = 'R2GC_127_40',
                       value = '(ee*complex(0,1)*G**2*gVu33)/(36.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2,'QED':1})

R2GC_127_41 = Coupling(name = 'R2GC_127_41',
                       value = '(ee*complex(0,1)*G**2*gVu11)/(36.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2,'QED':1})

R2GC_128_42 = Coupling(name = 'R2GC_128_42',
                       value = '(complex(0,1)*G**3*gVd33)/(48.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':3})

R2GC_128_43 = Coupling(name = 'R2GC_128_43',
                       value = '(complex(0,1)*G**3*gVu22)/(48.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':3})

R2GC_128_44 = Coupling(name = 'R2GC_128_44',
                       value = '(complex(0,1)*G**3*gVd11)/(48.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':3})

R2GC_128_45 = Coupling(name = 'R2GC_128_45',
                       value = '(complex(0,1)*G**3*gVd22)/(48.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':3})

R2GC_128_46 = Coupling(name = 'R2GC_128_46',
                       value = '(complex(0,1)*G**3*gVu33)/(48.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':3})

R2GC_128_47 = Coupling(name = 'R2GC_128_47',
                       value = '(complex(0,1)*G**3*gVu11)/(48.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':3})

R2GC_129_48 = Coupling(name = 'R2GC_129_48',
                       value = '-(cw*ee*G**2)/(48.*cmath.pi**2*sw) - (ee*G**2*sw)/(48.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_129_49 = Coupling(name = 'R2GC_129_49',
                       value = '(cw*ee*G**2)/(48.*cmath.pi**2*sw) + (ee*G**2*sw)/(48.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_130_50 = Coupling(name = 'R2GC_130_50',
                       value = '(cw*ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2*sw) - (ee**2*complex(0,1)*G**2*sw)/(864.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_130_51 = Coupling(name = 'R2GC_130_51',
                       value = '(cw*ee**2*complex(0,1)*G**2)/(144.*cmath.pi**2*sw) - (5*ee**2*complex(0,1)*G**2*sw)/(432.*cw*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_131_52 = Coupling(name = 'R2GC_131_52',
                       value = '-(cw*ee*complex(0,1)*G**3)/(192.*cmath.pi**2*sw) + (ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_131_53 = Coupling(name = 'R2GC_131_53',
                       value = '(cw*ee*complex(0,1)*G**3)/(192.*cmath.pi**2*sw) - (5*ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_132_54 = Coupling(name = 'R2GC_132_54',
                       value = '(3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) + (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_132_55 = Coupling(name = 'R2GC_132_55',
                       value = '(-3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) - (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)',
                       order = {'QCD':3,'QED':1})

R2GC_133_56 = Coupling(name = 'R2GC_133_56',
                       value = '(cw*ee*complex(0,1)*G**2*gAd33)/(96.*cmath.pi**2*sw) - (cw*ee*complex(0,1)*G**2*gVd33)/(96.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*gAd33*sw)/(96.*cw*cmath.pi**2) + (ee*complex(0,1)*G**2*gVd33*sw)/(288.*cw*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2,'QED':1})

R2GC_133_57 = Coupling(name = 'R2GC_133_57',
                       value = '-(cw*ee*complex(0,1)*G**2*gAu22)/(96.*cmath.pi**2*sw) + (cw*ee*complex(0,1)*G**2*gVu22)/(96.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*gAu22*sw)/(96.*cw*cmath.pi**2) - (5*ee*complex(0,1)*G**2*gVu22*sw)/(288.*cw*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2,'QED':1})

R2GC_133_58 = Coupling(name = 'R2GC_133_58',
                       value = '(cw*ee*complex(0,1)*G**2*gAd11)/(96.*cmath.pi**2*sw) - (cw*ee*complex(0,1)*G**2*gVd11)/(96.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*gAd11*sw)/(96.*cw*cmath.pi**2) + (ee*complex(0,1)*G**2*gVd11*sw)/(288.*cw*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2,'QED':1})

R2GC_133_59 = Coupling(name = 'R2GC_133_59',
                       value = '(cw*ee*complex(0,1)*G**2*gAd22)/(96.*cmath.pi**2*sw) - (cw*ee*complex(0,1)*G**2*gVd22)/(96.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*gAd22*sw)/(96.*cw*cmath.pi**2) + (ee*complex(0,1)*G**2*gVd22*sw)/(288.*cw*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2,'QED':1})

R2GC_133_60 = Coupling(name = 'R2GC_133_60',
                       value = '-(cw*ee*complex(0,1)*G**2*gAu33)/(96.*cmath.pi**2*sw) + (cw*ee*complex(0,1)*G**2*gVu33)/(96.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*gAu33*sw)/(96.*cw*cmath.pi**2) - (5*ee*complex(0,1)*G**2*gVu33*sw)/(288.*cw*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2,'QED':1})

R2GC_133_61 = Coupling(name = 'R2GC_133_61',
                       value = '-(cw*ee*complex(0,1)*G**2*gAu11)/(96.*cmath.pi**2*sw) + (cw*ee*complex(0,1)*G**2*gVu11)/(96.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*gAu11*sw)/(96.*cw*cmath.pi**2) - (5*ee*complex(0,1)*G**2*gVu11*sw)/(288.*cw*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2,'QED':1})

R2GC_134_62 = Coupling(name = 'R2GC_134_62',
                       value = '(ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2) + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (5*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_134_63 = Coupling(name = 'R2GC_134_63',
                       value = '-(ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2) + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (17*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_135_64 = Coupling(name = 'R2GC_135_64',
                       value = '-(complex(0,1)*G**2*yb**2)/(16.*cmath.pi**2) - (complex(0,1)*G**2*yt**2)/(16.*cmath.pi**2)',
                       order = {'QCD':2,'QED':2})

R2GC_136_65 = Coupling(name = 'R2GC_136_65',
                       value = '(ee**2*complex(0,1)*G**2)/(96.*cmath.pi**2*sw**2)',
                       order = {'QCD':2,'QED':2})

R2GC_137_66 = Coupling(name = 'R2GC_137_66',
                       value = '(complex(0,1)*G**2*gAd33**2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVd33**2)/(24.*cmath.pi**2)',
                       order = {'DMV':2,'QCD':2})

R2GC_137_67 = Coupling(name = 'R2GC_137_67',
                       value = '(complex(0,1)*G**2*gAu22**2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVu22**2)/(24.*cmath.pi**2)',
                       order = {'DMV':2,'QCD':2})

R2GC_137_68 = Coupling(name = 'R2GC_137_68',
                       value = '(complex(0,1)*G**2*gAd11**2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVd11**2)/(24.*cmath.pi**2)',
                       order = {'DMV':2,'QCD':2})

R2GC_137_69 = Coupling(name = 'R2GC_137_69',
                       value = '(complex(0,1)*G**2*gAd22**2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVd22**2)/(24.*cmath.pi**2)',
                       order = {'DMV':2,'QCD':2})

R2GC_137_70 = Coupling(name = 'R2GC_137_70',
                       value = '(complex(0,1)*G**2*gAu33**2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVu33**2)/(24.*cmath.pi**2)',
                       order = {'DMV':2,'QCD':2})

R2GC_137_71 = Coupling(name = 'R2GC_137_71',
                       value = '(complex(0,1)*G**2*gAu11**2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVu11**2)/(24.*cmath.pi**2)',
                       order = {'DMV':2,'QCD':2})

R2GC_137_72 = Coupling(name = 'R2GC_137_72',
                       value = '(complex(0,1)*G**2*gAd31**2)/(12.*cmath.pi**2) + (complex(0,1)*G**2*gVd31**2)/(12.*cmath.pi**2)',
                       order = {'DMV':2,'QCD':2})

R2GC_137_73 = Coupling(name = 'R2GC_137_73',
                       value = '(complex(0,1)*G**2*gAu31**2)/(12.*cmath.pi**2) + (complex(0,1)*G**2*gVu31**2)/(12.*cmath.pi**2)',
                       order = {'DMV':2,'QCD':2})

R2GC_147_74 = Coupling(name = 'R2GC_147_74',
                       value = '-G**4/(192.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_147_75 = Coupling(name = 'R2GC_147_75',
                       value = 'G**4/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_148_76 = Coupling(name = 'R2GC_148_76',
                       value = '-(complex(0,1)*G**4)/(192.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_148_77 = Coupling(name = 'R2GC_148_77',
                       value = '(complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_149_78 = Coupling(name = 'R2GC_149_78',
                       value = '(complex(0,1)*G**4)/(192.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_149_79 = Coupling(name = 'R2GC_149_79',
                       value = '-(complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_150_80 = Coupling(name = 'R2GC_150_80',
                       value = '-(complex(0,1)*G**4)/(48.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_151_81 = Coupling(name = 'R2GC_151_81',
                       value = '(complex(0,1)*G**4)/(288.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_151_82 = Coupling(name = 'R2GC_151_82',
                       value = '-(complex(0,1)*G**4)/(32.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_152_83 = Coupling(name = 'R2GC_152_83',
                       value = '-(complex(0,1)*G**4)/(16.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_153_84 = Coupling(name = 'R2GC_153_84',
                       value = '(-3*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                       order = {'QCD':4})

R2GC_154_85 = Coupling(name = 'R2GC_154_85',
                       value = '(ee*complex(0,1)*G**2)/(18.*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_155_86 = Coupling(name = 'R2GC_155_86',
                       value = '-(complex(0,1)*G**3)/(6.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_156_87 = Coupling(name = 'R2GC_156_87',
                       value = '-(ee*complex(0,1)*G**2)/(9.*cmath.pi**2)',
                       order = {'QCD':2,'QED':1})

R2GC_170_88 = Coupling(name = 'R2GC_170_88',
                       value = '-(ee*complex(0,1)*G**2)/(6.*cmath.pi**2*sw*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_175_89 = Coupling(name = 'R2GC_175_89',
                       value = '(complex(0,1)*G**2*gAd31)/(6.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2})

R2GC_176_90 = Coupling(name = 'R2GC_176_90',
                       value = '(complex(0,1)*G**2*gAd33)/(6.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2})

R2GC_177_91 = Coupling(name = 'R2GC_177_91',
                       value = '-(complex(0,1)*G**2*gVd31)/(6.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2})

R2GC_178_92 = Coupling(name = 'R2GC_178_92',
                       value = '-(complex(0,1)*G**2*gVd33)/(6.*cmath.pi**2)',
                       order = {'DMV':1,'QCD':2})

R2GC_179_93 = Coupling(name = 'R2GC_179_93',
                       value = '(complex(0,1)*G**2*MB)/(6.*cmath.pi**2)',
                       order = {'QCD':2})

R2GC_182_94 = Coupling(name = 'R2GC_182_94',
                       value = '(complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_183_95 = Coupling(name = 'R2GC_183_95',
                       value = '-(G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',
                       order = {'QCD':2,'QED':1})

R2GC_185_96 = Coupling(name = 'R2GC_185_96',
                       value = 'G**3/(24.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_185_97 = Coupling(name = 'R2GC_185_97',
                       value = '(11*G**3)/(64.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_186_98 = Coupling(name = 'R2GC_186_98',
                       value = '-G**3/(24.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_186_99 = Coupling(name = 'R2GC_186_99',
                       value = '(-11*G**3)/(64.*cmath.pi**2)',
                       order = {'QCD':3})

R2GC_187_100 = Coupling(name = 'R2GC_187_100',
                        value = '(5*complex(0,1)*G**4)/(48.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_187_101 = Coupling(name = 'R2GC_187_101',
                        value = '(7*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_188_102 = Coupling(name = 'R2GC_188_102',
                        value = '(23*complex(0,1)*G**4)/(192.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_188_103 = Coupling(name = 'R2GC_188_103',
                        value = '(15*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_190_104 = Coupling(name = 'R2GC_190_104',
                        value = '(-17*complex(0,1)*G**4)/(64.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_191_105 = Coupling(name = 'R2GC_191_105',
                        value = '(-7*complex(0,1)*G**4)/(32.*cmath.pi**2)',
                        order = {'QCD':4})

R2GC_196_106 = Coupling(name = 'R2GC_196_106',
                        value = '(complex(0,1)*G**2*gAu31)/(6.*cmath.pi**2)',
                        order = {'DMV':1,'QCD':2})

R2GC_197_107 = Coupling(name = 'R2GC_197_107',
                        value = '(complex(0,1)*G**2*gAu33)/(6.*cmath.pi**2)',
                        order = {'DMV':1,'QCD':2})

R2GC_198_108 = Coupling(name = 'R2GC_198_108',
                        value = '-(complex(0,1)*G**2*gVu31)/(6.*cmath.pi**2)',
                        order = {'DMV':1,'QCD':2})

R2GC_199_109 = Coupling(name = 'R2GC_199_109',
                        value = '-(complex(0,1)*G**2*gVu33)/(6.*cmath.pi**2)',
                        order = {'DMV':1,'QCD':2})

R2GC_200_110 = Coupling(name = 'R2GC_200_110',
                        value = '(complex(0,1)*G**2*MT)/(6.*cmath.pi**2)',
                        order = {'QCD':2})

R2GC_204_111 = Coupling(name = 'R2GC_204_111',
                        value = '(G**2*yb)/(3.*cmath.pi**2)',
                        order = {'QCD':2,'QED':1})

R2GC_205_112 = Coupling(name = 'R2GC_205_112',
                        value = '-(G**2*yb)/(3.*cmath.pi**2)',
                        order = {'QCD':2,'QED':1})

R2GC_206_113 = Coupling(name = 'R2GC_206_113',
                        value = '(G**2*yt)/(3.*cmath.pi**2)',
                        order = {'QCD':2,'QED':1})

R2GC_207_114 = Coupling(name = 'R2GC_207_114',
                        value = '-(G**2*yt)/(3.*cmath.pi**2)',
                        order = {'QCD':2,'QED':1})

R2GC_208_115 = Coupling(name = 'R2GC_208_115',
                        value = '(G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                        order = {'QCD':2,'QED':1})

R2GC_209_116 = Coupling(name = 'R2GC_209_116',
                        value = '(complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))',
                        order = {'QCD':2,'QED':1})

R2GC_98_117 = Coupling(name = 'R2GC_98_117',
                       value = '-(complex(0,1)*G**2)/(16.*cmath.pi**2)',
                       order = {'QCD':2})

UVGC_138_1 = Coupling(name = 'UVGC_138_1',
                      value = {-1:'-(complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                      order = {'QCD':2})

UVGC_139_2 = Coupling(name = 'UVGC_139_2',
                      value = {-1:'(ee*complex(0,1)*G**2)/(18.*cmath.pi**2)'},
                      order = {'QCD':2,'QED':1})

UVGC_141_3 = Coupling(name = 'UVGC_141_3',
                      value = {-1:'-(ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                      order = {'QCD':2,'QED':1})

UVGC_146_4 = Coupling(name = 'UVGC_146_4',
                      value = {-1:'(3*complex(0,1)*G**2)/(64.*cmath.pi**2)'},
                      order = {'QCD':2})

UVGC_146_5 = Coupling(name = 'UVGC_146_5',
                      value = {-1:'(-3*complex(0,1)*G**2)/(64.*cmath.pi**2)'},
                      order = {'QCD':2})

UVGC_147_6 = Coupling(name = 'UVGC_147_6',
                      value = {-1:'(3*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_147_7 = Coupling(name = 'UVGC_147_7',
                      value = {-1:'(-3*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_148_8 = Coupling(name = 'UVGC_148_8',
                      value = {-1:'(3*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_148_9 = Coupling(name = 'UVGC_148_9',
                      value = {-1:'(-3*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                      order = {'QCD':4})

UVGC_150_10 = Coupling(name = 'UVGC_150_10',
                       value = {-1:'-(complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_150_11 = Coupling(name = 'UVGC_150_11',
                       value = {-1:'(complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_151_12 = Coupling(name = 'UVGC_151_12',
                       value = {-1:'(-3*complex(0,1)*G**4)/(256.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_151_13 = Coupling(name = 'UVGC_151_13',
                       value = {-1:'(3*complex(0,1)*G**4)/(256.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_152_14 = Coupling(name = 'UVGC_152_14',
                       value = {-1:'-(complex(0,1)*G**4)/(24.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_153_15 = Coupling(name = 'UVGC_153_15',
                       value = {-1:'(5*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_154_16 = Coupling(name = 'UVGC_154_16',
                       value = {-1:'(ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_155_17 = Coupling(name = 'UVGC_155_17',
                       value = {-1:'(-13*complex(0,1)*G**3)/(48.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_156_18 = Coupling(name = 'UVGC_156_18',
                       value = {-1:'-(ee*complex(0,1)*G**2)/(18.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_157_19 = Coupling(name = 'UVGC_157_19',
                       value = {-1:'( 0 if MB else (complex(0,1)*G**3)/(48.*cmath.pi**2) )'},
                       order = {'QCD':3})

UVGC_157_20 = Coupling(name = 'UVGC_157_20',
                       value = {-1:'(complex(0,1)*G**3)/(48.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_157_21 = Coupling(name = 'UVGC_157_21',
                       value = {-1:'(-19*complex(0,1)*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_157_22 = Coupling(name = 'UVGC_157_22',
                       value = {-1:'-(complex(0,1)*G**3)/(128.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_157_23 = Coupling(name = 'UVGC_157_23',
                       value = {-1:'(complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_170_24 = Coupling(name = 'UVGC_170_24',
                       value = {-1:'(ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_170_25 = Coupling(name = 'UVGC_170_25',
                       value = {-1:'-(ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_172_26 = Coupling(name = 'UVGC_172_26',
                       value = {-1:'( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MB else -(complex(0,1)*G**2)/(12.*cmath.pi**2) ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MB**2/MU_R**2))/(4.*cmath.pi**2) if MB else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_173_27 = Coupling(name = 'UVGC_173_27',
                       value = {-1:'( (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) if MB else -(ee*complex(0,1)*G**2)/(36.*cmath.pi**2) )',0:'( (5*ee*complex(0,1)*G**2)/(36.*cmath.pi**2) - (ee*complex(0,1)*G**2*reglog(MB**2/MU_R**2))/(12.*cmath.pi**2) if MB else (ee*complex(0,1)*G**2)/(36.*cmath.pi**2) ) - (ee*complex(0,1)*G**2)/(36.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_174_28 = Coupling(name = 'UVGC_174_28',
                       value = {-1:'( -(complex(0,1)*G**3)/(6.*cmath.pi**2) if MB else (complex(0,1)*G**3)/(12.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MB**2/MU_R**2))/(4.*cmath.pi**2) if MB else -(complex(0,1)*G**3)/(12.*cmath.pi**2) ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_175_29 = Coupling(name = 'UVGC_175_29',
                       value = {-1:'( (complex(0,1)*G**2*gAd31)/(12.*cmath.pi**2) if MB else -(complex(0,1)*G**2*gAd31)/(24.*cmath.pi**2) )',0:'( (5*complex(0,1)*G**2*gAd31)/(24.*cmath.pi**2) - (complex(0,1)*G**2*gAd31*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2) if MB else (complex(0,1)*G**2*gAd31)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2*gAd31)/(24.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_175_30 = Coupling(name = 'UVGC_175_30',
                       value = {-1:'-(complex(0,1)*G**2*gAd31)/(24.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_175_31 = Coupling(name = 'UVGC_175_31',
                       value = {-1:'(complex(0,1)*G**2*gAd31)/(12.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_176_32 = Coupling(name = 'UVGC_176_32',
                       value = {-1:'( (complex(0,1)*G**2*gAd33)/(6.*cmath.pi**2) if MB else -(complex(0,1)*G**2*gAd33)/(12.*cmath.pi**2) ) + (complex(0,1)*G**2*gAd33)/(12.*cmath.pi**2)',0:'( (5*complex(0,1)*G**2*gAd33)/(12.*cmath.pi**2) - (complex(0,1)*G**2*gAd33*reglog(MB**2/MU_R**2))/(4.*cmath.pi**2) if MB else (complex(0,1)*G**2*gAd33)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*gAd33)/(12.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_177_33 = Coupling(name = 'UVGC_177_33',
                       value = {-1:'( -(complex(0,1)*G**2*gVd31)/(12.*cmath.pi**2) if MB else (complex(0,1)*G**2*gVd31)/(24.*cmath.pi**2) )',0:'( (-5*complex(0,1)*G**2*gVd31)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVd31*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2) if MB else -(complex(0,1)*G**2*gVd31)/(24.*cmath.pi**2) ) + (complex(0,1)*G**2*gVd31)/(24.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_177_34 = Coupling(name = 'UVGC_177_34',
                       value = {-1:'(complex(0,1)*G**2*gVd31)/(24.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_177_35 = Coupling(name = 'UVGC_177_35',
                       value = {-1:'-(complex(0,1)*G**2*gVd31)/(12.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_178_36 = Coupling(name = 'UVGC_178_36',
                       value = {-1:'( -(complex(0,1)*G**2*gVd33)/(6.*cmath.pi**2) if MB else (complex(0,1)*G**2*gVd33)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*gVd33)/(12.*cmath.pi**2)',0:'( (-5*complex(0,1)*G**2*gVd33)/(12.*cmath.pi**2) + (complex(0,1)*G**2*gVd33*reglog(MB**2/MU_R**2))/(4.*cmath.pi**2) if MB else -(complex(0,1)*G**2*gVd33)/(12.*cmath.pi**2) ) + (complex(0,1)*G**2*gVd33)/(12.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_179_37 = Coupling(name = 'UVGC_179_37',
                       value = {-1:'( (complex(0,1)*G**2*MB)/(6.*cmath.pi**2) if MB else -(complex(0,1)*G**2*MB)/(12.*cmath.pi**2) ) + (complex(0,1)*G**2*MB)/(3.*cmath.pi**2)',0:'( (3*complex(0,1)*G**2*MB)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MB*reglog(MB**2/MU_R**2))/(2.*cmath.pi**2) if MB else (complex(0,1)*G**2*MB)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MB)/(12.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_180_38 = Coupling(name = 'UVGC_180_38',
                       value = {-1:'( (cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw) if MB else -(cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) ) + (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw)',0:'( (5*cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) - (cw*ee*complex(0,1)*G**2*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2*sw) if MB else (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) ) - (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw)'},
                       order = {'QCD':2,'QED':1})

UVGC_181_39 = Coupling(name = 'UVGC_181_39',
                       value = {-1:'( (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) if MB else -(ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)',0:'( (5*ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) - (ee*complex(0,1)*G**2*sw*reglog(MB**2/MU_R**2))/(24.*cw*cmath.pi**2) if MB else (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_182_40 = Coupling(name = 'UVGC_182_40',
                       value = {-1:'( (complex(0,1)*G**2*yb)/(6.*cmath.pi**2*cmath.sqrt(2)) if MB else -(complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (3*complex(0,1)*G**2*yb)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yb*reglog(MB**2/MU_R**2))/(2.*cmath.pi**2*cmath.sqrt(2)) if MB else (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_183_41 = Coupling(name = 'UVGC_183_41',
                       value = {-1:'( -(G**2*yb)/(6.*cmath.pi**2*cmath.sqrt(2)) if MB else (G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))',0:'( (-3*G**2*yb)/(4.*cmath.pi**2*cmath.sqrt(2)) + (G**2*yb*reglog(MB**2/MU_R**2))/(2.*cmath.pi**2*cmath.sqrt(2)) if MB else -(G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_184_42 = Coupling(name = 'UVGC_184_42',
                       value = {-1:'( 0 if MB else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**2*reglog(MB**2/MU_R**2))/(24.*cmath.pi**2) if MB else 0 )'},
                       order = {'QCD':2})

UVGC_184_43 = Coupling(name = 'UVGC_184_43',
                       value = {-1:'-(complex(0,1)*G**2)/(24.*cmath.pi**2)',0:'(complex(0,1)*G**2*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_185_44 = Coupling(name = 'UVGC_185_44',
                       value = {-1:'( 0 if MB else -G**3/(16.*cmath.pi**2) ) + G**3/(24.*cmath.pi**2)',0:'( -(G**3*reglog(MB**2/MU_R**2))/(24.*cmath.pi**2) if MB else 0 )'},
                       order = {'QCD':3})

UVGC_185_45 = Coupling(name = 'UVGC_185_45',
                       value = {-1:'-G**3/(48.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_185_46 = Coupling(name = 'UVGC_185_46',
                       value = {-1:'(21*G**3)/(64.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_185_47 = Coupling(name = 'UVGC_185_47',
                       value = {-1:'G**3/(64.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_185_48 = Coupling(name = 'UVGC_185_48',
                       value = {-1:'G**3/(24.*cmath.pi**2)',0:'-(G**3*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_186_49 = Coupling(name = 'UVGC_186_49',
                       value = {-1:'( 0 if MB else G**3/(16.*cmath.pi**2) ) - G**3/(24.*cmath.pi**2)',0:'( (G**3*reglog(MB**2/MU_R**2))/(24.*cmath.pi**2) if MB else 0 )'},
                       order = {'QCD':3})

UVGC_186_50 = Coupling(name = 'UVGC_186_50',
                       value = {-1:'G**3/(48.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_186_51 = Coupling(name = 'UVGC_186_51',
                       value = {-1:'(-21*G**3)/(64.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_186_52 = Coupling(name = 'UVGC_186_52',
                       value = {-1:'-G**3/(64.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_186_53 = Coupling(name = 'UVGC_186_53',
                       value = {-1:'-G**3/(24.*cmath.pi**2)',0:'(G**3*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_187_54 = Coupling(name = 'UVGC_187_54',
                       value = {-1:'( 0 if MB else -(complex(0,1)*G**4)/(12.*cmath.pi**2) ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'( -(complex(0,1)*G**4*reglog(MB**2/MU_R**2))/(24.*cmath.pi**2) if MB else 0 )'},
                       order = {'QCD':4})

UVGC_187_55 = Coupling(name = 'UVGC_187_55',
                       value = {-1:'(83*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_187_56 = Coupling(name = 'UVGC_187_56',
                       value = {-1:'(3*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_187_57 = Coupling(name = 'UVGC_187_57',
                       value = {-1:'(complex(0,1)*G**4)/(12.*cmath.pi**2)',0:'-(complex(0,1)*G**4*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_188_58 = Coupling(name = 'UVGC_188_58',
                       value = {-1:'(335*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_188_59 = Coupling(name = 'UVGC_188_59',
                       value = {-1:'(21*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_189_60 = Coupling(name = 'UVGC_189_60',
                       value = {-1:'( 0 if MB else -(complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( -(complex(0,1)*G**4*reglog(MB**2/MU_R**2))/(24.*cmath.pi**2) if MB else 0 )'},
                       order = {'QCD':4})

UVGC_189_61 = Coupling(name = 'UVGC_189_61',
                       value = {-1:'-(complex(0,1)*G**4)/(12.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_189_62 = Coupling(name = 'UVGC_189_62',
                       value = {-1:'(13*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_189_63 = Coupling(name = 'UVGC_189_63',
                       value = {0:'-(complex(0,1)*G**4*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_190_64 = Coupling(name = 'UVGC_190_64',
                       value = {-1:'( 0 if MB else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'( (complex(0,1)*G**4*reglog(MB**2/MU_R**2))/(24.*cmath.pi**2) if MB else 0 )'},
                       order = {'QCD':4})

UVGC_190_65 = Coupling(name = 'UVGC_190_65',
                       value = {-1:'(complex(0,1)*G**4)/(24.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_190_66 = Coupling(name = 'UVGC_190_66',
                       value = {-1:'(-341*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_190_67 = Coupling(name = 'UVGC_190_67',
                       value = {-1:'(-11*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_190_68 = Coupling(name = 'UVGC_190_68',
                       value = {-1:'-(complex(0,1)*G**4)/(24.*cmath.pi**2)',0:'(complex(0,1)*G**4*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_191_69 = Coupling(name = 'UVGC_191_69',
                       value = {-1:'(-83*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_191_70 = Coupling(name = 'UVGC_191_70',
                       value = {-1:'(-5*complex(0,1)*G**4)/(128.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_192_71 = Coupling(name = 'UVGC_192_71',
                       value = {-1:'( 0 if MB else (complex(0,1)*G**4)/(12.*cmath.pi**2) )',0:'( (complex(0,1)*G**4*reglog(MB**2/MU_R**2))/(24.*cmath.pi**2) if MB else 0 )'},
                       order = {'QCD':4})

UVGC_192_72 = Coupling(name = 'UVGC_192_72',
                       value = {-1:'(complex(0,1)*G**4)/(12.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_192_73 = Coupling(name = 'UVGC_192_73',
                       value = {-1:'(-19*complex(0,1)*G**4)/(512.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_192_74 = Coupling(name = 'UVGC_192_74',
                       value = {0:'(complex(0,1)*G**4*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)'},
                       order = {'QCD':4})

UVGC_193_75 = Coupling(name = 'UVGC_193_75',
                       value = {-1:'(complex(0,1)*G**2)/(4.*cmath.pi**2)',0:'(complex(0,1)*G**2)/(3.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MT**2/MU_R**2))/(4.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_194_76 = Coupling(name = 'UVGC_194_76',
                       value = {-1:'-(ee*complex(0,1)*G**2)/(9.*cmath.pi**2)',0:'(-2*ee*complex(0,1)*G**2)/(9.*cmath.pi**2) + (ee*complex(0,1)*G**2*reglog(MT**2/MU_R**2))/(6.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_195_77 = Coupling(name = 'UVGC_195_77',
                       value = {-1:'-(complex(0,1)*G**3)/(6.*cmath.pi**2)',0:'-(complex(0,1)*G**3)/(3.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MT**2/MU_R**2))/(4.*cmath.pi**2)'},
                       order = {'QCD':3})

UVGC_196_78 = Coupling(name = 'UVGC_196_78',
                       value = {-1:'(complex(0,1)*G**2*gAu31)/(12.*cmath.pi**2)',0:'(complex(0,1)*G**2*gAu31)/(6.*cmath.pi**2) - (complex(0,1)*G**2*gAu31*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_196_79 = Coupling(name = 'UVGC_196_79',
                       value = {-1:'-(complex(0,1)*G**2*gAu31)/(24.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_196_80 = Coupling(name = 'UVGC_196_80',
                       value = {-1:'(complex(0,1)*G**2*gAu31)/(12.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_197_81 = Coupling(name = 'UVGC_197_81',
                       value = {-1:'(complex(0,1)*G**2*gAu33)/(4.*cmath.pi**2)',0:'(complex(0,1)*G**2*gAu33)/(3.*cmath.pi**2) - (complex(0,1)*G**2*gAu33*reglog(MT**2/MU_R**2))/(4.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_198_82 = Coupling(name = 'UVGC_198_82',
                       value = {-1:'-(complex(0,1)*G**2*gVu31)/(12.*cmath.pi**2)',0:'-(complex(0,1)*G**2*gVu31)/(6.*cmath.pi**2) + (complex(0,1)*G**2*gVu31*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_198_83 = Coupling(name = 'UVGC_198_83',
                       value = {-1:'(complex(0,1)*G**2*gVu31)/(24.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_198_84 = Coupling(name = 'UVGC_198_84',
                       value = {-1:'-(complex(0,1)*G**2*gVu31)/(12.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_199_85 = Coupling(name = 'UVGC_199_85',
                       value = {-1:'-(complex(0,1)*G**2*gVu33)/(4.*cmath.pi**2)',0:'-(complex(0,1)*G**2*gVu33)/(3.*cmath.pi**2) + (complex(0,1)*G**2*gVu33*reglog(MT**2/MU_R**2))/(4.*cmath.pi**2)'},
                       order = {'DMV':1,'QCD':2})

UVGC_200_86 = Coupling(name = 'UVGC_200_86',
                       value = {-1:'(complex(0,1)*G**2*MT)/(2.*cmath.pi**2)',0:'(2*complex(0,1)*G**2*MT)/(3.*cmath.pi**2) - (complex(0,1)*G**2*MT*reglog(MT**2/MU_R**2))/(2.*cmath.pi**2)'},
                       order = {'QCD':2})

UVGC_201_87 = Coupling(name = 'UVGC_201_87',
                       value = {-1:'( -(ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw*cmath.sqrt(2)) if MB else (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) )',0:'( (-5*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*G**2*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2*sw*cmath.sqrt(2)) if MB else -(ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) ) + (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_201_88 = Coupling(name = 'UVGC_201_88',
                       value = {-1:'-(ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw*cmath.sqrt(2))',0:'-(ee*complex(0,1)*G**2)/(6.*cmath.pi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*G**2*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2*sw*cmath.sqrt(2))'},
                       order = {'QCD':2,'QED':1})

UVGC_202_89 = Coupling(name = 'UVGC_202_89',
                       value = {-1:'-(cw*ee*complex(0,1)*G**2)/(8.*cmath.pi**2*sw)',0:'-(cw*ee*complex(0,1)*G**2)/(6.*cmath.pi**2*sw) + (cw*ee*complex(0,1)*G**2*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2*sw)'},
                       order = {'QCD':2,'QED':1})

UVGC_203_90 = Coupling(name = 'UVGC_203_90',
                       value = {-1:'(ee*complex(0,1)*G**2*sw)/(24.*cw*cmath.pi**2)',0:'(ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2) - (ee*complex(0,1)*G**2*sw*reglog(MT**2/MU_R**2))/(24.*cw*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_204_91 = Coupling(name = 'UVGC_204_91',
                       value = {-1:'( (G**2*yb)/(12.*cmath.pi**2) if MB else -(G**2*yb)/(24.*cmath.pi**2) )',0:'( (13*G**2*yb)/(24.*cmath.pi**2) - (3*G**2*yb*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2) if MB else (G**2*yb)/(24.*cmath.pi**2) ) - (G**2*yb)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_204_92 = Coupling(name = 'UVGC_204_92',
                       value = {-1:'(G**2*yb)/(12.*cmath.pi**2)',0:'(G**2*yb)/(6.*cmath.pi**2) - (G**2*yb*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_204_93 = Coupling(name = 'UVGC_204_93',
                       value = {-1:'(G**2*yb)/(3.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_205_94 = Coupling(name = 'UVGC_205_94',
                       value = {-1:'( -(G**2*yb)/(12.*cmath.pi**2) if MB else (G**2*yb)/(24.*cmath.pi**2) )',0:'( (-13*G**2*yb)/(24.*cmath.pi**2) + (3*G**2*yb*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2) if MB else -(G**2*yb)/(24.*cmath.pi**2) ) + (G**2*yb)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_205_95 = Coupling(name = 'UVGC_205_95',
                       value = {-1:'-(G**2*yb)/(12.*cmath.pi**2)',0:'-(G**2*yb)/(6.*cmath.pi**2) + (G**2*yb*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_205_96 = Coupling(name = 'UVGC_205_96',
                       value = {-1:'-(G**2*yb)/(3.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_206_97 = Coupling(name = 'UVGC_206_97',
                       value = {-1:'( (G**2*yt)/(12.*cmath.pi**2) if MB else -(G**2*yt)/(24.*cmath.pi**2) )',0:'( (5*G**2*yt)/(24.*cmath.pi**2) - (G**2*yt*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2) if MB else (G**2*yt)/(24.*cmath.pi**2) ) - (G**2*yt)/(24.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_206_98 = Coupling(name = 'UVGC_206_98',
                       value = {-1:'(G**2*yt)/(12.*cmath.pi**2)',0:'(G**2*yt)/(2.*cmath.pi**2) - (3*G**2*yt*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_206_99 = Coupling(name = 'UVGC_206_99',
                       value = {-1:'(G**2*yt)/(3.*cmath.pi**2)'},
                       order = {'QCD':2,'QED':1})

UVGC_207_100 = Coupling(name = 'UVGC_207_100',
                        value = {-1:'( -(G**2*yt)/(12.*cmath.pi**2) if MB else (G**2*yt)/(24.*cmath.pi**2) )',0:'( (-5*G**2*yt)/(24.*cmath.pi**2) + (G**2*yt*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2) if MB else -(G**2*yt)/(24.*cmath.pi**2) ) + (G**2*yt)/(24.*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_207_101 = Coupling(name = 'UVGC_207_101',
                        value = {-1:'-(G**2*yt)/(12.*cmath.pi**2)',0:'-(G**2*yt)/(2.*cmath.pi**2) + (3*G**2*yt*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_207_102 = Coupling(name = 'UVGC_207_102',
                        value = {-1:'-(G**2*yt)/(3.*cmath.pi**2)'},
                        order = {'QCD':2,'QED':1})

UVGC_208_103 = Coupling(name = 'UVGC_208_103',
                        value = {-1:'(G**2*yt)/(2.*cmath.pi**2*cmath.sqrt(2))',0:'(G**2*yt*cmath.sqrt(2))/(3.*cmath.pi**2) - (G**2*yt*reglog(MT**2/MU_R**2))/(2.*cmath.pi**2*cmath.sqrt(2))'},
                        order = {'QCD':2,'QED':1})

UVGC_209_104 = Coupling(name = 'UVGC_209_104',
                        value = {-1:'(complex(0,1)*G**2*yt)/(2.*cmath.pi**2*cmath.sqrt(2))',0:'(complex(0,1)*G**2*yt*cmath.sqrt(2))/(3.*cmath.pi**2) - (complex(0,1)*G**2*yt*reglog(MT**2/MU_R**2))/(2.*cmath.pi**2*cmath.sqrt(2))'},
                        order = {'QCD':2,'QED':1})

                                                                                                      CT_couplings.pyo                                                                                    0000644 0276724 0002567 00000104562 13234357560 012524  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc        	   @   s�%  d  d l  m Z m Z d  d l m Z m Z m Z m Z m Z m	 Z	 m
 Z
 m Z e d d d d d i d d	 6d
 d 6� Z e d d d d d i d d	 6d
 d 6� Z e d d d d d i d
 d 6d d 6� Z e d d d d d i d
 d 6d d 6� Z e d d d d d i d
 d 6� Z e d d d d d i d d	 6d
 d 6� Z e d d d d d i d d	 6d
 d 6� Z e d d d d d i d
 d 6d d 6� Z e d d d d d i d d	 6d
 d 6� Z e d d d d d i d d	 6d
 d 6� Z e d d d d  d i d d	 6d
 d 6� Z e d d! d d" d i d d	 6d
 d 6� Z e d d# d d$ d i d
 d 6� Z e d d% d d& d i d
 d 6� Z e d d' d d( d i d
 d 6d d 6� Z e d d) d d* d i d
 d 6d d 6� Z e d d+ d d, d i d
 d 6d
 d 6� Z e d d- d d. d i d
 d 6d
 d 6� Z e d d/ d d0 d i d
 d 6� Z e d d1 d d2 d i d
 d 6d
 d 6� Z e d d3 d d4 d i d
 d 6d
 d 6� Z  e d d5 d d6 d i d7 d 6d d 6� Z! e d d8 d d9 d i d7 d 6d d 6� Z" e d d: d d; d i d d	 6d
 d 6� Z# e d d< d d= d i d d	 6d
 d 6� Z$ e d d> d d? d i d d	 6d
 d 6� Z% e d d@ d dA d i d d	 6d
 d 6� Z& e d dB d dC d i d d	 6d
 d 6� Z' e d dD d dE d i d d	 6d
 d 6� Z( e d dF d dG d i d d	 6d7 d 6� Z) e d dH d dI d i d d	 6d7 d 6� Z* e d dJ d dK d i d d	 6d7 d 6� Z+ e d dL d dM d i d d	 6d7 d 6� Z, e d dN d dO d i d d	 6d7 d 6� Z- e d dP d dQ d i d d	 6d7 d 6� Z. e d dR d dS d i d d	 6d
 d 6d d 6� Z/ e d dT d dU d i d d	 6d
 d 6d d 6� Z0 e d dV d dW d i d d	 6d
 d 6d d 6� Z1 e d dX d dY d i d d	 6d
 d 6d d 6� Z2 e d dZ d d[ d i d d	 6d
 d 6d d 6� Z3 e d d\ d d] d i d d	 6d
 d 6d d 6� Z4 e d d^ d d_ d i d d	 6d7 d 6� Z5 e d d` d da d i d d	 6d7 d 6� Z6 e d db d dc d i d d	 6d7 d 6� Z7 e d dd d de d i d d	 6d7 d 6� Z8 e d df d dg d i d d	 6d7 d 6� Z9 e d dh d di d i d d	 6d7 d 6� Z: e d dj d dk d i d
 d 6d d 6� Z; e d dl d dm d i d
 d 6d d 6� Z< e d dn d do d i d
 d 6d
 d 6� Z= e d dp d dq d i d
 d 6d
 d 6� Z> e d dr d ds d i d7 d 6d d 6� Z? e d dt d du d i d7 d 6d d 6� Z@ e d dv d dw d i d7 d 6d d 6� ZA e d dx d dy d i d7 d 6d d 6� ZB e d dz d d{ d i d d	 6d
 d 6d d 6� ZC e d d| d d} d i d d	 6d
 d 6d d 6� ZD e d d~ d d d i d d	 6d
 d 6d d 6� ZE e d d� d d� d i d d	 6d
 d 6d d 6� ZF e d d� d d� d i d d	 6d
 d 6d d 6� ZG e d d� d d� d i d d	 6d
 d 6d d 6� ZH e d d� d d� d i d
 d 6d
 d 6� ZI e d d� d d� d i d
 d 6d
 d 6� ZJ e d d� d d� d i d
 d 6d
 d 6� ZK e d d� d d� d i d
 d 6d
 d 6� ZL e d d� d d� d i d
 d	 6d
 d 6� ZM e d d� d d� d i d
 d	 6d
 d 6� ZN e d d� d d� d i d
 d	 6d
 d 6� ZO e d d� d d� d i d
 d	 6d
 d 6� ZP e d d� d d� d i d
 d	 6d
 d 6� ZQ e d d� d d� d i d
 d	 6d
 d 6� ZR e d d� d d� d i d
 d	 6d
 d 6� ZS e d d� d d� d i d
 d	 6d
 d 6� ZT e d d� d d� d i d� d 6� ZU e d d� d d� d i d� d 6� ZV e d d� d d� d i d� d 6� ZW e d d� d d� d i d� d 6� ZX e d d� d d� d i d� d 6� ZY e d d� d d� d i d� d 6� ZZ e d d� d d� d i d� d 6� Z[ e d d� d d� d i d� d 6� Z\ e d d� d d� d i d� d 6� Z] e d d� d d� d i d� d 6� Z^ e d d� d d� d i d� d 6� Z_ e d d� d d� d i d
 d 6d d 6� Z` e d d� d d� d i d7 d 6� Za e d d� d d� d i d
 d 6d d 6� Zb e d d� d d� d i d
 d 6d d 6� Zc e d d� d d� d i d d	 6d
 d 6� Zd e d d� d d� d i d d	 6d
 d 6� Ze e d d� d d� d i d d	 6d
 d 6� Zf e d d� d d� d i d d	 6d
 d 6� Zg e d d� d d� d i d
 d 6� Zh e d d� d d� d i d
 d 6d d 6� Zi e d d� d d� d i d
 d 6d d 6� Zj e d d� d d� d i d7 d 6� Zk e d d� d d� d i d7 d 6� Zl e d d� d d� d i d7 d 6� Zm e d d� d d� d i d7 d 6� Zn e d d� d d� d i d� d 6� Zo e d d� d d� d i d� d 6� Zp e d d� d d� d i d� d 6� Zq e d d� d d� d i d� d 6� Zr e d d� d d� d i d� d 6� Zs e d d� d d� d i d� d 6� Zt e d d� d d� d i d d	 6d
 d 6� Zu e d d� d d� d i d d	 6d
 d 6� Zv e d d� d d� d i d d	 6d
 d 6� Zw e d d� d d� d i d d	 6d
 d 6� Zx e d d� d d� d i d
 d 6� Zy e d d� d d� d i d
 d 6d d 6� Zz e d d� d d� d i d
 d 6d d 6� Z{ e d d� d d� d i d
 d 6d d 6� Z| e d d� d d� d i d
 d 6d d 6� Z} e d d� d d� d i d
 d 6d d 6� Z~ e d d� d d� d i d
 d 6d d 6� Z e d d� d d� d i d
 d 6� Z� e d d� d i d� d  6d i d
 d 6� Z� e d d� d i d� d  6d i d
 d 6d d 6� Z� e d d� d i d� d  6d i d
 d 6d d 6� Z� e d d� d i d� d  6d i d
 d 6� Z� e d d� d i d� d  6d i d
 d 6� Z� e d d d i dd  6d i d� d 6� Z� e d dd i dd  6d i d� d 6� Z� e d dd i dd  6d i d� d 6� Z� e d dd i dd  6d i d� d 6� Z� e d dd i d	d  6d i d� d 6� Z� e d d
d i dd  6d i d� d 6� Z� e d dd i dd  6d i d� d 6� Z� e d dd i dd  6d i d� d 6� Z� e d dd i dd  6d i d� d 6� Z� e d dd i dd  6d i d� d 6� Z� e d dd i dd  6d i d
 d 6d d 6� Z� e d dd i dd  6d i d7 d 6� Z� e d dd i dd  6d i d
 d 6d d 6� Z� e d dd i dd  6d i d7 d 6� Z� e d dd i dd  6d i d7 d 6� Z� e d dd i dd  6d i d7 d 6� Z� e d d d i d!d  6d i d7 d 6� Z� e d d"d i d#d  6d i d7 d 6� Z� e d d$d i d%d  6d i d
 d 6d d 6� Z� e d d&d i d'd  6d i d
 d 6d d 6� Z� e d d(d i d)d  6d*d+6d i d
 d 6� Z� e d d,d i d-d  6d.d+6d i d
 d 6d d 6� Z� e d d/d i d0d  6d1d+6d i d7 d 6� Z� e d d2d i d3d  6d4d+6d i d d	 6d
 d 6� Z� e d d5d i d6d  6d i d d	 6d
 d 6� Z� e d d7d i d8d  6d i d d	 6d
 d 6� Z� e d d9d i d:d  6d;d+6d i d d	 6d
 d 6� Z� e d d<d i d=d  6d>d+6d i d d	 6d
 d 6� Z� e d d?d i d@d  6d i d d	 6d
 d 6� Z� e d dAd i dBd  6d i d d	 6d
 d 6� Z� e d dCd i dDd  6dEd+6d i d d	 6d
 d 6� Z� e d dFd i dGd  6dHd+6d i d
 d 6� Z� e d dId i dJd  6dKd+6d i d
 d 6d d 6� Z� e d dLd i dMd  6dNd+6d i d
 d 6d d 6� Z� e d dOd i dPd  6dQd+6d i d
 d 6d d 6� Z� e d dRd i dSd  6dTd+6d i d
 d 6d d 6� Z� e d dUd i dVd  6dWd+6d i d
 d 6� Z� e d dXd i dYd  6dZd+6d i d
 d 6� Z� e d d[d i d\d  6d]d+6d i d7 d 6� Z� e d d^d i d_d  6d i d7 d 6� Z� e d d`d i dad  6d i d7 d 6� Z� e d dbd i dcd  6d i d7 d 6� Z� e d ddd i d� d  6ded+6d i d7 d 6� Z� e d dfd i dgd  6dhd+6d i d7 d 6� Z� e d did i djd  6d i d7 d 6� Z� e d dkd i dld  6d i d7 d 6� Z� e d dmd i dnd  6d i d7 d 6� Z� e d dod i d� d  6dpd+6d i d7 d 6� Z� e d dqd i drd  6dsd+6d i d� d 6� Z� e d dtd i dud  6d i d� d 6� Z� e d dvd i dwd  6d i d� d 6� Z� e d dxd i dyd  6dzd+6d i d� d 6� Z� e d d{d i d|d  6d i d� d 6� Z� e d d}d i d~d  6d i d� d 6� Z� e d dd i d�d  6dsd+6d i d� d 6� Z� e d d�d i d�d  6d i d� d 6� Z� e d d�d i d�d  6d i d� d 6� Z� e d d�d i dzd+6d i d� d 6� Z� e d d�d i d�d  6d�d+6d i d� d 6� Z� e d d�d i d�d  6d i d� d 6� Z� e d d�d i d�d  6d i d� d 6� Z� e d d�d i d�d  6d i d� d 6� Z� e d d�d i dd  6d�d+6d i d� d 6� Z� e d d�d i d�d  6d i d� d 6� Z� e d d�d i d�d  6d i d� d 6� Z� e d d�d i d�d  6d�d+6d i d� d 6� Z� e d d�d i dyd  6d i d� d 6� Z� e d d�d i d�d  6d i d� d 6� Z� e d d�d i d�d+6d i d� d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6� Z� e d d�d i d� d  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d� d  6d�d+6d i d7 d 6� Z� e d d�d i d�d  6d�d+6d i d d	 6d
 d 6� Z� e d d�d i d�d  6d i d d	 6d
 d 6� Z� e d d�d i d�d  6d i d d	 6d
 d 6� Z� e d d�d i d�d  6d�d+6d i d d	 6d
 d 6� Z� e d d�d i d�d  6d�d+6d i d d	 6d
 d 6� Z� e d d�d i d�d  6d i d d	 6d
 d 6� Z� e d d�d i d�d  6d i d d	 6d
 d 6� Z� e d d�d i d�d  6d�d+6d i d d	 6d
 d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d'd  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d� d  6d i d
 d 6d d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d� d  6d i d
 d 6d d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d� d  6d i d
 d 6d d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d� d  6d i d
 d 6d d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6d d 6� Z� e d d�d i d�d  6d�d+6d i d
 d 6d d 6� Z� d�S(�  i����(   t   all_couplingst   Coupling(   t   complexconjugatet   ret   imt   csct   sect   acsct   asect   cott   namet
   R2GC_100_1t   values*   (complex(0,1)*G**2*gAu22)/(6.*cmath.pi**2)t   orderi   t   DMVi   t   QCDt
   R2GC_101_2s+   -(complex(0,1)*G**2*gVu22)/(6.*cmath.pi**2)t
   R2GC_102_3s/   -(cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw)t   QEDt
   R2GC_103_4s.   (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2)t
   R2GC_104_5s%   (complex(0,1)*G**2)/(12.*cmath.pi**2)t
   R2GC_105_6s*   (complex(0,1)*G**2*gAd11)/(6.*cmath.pi**2)t
   R2GC_106_7s+   -(complex(0,1)*G**2*gVd11)/(6.*cmath.pi**2)t
   R2GC_107_8s.   (cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw)t
   R2GC_110_9s*   (complex(0,1)*G**2*gAd22)/(6.*cmath.pi**2)t   R2GC_111_10s+   -(complex(0,1)*G**2*gVd22)/(6.*cmath.pi**2)t   R2GC_115_11s*   (complex(0,1)*G**2*gAu11)/(6.*cmath.pi**2)t   R2GC_116_12s+   -(complex(0,1)*G**2*gVu11)/(6.*cmath.pi**2)t   R2GC_119_13s+   -(complex(0,1)*G**2*MB**2)/(8.*cmath.pi**2)t   R2GC_119_14s+   -(complex(0,1)*G**2*MT**2)/(8.*cmath.pi**2)t   R2GC_120_15s9   -(complex(0,1)*G**2*MB*yb)/(8.*cmath.pi**2*cmath.sqrt(2))t   R2GC_120_16s9   -(complex(0,1)*G**2*MT*yt)/(8.*cmath.pi**2*cmath.sqrt(2))t   R2GC_121_17s,   -(complex(0,1)*G**2*yb**2)/(16.*cmath.pi**2)t   R2GC_121_18s,   -(complex(0,1)*G**2*yt**2)/(16.*cmath.pi**2)t   R2GC_122_19s%   (complex(0,1)*G**2)/(48.*cmath.pi**2)t   R2GC_123_20s,   (ee**2*complex(0,1)*G**2)/(216.*cmath.pi**2)t   R2GC_123_21s+   (ee**2*complex(0,1)*G**2)/(54.*cmath.pi**2)t   R2GC_124_22s*   -(ee*complex(0,1)*G**3)/(144.*cmath.pi**2)i   t   R2GC_124_23s(   (ee*complex(0,1)*G**3)/(72.*cmath.pi**2)t   R2GC_125_24s   -(G**2*gAd33)/(12.*cmath.pi**2)t   R2GC_125_25s   -(G**2*gAu22)/(12.*cmath.pi**2)t   R2GC_125_26s   -(G**2*gAd11)/(12.*cmath.pi**2)t   R2GC_125_27s   -(G**2*gAd22)/(12.*cmath.pi**2)t   R2GC_125_28s   -(G**2*gAu33)/(12.*cmath.pi**2)t   R2GC_125_29s   -(G**2*gAu11)/(12.*cmath.pi**2)t   R2GC_126_30s,   -(complex(0,1)*G**3*gAd33)/(16.*cmath.pi**2)t   R2GC_126_31s,   -(complex(0,1)*G**3*gAu22)/(16.*cmath.pi**2)t   R2GC_126_32s,   -(complex(0,1)*G**3*gAd11)/(16.*cmath.pi**2)t   R2GC_126_33s,   -(complex(0,1)*G**3*gAd22)/(16.*cmath.pi**2)t   R2GC_126_34s,   -(complex(0,1)*G**3*gAu33)/(16.*cmath.pi**2)t   R2GC_126_35s,   -(complex(0,1)*G**3*gAu11)/(16.*cmath.pi**2)t   R2GC_127_36s/   -(ee*complex(0,1)*G**2*gVd33)/(72.*cmath.pi**2)t   R2GC_127_37s.   (ee*complex(0,1)*G**2*gVu22)/(36.*cmath.pi**2)t   R2GC_127_38s/   -(ee*complex(0,1)*G**2*gVd11)/(72.*cmath.pi**2)t   R2GC_127_39s/   -(ee*complex(0,1)*G**2*gVd22)/(72.*cmath.pi**2)t   R2GC_127_40s.   (ee*complex(0,1)*G**2*gVu33)/(36.*cmath.pi**2)t   R2GC_127_41s.   (ee*complex(0,1)*G**2*gVu11)/(36.*cmath.pi**2)t   R2GC_128_42s+   (complex(0,1)*G**3*gVd33)/(48.*cmath.pi**2)t   R2GC_128_43s+   (complex(0,1)*G**3*gVu22)/(48.*cmath.pi**2)t   R2GC_128_44s+   (complex(0,1)*G**3*gVd11)/(48.*cmath.pi**2)t   R2GC_128_45s+   (complex(0,1)*G**3*gVd22)/(48.*cmath.pi**2)t   R2GC_128_46s+   (complex(0,1)*G**3*gVu33)/(48.*cmath.pi**2)t   R2GC_128_47s+   (complex(0,1)*G**3*gVu11)/(48.*cmath.pi**2)t   R2GC_129_48sF   -(cw*ee*G**2)/(48.*cmath.pi**2*sw) - (ee*G**2*sw)/(48.*cw*cmath.pi**2)t   R2GC_129_49sE   (cw*ee*G**2)/(48.*cmath.pi**2*sw) + (ee*G**2*sw)/(48.*cw*cmath.pi**2)t   R2GC_130_50sg   (cw*ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2*sw) - (ee**2*complex(0,1)*G**2*sw)/(864.*cw*cmath.pi**2)t   R2GC_130_51si   (cw*ee**2*complex(0,1)*G**2)/(144.*cmath.pi**2*sw) - (5*ee**2*complex(0,1)*G**2*sw)/(432.*cw*cmath.pi**2)t   R2GC_131_52sb   -(cw*ee*complex(0,1)*G**3)/(192.*cmath.pi**2*sw) + (ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)t   R2GC_131_53sc   (cw*ee*complex(0,1)*G**3)/(192.*cmath.pi**2*sw) - (5*ee*complex(0,1)*G**3*sw)/(576.*cw*cmath.pi**2)t   R2GC_132_54sc   (3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) + (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)t   R2GC_132_55sd   (-3*cw*ee*complex(0,1)*G**3)/(64.*cmath.pi**2*sw) - (3*ee*complex(0,1)*G**3*sw)/(64.*cw*cmath.pi**2)t   R2GC_133_56s�   (cw*ee*complex(0,1)*G**2*gAd33)/(96.*cmath.pi**2*sw) - (cw*ee*complex(0,1)*G**2*gVd33)/(96.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*gAd33*sw)/(96.*cw*cmath.pi**2) + (ee*complex(0,1)*G**2*gVd33*sw)/(288.*cw*cmath.pi**2)t   R2GC_133_57s�   -(cw*ee*complex(0,1)*G**2*gAu22)/(96.*cmath.pi**2*sw) + (cw*ee*complex(0,1)*G**2*gVu22)/(96.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*gAu22*sw)/(96.*cw*cmath.pi**2) - (5*ee*complex(0,1)*G**2*gVu22*sw)/(288.*cw*cmath.pi**2)t   R2GC_133_58s�   (cw*ee*complex(0,1)*G**2*gAd11)/(96.*cmath.pi**2*sw) - (cw*ee*complex(0,1)*G**2*gVd11)/(96.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*gAd11*sw)/(96.*cw*cmath.pi**2) + (ee*complex(0,1)*G**2*gVd11*sw)/(288.*cw*cmath.pi**2)t   R2GC_133_59s�   (cw*ee*complex(0,1)*G**2*gAd22)/(96.*cmath.pi**2*sw) - (cw*ee*complex(0,1)*G**2*gVd22)/(96.*cmath.pi**2*sw) + (ee*complex(0,1)*G**2*gAd22*sw)/(96.*cw*cmath.pi**2) + (ee*complex(0,1)*G**2*gVd22*sw)/(288.*cw*cmath.pi**2)t   R2GC_133_60s�   -(cw*ee*complex(0,1)*G**2*gAu33)/(96.*cmath.pi**2*sw) + (cw*ee*complex(0,1)*G**2*gVu33)/(96.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*gAu33*sw)/(96.*cw*cmath.pi**2) - (5*ee*complex(0,1)*G**2*gVu33*sw)/(288.*cw*cmath.pi**2)t   R2GC_133_61s�   -(cw*ee*complex(0,1)*G**2*gAu11)/(96.*cmath.pi**2*sw) + (cw*ee*complex(0,1)*G**2*gVu11)/(96.*cmath.pi**2*sw) - (ee*complex(0,1)*G**2*gAu11*sw)/(96.*cw*cmath.pi**2) - (5*ee*complex(0,1)*G**2*gVu11*sw)/(288.*cw*cmath.pi**2)t   R2GC_134_62s�   (ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2) + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (5*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)t   R2GC_134_63s�   -(ee**2*complex(0,1)*G**2)/(288.*cmath.pi**2) + (cw**2*ee**2*complex(0,1)*G**2)/(192.*cmath.pi**2*sw**2) + (17*ee**2*complex(0,1)*G**2*sw**2)/(1728.*cw**2*cmath.pi**2)t   R2GC_135_64sZ   -(complex(0,1)*G**2*yb**2)/(16.*cmath.pi**2) - (complex(0,1)*G**2*yt**2)/(16.*cmath.pi**2)t   R2GC_136_65s1   (ee**2*complex(0,1)*G**2)/(96.*cmath.pi**2*sw**2)t   R2GC_137_66s_   (complex(0,1)*G**2*gAd33**2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVd33**2)/(24.*cmath.pi**2)t   R2GC_137_67s_   (complex(0,1)*G**2*gAu22**2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVu22**2)/(24.*cmath.pi**2)t   R2GC_137_68s_   (complex(0,1)*G**2*gAd11**2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVd11**2)/(24.*cmath.pi**2)t   R2GC_137_69s_   (complex(0,1)*G**2*gAd22**2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVd22**2)/(24.*cmath.pi**2)t   R2GC_137_70s_   (complex(0,1)*G**2*gAu33**2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVu33**2)/(24.*cmath.pi**2)t   R2GC_137_71s_   (complex(0,1)*G**2*gAu11**2)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVu11**2)/(24.*cmath.pi**2)t   R2GC_137_72s_   (complex(0,1)*G**2*gAd31**2)/(12.*cmath.pi**2) + (complex(0,1)*G**2*gVd31**2)/(12.*cmath.pi**2)t   R2GC_137_73s_   (complex(0,1)*G**2*gAu31**2)/(12.*cmath.pi**2) + (complex(0,1)*G**2*gVu31**2)/(12.*cmath.pi**2)t   R2GC_147_74s   -G**4/(192.*cmath.pi**2)i   t   R2GC_147_75s   G**4/(64.*cmath.pi**2)t   R2GC_148_76s'   -(complex(0,1)*G**4)/(192.*cmath.pi**2)t   R2GC_148_77s%   (complex(0,1)*G**4)/(64.*cmath.pi**2)t   R2GC_149_78s&   (complex(0,1)*G**4)/(192.*cmath.pi**2)t   R2GC_149_79s&   -(complex(0,1)*G**4)/(64.*cmath.pi**2)t   R2GC_150_80s&   -(complex(0,1)*G**4)/(48.*cmath.pi**2)t   R2GC_151_81s&   (complex(0,1)*G**4)/(288.*cmath.pi**2)t   R2GC_151_82s&   -(complex(0,1)*G**4)/(32.*cmath.pi**2)t   R2GC_152_83s&   -(complex(0,1)*G**4)/(16.*cmath.pi**2)t   R2GC_153_84s(   (-3*complex(0,1)*G**4)/(64.*cmath.pi**2)t   R2GC_154_85s(   (ee*complex(0,1)*G**2)/(18.*cmath.pi**2)t   R2GC_155_86s%   -(complex(0,1)*G**3)/(6.*cmath.pi**2)t   R2GC_156_87s(   -(ee*complex(0,1)*G**2)/(9.*cmath.pi**2)t   R2GC_170_88s9   -(ee*complex(0,1)*G**2)/(6.*cmath.pi**2*sw*cmath.sqrt(2))t   R2GC_175_89s*   (complex(0,1)*G**2*gAd31)/(6.*cmath.pi**2)t   R2GC_176_90s*   (complex(0,1)*G**2*gAd33)/(6.*cmath.pi**2)t   R2GC_177_91s+   -(complex(0,1)*G**2*gVd31)/(6.*cmath.pi**2)t   R2GC_178_92s+   -(complex(0,1)*G**2*gVd33)/(6.*cmath.pi**2)t   R2GC_179_93s'   (complex(0,1)*G**2*MB)/(6.*cmath.pi**2)t   R2GC_182_94s5   (complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))t   R2GC_183_95s)   -(G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))t   R2GC_185_96s   G**3/(24.*cmath.pi**2)t   R2GC_185_97s   (11*G**3)/(64.*cmath.pi**2)t   R2GC_186_98s   -G**3/(24.*cmath.pi**2)t   R2GC_186_99s   (-11*G**3)/(64.*cmath.pi**2)t   R2GC_187_100s'   (5*complex(0,1)*G**4)/(48.*cmath.pi**2)t   R2GC_187_101s'   (7*complex(0,1)*G**4)/(32.*cmath.pi**2)t   R2GC_188_102s)   (23*complex(0,1)*G**4)/(192.*cmath.pi**2)t   R2GC_188_103s(   (15*complex(0,1)*G**4)/(64.*cmath.pi**2)t   R2GC_190_104s)   (-17*complex(0,1)*G**4)/(64.*cmath.pi**2)t   R2GC_191_105s(   (-7*complex(0,1)*G**4)/(32.*cmath.pi**2)t   R2GC_196_106s*   (complex(0,1)*G**2*gAu31)/(6.*cmath.pi**2)t   R2GC_197_107s*   (complex(0,1)*G**2*gAu33)/(6.*cmath.pi**2)t   R2GC_198_108s+   -(complex(0,1)*G**2*gVu31)/(6.*cmath.pi**2)t   R2GC_199_109s+   -(complex(0,1)*G**2*gVu33)/(6.*cmath.pi**2)t   R2GC_200_110s'   (complex(0,1)*G**2*MT)/(6.*cmath.pi**2)t   R2GC_204_111s   (G**2*yb)/(3.*cmath.pi**2)t   R2GC_205_112s   -(G**2*yb)/(3.*cmath.pi**2)t   R2GC_206_113s   (G**2*yt)/(3.*cmath.pi**2)t   R2GC_207_114s   -(G**2*yt)/(3.*cmath.pi**2)t   R2GC_208_115s(   (G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))t   R2GC_209_116s5   (complex(0,1)*G**2*yt)/(3.*cmath.pi**2*cmath.sqrt(2))t   R2GC_98_117s&   -(complex(0,1)*G**2)/(16.*cmath.pi**2)t
   UVGC_138_1s&   -(complex(0,1)*G**2)/(12.*cmath.pi**2)t
   UVGC_139_2t
   UVGC_141_3s)   -(ee*complex(0,1)*G**2)/(36.*cmath.pi**2)t
   UVGC_146_4s'   (3*complex(0,1)*G**2)/(64.*cmath.pi**2)t
   UVGC_146_5s(   (-3*complex(0,1)*G**2)/(64.*cmath.pi**2)t
   UVGC_147_6s   (3*G**4)/(512.*cmath.pi**2)t
   UVGC_147_7s   (-3*G**4)/(512.*cmath.pi**2)t
   UVGC_148_8s(   (3*complex(0,1)*G**4)/(512.*cmath.pi**2)t
   UVGC_148_9s)   (-3*complex(0,1)*G**4)/(512.*cmath.pi**2)t   UVGC_150_10s'   -(complex(0,1)*G**4)/(128.*cmath.pi**2)t   UVGC_150_11s&   (complex(0,1)*G**4)/(128.*cmath.pi**2)t   UVGC_151_12s)   (-3*complex(0,1)*G**4)/(256.*cmath.pi**2)t   UVGC_151_13s(   (3*complex(0,1)*G**4)/(256.*cmath.pi**2)t   UVGC_152_14s&   -(complex(0,1)*G**4)/(24.*cmath.pi**2)t   UVGC_153_15s(   (5*complex(0,1)*G**4)/(512.*cmath.pi**2)t   UVGC_154_16s(   (ee*complex(0,1)*G**2)/(36.*cmath.pi**2)t   UVGC_155_17s)   (-13*complex(0,1)*G**3)/(48.*cmath.pi**2)t   UVGC_156_18s)   -(ee*complex(0,1)*G**2)/(18.*cmath.pi**2)t   UVGC_157_19s6   ( 0 if MB else (complex(0,1)*G**3)/(48.*cmath.pi**2) )t   UVGC_157_20s%   (complex(0,1)*G**3)/(48.*cmath.pi**2)t   UVGC_157_21s*   (-19*complex(0,1)*G**3)/(128.*cmath.pi**2)t   UVGC_157_22s'   -(complex(0,1)*G**3)/(128.*cmath.pi**2)t   UVGC_157_23s%   (complex(0,1)*G**3)/(12.*cmath.pi**2)t   UVGC_170_24s9   (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))t   UVGC_170_25s:   -(ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw*cmath.sqrt(2))t   UVGC_172_26s�   ( (complex(0,1)*G**2)/(6.*cmath.pi**2) if MB else -(complex(0,1)*G**2)/(12.*cmath.pi**2) ) + (complex(0,1)*G**2)/(12.*cmath.pi**2)s�   ( (5*complex(0,1)*G**2)/(12.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MB**2/MU_R**2))/(4.*cmath.pi**2) if MB else (complex(0,1)*G**2)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2)/(12.*cmath.pi**2)i    t   UVGC_173_27sa   ( (ee*complex(0,1)*G**2)/(18.*cmath.pi**2) if MB else -(ee*complex(0,1)*G**2)/(36.*cmath.pi**2) )s�   ( (5*ee*complex(0,1)*G**2)/(36.*cmath.pi**2) - (ee*complex(0,1)*G**2*reglog(MB**2/MU_R**2))/(12.*cmath.pi**2) if MB else (ee*complex(0,1)*G**2)/(36.*cmath.pi**2) ) - (ee*complex(0,1)*G**2)/(36.*cmath.pi**2)t   UVGC_174_28sZ   ( -(complex(0,1)*G**3)/(6.*cmath.pi**2) if MB else (complex(0,1)*G**3)/(12.*cmath.pi**2) )s�   ( (-5*complex(0,1)*G**3)/(12.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MB**2/MU_R**2))/(4.*cmath.pi**2) if MB else -(complex(0,1)*G**3)/(12.*cmath.pi**2) ) + (complex(0,1)*G**3)/(12.*cmath.pi**2)t   UVGC_175_29sg   ( (complex(0,1)*G**2*gAd31)/(12.*cmath.pi**2) if MB else -(complex(0,1)*G**2*gAd31)/(24.*cmath.pi**2) )s�   ( (5*complex(0,1)*G**2*gAd31)/(24.*cmath.pi**2) - (complex(0,1)*G**2*gAd31*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2) if MB else (complex(0,1)*G**2*gAd31)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2*gAd31)/(24.*cmath.pi**2)t   UVGC_175_30s,   -(complex(0,1)*G**2*gAd31)/(24.*cmath.pi**2)t   UVGC_175_31s+   (complex(0,1)*G**2*gAd31)/(12.*cmath.pi**2)t   UVGC_176_32s�   ( (complex(0,1)*G**2*gAd33)/(6.*cmath.pi**2) if MB else -(complex(0,1)*G**2*gAd33)/(12.*cmath.pi**2) ) + (complex(0,1)*G**2*gAd33)/(12.*cmath.pi**2)s�   ( (5*complex(0,1)*G**2*gAd33)/(12.*cmath.pi**2) - (complex(0,1)*G**2*gAd33*reglog(MB**2/MU_R**2))/(4.*cmath.pi**2) if MB else (complex(0,1)*G**2*gAd33)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*gAd33)/(12.*cmath.pi**2)t   UVGC_177_33sg   ( -(complex(0,1)*G**2*gVd31)/(12.*cmath.pi**2) if MB else (complex(0,1)*G**2*gVd31)/(24.*cmath.pi**2) )s�   ( (-5*complex(0,1)*G**2*gVd31)/(24.*cmath.pi**2) + (complex(0,1)*G**2*gVd31*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2) if MB else -(complex(0,1)*G**2*gVd31)/(24.*cmath.pi**2) ) + (complex(0,1)*G**2*gVd31)/(24.*cmath.pi**2)t   UVGC_177_34s+   (complex(0,1)*G**2*gVd31)/(24.*cmath.pi**2)t   UVGC_177_35s,   -(complex(0,1)*G**2*gVd31)/(12.*cmath.pi**2)t   UVGC_178_36s�   ( -(complex(0,1)*G**2*gVd33)/(6.*cmath.pi**2) if MB else (complex(0,1)*G**2*gVd33)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*gVd33)/(12.*cmath.pi**2)s�   ( (-5*complex(0,1)*G**2*gVd33)/(12.*cmath.pi**2) + (complex(0,1)*G**2*gVd33*reglog(MB**2/MU_R**2))/(4.*cmath.pi**2) if MB else -(complex(0,1)*G**2*gVd33)/(12.*cmath.pi**2) ) + (complex(0,1)*G**2*gVd33)/(12.*cmath.pi**2)t   UVGC_179_37s�   ( (complex(0,1)*G**2*MB)/(6.*cmath.pi**2) if MB else -(complex(0,1)*G**2*MB)/(12.*cmath.pi**2) ) + (complex(0,1)*G**2*MB)/(3.*cmath.pi**2)s�   ( (3*complex(0,1)*G**2*MB)/(4.*cmath.pi**2) - (complex(0,1)*G**2*MB*reglog(MB**2/MU_R**2))/(2.*cmath.pi**2) if MB else (complex(0,1)*G**2*MB)/(12.*cmath.pi**2) ) - (complex(0,1)*G**2*MB)/(12.*cmath.pi**2)t   UVGC_180_38s�   ( (cw*ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw) if MB else -(cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) ) + (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw)s�   ( (5*cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) - (cw*ee*complex(0,1)*G**2*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2*sw) if MB else (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw) ) - (cw*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw)t   UVGC_181_39s�   ( (ee*complex(0,1)*G**2*sw)/(36.*cw*cmath.pi**2) if MB else -(ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) + (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)s�   ( (5*ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) - (ee*complex(0,1)*G**2*sw*reglog(MB**2/MU_R**2))/(24.*cw*cmath.pi**2) if MB else (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2) ) - (ee*complex(0,1)*G**2*sw)/(72.*cw*cmath.pi**2)t   UVGC_182_40s�   ( (complex(0,1)*G**2*yb)/(6.*cmath.pi**2*cmath.sqrt(2)) if MB else -(complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (complex(0,1)*G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))s  ( (3*complex(0,1)*G**2*yb)/(4.*cmath.pi**2*cmath.sqrt(2)) - (complex(0,1)*G**2*yb*reglog(MB**2/MU_R**2))/(2.*cmath.pi**2*cmath.sqrt(2)) if MB else (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (complex(0,1)*G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2))t   UVGC_183_41s�   ( -(G**2*yb)/(6.*cmath.pi**2*cmath.sqrt(2)) if MB else (G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) - (G**2*yb)/(3.*cmath.pi**2*cmath.sqrt(2))s�   ( (-3*G**2*yb)/(4.*cmath.pi**2*cmath.sqrt(2)) + (G**2*yb*reglog(MB**2/MU_R**2))/(2.*cmath.pi**2*cmath.sqrt(2)) if MB else -(G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2)) ) + (G**2*yb)/(12.*cmath.pi**2*cmath.sqrt(2))t   UVGC_184_42s^   ( 0 if MB else (complex(0,1)*G**2)/(24.*cmath.pi**2) ) - (complex(0,1)*G**2)/(24.*cmath.pi**2)sL   ( (complex(0,1)*G**2*reglog(MB**2/MU_R**2))/(24.*cmath.pi**2) if MB else 0 )t   UVGC_184_43s&   -(complex(0,1)*G**2)/(24.*cmath.pi**2)s;   (complex(0,1)*G**2*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)t   UVGC_185_44sA   ( 0 if MB else -G**3/(16.*cmath.pi**2) ) + G**3/(24.*cmath.pi**2)s@   ( -(G**3*reglog(MB**2/MU_R**2))/(24.*cmath.pi**2) if MB else 0 )t   UVGC_185_45s   -G**3/(48.*cmath.pi**2)t   UVGC_185_46s   (21*G**3)/(64.*cmath.pi**2)t   UVGC_185_47s   G**3/(64.*cmath.pi**2)t   UVGC_185_48s/   -(G**3*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)t   UVGC_186_49s@   ( 0 if MB else G**3/(16.*cmath.pi**2) ) - G**3/(24.*cmath.pi**2)s?   ( (G**3*reglog(MB**2/MU_R**2))/(24.*cmath.pi**2) if MB else 0 )t   UVGC_186_50s   G**3/(48.*cmath.pi**2)t   UVGC_186_51s   (-21*G**3)/(64.*cmath.pi**2)t   UVGC_186_52s   -G**3/(64.*cmath.pi**2)t   UVGC_186_53s.   (G**3*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)t   UVGC_187_54s_   ( 0 if MB else -(complex(0,1)*G**4)/(12.*cmath.pi**2) ) + (complex(0,1)*G**4)/(12.*cmath.pi**2)sM   ( -(complex(0,1)*G**4*reglog(MB**2/MU_R**2))/(24.*cmath.pi**2) if MB else 0 )t   UVGC_187_55s)   (83*complex(0,1)*G**4)/(128.*cmath.pi**2)t   UVGC_187_56s(   (3*complex(0,1)*G**4)/(128.*cmath.pi**2)t   UVGC_187_57s%   (complex(0,1)*G**4)/(12.*cmath.pi**2)s<   -(complex(0,1)*G**4*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)t   UVGC_188_58s*   (335*complex(0,1)*G**4)/(512.*cmath.pi**2)t   UVGC_188_59s)   (21*complex(0,1)*G**4)/(512.*cmath.pi**2)t   UVGC_189_60s7   ( 0 if MB else -(complex(0,1)*G**4)/(12.*cmath.pi**2) )t   UVGC_189_61s&   -(complex(0,1)*G**4)/(12.*cmath.pi**2)t   UVGC_189_62s)   (13*complex(0,1)*G**4)/(512.*cmath.pi**2)t   UVGC_189_63t   UVGC_190_64s^   ( 0 if MB else (complex(0,1)*G**4)/(12.*cmath.pi**2) ) - (complex(0,1)*G**4)/(24.*cmath.pi**2)sL   ( (complex(0,1)*G**4*reglog(MB**2/MU_R**2))/(24.*cmath.pi**2) if MB else 0 )t   UVGC_190_65s%   (complex(0,1)*G**4)/(24.*cmath.pi**2)t   UVGC_190_66s+   (-341*complex(0,1)*G**4)/(512.*cmath.pi**2)t   UVGC_190_67s*   (-11*complex(0,1)*G**4)/(512.*cmath.pi**2)t   UVGC_190_68s;   (complex(0,1)*G**4*reglog(MT**2/MU_R**2))/(24.*cmath.pi**2)t   UVGC_191_69s*   (-83*complex(0,1)*G**4)/(128.*cmath.pi**2)t   UVGC_191_70s)   (-5*complex(0,1)*G**4)/(128.*cmath.pi**2)t   UVGC_192_71s6   ( 0 if MB else (complex(0,1)*G**4)/(12.*cmath.pi**2) )t   UVGC_192_72t   UVGC_192_73s*   (-19*complex(0,1)*G**4)/(512.*cmath.pi**2)t   UVGC_192_74t   UVGC_193_75s$   (complex(0,1)*G**2)/(4.*cmath.pi**2)sa   (complex(0,1)*G**2)/(3.*cmath.pi**2) - (complex(0,1)*G**2*reglog(MT**2/MU_R**2))/(4.*cmath.pi**2)t   UVGC_194_76sj   (-2*ee*complex(0,1)*G**2)/(9.*cmath.pi**2) + (ee*complex(0,1)*G**2*reglog(MT**2/MU_R**2))/(6.*cmath.pi**2)t   UVGC_195_77sb   -(complex(0,1)*G**3)/(3.*cmath.pi**2) + (complex(0,1)*G**3*reglog(MT**2/MU_R**2))/(4.*cmath.pi**2)t   UVGC_196_78s+   (complex(0,1)*G**2*gAu31)/(12.*cmath.pi**2)sm   (complex(0,1)*G**2*gAu31)/(6.*cmath.pi**2) - (complex(0,1)*G**2*gAu31*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2)t   UVGC_196_79s,   -(complex(0,1)*G**2*gAu31)/(24.*cmath.pi**2)t   UVGC_196_80t   UVGC_197_81s*   (complex(0,1)*G**2*gAu33)/(4.*cmath.pi**2)sm   (complex(0,1)*G**2*gAu33)/(3.*cmath.pi**2) - (complex(0,1)*G**2*gAu33*reglog(MT**2/MU_R**2))/(4.*cmath.pi**2)t   UVGC_198_82s,   -(complex(0,1)*G**2*gVu31)/(12.*cmath.pi**2)sn   -(complex(0,1)*G**2*gVu31)/(6.*cmath.pi**2) + (complex(0,1)*G**2*gVu31*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2)t   UVGC_198_83s+   (complex(0,1)*G**2*gVu31)/(24.*cmath.pi**2)t   UVGC_198_84t   UVGC_199_85s+   -(complex(0,1)*G**2*gVu33)/(4.*cmath.pi**2)sn   -(complex(0,1)*G**2*gVu33)/(3.*cmath.pi**2) + (complex(0,1)*G**2*gVu33*reglog(MT**2/MU_R**2))/(4.*cmath.pi**2)t   UVGC_200_86s'   (complex(0,1)*G**2*MT)/(2.*cmath.pi**2)si   (2*complex(0,1)*G**2*MT)/(3.*cmath.pi**2) - (complex(0,1)*G**2*MT*reglog(MT**2/MU_R**2))/(2.*cmath.pi**2)t   UVGC_201_87s�   ( -(ee*complex(0,1)*G**2)/(12.*cmath.pi**2*sw*cmath.sqrt(2)) if MB else (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) )s  ( (-5*ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*G**2*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2*sw*cmath.sqrt(2)) if MB else -(ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2)) ) + (ee*complex(0,1)*G**2)/(24.*cmath.pi**2*sw*cmath.sqrt(2))t   UVGC_201_88s�   -(ee*complex(0,1)*G**2)/(6.*cmath.pi**2*sw*cmath.sqrt(2)) + (ee*complex(0,1)*G**2*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2*sw*cmath.sqrt(2))t   UVGC_202_89s.   -(cw*ee*complex(0,1)*G**2)/(8.*cmath.pi**2*sw)st   -(cw*ee*complex(0,1)*G**2)/(6.*cmath.pi**2*sw) + (cw*ee*complex(0,1)*G**2*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2*sw)t   UVGC_203_90s.   (ee*complex(0,1)*G**2*sw)/(24.*cw*cmath.pi**2)su   (ee*complex(0,1)*G**2*sw)/(18.*cw*cmath.pi**2) - (ee*complex(0,1)*G**2*sw*reglog(MT**2/MU_R**2))/(24.*cw*cmath.pi**2)t   UVGC_204_91sG   ( (G**2*yb)/(12.*cmath.pi**2) if MB else -(G**2*yb)/(24.*cmath.pi**2) )s�   ( (13*G**2*yb)/(24.*cmath.pi**2) - (3*G**2*yb*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2) if MB else (G**2*yb)/(24.*cmath.pi**2) ) - (G**2*yb)/(24.*cmath.pi**2)t   UVGC_204_92s   (G**2*yb)/(12.*cmath.pi**2)sM   (G**2*yb)/(6.*cmath.pi**2) - (G**2*yb*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2)t   UVGC_204_93t   UVGC_205_94sG   ( -(G**2*yb)/(12.*cmath.pi**2) if MB else (G**2*yb)/(24.*cmath.pi**2) )s�   ( (-13*G**2*yb)/(24.*cmath.pi**2) + (3*G**2*yb*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2) if MB else -(G**2*yb)/(24.*cmath.pi**2) ) + (G**2*yb)/(24.*cmath.pi**2)t   UVGC_205_95s   -(G**2*yb)/(12.*cmath.pi**2)sN   -(G**2*yb)/(6.*cmath.pi**2) + (G**2*yb*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2)t   UVGC_205_96t   UVGC_206_97sG   ( (G**2*yt)/(12.*cmath.pi**2) if MB else -(G**2*yt)/(24.*cmath.pi**2) )s�   ( (5*G**2*yt)/(24.*cmath.pi**2) - (G**2*yt*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2) if MB else (G**2*yt)/(24.*cmath.pi**2) ) - (G**2*yt)/(24.*cmath.pi**2)t   UVGC_206_98s   (G**2*yt)/(12.*cmath.pi**2)sO   (G**2*yt)/(2.*cmath.pi**2) - (3*G**2*yt*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2)t   UVGC_206_99t   UVGC_207_100sG   ( -(G**2*yt)/(12.*cmath.pi**2) if MB else (G**2*yt)/(24.*cmath.pi**2) )s�   ( (-5*G**2*yt)/(24.*cmath.pi**2) + (G**2*yt*reglog(MB**2/MU_R**2))/(8.*cmath.pi**2) if MB else -(G**2*yt)/(24.*cmath.pi**2) ) + (G**2*yt)/(24.*cmath.pi**2)t   UVGC_207_101s   -(G**2*yt)/(12.*cmath.pi**2)sP   -(G**2*yt)/(2.*cmath.pi**2) + (3*G**2*yt*reglog(MT**2/MU_R**2))/(8.*cmath.pi**2)t   UVGC_207_102t   UVGC_208_103s(   (G**2*yt)/(2.*cmath.pi**2*cmath.sqrt(2))si   (G**2*yt*cmath.sqrt(2))/(3.*cmath.pi**2) - (G**2*yt*reglog(MT**2/MU_R**2))/(2.*cmath.pi**2*cmath.sqrt(2))t   UVGC_209_104s5   (complex(0,1)*G**2*yt)/(2.*cmath.pi**2*cmath.sqrt(2))s�   (complex(0,1)*G**2*yt*cmath.sqrt(2))/(3.*cmath.pi**2) - (complex(0,1)*G**2*yt*reglog(MT**2/MU_R**2))/(2.*cmath.pi**2*cmath.sqrt(2))N(�   t   object_libraryR    R   t   function_libraryR   R   R   R   R   R   R   R	   R   R   R   R   R   R   R   R   R   R   R   R   R   R   R   R   R    R!   R"   R#   R$   R%   R&   R'   R(   R)   R*   R+   R,   R-   R.   R/   R0   R1   R2   R3   R4   R5   R6   R7   R8   R9   R:   R;   R<   R=   R>   R?   R@   RA   RB   RC   RD   RE   RF   RG   RH   RI   RJ   RK   RL   RM   RN   RO   RP   RQ   RR   RS   RT   RU   RV   RW   RX   RY   RZ   R[   R\   R]   R^   R_   R`   Ra   Rb   Rc   Rd   Re   Rf   Rg   Rh   Ri   Rj   Rk   Rl   Rm   Rn   Ro   Rp   Rq   Rr   Rs   Rt   Ru   Rv   Rw   Rx   Ry   Rz   R{   R|   R}   R~   R   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   (    (    (    sL   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/CT_couplings.pyt   <module>   s0  :                                                                                                                                              CT_vertices.py                                                                                      0000644 0276724 0002567 00000125667 13234357560 012177  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     # This file was automatically created by FeynRules 2.4.46
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Thu 27 Oct 2016 23:02:25


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_185_96,(0,0,1):C.R2GC_185_97,(0,1,0):C.R2GC_186_98,(0,1,1):C.R2GC_186_99,(0,2,0):C.R2GC_186_98,(0,2,1):C.R2GC_186_99,(0,3,0):C.R2GC_185_96,(0,3,1):C.R2GC_185_97,(0,4,0):C.R2GC_185_96,(0,4,1):C.R2GC_185_97,(0,5,0):C.R2GC_186_98,(0,5,1):C.R2GC_186_99})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_149_78,(2,0,1):C.R2GC_149_79,(0,0,0):C.R2GC_149_78,(0,0,1):C.R2GC_149_79,(4,0,0):C.R2GC_147_74,(4,0,1):C.R2GC_147_75,(3,0,0):C.R2GC_147_74,(3,0,1):C.R2GC_147_75,(8,0,0):C.R2GC_148_76,(8,0,1):C.R2GC_148_77,(7,0,0):C.R2GC_153_84,(7,0,1):C.R2GC_190_104,(6,0,0):C.R2GC_152_83,(6,0,1):C.R2GC_191_105,(5,0,0):C.R2GC_147_74,(5,0,1):C.R2GC_147_75,(1,0,0):C.R2GC_147_74,(1,0,1):C.R2GC_147_75,(11,0,0):C.R2GC_151_81,(11,0,1):C.R2GC_151_82,(10,0,0):C.R2GC_151_81,(10,0,1):C.R2GC_151_82,(9,0,1):C.R2GC_150_80,(2,1,0):C.R2GC_149_78,(2,1,1):C.R2GC_149_79,(0,1,0):C.R2GC_149_78,(0,1,1):C.R2GC_149_79,(6,1,0):C.R2GC_187_100,(6,1,1):C.R2GC_187_101,(4,1,0):C.R2GC_147_74,(4,1,1):C.R2GC_147_75,(3,1,0):C.R2GC_147_74,(3,1,1):C.R2GC_147_75,(8,1,0):C.R2GC_148_76,(8,1,1):C.R2GC_190_104,(7,1,0):C.R2GC_153_84,(7,1,1):C.R2GC_148_77,(5,1,0):C.R2GC_147_74,(5,1,1):C.R2GC_147_75,(1,1,0):C.R2GC_147_74,(1,1,1):C.R2GC_147_75,(11,1,0):C.R2GC_151_81,(11,1,1):C.R2GC_151_82,(10,1,0):C.R2GC_151_81,(10,1,1):C.R2GC_151_82,(9,1,1):C.R2GC_150_80,(2,2,0):C.R2GC_149_78,(2,2,1):C.R2GC_149_79,(0,2,0):C.R2GC_149_78,(0,2,1):C.R2GC_149_79,(4,2,0):C.R2GC_147_74,(4,2,1):C.R2GC_147_75,(3,2,0):C.R2GC_147_74,(3,2,1):C.R2GC_147_75,(8,2,0):C.R2GC_148_76,(8,2,1):C.R2GC_188_103,(6,2,0):C.R2GC_152_83,(7,2,0):C.R2GC_188_102,(7,2,1):C.R2GC_188_103,(5,2,0):C.R2GC_147_74,(5,2,1):C.R2GC_147_75,(1,2,0):C.R2GC_147_74,(1,2,1):C.R2GC_147_75,(11,2,0):C.R2GC_151_81,(11,2,1):C.R2GC_151_82,(10,2,0):C.R2GC_151_81,(10,2,1):C.R2GC_151_82,(9,2,1):C.R2GC_150_80})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_205_112,(0,1,0):C.R2GC_206_113})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_183_95})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_182_94})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_207_114,(0,1,0):C.R2GC_204_111})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_208_115})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_209_116})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV6, L.FFV7 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_176_90,(0,1,0):C.R2GC_178_92})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.d__tilde__, P.b, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.b, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_175_89,(0,1,0):C.R2GC_177_91})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_101_2})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.b__tilde__, P.d, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.b, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_175_89,(0,1,0):C.R2GC_177_91})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_105_6,(0,1,0):C.R2GC_106_7})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_110_9,(0,1,0):C.R2GC_111_10})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_197_107,(0,1,0):C.R2GC_199_109})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.u__tilde__, P.t, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.g, P.t, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_196_106,(0,1,0):C.R2GC_198_108})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.t__tilde__, P.u, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.g, P.t, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_196_106,(0,1,0):C.R2GC_198_108})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_115_11,(0,1,0):C.R2GC_116_12})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_156_87})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_156_87})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_156_87})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_154_85})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_154_85})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_154_85})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_155_86})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_155_86})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_155_86})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_155_86})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_155_86})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_155_86})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_170_88})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_170_88})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_170_88})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_170_88})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_170_88})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_170_88})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_102_3,(0,1,0):C.R2GC_103_4})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_102_3,(0,1,0):C.R2GC_103_4})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_102_3,(0,1,0):C.R2GC_103_4})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_107_8,(0,1,0):C.R2GC_103_4})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_107_8,(0,1,0):C.R2GC_103_4})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_107_8,(0,1,0):C.R2GC_103_4})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_200_110,(0,1,0):C.R2GC_104_5})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_104_5})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_179_93,(0,1,0):C.R2GC_104_5})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV2, L.VV3, L.VV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,2,2):C.R2GC_98_117,(0,0,0):C.R2GC_119_13,(0,0,3):C.R2GC_119_14,(0,1,1):C.R2GC_122_19})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.g, P.g, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVV2 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_125_24,(0,0,1):C.R2GC_125_25,(0,0,2):C.R2GC_125_26,(0,0,3):C.R2GC_125_27,(0,0,4):C.R2GC_125_28,(0,0,5):C.R2GC_125_29})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.g, P.g, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVV1 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_129_48,(0,0,1):C.R2GC_129_49})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_120_15,(0,0,1):C.R2GC_120_16})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.g, P.g, P.Y1, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.d] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.t, P.u] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_137_66,(0,0,2):C.R2GC_137_67,(0,0,3):C.R2GC_137_68,(0,0,4):C.R2GC_137_69,(0,0,5):C.R2GC_137_70,(0,0,7):C.R2GC_137_71,(0,0,1):C.R2GC_137_72,(0,0,6):C.R2GC_137_73})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Y1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_127_36,(0,0,1):C.R2GC_127_37,(0,0,2):C.R2GC_127_38,(0,0,3):C.R2GC_127_39,(0,0,4):C.R2GC_127_40,(0,0,5):C.R2GC_127_41})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.g, P.g, P.Y1, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_133_56,(0,0,1):C.R2GC_133_57,(0,0,2):C.R2GC_133_58,(0,0,3):C.R2GC_133_59,(0,0,4):C.R2GC_133_60,(0,0,5):C.R2GC_133_61})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Y1 ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV7 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_126_30,(1,0,1):C.R2GC_126_31,(1,0,2):C.R2GC_126_32,(1,0,3):C.R2GC_126_33,(1,0,4):C.R2GC_126_34,(1,0,5):C.R2GC_126_35,(0,1,0):C.R2GC_128_42,(0,1,1):C.R2GC_128_43,(0,1,2):C.R2GC_128_44,(0,1,3):C.R2GC_128_45,(0,1,4):C.R2GC_128_46,(0,1,5):C.R2GC_128_47})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_136_65})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_130_50,(0,0,1):C.R2GC_130_51})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_134_62,(0,0,1):C.R2GC_134_63})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_123_20,(0,0,1):C.R2GC_123_21})

V_61 = CTVertex(name = 'V_61',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_132_54,(1,0,1):C.R2GC_132_55,(0,1,0):C.R2GC_131_52,(0,1,1):C.R2GC_131_53})

V_62 = CTVertex(name = 'V_62',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV7 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_124_22,(0,0,1):C.R2GC_124_23})

V_63 = CTVertex(name = 'V_63',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_121_17,(0,0,1):C.R2GC_121_18})

V_64 = CTVertex(name = 'V_64',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_121_17,(0,0,1):C.R2GC_121_18})

V_65 = CTVertex(name = 'V_65',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_135_64})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_185_44,(0,0,1):C.UVGC_185_45,(0,0,2):C.UVGC_185_46,(0,0,3):C.UVGC_185_47,(0,0,4):C.UVGC_185_48,(0,1,0):C.UVGC_186_49,(0,1,1):C.UVGC_186_50,(0,1,2):C.UVGC_186_51,(0,1,3):C.UVGC_186_52,(0,1,4):C.UVGC_186_53,(0,2,0):C.UVGC_186_49,(0,2,1):C.UVGC_186_50,(0,2,2):C.UVGC_186_51,(0,2,3):C.UVGC_186_52,(0,2,4):C.UVGC_186_53,(0,3,0):C.UVGC_185_44,(0,3,1):C.UVGC_185_45,(0,3,2):C.UVGC_185_46,(0,3,3):C.UVGC_185_47,(0,3,4):C.UVGC_185_48,(0,4,0):C.UVGC_185_44,(0,4,1):C.UVGC_185_45,(0,4,2):C.UVGC_185_46,(0,4,3):C.UVGC_185_47,(0,4,4):C.UVGC_185_48,(0,5,0):C.UVGC_186_49,(0,5,1):C.UVGC_186_50,(0,5,2):C.UVGC_186_51,(0,5,3):C.UVGC_186_52,(0,5,4):C.UVGC_186_53})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,3):C.UVGC_148_9,(2,0,4):C.UVGC_148_8,(0,0,3):C.UVGC_148_9,(0,0,4):C.UVGC_148_8,(4,0,3):C.UVGC_147_6,(4,0,4):C.UVGC_147_7,(3,0,3):C.UVGC_147_6,(3,0,4):C.UVGC_147_7,(8,0,3):C.UVGC_148_8,(8,0,4):C.UVGC_148_9,(7,0,0):C.UVGC_190_64,(7,0,2):C.UVGC_190_65,(7,0,3):C.UVGC_190_66,(7,0,4):C.UVGC_190_67,(7,0,5):C.UVGC_190_68,(6,0,0):C.UVGC_190_64,(6,0,2):C.UVGC_190_65,(6,0,3):C.UVGC_191_69,(6,0,4):C.UVGC_191_70,(6,0,5):C.UVGC_190_68,(5,0,3):C.UVGC_147_6,(5,0,4):C.UVGC_147_7,(1,0,3):C.UVGC_147_6,(1,0,4):C.UVGC_147_7,(11,0,3):C.UVGC_151_12,(11,0,4):C.UVGC_151_13,(10,0,3):C.UVGC_151_12,(10,0,4):C.UVGC_151_13,(9,0,3):C.UVGC_150_10,(9,0,4):C.UVGC_150_11,(2,1,3):C.UVGC_148_9,(2,1,4):C.UVGC_148_8,(0,1,3):C.UVGC_148_9,(0,1,4):C.UVGC_148_8,(6,1,0):C.UVGC_187_54,(6,1,3):C.UVGC_187_55,(6,1,4):C.UVGC_187_56,(6,1,5):C.UVGC_187_57,(4,1,3):C.UVGC_147_6,(4,1,4):C.UVGC_147_7,(3,1,3):C.UVGC_147_6,(3,1,4):C.UVGC_147_7,(8,1,0):C.UVGC_192_71,(8,1,2):C.UVGC_192_72,(8,1,3):C.UVGC_190_66,(8,1,4):C.UVGC_192_73,(8,1,5):C.UVGC_192_74,(7,1,1):C.UVGC_152_14,(7,1,3):C.UVGC_148_8,(7,1,4):C.UVGC_153_15,(5,1,3):C.UVGC_147_6,(5,1,4):C.UVGC_147_7,(1,1,3):C.UVGC_147_6,(1,1,4):C.UVGC_147_7,(11,1,3):C.UVGC_151_12,(11,1,4):C.UVGC_151_13,(10,1,3):C.UVGC_151_12,(10,1,4):C.UVGC_151_13,(9,1,3):C.UVGC_150_10,(9,1,4):C.UVGC_150_11,(2,2,3):C.UVGC_148_9,(2,2,4):C.UVGC_148_8,(0,2,3):C.UVGC_148_9,(0,2,4):C.UVGC_148_8,(4,2,3):C.UVGC_147_6,(4,2,4):C.UVGC_147_7,(3,2,3):C.UVGC_147_6,(3,2,4):C.UVGC_147_7,(8,2,0):C.UVGC_189_60,(8,2,2):C.UVGC_189_61,(8,2,3):C.UVGC_188_58,(8,2,4):C.UVGC_189_62,(8,2,5):C.UVGC_189_63,(6,2,1):C.UVGC_152_14,(6,2,4):C.UVGC_150_10,(7,2,0):C.UVGC_187_54,(7,2,3):C.UVGC_188_58,(7,2,4):C.UVGC_188_59,(7,2,5):C.UVGC_187_57,(5,2,3):C.UVGC_147_6,(5,2,4):C.UVGC_147_7,(1,2,3):C.UVGC_147_6,(1,2,4):C.UVGC_147_7,(11,2,3):C.UVGC_151_12,(11,2,4):C.UVGC_151_13,(10,2,3):C.UVGC_151_12,(10,2,4):C.UVGC_151_13,(9,2,3):C.UVGC_150_10,(9,2,4):C.UVGC_150_11})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_205_94,(0,0,2):C.UVGC_205_95,(0,0,1):C.UVGC_205_96,(0,1,0):C.UVGC_206_97,(0,1,2):C.UVGC_206_98,(0,1,1):C.UVGC_206_99})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_183_41})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_182_40})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_207_100,(0,0,2):C.UVGC_207_101,(0,0,1):C.UVGC_207_102,(0,1,0):C.UVGC_204_91,(0,1,2):C.UVGC_204_92,(0,1,1):C.UVGC_204_93})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_208_103})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_209_104})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_176_32,(0,1,0):C.UVGC_178_36})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.d__tilde__, P.b, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.b, P.d, P.g] ], [ [P.b, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_175_29,(0,0,2):C.UVGC_175_30,(0,0,0):C.UVGC_175_31,(0,1,1):C.UVGC_177_33,(0,1,2):C.UVGC_177_34,(0,1,0):C.UVGC_177_35})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.b__tilde__, P.d, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.b, P.d, P.g] ], [ [P.b, P.g] ], [ [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_175_29,(0,0,2):C.UVGC_175_30,(0,0,0):C.UVGC_175_31,(0,1,1):C.UVGC_177_33,(0,1,2):C.UVGC_177_34,(0,1,0):C.UVGC_177_35})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_197_81,(0,1,0):C.UVGC_199_85})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.u__tilde__, P.t, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_196_78,(0,0,2):C.UVGC_196_79,(0,0,1):C.UVGC_196_80,(0,1,0):C.UVGC_198_82,(0,1,2):C.UVGC_198_83,(0,1,1):C.UVGC_198_84})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.t__tilde__, P.u, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV6, L.FFV7 ],
                loop_particles = [ [ [P.g, P.t] ], [ [P.g, P.t, P.u] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_196_78,(0,0,2):C.UVGC_196_79,(0,0,1):C.UVGC_196_80,(0,1,0):C.UVGC_198_82,(0,1,2):C.UVGC_198_83,(0,1,1):C.UVGC_198_84})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_156_18,(0,1,0):C.UVGC_139_2,(0,2,0):C.UVGC_139_2})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_156_18,(0,1,0):C.UVGC_139_2,(0,2,0):C.UVGC_139_2})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_156_18,(0,1,0):C.UVGC_194_76,(0,2,0):C.UVGC_194_76})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_154_16,(0,1,0):C.UVGC_141_3,(0,2,0):C.UVGC_141_3})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_154_16,(0,1,0):C.UVGC_141_3,(0,2,0):C.UVGC_141_3})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_154_16,(0,1,0):C.UVGC_173_27,(0,2,0):C.UVGC_173_27})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ] ],
                couplings = {(0,0,4):C.UVGC_155_17,(0,1,0):C.UVGC_157_19,(0,1,1):C.UVGC_157_20,(0,1,2):C.UVGC_157_21,(0,1,3):C.UVGC_157_22,(0,1,4):C.UVGC_157_23,(0,2,0):C.UVGC_157_19,(0,2,1):C.UVGC_157_20,(0,2,2):C.UVGC_157_21,(0,2,3):C.UVGC_157_22,(0,2,4):C.UVGC_157_23})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ] ],
                couplings = {(0,0,2):C.UVGC_155_17,(0,1,0):C.UVGC_157_19,(0,1,1):C.UVGC_157_20,(0,1,3):C.UVGC_157_21,(0,1,4):C.UVGC_157_22,(0,1,2):C.UVGC_157_23,(0,2,0):C.UVGC_157_19,(0,2,1):C.UVGC_157_20,(0,2,3):C.UVGC_157_21,(0,2,4):C.UVGC_157_22,(0,2,2):C.UVGC_157_23})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,4):C.UVGC_155_17,(0,1,0):C.UVGC_157_19,(0,1,1):C.UVGC_157_20,(0,1,2):C.UVGC_157_21,(0,1,3):C.UVGC_157_22,(0,1,4):C.UVGC_195_77,(0,2,0):C.UVGC_157_19,(0,2,1):C.UVGC_157_20,(0,2,2):C.UVGC_157_21,(0,2,3):C.UVGC_157_22,(0,2,4):C.UVGC_195_77})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ] ],
                couplings = {(0,0,2):C.UVGC_155_17,(0,1,0):C.UVGC_157_19,(0,1,1):C.UVGC_157_20,(0,1,3):C.UVGC_157_21,(0,1,4):C.UVGC_157_22,(0,1,2):C.UVGC_157_23,(0,2,0):C.UVGC_157_19,(0,2,1):C.UVGC_157_20,(0,2,3):C.UVGC_157_21,(0,2,4):C.UVGC_157_22,(0,2,2):C.UVGC_157_23})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ] ],
                couplings = {(0,0,4):C.UVGC_155_17,(0,1,0):C.UVGC_157_19,(0,1,1):C.UVGC_157_20,(0,1,2):C.UVGC_157_21,(0,1,3):C.UVGC_157_22,(0,1,4):C.UVGC_157_23,(0,2,0):C.UVGC_157_19,(0,2,1):C.UVGC_157_20,(0,2,2):C.UVGC_157_21,(0,2,3):C.UVGC_157_22,(0,2,4):C.UVGC_157_23})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ] ],
                couplings = {(0,0,1):C.UVGC_155_17,(0,1,0):C.UVGC_157_19,(0,1,2):C.UVGC_157_20,(0,1,3):C.UVGC_157_21,(0,1,4):C.UVGC_157_22,(0,1,1):C.UVGC_174_28,(0,2,0):C.UVGC_157_19,(0,2,2):C.UVGC_157_20,(0,2,3):C.UVGC_157_21,(0,2,4):C.UVGC_157_22,(0,2,1):C.UVGC_174_28})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_170_24,(0,0,1):C.UVGC_170_25})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_170_24,(0,0,1):C.UVGC_170_25})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_201_87,(0,0,2):C.UVGC_201_88,(0,0,1):C.UVGC_170_25})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_170_24,(0,0,1):C.UVGC_170_25})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_170_24,(0,0,1):C.UVGC_170_25})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_201_87,(0,0,2):C.UVGC_201_88,(0,0,1):C.UVGC_170_25})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_202_89,(0,1,0):C.UVGC_203_90})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_180_38,(0,1,0):C.UVGC_181_39})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.u__tilde__, P.u ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.u] ] ],
                 couplings = {(0,0,0):C.UVGC_138_1})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.c__tilde__, P.c ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.c, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_138_1})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.t__tilde__, P.t ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.g, P.t] ] ],
                 couplings = {(0,0,0):C.UVGC_200_86,(0,1,0):C.UVGC_193_75})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.d__tilde__, P.d ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.d, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_138_1})

V_104 = CTVertex(name = 'V_104',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF4 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_138_1})

V_105 = CTVertex(name = 'V_105',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_179_37,(0,1,0):C.UVGC_172_26})

V_106 = CTVertex(name = 'V_106',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV5 ],
                 loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                 couplings = {(0,1,0):C.UVGC_184_42,(0,1,3):C.UVGC_184_43,(0,0,1):C.UVGC_146_4,(0,0,2):C.UVGC_146_5})

                                                                         CT_vertices.pyo                                                                                     0000644 0276724 0002567 00000072510 13234357560 012342  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc           @   s%V  d  d l  m Z m Z m Z m Z d  d l Z d  d l Z d  d l	 Z
 e d d d d d e j e j e j g d d	 g d
 e
 j e
 j e
 j e
 j e
 j e
 j g d e j g e j g e j g e j g e j g e j g g e j g g g d i e j d d d f 6e j d d d f 6e j d d d f 6e j d d d f 6e j d d d f 6e j d d d f 6e j d d d f 6e j d d d f 6e j d d d f 6e j d d d f 6e j d d d f 6e j d d d f 6� Z e d d d d d e j e j e j e j g d d d d d d d d d d d d d g d
 e
 j e
 j e
 j g d e j g e j g e j g e j g e j g e j g g e j g g g d iD e j  d d d f 6e j! d d d f 6e j  d d d f 6e j! d d d f 6e j" d d d f 6e j# d d d f 6e j" d d d f 6e j# d d d f 6e j$ d  d d f 6e j% d  d d f 6e j& d! d d f 6e j' d! d d f 6e j( d" d d f 6e j) d" d d f 6e j" d d d f 6e j# d d d f 6e j" d d d f 6e j# d d d f 6e j* d# d d f 6e j+ d# d d f 6e j* d$ d d f 6e j+ d$ d d f 6e j, d% d d f 6e j  d d d f 6e j! d d d f 6e j  d d d f 6e j! d d d f 6e j- d" d d f 6e j. d" d d f 6e j" d d d f 6e j# d d d f 6e j" d d d f 6e j# d d d f 6e j$ d  d d f 6e j' d  d d f 6e j& d! d d f 6e j% d! d d f 6e j" d d d f 6e j# d d d f 6e j" d d d f 6e j# d d d f 6e j* d# d d f 6e j+ d# d d f 6e j* d$ d d f 6e j+ d$ d d f 6e j, d% d d f 6e j  d d d f 6e j! d d d f 6e j  d d d f 6e j! d d d f 6e j" d d d f 6e j# d d d f 6e j" d d d f 6e j# d d d f 6e j$ d  d d f 6e j/ d  d d f 6e j( d" d d f 6e j0 d! d d f 6e j/ d! d d f 6e j" d d d f 6e j# d d d f 6e j" d d d f 6e j# d d d f 6e j* d# d d f 6e j+ d# d d f 6e j* d$ d d f 6e j+ d$ d d f 6e j, d% d d f 6� Z1 e d d& d d d e j2 e j e j3 g d d' g d
 e
 j4 e
 j5 g d e j e j e j g g g d i e j6 d d d f 6e j7 d d d f 6� Z8 e d d( d d d e j9 e j e j: g d d' g d
 e
 j; g d e j e j g g g d i e j< d d d f 6� Z= e d d) d d d e j9 e j e j> g d d' g d
 e
 j? g d e j e j g g g d i e j@ d d d f 6� ZA e d d* d d d e j9 e j e jB g d d' g d
 e
 j4 e
 j5 g d e j e j e j g g g d i e jC d d d f 6e jD d d d f 6� ZE e d d+ d d d e j2 e j e j: g d d' g d
 e
 j; g d e j e j g g g d i e jF d d d f 6� ZG e d d, d d d e j2 e j e j> g d d' g d
 e
 j? g d e j e j g g g d i e jH d d d f 6� ZI e d d- d d d e j9 e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j g g g d i e jM d d d f 6e jN d d d f 6� ZO e d d. d d d e jP e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j e j g g g d i e jQ d d d f 6e jR d d d f 6� ZS e d d/ d d d e jT e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j g g g d i e jU d d d f 6e jV d d d f 6� ZW e d d0 d d d e j9 e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j e j g g g d i e jQ d d d f 6e jR d d d f 6� ZX e d d1 d d d e jP e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j g g g d i e jY d d d f 6e jZ d d d f 6� Z[ e d d2 d d d e j\ e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j g g g d i e j] d d d f 6e j^ d d d f 6� Z_ e d d3 d d d e j2 e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j g g g d i e j` d d d f 6e ja d d d f 6� Zb e d d4 d d d e jc e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j e j g g g d i e jd d d d f 6e je d d d f 6� Zf e d d5 d d d e j2 e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j e j g g g d i e jd d d d f 6e je d d d f 6� Zg e d d6 d d d e jc e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j g g g d i e jh d d d f 6e ji d d d f 6� Zj e d d7 d d d e jc e j e jk g d d' g d
 e
 jl g d e j e j g g g d i e jm d d d f 6� Zn e d d8 d d d e jT e j e jk g d d' g d
 e
 jl g d e j e j g g g d i e jm d d d f 6� Zo e d d9 d d d e j2 e j e jk g d d' g d
 e
 jl g d e j e j g g g d i e jm d d d f 6� Zp e d d: d d d e jP e j e jk g d d' g d
 e
 jl g d e j e j g g g d i e jq d d d f 6� Zr e d d; d d d e j\ e j e jk g d d' g d
 e
 jl g d e j e j g g g d i e jq d d d f 6� Zs e d d< d d d e j9 e j e jk g d d' g d
 e
 jl g d e j e j g g g d i e jq d d d f 6� Zt e d d= d d d e jc e j e j g d d> g d
 e
 jl g d e j e j g g g d i e ju d d d f 6� Zv e d d? d d d e jT e j e j g d d> g d
 e
 jl g d e j e j g g g d i e ju d d d f 6� Zw e d d@ d d d e j2 e j e j g d d> g d
 e
 jl g d e j e j g g g d i e ju d d d f 6� Zx e d dA d d d e jP e j e j g d d> g d
 e
 jl g d e j e j g g g d i e ju d d d f 6� Zy e d dB d d d e j\ e j e j g d d> g d
 e
 jl g d e j e j g g g d i e ju d d d f 6� Zz e d dC d d d e j9 e j e j g d d> g d
 e
 jl g d e j e j g g g d i e ju d d d f 6� Z{ e d dD d d d e jP e j e j| g d d' g d
 e
 j} g d e j e j e j g g g d i e j~ d d d f 6� Z e d dE d d d e j\ e j e j| g d d' g d
 e
 j} g d e j e j e j g g g d i e j~ d d d f 6� Z� e d dF d d d e j9 e j e j| g d d' g d
 e
 j} g d e j e j e j g g g d i e j~ d d d f 6� Z� e d dG d d d e jc e j e j� g d d' g d
 e
 j} g d e j e j e j g g g d i e j~ d d d f 6� Z� e d dH d d d e jT e j e j� g d d' g d
 e
 j} g d e j e j e j g g g d i e j~ d d d f 6� Z� e d dI d d d e j2 e j e j� g d d' g d
 e
 j} g d e j e j e j g g g d i e j~ d d d f 6� Z� e d dJ d d d e jc e j e j� g d d' g d
 e
 j} e
 j� g d e j e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d dK d d d e jT e j e j� g d d' g d
 e
 j} e
 j� g d e j e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d dL d d d e j2 e j e j� g d d' g d
 e
 j} e
 j� g d e j e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d dM d d d e jP e j e j� g d d' g d
 e
 j} e
 j� g d e j e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d dN d d d e j\ e j e j� g d d' g d
 e
 j} e
 j� g d e j e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d dO d d d e j9 e j e j� g d d' g d
 e
 j} e
 j� g d e j e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d dP d d d e jc e j g d d' g d
 e
 j� g d e j e j g g g d i e j� d d d f 6� Z� e d dQ d d d e jT e j g d d' g d
 e
 j� g d e j e j g g g d i e j� d d d f 6� Z� e d dR d d d e j2 e j g d d' g d
 e
 j� e
 j� g d e j e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d dS d d d e jP e j g d d' g d
 e
 j� g d e j e j g g g d i e j� d d d f 6� Z� e d dT d d d e j\ e j g d d' g d
 e
 j� g d e j e j g g g d i e j� d d d f 6� Z� e d dU d d d e j9 e j g d d' g d
 e
 j� e
 j� g d e j e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d dV d d d e j e j g d d' g d
 e
 j� e
 j� e
 j� g d e j g g e j g e j g e j g e j g e j g e j g g e j g g e j g g g d i e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6� Z� e d dW d d d e j e j e jJ g d d' g d
 e
 j� g d e j g g e j g g e j g g e j g g e j g g e j g g g d i e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6� Z� e d dX d d d e j e j e j� g d d' g d
 e
 j� g d e j g e j g e j g g e j g e j g e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d dY d d d e j e j e j> g d d' g d
 e
 j� g d e j g g e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d dZ d d d e j e j e jJ e jJ g d d' g d
 e
 j� g d e j g g e j e j g g e j g g e j g g e j g g e j g g e j e j g g e j g g g d i e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d! f 6e j� d d d f 6e j� d d d" f 6� Z� e d d[ d d d e jk e j e j e jJ g d d\ g d
 e
 j� g d e j g g e j g g e j g g e j g g e j g g e j g g g d i e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6� Z� e d d] d d d e j e j e jJ e j� g d d' g d
 e
 j� g d e j g g e j g g e j g g e j g g e j g g e j g g g d i e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6� Z� e d d^ d d d e j e j e j e jJ g d d_ d	 g d
 e
 j� e
 j� g d e j g g e j g g e j g g e j g g e j g g e j g g g d i e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6� Z� e d d` d d d e j e j e j| e j� g d d' g d
 e
 j� g d e j e j g e j e j g e j e j g g g d i e j� d d d f 6� Z� e d da d d d e jk e j e j e j� g d d\ g d
 e
 j� g d e j g e j g e j g g e j g e j g e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d db d d d e j e j e j� e j� g d d' g d
 e
 j� g d e j g e j g e j g g e j g e j g e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d dc d d d e jk e jk e j e j g d dd g d
 e
 j� g d e j g e j g e j g g e j g e j g e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d de d d d e j e j e j e j� g d d_ d	 g d
 e
 j� e
 j� g d e j g e j g e j g g e j g e j g e j g g g d i e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6� Z� e d df d d d e jk e j e j e j g d dg g d
 e
 j� g d e j g e j g e j g g e j g e j g e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d dh d d d e j e j e j> e j> g d d' g d
 e
 j� g d e j g g e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d di d d d e j e j e j: e j: g d d' g d
 e
 j� g d e j g g e j g g g d i e j� d d d f 6e j� d d d f 6� Z� e d dj d d d e j e j e jB e j3 g d d' g d
 e
 j� g d e j e j g g g d i e j� d d d f 6� Z� e d dk d dl d e j e j e j g d d	 g d
 e
 j e
 j e
 j e
 j e
 j e
 j g d e j g g e j g e j g e j g e j g g e j g g e j� g g e j g g g d i e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j� d d d f 6e j d d d f 6� Ze d dm d dl d e j e j e j e j g d d d d d d d d d d d d d g d
 e
 j e
 j e
 j g d e j g g e j g e j g e j g e j g e j g e j g g e j g e j g e j g e j g g e j g g e j� g g e j g g g d iY e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd  d d f 6e jd  d d f 6e jd! d d f 6e jd! d d f 6e jd! d d f 6e j	d! d d f 6e j
d! d d f 6e jd" d d f 6e jd" d d f 6e jd" d d f 6e jd" d d f 6e j
d" d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd# d d f 6e jd# d d f 6e jd$ d d f 6e jd$ d d f 6e jd% d d f 6e jd% d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd" d d f 6e jd" d d f 6e jd" d d f 6e jd" d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd  d d f 6e jd  d d f 6e jd  d d f 6e jd  d d f 6e jd  d d f 6e jd! d d f 6e jd! d d f 6e jd! d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd# d d f 6e jd# d d f 6e jd$ d d f 6e jd$ d d f 6e jd% d d f 6e jd% d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd  d d f 6e jd  d d f 6e jd  d d f 6e jd  d d f 6e jd  d d f 6e jd" d d f 6e jd" d d f 6e jd! d d f 6e jd! d d f 6e j d! d d f 6e jd! d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd d d f 6e jd# d d f 6e jd# d d f 6e jd$ d d f 6e jd$ d d f 6e jd% d d f 6e jd% d d f 6� Z!e d dn d dl d e j2 e j e j3 g d d' g d
 e
 j4 e
 j5 g d e j e j g g e j e j e j g g e j e j g g g d i e j"d d d f 6e j#d d d f 6e j$d d d f 6e j%d d d f 6e j&d d d f 6e j'd d d f 6� Z(e d do d dl d e j9 e j e j: g d d' g d
 e
 j; g d e j e j g g g d i e j)d d d f 6� Z*e d dp d dl d e j9 e j e j> g d d' g d
 e
 j? g d e j e j g g g d i e j+d d d f 6� Z,e d dq d dl d e j9 e j e jB g d d' g d
 e
 j4 e
 j5 g d e j e j g g e j e j e j g g e j e j g g g d i e j-d d d f 6e j.d d d f 6e j/d d d f 6e j0d d d f 6e j1d d d f 6e j2d d d f 6� Z3e d dr d dl d e j2 e j e j: g d d' g d
 e
 j; g d e j e j g g g d i e j4d d d f 6� Z5e d ds d dl d e j2 e j e j> g d d' g d
 e
 j? g d e j e j g g g d i e j6d d d f 6� Z7e d dt d dl d e j9 e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j g g g d i e j8d d d f 6e j9d d d f 6� Z:e d du d dl d e jP e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j e j g g e j e j g g e j e j g g g d i e j;d d d f 6e j<d d d f 6e j=d d d f 6e j>d d d f 6e j?d d d f 6e j@d d d f 6� ZAe d dv d dl d e j9 e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j e j g g e j e j g g e j e j g g g d i e j;d d d f 6e j<d d d f 6e j=d d d f 6e j>d d d f 6e j?d d d f 6e j@d d d f 6� ZBe d dw d dl d e j2 e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j g g g d i e jCd d d f 6e jDd d d f 6� ZEe d dx d dl d e jc e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j g g e j e j e j g g e j e j g g g d i e jFd d d f 6e jGd d d f 6e jHd d d f 6e jId d d f 6e jJd d d f 6e jKd d d f 6� ZLe d dy d dl d e j2 e j e jJ g d d' g d
 e
 jK e
 jL g d e j e j g g e j e j e j g g e j e j g g g d i e jFd d d f 6e jGd d d f 6e jHd d d f 6e jId d d f 6e jJd d d f 6e jKd d d f 6� ZMe d dz d dl d e jc e j e jk g d d' g d
 e
 jl e
 j} e
 jNg d e j e j g g g d i e jOd d d f 6e jPd d d f 6e jPd d d f 6� ZQe d d{ d dl d e jT e j e jk g d d' g d
 e
 jl e
 j} e
 jNg d e j e j g g g d i e jOd d d f 6e jPd d d f 6e jPd d d f 6� ZRe d d| d dl d e j2 e j e jk g d d' g d
 e
 jl e
 j} e
 jNg d e j e j g g g d i e jOd d d f 6e jSd d d f 6e jSd d d f 6� ZTe d d} d dl d e jP e j e jk g d d' g d
 e
 jl e
 j} e
 jNg d e j e j g g g d i e jUd d d f 6e jVd d d f 6e jVd d d f 6� ZWe d d~ d dl d e j\ e j e jk g d d' g d
 e
 jl e
 j} e
 jNg d e j e j g g g d i e jUd d d f 6e jVd d d f 6e jVd d d f 6� ZXe d d d dl d e j9 e j e jk g d d' g d
 e
 jl e
 j} e
 jNg d e j e j g g g d i e jUd d d f 6e jYd d d f 6e jYd d d f 6� ZZe d d� d dl d e jc e j e j g d d> g d
 e
 jl e
 j} e
 jNg d e j g g e j g e j g e j g e j g g e j g g e j� g g e j e j g g g d i e j[d d d f 6e j\d d d f 6e j]d d d f 6e j^d d d f 6e j_d d d f 6e j`d d d f 6e j\d d d f 6e j]d d d f 6e j^d d d f 6e j_d d d f 6e j`d d d f 6� Zae d d� d dl d e jT e j e j g d d> g d
 e
 jl e
 j} e
 jNg d e j g g e j g e j g e j g e j g g e j e j g g e j g g e j� g g g d i e j[d d d f 6e j\d d d f 6e j]d d d f 6e j^d d d f 6e j_d d d f 6e j`d d d f 6e j\d d d f 6e j]d d d f 6e j^d d d f 6e j_d d d f 6e j`d d d f 6� Zbe d d� d dl d e j2 e j e j g d d> g d
 e
 jl e
 j} e
 jNg d e j g g e j g e j g e j g e j g g e j g g e j� g g e j e j g g g d i e j[d d d f 6e j\d d d f 6e j]d d d f 6e j^d d d f 6e j_d d d f 6e jcd d d f 6e j\d d d f 6e j]d d d f 6e j^d d d f 6e j_d d d f 6e jcd d d f 6� Zde d d� d dl d e jP e j e j g d d> g d
 e
 jl e
 j} e
 jNg d e j g g e j g e j g e j g e j g g e j e j g g e j g g e j� g g g d i e j[d d d f 6e j\d d d f 6e j]d d d f 6e j^d d d f 6e j_d d d f 6e j`d d d f 6e j\d d d f 6e j]d d d f 6e j^d d d f 6e j_d d d f 6e j`d d d f 6� Zee d d� d dl d e j\ e j e j g d d> g d
 e
 jl e
 j} e
 jNg d e j g g e j g e j g e j g e j g g e j g g e j� g g e j e j g g g d i e j[d d d f 6e j\d d d f 6e j]d d d f 6e j^d d d f 6e j_d d d f 6e j`d d d f 6e j\d d d f 6e j]d d d f 6e j^d d d f 6e j_d d d f 6e j`d d d f 6� Zfe d d� d dl d e j9 e j e j g d d> g d
 e
 jl e
 j} e
 jNg d e j g g e j e j g g e j g e j g e j g e j g g e j g g e j� g g g d i e j[d d d f 6e j\d d d f 6e j]d d d f 6e j^d d d f 6e j_d d d f 6e jgd d d f 6e j\d d d f 6e j]d d d f 6e j^d d d f 6e j_d d d f 6e jgd d d f 6� Zhe d d� d dl d e jP e j e j| g d d' g d
 e
 j} g d e j e j g e j e j g g e j e j e j g g g d i e jid d d f 6e jjd d d f 6� Zke d d� d dl d e j\ e j e j| g d d' g d
 e
 j} g d e j e j g e j e j g g e j e j e j g g g d i e jid d d f 6e jjd d d f 6� Zle d d� d dl d e j9 e j e j| g d d' g d
 e
 j} g d e j e j g g e j e j e j g g e j e j g g g d i e jmd d d f 6e jnd d d f 6e jjd d d f 6� Zoe d d� d dl d e jc e j e j� g d d' g d
 e
 j} g d e j e j g e j e j g g e j e j e j g g g d i e jid d d f 6e jjd d d f 6� Zpe d d� d dl d e jT e j e j� g d d' g d
 e
 j} g d e j e j g e j e j g g e j e j e j g g g d i e jid d d f 6e jjd d d f 6� Zqe d d� d dl d e j2 e j e j� g d d' g d
 e
 j} g d e j e j g g e j e j e j g g e j e j g g g d i e jmd d d f 6e jnd d d f 6e jjd d d f 6� Zre d d� d dl d e j2 e j e j� g d d' g d
 e
 j} e
 j� g d e j e j g g g d i e jsd d d f 6e jtd d d f 6� Zue d d� d dl d e j9 e j e j� g d d' g d
 e
 j} e
 j� g d e j e j g g g d i e jvd d d f 6e jwd d d f 6� Zxe d d� d dl d e jc e j g d d' g d
 e
 jyg d e j e j g g g d i e jzd d d f 6� Z{e d d� d dl d e jT e j g d d' g d
 e
 jyg d e j e j g g g d i e jzd d d f 6� Z|e d d� d dl d e j2 e j g d d' g d
 e
 j� e
 j� g d e j e j g g g d i e j}d d d f 6e j~d d d f 6� Ze d d� d dl d e jP e j g d d' g d
 e
 jyg d e j e j g g g d i e jzd d d f 6� Z�e d d� d dl d e j\ e j g d d' g d
 e
 jyg d e j e j g g g d i e jzd d d f 6� Z�e d d� d dl d e j9 e j g d d' g d
 e
 j� e
 j� g d e j e j g g g d i e j�d d d f 6e j�d d d f 6� Z�e d d� d dl d e j e j g d d' g d
 e
 j�e
 j�g d e j g g e j g g e j� g g e j g g g d i e j�d d d f 6e j�d d d f 6e j�d d d f 6e j�d d d f 6� Z�d S(�   i����(   t   all_verticest   all_CTverticest   Vertext   CTVertexNt   namet   V_1t   typet   R2t	   particlest   colors   f(1,2,3)t   lorentzt   loop_particlest	   couplingsi    i   i   i   i   i   t   V_2s   d(-1,1,3)*d(-1,2,4)s   d(-1,1,3)*f(-1,2,4)s   d(-1,1,4)*d(-1,2,3)s   d(-1,1,4)*f(-1,2,3)s   d(-1,2,3)*f(-1,1,4)s   d(-1,2,4)*f(-1,1,3)s   f(-1,1,2)*f(-1,3,4)s   f(-1,1,3)*f(-1,2,4)s   f(-1,1,4)*f(-1,2,3)s   Identity(1,2)*Identity(3,4)s   Identity(1,3)*Identity(2,4)s   Identity(1,4)*Identity(2,3)i   i   i   i   i
   i	   t   V_3s   Identity(1,2)t   V_4t   V_5t   V_6t   V_7t   V_8t   V_9t   V_10t   V_11t   V_12t   V_13t   V_14t   V_15t   V_16t   V_17t   V_18t   V_19t   V_20t   V_21t   V_22t   V_23t   V_24t   V_25s   T(3,2,1)t   V_26t   V_27t   V_28t   V_29t   V_30t   V_31t   V_32t   V_33t   V_34t   V_35t   V_36t   V_37t   V_38t   V_39t   V_40t   V_41t   V_42t   V_43t   V_44t   V_45t   V_46t   V_47t   V_48t   V_49t   V_50t   V_51t   V_52t   V_53t   V_54s   Identity(2,3)t   V_55t   V_56s   d(1,2,3)t   V_57t   V_58t   V_59t   V_60s   Identity(3,4)t   V_61t   V_62s   d(2,3,4)t   V_63t   V_64t   V_65t   V_66t   UVt   V_67t   V_68t   V_69t   V_70t   V_71t   V_72t   V_73t   V_74t   V_75t   V_76t   V_77t   V_78t   V_79t   V_80t   V_81t   V_82t   V_83t   V_84t   V_85t   V_86t   V_87t   V_88t   V_89t   V_90t   V_91t   V_92t   V_93t   V_94t   V_95t   V_96t   V_97t   V_98t   V_99t   V_100t   V_101t   V_102t   V_103t   V_104t   V_105t   V_106(�  t   object_libraryR    R   R   R   R   t   Pt   CT_couplingst   CR
   t   Lt   gt   VVV3t   VVV4t   VVV5t   VVV6t   VVV7t   VVV8t   bt   ct   dt   st   tt   ut   R2GC_185_96t   R2GC_185_97t   R2GC_186_98t   R2GC_186_99R   t   VVVV2t   VVVV3t   VVVV4t   R2GC_149_78t   R2GC_149_79t   R2GC_147_74t   R2GC_147_75t   R2GC_148_76t   R2GC_148_77t   R2GC_153_84t   R2GC_190_104t   R2GC_152_83t   R2GC_191_105t   R2GC_151_81t   R2GC_151_82t   R2GC_150_80t   R2GC_187_100t   R2GC_187_101t   R2GC_188_103t   R2GC_188_102R   t
   t__tilde__t	   G__plus__t   FFS3t   FFS5t   R2GC_205_112t   R2GC_206_113R   t
   b__tilde__t   G0t   FFS1t   R2GC_183_95R   t   Ht   FFS2t   R2GC_182_94R   t
   G__minus__t   R2GC_207_114t   R2GC_204_111R   t   R2GC_208_115R   t   R2GC_209_116R   t   Y1t   FFV6t   FFV7t   R2GC_176_90t   R2GC_178_92R   t
   d__tilde__t   R2GC_175_89t   R2GC_177_91R   t
   c__tilde__t
   R2GC_100_1t
   R2GC_101_2R   R   t
   R2GC_105_6t
   R2GC_106_7R   t
   s__tilde__t
   R2GC_110_9t   R2GC_111_10R   t   R2GC_197_107t   R2GC_199_109R   t
   u__tilde__t   R2GC_196_106t   R2GC_198_108R   R   t   R2GC_115_11t   R2GC_116_12R   t   at   FFV1t   R2GC_156_87R   R   R    t   R2GC_154_85R!   R"   R#   t   R2GC_155_86R$   R%   R&   R'   R(   R)   t
   W__minus__t   FFV3t   R2GC_170_88R*   R+   R,   t	   W__plus__R-   R.   R/   t   Zt   FFV9t
   R2GC_102_3t
   R2GC_103_4R0   R1   R2   t   FFV5t
   R2GC_107_8R3   R4   R5   t   FF1t
   R2GC_104_5R6   R7   t   FF2t   FF3t   R2GC_200_110R8   R9   R:   t   R2GC_179_93R;   t   VV2t   VV3t   VV4t   R2GC_98_117t   R2GC_119_13t   R2GC_119_14t   R2GC_122_19R<   t   VVV2t   R2GC_125_24t   R2GC_125_25t   R2GC_125_26t   R2GC_125_27t   R2GC_125_28t   R2GC_125_29R=   t   VVV1t   R2GC_129_48t   R2GC_129_49R>   t   VVS1t   R2GC_120_15t   R2GC_120_16R?   t   VVVV7t   R2GC_137_66t   R2GC_137_67t   R2GC_137_68t   R2GC_137_69t   R2GC_137_70t   R2GC_137_71t   R2GC_137_72t   R2GC_137_73R@   t   R2GC_127_36t   R2GC_127_37t   R2GC_127_38t   R2GC_127_39t   R2GC_127_40t   R2GC_127_41RA   t   R2GC_133_56t   R2GC_133_57t   R2GC_133_58t   R2GC_133_59t   R2GC_133_60t   R2GC_133_61RB   t   VVVV1t   R2GC_126_30t   R2GC_126_31t   R2GC_126_32t   R2GC_126_33t   R2GC_126_34t   R2GC_126_35t   R2GC_128_42t   R2GC_128_43t   R2GC_128_44t   R2GC_128_45t   R2GC_128_46t   R2GC_128_47RC   t   R2GC_136_65RD   t   R2GC_130_50t   R2GC_130_51RE   t   R2GC_134_62t   R2GC_134_63RF   t   R2GC_123_20t   R2GC_123_21RG   t   R2GC_132_54t   R2GC_132_55t   R2GC_131_52t   R2GC_131_53RH   t   R2GC_124_22t   R2GC_124_23RI   t   VVSS1t   R2GC_121_17t   R2GC_121_18RJ   RK   t   R2GC_135_64RL   t   ghGt   UVGC_185_44t   UVGC_185_45t   UVGC_185_46t   UVGC_185_47t   UVGC_185_48t   UVGC_186_49t   UVGC_186_50t   UVGC_186_51t   UVGC_186_52t   UVGC_186_53RM   t
   UVGC_148_9t
   UVGC_148_8t
   UVGC_147_6t
   UVGC_147_7t   UVGC_190_64t   UVGC_190_65t   UVGC_190_66t   UVGC_190_67t   UVGC_190_68t   UVGC_191_69t   UVGC_191_70t   UVGC_151_12t   UVGC_151_13t   UVGC_150_10t   UVGC_150_11t   UVGC_187_54t   UVGC_187_55t   UVGC_187_56t   UVGC_187_57t   UVGC_192_71t   UVGC_192_72t   UVGC_192_73t   UVGC_192_74t   UVGC_152_14t   UVGC_153_15t   UVGC_189_60t   UVGC_189_61t   UVGC_188_58t   UVGC_189_62t   UVGC_189_63t   UVGC_188_59RO   t   UVGC_205_94t   UVGC_205_95t   UVGC_205_96t   UVGC_206_97t   UVGC_206_98t   UVGC_206_99RP   t   UVGC_183_41RQ   t   UVGC_182_40RR   t   UVGC_207_100t   UVGC_207_101t   UVGC_207_102t   UVGC_204_91t   UVGC_204_92t   UVGC_204_93RS   t   UVGC_208_103RT   t   UVGC_209_104RU   t   UVGC_176_32t   UVGC_178_36RV   t   UVGC_175_29t   UVGC_175_30t   UVGC_175_31t   UVGC_177_33t   UVGC_177_34t   UVGC_177_35RW   RX   t   UVGC_197_81t   UVGC_199_85RY   t   UVGC_196_78t   UVGC_196_79t   UVGC_196_80t   UVGC_198_82t   UVGC_198_83t   UVGC_198_84RZ   R[   t   FFV4t   UVGC_156_18t
   UVGC_139_2R\   R]   t   UVGC_194_76R^   t   UVGC_154_16t
   UVGC_141_3R_   R`   t   UVGC_173_27Ra   t   UVGC_155_17t   UVGC_157_19t   UVGC_157_20t   UVGC_157_21t   UVGC_157_22t   UVGC_157_23Rb   Rc   t   UVGC_195_77Rd   Re   Rf   t   UVGC_174_28Rg   t   UVGC_170_24t   UVGC_170_25Rh   Ri   t   UVGC_201_87t   UVGC_201_88Rj   Rk   Rl   Rm   t   UVGC_202_89t   UVGC_203_90Rn   t   UVGC_180_38t   UVGC_181_39Ro   t   FF4t
   UVGC_138_1Rp   Rq   t   UVGC_200_86t   UVGC_193_75Rr   Rs   Rt   t   UVGC_179_37t   UVGC_172_26Ru   t   VV1t   VV5t   UVGC_184_42t   UVGC_184_43t
   UVGC_146_4t
   UVGC_146_5Rv   (    (    (    sK   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/CT_vertices.pyt   <module>   s�  "	*K�*K� � � � � 	/			/			/	/	/	/	/	/	/	/	/	/																			/	/	/	/	/	/			/			/	cU	N{	B/	/	r�	N{	N{N�	6	B/	B/	B/BU	B/	/	/		*]� � E*�� � � � � � �	B{			B{			/	B{	B{	/	B{	B{	B	B	B	B	B	B	c�	c�	c�	c�	c�	c�	?/	?/	BB	?/	?/	BB	/	/			/			/	6                                                                                                                                                                                        decays.py                                                                                           0000644 0276724 0002567 00000024240 13234357560 011216  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     # This file was automatically created by FeynRules 2.4.46
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Thu 27 Oct 2016 23:02:25


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.Y1,P.d):'((MB**2 - MY1**2)*(6*gAd31**2*MB**2 + 6*gVd31**2*MB**2 + (6*gAd31**2*MB**4)/MY1**2 + (6*gVd31**2*MB**4)/MY1**2 - 12*gAd31**2*MY1**2 - 12*gVd31**2*MY1**2))/(96.*cmath.pi*abs(MB)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.Y1,P.u):'((MT**2 - MY1**2)*(6*gAu31**2*MT**2 + 6*gVu31**2*MT**2 + (6*gAu31**2*MT**4)/MY1**2 + (6*gVu31**2*MT**4)/MY1**2 - 12*gAu31**2*MY1**2 - 12*gVu31**2*MY1**2))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Y1 = Decay(name = 'Decay_Y1',
                 particle = P.Y1,
                 partial_widths = {(P.b,P.b__tilde__):'((-48*gAd33**2*MB**2 + 24*gVd33**2*MB**2 + 12*gAd33**2*MY1**2 + 12*gVd33**2*MY1**2)*cmath.sqrt(-4*MB**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.b,P.d__tilde__):'((-MB**2 + MY1**2)*(-6*gAd31**2*MB**2 - 6*gVd31**2*MB**2 - (6*gAd31**2*MB**4)/MY1**2 - (6*gVd31**2*MB**4)/MY1**2 + 12*gAd31**2*MY1**2 + 12*gVd31**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.c,P.c__tilde__):'(MY1**2*(12*gAu22**2*MY1**2 + 12*gVu22**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.d,P.b__tilde__):'((-MB**2 + MY1**2)*(-6*gAd31**2*MB**2 - 6*gVd31**2*MB**2 - (6*gAd31**2*MB**4)/MY1**2 - (6*gVd31**2*MB**4)/MY1**2 + 12*gAd31**2*MY1**2 + 12*gVd31**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.d,P.d__tilde__):'(MY1**2*(12*gAd11**2*MY1**2 + 12*gVd11**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.e__minus__,P.e__plus__):'(MY1**2*(4*gAl11**2*MY1**2 + 4*gVl11**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.mu__minus__,P.mu__plus__):'(MY1**2*(4*gAl22**2*MY1**2 + 4*gVl22**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.s,P.s__tilde__):'(MY1**2*(12*gAd22**2*MY1**2 + 12*gVd22**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.t,P.t__tilde__):'((-48*gAu33**2*MT**2 + 24*gVu33**2*MT**2 + 12*gAu33**2*MY1**2 + 12*gVu33**2*MY1**2)*cmath.sqrt(-4*MT**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.t,P.u__tilde__):'((-MT**2 + MY1**2)*(-6*gAu31**2*MT**2 - 6*gVu31**2*MT**2 - (6*gAu31**2*MT**4)/MY1**2 - (6*gVu31**2*MT**4)/MY1**2 + 12*gAu31**2*MY1**2 + 12*gVu31**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.ta__minus__,P.ta__plus__):'((-16*gAl33**2*MTA**2 + 8*gVl33**2*MTA**2 + 4*gAl33**2*MY1**2 + 4*gVl33**2*MY1**2)*cmath.sqrt(-4*MTA**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.u,P.t__tilde__):'((-MT**2 + MY1**2)*(-6*gAu31**2*MT**2 - 6*gVu31**2*MT**2 - (6*gAu31**2*MT**4)/MY1**2 - (6*gVu31**2*MT**4)/MY1**2 + 12*gAu31**2*MY1**2 + 12*gVu31**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.u,P.u__tilde__):'(MY1**2*(12*gAu11**2*MY1**2 + 12*gVu11**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.ve,P.ve__tilde__):'(gnu11**2*MY1**4)/(24.*cmath.pi*abs(MY1)**3)',
                                   (P.vm,P.vm__tilde__):'(gnu22**2*MY1**4)/(24.*cmath.pi*abs(MY1)**3)',
                                   (P.vt,P.vt__tilde__):'(gnu33**2*MY1**4)/(24.*cmath.pi*abs(MY1)**3)',
                                   (P.Xc__tilde__,P.Xc):'((-(gVXc**2*MXc**2) + (gVXc**2*MY1**2)/4.)*cmath.sqrt(-4*MXc**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.Xd,P.Xd__tilde__):'((-16*gAXd**2*MXd**2 + 8*gVXd**2*MXd**2 + 4*gAXd**2*MY1**2 + 4*gVXd**2*MY1**2)*cmath.sqrt(-4*MXd**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

                                                                                                                                                                                                                                                                                                                                                                decays.pyo                                                                                          0000644 0276724 0002567 00000017473 13234357560 011407  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc        
   @   su  d  d l  m Z m Z d  d l Z e d d d e j d i d e j e j f 6d e j e j	 f 6� Z
 e d d	 d e j d i d
 e j e j f 6d e j e j f 6d e j e j f 6d e j e j f 6d e j e j f 6� Z e d d d e j d i d e j e j f 6d e j e j f 6� Z e d d d e j d i d e j e j f 6� Z e d d d e j d i d e j e j f 6d e j e j f 6d e j e j f 6d e j e j f 6d e j e j f 6d e j e j f 6� Z e d d d e j d i d e j e j f 6d e j e j f 6d e j e j f 6d e j	 e j f 6d e j	 e j f 6d e j  e j f 6d e j! e j f 6d  e j" e j f 6d! e j e j f 6d" e j e j# f 6d# e j e j f 6d" e j e j f 6d$ e j e j# f 6d% e j e j$ f 6d& e j e j% f 6d' e j e j& f 6d( e j' e j( f 6d) e j) e j* f 6� Z+ e d d* d e j d i d+ e j e j f 6d, e j e j f 6d- e j	 e j f 6d. e j  e j f 6d. e j! e j f 6d- e j" e j f 6d/ e j e j f 6d0 e j e j f 6d, e j e j# f 6d1 e j e j$ f 6d1 e j e j% f 6d1 e j e j& f 6d2 e j e j f 6� Z, d S(3   i����(   t
   all_decayst   DecayNt   namet   Decay_bt   particlet   partial_widthss+  (((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)s�   ((MB**2 - MY1**2)*(6*gAd31**2*MB**2 + 6*gVd31**2*MB**2 + (6*gAd31**2*MB**4)/MY1**2 + (6*gVd31**2*MB**4)/MY1**2 - 12*gAd31**2*MY1**2 - 12*gVd31**2*MY1**2))/(96.*cmath.pi*abs(MB)**3)t   Decay_Hs`   ((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)s^   ((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)sa   ((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)s�   (((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)s�  (((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)t   Decay_ts+  (((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)s�   ((MT**2 - MY1**2)*(6*gAu31**2*MT**2 + 6*gVu31**2*MT**2 + (6*gAu31**2*MT**4)/MY1**2 + (6*gVu31**2*MT**4)/MY1**2 - 12*gAu31**2*MY1**2 - 12*gVu31**2*MY1**2))/(96.*cmath.pi*abs(MT)**3)t   Decay_ta__minus__s�   ((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)t   Decay_W__plus__s-   (ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)s,  (((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)s-   (ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)s�   ((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)t   Decay_Y1s�   ((-48*gAd33**2*MB**2 + 24*gVd33**2*MB**2 + 12*gAd33**2*MY1**2 + 12*gVd33**2*MY1**2)*cmath.sqrt(-4*MB**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)s�   ((-MB**2 + MY1**2)*(-6*gAd31**2*MB**2 - 6*gVd31**2*MB**2 - (6*gAd31**2*MB**4)/MY1**2 - (6*gVd31**2*MB**4)/MY1**2 + 12*gAd31**2*MY1**2 + 12*gVd31**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)sM   (MY1**2*(12*gAu22**2*MY1**2 + 12*gVu22**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)sM   (MY1**2*(12*gAd11**2*MY1**2 + 12*gVd11**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)sK   (MY1**2*(4*gAl11**2*MY1**2 + 4*gVl11**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)sK   (MY1**2*(4*gAl22**2*MY1**2 + 4*gVl22**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)sM   (MY1**2*(12*gAd22**2*MY1**2 + 12*gVd22**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)s�   ((-48*gAu33**2*MT**2 + 24*gVu33**2*MT**2 + 12*gAu33**2*MY1**2 + 12*gVu33**2*MY1**2)*cmath.sqrt(-4*MT**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)s�   ((-MT**2 + MY1**2)*(-6*gAu31**2*MT**2 - 6*gVu31**2*MT**2 - (6*gAu31**2*MT**4)/MY1**2 - (6*gVu31**2*MT**4)/MY1**2 + 12*gAu31**2*MY1**2 + 12*gVu31**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)s�   ((-16*gAl33**2*MTA**2 + 8*gVl33**2*MTA**2 + 4*gAl33**2*MY1**2 + 4*gVl33**2*MY1**2)*cmath.sqrt(-4*MTA**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)sM   (MY1**2*(12*gAu11**2*MY1**2 + 12*gVu11**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)s,   (gnu11**2*MY1**4)/(24.*cmath.pi*abs(MY1)**3)s,   (gnu22**2*MY1**4)/(24.*cmath.pi*abs(MY1)**3)s,   (gnu33**2*MY1**4)/(24.*cmath.pi*abs(MY1)**3)sl   ((-(gVXc**2*MXc**2) + (gVXc**2*MY1**2)/4.)*cmath.sqrt(-4*MXc**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)s�   ((-16*gAXd**2*MXd**2 + 8*gVXd**2*MXd**2 + 4*gAXd**2*MY1**2 + 4*gVXd**2*MY1**2)*cmath.sqrt(-4*MXd**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)t   Decay_Zs�   ((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)sy   (MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)su   (MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)sv   (MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)s�   ((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)s�   ((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)sq   (MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)s�   (((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)(-   t   object_libraryR    R   t	   particlest   Pt   bt
   W__minus__t   tt   Y1t   dR   t   Ht
   b__tilde__t
   t__tilde__t   ta__minus__t
   ta__plus__t	   W__plus__t   ZR   t   uR   t   vtR   t   ct
   s__tilde__t
   d__tilde__t   vet	   e__plus__t   vmt
   mu__plus__R	   t
   c__tilde__t
   e__minus__t   mu__minus__t   st
   u__tilde__t   ve__tilde__t   vm__tilde__t   vt__tilde__t   Xc__tilde__t   Xct   Xdt   Xd__tilde__R
   R   (    (    (    sF   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/decays.pyt   <module>   s|   							                                                                                                                                                                                                     DM_s_sp1_monotops.log                                                                               0000644 0276724 0002567 00000004051 13234357560 013440  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     # This file was automatically created by FeynRules 2.4.46
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Thu 27 Oct 2016 23:01:15


# 
# This is the logfile for the model DMsimp_s_spin1

# Authors: A. Martini, K. Mawatari, J. Wang, C. Zhang, B. Zaldivar, B. Fuks
# Model version: 2.1
# Checking the Quantum numbers
   * Electric charge defined.
# Checking the Lagrangians
   * All Lagrangians are ok.
#
# Particle definitions
#

   * No particles removed. All particles correspond to GenInt setup.

# Automatically assigned PDG numbers
   * Assigned PDG number 9000001 to particle ghA
   * Assigned PDG number 9000002 to particle ghZ
   * Assigned PDG number 9000003 to particle ghWp
   * Assigned PDG number 9000004 to particle ghWm


# Compulsory PDG codes:
   * Class SM leptons complete.
   * Class SM neutrinos complete.
   * Class SM quarks complete.
   * Class SM gauge bosons complete.
#
# Parameter definitions
#

   * All parameters are ok.


# Vertices
   * Calling FeynmanRules for 1 Lagrangians.
   * Number of classes vertices: 164
   * Number of flavored vertices: 160
   * Saved vertices in InterfaceRun[ 1 ].
   * Checked QNumber conservation.
      - Quantum number GhostNumber conserved in all vertices.
      - Quantum number LeptonNumber conserved in all vertices.
      - Quantum number Q conserved in all vertices.
      - Quantum number Y conserved in all vertices.
   * particles.py written.
   * parameters.py written.
#
# Vertex definitions
#

   * 137 vertices written.
   * vertices.py written.
#
# Lorentz structure definitions
#

   * 49 lorentz structures written.
   * lorentz.py written.
#
# Coupling definitions
#

   * 97 couplings written.
   * couplings.py written.
#
# Coupling order definitions
#

   * 0 couplings orders written.
   * coupling_orders.py written.
#
# Decay definitions
#

   * 7 decays written.
   * decay.py not written
#
# CTCoupling definitions
#

   * 221 CTcouplings written.
   * CT_couplings.py written.
#
# CTVertex definitions
#

   * 106 CTvertices written.
   * CT_vertices.py written.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       function_library.py                                                                                 0000644 0276724 0002567 00000003635 13234357560 013324  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     # This file is part of the UFO.
#
# This file contains definitions for functions that
# are extensions of the cmath library, and correspond
# either to functions that are in cmath, but inconvenient
# to access from there (e.g. z.conjugate()),
# or functions that are simply not defined.
#
#

__date__ = "22 July 2010"
__author__ = "claude.duhr@durham.ac.uk"

import cmath
from object_library import all_functions, Function

#
# shortcuts for functions from cmath
#

complexconjugate = Function(name = 'complexconjugate',
                            arguments = ('z',),
                            expression = 'z.conjugate()')


re = Function(name = 're',
              arguments = ('z',),
              expression = 'z.real')

im = Function(name = 'im',
              arguments = ('z',),
              expression = 'z.imag')

# New functions (trigonometric)

sec = Function(name = 'sec',
             arguments = ('z',),
             expression = '1./cmath.cos(z.real)')

asec = Function(name = 'asec',
             arguments = ('z',),
             expression = 'cmath.acos(1./(z.real))')

csc = Function(name = 'csc',
             arguments = ('z',),
             expression = '1./cmath.sin(z.real)')

acsc = Function(name = 'acsc',
             arguments = ('z',),
             expression = 'cmath.asin(1./(z.real))')

cot = Function(name = 'cot',
               arguments = ('z',),
               expression = '1./cmath.tan(z.real)')

# Heaviside theta function

theta_function = Function(name = 'theta_function',
             arguments = ('x','y','z'),
             expression = 'y if x else z')

# Auxiliary functions for NLO

cond = Function(name = 'cond',
                arguments = ('condition','ExprTrue','ExprFalse'),
                expression = '(ExprTrue if condition==0.0 else ExprFalse)')

reglog = Function(name = 'reglog',
                arguments = ('z'),
                expression = '(0.0 if z==0.0 else cmath.log(z.real))')

                                                                                                   function_library.pyo                                                                                0000644 0276724 0002567 00000002605 13234357560 013477  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc           @   s[  d  Z  d Z d d l Z d d l m Z m Z e d d d d$ d	 d
 � Z e d d d d% d	 d � Z e d d d d& d	 d � Z e d d d d' d	 d � Z	 e d d d d( d	 d � Z
 e d d d d) d	 d � Z e d d d d* d	 d � Z e d d d d+ d	 d � Z e d d d d, d	 d � Z e d d d d- d	 d! � Z e d d" d d d	 d# � Z d S(.   s   22 July 2010s   claude.duhr@durham.ac.uki����N(   t   all_functionst   Functiont   namet   complexconjugatet	   argumentst   zt
   expressions   z.conjugate()t   res   z.realt   ims   z.imagt   secs   1./cmath.cos(z.real)t   asecs   cmath.acos(1./(z.real))t   cscs   1./cmath.sin(z.real)t   acscs   cmath.asin(1./(z.real))t   cots   1./cmath.tan(z.real)t   theta_functiont   xt   ys   y if x else zt   condt	   conditiont   ExprTruet	   ExprFalses+   (ExprTrue if condition==0.0 else ExprFalse)t   reglogs&   (0.0 if z==0.0 else cmath.log(z.real))(   R   (   R   (   R   (   R   (   R   (   R   (   R   (   R   (   R   R   R   (   s	   conditionR   R   (   t   __date__t
   __author__t   cmatht   object_libraryR    R   R   R   R   R	   R
   R   R   R   R   R   R   (    (    (    sP   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/function_library.pyt   <module>   sH   										                                                                                                                           __init__.py                                                                                         0000644 0276724 0002567 00000002037 13234357560 011505  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     
import particles
import couplings
import lorentz
import parameters
import vertices
import coupling_orders
import write_param_card
import propagators


all_particles = particles.all_particles
all_vertices = vertices.all_vertices
all_couplings = couplings.all_couplings
all_lorentz = lorentz.all_lorentz
all_parameters = parameters.all_parameters
all_orders = coupling_orders.all_orders
all_functions = function_library.all_functions
all_propagators = propagators.all_propagators

try:
   import decays
except ImportError:
   pass
else:
   all_decays = decays.all_decays

try:
   import form_factors
except ImportError:
   pass
else:
   all_form_factors = form_factors.all_form_factors

try:
   import CT_vertices
except ImportError:
   pass
else:
   all_CTvertices = CT_vertices.all_CTvertices

try:
   import CT_parameters
except ImportError:
   pass
else:
   all_CTparameters = CT_parameters.all_CTparameters




gauge = [0, 1]


__author__ = "A. Martini, K. Mawatari, J. Wang, C. Zhang, B. Zaldivar, B. Fuks"
__date__ = "2016.10.27"
__version__= "2.1"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 __init__.pyo                                                                                        0000644 0276724 0002567 00000002301 13234357560 011656  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc           @   s~  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z e  j Z e j	 Z	 e j
 Z
 e j Z e j Z e j Z e j Z e j Z y d  d l Z Wn e k
 r� n
 Xe j Z y d  d l Z Wn e k
 r� n
 Xe j Z y d  d l Z Wn e k
 r%n
 Xe j Z y d  d l Z Wn e k
 rRn
 Xe j Z d d g Z d Z d Z d Z d S(   i����Ni    i   s@   A. Martini, K. Mawatari, J. Wang, C. Zhang, B. Zaldivar, B. Fukss
   2016.10.27s   2.1(   t	   particlest	   couplingst   lorentzt
   parameterst   verticest   coupling_orderst   write_param_cardt   propagatorst   all_particlest   all_verticest   all_couplingst   all_lorentzt   all_parameterst
   all_orderst   function_libraryt   all_functionst   all_propagatorst   decayst   ImportErrort
   all_decayst   form_factorst   all_form_factorst   CT_verticest   all_CTverticest   CT_parameterst   all_CTparameterst   gauget
   __author__t   __date__t   __version__(    (    (    sH   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/__init__.pyt   <module>   sN   												                                                                                                                                                                                                                                                                                                                               lorentz.py                                                                                          0000644 0276724 0002567 00000015053 13234357560 011445  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     # This file was automatically created by FeynRules 2.4.46
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Thu 27 Oct 2016 23:02:25


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


FF1 = Lorentz(name = 'FF1',
              spins = [ 2, 2 ],
              structure = 'P(-1,1)*Gamma(-1,2,1)')

FF2 = Lorentz(name = 'FF2',
              spins = [ 2, 2 ],
              structure = 'ProjM(2,1) + ProjP(2,1)')

FF3 = Lorentz(name = 'FF3',
              spins = [ 2, 2 ],
              structure = 'P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1) + P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)')

FF4 = Lorentz(name = 'FF4',
              spins = [ 2, 2 ],
              structure = '-(P(-1,1)*Gamma(-1,2,1)) + P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1) + P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)')

VV1 = Lorentz(name = 'VV1',
              spins = [ 3, 3 ],
              structure = 'P(1,2)*P(2,2)')

VV2 = Lorentz(name = 'VV2',
              spins = [ 3, 3 ],
              structure = 'Metric(1,2)')

VV3 = Lorentz(name = 'VV3',
              spins = [ 3, 3 ],
              structure = 'P(-1,2)**2*Metric(1,2)')

VV4 = Lorentz(name = 'VV4',
              spins = [ 3, 3 ],
              structure = 'P(1,2)*P(2,2) - (3*P(-1,2)**2*Metric(1,2))/2.')

VV5 = Lorentz(name = 'VV5',
              spins = [ 3, 3 ],
              structure = 'P(1,2)*P(2,2) - P(-1,2)**2*Metric(1,2)')

UUS1 = Lorentz(name = 'UUS1',
               spins = [ -1, -1, 1 ],
               structure = '1')

UUV1 = Lorentz(name = 'UUV1',
               spins = [ -1, -1, 3 ],
               structure = 'P(3,2)')

UUV2 = Lorentz(name = 'UUV2',
               spins = [ -1, -1, 3 ],
               structure = 'P(3,3)')

UUV3 = Lorentz(name = 'UUV3',
               spins = [ -1, -1, 3 ],
               structure = 'P(3,2) + P(3,3)')

SSS1 = Lorentz(name = 'SSS1',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS1 = Lorentz(name = 'FFS1',
               spins = [ 2, 2, 1 ],
               structure = 'Gamma5(2,1)')

FFS2 = Lorentz(name = 'FFS2',
               spins = [ 2, 2, 1 ],
               structure = 'Identity(2,1)')

FFS3 = Lorentz(name = 'FFS3',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1)')

FFS4 = Lorentz(name = 'FFS4',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) - ProjP(2,1)')

FFS5 = Lorentz(name = 'FFS5',
               spins = [ 2, 2, 1 ],
               structure = 'ProjP(2,1)')

FFS6 = Lorentz(name = 'FFS6',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) + ProjP(2,1)')

FFV1 = Lorentz(name = 'FFV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV2 = Lorentz(name = 'FFV2',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma5(-1,1)*Gamma(3,2,-1)')

FFV3 = Lorentz(name = 'FFV3',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV4 = Lorentz(name = 'FFV4',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

FFV5 = Lorentz(name = 'FFV5',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) - 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV6 = Lorentz(name = 'FFV6',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) - Gamma(3,2,-1)*ProjP(-1,1)')

FFV7 = Lorentz(name = 'FFV7',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + Gamma(3,2,-1)*ProjP(-1,1)')

FFV8 = Lorentz(name = 'FFV8',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV9 = Lorentz(name = 'FFV9',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 4*Gamma(3,2,-1)*ProjP(-1,1)')

VSS1 = Lorentz(name = 'VSS1',
               spins = [ 3, 1, 1 ],
               structure = 'P(1,2) - P(1,3)')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVV1 = Lorentz(name = 'VVV1',
               spins = [ 3, 3, 3 ],
               structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) + Epsilon(1,2,3,-1)*P(-1,2)')

VVV2 = Lorentz(name = 'VVV2',
               spins = [ 3, 3, 3 ],
               structure = '-(Epsilon(1,2,3,-1)*P(-1,2)) + Epsilon(1,2,3,-1)*P(-1,3)')

VVV3 = Lorentz(name = 'VVV3',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2)')

VVV4 = Lorentz(name = 'VVV4',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,2)*Metric(1,2)')

VVV5 = Lorentz(name = 'VVV5',
               spins = [ 3, 3, 3 ],
               structure = 'P(2,1)*Metric(1,3)')

VVV6 = Lorentz(name = 'VVV6',
               spins = [ 3, 3, 3 ],
               structure = 'P(2,3)*Metric(1,3)')

VVV7 = Lorentz(name = 'VVV7',
               spins = [ 3, 3, 3 ],
               structure = 'P(1,2)*Metric(2,3)')

VVV8 = Lorentz(name = 'VVV8',
               spins = [ 3, 3, 3 ],
               structure = 'P(1,3)*Metric(2,3)')

VVV9 = Lorentz(name = 'VVV9',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Epsilon(1,2,3,4)')

VVVV2 = Lorentz(name = 'VVVV2',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,2)*Metric(3,4)')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV6 = Lorentz(name = 'VVVV6',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

VVVV7 = Lorentz(name = 'VVVV7',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     lorentz.pyo                                                                                         0000644 0276724 0002567 00000011642 13234357560 011624  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc           @   s\  d  d l  m Z m Z d  d l m Z m Z m Z m Z m Z m	 Z	 m
 Z
 m Z y d  d l Z Wn e k
 rs n Xe d d d d d g d d	 � Z e d d
 d d d g d d � Z e d d d d d g d d � Z e d d d d d g d d � Z e d d d d d g d d � Z e d d d d d g d d � Z e d d d d d g d d � Z e d d d d d g d d � Z e d d d d d g d d � Z e d d d d  d  d g d d � Z e d d d d  d  d g d d � Z e d d  d d  d  d g d d! � Z e d d" d d  d  d g d d# � Z e d d$ d d d d g d d � Z e d d% d d d d g d d& � Z e d d' d d d d g d d( � Z e d d) d d d d g d d* � Z e d d+ d d d d g d d, � Z  e d d- d d d d g d d. � Z! e d d/ d d d d g d d � Z" e d d0 d d d d g d d1 � Z# e d d2 d d d d g d d3 � Z$ e d d4 d d d d g d d5 � Z% e d d6 d d d d g d d7 � Z& e d d8 d d d d g d d9 � Z' e d d: d d d d g d d; � Z( e d d< d d d d g d d= � Z) e d d> d d d d g d d? � Z* e d d@ d d d d g d dA � Z+ e d dB d d d d g d dC � Z, e d dD d d d d g d d � Z- e d dE d d d d g d dF � Z. e d dG d d d d g d dH � Z/ e d dI d d d d g d dJ � Z0 e d dK d d d d g d dL � Z1 e d dM d d d d g d dN � Z2 e d dO d d d d g d dP � Z3 e d dQ d d d d g d dR � Z4 e d dS d d d d g d dT � Z5 e d dU d d d d g d dV � Z6 e d dW d d d d d g d d � Z7 e d dX d d d d d g d d � Z8 e d dY d d d d d g d dZ � Z9 e d d[ d d d d d g d d\ � Z: e d d] d d d d d g d d^ � Z; e d d_ d d d d d g d d` � Z< e d da d d d d d g d db � Z= e d dc d d d d d g d dd � Z> e d de d d d d d g d df � Z? d S(g   i����(   t   all_lorentzt   Lorentz(   t   complexconjugatet   ret   imt   csct   sect   acsct   asect   cotNt   namet   FF1t   spinsi   t	   structures   P(-1,1)*Gamma(-1,2,1)t   FF2s   ProjM(2,1) + ProjP(2,1)t   FF3sG   P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1) + P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)t   FF4sb   -(P(-1,1)*Gamma(-1,2,1)) + P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1) + P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)t   VV1i   s   P(1,2)*P(2,2)t   VV2s   Metric(1,2)t   VV3s   P(-1,2)**2*Metric(1,2)t   VV4s-   P(1,2)*P(2,2) - (3*P(-1,2)**2*Metric(1,2))/2.t   VV5s&   P(1,2)*P(2,2) - P(-1,2)**2*Metric(1,2)t   UUS1i   t   1t   UUV1s   P(3,2)t   UUV2s   P(3,3)t   UUV3s   P(3,2) + P(3,3)t   SSS1t   FFS1s   Gamma5(2,1)t   FFS2s   Identity(2,1)t   FFS3s
   ProjM(2,1)t   FFS4s   ProjM(2,1) - ProjP(2,1)t   FFS5s
   ProjP(2,1)t   FFS6t   FFV1s   Gamma(3,2,1)t   FFV2s   Gamma5(-1,1)*Gamma(3,2,-1)t   FFV3s   Gamma(3,2,-1)*ProjM(-1,1)t   FFV4s   Gamma(3,2,-1)*ProjP(-1,1)t   FFV5s7   Gamma(3,2,-1)*ProjM(-1,1) - 2*Gamma(3,2,-1)*ProjP(-1,1)t   FFV6s5   Gamma(3,2,-1)*ProjM(-1,1) - Gamma(3,2,-1)*ProjP(-1,1)t   FFV7s5   Gamma(3,2,-1)*ProjM(-1,1) + Gamma(3,2,-1)*ProjP(-1,1)t   FFV8s7   Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)t   FFV9s7   Gamma(3,2,-1)*ProjM(-1,1) + 4*Gamma(3,2,-1)*ProjP(-1,1)t   VSS1s   P(1,2) - P(1,3)t   VVS1t   VVV1s8   -(Epsilon(1,2,3,-1)*P(-1,1)) + Epsilon(1,2,3,-1)*P(-1,2)t   VVV2s8   -(Epsilon(1,2,3,-1)*P(-1,2)) + Epsilon(1,2,3,-1)*P(-1,3)t   VVV3s   P(3,1)*Metric(1,2)t   VVV4s   P(3,2)*Metric(1,2)t   VVV5s   P(2,1)*Metric(1,3)t   VVV6s   P(2,3)*Metric(1,3)t   VVV7s   P(1,2)*Metric(2,3)t   VVV8s   P(1,3)*Metric(2,3)t   VVV9s{   P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)t   SSSS1t   VVSS1t   VVVV1s   Epsilon(1,2,3,4)t   VVVV2s   Metric(1,4)*Metric(2,3)t   VVVV3s   Metric(1,3)*Metric(2,4)t   VVVV4s   Metric(1,2)*Metric(3,4)t   VVVV5sM   Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)t   VVVV6sU   Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.t   VVVV7sK   Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)(@   t   object_libraryR    R   t   function_libraryR   R   R   R   R   R   R   R	   t   form_factorst   ForFact   ImportErrorR   R   R   R   R   R   R   R   R   R   R   R   R   R   R   R   R   R   R    R!   R"   R#   R$   R%   R&   R'   R(   R)   R*   R+   R,   R-   R.   R/   R0   R1   R2   R3   R4   R5   R6   R7   R8   R9   R:   R;   R<   R=   R>   (    (    (    sG   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/lorentz.pyt   <module>   s0  :																																																                                                                                              model.pkl                                                                                           0000644 0276724 0002567 00000512657 13234357560 011222  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �cmadgraph.loop.loop_base_objects
LoopModel
q)�q(Uref_dict_to0q}qUversion_tagqUu/group/hepheno/smsharma/Dark-Showers/MG5_aMC_v2_5_2/models/DMsimp_s_spin1##{'date': '2016-12-10', 'version': '2.5.2'}qU	functionsq]q(cDMsimp_s_spin1.object_library
Function
q	)�q
}q(UexprqUz.conjugate()UnameqUcomplexconjugateqU	argumentsqUz�ubh	)�q}q(hUz.realhUreqhUz�ubh	)�q}q(hUz.imaghUimqhUz�ubh	)�q}q(hU1./cmath.cos(z.real)hUsecqhUz�ubh	)�q}q(hUcmath.acos(1./(z.real))hUasecqhUz�ubh	)�q}q(hU1./cmath.sin(z.real)hUcscqhUz�ubh	)�q}q (hUcmath.asin(1./(z.real))hUacscq!hUz�ubh	)�q"}q#(hU1./cmath.tan(z.real)hUcotq$hUz�ubh	)�q%}q&(hUy if x else zhUtheta_functionq'hUxUyUz�ubh	)�q(}q)(hU+(ExprTrue if condition==0.0 else ExprFalse)hUcondq*hU	conditionUExprTrueU	ExprFalse�ubh	)�q+}q,(hU&(0.0 if z==0.0 else cmath.log(z.real))hUreglogq-hUzubeUinteraction_dictq.}q/hUDMsimp_s_spin1q0U
parametersq1}q2(UaEWM1q3�q4]q5(cmadgraph.core.base_objects
ModelVariable
q6)�q7}q8(hU1/aEWM1q9Utypeq:Urealq;hUmdl_aEWUvalueq<NUdependq=h4ubh6)�q>}q?(hUvcmath.sqrt(mdl_MZ__exp__2/2. + cmath.sqrt(mdl_MZ__exp__4/4. - (mdl_aEW*cmath.pi*mdl_MZ__exp__2)/(mdl_Gf*mdl_sqrt__2)))h:h;hUmdl_MWq@h<Nh=h3�ubh6)�qA}qB(hU cmath.sqrt(mdl_aEW) h:h;hUmdl_sqrt__aEWh<Nh=h3�ubh6)�qC}qD(hU$2*mdl_sqrt__aEW*cmath.sqrt(cmath.pi)h:h;hUmdl_eeh<Nh=h3�ubh6)�qE}qF(hU	mdl_MW**2h:h;hUmdl_MW__exp__2h<Nh=h3�ubh6)�qG}qH(hU!1 - mdl_MW__exp__2/mdl_MZ__exp__2h:h;hUmdl_sw2h<Nh=h3�ubh6)�qI}qJ(hUcmath.sqrt(1 - mdl_sw2)h:h;hUmdl_cwh<Nh=h3�ubh6)�qK}qL(hU cmath.sqrt(mdl_sw2) h:h;hUmdl_sqrt__sw2qMh<Nh=h3�ubh6)�qN}qO(hhMh:h;hUmdl_swh<Nh=h3�ubh6)�qP}qQ(hUmdl_ee/mdl_cwh:h;hUmdl_g1h<Nh=h3�ubh6)�qR}qS(hUmdl_ee/mdl_swh:h;hUmdl_gwh<Nh=h3�ubh6)�qT}qU(hU(2*mdl_MW*mdl_sw)/mdl_eeh:h;hUmdl_vevh<Nh=h3�ubh6)�qV}qW(hU
mdl_vev**2h:h;hUmdl_vev__exp__2h<Nh=h3�ubh6)�qX}qY(hU#mdl_MH__exp__2/(2.*mdl_vev__exp__2)h:h;hUmdl_lamh<Nh=h3�ubh6)�qZ}q[(hU(mdl_ymb*mdl_sqrt__2)/mdl_vevh:h;hUmdl_ybq\h<Nh=h3�ubh6)�q]}q^(hU(mdl_ymt*mdl_sqrt__2)/mdl_vevh:h;hUmdl_ytq_h<Nh=h3�ubh6)�q`}qa(hU(mdl_ymtau*mdl_sqrt__2)/mdl_vevh:h;hUmdl_ytauqbh<Nh=h3�ubh6)�qc}qd(hU#cmath.sqrt(mdl_lam*mdl_vev__exp__2)h:h;hUmdl_muHh<Nh=h3�ubh6)�qe}qf(hh\h:UcomplexqghU	mdl_I1a33qhh<Nh=h3�ubh6)�qi}qj(hh_h:hghU	mdl_I2a33h<Nh=h3�ubh6)�qk}ql(hh_h:hghU	mdl_I3a33qmh<Nh=h3�ubh6)�qn}qo(hh\h:hghU	mdl_I4a33h<Nh=h3�ubh6)�qp}qq(hU	mdl_ee**2h:h;hUmdl_ee__exp__2h<Nh=h3�ubh6)�qr}qs(hU	mdl_sw**2h:h;hUmdl_sw__exp__2h<Nh=h3�ubh6)�qt}qu(hU	mdl_cw**2h:h;hUmdl_cw__exp__2h<Nh=h3�ubh6)�qv}qw(hU	mdl_yb**2h:h;hUmdl_yb__exp__2h<Nh=h3�ubh6)�qx}qy(hU	mdl_yt**2h:h;hUmdl_yt__exp__2h<Nh=h3�ubeUexternal�qz]q{(cmadgraph.core.base_objects
ParamCardVariable
q|)�q}}q~(UlhablockqULOOPq�hUMU_Rq�h<G@V�1&�yUlhacodeq�]q�Kaubh|)�q�}q�(hUDMINPUTSq�hUmdl_gVXch<G        h�]q�Kaubh|)�q�}q�(hh�hUmdl_gVXdh<G?�      h�]q�Kaubh|)�q�}q�(hh�hUmdl_gAXdh<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gVd11h<G?�      h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gVu11h<G?�      h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gVd22h<G?�      h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gVu22h<G?�      h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gVd33h<G?�      h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gVu33h<G?�      h�]q�K	aubh|)�q�}q�(hh�hU	mdl_gVl11h<G        h�]q�K
aubh|)�q�}q�(hh�hU	mdl_gVl22h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gVl33h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gAd11h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gAu11h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gAd22h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gAu22h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gAd33h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gAu33h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gAl11h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gAl22h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gAl33h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gnu11h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gnu22h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gnu33h<G        h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gVu31h<G?�      h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gAu31h<G?�      h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gVd31h<G?�      h�]q�Kaubh|)�q�}q�(hh�hU	mdl_gAd31h<G?�      h�]q�Kaubh|)�q�}q�(hh�hUmdl_gVhh<G        h�]q�Kaubh|)�q�}q�(hUSMINPUTSq�hUaEWM1q�h<G@_������h�]q�Kaubh|)�q�}q�(hh�hUmdl_Gfh<G>�u渻��h�]q�Kaubh|)�q�}q�(hh�hUaSq�h<G?�Ov_ح�h�]q�Kaubh|)�q�}q�(hUYUKAWAq�hUmdl_ymbh<G@������h�]q�Kaubh|)�q�}q�(hh�hUmdl_ymth<K�h�]q�Kaubh|)�q�}q�(hh�hU	mdl_ymtauh<G?�n��O�;h�]q�Kaubh|)�q�}q�(hUMASSq�hUmdl_MZq�h<G@V��n.�h�]q�Kaubh|)�q�}q�(hh�hUmdl_MTAq�h<G?�n��O�;h�]q�Kaubh|)�q�}q�(hh�hUmdl_MTq�h<K�h�]q�Kaubh|)�q�}r   (hh�hUmdl_MBr  h<G@������h�]r  Kaubh|)�r  }r  (hh�hUmdl_MHr  h<K}h�]r  Kaubh|)�r  }r  (hh�hUmdl_MXrr	  h<G@$      h�]r
  J?ML aubh|)�r  }r  (hh�hUmdl_MXcr  h<G@$      h�]r  J@ML aubh|)�r  }r  (hh�hUmdl_MXdr  h<G@$      h�]r  JIML aubh|)�r  }r  (hh�hUmdl_MY1r  h<G@�@     h�]r  JAKL aubh|)�r  }r  (hUDECAYr  hUmdl_WZr  h<G@�+j��gh�]r  Kaubh|)�r  }r  (hj  hUmdl_WWr  h<G@ �z�G�h�]r  Kaubh|)�r   }r!  (hj  hUmdl_WTr"  h<G?�"%q~�jh�]r#  Kaubh|)�r$  }r%  (hj  hUmdl_WHr&  h<G?p��NP��h�]r'  Kaubh|)�r(  }r)  (hj  hUmdl_WY1r*  h<G@$      h�]r+  JAKL aube)]r,  (h6)�r-  }r.  (hU0.0r/  h:h;hUZEROr0  h<Nh=)ubh6)�r1  }r2  (hU	mdl_MZ**2h:h;hUmdl_MZ__exp__2h<Nh=)ubh6)�r3  }r4  (hU	mdl_MZ**4h:h;hUmdl_MZ__exp__4h<Nh=)ubh6)�r5  }r6  (hU cmath.sqrt(2) h:h;hUmdl_sqrt__2h<Nh=)ubh6)�r7  }r8  (hU	mdl_MH**2h:h;hUmdl_MH__exp__2h<Nh=)ubh6)�r9  }r:  (hUcomplex(0,1)r;  h:hghUmdl_complexih<Nh=)ubh6)�r<  }r=  (hU	mdl_MB**2h:h;hUmdl_MB__exp__2h<Nh=)ubh6)�r>  }r?  (hU	mdl_MT**2h:h;hUmdl_MT__exp__2h<Nh=)ubh6)�r@  }rA  (hUmdl_gAd33**2h:h;hUmdl_gAd33__exp__2h<Nh=)ubh6)�rB  }rC  (hUmdl_gVd33**2h:h;hUmdl_gVd33__exp__2h<Nh=)ubh6)�rD  }rE  (hUmdl_gAu22**2h:h;hUmdl_gAu22__exp__2h<Nh=)ubh6)�rF  }rG  (hUmdl_gVu22**2h:h;hUmdl_gVu22__exp__2h<Nh=)ubh6)�rH  }rI  (hUmdl_gAd11**2h:h;hUmdl_gAd11__exp__2h<Nh=)ubh6)�rJ  }rK  (hUmdl_gVd11**2h:h;hUmdl_gVd11__exp__2h<Nh=)ubh6)�rL  }rM  (hUmdl_gAd22**2h:h;hUmdl_gAd22__exp__2h<Nh=)ubh6)�rN  }rO  (hUmdl_gVd22**2h:h;hUmdl_gVd22__exp__2h<Nh=)ubh6)�rP  }rQ  (hUmdl_gAu33**2h:h;hUmdl_gAu33__exp__2h<Nh=)ubh6)�rR  }rS  (hUmdl_gVu33**2h:h;hUmdl_gVu33__exp__2h<Nh=)ubh6)�rT  }rU  (hUmdl_gAu11**2h:h;hUmdl_gAu11__exp__2h<Nh=)ubh6)�rV  }rW  (hUmdl_gVu11**2h:h;hUmdl_gVu11__exp__2h<Nh=)ubh6)�rX  }rY  (hUmdl_gAd31**2h:h;hUmdl_gAd31__exp__2h<Nh=)ubh6)�rZ  }r[  (hUmdl_gVd31**2h:h;hUmdl_gVd31__exp__2h<Nh=)ubh6)�r\  }r]  (hUmdl_gAu31**2h:h;hUmdl_gAu31__exp__2h<Nh=)ubh6)�r^  }r_  (hUmdl_gVu31**2h:h;hUmdl_gVu31__exp__2h<Nh=)ubeUMU_Rr`  �ra  ]rb  h6)�rc  }rd  (hUMU_R**2h:h;hUmdl_MU_R__exp__2h<Nh=ja  ubaUaSre  �rf  ]rg  (h6)�rh  }ri  (hU cmath.sqrt(aS) h:h;hUmdl_sqrt__aSh<Nh=jf  ubh6)�rj  }rk  (hU#2*mdl_sqrt__aS*cmath.sqrt(cmath.pi)h:h;hUGh<Nh=je  �ubh6)�rl  }rm  (hUG**2h:hghUmdl_G__exp__2h<Nh=je  �ubh6)�rn  }ro  (hUG**3h:hghUmdl_G__exp__3h<Nh=je  �ubh6)�rp  }rq  (hUG**4h:hghUmdl_G__exp__4h<Nh=je  �ubeuUinteractionsrr  cmadgraph.core.base_objects
InteractionList
rs  )�rt  (cmadgraph.core.base_objects
Interaction
ru  )�rv  (Uloop_particlesrw  NUperturbation_typerx  NUcolorry  ]rz  cmadgraph.core.color_algebra
ColorString
r{  )�r|  }r}  (Ucoeffr~  cfractions
Fraction
r  U1�Rr�  Uloop_Nc_powerr�  K Uis_imaginaryr�  �UNc_powerr�  K ubaUordersr�  }r�  UQEDr�  KsU	particlesr�  cmadgraph.core.base_objects
ParticleList
r�  )�r�  (cmadgraph.core.base_objects
Particle
r�  )�r�  (Ucountertermr�  }r�  hUhUself_antipartr�  �jy  Kh:U Uwidthr�  j&  Ucharger�  G        Umassr�  j  ULeptonNumberr�  K UYK Uantinamer�  UhUliner�  Udashedr�  Uis_partr�  �Uspinr�  KU
propagatorr�  U Updg_coder�  Ku}r�  bj�  j�  j�  e}r�  bUlorentzr�  ]r�  USSSS1r�  aU	couplingsr�  }r�  K K �r�  UGC_49sh:Ubaser�  Uidr�  Ku}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  USSS1r�  aj�  }r�  K K �r�  UGC_76sh:j�  j�  Ku}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  )�r�  (j�  }r�  hUghar�  j�  �jy  Kh:Ughostr�  j�  j0  j�  G        j�  j0  j�  K UYK j�  Ugha~r�  j�  Udottedr�  j�  �j�  Kj�  U j�  JAT� u}r�  bj�  )�r�  (j�  }r�  hUghwmr�  j�  �jy  Kj�  Kj�  j  j�  G��      j�  h@j�  Ughwm~r�  UYK j�  K j�  j�  j�  �h:j�  j�  U j�  JDT� u}r�  bj�  )�r�  (j�  }r�  hUw+r�  j�  �jy  Kj�  Kj�  j  j�  G?�      j�  h@j�  Uw-r�  UYK j�  K j�  Uwavyr�  j�  �h:U j�  U j�  Ku}r�  be}r�  bj�  ]r�  UUUV3r�  aj�  }r�  K K �r�  UGC_3sh:j�  j�  Ku}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  )�r�  (j�  }r�  hUghwpr�  j�  �jy  Kj�  Kj�  j  j�  G?�      j�  h@j�  Ughwp~r�  UYK j�  K j�  j�  j�  �h:j�  j�  U j�  JCT� u}r�  bj�  )�r�  (j�  }r�  hj�  j�  �jy  Kh:U j�  j  j�  G?�      j�  h@j�  K UYK j�  j�  j�  j�  j�  �j�  Kj�  U j�  Ku}r�  be}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_4sh:j�  j�  Ku}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  )�r�  (j�  }r�  hj�  j�  �jy  Kh:j�  j�  j  j�  G��      j�  h@j�  K UYK j�  j�  j�  j�  j�  �j�  Kj�  U j�  JDT� u}r�  bj�  )�r�  (j�  }r�  hj�  j�  �jy  Kj�  Kj�  j0  j�  G        j�  j0  j�  j�  UYK j�  K j�  j�  j�  �h:j�  j�  U j�  JAT� u}r�  bj�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_3sh:j�  j�  Ku}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  UUUS1r�  aj�  }r   K K �r  UGC_78sh:j�  j�  Ku}r  bju  )�r  (jw  Njx  Njy  ]r  j{  )�r  }r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r  (j�  j�  j�  )�r	  (j�  }r
  hUaj�  �jy  Kh:U j�  j0  j�  G        j�  j0  j�  K UYK j�  Uaj�  j�  j�  �j�  Kj�  K j�  Ku}r  be}r  bj�  ]r  j�  aj�  }r  K K �r  UGC_4sh:j�  j�  Ku}r  bju  )�r  (jw  Njx  Njy  ]r  j{  )�r  }r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  }r  j�  Ksj�  j�  )�r  (j�  j�  j�  )�r  (j�  }r  hUzj�  �jy  Kh:U j�  j  j�  G        j�  h�j�  K UYK j�  Uzj�  j�  j�  �j�  Kj�  U j�  Ku}r  be}r  bj�  ]r  j�  aj�  }r  K K �r  UGC_60sh:j�  j�  Ku}r  bju  )�r   (jw  Njx  Njy  ]r!  j{  )�r"  }r#  (j~  j  U1�Rr$  j�  K j�  �j�  K ubaj�  }r%  j�  Ksj�  j�  )�r&  (j�  j�  )�r'  (j�  }r(  hUghzr)  j�  �jy  Kj�  Kj�  j  j�  G        j�  h�j�  Ughz~r*  UYK j�  K j�  j�  j�  �h:j�  j�  U j�  JBT� u}r+  bj�  e}r,  bj�  ]r-  (UUUV1r.  UUUV2r/  ej�  }r0  (K K�r1  UGC_59K K �r2  UGC_59uh:j�  j�  K	u}r3  bju  )�r4  (jw  Njx  Njy  ]r5  j{  )�r6  }r7  (j~  j  U1�Rr8  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r9  (j�  )�r:  (j�  }r;  hj�  j�  �jy  Kh:j�  j�  j  j�  G?�      j�  h@j�  K UYK j�  j�  j�  j�  j�  �j�  Kj�  U j�  JCT� u}r<  bj�  j�  e}r=  bj�  ]r>  (j.  j/  ej�  }r?  (K K�r@  UGC_4K K �rA  UGC_4uh:j�  j�  K
u}rB  bju  )�rC  (jw  Njx  Njy  ]rD  j{  )�rE  }rF  (j~  j  U1�RrG  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�rH  (j:  j�  j�  e}rI  bj�  ]rJ  j�  aj�  }rK  K K �rL  UGC_78sh:j�  j�  Ku}rM  bju  )�rN  (jw  Njx  Njy  ]rO  j{  )�rP  }rQ  (j~  j  U1�RrR  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�rS  (j:  j�  j	  e}rT  bj�  ]rU  (j.  j/  ej�  }rV  (K K�rW  UGC_3K K �rX  UGC_3uh:j�  j�  Ku}rY  bju  )�rZ  (jw  Njx  Njy  ]r[  j{  )�r\  }r]  (j~  j  U1�Rr^  j�  K j�  �j�  K ubaj�  j%  j�  j�  )�r_  (j:  j�  j  e}r`  bj�  ]ra  (j.  j/  ej�  }rb  (K K�rc  UGC_59K K �rd  UGC_59uh:j�  j�  Ku}re  bju  )�rf  (jw  Njx  Njy  ]rg  j{  )�rh  }ri  (j~  j  U1�Rrj  j�  K j�  �j�  K ubaj�  j  j�  j�  )�rk  (j:  j'  j�  e}rl  bj�  ]rm  (j.  j/  ej�  }rn  (K K�ro  UGC_60K K �rp  UGC_60uh:j�  j�  Ku}rq  bju  )�rr  (jw  Njx  Njy  ]rs  j{  )�rt  }ru  (j~  j  U1�Rrv  j�  K j�  �j�  K ubaj�  j%  j�  j�  )�rw  (j�  )�rx  (j�  }ry  hj)  j�  �jy  Kh:j�  j�  j  j�  G        j�  h�j�  K UYK j�  j*  j�  j�  j�  �j�  Kj�  U j�  JBT� u}rz  bj�  j�  e}r{  bj�  ]r|  (j.  j/  ej�  }r}  (K K�r~  UGC_59K K �r  UGC_59uh:j�  j�  Ku}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j  j�  j�  )�r�  (jx  j�  j�  e}r�  bj�  ]r�  (j.  j/  ej�  }r�  (K K�r�  UGC_60K K �r�  UGC_60uh:j�  j�  Ku}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (jx  j'  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_87sh:j�  j�  Ku}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  cmadgraph.core.color_algebra
f
r�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  UQCDr�  Ksj�  j�  )�r�  (j�  )�r�  (j�  }r�  hUghgr�  j�  �jy  Kh:j�  j�  j0  j�  G        j�  j0  j�  K UYK j�  Ughg~r�  j�  j�  j�  �j�  Kj�  U j�  KRu}r�  bj�  )�r�  (j�  }r�  hj�  j�  �jy  Kj�  Kj�  j0  j�  G        j�  j0  j�  j�  UYK j�  K j�  j�  j�  �h:j�  j�  U j�  KRu}r�  bj�  )�r�  (j�  }r�  hUgj�  �jy  Kh:U j�  j0  j�  G        j�  j0  j�  K UYK j�  Ugj�  Ucurlyr�  j�  �j�  Kj�  K j�  Ku}r�  be}r�  bj�  ]r�  (j.  j/  ej�  }r�  (K K�r�  UGC_10K K �r�  UGC_10uh:j�  j�  Ku}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (UVVV3r�  UVVV4r�  UVVV5r�  UVVV6r�  UVVV7r�  UVVV8r�  ej�  }r�  (K K�r�  UGC_12K K �r�  UGC_10K K�r�  UGC_12K K�r�  UGC_10K K�r�  UGC_10K K�r�  UGC_12uh:j�  j�  Ku}r�  bju  )�r�  (jw  Njx  Njy  ]r�  (j{  )�r�  (j�  J����K K�Rr�  j�  KKJ�����Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  KKJ�����Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  KKJ�����Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubej�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j�  j�  e}r�  bj�  ]r�  (UVVVV2r�  UVVVV3r�  UVVVV4r�  ej�  }r�  (K K�r�  UGC_13KK�r�  UGC_13K K �r�  UGC_14KK�r�  UGC_14KK�r�  UGC_13KK �r�  UGC_14uh:j�  j�  Ku}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  cmadgraph.core.color_algebra
T
r�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  )�r�  (j�  }r�  hUbj�  �jy  Kj�  Kj�  j0  j�  G��UUUUUUj�  j  j�  Ub~r�  UYK j�  K j�  Ustraightr�  j�  �h:U j�  U j�  Ku}r�  bj�  )�r�  (j�  }r�  hUbj�  �jy  Kh:U j�  j0  j�  G��UUUUUUj�  j  j�  K UYK j�  j�  j�  j�  j�  �j�  Kj�  U j�  Ku}r�  bj�  e}r�  bj�  ]r�  (UFFS3r   UFFS5r  ej�  }r  (K K�r  UGC_90K K �r  UGC_90uh:j�  j�  Ku}r  bju  )�r  (jw  Njx  Njy  ]r  j{  )�r  }r	  (j~  j  U1�Rr
  j�  K j�  �j�  K ubaj�  }r  j�  Ksj�  j�  )�r  (j�  )�r  (j�  }r  hUta-r  j�  �jy  Kj�  Kj�  j0  j�  G��      j�  h�j�  Uta+r  UYK j�  Kj�  j�  j�  �h:U j�  U j�  Ku}r  bj�  )�r  (j�  }r  hj  j�  �jy  Kh:U j�  j0  j�  G��      j�  h�j�  KUYK j�  j  j�  j�  j�  �j�  Kj�  U j�  Ku}r  bj�  e}r  bj�  ]r  UFFS6r  aj�  }r  K K �r  UGC_97sh:j�  j�  Ku}r  bju  )�r  (jw  Njx  Njy  ]r  j{  )�r  j�  KK �Rr  a}r  (j~  j  U1�Rr   j�  K j�  �j�  K ubaj�  }r!  j�  Ksj�  j�  )�r"  (j�  )�r#  (j�  }r$  hUtj�  �jy  Kj�  Kj�  j"  j�  G?�UUUUUUj�  h�j�  Ut~r%  UYK j�  K j�  j�  j�  �h:U j�  U j�  Ku}r&  bj�  )�r'  (j�  }r(  hUtj�  �jy  Kh:U j�  j"  j�  G?�UUUUUUj�  h�j�  K UYK j�  j%  j�  j�  j�  �j�  Kj�  U j�  Ku}r)  bj�  e}r*  bj�  ]r+  j  aj�  }r,  K K �r-  UGC_92sh:j�  j�  Ku}r.  bju  )�r/  (jw  Njx  Njy  ]r0  j{  )�r1  }r2  (j~  j  U1�Rr3  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r4  (j	  j�  j�  e}r5  bj�  ]r6  UVVV9r7  aj�  }r8  K K �r9  UGC_4sh:j�  j�  Ku}r:  bju  )�r;  (jw  Njx  Njy  ]r<  j{  )�r=  }r>  (j~  j  U1�Rr?  j�  K j�  �j�  K ubaj�  }r@  j�  Ksj�  j�  )�rA  (j�  j�  j�  j�  e}rB  bj�  ]rC  UVVSS1rD  aj�  }rE  K K �rF  UGC_50sh:j�  j�  Ku}rG  bju  )�rH  (jw  Njx  Njy  ]rI  j{  )�rJ  }rK  (j~  j  U1�RrL  j�  K j�  �j�  K ubaj�  }rM  j�  Ksj�  j�  )�rN  (j�  j�  j�  e}rO  bj�  ]rP  UVVS1rQ  aj�  }rR  K K �rS  UGC_79sh:j�  j�  Ku}rT  bju  )�rU  (jw  Njx  Njy  ]rV  j{  )�rW  }rX  (j~  j  U1�RrY  j�  K j�  �j�  K ubaj�  }rZ  j�  Ksj�  j�  )�r[  (j	  j	  j�  j�  e}r\  bj�  ]r]  UVVVV5r^  aj�  }r_  K K �r`  UGC_5sh:j�  j�  Ku}ra  bju  )�rb  (jw  Njx  Njy  ]rc  j{  )�rd  }re  (j~  j  U1�Rrf  j�  K j�  �j�  K ubaj�  j  j�  j�  )�rg  (j�  j�  j  e}rh  bj�  ]ri  j7  aj�  }rj  K K �rk  UGC_60sh:j�  j�  Ku}rl  bju  )�rm  (jw  Njx  Njy  ]rn  j{  )�ro  }rp  (j~  j  U1�Rrq  j�  K j�  �j�  K ubaj�  }rr  j�  Ksj�  j�  )�rs  (j�  j�  j�  j�  e}rt  bj�  ]ru  j^  aj�  }rv  K K �rw  UGC_51sh:j�  j�  Ku}rx  bju  )�ry  (jw  Njx  Njy  ]rz  j{  )�r{  }r|  (j~  j  U1�Rr}  j�  K j�  �j�  K ubaj�  }r~  UDMVr  Ksj�  j�  )�r�  (j�  )�r�  (j�  }r�  hUy1r�  j�  �jy  Kh:U j�  j*  j�  G        j�  j  j�  K UYK j�  Uy1r�  j�  j�  j�  �j�  Kj�  U j�  JAKL u}r�  bj�  )�r�  (j�  }r�  hUxcr�  j�  �jy  Kj�  Kj�  j0  j�  G        j�  j  j�  Uxc~r�  UYK j�  K j�  j�  j�  �h:U j�  U j�  J@ML u}r�  bj�  )�r�  (j�  }r�  hj�  j�  �jy  Kh:U j�  j0  j�  G        j�  j  j�  K UYK j�  j�  j�  j�  j�  �j�  Kj�  U j�  J@ML u}r�  be}r�  bj�  ]r�  UVSS1r�  aj�  }r�  K K �r�  UGC_41sh:j�  j�  Ku}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j  Ksj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (UFFV1r�  UFFV2r�  ej�  }r�  (K K�r�  UGC_18K K �r�  UGC_33uh:j�  j�  Ku}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j  Ksj�  j�  )�r�  (j�  )�r�  (j�  }r�  hUdj�  �jy  Kj�  Kj�  j0  j�  G��UUUUUUj�  j0  j�  Ud~r�  UYK j�  K j�  j�  j�  �h:U j�  U j�  Ku}r�  bj�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�r�  UGC_17K K �r�  UGC_32uh:j�  j�  K u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j  Ksj�  j�  )�r�  (j�  )�r�  (j�  }r�  hUcj�  �jy  Kj�  Kj�  j0  j�  G?�UUUUUUj�  j0  j�  Uc~r�  UYK j�  K j�  j�  j�  �h:U j�  U j�  Ku}r�  bj�  )�r�  (j�  }r�  hUcj�  �jy  Kh:U j�  j0  j�  G?�UUUUUUj�  j0  j�  K UYK j�  j�  j�  j�  j�  �j�  Kj�  U j�  Ku}r�  bj�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�r�  UGC_23K K �r�  UGC_38uh:j�  j�  K!u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  )�r�  (j�  }r�  hUdj�  �jy  Kh:U j�  j0  j�  G��UUUUUUj�  j0  j�  K UYK j�  j�  j�  j�  j�  �j�  Kj�  U j�  Ku}r�  bj�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�r�  UGC_17K K �r�  UGC_32uh:j�  j�  K"u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j  Ksj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�r�  UGC_15K K �r�  UGC_30uh:j�  j�  K#u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j  Ksj�  j�  )�r�  (j�  )�r�  (j�  }r�  hUe-r�  j�  �jy  Kj�  Kj�  j0  j�  G��      j�  j0  j�  Ue+r�  UYK j�  Kj�  j�  j�  �h:U j�  U j�  Ku}r�  bj�  )�r�  (j�  }r�  hj�  j�  �jy  Kh:U j�  j0  j�  G��      j�  j0  j�  KUYK j�  j�  j�  j�  j�  �j�  Kj�  U j�  Ku}r�  bj�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�r�  UGC_19K K �r�  UGC_34uh:j�  j�  K$u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r   }r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  }r  j  Ksj�  j�  )�r  (j�  )�r  (j�  }r  hUmu-r  j�  �jy  Kj�  Kj�  j0  j�  G��      j�  j0  j�  Umu+r  UYK j�  Kj�  j�  j�  �h:U j�  U j�  Ku}r	  bj�  )�r
  (j�  }r  hj  j�  �jy  Kh:U j�  j0  j�  G��      j�  j0  j�  KUYK j�  j  j�  j�  j�  �j�  Kj�  U j�  Ku}r  bj�  e}r  bj�  ]r  (j�  j�  ej�  }r  (K K�r  UGC_20K K �r  UGC_35uh:j�  j�  K%u}r  bju  )�r  (jw  Njx  Njy  ]r  j{  )�r  j�  KK �Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  }r  j  Ksj�  j�  )�r  (j�  )�r  (j�  }r  hUsj�  �jy  Kj�  Kj�  j0  j�  G��UUUUUUj�  j0  j�  Us~r  UYK j�  K j�  j�  j�  �h:U j�  U j�  Ku}r  bj�  )�r  (j�  }r   hUsj�  �jy  Kh:U j�  j0  j�  G��UUUUUUj�  j0  j�  K UYK j�  j  j�  j�  j�  �j�  Kj�  U j�  Ku}r!  bj�  e}r"  bj�  ]r#  (j�  j�  ej�  }r$  (K K�r%  UGC_16K K �r&  UGC_31uh:j�  j�  K&u}r'  bju  )�r(  (jw  Njx  Njy  ]r)  j{  )�r*  }r+  (j~  j  U1�Rr,  j�  K j�  �j�  K ubaj�  }r-  j  Ksj�  j�  )�r.  (j  j  j�  e}r/  bj�  ]r0  (j�  j�  ej�  }r1  (K K�r2  UGC_21K K �r3  UGC_36uh:j�  j�  K'u}r4  bju  )�r5  (jw  Njx  Njy  ]r6  j{  )�r7  j�  KK �Rr8  a}r9  (j~  j  U1�Rr:  j�  K j�  �j�  K ubaj�  }r;  j  Ksj�  j�  )�r<  (j#  j'  j�  e}r=  bj�  ]r>  (j�  j�  ej�  }r?  (K K�r@  UGC_25K K �rA  UGC_40uh:j�  j�  K(u}rB  bju  )�rC  (jw  Njx  Njy  ]rD  j{  )�rE  j�  KK �RrF  a}rG  (j~  j  U1�RrH  j�  K j�  �j�  K ubaj�  }rI  j  Ksj�  j�  )�rJ  (j�  )�rK  (j�  }rL  hUuj�  �jy  Kj�  Kj�  j0  j�  G?�UUUUUUj�  j0  j�  Uu~rM  UYK j�  K j�  j�  j�  �h:U j�  U j�  Ku}rN  bj'  j�  e}rO  bj�  ]rP  (j�  j�  ej�  }rQ  (K K�rR  UGC_24K K �rS  UGC_39uh:j�  j�  K)u}rT  bju  )�rU  (jw  Njx  Njy  ]rV  j{  )�rW  j�  KK �RrX  a}rY  (j~  j  U1�RrZ  j�  K j�  �j�  K ubaj�  jI  j�  j�  )�r[  (j#  j�  )�r\  (j�  }r]  hUuj�  �jy  Kh:U j�  j0  j�  G?�UUUUUUj�  j0  j�  K UYK j�  jM  j�  j�  j�  �j�  Kj�  U j�  Ku}r^  bj�  e}r_  bj�  ]r`  (j�  j�  ej�  }ra  (K K�rb  UGC_24K K �rc  UGC_39uh:j�  j�  K*u}rd  bju  )�re  (jw  Njx  Njy  ]rf  j{  )�rg  j�  KK �Rrh  a}ri  (j~  j  U1�Rrj  j�  K j�  �j�  K ubaj�  }rk  j  Ksj�  j�  )�rl  (jK  j\  j�  e}rm  bj�  ]rn  (j�  j�  ej�  }ro  (K K�rp  UGC_22K K �rq  UGC_37uh:j�  j�  K+u}rr  bju  )�rs  (jw  Njx  Njy  ]rt  j{  )�ru  }rv  (j~  j  U1�Rrw  j�  K j�  �j�  K ubaj�  }rx  j  Ksj�  j�  )�ry  (j�  )�rz  (j�  }r{  hUxdr|  j�  �jy  Kj�  Kj�  j0  j�  G        j�  j  j�  Uxd~r}  UYK j�  K j�  j�  j�  �h:U j�  U j�  JIML u}r~  bj�  )�r  (j�  }r�  hj|  j�  �jy  Kh:U j�  j0  j�  G        j�  j  j�  K UYK j�  j}  j�  j�  j�  �j�  Kj�  U j�  JIML u}r�  bj�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�r�  UGC_26K K �r�  UGC_42uh:j�  j�  K,u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j	  j�  j�  j  e}r�  bj�  ]r�  UVVVV6r�  aj�  }r�  K K �r�  UGC_64sh:j�  j�  K-u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j  j  j�  j�  e}r�  bj�  ]r�  jD  aj�  }r�  K K �r�  UGC_72sh:j�  j�  K.u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j  j  j�  e}r�  bj�  ]r�  jQ  aj�  }r�  K K �r�  UGC_88sh:j�  j�  K/u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j  j  e}r�  bj�  ]r�  j^  aj�  }r�  K K �r�  UGC_52sh:j�  j�  K0u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j  Ksj�  j�  )�r�  (j�  )�r�  (j�  }r�  hUver�  j�  �jy  Kj�  Kj�  j0  j�  G        j�  j0  j�  Uve~r�  UYK j�  Kj�  j�  j�  �h:U j�  U j�  Ku}r�  bj�  )�r�  (j�  }r�  hj�  j�  �jy  Kh:U j�  j0  j�  G        j�  j0  j�  KUYK j�  j�  j�  j�  j�  �j�  Kj�  U j�  Ku}r�  bj�  e}r�  bj�  ]r�  UFFV3r�  aj�  }r�  K K �r�  UGC_27sh:j�  j�  K1u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j  Ksj�  j�  )�r�  (j�  )�r�  (j�  }r�  hUvmr�  j�  �jy  Kj�  Kj�  j0  j�  G        j�  j0  j�  Uvm~r�  UYK j�  Kj�  j�  j�  �h:U j�  U j�  Ku}r�  bj�  )�r�  (j�  }r�  hj�  j�  �jy  Kh:U j�  j0  j�  G        j�  j0  j�  KUYK j�  j�  j�  j�  j�  �j�  Kj�  U j�  Ku}r�  bj�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_28sh:j�  j�  K2u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j  Ksj�  j�  )�r�  (j�  )�r�  (j�  }r�  hUvtr�  j�  �jy  Kj�  Kj�  j0  j�  G        j�  j0  j�  Uvt~r�  UYK j�  Kj�  j�  j�  �h:U j�  U j�  Ku}r�  bj�  )�r�  (j�  }r�  hj�  j�  �jy  Kh:U j�  j0  j�  G        j�  j0  j�  KUYK j�  j�  j�  j�  j�  �j�  Kj�  U j�  Ku}r�  bj�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_29sh:j�  j�  K3u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j	  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_3sh:j�  j�  K4u}r   bju  )�r  (jw  Njx  Njy  ]r  j{  )�r  }r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r  (j  j
  j	  e}r  bj�  ]r  j�  aj�  }r	  K K �r
  UGC_3sh:j�  j�  K5u}r  bju  )�r  (jw  Njx  Njy  ]r  j{  )�r  }r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r  (j  j  j	  e}r  bj�  ]r  j�  aj�  }r  K K �r  UGC_3sh:j�  j�  K6u}r  bju  )�r  (jw  Njx  Njy  ]r  j{  )�r  j�  KK �Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  }r  j�  Ksj�  j�  )�r  (jK  j\  j	  e}r  bj�  ]r   j�  aj�  }r!  K K �r"  UGC_2sh:j�  j�  K7u}r#  bju  )�r$  (jw  Njx  Njy  ]r%  j{  )�r&  j�  KK �Rr'  a}r(  (j~  j  U1�Rr)  j�  K j�  �j�  K ubaj�  j  j�  j�  )�r*  (j�  j�  j	  e}r+  bj�  ]r,  j�  aj�  }r-  K K �r.  UGC_2sh:j�  j�  K8u}r/  bju  )�r0  (jw  Njx  Njy  ]r1  j{  )�r2  j�  KK �Rr3  a}r4  (j~  j  U1�Rr5  j�  K j�  �j�  K ubaj�  j  j�  j�  )�r6  (j#  j'  j	  e}r7  bj�  ]r8  j�  aj�  }r9  K K �r:  UGC_2sh:j�  j�  K9u}r;  bju  )�r<  (jw  Njx  Njy  ]r=  j{  )�r>  j�  KK �Rr?  a}r@  (j~  j  U1�RrA  j�  K j�  �j�  K ubaj�  }rB  j�  Ksj�  j�  )�rC  (j�  j�  j	  e}rD  bj�  ]rE  j�  aj�  }rF  K K �rG  UGC_1sh:j�  j�  K:u}rH  bju  )�rI  (jw  Njx  Njy  ]rJ  j{  )�rK  j�  KK �RrL  a}rM  (j~  j  U1�RrN  j�  K j�  �j�  K ubaj�  jB  j�  j�  )�rO  (j  j  j	  e}rP  bj�  ]rQ  j�  aj�  }rR  K K �rS  UGC_1sh:j�  j�  K;u}rT  bju  )�rU  (jw  Njx  Njy  ]rV  j{  )�rW  j�  KK �RrX  a}rY  (j~  j  U1�RrZ  j�  K j�  �j�  K ubaj�  jB  j�  j�  )�r[  (j�  j�  j	  e}r\  bj�  ]r]  j�  aj�  }r^  K K �r_  UGC_1sh:j�  j�  K<u}r`  bju  )�ra  (jw  Njx  Njy  ]rb  j{  )�rc  j�  KKK �Rrd  a}re  (j~  j  U1�Rrf  j�  K j�  �j�  K ubaj�  }rg  j�  Ksj�  j�  )�rh  (jK  j\  j�  e}ri  bj�  ]rj  j�  aj�  }rk  K K �rl  UGC_11sh:j�  j�  K=u}rm  bju  )�rn  (jw  Njx  Njy  ]ro  j{  )�rp  j�  KKK �Rrq  a}rr  (j~  j  U1�Rrs  j�  K j�  �j�  K ubaj�  jg  j�  j�  )�rt  (j�  j�  j�  e}ru  bj�  ]rv  j�  aj�  }rw  K K �rx  UGC_11sh:j�  j�  K>u}ry  bju  )�rz  (jw  Njx  Njy  ]r{  j{  )�r|  j�  KKK �Rr}  a}r~  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  jg  j�  j�  )�r�  (j#  j'  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_11sh:j�  j�  K?u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  jg  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_11sh:j�  j�  K@u}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  jg  j�  j�  )�r�  (j  j  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_11sh:j�  j�  KAu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  jg  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_11sh:j�  j�  KBu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j\  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_56sh:j�  j�  KCu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_56sh:j�  j�  KDu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j'  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_56sh:j�  j�  KEu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (jK  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_56sh:j�  j�  KFu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_56sh:j�  j�  KGu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j#  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_56sh:j�  j�  KHu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_56sh:j�  j�  KIu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r   }r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r  (j  j�  j�  e}r  bj�  ]r  j�  aj�  }r  K K �r  UGC_56sh:j�  j�  KJu}r  bju  )�r	  (jw  Njx  Njy  ]r
  j{  )�r  }r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r  (j  j�  j�  e}r  bj�  ]r  j�  aj�  }r  K K �r  UGC_56sh:j�  j�  KKu}r  bju  )�r  (jw  Njx  Njy  ]r  j{  )�r  }r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r  (j�  j�  j�  e}r  bj�  ]r  j�  aj�  }r  K K �r  UGC_56sh:j�  j�  KLu}r  bju  )�r  (jw  Njx  Njy  ]r   j{  )�r!  }r"  (j~  j  U1�Rr#  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r$  (j�  j
  j�  e}r%  bj�  ]r&  j�  aj�  }r'  K K �r(  UGC_56sh:j�  j�  KMu}r)  bju  )�r*  (jw  Njx  Njy  ]r+  j{  )�r,  }r-  (j~  j  U1�Rr.  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r/  (j�  j  j�  e}r0  bj�  ]r1  j�  aj�  }r2  K K �r3  UGC_56sh:j�  j�  KNu}r4  bju  )�r5  (jw  Njx  Njy  ]r6  j{  )�r7  j�  KK �Rr8  a}r9  (j~  j  U1�Rr:  j�  K j�  �j�  K ubaj�  }r;  j�  Ksj�  j�  )�r<  (jK  j\  j  e}r=  bj�  ]r>  (j�  UFFV9r?  ej�  }r@  (K K�rA  UGC_65K K �rB  UGC_58uh:j�  j�  KOu}rC  bju  )�rD  (jw  Njx  Njy  ]rE  j{  )�rF  j�  KK �RrG  a}rH  (j~  j  U1�RrI  j�  K j�  �j�  K ubaj�  j;  j�  j�  )�rJ  (j�  j�  j  e}rK  bj�  ]rL  (j�  j?  ej�  }rM  (K K�rN  UGC_65K K �rO  UGC_58uh:j�  j�  KPu}rP  bju  )�rQ  (jw  Njx  Njy  ]rR  j{  )�rS  j�  KK �RrT  a}rU  (j~  j  U1�RrV  j�  K j�  �j�  K ubaj�  j;  j�  j�  )�rW  (j#  j'  j  e}rX  bj�  ]rY  (j�  j?  ej�  }rZ  (K K�r[  UGC_65K K �r\  UGC_58uh:j�  j�  KQu}r]  bju  )�r^  (jw  Njx  Njy  ]r_  j{  )�r`  j�  KK �Rra  a}rb  (j~  j  U1�Rrc  j�  K j�  �j�  K ubaj�  j;  j�  j�  )�rd  (j�  j�  j  e}re  bj�  ]rf  (j�  UFFV5rg  ej�  }rh  (K K�ri  UGC_65K K �rj  UGC_57uh:j�  j�  KRu}rk  bju  )�rl  (jw  Njx  Njy  ]rm  j{  )�rn  j�  KK �Rro  a}rp  (j~  j  U1�Rrq  j�  K j�  �j�  K ubaj�  j;  j�  j�  )�rr  (j  j  j  e}rs  bj�  ]rt  (j�  jg  ej�  }ru  (K K�rv  UGC_65K K �rw  UGC_57uh:j�  j�  KSu}rx  bju  )�ry  (jw  Njx  Njy  ]rz  j{  )�r{  j�  KK �Rr|  a}r}  (j~  j  U1�Rr~  j�  K j�  �j�  K ubaj�  j;  j�  j�  )�r  (j�  j�  j  e}r�  bj�  ]r�  (j�  jg  ej�  }r�  (K K�r�  UGC_65K K �r�  UGC_57uh:j�  j�  KTu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_69sh:j�  j�  KUu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_69sh:j�  j�  KVu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j  e}r�  bj�  ]r�  j�  aj�  }r�  K K �r�  UGC_69sh:j�  j�  KWu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j  e}r�  bj�  ]r�  (j�  UFFV8r�  ej�  }r�  (K K�r�  UGC_66K K �r�  UGC_57uh:j�  j�  KXu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j  j
  j  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�r�  UGC_66K K �r�  UGC_57uh:j�  j�  KYu}r�  bju  )�r�  (jw  Njx  Njy  ]r�  j{  )�r�  }r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j  j  j  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�r�  UGC_66K K �r�  UGC_57uh:j�  j�  KZu}r�  bju  )�r�  (jw  ]r�  (]r�  Ka]r�  Ka]r�  Ka]r�  Ka]r�  Ka]r�  Kaejx  Njy  ]r�  j{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  j�  j�  j�  ej�  }r�  (K K�UR2GC_186_98K K �UR2GC_185_96K K�UR2GC_186_98K K�UR2GC_185_96K K�UR2GC_185_96K K�UR2GC_186_98uh:UR2r�  j�  K[u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  j�  j�  j�  ej�  }r�  (K K�UR2GC_186_99K K �UR2GC_185_97K K�UR2GC_186_99K K�UR2GC_185_97K K�UR2GC_185_97K K�UR2GC_186_99uh:j�  j�  K\u}r�  bju  )�r�  (jw  ]r�  (]r�  Ka]r�  Ka]r�  Ka]r�  Ka]r�  Ka]r�  Kaejx  Njy  ]r�  (j{  )�r�  (cmadgraph.core.color_algebra
d
r�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr   j�  J����KK�Rr  e}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j�  J����K K�Rr  j�  J����KK�Rr  e}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r	  (j�  J����K K�Rr
  j�  J����KK�Rr  e}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j�  J����KK�Rr  j�  J����K K�Rr  e}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j�  J����KK�Rr  j�  J����K K�Rr  e}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j�  J����K K�Rr  j�  J����KK�Rr  e}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j�  J����K K�Rr  j�  J����KK�Rr  e}r   (j~  j  U1�Rr!  j�  K j�  �j�  K ubj{  )�r"  (j�  J����K K�Rr#  j�  J����KK�Rr$  e}r%  (j~  j  U1�Rr&  j�  K j�  �j�  K ubj{  )�r'  (cmadgraph.core.color_algebra
Tr
r(  K K�Rr)  j(  KK�Rr*  e}r+  (j~  j  U4�Rr,  j�  K j�  �j�  K ubj{  )�r-  (j(  K K�Rr.  j(  KK�Rr/  e}r0  (j~  j  U4�Rr1  j�  K j�  �j�  K ubj{  )�r2  (j(  K K�Rr3  j(  KK�Rr4  e}r5  (j~  j  U4�Rr6  j�  K j�  �j�  K ubej�  }r7  j�  Ksj�  j�  )�r8  (j�  j�  j�  j�  e}r9  bj�  ]r:  (j�  j�  j�  ej�  }r;  (KK �UR2GC_147_74KK�UR2GC_151_81KK �UR2GC_148_76KK�UR2GC_149_78KK�UR2GC_152_83KK�UR2GC_147_74KK�UR2GC_188_102KK �UR2GC_147_74KK�UR2GC_147_74KK�UR2GC_148_76KK�UR2GC_151_81KK �UR2GC_147_74KK�UR2GC_149_78K
K �UR2GC_151_81KK�UR2GC_147_74KK�UR2GC_147_74KK�UR2GC_147_74K K �UR2GC_149_78KK�UR2GC_148_76KK�UR2GC_153_84KK �UR2GC_152_83KK �UR2GC_151_81K
K�UR2GC_151_81KK�UR2GC_147_74KK �UR2GC_147_74K K�UR2GC_149_78KK �UR2GC_153_84KK�UR2GC_187_100KK�UR2GC_147_74KK �UR2GC_149_78KK�UR2GC_147_74K K�UR2GC_149_78K
K�UR2GC_151_81uh:j�  j�  K]u}r<  bju  )�r=  (jw  ]r>  ]r?  Kaajx  Njy  ]r@  (j{  )�rA  (j�  J����K K�RrB  j�  J����KK�RrC  e}rD  (j~  j  U1�RrE  j�  K j�  �j�  K ubj{  )�rF  (j�  J����K K�RrG  j�  J����KK�RrH  e}rI  (j~  j  U1�RrJ  j�  K j�  �j�  K ubj{  )�rK  (j�  J����K K�RrL  j�  J����KK�RrM  e}rN  (j~  j  U1�RrO  j�  K j�  �j�  K ubj{  )�rP  (j�  J����K K�RrQ  j�  J����KK�RrR  e}rS  (j~  j  U1�RrT  j�  K j�  �j�  K ubj{  )�rU  (j�  J����KK�RrV  j�  J����K K�RrW  e}rX  (j~  j  U1�RrY  j�  K j�  �j�  K ubj{  )�rZ  (j�  J����KK�Rr[  j�  J����K K�Rr\  e}r]  (j~  j  U1�Rr^  j�  K j�  �j�  K ubj{  )�r_  (j�  J����K K�Rr`  j�  J����KK�Rra  e}rb  (j~  j  U1�Rrc  j�  K j�  �j�  K ubj{  )�rd  (j�  J����K K�Rre  j�  J����KK�Rrf  e}rg  (j~  j  U1�Rrh  j�  K j�  �j�  K ubj{  )�ri  (j�  J����K K�Rrj  j�  J����KK�Rrk  e}rl  (j~  j  U1�Rrm  j�  K j�  �j�  K ubj{  )�rn  (j(  K K�Rro  j(  KK�Rrp  e}rq  (j~  j  U4�Rrr  j�  K j�  �j�  K ubj{  )�rs  (j(  K K�Rrt  j(  KK�Rru  e}rv  (j~  j  U4�Rrw  j�  K j�  �j�  K ubj{  )�rx  (j(  K K�Rry  j(  KK�Rrz  e}r{  (j~  j  U4�Rr|  j�  K j�  �j�  K ubej�  }r}  j�  Ksj�  j�  )�r~  (j�  j�  j�  j�  e}r  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K	K�UR2GC_150_80KK �UR2GC_147_75KK�UR2GC_151_82KK �UR2GC_148_77KK�UR2GC_149_79KK�UR2GC_147_75KK�UR2GC_188_103KK �UR2GC_147_75KK�UR2GC_147_75K	K �UR2GC_150_80KK�UR2GC_190_104KK�UR2GC_151_82KK �UR2GC_147_75KK�UR2GC_149_79K
K �UR2GC_151_82KK�UR2GC_147_75KK�UR2GC_147_75KK�UR2GC_147_75K K �UR2GC_149_79KK�UR2GC_188_103KK�UR2GC_148_77KK �UR2GC_191_105KK �UR2GC_151_82K
K�UR2GC_151_82KK�UR2GC_147_75KK �UR2GC_147_75K K�UR2GC_149_79KK �UR2GC_190_104K	K�UR2GC_150_80KK�UR2GC_187_101KK�UR2GC_147_75KK �UR2GC_149_79KK�UR2GC_147_75K K�UR2GC_149_79K
K�UR2GC_151_82uh:j�  j�  K^u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  UFFS2r�  aj�  }r�  K K �UR2GC_182_94sh:j�  j�  K_u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj�  Kuj�  j�  )�r�  (j#  j'  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UR2GC_209_116sh:j�  j�  K`u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (UFFV6r�  UFFV7r�  ej�  }r�  (K K�UR2GC_178_92K K �UR2GC_176_90uh:j�  j�  Kau}r�  bju  )�r�  (jw  ]r�  ]r�  (KKKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�UR2GC_177_91K K �UR2GC_175_89uh:j�  j�  Kbu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�U
R2GC_101_2K K �U
R2GC_100_1uh:j�  j�  Kcu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�UR2GC_177_91K K �UR2GC_175_89uh:j�  j�  Kdu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�U
R2GC_106_7K K �U
R2GC_105_6uh:j�  j�  Keu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j  j  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�UR2GC_111_10K K �U
R2GC_110_9uh:j�  j�  Kfu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j#  j'  j�  e}r�  bj�  ]r   (j�  j�  ej�  }r  (K K�UR2GC_199_109K K �UR2GC_197_107uh:j�  j�  Kgu}r  bju  )�r  (jw  ]r  ]r  (KKKeajx  Njy  ]r  j{  )�r  j�  KK �Rr  a}r	  (j~  j  U1�Rr
  j�  K j�  �j�  K ubaj�  }r  (j  Kj�  Kuj�  j�  )�r  (jK  j'  j�  e}r  bj�  ]r  (j�  j�  ej�  }r  (K K�UR2GC_198_108K K �UR2GC_196_106uh:j�  j�  Khu}r  bju  )�r  (jw  ]r  ]r  (KKKeajx  Njy  ]r  j{  )�r  j�  KK �Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  j  j�  j�  )�r  (j#  j\  j�  e}r  bj�  ]r  (j�  j�  ej�  }r  (K K�UR2GC_198_108K K �UR2GC_196_106uh:j�  j�  Kiu}r  bju  )�r  (jw  ]r  ]r   (KKeajx  Njy  ]r!  j{  )�r"  j�  KK �Rr#  a}r$  (j~  j  U1�Rr%  j�  K j�  �j�  K ubaj�  }r&  (j  Kj�  Kuj�  j�  )�r'  (jK  j\  j�  e}r(  bj�  ]r)  (j�  j�  ej�  }r*  (K K�UR2GC_116_12K K �UR2GC_115_11uh:j�  j�  Kju}r+  bju  )�r,  (jw  ]r-  ]r.  (KKeajx  Njy  ]r/  j{  )�r0  j�  KK �Rr1  a}r2  (j~  j  U1�Rr3  j�  K j�  �j�  K ubaj�  }r4  (j�  Kj�  Kuj�  j�  )�r5  (jK  j\  j	  e}r6  bj�  ]r7  j�  aj�  }r8  K K �UR2GC_156_87sh:j�  j�  Kku}r9  bju  )�r:  (jw  ]r;  ]r<  (KKeajx  Njy  ]r=  j{  )�r>  j�  KK �Rr?  a}r@  (j~  j  U1�RrA  j�  K j�  �j�  K ubaj�  j4  j�  j�  )�rB  (j�  j�  j	  e}rC  bj�  ]rD  j�  aj�  }rE  K K �UR2GC_156_87sh:j�  j�  Klu}rF  bju  )�rG  (jw  ]rH  ]rI  (KKeajx  Njy  ]rJ  j{  )�rK  j�  KK �RrL  a}rM  (j~  j  U1�RrN  j�  K j�  �j�  K ubaj�  j4  j�  j�  )�rO  (j#  j'  j	  e}rP  bj�  ]rQ  j�  aj�  }rR  K K �UR2GC_156_87sh:j�  j�  Kmu}rS  bju  )�rT  (jw  ]rU  ]rV  (KKeajx  Njy  ]rW  j{  )�rX  j�  KK �RrY  a}rZ  (j~  j  U1�Rr[  j�  K j�  �j�  K ubaj�  }r\  (j�  Kj�  Kuj�  j�  )�r]  (j�  j�  j	  e}r^  bj�  ]r_  j�  aj�  }r`  K K �UR2GC_154_85sh:j�  j�  Knu}ra  bju  )�rb  (jw  ]rc  ]rd  (KKeajx  Njy  ]re  j{  )�rf  j�  KK �Rrg  a}rh  (j~  j  U1�Rri  j�  K j�  �j�  K ubaj�  j\  j�  j�  )�rj  (j  j  j	  e}rk  bj�  ]rl  j�  aj�  }rm  K K �UR2GC_154_85sh:j�  j�  Kou}rn  bju  )�ro  (jw  ]rp  ]rq  (KKeajx  Njy  ]rr  j{  )�rs  j�  KK �Rrt  a}ru  (j~  j  U1�Rrv  j�  K j�  �j�  K ubaj�  j\  j�  j�  )�rw  (j�  j�  j	  e}rx  bj�  ]ry  j�  aj�  }rz  K K �UR2GC_154_85sh:j�  j�  Kpu}r{  bju  )�r|  (jw  ]r}  ]r~  (KKeajx  Njy  ]r  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (jK  j\  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UR2GC_155_86sh:j�  j�  Kqu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UR2GC_155_86sh:j�  j�  Kru}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j#  j'  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UR2GC_155_86sh:j�  j�  Ksu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UR2GC_155_86sh:j�  j�  Ktu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j  j  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UR2GC_155_86sh:j�  j�  Kuu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UR2GC_155_86sh:j�  j�  Kvu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj�  Kuj�  j�  )�r�  (j�  j\  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UR2GC_170_88sh:j�  j�  Kwu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UR2GC_170_88sh:j�  j�  Kxu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j'  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UR2GC_170_88sh:j�  j�  Kyu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (jK  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UR2GC_170_88sh:j�  j�  Kzu}r�  bju  )�r 	  (jw  ]r	  ]r	  (KKKeajx  Njy  ]r	  j{  )�r	  j�  KK �Rr	  a}r	  (j~  j  U1�Rr	  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r	  (j�  j  j�  e}r		  bj�  ]r
	  j�  aj�  }r	  K K �UR2GC_170_88sh:j�  j�  K{u}r	  bju  )�r	  (jw  ]r	  ]r	  (KKKeajx  Njy  ]r	  j{  )�r	  j�  KK �Rr	  a}r	  (j~  j  U1�Rr	  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r	  (j#  j�  j�  e}r	  bj�  ]r	  j�  aj�  }r	  K K �UR2GC_170_88sh:j�  j�  K|u}r	  bju  )�r	  (jw  ]r	  ]r	  (KKeajx  Njy  ]r	  j{  )�r	  j�  KK �Rr	  a}r 	  (j~  j  U1�Rr!	  j�  K j�  �j�  K ubaj�  }r"	  (j�  Kj�  Kuj�  j�  )�r#	  (jK  j\  j  e}r$	  bj�  ]r%	  (j�  j?  ej�  }r&	  (K K�U
R2GC_103_4K K �U
R2GC_102_3uh:j�  j�  K}u}r'	  bju  )�r(	  (jw  ]r)	  ]r*	  (KKeajx  Njy  ]r+	  j{  )�r,	  j�  KK �Rr-	  a}r.	  (j~  j  U1�Rr/	  j�  K j�  �j�  K ubaj�  j"	  j�  j�  )�r0	  (j�  j�  j  e}r1	  bj�  ]r2	  (j�  j?  ej�  }r3	  (K K�U
R2GC_103_4K K �U
R2GC_102_3uh:j�  j�  K~u}r4	  bju  )�r5	  (jw  ]r6	  ]r7	  (KKeajx  Njy  ]r8	  j{  )�r9	  j�  KK �Rr:	  a}r;	  (j~  j  U1�Rr<	  j�  K j�  �j�  K ubaj�  j"	  j�  j�  )�r=	  (j#  j'  j  e}r>	  bj�  ]r?	  (j�  j?  ej�  }r@	  (K K�U
R2GC_103_4K K �U
R2GC_102_3uh:j�  j�  Ku}rA	  bju  )�rB	  (jw  ]rC	  ]rD	  (KKeajx  Njy  ]rE	  j{  )�rF	  j�  KK �RrG	  a}rH	  (j~  j  U1�RrI	  j�  K j�  �j�  K ubaj�  j"	  j�  j�  )�rJ	  (j�  j�  j  e}rK	  bj�  ]rL	  (j�  jg  ej�  }rM	  (K K�U
R2GC_103_4K K �U
R2GC_107_8uh:j�  j�  K�u}rN	  bju  )�rO	  (jw  ]rP	  ]rQ	  (KKeajx  Njy  ]rR	  j{  )�rS	  j�  KK �RrT	  a}rU	  (j~  j  U1�RrV	  j�  K j�  �j�  K ubaj�  j"	  j�  j�  )�rW	  (j  j  j  e}rX	  bj�  ]rY	  (j�  jg  ej�  }rZ	  (K K�U
R2GC_103_4K K �U
R2GC_107_8uh:j�  j�  K�u}r[	  bju  )�r\	  (jw  ]r]	  ]r^	  (KKeajx  Njy  ]r_	  j{  )�r`	  j�  KK �Rra	  a}rb	  (j~  j  U1�Rrc	  j�  K j�  �j�  K ubaj�  j"	  j�  j�  )�rd	  (j�  j�  j  e}re	  bj�  ]rf	  (j�  jg  ej�  }rg	  (K K�U
R2GC_103_4K K �U
R2GC_107_8uh:j�  j�  K�u}rh	  bju  )�ri	  (jw  ]rj	  ]rk	  (KKeajx  Njy  ]rl	  j{  )�rm	  j�  KK �Rrn	  a}ro	  (j~  j  U1�Rrp	  j�  K j�  �j�  K ubaj�  }rq	  j�  Ksj�  j�  )�rr	  (jK  j\  e}rs	  bj�  ]rt	  UFF1ru	  aj�  }rv	  K K �U
R2GC_104_5sh:j�  j�  K�u}rw	  bju  )�rx	  (jw  ]ry	  ]rz	  (KKeajx  Njy  ]r{	  j{  )�r|	  j�  KK �Rr}	  a}r~	  (j~  j  U1�Rr	  j�  K j�  �j�  K ubaj�  jq	  j�  j�  )�r�	  (j�  j�  e}r�	  bj�  ]r�	  ju	  aj�  }r�	  K K �U
R2GC_104_5sh:j�  j�  K�u}r�	  bju  )�r�	  (jw  ]r�	  ]r�	  (KKeajx  Njy  ]r�	  j{  )�r�	  j�  KK �Rr�	  a}r�	  (j~  j  U1�Rr�	  j�  K j�  �j�  K ubaj�  jq	  j�  j�  )�r�	  (j#  j'  e}r�	  bj�  ]r�	  (UFF2r�	  UFF3r�	  ej�  }r�	  (K K�U
R2GC_104_5K K �UR2GC_200_110uh:j�  j�  K�u}r�	  bju  )�r�	  (jw  ]r�	  ]r�	  (KKeajx  Njy  ]r�	  j{  )�r�	  j�  KK �Rr�	  a}r�	  (j~  j  U1�Rr�	  j�  K j�  �j�  K ubaj�  jq	  j�  j�  )�r�	  (j�  j�  e}r�	  bj�  ]r�	  ju	  aj�  }r�	  K K �U
R2GC_104_5sh:j�  j�  K�u}r�	  bju  )�r�	  (jw  ]r�	  ]r�	  (KKeajx  Njy  ]r�	  j{  )�r�	  j�  KK �Rr�	  a}r�	  (j~  j  U1�Rr�	  j�  K j�  �j�  K ubaj�  jq	  j�  j�  )�r�	  (j  j  e}r�	  bj�  ]r�	  ju	  aj�  }r�	  K K �U
R2GC_104_5sh:j�  j�  K�u}r�	  bju  )�r�	  (jw  ]r�	  ]r�	  (KKeajx  Njy  ]r�	  j{  )�r�	  j�  KK �Rr�	  a}r�	  (j~  j  U1�Rr�	  j�  K j�  �j�  K ubaj�  jq	  j�  j�  )�r�	  (j�  j�  e}r�	  bj�  ]r�	  (j�	  j�	  ej�  }r�	  (K K�U
R2GC_104_5K K �UR2GC_179_93uh:j�  j�  K�u}r�	  bju  )�r�	  (jw  ]r�	  ]r�	  Kaajx  Njy  ]r�	  j{  )�r�	  j(  K K�Rr�	  a}r�	  (j~  j  U2�Rr�	  j�  K j�  �j�  K ubaj�  }r�	  j�  Ksj�  j�  )�r�	  (j�  j�  e}r�	  bj�  ]r�	  (UVV2r�	  UVV3r�	  UVV4r�	  ej�  }r�	  K K �UR2GC_119_13sh:j�  j�  K�u}r�	  bju  )�r�	  (jw  ]r�	  (]r�	  Ka]r�	  Ka]r�	  Ka]r�	  Ka]r�	  Ka]r�	  Kaejx  Njy  ]r�	  j{  )�r�	  j(  K K�Rr�	  a}r�	  (j~  j  U2�Rr�	  j�  K j�  �j�  K ubaj�  }r�	  j�  Ksj�  j�  )�r�	  (j�  j�  e}r�	  bj�  ]r�	  (j�	  j�	  j�	  ej�  }r�	  K K�UR2GC_122_19sh:j�  j�  K�u}r�	  bju  )�r�	  (jw  ]r�	  ]r�	  Kaajx  Njy  ]r�	  j{  )�r�	  j(  K K�Rr�	  a}r�	  (j~  j  U2�Rr�	  j�  K j�  �j�  K ubaj�  }r�	  j�  Ksj�  j�  )�r�	  (j�  j�  e}r�	  bj�  ]r�	  (j�	  j�	  j�	  ej�  }r�	  K K�UR2GC_98_117sh:j�  j�  K�u}r�	  bju  )�r�	  (jw  ]r�	  ]r�	  Kaajx  Njy  ]r�	  j{  )�r�	  j(  K K�Rr�	  a}r�	  (j~  j  U2�Rr�	  j�  K j�  �j�  K ubaj�  }r�	  j�  Ksj�  j�  )�r�	  (j�  j�  e}r�	  bj�  ]r�	  (j�	  j�	  j�	  ej�  }r�	  K K �UR2GC_119_14sh:j�  j�  K�u}r�	  bju  )�r�	  (jw  ]r�	  ]r�	  Kaajx  Njy  ]r�	  j{  )�r�	  j(  K K�Rr 
  a}r
  (j~  j  U2�Rr
  j�  K j�  �j�  K ubaj�  }r
  (j  Kj�  Kuj�  j�  )�r
  (j�  j�  j�  e}r
  bj�  ]r
  UVVV2r
  aj�  }r
  K K �UR2GC_125_24sh:j�  j�  K�u}r	
  bju  )�r

  (jw  ]r
  ]r
  Kaajx  Njy  ]r
  j{  )�r
  j(  K K�Rr
  a}r
  (j~  j  U2�Rr
  j�  K j�  �j�  K ubaj�  }r
  (j  Kj�  Kuj�  j�  )�r
  (j�  j�  j�  e}r
  bj�  ]r
  j
  aj�  }r
  K K �UR2GC_125_25sh:j�  j�  K�u}r
  bju  )�r
  (jw  ]r
  ]r
  Kaajx  Njy  ]r
  j{  )�r
  j(  K K�Rr
  a}r
  (j~  j  U2�Rr
  j�  K j�  �j�  K ubaj�  }r 
  (j  Kj�  Kuj�  j�  )�r!
  (j�  j�  j�  e}r"
  bj�  ]r#
  j
  aj�  }r$
  K K �UR2GC_125_26sh:j�  j�  K�u}r%
  bju  )�r&
  (jw  ]r'
  ]r(
  Kaajx  Njy  ]r)
  j{  )�r*
  j(  K K�Rr+
  a}r,
  (j~  j  U2�Rr-
  j�  K j�  �j�  K ubaj�  }r.
  (j  Kj�  Kuj�  j�  )�r/
  (j�  j�  j�  e}r0
  bj�  ]r1
  j
  aj�  }r2
  K K �UR2GC_125_27sh:j�  j�  K�u}r3
  bju  )�r4
  (jw  ]r5
  ]r6
  Kaajx  Njy  ]r7
  j{  )�r8
  j(  K K�Rr9
  a}r:
  (j~  j  U2�Rr;
  j�  K j�  �j�  K ubaj�  }r<
  (j  Kj�  Kuj�  j�  )�r=
  (j�  j�  j�  e}r>
  bj�  ]r?
  j
  aj�  }r@
  K K �UR2GC_125_28sh:j�  j�  K�u}rA
  bju  )�rB
  (jw  ]rC
  ]rD
  Kaajx  Njy  ]rE
  j{  )�rF
  j(  K K�RrG
  a}rH
  (j~  j  U2�RrI
  j�  K j�  �j�  K ubaj�  }rJ
  (j  Kj�  Kuj�  j�  )�rK
  (j�  j�  j�  e}rL
  bj�  ]rM
  j
  aj�  }rN
  K K �UR2GC_125_29sh:j�  j�  K�u}rO
  bju  )�rP
  (jw  ]rQ
  (]rR
  Ka]rS
  Ka]rT
  Kaejx  Njy  ]rU
  j{  )�rV
  j(  K K�RrW
  a}rX
  (j~  j  U2�RrY
  j�  K j�  �j�  K ubaj�  }rZ
  (j�  Kj�  Kuj�  j�  )�r[
  (j�  j�  j  e}r\
  bj�  ]r]
  UVVV1r^
  aj�  }r_
  K K �UR2GC_129_48sh:j�  j�  K�u}r`
  bju  )�ra
  (jw  ]rb
  (]rc
  Ka]rd
  Ka]re
  Kaejx  Njy  ]rf
  j{  )�rg
  j(  K K�Rrh
  a}ri
  (j~  j  U2�Rrj
  j�  K j�  �j�  K ubaj�  }rk
  (j�  Kj�  Kuj�  j�  )�rl
  (j�  j�  j  e}rm
  bj�  ]rn
  j^
  aj�  }ro
  K K �UR2GC_129_49sh:j�  j�  K�u}rp
  bju  )�rq
  (jw  ]rr
  ]rs
  Kaajx  Njy  ]rt
  j{  )�ru
  j(  K K�Rrv
  a}rw
  (j~  j  U2�Rrx
  j�  K j�  �j�  K ubaj�  }ry
  (j�  Kj�  Kuj�  j�  )�rz
  (j�  j�  j�  e}r{
  bj�  ]r|
  jQ  aj�  }r}
  K K �UR2GC_120_15sh:j�  j�  K�u}r~
  bju  )�r
  (jw  ]r�
  ]r�
  Kaajx  Njy  ]r�
  j{  )�r�
  j(  K K�Rr�
  a}r�
  (j~  j  U2�Rr�
  j�  K j�  �j�  K ubaj�  }r�
  (j�  Kj�  Kuj�  j�  )�r�
  (j�  j�  j�  e}r�
  bj�  ]r�
  jQ  aj�  }r�
  K K �UR2GC_120_16sh:j�  j�  K�u}r�
  bju  )�r�
  (jw  ]r�
  ]r�
  Kaajx  Njy  ]r�
  j{  )�r�
  j(  K K�Rr�
  a}r�
  (j~  j  U2�Rr�
  j�  K j�  �j�  K ubaj�  }r�
  (j  Kj�  Kuj�  j�  )�r�
  (j�  j�  j�  j�  e}r�
  bj�  ]r�
  UVVVV7r�
  aj�  }r�
  K K �UR2GC_137_66sh:j�  j�  K�u}r�
  bju  )�r�
  (jw  ]r�
  ]r�
  (KKeajx  Njy  ]r�
  j{  )�r�
  j(  K K�Rr�
  a}r�
  (j~  j  U2�Rr�
  j�  K j�  �j�  K ubaj�  }r�
  (j  Kj�  Kuj�  j�  )�r�
  (j�  j�  j�  j�  e}r�
  bj�  ]r�
  j�
  aj�  }r�
  K K �UR2GC_137_72sh:j�  j�  K�u}r�
  bju  )�r�
  (jw  ]r�
  ]r�
  Kaajx  Njy  ]r�
  j{  )�r�
  j(  K K�Rr�
  a}r�
  (j~  j  U2�Rr�
  j�  K j�  �j�  K ubaj�  }r�
  (j  Kj�  Kuj�  j�  )�r�
  (j�  j�  j�  j�  e}r�
  bj�  ]r�
  j�
  aj�  }r�
  K K �UR2GC_137_67sh:j�  j�  K�u}r�
  bju  )�r�
  (jw  ]r�
  ]r�
  Kaajx  Njy  ]r�
  j{  )�r�
  j(  K K�Rr�
  a}r�
  (j~  j  U2�Rr�
  j�  K j�  �j�  K ubaj�  }r�
  (j  Kj�  Kuj�  j�  )�r�
  (j�  j�  j�  j�  e}r�
  bj�  ]r�
  j�
  aj�  }r�
  K K �UR2GC_137_68sh:j�  j�  K�u}r�
  bju  )�r�
  (jw  ]r�
  ]r�
  Kaajx  Njy  ]r�
  j{  )�r�
  j(  K K�Rr�
  a}r�
  (j~  j  U2�Rr�
  j�  K j�  �j�  K ubaj�  }r�
  (j  Kj�  Kuj�  j�  )�r�
  (j�  j�  j�  j�  e}r�
  bj�  ]r�
  j�
  aj�  }r�
  K K �UR2GC_137_69sh:j�  j�  K�u}r�
  bju  )�r�
  (jw  ]r�
  ]r�
  Kaajx  Njy  ]r�
  j{  )�r�
  j(  K K�Rr�
  a}r�
  (j~  j  U2�Rr�
  j�  K j�  �j�  K ubaj�  }r�
  (j  Kj�  Kuj�  j�  )�r�
  (j�  j�  j�  j�  e}r�
  bj�  ]r�
  j�
  aj�  }r�
  K K �UR2GC_137_70sh:j�  j�  K�u}r�
  bju  )�r�
  (jw  ]r�
  ]r�
  (KKeajx  Njy  ]r�
  j{  )�r�
  j(  K K�Rr�
  a}r�
  (j~  j  U2�Rr�
  j�  K j�  �j�  K ubaj�  }r�
  (j  Kj�  Kuj�  j�  )�r�
  (j�  j�  j�  j�  e}r�
  bj�  ]r�
  j�
  aj�  }r�
  K K �UR2GC_137_73sh:j�  j�  K�u}r�
  bju  )�r�
  (jw  ]r�
  ]r�
  Kaajx  Njy  ]r�
  j{  )�r�
  j(  K K�Rr�
  a}r�
  (j~  j  U2�Rr�
  j�  K j�  �j�  K ubaj�  }r�
  (j  Kj�  Kuj�  j�  )�r�
  (j�  j�  j�  j�  e}r�
  bj�  ]r�
  j�
  aj�  }r�
  K K �UR2GC_137_71sh:j�  j�  K�u}r�
  bju  )�r�
  (jw  ]r�
  ]r   Kaajx  Njy  ]r  j{  )�r  j(  KK�Rr  a}r  (j~  j  U2�Rr  j�  K j�  �j�  K ubaj�  }r  (j�  Kj  Kj�  Kuj�  j�  )�r  (j	  j�  j�  j�  e}r  bj�  ]r	  j�
  aj�  }r
  K K �UR2GC_127_36sh:j�  j�  K�u}r  bju  )�r  (jw  ]r  ]r  Kaajx  Njy  ]r  j{  )�r  j(  KK�Rr  a}r  (j~  j  U2�Rr  j�  K j�  �j�  K ubaj�  }r  (j�  Kj  Kj�  Kuj�  j�  )�r  (j	  j�  j�  j�  e}r  bj�  ]r  j�
  aj�  }r  K K �UR2GC_127_37sh:j�  j�  K�u}r  bju  )�r  (jw  ]r  ]r  Kaajx  Njy  ]r  j{  )�r  j(  KK�Rr  a}r   (j~  j  U2�Rr!  j�  K j�  �j�  K ubaj�  }r"  (j�  Kj  Kj�  Kuj�  j�  )�r#  (j	  j�  j�  j�  e}r$  bj�  ]r%  j�
  aj�  }r&  K K �UR2GC_127_38sh:j�  j�  K�u}r'  bju  )�r(  (jw  ]r)  ]r*  Kaajx  Njy  ]r+  j{  )�r,  j(  KK�Rr-  a}r.  (j~  j  U2�Rr/  j�  K j�  �j�  K ubaj�  }r0  (j�  Kj  Kj�  Kuj�  j�  )�r1  (j	  j�  j�  j�  e}r2  bj�  ]r3  j�
  aj�  }r4  K K �UR2GC_127_39sh:j�  j�  K�u}r5  bju  )�r6  (jw  ]r7  ]r8  Kaajx  Njy  ]r9  j{  )�r:  j(  KK�Rr;  a}r<  (j~  j  U2�Rr=  j�  K j�  �j�  K ubaj�  }r>  (j�  Kj  Kj�  Kuj�  j�  )�r?  (j	  j�  j�  j�  e}r@  bj�  ]rA  j�
  aj�  }rB  K K �UR2GC_127_40sh:j�  j�  K�u}rC  bju  )�rD  (jw  ]rE  ]rF  Kaajx  Njy  ]rG  j{  )�rH  j(  KK�RrI  a}rJ  (j~  j  U2�RrK  j�  K j�  �j�  K ubaj�  }rL  (j�  Kj  Kj�  Kuj�  j�  )�rM  (j	  j�  j�  j�  e}rN  bj�  ]rO  j�
  aj�  }rP  K K �UR2GC_127_41sh:j�  j�  K�u}rQ  bju  )�rR  (jw  ]rS  ]rT  Kaajx  Njy  ]rU  j{  )�rV  j(  K K�RrW  a}rX  (j~  j  U2�RrY  j�  K j�  �j�  K ubaj�  }rZ  (j�  Kj  Kj�  Kuj�  j�  )�r[  (j�  j�  j�  j  e}r\  bj�  ]r]  j�
  aj�  }r^  K K �UR2GC_133_56sh:j�  j�  K�u}r_  bju  )�r`  (jw  ]ra  ]rb  Kaajx  Njy  ]rc  j{  )�rd  j(  K K�Rre  a}rf  (j~  j  U2�Rrg  j�  K j�  �j�  K ubaj�  }rh  (j�  Kj  Kj�  Kuj�  j�  )�ri  (j�  j�  j�  j  e}rj  bj�  ]rk  j�
  aj�  }rl  K K �UR2GC_133_57sh:j�  j�  K�u}rm  bju  )�rn  (jw  ]ro  ]rp  Kaajx  Njy  ]rq  j{  )�rr  j(  K K�Rrs  a}rt  (j~  j  U2�Rru  j�  K j�  �j�  K ubaj�  }rv  (j�  Kj  Kj�  Kuj�  j�  )�rw  (j�  j�  j�  j  e}rx  bj�  ]ry  j�
  aj�  }rz  K K �UR2GC_133_58sh:j�  j�  K�u}r{  bju  )�r|  (jw  ]r}  ]r~  Kaajx  Njy  ]r  j{  )�r�  j(  K K�Rr�  a}r�  (j~  j  U2�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  j  e}r�  bj�  ]r�  j�
  aj�  }r�  K K �UR2GC_133_59sh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j(  K K�Rr�  a}r�  (j~  j  U2�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  j  e}r�  bj�  ]r�  j�
  aj�  }r�  K K �UR2GC_133_60sh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j(  K K�Rr�  a}r�  (j~  j  U2�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  j  e}r�  bj�  ]r�  j�
  aj�  }r�  K K �UR2GC_133_61sh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  (j{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubej�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  j�  e}r�  bj�  ]r�  (UVVVV1r�  j�
  ej�  }r�  (K K�UR2GC_128_42KK �UR2GC_126_30uh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  (j{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubej�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  j�  e}r�  bj�  ]r�  (j�  j�
  ej�  }r�  (K K�UR2GC_128_43KK �UR2GC_126_31uh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  (j{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubej�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  j�  e}r�  bj�  ]r�  (j�  j�
  ej�  }r�  (K K�UR2GC_128_44KK �UR2GC_126_32uh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  (j{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubej�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  j�  e}r�  bj�  ]r�  (j�  j�
  ej�  }r�  (K K�UR2GC_128_45KK �UR2GC_126_33uh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  (j{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubej�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  j�  e}r�  bj�  ]r�  (j�  j�
  ej�  }r�  (K K�UR2GC_128_46KK �UR2GC_126_34uh:j�  j�  K�u}r   bju  )�r  (jw  ]r  ]r  Kaajx  Njy  ]r  (j{  )�r  j�  K KK�Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r	  j�  K KK�Rr
  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubej�  }r  (j  Kj�  Kuj�  j�  )�r  (j�  j�  j�  j�  e}r  bj�  ]r  (j�  j�
  ej�  }r  (K K�UR2GC_128_47KK �UR2GC_126_35uh:j�  j�  K�u}r  bju  )�r  (jw  ]r  (]r  (KKe]r  (KKe]r  (KKeejx  Njy  ]r  j{  )�r  j(  K K�Rr  a}r  (j~  j  U2�Rr  j�  K j�  �j�  K ubaj�  }r  (j�  Kj�  Kuj�  j�  )�r  (j�  j�  j�  j�  e}r  bj�  ]r   j�
  aj�  }r!  K K �UR2GC_136_65sh:j�  j�  K�u}r"  bju  )�r#  (jw  ]r$  (]r%  Ka]r&  Ka]r'  Kaejx  Njy  ]r(  j{  )�r)  j(  KK�Rr*  a}r+  (j~  j  U2�Rr,  j�  K j�  �j�  K ubaj�  }r-  (j�  Kj�  Kuj�  j�  )�r.  (j	  j�  j�  j  e}r/  bj�  ]r0  j�
  aj�  }r1  K K �UR2GC_130_50sh:j�  j�  K�u}r2  bju  )�r3  (jw  ]r4  (]r5  Ka]r6  Ka]r7  Kaejx  Njy  ]r8  j{  )�r9  j(  KK�Rr:  a}r;  (j~  j  U2�Rr<  j�  K j�  �j�  K ubaj�  }r=  (j�  Kj�  Kuj�  j�  )�r>  (j	  j�  j�  j  e}r?  bj�  ]r@  j�
  aj�  }rA  K K �UR2GC_130_51sh:j�  j�  K�u}rB  bju  )�rC  (jw  ]rD  (]rE  Ka]rF  Ka]rG  Kaejx  Njy  ]rH  j{  )�rI  j(  K K�RrJ  a}rK  (j~  j  U2�RrL  j�  K j�  �j�  K ubaj�  }rM  (j�  Kj�  Kuj�  j�  )�rN  (j�  j�  j  j  e}rO  bj�  ]rP  j�
  aj�  }rQ  K K �UR2GC_134_62sh:j�  j�  K�u}rR  bju  )�rS  (jw  ]rT  (]rU  Ka]rV  Ka]rW  Kaejx  Njy  ]rX  j{  )�rY  j(  K K�RrZ  a}r[  (j~  j  U2�Rr\  j�  K j�  �j�  K ubaj�  }r]  (j�  Kj�  Kuj�  j�  )�r^  (j�  j�  j  j  e}r_  bj�  ]r`  j�
  aj�  }ra  K K �UR2GC_134_63sh:j�  j�  K�u}rb  bju  )�rc  (jw  ]rd  (]re  Ka]rf  Ka]rg  Kaejx  Njy  ]rh  j{  )�ri  j(  KK�Rrj  a}rk  (j~  j  U2�Rrl  j�  K j�  �j�  K ubaj�  }rm  (j�  Kj�  Kuj�  j�  )�rn  (j	  j	  j�  j�  e}ro  bj�  ]rp  j�
  aj�  }rq  K K �UR2GC_123_20sh:j�  j�  K�u}rr  bju  )�rs  (jw  ]rt  (]ru  Ka]rv  Ka]rw  Kaejx  Njy  ]rx  j{  )�ry  j(  KK�Rrz  a}r{  (j~  j  U2�Rr|  j�  K j�  �j�  K ubaj�  }r}  (j�  Kj�  Kuj�  j�  )�r~  (j	  j	  j�  j�  e}r  bj�  ]r�  j�
  aj�  }r�  K K �UR2GC_123_21sh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  (]r�  Ka]r�  Ka]r�  Kaejx  Njy  ]r�  (j{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubej�  }r�  (j�  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  j  e}r�  bj�  ]r�  (j�  j�
  ej�  }r�  (K K�UR2GC_131_52KK �UR2GC_132_54uh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  (]r�  Ka]r�  Ka]r�  Kaejx  Njy  ]r�  (j{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubej�  }r�  (j�  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  j  e}r�  bj�  ]r�  (j�  j�
  ej�  }r�  (K K�UR2GC_131_53KK �UR2GC_132_55uh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  (]r�  Ka]r�  Ka]r�  Kaejx  Njy  ]r�  j{  )�r�  j�  KKK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj�  Kuj�  j�  )�r�  (j	  j�  j�  j�  e}r�  bj�  ]r�  j�
  aj�  }r�  K K �UR2GC_124_22sh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  (]r�  Ka]r�  Ka]r�  Kaejx  Njy  ]r�  j{  )�r�  j�  KKK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj�  Kuj�  j�  )�r�  (j	  j�  j�  j�  e}r�  bj�  ]r�  j�
  aj�  }r�  K K �UR2GC_124_23sh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j(  K K�Rr�  a}r�  (j~  j  U2�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  j�  e}r�  bj�  ]r�  jD  aj�  }r�  K K �UR2GC_121_17sh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j(  K K�Rr�  a}r�  (j~  j  U2�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  j�  e}r�  bj�  ]r�  jD  aj�  }r�  K K �UR2GC_121_18sh:j�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  j�  j�  j�  ej�  }r�  (K K�UUVGC_186_49K K �UUVGC_185_44K K�UUVGC_186_49K K�UUVGC_185_44K K�UUVGC_185_44K K�UUVGC_186_49uh:UUVloopr�  j�  K�u}r�  bju  )�r�  (jw  j�  jx  Njy  ]r�  j{  )�r�  j�  K KK�Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  j�  j�  j�  ej�  }r�  (K K�UUVGC_186_49_1epsK K �UUVGC_185_44_1epsK K�UUVGC_186_49_1epsK K�UUVGC_185_44_1epsK K�UUVGC_185_44_1epsK K�UUVGC_186_49_1epsuh:U
UVloop1epsr   j�  K�u}r  bju  )�r  (jw  ]r  (]r  Ka]r  Ka]r  Ka]r  Kaejx  Njy  ]r  j{  )�r	  j�  K KK�Rr
  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  }r  j�  Ksj�  j�  )�r  (j�  j�  j�  e}r  bj�  ]r  (j�  j�  j�  j�  j�  j�  ej�  }r  (K K�UUVGC_186_50_1epsK K �UUVGC_185_45_1epsK K�UUVGC_186_50_1epsK K�UUVGC_185_45_1epsK K�UUVGC_185_45_1epsK K�UUVGC_186_50_1epsuh:U
UVloop1epsr  j�  K�u}r  bju  )�r  (jw  ]r  ]r  Kaajx  Njy  ]r  j{  )�r  j�  K KK�Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  }r  j�  Ksj�  j�  )�r  (j�  j�  j�  e}r  bj�  ]r  (j�  j�  j�  j�  j�  j�  ej�  }r   (K K�UUVGC_186_51_1epsK K �UUVGC_185_46_1epsK K�UUVGC_186_51_1epsK K�UUVGC_185_46_1epsK K�UUVGC_185_46_1epsK K�UUVGC_186_51_1epsuh:U
UVloop1epsr!  j�  K�u}r"  bju  )�r#  (jw  ]r$  ]r%  KRaajx  Njy  ]r&  j{  )�r'  j�  K KK�Rr(  a}r)  (j~  j  U1�Rr*  j�  K j�  �j�  K ubaj�  }r+  j�  Ksj�  j�  )�r,  (j�  j�  j�  e}r-  bj�  ]r.  (j�  j�  j�  j�  j�  j�  ej�  }r/  (K K�UUVGC_186_52_1epsK K �UUVGC_185_47_1epsK K�UUVGC_186_52_1epsK K�UUVGC_185_47_1epsK K�UUVGC_185_47_1epsK K�UUVGC_186_52_1epsuh:U
UVloop1epsr0  j�  K�u}r1  bju  )�r2  (jw  ]r3  ]r4  Kaajx  Njy  ]r5  j{  )�r6  j�  K KK�Rr7  a}r8  (j~  j  U1�Rr9  j�  K j�  �j�  K ubaj�  }r:  j�  Ksj�  j�  )�r;  (j�  j�  j�  e}r<  bj�  ]r=  (j�  j�  j�  j�  j�  j�  ej�  }r>  (K K�UUVGC_186_53K K �UUVGC_185_48K K�UUVGC_186_53K K�UUVGC_185_48K K�UUVGC_185_48K K�UUVGC_186_53uh:j�  j�  K�u}r?  bju  )�r@  (jw  j3  jx  Njy  ]rA  j{  )�rB  j�  K KK�RrC  a}rD  (j~  j  U1�RrE  j�  K j�  �j�  K ubaj�  j:  j�  j�  )�rF  (j�  j�  j�  e}rG  bj�  ]rH  (j�  j�  j�  j�  j�  j�  ej�  }rI  (K K�UUVGC_186_53_1epsK K �UUVGC_185_48_1epsK K�UUVGC_186_53_1epsK K�UUVGC_185_48_1epsK K�UUVGC_185_48_1epsK K�UUVGC_186_53_1epsuh:U
UVloop1epsrJ  j�  K�u}rK  bju  )�rL  (jw  ]rM  ]rN  Kaajx  Njy  ]rO  (j{  )�rP  (j�  J����K K�RrQ  j�  J����KK�RrR  e}rS  (j~  j  U1�RrT  j�  K j�  �j�  K ubj{  )�rU  (j�  J����K K�RrV  j�  J����KK�RrW  e}rX  (j~  j  U1�RrY  j�  K j�  �j�  K ubj{  )�rZ  (j�  J����K K�Rr[  j�  J����KK�Rr\  e}r]  (j~  j  U1�Rr^  j�  K j�  �j�  K ubj{  )�r_  (j�  J����K K�Rr`  j�  J����KK�Rra  e}rb  (j~  j  U1�Rrc  j�  K j�  �j�  K ubj{  )�rd  (j�  J����KK�Rre  j�  J����K K�Rrf  e}rg  (j~  j  U1�Rrh  j�  K j�  �j�  K ubj{  )�ri  (j�  J����KK�Rrj  j�  J����K K�Rrk  e}rl  (j~  j  U1�Rrm  j�  K j�  �j�  K ubj{  )�rn  (j�  J����K K�Rro  j�  J����KK�Rrp  e}rq  (j~  j  U1�Rrr  j�  K j�  �j�  K ubj{  )�rs  (j�  J����K K�Rrt  j�  J����KK�Rru  e}rv  (j~  j  U1�Rrw  j�  K j�  �j�  K ubj{  )�rx  (j�  J����K K�Rry  j�  J����KK�Rrz  e}r{  (j~  j  U1�Rr|  j�  K j�  �j�  K ubj{  )�r}  (j(  K K�Rr~  j(  KK�Rr  e}r�  (j~  j  U4�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j(  K K�Rr�  j(  KK�Rr�  e}r�  (j~  j  U4�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j(  K K�Rr�  j(  KK�Rr�  e}r�  (j~  j  U4�Rr�  j�  K j�  �j�  K ubej�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (KK �UUVGC_190_64KK�UUVGC_189_60KK�UUVGC_192_71KK�UUVGC_187_54KK �UUVGC_190_64KK�UUVGC_187_54uh:j�  j�  K�u}r�  bju  )�r�  (jw  jM  jx  Njy  ]r�  (j{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����KK�Rr�  j�  J����K K�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����KK�Rr�  j�  J����K K�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j(  K K�Rr�  j(  KK�Rr�  e}r�  (j~  j  U4�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j(  K K�Rr�  j(  KK�Rr�  e}r�  (j~  j  U4�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j(  K K�Rr�  j(  KK�Rr�  e}r�  (j~  j  U4�Rr�  j�  K j�  �j�  K ubej�  j�  j�  j�  )�r�  (j�  j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (KK �UUVGC_190_64_1epsKK�UUVGC_189_60_1epsKK�UUVGC_192_71_1epsKK�UUVGC_187_54_1epsKK �UUVGC_190_64_1epsKK�UUVGC_187_54_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  (]r�  Ka]r�  Ka]r�  Ka]r�  Ka]r�  Ka]r�  Kaejx  Njy  ]r�  (j{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����KK�Rr�  j�  J����K K�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����KK�Rr�  j�  J����K K�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r   (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j�  J����K K�Rr  j�  J����KK�Rr  e}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j�  J����K K�Rr  j�  J����KK�Rr	  e}r
  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j(  K K�Rr  j(  KK�Rr  e}r  (j~  j  U4�Rr  j�  K j�  �j�  K ubj{  )�r  (j(  K K�Rr  j(  KK�Rr  e}r  (j~  j  U4�Rr  j�  K j�  �j�  K ubj{  )�r  (j(  K K�Rr  j(  KK�Rr  e}r  (j~  j  U4�Rr  j�  K j�  �j�  K ubej�  }r  j�  Ksj�  j�  )�r  (j�  j�  j�  j�  e}r  bj�  ]r  (j�  j�  j�  ej�  }r  (KK�UUVGC_152_14_1epsKK�UUVGC_152_14_1epsuh:U
UVloop1epsr   j�  K�u}r!  bju  )�r"  (jw  ]r#  (]r$  Ka]r%  Ka]r&  Ka]r'  Kaejx  Njy  ]r(  (j{  )�r)  (j�  J����K K�Rr*  j�  J����KK�Rr+  e}r,  (j~  j  U1�Rr-  j�  K j�  �j�  K ubj{  )�r.  (j�  J����K K�Rr/  j�  J����KK�Rr0  e}r1  (j~  j  U1�Rr2  j�  K j�  �j�  K ubj{  )�r3  (j�  J����K K�Rr4  j�  J����KK�Rr5  e}r6  (j~  j  U1�Rr7  j�  K j�  �j�  K ubj{  )�r8  (j�  J����K K�Rr9  j�  J����KK�Rr:  e}r;  (j~  j  U1�Rr<  j�  K j�  �j�  K ubj{  )�r=  (j�  J����KK�Rr>  j�  J����K K�Rr?  e}r@  (j~  j  U1�RrA  j�  K j�  �j�  K ubj{  )�rB  (j�  J����KK�RrC  j�  J����K K�RrD  e}rE  (j~  j  U1�RrF  j�  K j�  �j�  K ubj{  )�rG  (j�  J����K K�RrH  j�  J����KK�RrI  e}rJ  (j~  j  U1�RrK  j�  K j�  �j�  K ubj{  )�rL  (j�  J����K K�RrM  j�  J����KK�RrN  e}rO  (j~  j  U1�RrP  j�  K j�  �j�  K ubj{  )�rQ  (j�  J����K K�RrR  j�  J����KK�RrS  e}rT  (j~  j  U1�RrU  j�  K j�  �j�  K ubj{  )�rV  (j(  K K�RrW  j(  KK�RrX  e}rY  (j~  j  U4�RrZ  j�  K j�  �j�  K ubj{  )�r[  (j(  K K�Rr\  j(  KK�Rr]  e}r^  (j~  j  U4�Rr_  j�  K j�  �j�  K ubj{  )�r`  (j(  K K�Rra  j(  KK�Rrb  e}rc  (j~  j  U4�Rrd  j�  K j�  �j�  K ubej�  }re  j�  Ksj�  j�  )�rf  (j�  j�  j�  j�  e}rg  bj�  ]rh  (j�  j�  j�  ej�  }ri  (KK�UUVGC_192_72_1epsKK �UUVGC_190_65_1epsKK �UUVGC_190_65_1epsKK�UUVGC_189_61_1epsuh:U
UVloop1epsrj  j�  K�u}rk  bju  )�rl  (jw  ]rm  ]rn  Kaajx  Njy  ]ro  (j{  )�rp  (j�  J����K K�Rrq  j�  J����KK�Rrr  e}rs  (j~  j  U1�Rrt  j�  K j�  �j�  K ubj{  )�ru  (j�  J����K K�Rrv  j�  J����KK�Rrw  e}rx  (j~  j  U1�Rry  j�  K j�  �j�  K ubj{  )�rz  (j�  J����K K�Rr{  j�  J����KK�Rr|  e}r}  (j~  j  U1�Rr~  j�  K j�  �j�  K ubj{  )�r  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����KK�Rr�  j�  J����K K�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����KK�Rr�  j�  J����K K�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j(  K K�Rr�  j(  KK�Rr�  e}r�  (j~  j  U4�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j(  K K�Rr�  j(  KK�Rr�  e}r�  (j~  j  U4�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j(  K K�Rr�  j(  KK�Rr�  e}r�  (j~  j  U4�Rr�  j�  K j�  �j�  K ubej�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K	K�UUVGC_150_10_1epsKK �UUVGC_147_6_1epsKK�UUVGC_151_12_1epsKK �UUVGC_148_8_1epsKK�UUVGC_148_9_1epsKK�UUVGC_147_6_1epsKK�UUVGC_188_58_1epsKK �UUVGC_147_6_1epsKK�UUVGC_147_6_1epsK	K �UUVGC_150_10_1epsKK�UUVGC_190_66_1epsKK�UUVGC_151_12_1epsKK �UUVGC_147_6_1epsKK�UUVGC_148_9_1epsK
K �UUVGC_151_12_1epsKK�UUVGC_147_6_1epsKK�UUVGC_147_6_1epsKK�UUVGC_147_6_1epsK K �UUVGC_148_9_1epsKK�UUVGC_188_58_1epsKK�UUVGC_148_8_1epsKK �UUVGC_191_69_1epsKK �UUVGC_151_12_1epsK
K�UUVGC_151_12_1epsKK�UUVGC_147_6_1epsKK �UUVGC_147_6_1epsK K�UUVGC_148_9_1epsKK �UUVGC_190_66_1epsK	K�UUVGC_150_10_1epsKK�UUVGC_187_55_1epsKK�UUVGC_147_6_1epsKK �UUVGC_148_9_1epsKK�UUVGC_147_6_1epsK K�UUVGC_148_9_1epsK
K�UUVGC_151_12_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  KRaajx  Njy  ]r�  (j{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����KK�Rr�  j�  J����K K�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����KK�Rr�  j�  J����K K�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr�  e}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j(  K K�Rr�  j(  KK�Rr�  e}r�  (j~  j  U4�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j(  K K�Rr�  j(  KK�Rr�  e}r�  (j~  j  U4�Rr�  j�  K j�  �j�  K ubj{  )�r�  (j(  K K�Rr�  j(  KK�Rr�  e}r�  (j~  j  U4�Rr�  j�  K j�  �j�  K ubej�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K	K�UUVGC_150_11_1epsKK �UUVGC_147_7_1epsKK�UUVGC_151_13_1epsKK �UUVGC_148_9_1epsKK�UUVGC_148_8_1epsKK�UUVGC_150_10_1epsKK�UUVGC_147_7_1epsKK�UUVGC_188_59_1epsKK �UUVGC_147_7_1epsKK�UUVGC_147_7_1epsK	K �UUVGC_150_11_1epsKK�UUVGC_192_73_1epsKK�UUVGC_151_13_1epsKK �UUVGC_147_7_1epsKK�UUVGC_148_8_1epsK
K �UUVGC_151_13_1epsKK�UUVGC_147_7_1epsKK�UUVGC_147_7_1epsKK�UUVGC_147_7_1epsK K �UUVGC_148_8_1epsKK�UUVGC_189_62_1epsKK�UUVGC_153_15_1epsKK �UUVGC_191_70_1epsKK �UUVGC_151_13_1epsK
K�UUVGC_151_13_1epsKK�UUVGC_147_7_1epsKK �UUVGC_147_7_1epsK K�UUVGC_148_8_1epsKK �UUVGC_190_67_1epsK	K�UUVGC_150_11_1epsKK�UUVGC_187_56_1epsKK�UUVGC_147_7_1epsKK �UUVGC_148_8_1epsKK�UUVGC_147_7_1epsK K�UUVGC_148_8_1epsK
K�UUVGC_151_13_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  (j{  )�r�  (j�  J����K K�Rr�  j�  J����KK�Rr   e}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j�  J����K K�Rr  j�  J����KK�Rr  e}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j�  J����K K�Rr	  j�  J����KK�Rr
  e}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j�  J����K K�Rr  j�  J����KK�Rr  e}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j�  J����KK�Rr  j�  J����K K�Rr  e}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j�  J����KK�Rr  j�  J����K K�Rr  e}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubj{  )�r  (j�  J����K K�Rr  j�  J����KK�Rr  e}r  (j~  j  U1�Rr   j�  K j�  �j�  K ubj{  )�r!  (j�  J����K K�Rr"  j�  J����KK�Rr#  e}r$  (j~  j  U1�Rr%  j�  K j�  �j�  K ubj{  )�r&  (j�  J����K K�Rr'  j�  J����KK�Rr(  e}r)  (j~  j  U1�Rr*  j�  K j�  �j�  K ubj{  )�r+  (j(  K K�Rr,  j(  KK�Rr-  e}r.  (j~  j  U4�Rr/  j�  K j�  �j�  K ubj{  )�r0  (j(  K K�Rr1  j(  KK�Rr2  e}r3  (j~  j  U4�Rr4  j�  K j�  �j�  K ubj{  )�r5  (j(  K K�Rr6  j(  KK�Rr7  e}r8  (j~  j  U4�Rr9  j�  K j�  �j�  K ubej�  }r:  j�  Ksj�  j�  )�r;  (j�  j�  j�  j�  e}r<  bj�  ]r=  (j�  j�  j�  ej�  }r>  (KK �UUVGC_190_68KK�UUVGC_189_63KK�UUVGC_192_74KK�UUVGC_187_57KK �UUVGC_190_68KK�UUVGC_187_57uh:j�  j�  K�u}r?  bju  )�r@  (jw  j�  jx  Njy  ]rA  (j{  )�rB  (j�  J����K K�RrC  j�  J����KK�RrD  e}rE  (j~  j  U1�RrF  j�  K j�  �j�  K ubj{  )�rG  (j�  J����K K�RrH  j�  J����KK�RrI  e}rJ  (j~  j  U1�RrK  j�  K j�  �j�  K ubj{  )�rL  (j�  J����K K�RrM  j�  J����KK�RrN  e}rO  (j~  j  U1�RrP  j�  K j�  �j�  K ubj{  )�rQ  (j�  J����K K�RrR  j�  J����KK�RrS  e}rT  (j~  j  U1�RrU  j�  K j�  �j�  K ubj{  )�rV  (j�  J����KK�RrW  j�  J����K K�RrX  e}rY  (j~  j  U1�RrZ  j�  K j�  �j�  K ubj{  )�r[  (j�  J����KK�Rr\  j�  J����K K�Rr]  e}r^  (j~  j  U1�Rr_  j�  K j�  �j�  K ubj{  )�r`  (j�  J����K K�Rra  j�  J����KK�Rrb  e}rc  (j~  j  U1�Rrd  j�  K j�  �j�  K ubj{  )�re  (j�  J����K K�Rrf  j�  J����KK�Rrg  e}rh  (j~  j  U1�Rri  j�  K j�  �j�  K ubj{  )�rj  (j�  J����K K�Rrk  j�  J����KK�Rrl  e}rm  (j~  j  U1�Rrn  j�  K j�  �j�  K ubj{  )�ro  (j(  K K�Rrp  j(  KK�Rrq  e}rr  (j~  j  U4�Rrs  j�  K j�  �j�  K ubj{  )�rt  (j(  K K�Rru  j(  KK�Rrv  e}rw  (j~  j  U4�Rrx  j�  K j�  �j�  K ubj{  )�ry  (j(  K K�Rrz  j(  KK�Rr{  e}r|  (j~  j  U4�Rr}  j�  K j�  �j�  K ubej�  }r~  j�  Ksj�  j�  )�r  (j�  j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (KK�UUVGC_187_57_1epsKK �UUVGC_190_68_1epsKK �UUVGC_190_68_1epsKK�UUVGC_187_57_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_182_40sh:j�  j�  K�u}r�  bju  )�r�  (jw  j�  jx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_182_40_1epssh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj�  Kuj�  j�  )�r�  (j#  j'  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_209_104sh:j�  j�  K�u}r�  bju  )�r�  (jw  j�  jx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j#  j'  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_209_104_1epssh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�UUVGC_178_36K K �UUVGC_176_32uh:j�  j�  K�u}r�  bju  )�r�  (jw  j�  jx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�UUVGC_178_36_1epsK K �UUVGC_176_32_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�UUVGC_177_35_1epsK K �UUVGC_175_31_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j  Kj�  Kuj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�UUVGC_177_33K K �UUVGC_175_29uh:j�  j�  K�u}r�  bju  )�r�  (jw  j�  jx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�UUVGC_177_33_1epsK K �UUVGC_175_29_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r   j�  KK �Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  }r  (j  Kj�  Kuj�  j�  )�r  (j�  j�  j�  e}r  bj�  ]r  (j�  j�  ej�  }r  (K K�UUVGC_177_34_1epsK K �UUVGC_175_30_1epsuh:U
UVloop1epsr	  j�  K�u}r
  bju  )�r  (jw  ]r  ]r  (KKKeajx  Njy  ]r  j{  )�r  j�  KK �Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r  (j�  j�  j�  e}r  bj�  ]r  (j�  j�  ej�  }r  (K K�UUVGC_177_35_1epsK K �UUVGC_175_31_1epsuh:U
UVloop1epsr  j�  K�u}r  bju  )�r  (jw  ]r  ]r  (KKeajx  Njy  ]r  j{  )�r  j�  KK �Rr  a}r  (j~  j  U1�Rr   j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r!  (j�  j�  j�  e}r"  bj�  ]r#  (j�  j�  ej�  }r$  (K K�UUVGC_177_33K K �UUVGC_175_29uh:j�  j�  K�u}r%  bju  )�r&  (jw  j  jx  Njy  ]r'  j{  )�r(  j�  KK �Rr)  a}r*  (j~  j  U1�Rr+  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r,  (j�  j�  j�  e}r-  bj�  ]r.  (j�  j�  ej�  }r/  (K K�UUVGC_177_33_1epsK K �UUVGC_175_29_1epsuh:U
UVloop1epsr0  j�  K�u}r1  bju  )�r2  (jw  ]r3  ]r4  (KKeajx  Njy  ]r5  j{  )�r6  j�  KK �Rr7  a}r8  (j~  j  U1�Rr9  j�  K j�  �j�  K ubaj�  j  j�  j�  )�r:  (j�  j�  j�  e}r;  bj�  ]r<  (j�  j�  ej�  }r=  (K K�UUVGC_177_34_1epsK K �UUVGC_175_30_1epsuh:U
UVloop1epsr>  j�  K�u}r?  bju  )�r@  (jw  ]rA  ]rB  (KKeajx  Njy  ]rC  j{  )�rD  j�  KK �RrE  a}rF  (j~  j  U1�RrG  j�  K j�  �j�  K ubaj�  }rH  (j  Kj�  Kuj�  j�  )�rI  (j#  j'  j�  e}rJ  bj�  ]rK  (j�  j�  ej�  }rL  (K K�UUVGC_199_85K K �UUVGC_197_81uh:j�  j�  K�u}rM  bju  )�rN  (jw  jA  jx  Njy  ]rO  j{  )�rP  j�  KK �RrQ  a}rR  (j~  j  U1�RrS  j�  K j�  �j�  K ubaj�  jH  j�  j�  )�rT  (j#  j'  j�  e}rU  bj�  ]rV  (j�  j�  ej�  }rW  (K K�UUVGC_199_85_1epsK K �UUVGC_197_81_1epsuh:U
UVloop1epsrX  j�  K�u}rY  bju  )�rZ  (jw  ]r[  ]r\  (KKeajx  Njy  ]r]  j{  )�r^  j�  KK �Rr_  a}r`  (j~  j  U1�Rra  j�  K j�  �j�  K ubaj�  }rb  (j  Kj�  Kuj�  j�  )�rc  (jK  j'  j�  e}rd  bj�  ]re  (j�  j�  ej�  }rf  (K K�UUVGC_198_82K K �UUVGC_196_78uh:j�  j�  K�u}rg  bju  )�rh  (jw  j[  jx  Njy  ]ri  j{  )�rj  j�  KK �Rrk  a}rl  (j~  j  U1�Rrm  j�  K j�  �j�  K ubaj�  jb  j�  j�  )�rn  (jK  j'  j�  e}ro  bj�  ]rp  (j�  j�  ej�  }rq  (K K�UUVGC_198_82_1epsK K �UUVGC_196_78_1epsuh:U
UVloop1epsrr  j�  K�u}rs  bju  )�rt  (jw  ]ru  ]rv  (KKKeajx  Njy  ]rw  j{  )�rx  j�  KK �Rry  a}rz  (j~  j  U1�Rr{  j�  K j�  �j�  K ubaj�  }r|  (j  Kj�  Kuj�  j�  )�r}  (jK  j'  j�  e}r~  bj�  ]r  (j�  j�  ej�  }r�  (K K�UUVGC_198_84_1epsK K �UUVGC_196_80_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j  Kj�  Kuj�  j�  )�r�  (jK  j'  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�UUVGC_198_83_1epsK K �UUVGC_196_79_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  jb  j�  j�  )�r�  (j#  j\  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�UUVGC_198_82K K �UUVGC_196_78uh:j�  j�  K�u}r�  bju  )�r�  (jw  j�  jx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  jb  j�  j�  )�r�  (j#  j\  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�UUVGC_198_82_1epsK K �UUVGC_196_78_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j|  j�  j�  )�r�  (j#  j\  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�UUVGC_198_84_1epsK K �UUVGC_196_80_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j#  j\  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  (K K�UUVGC_198_83_1epsK K �UUVGC_196_79_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj�  Kuj�  j�  )�r�  (jK  j\  j	  e}r�  bj�  ]r�  (j�  j�  UFFV4r�  ej�  }r�  (K K�UUVGC_139_2_1epsK K �UUVGC_156_18_1epsK K�UUVGC_139_2_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j	  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_139_2_1epsK K �UUVGC_156_18_1epsK K�UUVGC_139_2_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  (j�  Kj�  Kuj�  j�  )�r�  (j#  j'  j	  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_194_76K K�UUVGC_194_76uh:j�  j�  K�u}r�  bju  )�r�  (jw  j�  jx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j#  j'  j	  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_194_76_1epsK K �UUVGC_156_18_1epsK K�UUVGC_194_76_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r   ]r  (KKeajx  Njy  ]r  j{  )�r  j�  KK �Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  }r  (j�  Kj�  Kuj�  j�  )�r  (j�  j�  j	  e}r	  bj�  ]r
  (j�  j�  j�  ej�  }r  (K K�UUVGC_141_3_1epsK K �UUVGC_154_16_1epsK K�UUVGC_141_3_1epsuh:U
UVloop1epsr  j�  K�u}r  bju  )�r  (jw  ]r  ]r  (KKeajx  Njy  ]r  j{  )�r  j�  KK �Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  j  j�  j�  )�r  (j  j  j	  e}r  bj�  ]r  (j�  j�  j�  ej�  }r  (K K�UUVGC_141_3_1epsK K �UUVGC_154_16_1epsK K�UUVGC_141_3_1epsuh:U
UVloop1epsr  j�  K�u}r  bju  )�r  (jw  ]r  ]r  (KKeajx  Njy  ]r  j{  )�r   j�  KK �Rr!  a}r"  (j~  j  U1�Rr#  j�  K j�  �j�  K ubaj�  }r$  (j�  Kj�  Kuj�  j�  )�r%  (j�  j�  j	  e}r&  bj�  ]r'  (j�  j�  j�  ej�  }r(  (K K�UUVGC_173_27K K�UUVGC_173_27uh:j�  j�  K�u}r)  bju  )�r*  (jw  j  jx  Njy  ]r+  j{  )�r,  j�  KK �Rr-  a}r.  (j~  j  U1�Rr/  j�  K j�  �j�  K ubaj�  j$  j�  j�  )�r0  (j�  j�  j	  e}r1  bj�  ]r2  (j�  j�  j�  ej�  }r3  (K K�UUVGC_173_27_1epsK K �UUVGC_154_16_1epsK K�UUVGC_173_27_1epsuh:U
UVloop1epsr4  j�  K�u}r5  bju  )�r6  (jw  ]r7  ]r8  Kaajx  Njy  ]r9  j{  )�r:  j�  KKK �Rr;  a}r<  (j~  j  U1�Rr=  j�  K j�  �j�  K ubaj�  }r>  j�  Ksj�  j�  )�r?  (jK  j\  j�  e}r@  bj�  ]rA  (j�  j�  j�  ej�  }rB  (K K�UUVGC_157_19_1epsK K�UUVGC_157_19_1epsuh:U
UVloop1epsrC  j�  K�u}rD  bju  )�rE  (jw  ]rF  (]rG  Ka]rH  Ka]rI  Ka]rJ  Kaejx  Njy  ]rK  j{  )�rL  j�  KKK �RrM  a}rN  (j~  j  U1�RrO  j�  K j�  �j�  K ubaj�  }rP  j�  Ksj�  j�  )�rQ  (jK  j\  j�  e}rR  bj�  ]rS  (j�  j�  j�  ej�  }rT  (K K�UUVGC_157_20_1epsK K�UUVGC_157_20_1epsuh:U
UVloop1epsrU  j�  K�u}rV  bju  )�rW  (jw  ]rX  ]rY  Kaajx  Njy  ]rZ  j{  )�r[  j�  KKK �Rr\  a}r]  (j~  j  U1�Rr^  j�  K j�  �j�  K ubaj�  }r_  j�  Ksj�  j�  )�r`  (jK  j\  j�  e}ra  bj�  ]rb  (j�  j�  j�  ej�  }rc  (K K�UUVGC_157_21_1epsK K�UUVGC_157_21_1epsuh:U
UVloop1epsrd  j�  K�u}re  bju  )�rf  (jw  ]rg  ]rh  KRaajx  Njy  ]ri  j{  )�rj  j�  KKK �Rrk  a}rl  (j~  j  U1�Rrm  j�  K j�  �j�  K ubaj�  }rn  j�  Ksj�  j�  )�ro  (jK  j\  j�  e}rp  bj�  ]rq  (j�  j�  j�  ej�  }rr  (K K�UUVGC_157_22_1epsK K�UUVGC_157_22_1epsuh:U
UVloop1epsrs  j�  K�u}rt  bju  )�ru  (jw  ]rv  ]rw  (KKeajx  Njy  ]rx  j{  )�ry  j�  KKK �Rrz  a}r{  (j~  j  U1�Rr|  j�  K j�  �j�  K ubaj�  }r}  j�  Ksj�  j�  )�r~  (jK  j\  j�  e}r  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_23_1epsK K �UUVGC_155_17_1epsK K�UUVGC_157_23_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j>  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_19_1epsK K�UUVGC_157_19_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  (]r�  Ka]r�  Ka]r�  Ka]r�  Kaejx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  jP  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_20_1epsK K�UUVGC_157_20_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j}  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_23_1epsK K �UUVGC_155_17_1epsK K�UUVGC_157_23_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j_  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_21_1epsK K�UUVGC_157_21_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  KRaajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  jn  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_22_1epsK K�UUVGC_157_22_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j>  j�  j�  )�r�  (j#  j'  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_19_1epsK K�UUVGC_157_19_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  (]r�  Ka]r�  Ka]r�  Ka]r�  Kaejx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  jP  j�  j�  )�r�  (j#  j'  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_20_1epsK K�UUVGC_157_20_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j_  j�  j�  )�r�  (j#  j'  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_21_1epsK K�UUVGC_157_21_1epsuh:U
UVloop1epsr�  j�  K�u}r�  bju  )�r�  (jw  ]r�  ]r�  KRaajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r   (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  jn  j�  j�  )�r  (j#  j'  j�  e}r  bj�  ]r  (j�  j�  j�  ej�  }r  (K K�UUVGC_157_22_1epsK K�UUVGC_157_22_1epsuh:U
UVloop1epsr  j�  K�u}r  bju  )�r  (jw  ]r	  ]r
  (KKeajx  Njy  ]r  j{  )�r  j�  KKK �Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  }r  j�  Ksj�  j�  )�r  (j#  j'  j�  e}r  bj�  ]r  (j�  j�  j�  ej�  }r  (K K�UUVGC_195_77K K�UUVGC_195_77uh:j�  j�  K�u}r  bju  )�r  (jw  j	  jx  Njy  ]r  j{  )�r  j�  KKK �Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  j  j�  j�  )�r  (j#  j'  j�  e}r  bj�  ]r  (j�  j�  j�  ej�  }r  (K K�UUVGC_195_77_1epsK K �UUVGC_155_17_1epsK K�UUVGC_195_77_1epsuh:U
UVloop1epsr   j�  K�u}r!  bju  )�r"  (jw  ]r#  ]r$  Kaajx  Njy  ]r%  j{  )�r&  j�  KKK �Rr'  a}r(  (j~  j  U1�Rr)  j�  K j�  �j�  K ubaj�  j>  j�  j�  )�r*  (j�  j�  j�  e}r+  bj�  ]r,  (j�  j�  j�  ej�  }r-  (K K�UUVGC_157_19_1epsK K�UUVGC_157_19_1epsuh:U
UVloop1epsr.  j�  K�u}r/  bju  )�r0  (jw  ]r1  (]r2  Ka]r3  Ka]r4  Ka]r5  Kaejx  Njy  ]r6  j{  )�r7  j�  KKK �Rr8  a}r9  (j~  j  U1�Rr:  j�  K j�  �j�  K ubaj�  jP  j�  j�  )�r;  (j�  j�  j�  e}r<  bj�  ]r=  (j�  j�  j�  ej�  }r>  (K K�UUVGC_157_20_1epsK K�UUVGC_157_20_1epsuh:U
UVloop1epsr?  j�  K�u}r@  bju  )�rA  (jw  ]rB  ]rC  (KKeajx  Njy  ]rD  j{  )�rE  j�  KKK �RrF  a}rG  (j~  j  U1�RrH  j�  K j�  �j�  K ubaj�  j}  j�  j�  )�rI  (j�  j�  j�  e}rJ  bj�  ]rK  (j�  j�  j�  ej�  }rL  (K K�UUVGC_157_23_1epsK K �UUVGC_155_17_1epsK K�UUVGC_157_23_1epsuh:U
UVloop1epsrM  j�  K�u}rN  bju  )�rO  (jw  ]rP  ]rQ  Kaajx  Njy  ]rR  j{  )�rS  j�  KKK �RrT  a}rU  (j~  j  U1�RrV  j�  K j�  �j�  K ubaj�  j_  j�  j�  )�rW  (j�  j�  j�  e}rX  bj�  ]rY  (j�  j�  j�  ej�  }rZ  (K K�UUVGC_157_21_1epsK K�UUVGC_157_21_1epsuh:U
UVloop1epsr[  j�  M u}r\  bju  )�r]  (jw  ]r^  ]r_  KRaajx  Njy  ]r`  j{  )�ra  j�  KKK �Rrb  a}rc  (j~  j  U1�Rrd  j�  K j�  �j�  K ubaj�  jn  j�  j�  )�re  (j�  j�  j�  e}rf  bj�  ]rg  (j�  j�  j�  ej�  }rh  (K K�UUVGC_157_22_1epsK K�UUVGC_157_22_1epsuh:U
UVloop1epsri  j�  Mu}rj  bju  )�rk  (jw  ]rl  ]rm  Kaajx  Njy  ]rn  j{  )�ro  j�  KKK �Rrp  a}rq  (j~  j  U1�Rrr  j�  K j�  �j�  K ubaj�  j>  j�  j�  )�rs  (j  j  j�  e}rt  bj�  ]ru  (j�  j�  j�  ej�  }rv  (K K�UUVGC_157_19_1epsK K�UUVGC_157_19_1epsuh:U
UVloop1epsrw  j�  Mu}rx  bju  )�ry  (jw  ]rz  (]r{  Ka]r|  Ka]r}  Ka]r~  Kaejx  Njy  ]r  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  jP  j�  j�  )�r�  (j  j  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_20_1epsK K�UUVGC_157_20_1epsuh:U
UVloop1epsr�  j�  Mu}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j_  j�  j�  )�r�  (j  j  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_21_1epsK K�UUVGC_157_21_1epsuh:U
UVloop1epsr�  j�  Mu}r�  bju  )�r�  (jw  ]r�  ]r�  KRaajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  jn  j�  j�  )�r�  (j  j  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_22_1epsK K�UUVGC_157_22_1epsuh:U
UVloop1epsr�  j�  Mu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j}  j�  j�  )�r�  (j  j  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_23_1epsK K �UUVGC_155_17_1epsK K�UUVGC_157_23_1epsuh:U
UVloop1epsr�  j�  Mu}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j>  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_19_1epsK K�UUVGC_157_19_1epsuh:U
UVloop1epsr�  j�  Mu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_174_28K K�UUVGC_174_28uh:j�  j�  Mu}r�  bju  )�r�  (jw  j�  jx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_174_28_1epsK K �UUVGC_155_17_1epsK K�UUVGC_174_28_1epsuh:U
UVloop1epsr�  j�  M	u}r�  bju  )�r�  (jw  ]r�  (]r�  Ka]r�  Ka]r�  Ka]r�  Kaejx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  jP  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_20_1epsK K�UUVGC_157_20_1epsuh:U
UVloop1epsr�  j�  M
u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j_  j�  j�  )�r�  (j�  j�  j�  e}r�  bj�  ]r�  (j�  j�  j�  ej�  }r�  (K K�UUVGC_157_21_1epsK K�UUVGC_157_21_1epsuh:U
UVloop1epsr�  j�  Mu}r�  bju  )�r�  (jw  ]r�  ]r�  KRaajx  Njy  ]r�  j{  )�r�  j�  KKK �Rr   a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  jn  j�  j�  )�r  (j�  j�  j�  e}r  bj�  ]r  (j�  j�  j�  ej�  }r  (K K�UUVGC_157_22_1epsK K�UUVGC_157_22_1epsuh:U
UVloop1epsr  j�  Mu}r  bju  )�r	  (jw  ]r
  (]r  (KKe]r  (KKeejx  Njy  ]r  j{  )�r  j�  KK �Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  }r  (j�  Kj�  Kuj�  j�  )�r  (j�  j\  j�  e}r  bj�  ]r  j�  aj�  }r  K K �UUVGC_170_24_1epssh:U
UVloop1epsr  j�  Mu}r  bju  )�r  (jw  ]r  ]r  (KKKeajx  Njy  ]r  j{  )�r  j�  KK �Rr  a}r  (j~  j  U1�Rr   j�  K j�  �j�  K ubaj�  }r!  (j�  Kj�  Kuj�  j�  )�r"  (j�  j\  j�  e}r#  bj�  ]r$  j�  aj�  }r%  K K �UUVGC_170_25_1epssh:U
UVloop1epsr&  j�  Mu}r'  bju  )�r(  (jw  ]r)  (]r*  (KKe]r+  (KKeejx  Njy  ]r,  j{  )�r-  j�  KK �Rr.  a}r/  (j~  j  U1�Rr0  j�  K j�  �j�  K ubaj�  j  j�  j�  )�r1  (j  j�  j�  e}r2  bj�  ]r3  j�  aj�  }r4  K K �UUVGC_170_24_1epssh:U
UVloop1epsr5  j�  Mu}r6  bju  )�r7  (jw  ]r8  ]r9  (KKKeajx  Njy  ]r:  j{  )�r;  j�  KK �Rr<  a}r=  (j~  j  U1�Rr>  j�  K j�  �j�  K ubaj�  j!  j�  j�  )�r?  (j  j�  j�  e}r@  bj�  ]rA  j�  aj�  }rB  K K �UUVGC_170_25_1epssh:U
UVloop1epsrC  j�  Mu}rD  bju  )�rE  (jw  ]rF  ]rG  (KKeajx  Njy  ]rH  j{  )�rI  j�  KK �RrJ  a}rK  (j~  j  U1�RrL  j�  K j�  �j�  K ubaj�  }rM  (j�  Kj�  Kuj�  j�  )�rN  (j�  j'  j�  e}rO  bj�  ]rP  j�  aj�  }rQ  K K �UUVGC_201_87sh:j�  j�  Mu}rR  bju  )�rS  (jw  jF  jx  Njy  ]rT  j{  )�rU  j�  KK �RrV  a}rW  (j~  j  U1�RrX  j�  K j�  �j�  K ubaj�  jM  j�  j�  )�rY  (j�  j'  j�  e}rZ  bj�  ]r[  j�  aj�  }r\  K K �UUVGC_201_87_1epssh:U
UVloop1epsr]  j�  Mu}r^  bju  )�r_  (jw  ]r`  ]ra  (KKKeajx  Njy  ]rb  j{  )�rc  j�  KK �Rrd  a}re  (j~  j  U1�Rrf  j�  K j�  �j�  K ubaj�  j!  j�  j�  )�rg  (j�  j'  j�  e}rh  bj�  ]ri  j�  aj�  }rj  K K �UUVGC_170_25_1epssh:U
UVloop1epsrk  j�  Mu}rl  bju  )�rm  (jw  ]rn  ]ro  (KKeajx  Njy  ]rp  j{  )�rq  j�  KK �Rrr  a}rs  (j~  j  U1�Rrt  j�  K j�  �j�  K ubaj�  }ru  (j�  Kj�  Kuj�  j�  )�rv  (j�  j'  j�  e}rw  bj�  ]rx  j�  aj�  }ry  K K �UUVGC_201_88sh:j�  j�  Mu}rz  bju  )�r{  (jw  jn  jx  Njy  ]r|  j{  )�r}  j�  KK �Rr~  a}r  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  ju  j�  j�  )�r�  (j�  j'  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_201_88_1epssh:U
UVloop1epsr�  j�  Mu}r�  bju  )�r�  (jw  ]r�  (]r�  (KKe]r�  (KKeejx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j  j�  j�  )�r�  (jK  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_170_24_1epssh:U
UVloop1epsr�  j�  Mu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j!  j�  j�  )�r�  (jK  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_170_25_1epssh:U
UVloop1epsr�  j�  Mu}r�  bju  )�r�  (jw  ]r�  (]r�  (KKe]r�  (KKeejx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j  j�  j�  )�r�  (j�  j  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_170_24_1epssh:U
UVloop1epsr�  j�  Mu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j!  j�  j�  )�r�  (j�  j  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_170_25_1epssh:U
UVloop1epsr�  j�  Mu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  jM  j�  j�  )�r�  (j#  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_201_87sh:j�  j�  Mu}r�  bju  )�r�  (jw  j�  jx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  jM  j�  j�  )�r�  (j#  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_201_87_1epssh:U
UVloop1epsr�  j�  Mu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j!  j�  j�  )�r�  (j#  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_170_25_1epssh:U
UVloop1epsr�  j�  Mu}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  ju  j�  j�  )�r�  (j#  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_201_88sh:j�  j�  Mu}r�  bju  )�r�  (jw  j�  jx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  ju  j�  j�  )�r�  (j#  j�  j�  e}r�  bj�  ]r�  j�  aj�  }r�  K K �UUVGC_201_88_1epssh:U
UVloop1epsr�  j�  Mu}r   bju  )�r  (jw  ]r  ]r  (KKeajx  Njy  ]r  j{  )�r  j�  KK �Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  }r	  (j�  Kj�  Kuj�  j�  )�r
  (j#  j'  j  e}r  bj�  ]r  (j�  j?  ej�  }r  (K K�UUVGC_203_90K K �UUVGC_202_89uh:j�  j�  Mu}r  bju  )�r  (jw  j  jx  Njy  ]r  j{  )�r  j�  KK �Rr  a}r  (j~  j  U1�Rr  j�  K j�  �j�  K ubaj�  j	  j�  j�  )�r  (j#  j'  j  e}r  bj�  ]r  (j�  j?  ej�  }r  (K K�UUVGC_203_90_1epsK K �UUVGC_202_89_1epsuh:U
UVloop1epsr  j�  M u}r  bju  )�r  (jw  ]r  ]r  (KKeajx  Njy  ]r  j{  )�r  j�  KK �Rr   a}r!  (j~  j  U1�Rr"  j�  K j�  �j�  K ubaj�  }r#  (j�  Kj�  Kuj�  j�  )�r$  (j�  j�  j  e}r%  bj�  ]r&  (j�  jg  ej�  }r'  (K K�UUVGC_181_39K K �UUVGC_180_38uh:j�  j�  M!u}r(  bju  )�r)  (jw  j  jx  Njy  ]r*  j{  )�r+  j�  KK �Rr,  a}r-  (j~  j  U1�Rr.  j�  K j�  �j�  K ubaj�  j#  j�  j�  )�r/  (j�  j�  j  e}r0  bj�  ]r1  (j�  jg  ej�  }r2  (K K�UUVGC_181_39_1epsK K �UUVGC_180_38_1epsuh:U
UVloop1epsr3  j�  M"u}r4  bju  )�r5  (jw  ]r6  ]r7  (KKeajx  Njy  ]r8  j{  )�r9  j�  KK �Rr:  a}r;  (j~  j  U1�Rr<  j�  K j�  �j�  K ubaj�  }r=  j�  Ksj�  j�  )�r>  (jK  j\  e}r?  bj�  ]r@  UFF4rA  aj�  }rB  K K �UUVGC_138_1_1epssh:U
UVloop1epsrC  j�  M#u}rD  bju  )�rE  (jw  ]rF  ]rG  (KKeajx  Njy  ]rH  j{  )�rI  j�  KK �RrJ  a}rK  (j~  j  U1�RrL  j�  K j�  �j�  K ubaj�  j=  j�  j�  )�rM  (j�  j�  e}rN  bj�  ]rO  jA  aj�  }rP  K K �UUVGC_138_1_1epssh:U
UVloop1epsrQ  j�  M$u}rR  bju  )�rS  (jw  ]rT  ]rU  (KKeajx  Njy  ]rV  j{  )�rW  j�  KK �RrX  a}rY  (j~  j  U1�RrZ  j�  K j�  �j�  K ubaj�  }r[  j�  Ksj�  j�  )�r\  (j#  j'  e}r]  bj�  ]r^  (j�	  j�	  ej�  }r_  (K K�UUVGC_193_75K K �UUVGC_200_86uh:j�  j�  M%u}r`  bju  )�ra  (jw  jT  jx  Njy  ]rb  j{  )�rc  j�  KK �Rrd  a}re  (j~  j  U1�Rrf  j�  K j�  �j�  K ubaj�  j[  j�  j�  )�rg  (j#  j'  e}rh  bj�  ]ri  (j�	  j�	  ej�  }rj  (K K�UUVGC_193_75_1epsK K �UUVGC_200_86_1epsuh:U
UVloop1epsrk  j�  M&u}rl  bju  )�rm  (jw  ]rn  ]ro  (KKeajx  Njy  ]rp  j{  )�rq  j�  KK �Rrr  a}rs  (j~  j  U1�Rrt  j�  K j�  �j�  K ubaj�  j=  j�  j�  )�ru  (j�  j�  e}rv  bj�  ]rw  jA  aj�  }rx  K K �UUVGC_138_1_1epssh:U
UVloop1epsry  j�  M'u}rz  bju  )�r{  (jw  ]r|  ]r}  (KKeajx  Njy  ]r~  j{  )�r  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j=  j�  j�  )�r�  (j  j  e}r�  bj�  ]r�  jA  aj�  }r�  K K �UUVGC_138_1_1epssh:U
UVloop1epsr�  j�  M(u}r�  bju  )�r�  (jw  ]r�  ]r�  (KKeajx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  e}r�  bj�  ]r�  (j�	  j�	  ej�  }r�  (K K�UUVGC_172_26K K �UUVGC_179_37uh:j�  j�  M)u}r�  bju  )�r�  (jw  j�  jx  Njy  ]r�  j{  )�r�  j�  KK �Rr�  a}r�  (j~  j  U1�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  e}r�  bj�  ]r�  (j�	  j�	  ej�  }r�  (K K�UUVGC_172_26_1epsK K �UUVGC_179_37_1epsuh:U
UVloop1epsr�  j�  M*u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j(  K K�Rr�  a}r�  (j~  j  U2�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  e}r�  bj�  ]r�  (UVV1r�  UVV5r�  ej�  }r�  K K�UUVGC_184_42sh:UUVmassr�  j�  M+u}r�  bju  )�r�  (jw  j�  jx  Njy  ]r�  j{  )�r�  j(  K K�Rr�  a}r�  (j~  j  U2�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  K K�UUVGC_184_42_1epssh:U
UVmass1epsr�  j�  M,u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j(  K K�Rr�  a}r�  (j~  j  U2�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  K K �UUVGC_146_4_1epssh:U
UVmass1epsr�  j�  M-u}r�  bju  )�r�  (jw  ]r�  ]r�  KRaajx  Njy  ]r�  j{  )�r�  j(  K K�Rr�  a}r�  (j~  j  U2�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  K K �UUVGC_146_5_1epssh:U
UVmass1epsr�  j�  M.u}r�  bju  )�r�  (jw  ]r�  ]r�  Kaajx  Njy  ]r�  j{  )�r�  j(  K K�Rr�  a}r�  (j~  j  U2�Rr�  j�  K j�  �j�  K ubaj�  }r�  j�  Ksj�  j�  )�r�  (j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  K K�UUVGC_184_43sh:j�  j�  M/u}r�  bju  )�r�  (jw  j�  jx  Njy  ]r�  j{  )�r�  j(  K K�Rr�  a}r�  (j~  j  U2�Rr�  j�  K j�  �j�  K ubaj�  j�  j�  j�  )�r�  (j�  j�  e}r�  bj�  ]r�  (j�  j�  ej�  }r�  K K�UUVGC_184_43_1epssh:U
UVmass1epsr�  j�  M0u}r�  be}r�  bUperturbation_couplingsr�  ]r�  j�  aUref_dict_to1r�  }r�  Ucoupling_ordersr�  NUexpansion_orderr�  }r�  (j�  Kcj  Kj�  KcuUorder_hierarchyr   }r  (j�  Kj  Kj�  KuUcase_sensitiver  �j�  j�  )�r  (j	  j  j�  j�  j�  jx  j:  j�  j�  j�  j�  j�  j�  j
  j  j\  j�  j'  j�  j  j�  j�  j�  )�r  (j�  }r  hUxrr  j�  �jy  Kh:U j�  j0  j�  G        j�  j	  j�  K UYK j�  Uxrr  j�  j�  j�  �j�  Kj�  U j�  J?ML u}r  bj�  j  j�  e}r	  bj�  ]r
  (cDMsimp_s_spin1.object_library
Lorentz
r  )�r  }r  (U	structurer  UP(-1,1)*Gamma(-1,2,1)hju	  Uspinsr  ]r  (KKeubj  )�r  }r  (j  UProjM(2,1) + ProjP(2,1)r  hj�	  j  ]r  (KKeubj  )�r  }r  (j  UGP(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1) + P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)hj�	  j  ]r  (KKeubj  )�r  }r  (j  Ub-(P(-1,1)*Gamma(-1,2,1)) + P(-1,1)*Gamma(-1,2,-2)*ProjM(-2,1) + P(-1,1)*Gamma(-1,2,-2)*ProjP(-2,1)hjA  j  ]r  (KKeubj  )�r  }r  (j  UP(1,2)*P(2,2)hj�  j  ]r  (KKeubj  )�r  }r  (j  UMetric(1,2)r   hj�	  j  ]r!  (KKeubj  )�r"  }r#  (j  UP(-1,2)**2*Metric(1,2)hj�	  j  ]r$  (KKeubj  )�r%  }r&  (j  U-P(1,2)*P(2,2) - (3*P(-1,2)**2*Metric(1,2))/2.hj�	  j  ]r'  (KKeubj  )�r(  }r)  (j  U&P(1,2)*P(2,2) - P(-1,2)**2*Metric(1,2)hj�  j  ]r*  (KKeubj  )�r+  }r,  (j  U1hj�  j  ]r-  (J����J����Keubj  )�r.  }r/  (j  UP(3,2)hj.  j  ]r0  (J����J����Keubj  )�r1  }r2  (j  UP(3,3)hj/  j  ]r3  (J����J����Keubj  )�r4  }r5  (j  UP(3,2) + P(3,3)hj�  j  ]r6  (J����J����Keubj  )�r7  }r8  (j  U1hj�  j  ]r9  (KKKeubj  )�r:  }r;  (j  UGamma5(2,1)hUFFS1r<  j  ]r=  (KKKeubj  )�r>  }r?  (j  UIdentity(2,1)hj�  j  ]r@  (KKKeubj  )�rA  }rB  (j  U
ProjM(2,1)hj   j  ]rC  (KKKeubj  )�rD  }rE  (j  UProjM(2,1) - ProjP(2,1)hUFFS4rF  j  ]rG  (KKKeubj  )�rH  }rI  (j  U
ProjP(2,1)hj  j  ]rJ  (KKKeubj  )�rK  }rL  (j  j  hj  j  ]rM  (KKKeubj  )�rN  }rO  (j  UGamma(3,2,1)hj�  j  ]rP  (KKKeubj  )�rQ  }rR  (j  UGamma5(-1,1)*Gamma(3,2,-1)hj�  j  ]rS  (KKKeubj  )�rT  }rU  (j  UGamma(3,2,-1)*ProjM(-1,1)hj�  j  ]rV  (KKKeubj  )�rW  }rX  (j  UGamma(3,2,-1)*ProjP(-1,1)hj�  j  ]rY  (KKKeubj  )�rZ  }r[  (j  U7Gamma(3,2,-1)*ProjM(-1,1) - 2*Gamma(3,2,-1)*ProjP(-1,1)hjg  j  ]r\  (KKKeubj  )�r]  }r^  (j  U5Gamma(3,2,-1)*ProjM(-1,1) - Gamma(3,2,-1)*ProjP(-1,1)hj�  j  ]r_  (KKKeubj  )�r`  }ra  (j  U5Gamma(3,2,-1)*ProjM(-1,1) + Gamma(3,2,-1)*ProjP(-1,1)hj�  j  ]rb  (KKKeubj  )�rc  }rd  (j  U7Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)hj�  j  ]re  (KKKeubj  )�rf  }rg  (j  U7Gamma(3,2,-1)*ProjM(-1,1) + 4*Gamma(3,2,-1)*ProjP(-1,1)hj?  j  ]rh  (KKKeubj  )�ri  }rj  (j  UP(1,2) - P(1,3)hj�  j  ]rk  (KKKeubj  )�rl  }rm  (j  j   hjQ  j  ]rn  (KKKeubj  )�ro  }rp  (j  U8-(Epsilon(1,2,3,-1)*P(-1,1)) + Epsilon(1,2,3,-1)*P(-1,2)hj^
  j  ]rq  (KKKeubj  )�rr  }rs  (j  U8-(Epsilon(1,2,3,-1)*P(-1,2)) + Epsilon(1,2,3,-1)*P(-1,3)hj
  j  ]rt  (KKKeubj  )�ru  }rv  (j  UP(3,1)*Metric(1,2)hj�  j  ]rw  (KKKeubj  )�rx  }ry  (j  UP(3,2)*Metric(1,2)hj�  j  ]rz  (KKKeubj  )�r{  }r|  (j  UP(2,1)*Metric(1,3)hj�  j  ]r}  (KKKeubj  )�r~  }r  (j  UP(2,3)*Metric(1,3)hj�  j  ]r�  (KKKeubj  )�r�  }r�  (j  UP(1,2)*Metric(2,3)hj�  j  ]r�  (KKKeubj  )�r�  }r�  (j  UP(1,3)*Metric(2,3)hj�  j  ]r�  (KKKeubj  )�r�  }r�  (j  U{P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)hj7  j  ]r�  (KKKeubj  )�r�  }r�  (j  U1hj�  j  ]r�  (KKKKeubj  )�r�  }r�  (j  j   hjD  j  ]r�  (KKKKeubj  )�r�  }r�  (j  UEpsilon(1,2,3,4)hj�  j  ]r�  (KKKKeubj  )�r�  }r�  (j  UMetric(1,4)*Metric(2,3)hj�  j  ]r�  (KKKKeubj  )�r�  }r�  (j  UMetric(1,3)*Metric(2,4)hj�  j  ]r�  (KKKKeubj  )�r�  }r�  (j  UMetric(1,2)*Metric(3,4)hj�  j  ]r�  (KKKKeubj  )�r�  }r�  (j  UMMetric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)hj^  j  ]r�  (KKKKeubj  )�r�  }r�  (j  UUMetric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.hj�  j  ]r�  (KKKKeubj  )�r�  }r�  (j  UKMetric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)hj�
  j  ]r�  (KKKKeubeUgot_majoranasr�  NUconserved_charger�  c__builtin__
set
r�  ]r�  (UYj�  j�  e�Rr�  Ucoupling_orders_countertermsr�  }r�  Uparticle_dictr�  }r�  (Kj�  Kj\  Kj  Kj�  Kj�  Kj'  JAKL j�  Kj�  Kj�  Kj
  Kj�  Kj  Kj�  Kj�  Kj	  Kj  Kj�  Kj�  J����j�  J����j�  JIML j  J��v�j�  J��v�j�  J��v�j'  J��v�j�  J@ML j�  JAT� j�  JBT� jx  JCT� j:  JDT� j�  J����j�  J����jz  J?ML j  KRj�  J����j�  J����j�  J����j  J����j�  J����j  J����j�  J����j�  J����j#  J����j�  J����j�  J����j  J����jK  uUgauger�  ]r�  (K Kej�  }r�  (je  j`  �r�  ]r�  (h6)�r�  }r�  (hU�( (5*mdl_complexi*mdl_G__exp__2)/(12.*cmath.pi**2) - (mdl_complexi*mdl_G__exp__2*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(4.*cmath.pi**2) if mdl_MB else (mdl_complexi*mdl_G__exp__2)/(12.*cmath.pi**2) ) - (mdl_complexi*mdl_G__exp__2)/(12.*cmath.pi**2)h:hghUUVGC_172_26r�  h<Nh=j�  ubh6)�r�  }r�  (hU�( (-5*mdl_complexi*mdl_G__exp__3)/(12.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__3*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(4.*cmath.pi**2) if mdl_MB else -(mdl_complexi*mdl_G__exp__3)/(12.*cmath.pi**2) ) + (mdl_complexi*mdl_G__exp__3)/(12.*cmath.pi**2)h:hghUUVGC_174_28r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hT#  ( (5*mdl_complexi*mdl_G__exp__2*mdl_gAd31)/(24.*cmath.pi**2) - (mdl_complexi*mdl_G__exp__2*mdl_gAd31*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2) if mdl_MB else (mdl_complexi*mdl_G__exp__2*mdl_gAd31)/(24.*cmath.pi**2) ) - (mdl_complexi*mdl_G__exp__2*mdl_gAd31)/(24.*cmath.pi**2)h:hghUUVGC_175_29r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hT#  ( (5*mdl_complexi*mdl_G__exp__2*mdl_gAd33)/(12.*cmath.pi**2) - (mdl_complexi*mdl_G__exp__2*mdl_gAd33*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(4.*cmath.pi**2) if mdl_MB else (mdl_complexi*mdl_G__exp__2*mdl_gAd33)/(12.*cmath.pi**2) ) - (mdl_complexi*mdl_G__exp__2*mdl_gAd33)/(12.*cmath.pi**2)h:hghUUVGC_176_32r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hT%  ( (-5*mdl_complexi*mdl_G__exp__2*mdl_gVd31)/(24.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__2*mdl_gVd31*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2) if mdl_MB else -(mdl_complexi*mdl_G__exp__2*mdl_gVd31)/(24.*cmath.pi**2) ) + (mdl_complexi*mdl_G__exp__2*mdl_gVd31)/(24.*cmath.pi**2)h:hghUUVGC_177_33r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hT%  ( (-5*mdl_complexi*mdl_G__exp__2*mdl_gVd33)/(12.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__2*mdl_gVd33*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(4.*cmath.pi**2) if mdl_MB else -(mdl_complexi*mdl_G__exp__2*mdl_gVd33)/(12.*cmath.pi**2) ) + (mdl_complexi*mdl_G__exp__2*mdl_gVd33)/(12.*cmath.pi**2)h:hghUUVGC_178_36r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hT  ( (3*mdl_complexi*mdl_G__exp__2*mdl_MB)/(4.*cmath.pi**2) - (mdl_complexi*mdl_G__exp__2*mdl_MB*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(2.*cmath.pi**2) if mdl_MB else (mdl_complexi*mdl_G__exp__2*mdl_MB)/(12.*cmath.pi**2) ) - (mdl_complexi*mdl_G__exp__2*mdl_MB)/(12.*cmath.pi**2)h:hghUUVGC_179_37r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hUk( (mdl_complexi*mdl_G__exp__2*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2) if mdl_MB else 0 )h:hghUUVGC_184_42r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hUV(mdl_complexi*mdl_G__exp__2*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2)h:hghUUVGC_184_43r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hU_( -(mdl_G__exp__3*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2) if mdl_MB else 0 )h:hghUUVGC_185_44r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hUJ-(mdl_G__exp__3*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2)h:hghUUVGC_185_48r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hU^( (mdl_G__exp__3*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2) if mdl_MB else 0 )h:hghUUVGC_186_49r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hUI(mdl_G__exp__3*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2)h:hghUUVGC_186_53r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hUl( -(mdl_complexi*mdl_G__exp__4*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2) if mdl_MB else 0 )h:hghUUVGC_187_54r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hUW-(mdl_complexi*mdl_G__exp__4*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2)h:hghUUVGC_187_57r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hUl( -(mdl_complexi*mdl_G__exp__4*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2) if mdl_MB else 0 )h:hghUUVGC_189_60r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hUW-(mdl_complexi*mdl_G__exp__4*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2)h:hghUUVGC_189_63r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hUk( (mdl_complexi*mdl_G__exp__4*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2) if mdl_MB else 0 )h:hghUUVGC_190_64r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hUV(mdl_complexi*mdl_G__exp__4*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2)h:hghUUVGC_190_68r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hUk( (mdl_complexi*mdl_G__exp__4*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2) if mdl_MB else 0 )h:hghUUVGC_192_71r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hUV(mdl_complexi*mdl_G__exp__4*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(24.*cmath.pi**2)h:hghUUVGC_192_74r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hU�(mdl_complexi*mdl_G__exp__2)/(3.*cmath.pi**2) - (mdl_complexi*mdl_G__exp__2*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(4.*cmath.pi**2)h:hghUUVGC_193_75r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hU�-(mdl_complexi*mdl_G__exp__3)/(3.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__3*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(4.*cmath.pi**2)h:hghUUVGC_195_77r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hU�(mdl_complexi*mdl_G__exp__2*mdl_gAu31)/(6.*cmath.pi**2) - (mdl_complexi*mdl_G__exp__2*mdl_gAu31*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2)h:hghUUVGC_196_78r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hU�(mdl_complexi*mdl_G__exp__2*mdl_gAu33)/(3.*cmath.pi**2) - (mdl_complexi*mdl_G__exp__2*mdl_gAu33*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(4.*cmath.pi**2)h:hghUUVGC_197_81r�  h<Nh=je  j`  �ubh6)�r�  }r�  (hU�-(mdl_complexi*mdl_G__exp__2*mdl_gVu31)/(6.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__2*mdl_gVu31*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2)h:hghUUVGC_198_82r   h<Nh=je  j`  �ubh6)�r  }r  (hU�-(mdl_complexi*mdl_G__exp__2*mdl_gVu33)/(3.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__2*mdl_gVu33*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(4.*cmath.pi**2)h:hghUUVGC_199_85r  h<Nh=je  j`  �ubh6)�r  }r  (hU�(2*mdl_complexi*mdl_G__exp__2*mdl_MT)/(3.*cmath.pi**2) - (mdl_complexi*mdl_G__exp__2*mdl_MT*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(2.*cmath.pi**2)h:hghUUVGC_200_86r  h<Nh=je  j`  �ubeje  h3j`  �r  ]r  (h6)�r	  }r
  (hTF  ( (3*mdl_complexi*mdl_G__exp__2*mdl_yb)/(4.*cmath.pi**2*mdl_sqrt__2) - (mdl_complexi*mdl_G__exp__2*mdl_yb*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(2.*cmath.pi**2*mdl_sqrt__2) if mdl_MB else (mdl_complexi*mdl_G__exp__2*mdl_yb)/(12.*cmath.pi**2*mdl_sqrt__2) ) - (mdl_complexi*mdl_G__exp__2*mdl_yb)/(12.*cmath.pi**2*mdl_sqrt__2)h:hghUUVGC_182_40r  h<Nh=j  ubh6)�r  }r  (hT  ( (-3*mdl_G__exp__2*mdl_yb)/(4.*cmath.pi**2*mdl_sqrt__2) + (mdl_G__exp__2*mdl_yb*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(2.*cmath.pi**2*mdl_sqrt__2) if mdl_MB else -(mdl_G__exp__2*mdl_yb)/(12.*cmath.pi**2*mdl_sqrt__2) ) + (mdl_G__exp__2*mdl_yb)/(12.*cmath.pi**2*mdl_sqrt__2)h:hghUUVGC_183_41r  h<Nh=je  h3j`  �ubh6)�r  }r  (hU�( (13*mdl_G__exp__2*mdl_yb)/(24.*cmath.pi**2) - (3*mdl_G__exp__2*mdl_yb*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2) if mdl_MB else (mdl_G__exp__2*mdl_yb)/(24.*cmath.pi**2) ) - (mdl_G__exp__2*mdl_yb)/(24.*cmath.pi**2)h:hghUUVGC_204_91r  h<Nh=je  h3j`  �ubh6)�r  }r  (hUy(mdl_G__exp__2*mdl_yb)/(6.*cmath.pi**2) - (mdl_G__exp__2*mdl_yb*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2)h:hghUUVGC_204_92r  h<Nh=je  h3j`  �ubh6)�r  }r  (hU�( (-13*mdl_G__exp__2*mdl_yb)/(24.*cmath.pi**2) + (3*mdl_G__exp__2*mdl_yb*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2) if mdl_MB else -(mdl_G__exp__2*mdl_yb)/(24.*cmath.pi**2) ) + (mdl_G__exp__2*mdl_yb)/(24.*cmath.pi**2)h:hghUUVGC_205_94r  h<Nh=je  h3j`  �ubh6)�r  }r  (hUz-(mdl_G__exp__2*mdl_yb)/(6.*cmath.pi**2) + (mdl_G__exp__2*mdl_yb*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2)h:hghUUVGC_205_95r  h<Nh=je  h3j`  �ubh6)�r  }r  (hU�( (5*mdl_G__exp__2*mdl_yt)/(24.*cmath.pi**2) - (mdl_G__exp__2*mdl_yt*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2) if mdl_MB else (mdl_G__exp__2*mdl_yt)/(24.*cmath.pi**2) ) - (mdl_G__exp__2*mdl_yt)/(24.*cmath.pi**2)h:hghUUVGC_206_97r  h<Nh=je  h3j`  �ubh6)�r  }r  (hU{(mdl_G__exp__2*mdl_yt)/(2.*cmath.pi**2) - (3*mdl_G__exp__2*mdl_yt*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2)h:hghUUVGC_206_98r   h<Nh=je  h3j`  �ubh6)�r!  }r"  (hU�( (-5*mdl_G__exp__2*mdl_yt)/(24.*cmath.pi**2) + (mdl_G__exp__2*mdl_yt*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2) if mdl_MB else -(mdl_G__exp__2*mdl_yt)/(24.*cmath.pi**2) ) + (mdl_G__exp__2*mdl_yt)/(24.*cmath.pi**2)h:hghUUVGC_207_100r#  h<Nh=je  h3j`  �ubh6)�r$  }r%  (hU|-(mdl_G__exp__2*mdl_yt)/(2.*cmath.pi**2) + (3*mdl_G__exp__2*mdl_yt*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2)h:hghUUVGC_207_101r&  h<Nh=je  h3j`  �ubh6)�r'  }r(  (hU�(mdl_G__exp__2*mdl_yt*mdl_sqrt__2)/(3.*cmath.pi**2) - (mdl_G__exp__2*mdl_yt*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(2.*cmath.pi**2*mdl_sqrt__2)h:hghUUVGC_208_103r)  h<Nh=je  h3j`  �ubh6)�r*  }r+  (hU�(mdl_complexi*mdl_G__exp__2*mdl_yt*mdl_sqrt__2)/(3.*cmath.pi**2) - (mdl_complexi*mdl_G__exp__2*mdl_yt*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(2.*cmath.pi**2*mdl_sqrt__2)h:hghUUVGC_209_104r,  h<Nh=je  h3j`  �ubeh3je  �r-  ]r.  (h6)�r/  }r0  (hUD-(mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2)/(12.*cmath.pi**2*mdl_sw)h:hghU
R2GC_102_3r1  h<Nh=j-  ubh6)�r2  }r3  (hUC(mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_sw)/(36.*mdl_cw*cmath.pi**2)h:hghU
R2GC_103_4r4  h<Nh=h3je  �ubh6)�r5  }r6  (hUC(mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2)/(12.*cmath.pi**2*mdl_sw)h:hghU
R2GC_107_8r7  h<Nh=h3je  �ubh6)�r8  }r9  (hU>(mdl_ee__exp__2*mdl_complexi*mdl_G__exp__2)/(216.*cmath.pi**2)h:hghUR2GC_123_20r:  h<Nh=h3je  �ubh6)�r;  }r<  (hU=(mdl_ee__exp__2*mdl_complexi*mdl_G__exp__2)/(54.*cmath.pi**2)h:hghUR2GC_123_21r=  h<Nh=h3je  �ubh6)�r>  }r?  (hU7-(mdl_ee*mdl_complexi*mdl_G__exp__3)/(144.*cmath.pi**2)h:hghUR2GC_124_22r@  h<Nh=h3je  �ubh6)�rA  }rB  (hU5(mdl_ee*mdl_complexi*mdl_G__exp__3)/(72.*cmath.pi**2)h:hghUR2GC_124_23rC  h<Nh=h3je  �ubh6)�rD  }rE  (hU@-(mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVd33)/(72.*cmath.pi**2)h:hghUR2GC_127_36rF  h<Nh=h3je  �ubh6)�rG  }rH  (hU?(mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVu22)/(36.*cmath.pi**2)h:hghUR2GC_127_37rI  h<Nh=h3je  �ubh6)�rJ  }rK  (hU@-(mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVd11)/(72.*cmath.pi**2)h:hghUR2GC_127_38rL  h<Nh=h3je  �ubh6)�rM  }rN  (hU@-(mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVd22)/(72.*cmath.pi**2)h:hghUR2GC_127_39rO  h<Nh=h3je  �ubh6)�rP  }rQ  (hU?(mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVu33)/(36.*cmath.pi**2)h:hghUR2GC_127_40rR  h<Nh=h3je  �ubh6)�rS  }rT  (hU?(mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVu11)/(36.*cmath.pi**2)h:hghUR2GC_127_41rU  h<Nh=h3je  �ubh6)�rV  }rW  (hUp-(mdl_cw*mdl_ee*mdl_G__exp__2)/(48.*cmath.pi**2*mdl_sw) - (mdl_ee*mdl_G__exp__2*mdl_sw)/(48.*mdl_cw*cmath.pi**2)h:hghUR2GC_129_48rX  h<Nh=h3je  �ubh6)�rY  }rZ  (hUo(mdl_cw*mdl_ee*mdl_G__exp__2)/(48.*cmath.pi**2*mdl_sw) + (mdl_ee*mdl_G__exp__2*mdl_sw)/(48.*mdl_cw*cmath.pi**2)h:hghUR2GC_129_49r[  h<Nh=h3je  �ubh6)�r\  }r]  (hU�(mdl_cw*mdl_ee__exp__2*mdl_complexi*mdl_G__exp__2)/(288.*cmath.pi**2*mdl_sw) - (mdl_ee__exp__2*mdl_complexi*mdl_G__exp__2*mdl_sw)/(864.*mdl_cw*cmath.pi**2)h:hghUR2GC_130_50r^  h<Nh=h3je  �ubh6)�r_  }r`  (hU�(mdl_cw*mdl_ee__exp__2*mdl_complexi*mdl_G__exp__2)/(144.*cmath.pi**2*mdl_sw) - (5*mdl_ee__exp__2*mdl_complexi*mdl_G__exp__2*mdl_sw)/(432.*mdl_cw*cmath.pi**2)h:hghUR2GC_130_51ra  h<Nh=h3je  �ubh6)�rb  }rc  (hU�-(mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__3)/(192.*cmath.pi**2*mdl_sw) + (mdl_ee*mdl_complexi*mdl_G__exp__3*mdl_sw)/(576.*mdl_cw*cmath.pi**2)h:hghUR2GC_131_52rd  h<Nh=h3je  �ubh6)�re  }rf  (hU�(mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__3)/(192.*cmath.pi**2*mdl_sw) - (5*mdl_ee*mdl_complexi*mdl_G__exp__3*mdl_sw)/(576.*mdl_cw*cmath.pi**2)h:hghUR2GC_131_53rg  h<Nh=h3je  �ubh6)�rh  }ri  (hU�(3*mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__3)/(64.*cmath.pi**2*mdl_sw) + (3*mdl_ee*mdl_complexi*mdl_G__exp__3*mdl_sw)/(64.*mdl_cw*cmath.pi**2)h:hghUR2GC_132_54rj  h<Nh=h3je  �ubh6)�rk  }rl  (hU�(-3*mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__3)/(64.*cmath.pi**2*mdl_sw) - (3*mdl_ee*mdl_complexi*mdl_G__exp__3*mdl_sw)/(64.*mdl_cw*cmath.pi**2)h:hghUR2GC_132_55rm  h<Nh=h3je  �ubh6)�rn  }ro  (hT>  (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gAd33)/(96.*cmath.pi**2*mdl_sw) - (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVd33)/(96.*cmath.pi**2*mdl_sw) + (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gAd33*mdl_sw)/(96.*mdl_cw*cmath.pi**2) + (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVd33*mdl_sw)/(288.*mdl_cw*cmath.pi**2)h:hghUR2GC_133_56rp  h<Nh=h3je  �ubh6)�rq  }rr  (hTA  -(mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gAu22)/(96.*cmath.pi**2*mdl_sw) + (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVu22)/(96.*cmath.pi**2*mdl_sw) - (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gAu22*mdl_sw)/(96.*mdl_cw*cmath.pi**2) - (5*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVu22*mdl_sw)/(288.*mdl_cw*cmath.pi**2)h:hghUR2GC_133_57rs  h<Nh=h3je  �ubh6)�rt  }ru  (hT>  (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gAd11)/(96.*cmath.pi**2*mdl_sw) - (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVd11)/(96.*cmath.pi**2*mdl_sw) + (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gAd11*mdl_sw)/(96.*mdl_cw*cmath.pi**2) + (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVd11*mdl_sw)/(288.*mdl_cw*cmath.pi**2)h:hghUR2GC_133_58rv  h<Nh=h3je  �ubh6)�rw  }rx  (hT>  (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gAd22)/(96.*cmath.pi**2*mdl_sw) - (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVd22)/(96.*cmath.pi**2*mdl_sw) + (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gAd22*mdl_sw)/(96.*mdl_cw*cmath.pi**2) + (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVd22*mdl_sw)/(288.*mdl_cw*cmath.pi**2)h:hghUR2GC_133_59ry  h<Nh=h3je  �ubh6)�rz  }r{  (hTA  -(mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gAu33)/(96.*cmath.pi**2*mdl_sw) + (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVu33)/(96.*cmath.pi**2*mdl_sw) - (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gAu33*mdl_sw)/(96.*mdl_cw*cmath.pi**2) - (5*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVu33*mdl_sw)/(288.*mdl_cw*cmath.pi**2)h:hghUR2GC_133_60r|  h<Nh=h3je  �ubh6)�r}  }r~  (hTA  -(mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gAu11)/(96.*cmath.pi**2*mdl_sw) + (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVu11)/(96.*cmath.pi**2*mdl_sw) - (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gAu11*mdl_sw)/(96.*mdl_cw*cmath.pi**2) - (5*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_gVu11*mdl_sw)/(288.*mdl_cw*cmath.pi**2)h:hghUR2GC_133_61r  h<Nh=h3je  �ubh6)�r�  }r�  (hU�(mdl_ee__exp__2*mdl_complexi*mdl_G__exp__2)/(288.*cmath.pi**2) + (mdl_cw__exp__2*mdl_ee__exp__2*mdl_complexi*mdl_G__exp__2)/(192.*cmath.pi**2*mdl_sw__exp__2) + (5*mdl_ee__exp__2*mdl_complexi*mdl_G__exp__2*mdl_sw__exp__2)/(1728.*mdl_cw__exp__2*cmath.pi**2)h:hghUR2GC_134_62r�  h<Nh=h3je  �ubh6)�r�  }r�  (hT  -(mdl_ee__exp__2*mdl_complexi*mdl_G__exp__2)/(288.*cmath.pi**2) + (mdl_cw__exp__2*mdl_ee__exp__2*mdl_complexi*mdl_G__exp__2)/(192.*cmath.pi**2*mdl_sw__exp__2) + (17*mdl_ee__exp__2*mdl_complexi*mdl_G__exp__2*mdl_sw__exp__2)/(1728.*mdl_cw__exp__2*cmath.pi**2)h:hghUR2GC_134_63r�  h<Nh=h3je  �ubh6)�r�  }r�  (hUL(mdl_ee__exp__2*mdl_complexi*mdl_G__exp__2)/(96.*cmath.pi**2*mdl_sw__exp__2)h:hghUR2GC_136_65r�  h<Nh=h3je  �ubh6)�r�  }r�  (hU5(mdl_ee*mdl_complexi*mdl_G__exp__2)/(18.*cmath.pi**2)h:hghUR2GC_154_85r�  h<Nh=h3je  �ubh6)�r�  }r�  (hU5-(mdl_ee*mdl_complexi*mdl_G__exp__2)/(9.*cmath.pi**2)h:hghUR2GC_156_87r�  h<Nh=h3je  �ubh6)�r�  }r�  (hUH-(mdl_ee*mdl_complexi*mdl_G__exp__2)/(6.*cmath.pi**2*mdl_sw*mdl_sqrt__2)h:hghUR2GC_170_88r�  h<Nh=h3je  �ubh6)�r�  }r�  (hU5(mdl_ee*mdl_complexi*mdl_G__exp__2)/(18.*cmath.pi**2)h:hghUUVGC_139_2_1epsh<Nh=h3je  �ubh6)�r�  }r�  (hU6-(mdl_ee*mdl_complexi*mdl_G__exp__2)/(36.*cmath.pi**2)h:hghUUVGC_141_3_1epsh<Nh=h3je  �ubh6)�r�  }r�  (hU5(mdl_ee*mdl_complexi*mdl_G__exp__2)/(36.*cmath.pi**2)h:hghUUVGC_154_16_1epsh<Nh=h3je  �ubh6)�r�  }r�  (hU6-(mdl_ee*mdl_complexi*mdl_G__exp__2)/(18.*cmath.pi**2)h:hghUUVGC_156_18_1epsh<Nh=h3je  �ubh6)�r�  }r�  (hUH(mdl_ee*mdl_complexi*mdl_G__exp__2)/(24.*cmath.pi**2*mdl_sw*mdl_sqrt__2)h:hghUUVGC_170_24_1epsh<Nh=h3je  �ubh6)�r�  }r�  (hUI-(mdl_ee*mdl_complexi*mdl_G__exp__2)/(12.*cmath.pi**2*mdl_sw*mdl_sqrt__2)h:hghUUVGC_170_25_1epsh<Nh=h3je  �ubh6)�r�  }r�  (hU( (mdl_ee*mdl_complexi*mdl_G__exp__2)/(18.*cmath.pi**2) if mdl_MB else -(mdl_ee*mdl_complexi*mdl_G__exp__2)/(36.*cmath.pi**2) )h:hghUUVGC_173_27_1epsh<Nh=h3je  �ubh6)�r�  }r�  (hU�( (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2)/(12.*cmath.pi**2*mdl_sw) if mdl_MB else -(mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2)/(24.*cmath.pi**2*mdl_sw) ) + (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2)/(24.*cmath.pi**2*mdl_sw)h:hghUUVGC_180_38_1epsh<Nh=h3je  �ubh6)�r�  }r�  (hU�( (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_sw)/(36.*mdl_cw*cmath.pi**2) if mdl_MB else -(mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_sw)/(72.*mdl_cw*cmath.pi**2) ) + (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_sw)/(72.*mdl_cw*cmath.pi**2)h:hghUUVGC_181_39_1epsh<Nh=h3je  �ubh6)�r�  }r�  (hU5-(mdl_ee*mdl_complexi*mdl_G__exp__2)/(9.*cmath.pi**2)h:hghUUVGC_194_76_1epsh<Nh=h3je  �ubh6)�r�  }r�  (hU�( -(mdl_ee*mdl_complexi*mdl_G__exp__2)/(12.*cmath.pi**2*mdl_sw*mdl_sqrt__2) if mdl_MB else (mdl_ee*mdl_complexi*mdl_G__exp__2)/(24.*cmath.pi**2*mdl_sw*mdl_sqrt__2) )h:hghUUVGC_201_87_1epsh<Nh=h3je  �ubh6)�r�  }r�  (hUI-(mdl_ee*mdl_complexi*mdl_G__exp__2)/(12.*cmath.pi**2*mdl_sw*mdl_sqrt__2)h:hghUUVGC_201_88_1epsh<Nh=h3je  �ubh6)�r�  }r�  (hUC-(mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2)/(8.*cmath.pi**2*mdl_sw)h:hghUUVGC_202_89_1epsh<Nh=h3je  �ubh6)�r�  }r�  (hUC(mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_sw)/(24.*mdl_cw*cmath.pi**2)h:hghUUVGC_203_90_1epsh<Nh=h3je  �ubeh3je  j`  �r�  ]r�  (h6)�r�  }r�  (hT  ( (5*mdl_ee*mdl_complexi*mdl_G__exp__2)/(36.*cmath.pi**2) - (mdl_ee*mdl_complexi*mdl_G__exp__2*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(12.*cmath.pi**2) if mdl_MB else (mdl_ee*mdl_complexi*mdl_G__exp__2)/(36.*cmath.pi**2) ) - (mdl_ee*mdl_complexi*mdl_G__exp__2)/(36.*cmath.pi**2)h:hghUUVGC_173_27r�  h<Nh=j�  ubh6)�r�  }r�  (hTO  ( (5*mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2)/(24.*cmath.pi**2*mdl_sw) - (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2*mdl_sw) if mdl_MB else (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2)/(24.*cmath.pi**2*mdl_sw) ) - (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2)/(24.*cmath.pi**2*mdl_sw)h:hghUUVGC_180_38r�  h<Nh=h3je  j`  �ubh6)�r�  }r�  (hTP  ( (5*mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_sw)/(72.*mdl_cw*cmath.pi**2) - (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_sw*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(24.*mdl_cw*cmath.pi**2) if mdl_MB else (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_sw)/(72.*mdl_cw*cmath.pi**2) ) - (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_sw)/(72.*mdl_cw*cmath.pi**2)h:hghUUVGC_181_39r�  h<Nh=h3je  j`  �ubh6)�r�  }r�  (hU�(-2*mdl_ee*mdl_complexi*mdl_G__exp__2)/(9.*cmath.pi**2) + (mdl_ee*mdl_complexi*mdl_G__exp__2*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(6.*cmath.pi**2)h:hghUUVGC_194_76r�  h<Nh=h3je  j`  �ubh6)�r�  }r�  (hTe  ( (-5*mdl_ee*mdl_complexi*mdl_G__exp__2)/(24.*cmath.pi**2*mdl_sw*mdl_sqrt__2) + (mdl_ee*mdl_complexi*mdl_G__exp__2*reglog(mdl_MB__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2*mdl_sw*mdl_sqrt__2) if mdl_MB else -(mdl_ee*mdl_complexi*mdl_G__exp__2)/(24.*cmath.pi**2*mdl_sw*mdl_sqrt__2) ) + (mdl_ee*mdl_complexi*mdl_G__exp__2)/(24.*cmath.pi**2*mdl_sw*mdl_sqrt__2)h:hghUUVGC_201_87r�  h<Nh=h3je  j`  �ubh6)�r�  }r�  (hU�-(mdl_ee*mdl_complexi*mdl_G__exp__2)/(6.*cmath.pi**2*mdl_sw*mdl_sqrt__2) + (mdl_ee*mdl_complexi*mdl_G__exp__2*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2*mdl_sw*mdl_sqrt__2)h:hghUUVGC_201_88r�  h<Nh=h3je  j`  �ubh6)�r�  }r�  (hU�-(mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2)/(6.*cmath.pi**2*mdl_sw) + (mdl_cw*mdl_ee*mdl_complexi*mdl_G__exp__2*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(8.*cmath.pi**2*mdl_sw)h:hghUUVGC_202_89r�  h<Nh=h3je  j`  �ubh6)�r�  }r�  (hU�(mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_sw)/(18.*mdl_cw*cmath.pi**2) - (mdl_ee*mdl_complexi*mdl_G__exp__2*mdl_sw*reglog(mdl_MT__exp__2/mdl_MU_R__exp__2))/(24.*mdl_cw*cmath.pi**2)h:hghUUVGC_203_90r�  h<Nh=h3je  j`  �ube)]r�  (h6)�r�  }r�  (hUmdl_complexi*mdl_gAd11h:hghUGC_15r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gAd22h:hghUGC_16r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gAd31h:hghUGC_17r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gAd33h:hghUGC_18r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gAl11h:hghUGC_19r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gAl22h:hghUGC_20r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gAl33h:hghUGC_21r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gAu11h:hghUGC_22r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gAu22h:hghUGC_23r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gAu31h:hghUGC_24r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gAu33h:hghUGC_25r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gAXdh:hghUGC_26r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gnu11h:hghUGC_27r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gnu22h:hghUGC_28r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gnu33h:hghUGC_29r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gVd11h:hghUGC_30r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gVd22h:hghUGC_31r�  h<Nh=)ubh6)�r�  }r�  (hUmdl_complexi*mdl_gVd31h:hghUGC_32r�  h<Nh=)ubh6)�r�  }r   (hUmdl_complexi*mdl_gVd33h:hghUGC_33r  h<Nh=)ubh6)�r  }r  (hUmdl_complexi*mdl_gVl11h:hghUGC_34r  h<Nh=)ubh6)�r  }r  (hUmdl_complexi*mdl_gVl22h:hghUGC_35r  h<Nh=)ubh6)�r  }r	  (hUmdl_complexi*mdl_gVl33h:hghUGC_36r
  h<Nh=)ubh6)�r  }r  (hUmdl_complexi*mdl_gVu11h:hghUGC_37r  h<Nh=)ubh6)�r  }r  (hUmdl_complexi*mdl_gVu22h:hghUGC_38r  h<Nh=)ubh6)�r  }r  (hUmdl_complexi*mdl_gVu31h:hghUGC_39r  h<Nh=)ubh6)�r  }r  (hUmdl_complexi*mdl_gVu33h:hghUGC_40r  h<Nh=)ubh6)�r  }r  (hU-(mdl_complexi*mdl_gVXc)/2.h:hghUGC_41r  h<Nh=)ubh6)�r  }r  (hUmdl_complexi*mdl_gVXdh:hghUGC_42r  h<Nh=)ubeje  h3�r  ]r  (h6)�r  }r   (hUH-(mdl_complexi*mdl_G__exp__2*mdl_MB*mdl_yb)/(8.*cmath.pi**2*mdl_sqrt__2)h:hghUR2GC_120_15r!  h<Nh=j  ubh6)�r"  }r#  (hUH-(mdl_complexi*mdl_G__exp__2*mdl_MT*mdl_yt)/(8.*cmath.pi**2*mdl_sqrt__2)h:hghUR2GC_120_16r$  h<Nh=je  h3�ubh6)�r%  }r&  (hU>-(mdl_complexi*mdl_G__exp__2*mdl_yb__exp__2)/(16.*cmath.pi**2)h:hghUR2GC_121_17r'  h<Nh=je  h3�ubh6)�r(  }r)  (hU>-(mdl_complexi*mdl_G__exp__2*mdl_yt__exp__2)/(16.*cmath.pi**2)h:hghUR2GC_121_18r*  h<Nh=je  h3�ubh6)�r+  }r,  (hU~-(mdl_complexi*mdl_G__exp__2*mdl_yb__exp__2)/(16.*cmath.pi**2) - (mdl_complexi*mdl_G__exp__2*mdl_yt__exp__2)/(16.*cmath.pi**2)h:hghUR2GC_135_64r-  h<Nh=je  h3�ubh6)�r.  }r/  (hU@(mdl_complexi*mdl_G__exp__2*mdl_yb)/(3.*cmath.pi**2*mdl_sqrt__2)h:hghUR2GC_182_94r0  h<Nh=je  h3�ubh6)�r1  }r2  (hU4-(mdl_G__exp__2*mdl_yb)/(3.*cmath.pi**2*mdl_sqrt__2)h:hghUR2GC_183_95r3  h<Nh=je  h3�ubh6)�r4  }r5  (hU'(mdl_G__exp__2*mdl_yb)/(3.*cmath.pi**2)h:hghUR2GC_204_111r6  h<Nh=je  h3�ubh6)�r7  }r8  (hU(-(mdl_G__exp__2*mdl_yb)/(3.*cmath.pi**2)h:hghUR2GC_205_112r9  h<Nh=je  h3�ubh6)�r:  }r;  (hU'(mdl_G__exp__2*mdl_yt)/(3.*cmath.pi**2)h:hghUR2GC_206_113r<  h<Nh=je  h3�ubh6)�r=  }r>  (hU(-(mdl_G__exp__2*mdl_yt)/(3.*cmath.pi**2)h:hghUR2GC_207_114r?  h<Nh=je  h3�ubh6)�r@  }rA  (hU3(mdl_G__exp__2*mdl_yt)/(3.*cmath.pi**2*mdl_sqrt__2)h:hghUR2GC_208_115rB  h<Nh=je  h3�ubh6)�rC  }rD  (hU@(mdl_complexi*mdl_G__exp__2*mdl_yt)/(3.*cmath.pi**2*mdl_sqrt__2)h:hghUR2GC_209_116rE  h<Nh=je  h3�ubh6)�rF  }rG  (hU�( (mdl_complexi*mdl_G__exp__2*mdl_yb)/(6.*cmath.pi**2*mdl_sqrt__2) if mdl_MB else -(mdl_complexi*mdl_G__exp__2*mdl_yb)/(12.*cmath.pi**2*mdl_sqrt__2) ) + (mdl_complexi*mdl_G__exp__2*mdl_yb)/(3.*cmath.pi**2*mdl_sqrt__2)h:hghUUVGC_182_40_1epsh<Nh=je  h3�ubh6)�rH  }rI  (hU�( -(mdl_G__exp__2*mdl_yb)/(6.*cmath.pi**2*mdl_sqrt__2) if mdl_MB else (mdl_G__exp__2*mdl_yb)/(12.*cmath.pi**2*mdl_sqrt__2) ) - (mdl_G__exp__2*mdl_yb)/(3.*cmath.pi**2*mdl_sqrt__2)h:hghUUVGC_183_41_1epsh<Nh=je  h3�ubh6)�rJ  }rK  (hUe( (mdl_G__exp__2*mdl_yb)/(12.*cmath.pi**2) if mdl_MB else -(mdl_G__exp__2*mdl_yb)/(24.*cmath.pi**2) )h:hghUUVGC_204_91_1epsh<Nh=je  h3�ubh6)�rL  }rM  (hU((mdl_G__exp__2*mdl_yb)/(12.*cmath.pi**2)h:hghUUVGC_204_92_1epsh<Nh=je  h3�ubh6)�rN  }rO  (hU'(mdl_G__exp__2*mdl_yb)/(3.*cmath.pi**2)h:hghUUVGC_204_93_1epsh<Nh=je  h3�ubh6)�rP  }rQ  (hUe( -(mdl_G__exp__2*mdl_yb)/(12.*cmath.pi**2) if mdl_MB else (mdl_G__exp__2*mdl_yb)/(24.*cmath.pi**2) )h:hghUUVGC_205_94_1epsh<Nh=je  h3�ubh6)�rR  }rS  (hU)-(mdl_G__exp__2*mdl_yb)/(12.*cmath.pi**2)h:hghUUVGC_205_95_1epsh<Nh=je  h3�ubh6)�rT  }rU  (hU(-(mdl_G__exp__2*mdl_yb)/(3.*cmath.pi**2)h:hghUUVGC_205_96_1epsh<Nh=je  h3�ubh6)�rV  }rW  (hUe( (mdl_G__exp__2*mdl_yt)/(12.*cmath.pi**2) if mdl_MB else -(mdl_G__exp__2*mdl_yt)/(24.*cmath.pi**2) )h:hghUUVGC_206_97_1epsh<Nh=je  h3�ubh6)�rX  }rY  (hU((mdl_G__exp__2*mdl_yt)/(12.*cmath.pi**2)h:hghUUVGC_206_98_1epsh<Nh=je  h3�ubh6)�rZ  }r[  (hU'(mdl_G__exp__2*mdl_yt)/(3.*cmath.pi**2)h:hghUUVGC_206_99_1epsh<Nh=je  h3�ubh6)�r\  }r]  (hUe( -(mdl_G__exp__2*mdl_yt)/(12.*cmath.pi**2) if mdl_MB else (mdl_G__exp__2*mdl_yt)/(24.*cmath.pi**2) )h:hghUUVGC_207_100_1epsh<Nh=je  h3�ubh6)�r^  }r_  (hU)-(mdl_G__exp__2*mdl_yt)/(12.*cmath.pi**2)h:hghUUVGC_207_101_1epsh<Nh=je  h3�ubh6)�r`  }ra  (hU(-(mdl_G__exp__2*mdl_yt)/(3.*cmath.pi**2)h:hghUUVGC_207_102_1epsh<Nh=je  h3�ubh6)�rb  }rc  (hU3(mdl_G__exp__2*mdl_yt)/(2.*cmath.pi**2*mdl_sqrt__2)h:hghUUVGC_208_103_1epsh<Nh=je  h3�ubh6)�rd  }re  (hU@(mdl_complexi*mdl_G__exp__2*mdl_yt)/(2.*cmath.pi**2*mdl_sqrt__2)h:hghUUVGC_209_104_1epsh<Nh=je  h3�ubeh3�rf  ]rg  (h6)�rh  }ri  (hU-(mdl_ee*mdl_complexi)/3.h:hghUGC_1rj  h<Nh=jf  ubh6)�rk  }rl  (hU(2*mdl_ee*mdl_complexi)/3.h:hghUGC_2rm  h<Nh=h3�ubh6)�rn  }ro  (hU-(mdl_ee*mdl_complexi)h:hghUGC_3rp  h<Nh=h3�ubh6)�rq  }rr  (hUmdl_ee*mdl_complexih:hghUGC_4rs  h<Nh=h3�ubh6)�rt  }ru  (hhhh:hghUGC_43rv  h<Nh=h3�ubh6)�rw  }rx  (hU
-mdl_I2a33h:hghUGC_44ry  h<Nh=h3�ubh6)�rz  }r{  (hhmh:hghUGC_45r|  h<Nh=h3�ubh6)�r}  }r~  (hU
-mdl_I4a33h:hghUGC_46r  h<Nh=h3�ubh6)�r�  }r�  (hU-2*mdl_complexi*mdl_lamh:hghUGC_47r�  h<Nh=h3�ubh6)�r�  }r�  (hU-4*mdl_complexi*mdl_lamh:hghUGC_48r�  h<Nh=h3�ubh6)�r�  }r�  (hU-6*mdl_complexi*mdl_lamh:hghUGC_49r�  h<Nh=h3�ubh6)�r�  }r�  (hUmdl_ee__exp__2*mdl_complexih:hghUGC_5r�  h<Nh=h3�ubh6)�r�  }r�  (hU1(mdl_ee__exp__2*mdl_complexi)/(2.*mdl_sw__exp__2)h:hghUGC_50r�  h<Nh=h3�ubh6)�r�  }r�  (hU/-((mdl_ee__exp__2*mdl_complexi)/mdl_sw__exp__2)h:hghUGC_51r�  h<Nh=h3�ubh6)�r�  }r�  (hU;(mdl_cw__exp__2*mdl_ee__exp__2*mdl_complexi)/mdl_sw__exp__2h:hghUGC_52r�  h<Nh=h3�ubh6)�r�  }r�  (hU-mdl_ee/(2.*mdl_sw)h:hghUGC_53r�  h<Nh=h3�ubh6)�r�  }r�  (hU"-(mdl_ee*mdl_complexi)/(2.*mdl_sw)h:hghUGC_54r�  h<Nh=h3�ubh6)�r�  }r�  (hU!(mdl_ee*mdl_complexi)/(2.*mdl_sw)h:hghUGC_55r�  h<Nh=h3�ubh6)�r�  }r�  (hU*(mdl_ee*mdl_complexi)/(mdl_sw*mdl_sqrt__2)h:hghUGC_56r�  h<Nh=h3�ubh6)�r�  }r�  (hU)-(mdl_cw*mdl_ee*mdl_complexi)/(2.*mdl_sw)h:hghUGC_57r�  h<Nh=h3�ubh6)�r�  }r�  (hU((mdl_cw*mdl_ee*mdl_complexi)/(2.*mdl_sw)h:hghUGC_58r�  h<Nh=h3�ubh6)�r�  }r�  (hU&-((mdl_cw*mdl_ee*mdl_complexi)/mdl_sw)h:hghUGC_59r�  h<Nh=h3�ubh6)�r�  }r�  (hU2*mdl_ee__exp__2*mdl_complexih:hghUGC_6r�  h<Nh=h3�ubh6)�r�  }r�  (hU#(mdl_cw*mdl_ee*mdl_complexi)/mdl_swh:hghUGC_60r�  h<Nh=h3�ubh6)�r�  }r�  (hU-mdl_ee__exp__2/(2.*mdl_sw)h:hghUGC_61r�  h<Nh=h3�ubh6)�r�  }r�  (hU*-(mdl_ee__exp__2*mdl_complexi)/(2.*mdl_sw)h:hghUGC_62r�  h<Nh=h3�ubh6)�r�  }r�  (hUmdl_ee__exp__2/(2.*mdl_sw)h:hghUGC_63r�  h<Nh=h3�ubh6)�r�  }r�  (hU.(-2*mdl_cw*mdl_ee__exp__2*mdl_complexi)/mdl_swh:hghUGC_64r�  h<Nh=h3�ubh6)�r�  }r�  (hU)-(mdl_ee*mdl_complexi*mdl_sw)/(6.*mdl_cw)h:hghUGC_65r�  h<Nh=h3�ubh6)�r�  }r�  (hU((mdl_ee*mdl_complexi*mdl_sw)/(2.*mdl_cw)h:hghUGC_66r�  h<Nh=h3�ubh6)�r�  }r�  (hU:-(mdl_cw*mdl_ee)/(2.*mdl_sw) - (mdl_ee*mdl_sw)/(2.*mdl_cw)h:hghUGC_67r�  h<Nh=h3�ubh6)�r�  }r�  (hUT-(mdl_cw*mdl_ee*mdl_complexi)/(2.*mdl_sw) + (mdl_ee*mdl_complexi*mdl_sw)/(2.*mdl_cw)h:hghUGC_68r�  h<Nh=h3�ubh6)�r�  }r�  (hUS(mdl_cw*mdl_ee*mdl_complexi)/(2.*mdl_sw) + (mdl_ee*mdl_complexi*mdl_sw)/(2.*mdl_cw)h:hghUGC_69r�  h<Nh=h3�ubh6)�r�  }r�  (hU-mdl_ee__exp__2/(2.*mdl_cw)h:hghUGC_7r�  h<Nh=h3�ubh6)�r�  }r�  (hUY(mdl_cw*mdl_ee__exp__2*mdl_complexi)/mdl_sw - (mdl_ee__exp__2*mdl_complexi*mdl_sw)/mdl_cwh:hghUGC_70r�  h<Nh=h3�ubh6)�r�  }r�  (hU�-(mdl_ee__exp__2*mdl_complexi) + (mdl_cw__exp__2*mdl_ee__exp__2*mdl_complexi)/(2.*mdl_sw__exp__2) + (mdl_ee__exp__2*mdl_complexi*mdl_sw__exp__2)/(2.*mdl_cw__exp__2)h:hghUGC_71r�  h<Nh=h3�ubh6)�r�  }r�  (hU�mdl_ee__exp__2*mdl_complexi + (mdl_cw__exp__2*mdl_ee__exp__2*mdl_complexi)/(2.*mdl_sw__exp__2) + (mdl_ee__exp__2*mdl_complexi*mdl_sw__exp__2)/(2.*mdl_cw__exp__2)h:hghUGC_72r�  h<Nh=h3�ubh6)�r�  }r�  (hU%-(mdl_ee__exp__2*mdl_vev)/(2.*mdl_cw)h:hghUGC_73r�  h<Nh=h3�ubh6)�r�  }r�  (hU$(mdl_ee__exp__2*mdl_vev)/(2.*mdl_cw)h:hghUGC_74r�  h<Nh=h3�ubh6)�r�  }r�  (hU-2*mdl_complexi*mdl_lam*mdl_vevh:hghUGC_75r�  h<Nh=h3�ubh6)�r�  }r�  (hU-6*mdl_complexi*mdl_lam*mdl_vevh:hghUGC_76r�  h<Nh=h3�ubh6)�r�  }r�  (hU--(mdl_ee__exp__2*mdl_vev)/(4.*mdl_sw__exp__2)h:hghUGC_77r�  h<Nh=h3�ubh6)�r�  }r�  (hU:-(mdl_ee__exp__2*mdl_complexi*mdl_vev)/(4.*mdl_sw__exp__2)h:hghUGC_78r�  h<Nh=h3�ubh6)�r�  }r�  (hU9(mdl_ee__exp__2*mdl_complexi*mdl_vev)/(2.*mdl_sw__exp__2)h:hghUGC_79r�  h<Nh=h3�ubh6)�r�  }r�  (hU)(mdl_ee__exp__2*mdl_complexi)/(2.*mdl_cw)h:hghUGC_8r�  h<Nh=h3�ubh6)�r�  }r�  (hU,(mdl_ee__exp__2*mdl_vev)/(4.*mdl_sw__exp__2)h:hghUGC_80r�  h<Nh=h3�ubh6)�r�  }r�  (hU%-(mdl_ee__exp__2*mdl_vev)/(2.*mdl_sw)h:hghUGC_81r�  h<Nh=h3�ubh6)�r�  }r�  (hU$(mdl_ee__exp__2*mdl_vev)/(2.*mdl_sw)h:hghUGC_82r�  h<Nh=h3�ubh6)�r�  }r�  (hU[-(mdl_ee__exp__2*mdl_vev)/(4.*mdl_cw) - (mdl_cw*mdl_ee__exp__2*mdl_vev)/(4.*mdl_sw__exp__2)h:hghUGC_83r�  h<Nh=h3�ubh6)�r�  }r�  (hUZ(mdl_ee__exp__2*mdl_vev)/(4.*mdl_cw) - (mdl_cw*mdl_ee__exp__2*mdl_vev)/(4.*mdl_sw__exp__2)h:hghUGC_84r�  h<Nh=h3�ubh6)�r�  }r�  (hU[-(mdl_ee__exp__2*mdl_vev)/(4.*mdl_cw) + (mdl_cw*mdl_ee__exp__2*mdl_vev)/(4.*mdl_sw__exp__2)h:hghUGC_85r   h<Nh=h3�ubh6)�r  }r  (hUZ(mdl_ee__exp__2*mdl_vev)/(4.*mdl_cw) + (mdl_cw*mdl_ee__exp__2*mdl_vev)/(4.*mdl_sw__exp__2)h:hghUGC_86r  h<Nh=h3�ubh6)�r  }r  (hU�-(mdl_ee__exp__2*mdl_complexi*mdl_vev)/2. - (mdl_cw__exp__2*mdl_ee__exp__2*mdl_complexi*mdl_vev)/(4.*mdl_sw__exp__2) - (mdl_ee__exp__2*mdl_complexi*mdl_sw__exp__2*mdl_vev)/(4.*mdl_cw__exp__2)h:hghUGC_87r  h<Nh=h3�ubh6)�r  }r  (hU�mdl_ee__exp__2*mdl_complexi*mdl_vev + (mdl_cw__exp__2*mdl_ee__exp__2*mdl_complexi*mdl_vev)/(2.*mdl_sw__exp__2) + (mdl_ee__exp__2*mdl_complexi*mdl_sw__exp__2*mdl_vev)/(2.*mdl_cw__exp__2)h:hghUGC_88r	  h<Nh=h3�ubh6)�r
  }r  (hU-(mdl_yb/mdl_sqrt__2)h:hghUGC_89r  h<Nh=h3�ubh6)�r  }r  (hUmdl_ee__exp__2/(2.*mdl_cw)h:hghUGC_9r  h<Nh=h3�ubh6)�r  }r  (hU$-((mdl_complexi*mdl_yb)/mdl_sqrt__2)h:hghUGC_90r  h<Nh=h3�ubh6)�r  }r  (hUmdl_yb/mdl_sqrt__2h:hghUGC_91r  h<Nh=h3�ubh6)�r  }r  (hU$-((mdl_complexi*mdl_yt)/mdl_sqrt__2)h:hghUGC_92r  h<Nh=h3�ubh6)�r  }r  (hUmdl_yt/mdl_sqrt__2h:hghUGC_93r  h<Nh=h3�ubh6)�r  }r  (hU	-mdl_ytauh:hghUGC_94r  h<Nh=h3�ubh6)�r  }r   (hhbh:hghUGC_95r!  h<Nh=h3�ubh6)�r"  }r#  (hU-(mdl_ytau/mdl_sqrt__2)h:hghUGC_96r$  h<Nh=h3�ubh6)�r%  }r&  (hU&-((mdl_complexi*mdl_ytau)/mdl_sqrt__2)h:hghUGC_97r'  h<Nh=h3�ubeje  �r(  ]r)  (h6)�r*  }r+  (hU-Gr,  h:hghUGC_10r-  h<Nh=j(  ubh6)�r.  }r/  (hUmdl_complexi*Gh:hghUGC_11r0  h<Nh=je  �ubh6)�r1  }r2  (hUGh:hghUGC_12r3  h<Nh=je  �ubh6)�r4  }r5  (hU-(mdl_complexi*mdl_G__exp__2)h:hghUGC_13r6  h<Nh=je  �ubh6)�r7  }r8  (hUmdl_complexi*mdl_G__exp__2h:hghUGC_14r9  h<Nh=je  �ubh6)�r:  }r;  (hU7(mdl_complexi*mdl_G__exp__2*mdl_gAu22)/(6.*cmath.pi**2)h:hghU
R2GC_100_1r<  h<Nh=je  �ubh6)�r=  }r>  (hU8-(mdl_complexi*mdl_G__exp__2*mdl_gVu22)/(6.*cmath.pi**2)h:hghU
R2GC_101_2r?  h<Nh=je  �ubh6)�r@  }rA  (hU.(mdl_complexi*mdl_G__exp__2)/(12.*cmath.pi**2)h:hghU
R2GC_104_5rB  h<Nh=je  �ubh6)�rC  }rD  (hU7(mdl_complexi*mdl_G__exp__2*mdl_gAd11)/(6.*cmath.pi**2)h:hghU
R2GC_105_6rE  h<Nh=je  �ubh6)�rF  }rG  (hU8-(mdl_complexi*mdl_G__exp__2*mdl_gVd11)/(6.*cmath.pi**2)h:hghU
R2GC_106_7rH  h<Nh=je  �ubh6)�rI  }rJ  (hU7(mdl_complexi*mdl_G__exp__2*mdl_gAd22)/(6.*cmath.pi**2)h:hghU
R2GC_110_9rK  h<Nh=je  �ubh6)�rL  }rM  (hU8-(mdl_complexi*mdl_G__exp__2*mdl_gVd22)/(6.*cmath.pi**2)h:hghUR2GC_111_10rN  h<Nh=je  �ubh6)�rO  }rP  (hU7(mdl_complexi*mdl_G__exp__2*mdl_gAu11)/(6.*cmath.pi**2)h:hghUR2GC_115_11rQ  h<Nh=je  �ubh6)�rR  }rS  (hU8-(mdl_complexi*mdl_G__exp__2*mdl_gVu11)/(6.*cmath.pi**2)h:hghUR2GC_116_12rT  h<Nh=je  �ubh6)�rU  }rV  (hU=-(mdl_complexi*mdl_G__exp__2*mdl_MB__exp__2)/(8.*cmath.pi**2)h:hghUR2GC_119_13rW  h<Nh=je  �ubh6)�rX  }rY  (hU=-(mdl_complexi*mdl_G__exp__2*mdl_MT__exp__2)/(8.*cmath.pi**2)h:hghUR2GC_119_14rZ  h<Nh=je  �ubh6)�r[  }r\  (hU.(mdl_complexi*mdl_G__exp__2)/(48.*cmath.pi**2)h:hghUR2GC_122_19r]  h<Nh=je  �ubh6)�r^  }r_  (hU,-(mdl_G__exp__2*mdl_gAd33)/(12.*cmath.pi**2)h:hghUR2GC_125_24r`  h<Nh=je  �ubh6)�ra  }rb  (hU,-(mdl_G__exp__2*mdl_gAu22)/(12.*cmath.pi**2)h:hghUR2GC_125_25rc  h<Nh=je  �ubh6)�rd  }re  (hU,-(mdl_G__exp__2*mdl_gAd11)/(12.*cmath.pi**2)h:hghUR2GC_125_26rf  h<Nh=je  �ubh6)�rg  }rh  (hU,-(mdl_G__exp__2*mdl_gAd22)/(12.*cmath.pi**2)h:hghUR2GC_125_27ri  h<Nh=je  �ubh6)�rj  }rk  (hU,-(mdl_G__exp__2*mdl_gAu33)/(12.*cmath.pi**2)h:hghUR2GC_125_28rl  h<Nh=je  �ubh6)�rm  }rn  (hU,-(mdl_G__exp__2*mdl_gAu11)/(12.*cmath.pi**2)h:hghUR2GC_125_29ro  h<Nh=je  �ubh6)�rp  }rq  (hU9-(mdl_complexi*mdl_G__exp__3*mdl_gAd33)/(16.*cmath.pi**2)h:hghUR2GC_126_30rr  h<Nh=je  �ubh6)�rs  }rt  (hU9-(mdl_complexi*mdl_G__exp__3*mdl_gAu22)/(16.*cmath.pi**2)h:hghUR2GC_126_31ru  h<Nh=je  �ubh6)�rv  }rw  (hU9-(mdl_complexi*mdl_G__exp__3*mdl_gAd11)/(16.*cmath.pi**2)h:hghUR2GC_126_32rx  h<Nh=je  �ubh6)�ry  }rz  (hU9-(mdl_complexi*mdl_G__exp__3*mdl_gAd22)/(16.*cmath.pi**2)h:hghUR2GC_126_33r{  h<Nh=je  �ubh6)�r|  }r}  (hU9-(mdl_complexi*mdl_G__exp__3*mdl_gAu33)/(16.*cmath.pi**2)h:hghUR2GC_126_34r~  h<Nh=je  �ubh6)�r  }r�  (hU9-(mdl_complexi*mdl_G__exp__3*mdl_gAu11)/(16.*cmath.pi**2)h:hghUR2GC_126_35r�  h<Nh=je  �ubh6)�r�  }r�  (hU8(mdl_complexi*mdl_G__exp__3*mdl_gVd33)/(48.*cmath.pi**2)h:hghUR2GC_128_42r�  h<Nh=je  �ubh6)�r�  }r�  (hU8(mdl_complexi*mdl_G__exp__3*mdl_gVu22)/(48.*cmath.pi**2)h:hghUR2GC_128_43r�  h<Nh=je  �ubh6)�r�  }r�  (hU8(mdl_complexi*mdl_G__exp__3*mdl_gVd11)/(48.*cmath.pi**2)h:hghUR2GC_128_44r�  h<Nh=je  �ubh6)�r�  }r�  (hU8(mdl_complexi*mdl_G__exp__3*mdl_gVd22)/(48.*cmath.pi**2)h:hghUR2GC_128_45r�  h<Nh=je  �ubh6)�r�  }r�  (hU8(mdl_complexi*mdl_G__exp__3*mdl_gVu33)/(48.*cmath.pi**2)h:hghUR2GC_128_46r�  h<Nh=je  �ubh6)�r�  }r�  (hU8(mdl_complexi*mdl_G__exp__3*mdl_gVu11)/(48.*cmath.pi**2)h:hghUR2GC_128_47r�  h<Nh=je  �ubh6)�r�  }r�  (hU�(mdl_complexi*mdl_G__exp__2*mdl_gAd33__exp__2)/(24.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__2*mdl_gVd33__exp__2)/(24.*cmath.pi**2)h:hghUR2GC_137_66r�  h<Nh=je  �ubh6)�r�  }r�  (hU�(mdl_complexi*mdl_G__exp__2*mdl_gAu22__exp__2)/(24.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__2*mdl_gVu22__exp__2)/(24.*cmath.pi**2)h:hghUR2GC_137_67r�  h<Nh=je  �ubh6)�r�  }r�  (hU�(mdl_complexi*mdl_G__exp__2*mdl_gAd11__exp__2)/(24.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__2*mdl_gVd11__exp__2)/(24.*cmath.pi**2)h:hghUR2GC_137_68r�  h<Nh=je  �ubh6)�r�  }r�  (hU�(mdl_complexi*mdl_G__exp__2*mdl_gAd22__exp__2)/(24.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__2*mdl_gVd22__exp__2)/(24.*cmath.pi**2)h:hghUR2GC_137_69r�  h<Nh=je  �ubh6)�r�  }r�  (hU�(mdl_complexi*mdl_G__exp__2*mdl_gAu33__exp__2)/(24.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__2*mdl_gVu33__exp__2)/(24.*cmath.pi**2)h:hghUR2GC_137_70r�  h<Nh=je  �ubh6)�r�  }r�  (hU�(mdl_complexi*mdl_G__exp__2*mdl_gAu11__exp__2)/(24.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__2*mdl_gVu11__exp__2)/(24.*cmath.pi**2)h:hghUR2GC_137_71r�  h<Nh=je  �ubh6)�r�  }r�  (hU�(mdl_complexi*mdl_G__exp__2*mdl_gAd31__exp__2)/(12.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__2*mdl_gVd31__exp__2)/(12.*cmath.pi**2)h:hghUR2GC_137_72r�  h<Nh=je  �ubh6)�r�  }r�  (hU�(mdl_complexi*mdl_G__exp__2*mdl_gAu31__exp__2)/(12.*cmath.pi**2) + (mdl_complexi*mdl_G__exp__2*mdl_gVu31__exp__2)/(12.*cmath.pi**2)h:hghUR2GC_137_73r�  h<Nh=je  �ubh6)�r�  }r�  (hU!-mdl_G__exp__4/(192.*cmath.pi**2)h:hghUR2GC_147_74r�  h<Nh=je  �ubh6)�r�  }r�  (hUmdl_G__exp__4/(64.*cmath.pi**2)h:hghUR2GC_147_75r�  h<Nh=je  �ubh6)�r�  }r�  (hU0-(mdl_complexi*mdl_G__exp__4)/(192.*cmath.pi**2)h:hghUR2GC_148_76r�  h<Nh=je  �ubh6)�r�  }r�  (hU.(mdl_complexi*mdl_G__exp__4)/(64.*cmath.pi**2)h:hghUR2GC_148_77r�  h<Nh=je  �ubh6)�r�  }r�  (hU/(mdl_complexi*mdl_G__exp__4)/(192.*cmath.pi**2)h:hghUR2GC_149_78r�  h<Nh=je  �ubh6)�r�  }r�  (hU/-(mdl_complexi*mdl_G__exp__4)/(64.*cmath.pi**2)h:hghUR2GC_149_79r�  h<Nh=je  �ubh6)�r�  }r�  (hU/-(mdl_complexi*mdl_G__exp__4)/(48.*cmath.pi**2)h:hghUR2GC_150_80r�  h<Nh=je  �ubh6)�r�  }r�  (hU/(mdl_complexi*mdl_G__exp__4)/(288.*cmath.pi**2)h:hghUR2GC_151_81r�  h<Nh=je  �ubh6)�r�  }r�  (hU/-(mdl_complexi*mdl_G__exp__4)/(32.*cmath.pi**2)h:hghUR2GC_151_82r�  h<Nh=je  �ubh6)�r�  }r�  (hU/-(mdl_complexi*mdl_G__exp__4)/(16.*cmath.pi**2)h:hghUR2GC_152_83r�  h<Nh=je  �ubh6)�r�  }r�  (hU1(-3*mdl_complexi*mdl_G__exp__4)/(64.*cmath.pi**2)h:hghUR2GC_153_84r�  h<Nh=je  �ubh6)�r�  }r�  (hU.-(mdl_complexi*mdl_G__exp__3)/(6.*cmath.pi**2)h:hghUR2GC_155_86r�  h<Nh=je  �ubh6)�r�  }r�  (hU7(mdl_complexi*mdl_G__exp__2*mdl_gAd31)/(6.*cmath.pi**2)h:hghUR2GC_175_89r�  h<Nh=je  �ubh6)�r�  }r�  (hU7(mdl_complexi*mdl_G__exp__2*mdl_gAd33)/(6.*cmath.pi**2)h:hghUR2GC_176_90r�  h<Nh=je  �ubh6)�r�  }r�  (hU8-(mdl_complexi*mdl_G__exp__2*mdl_gVd31)/(6.*cmath.pi**2)h:hghUR2GC_177_91r�  h<Nh=je  �ubh6)�r�  }r�  (hU8-(mdl_complexi*mdl_G__exp__2*mdl_gVd33)/(6.*cmath.pi**2)h:hghUR2GC_178_92r�  h<Nh=je  �ubh6)�r�  }r�  (hU4(mdl_complexi*mdl_G__exp__2*mdl_MB)/(6.*cmath.pi**2)h:hghUR2GC_179_93r�  h<Nh=je  �ubh6)�r�  }r�  (hUmdl_G__exp__3/(24.*cmath.pi**2)h:hghUR2GC_185_96r�  h<Nh=je  �ubh6)�r�  }r�  (hU$(11*mdl_G__exp__3)/(64.*cmath.pi**2)h:hghUR2GC_185_97r�  h<Nh=je  �ubh6)�r�  }r�  (hU -mdl_G__exp__3/(24.*cmath.pi**2)h:hghUR2GC_186_98r�  h<Nh=je  �ubh6)�r�  }r�  (hU%(-11*mdl_G__exp__3)/(64.*cmath.pi**2)h:hghUR2GC_186_99r�  h<Nh=je  �ubh6)�r�  }r�  (hU0(5*mdl_complexi*mdl_G__exp__4)/(48.*cmath.pi**2)h:hghUR2GC_187_100r�  h<Nh=je  �ubh6)�r�  }r�  (hU0(7*mdl_complexi*mdl_G__exp__4)/(32.*cmath.pi**2)h:hghUR2GC_187_101r�  h<Nh=je  �ubh6)�r�  }r�  (hU2(23*mdl_complexi*mdl_G__exp__4)/(192.*cmath.pi**2)h:hghUR2GC_188_102r�  h<Nh=je  �ubh6)�r�  }r�  (hU1(15*mdl_complexi*mdl_G__exp__4)/(64.*cmath.pi**2)h:hghUR2GC_188_103r�  h<Nh=je  �ubh6)�r�  }r�  (hU2(-17*mdl_complexi*mdl_G__exp__4)/(64.*cmath.pi**2)h:hghUR2GC_190_104r�  h<Nh=je  �ubh6)�r�  }r�  (hU1(-7*mdl_complexi*mdl_G__exp__4)/(32.*cmath.pi**2)h:hghUR2GC_191_105r�  h<Nh=je  �ubh6)�r�  }r�  (hU7(mdl_complexi*mdl_G__exp__2*mdl_gAu31)/(6.*cmath.pi**2)h:hghUR2GC_196_106r�  h<Nh=je  �ubh6)�r   }r  (hU7(mdl_complexi*mdl_G__exp__2*mdl_gAu33)/(6.*cmath.pi**2)h:hghUR2GC_197_107r  h<Nh=je  �ubh6)�r  }r  (hU8-(mdl_complexi*mdl_G__exp__2*mdl_gVu31)/(6.*cmath.pi**2)h:hghUR2GC_198_108r  h<Nh=je  �ubh6)�r  }r  (hU8-(mdl_complexi*mdl_G__exp__2*mdl_gVu33)/(6.*cmath.pi**2)h:hghUR2GC_199_109r  h<Nh=je  �ubh6)�r	  }r
  (hU4(mdl_complexi*mdl_G__exp__2*mdl_MT)/(6.*cmath.pi**2)h:hghUR2GC_200_110r  h<Nh=je  �ubh6)�r  }r  (hU/-(mdl_complexi*mdl_G__exp__2)/(16.*cmath.pi**2)h:hghUR2GC_98_117r  h<Nh=je  �ubh6)�r  }r  (hU/-(mdl_complexi*mdl_G__exp__2)/(12.*cmath.pi**2)h:hghUUVGC_138_1_1epsh<Nh=je  �ubh6)�r  }r  (hU0(3*mdl_complexi*mdl_G__exp__2)/(64.*cmath.pi**2)h:hghUUVGC_146_4_1epsh<Nh=je  �ubh6)�r  }r  (hU1(-3*mdl_complexi*mdl_G__exp__2)/(64.*cmath.pi**2)h:hghUUVGC_146_5_1epsh<Nh=je  �ubh6)�r  }r  (hU$(3*mdl_G__exp__4)/(512.*cmath.pi**2)h:hghUUVGC_147_6_1epsh<Nh=je  �ubh6)�r  }r  (hU%(-3*mdl_G__exp__4)/(512.*cmath.pi**2)h:hghUUVGC_147_7_1epsh<Nh=je  �ubh6)�r  }r  (hU1(3*mdl_complexi*mdl_G__exp__4)/(512.*cmath.pi**2)h:hghUUVGC_148_8_1epsh<Nh=je  �ubh6)�r  }r  (hU2(-3*mdl_complexi*mdl_G__exp__4)/(512.*cmath.pi**2)h:hghUUVGC_148_9_1epsh<Nh=je  �ubh6)�r  }r  (hU0-(mdl_complexi*mdl_G__exp__4)/(128.*cmath.pi**2)h:hghUUVGC_150_10_1epsh<Nh=je  �ubh6)�r  }r   (hU/(mdl_complexi*mdl_G__exp__4)/(128.*cmath.pi**2)h:hghUUVGC_150_11_1epsh<Nh=je  �ubh6)�r!  }r"  (hU2(-3*mdl_complexi*mdl_G__exp__4)/(256.*cmath.pi**2)h:hghUUVGC_151_12_1epsh<Nh=je  �ubh6)�r#  }r$  (hU1(3*mdl_complexi*mdl_G__exp__4)/(256.*cmath.pi**2)h:hghUUVGC_151_13_1epsh<Nh=je  �ubh6)�r%  }r&  (hU/-(mdl_complexi*mdl_G__exp__4)/(24.*cmath.pi**2)h:hghUUVGC_152_14_1epsh<Nh=je  �ubh6)�r'  }r(  (hU1(5*mdl_complexi*mdl_G__exp__4)/(512.*cmath.pi**2)h:hghUUVGC_153_15_1epsh<Nh=je  �ubh6)�r)  }r*  (hU2(-13*mdl_complexi*mdl_G__exp__3)/(48.*cmath.pi**2)h:hghUUVGC_155_17_1epsh<Nh=je  �ubh6)�r+  }r,  (hUC( 0 if mdl_MB else (mdl_complexi*mdl_G__exp__3)/(48.*cmath.pi**2) )h:hghUUVGC_157_19_1epsh<Nh=je  �ubh6)�r-  }r.  (hU.(mdl_complexi*mdl_G__exp__3)/(48.*cmath.pi**2)h:hghUUVGC_157_20_1epsh<Nh=je  �ubh6)�r/  }r0  (hU3(-19*mdl_complexi*mdl_G__exp__3)/(128.*cmath.pi**2)h:hghUUVGC_157_21_1epsh<Nh=je  �ubh6)�r1  }r2  (hU0-(mdl_complexi*mdl_G__exp__3)/(128.*cmath.pi**2)h:hghUUVGC_157_22_1epsh<Nh=je  �ubh6)�r3  }r4  (hU.(mdl_complexi*mdl_G__exp__3)/(12.*cmath.pi**2)h:hghUUVGC_157_23_1epsh<Nh=je  �ubh6)�r5  }r6  (hU�( (mdl_complexi*mdl_G__exp__2)/(6.*cmath.pi**2) if mdl_MB else -(mdl_complexi*mdl_G__exp__2)/(12.*cmath.pi**2) ) + (mdl_complexi*mdl_G__exp__2)/(12.*cmath.pi**2)h:hghUUVGC_172_26_1epsh<Nh=je  �ubh6)�r7  }r8  (hUp( -(mdl_complexi*mdl_G__exp__3)/(6.*cmath.pi**2) if mdl_MB else (mdl_complexi*mdl_G__exp__3)/(12.*cmath.pi**2) )h:hghUUVGC_174_28_1epsh<Nh=je  �ubh6)�r9  }r:  (hU�( (mdl_complexi*mdl_G__exp__2*mdl_gAd31)/(12.*cmath.pi**2) if mdl_MB else -(mdl_complexi*mdl_G__exp__2*mdl_gAd31)/(24.*cmath.pi**2) )h:hghUUVGC_175_29_1epsh<Nh=je  �ubh6)�r;  }r<  (hU9-(mdl_complexi*mdl_G__exp__2*mdl_gAd31)/(24.*cmath.pi**2)h:hghUUVGC_175_30_1epsh<Nh=je  �ubh6)�r=  }r>  (hU8(mdl_complexi*mdl_G__exp__2*mdl_gAd31)/(12.*cmath.pi**2)h:hghUUVGC_175_31_1epsh<Nh=je  �ubh6)�r?  }r@  (hU�( (mdl_complexi*mdl_G__exp__2*mdl_gAd33)/(6.*cmath.pi**2) if mdl_MB else -(mdl_complexi*mdl_G__exp__2*mdl_gAd33)/(12.*cmath.pi**2) ) + (mdl_complexi*mdl_G__exp__2*mdl_gAd33)/(12.*cmath.pi**2)h:hghUUVGC_176_32_1epsh<Nh=je  �ubh6)�rA  }rB  (hU�( -(mdl_complexi*mdl_G__exp__2*mdl_gVd31)/(12.*cmath.pi**2) if mdl_MB else (mdl_complexi*mdl_G__exp__2*mdl_gVd31)/(24.*cmath.pi**2) )h:hghUUVGC_177_33_1epsh<Nh=je  �ubh6)�rC  }rD  (hU8(mdl_complexi*mdl_G__exp__2*mdl_gVd31)/(24.*cmath.pi**2)h:hghUUVGC_177_34_1epsh<Nh=je  �ubh6)�rE  }rF  (hU9-(mdl_complexi*mdl_G__exp__2*mdl_gVd31)/(12.*cmath.pi**2)h:hghUUVGC_177_35_1epsh<Nh=je  �ubh6)�rG  }rH  (hU�( -(mdl_complexi*mdl_G__exp__2*mdl_gVd33)/(6.*cmath.pi**2) if mdl_MB else (mdl_complexi*mdl_G__exp__2*mdl_gVd33)/(12.*cmath.pi**2) ) - (mdl_complexi*mdl_G__exp__2*mdl_gVd33)/(12.*cmath.pi**2)h:hghUUVGC_178_36_1epsh<Nh=je  �ubh6)�rI  }rJ  (hU�( (mdl_complexi*mdl_G__exp__2*mdl_MB)/(6.*cmath.pi**2) if mdl_MB else -(mdl_complexi*mdl_G__exp__2*mdl_MB)/(12.*cmath.pi**2) ) + (mdl_complexi*mdl_G__exp__2*mdl_MB)/(3.*cmath.pi**2)h:hghUUVGC_179_37_1epsh<Nh=je  �ubh6)�rK  }rL  (hUt( 0 if mdl_MB else (mdl_complexi*mdl_G__exp__2)/(24.*cmath.pi**2) ) - (mdl_complexi*mdl_G__exp__2)/(24.*cmath.pi**2)h:hghUUVGC_184_42_1epsh<Nh=je  �ubh6)�rM  }rN  (hU/-(mdl_complexi*mdl_G__exp__2)/(24.*cmath.pi**2)h:hghUUVGC_184_43_1epsh<Nh=je  �ubh6)�rO  }rP  (hUW( 0 if mdl_MB else -mdl_G__exp__3/(16.*cmath.pi**2) ) + mdl_G__exp__3/(24.*cmath.pi**2)h:hghUUVGC_185_44_1epsh<Nh=je  �ubh6)�rQ  }rR  (hU -mdl_G__exp__3/(48.*cmath.pi**2)h:hghUUVGC_185_45_1epsh<Nh=je  �ubh6)�rS  }rT  (hU$(21*mdl_G__exp__3)/(64.*cmath.pi**2)h:hghUUVGC_185_46_1epsh<Nh=je  �ubh6)�rU  }rV  (hUmdl_G__exp__3/(64.*cmath.pi**2)h:hghUUVGC_185_47_1epsh<Nh=je  �ubh6)�rW  }rX  (hUmdl_G__exp__3/(24.*cmath.pi**2)h:hghUUVGC_185_48_1epsh<Nh=je  �ubh6)�rY  }rZ  (hUV( 0 if mdl_MB else mdl_G__exp__3/(16.*cmath.pi**2) ) - mdl_G__exp__3/(24.*cmath.pi**2)h:hghUUVGC_186_49_1epsh<Nh=je  �ubh6)�r[  }r\  (hUmdl_G__exp__3/(48.*cmath.pi**2)h:hghUUVGC_186_50_1epsh<Nh=je  �ubh6)�r]  }r^  (hU%(-21*mdl_G__exp__3)/(64.*cmath.pi**2)h:hghUUVGC_186_51_1epsh<Nh=je  �ubh6)�r_  }r`  (hU -mdl_G__exp__3/(64.*cmath.pi**2)h:hghUUVGC_186_52_1epsh<Nh=je  �ubh6)�ra  }rb  (hU -mdl_G__exp__3/(24.*cmath.pi**2)h:hghUUVGC_186_53_1epsh<Nh=je  �ubh6)�rc  }rd  (hUu( 0 if mdl_MB else -(mdl_complexi*mdl_G__exp__4)/(12.*cmath.pi**2) ) + (mdl_complexi*mdl_G__exp__4)/(12.*cmath.pi**2)h:hghUUVGC_187_54_1epsh<Nh=je  �ubh6)�re  }rf  (hU2(83*mdl_complexi*mdl_G__exp__4)/(128.*cmath.pi**2)h:hghUUVGC_187_55_1epsh<Nh=je  �ubh6)�rg  }rh  (hU1(3*mdl_complexi*mdl_G__exp__4)/(128.*cmath.pi**2)h:hghUUVGC_187_56_1epsh<Nh=je  �ubh6)�ri  }rj  (hU.(mdl_complexi*mdl_G__exp__4)/(12.*cmath.pi**2)h:hghUUVGC_187_57_1epsh<Nh=je  �ubh6)�rk  }rl  (hU3(335*mdl_complexi*mdl_G__exp__4)/(512.*cmath.pi**2)h:hghUUVGC_188_58_1epsh<Nh=je  �ubh6)�rm  }rn  (hU2(21*mdl_complexi*mdl_G__exp__4)/(512.*cmath.pi**2)h:hghUUVGC_188_59_1epsh<Nh=je  �ubh6)�ro  }rp  (hUD( 0 if mdl_MB else -(mdl_complexi*mdl_G__exp__4)/(12.*cmath.pi**2) )h:hghUUVGC_189_60_1epsh<Nh=je  �ubh6)�rq  }rr  (hU/-(mdl_complexi*mdl_G__exp__4)/(12.*cmath.pi**2)h:hghUUVGC_189_61_1epsh<Nh=je  �ubh6)�rs  }rt  (hU2(13*mdl_complexi*mdl_G__exp__4)/(512.*cmath.pi**2)h:hghUUVGC_189_62_1epsh<Nh=je  �ubh6)�ru  }rv  (hUt( 0 if mdl_MB else (mdl_complexi*mdl_G__exp__4)/(12.*cmath.pi**2) ) - (mdl_complexi*mdl_G__exp__4)/(24.*cmath.pi**2)h:hghUUVGC_190_64_1epsh<Nh=je  �ubh6)�rw  }rx  (hU.(mdl_complexi*mdl_G__exp__4)/(24.*cmath.pi**2)h:hghUUVGC_190_65_1epsh<Nh=je  �ubh6)�ry  }rz  (hU4(-341*mdl_complexi*mdl_G__exp__4)/(512.*cmath.pi**2)h:hghUUVGC_190_66_1epsh<Nh=je  �ubh6)�r{  }r|  (hU3(-11*mdl_complexi*mdl_G__exp__4)/(512.*cmath.pi**2)h:hghUUVGC_190_67_1epsh<Nh=je  �ubh6)�r}  }r~  (hU/-(mdl_complexi*mdl_G__exp__4)/(24.*cmath.pi**2)h:hghUUVGC_190_68_1epsh<Nh=je  �ubh6)�r  }r�  (hU3(-83*mdl_complexi*mdl_G__exp__4)/(128.*cmath.pi**2)h:hghUUVGC_191_69_1epsh<Nh=je  �ubh6)�r�  }r�  (hU2(-5*mdl_complexi*mdl_G__exp__4)/(128.*cmath.pi**2)h:hghUUVGC_191_70_1epsh<Nh=je  �ubh6)�r�  }r�  (hUC( 0 if mdl_MB else (mdl_complexi*mdl_G__exp__4)/(12.*cmath.pi**2) )h:hghUUVGC_192_71_1epsh<Nh=je  �ubh6)�r�  }r�  (hU.(mdl_complexi*mdl_G__exp__4)/(12.*cmath.pi**2)h:hghUUVGC_192_72_1epsh<Nh=je  �ubh6)�r�  }r�  (hU3(-19*mdl_complexi*mdl_G__exp__4)/(512.*cmath.pi**2)h:hghUUVGC_192_73_1epsh<Nh=je  �ubh6)�r�  }r�  (hU-(mdl_complexi*mdl_G__exp__2)/(4.*cmath.pi**2)h:hghUUVGC_193_75_1epsh<Nh=je  �ubh6)�r�  }r�  (hU.-(mdl_complexi*mdl_G__exp__3)/(6.*cmath.pi**2)h:hghUUVGC_195_77_1epsh<Nh=je  �ubh6)�r�  }r�  (hU8(mdl_complexi*mdl_G__exp__2*mdl_gAu31)/(12.*cmath.pi**2)h:hghUUVGC_196_78_1epsh<Nh=je  �ubh6)�r�  }r�  (hU9-(mdl_complexi*mdl_G__exp__2*mdl_gAu31)/(24.*cmath.pi**2)h:hghUUVGC_196_79_1epsh<Nh=je  �ubh6)�r�  }r�  (hU8(mdl_complexi*mdl_G__exp__2*mdl_gAu31)/(12.*cmath.pi**2)h:hghUUVGC_196_80_1epsh<Nh=je  �ubh6)�r�  }r�  (hU7(mdl_complexi*mdl_G__exp__2*mdl_gAu33)/(4.*cmath.pi**2)h:hghUUVGC_197_81_1epsh<Nh=je  �ubh6)�r�  }r�  (hU9-(mdl_complexi*mdl_G__exp__2*mdl_gVu31)/(12.*cmath.pi**2)h:hghUUVGC_198_82_1epsh<Nh=je  �ubh6)�r�  }r�  (hU8(mdl_complexi*mdl_G__exp__2*mdl_gVu31)/(24.*cmath.pi**2)h:hghUUVGC_198_83_1epsh<Nh=je  �ubh6)�r�  }r�  (hU9-(mdl_complexi*mdl_G__exp__2*mdl_gVu31)/(12.*cmath.pi**2)h:hghUUVGC_198_84_1epsh<Nh=je  �ubh6)�r�  }r�  (hU8-(mdl_complexi*mdl_G__exp__2*mdl_gVu33)/(4.*cmath.pi**2)h:hghUUVGC_199_85_1epsh<Nh=je  �ubh6)�r�  }r�  (hU4(mdl_complexi*mdl_G__exp__2*mdl_MT)/(2.*cmath.pi**2)h:hghUUVGC_200_86_1epsh<Nh=je  �ubeuu}r�  Umap_CTcoup_CTparamr�  }sb.                                                                                 object_library.py                                                                                   0000644 0276724 0002567 00000023217 13234357560 012743  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     ##
##
## Feynrules Header
##
##
##
##
##

import cmath
import re

class UFOError(Exception):
        """Exception raised if when inconsistencies are detected in the UFO model."""
        pass

class UFOBaseClass(object):
    """The class from which all FeynRules classes are derived."""

    require_args = []

    def __init__(self, *args, **options):
        assert(len(self.require_args) == len (args))
    
        for i, name in enumerate(self.require_args):
            setattr(self, name, args[i])
    
        for (option, value) in options.items():
            setattr(self, option, value)

    def get(self, name):
        return getattr(self, name)
    
    def set(self, name, value):
        setattr(self, name, value)
        
    def get_all(self):
        """Return a dictionary containing all the information of the object"""
        return self.__dict__

    def __str__(self):
        return self.name

    def nice_string(self):
        """ return string with the full information """
        return '\n'.join(['%s \t: %s' %(name, value) for name, value in self.__dict__.items()])

    def __repr__(self):
        replacements = [
            ('+','__plus__'),
            ('-','__minus__'),
            ('@','__at__'),
            ('!','__exclam__'),
            ('?','__quest__'),
            ('*','__star__'),
            ('~','__tilde__')
            ]
        text = self.name
        for orig,sub in replacements:
            text = text.replace(orig,sub)
        return text



all_particles = []

class Particle(UFOBaseClass):
    """A standard Particle"""

    require_args=['pdg_code', 'name', 'antiname', 'spin', 'color', 'mass', 'width', 'texname', 'antitexname', 'charge']

    require_args_all = ['pdg_code', 'name', 'antiname', 'spin', 'color', 'mass', 'width', 'texname', 'antitexname','counterterm','charge', 'line', 'propagating', 'goldstoneboson', 'propagator']

    def __init__(self, pdg_code, name, antiname, spin, color, mass, width, texname,
                 antitexname, charge , line=None, propagating=True, counterterm=None, goldstoneboson=False, 
                 propagator=None, **options):

        args= (pdg_code, name, antiname, spin, color, mass, width, texname,
                antitexname, float(charge))

        UFOBaseClass.__init__(self, *args,  **options)

        global all_particles
        all_particles.append(self)

        self.propagating = propagating
        self.goldstoneboson= goldstoneboson

        self.selfconjugate = (name == antiname)
        if not line:                                                                                                                                                                                   
            self.line = self.find_line_type()
        else:
            self.line = line

        if propagator:
            if isinstance(propagator, dict):
                self.propagator = propagator
            else:
                self.propagator = {0: propagator, 1: propagator}
             
    def find_line_type(self):
        """ find how we draw a line if not defined
        valid output: dashed/straight/wavy/curly/double/swavy/scurly
        """
        
        spin = self.spin
        color = self.color
        
        #use default
        if spin == 1:
            return 'dashed'
        elif spin == 2:
            if not self.selfconjugate:
                return 'straight'
            elif color == 1:
                return 'swavy'
            else:
                return 'scurly'
        elif spin == 3:
            if color == 1:
                return 'wavy'
            
            else:
                return 'curly'
        elif spin == 5:
            return 'double'
        elif spin == -1:
            return 'dotted'
        else:
            return 'dashed' # not supported yet
        
    def anti(self):
        if self.selfconjugate:
            raise Exception('%s has no anti particle.' % self.name) 
        outdic = {}
        for k,v in self.__dict__.iteritems():
            if k not in self.require_args_all:                
                outdic[k] = -v
        if self.color in [1,8]:
            newcolor = self.color
        else:
            newcolor = -self.color
                
        return Particle(-self.pdg_code, self.antiname, self.name, self.spin, newcolor, self.mass, self.width,
                        self.antitexname, self.texname, -self.charge, self.line, self.propagating, self.goldstoneboson, **outdic)



all_parameters = []

class Parameter(UFOBaseClass):

    require_args=['name', 'nature', 'type', 'value', 'texname']

    def __init__(self, name, nature, type, value, texname, lhablock=None, lhacode=None):

        args = (name,nature,type,value,texname)

        UFOBaseClass.__init__(self, *args)

        args=(name,nature,type,value,texname)

        global all_parameters
        all_parameters.append(self)

        if (lhablock is None or lhacode is None)  and nature == 'external':
            raise Exception('Need LHA information for external parameter "%s".' % name)
        self.lhablock = lhablock
        self.lhacode = lhacode

all_CTparameters = []

class CTParameter(UFOBaseClass):

    require_args=['name', 'nature,', 'type', 'value', 'texname']

    def __init__(self, name, type, value, texname):

        args = (name,'internal',type,value,texname)

        UFOBaseClass.__init__(self, *args)

        args=(name,'internal',type,value,texname)

        self.nature='interal'

        global all_CTparameters
        all_CTparameters.append(self)

    def finite(self):
        try:
            return self.value[0]
        except KeyError:
            return 'ZERO'
    
    def pole(self, x):
        try:
            return self.value[-x]
        except KeyError:
            return 'ZERO'

all_vertices = []

class Vertex(UFOBaseClass):

    require_args=['name', 'particles', 'color', 'lorentz', 'couplings']

    def __init__(self, name, particles, color, lorentz, couplings, **opt):
 
        args = (name, particles, color, lorentz, couplings)

        UFOBaseClass.__init__(self, *args, **opt)

        args=(particles,color,lorentz,couplings)

        global all_vertices
        all_vertices.append(self)

all_CTvertices = []

class CTVertex(UFOBaseClass):

    require_args=['name', 'particles', 'color', 'lorentz', 'couplings', 'type', 'loop_particles']

    def __init__(self, name, particles, color, lorentz, couplings, type, loop_particles, **opt):
 
        args = (name, particles, color, lorentz, couplings, type, loop_particles)

        UFOBaseClass.__init__(self, *args, **opt)

        args=(particles,color,lorentz,couplings, type, loop_particles)
        
        global all_CTvertices
        all_CTvertices.append(self)

all_couplings = []

class Coupling(UFOBaseClass):

    require_args=['name', 'value', 'order']

    require_args_all=['name', 'value', 'order', 'loop_particles', 'counterterm']

    def __init__(self, name, value, order, **opt):

        args =(name, value, order)	
        UFOBaseClass.__init__(self, *args, **opt)
        global all_couplings
        all_couplings.append(self)

    def value(self):
        return self.pole(0)

    def pole(self, x):
        """ the self.value attribute can be a dictionary directly specifying the Laurent serie using normal
        parameter or just a string which can possibly contain CTparameter defining the Laurent serie."""

        if isinstance(self.value,dict):
            if -x in self.value.keys():
                return self.value[-x]
            else:
                return 'ZERO'
        if x==0:
            return self.value
        else:
            return 'ZERO'


all_lorentz = []

class Lorentz(UFOBaseClass):

    require_args=['name','spins','structure']
    
    def __init__(self, name, spins, structure='external', **opt):
        args = (name, spins, structure)
        UFOBaseClass.__init__(self, *args, **opt)

        global all_lorentz
        all_lorentz.append(self)


all_functions = []

class Function(object):

    def __init__(self, name, arguments, expression):

        global all_functions
        all_functions.append(self)

        self.name = name
        self.arguments = arguments
        self.expr = expression
    
    def __call__(self, *opt):

        for i, arg in enumerate(self.arguments):
            exec('%s = %s' % (arg, opt[i] ))

        return eval(self.expr)

all_orders = []

class CouplingOrder(object):

    def __init__(self, name, expansion_order, hierarchy, perturbative_expansion = 0):
        
        global all_orders
        all_orders.append(self)

        self.name = name
        self.expansion_order = expansion_order
        self.hierarchy = hierarchy
        self.perturbative_expansion = perturbative_expansion

all_decays = []

class Decay(UFOBaseClass):
    require_args = ['particle','partial_widths']

    def __init__(self, particle, partial_widths, **opt):
        args = (particle, partial_widths)
        UFOBaseClass.__init__(self, *args, **opt)

        global all_decays
        all_decays.append(self)
    
        # Add the information directly to the particle
        particle.partial_widths = partial_widths

all_form_factors = []

class FormFactor(UFOBaseClass):
    require_args = ['name','type','value']

    def __init__(self, name, type, value, **opt):
        args = (name, type, value)
        UFOBaseClass.__init__(self, *args, **opt)

        global all_form_factors
        all_form_factors.append(self)

        
all_propagators = []

class Propagator(UFOBaseClass):
    
    require_args = ['name','numerator','denominator']

    def __init__(self, name, numerator, denominator=None, **opt):
        args = (name, numerator, denominator)
        UFOBaseClass.__init__(self, *args, **opt)

        global all_propagators
        all_propagators.append(self)
                                                                                                                                                                                                                                                                                                                                                                                 object_library.pyo                                                                                  0000644 0276724 0002567 00000032372 13234357560 013124  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc           @   s�  d  d l  Z  d  d l Z d e f d �  �  YZ d e f d �  �  YZ g  a d e f d �  �  YZ g  a d e f d	 �  �  YZ	 g  a
 d
 e f d �  �  YZ g  a d e f d �  �  YZ g  a d e f d �  �  YZ g  a d e f d �  �  YZ g  a d e f d �  �  YZ g  a d e f d �  �  YZ g  a d e f d �  �  YZ g  a d e f d �  �  YZ g  a d e f d �  �  YZ g  a d e f d �  �  YZ d S(   i����Nt   UFOErrorc           B   s   e  Z d  Z RS(   sG   Exception raised if when inconsistencies are detected in the UFO model.(   t   __name__t
   __module__t   __doc__(    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR       s   t   UFOBaseClassc           B   sS   e  Z d  Z g  Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z	 d �  Z
 RS(   s7   The class from which all FeynRules classes are derived.c         O   se   x1 t  |  j � D]  \ } } t |  | | | � q Wx* | j �  D] \ } } t |  | | � qA Wd  S(   N(   t	   enumeratet   require_argst   setattrt   items(   t   selft   argst   optionst   it   namet   optiont   value(    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyt   __init__   s    c         C   s   t  |  | � S(   N(   t   getattr(   R	   R   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyt   get   s    c         C   s   t  |  | | � d  S(   N(   R   (   R	   R   R   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyt   set"   s    c         C   s   |  j  S(   s@   Return a dictionary containing all the information of the object(   t   __dict__(   R	   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyt   get_all%   s    c         C   s   |  j  S(   N(   R   (   R	   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyt   __str__)   s    c         C   s9   d j  g  |  j j �  D] \ } } d | | f ^ q � S(   s)    return string with the full information s   
s   %s 	: %s(   t   joinR   R   (   R	   R   R   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyt   nice_string,   s    c         C   sQ   d d d d d d d g } |  j  } x& | D] \ } } | j | | � } q+ W| S(   Nt   +t   __plus__t   -t	   __minus__t   @t   __at__t   !t
   __exclam__t   ?t	   __quest__t   *t   __star__t   ~t	   __tilde__(   R   s   __plus__(   R   s	   __minus__(   R   s   __at__(   R   s
   __exclam__(   R!   s	   __quest__(   R#   s   __star__(   R%   s	   __tilde__(   R   t   replace(   R	   t   replacementst   textt   origt   sub(    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyt   __repr__0   s    		(   R   R   R   R   R   R   R   R   R   R   R,   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR      s   							t   Particlec           B   s�   e  Z d  Z d d d d d d d d d	 d
 g
 Z d d d d d d d d d	 d d
 d d d d g Z d e d e d d � Z d �  Z	 d �  Z
 RS(   s   A standard Particlet   pdg_codeR   t   antinamet   spint   colort   masst   widtht   texnamet   antitexnamet   charget   countertermt   linet   propagatingt   goldstonebosont
   propagatorc         K   s�   | | | | | | | | |	 t  |
 � f
 } t j |  | | � t j |  � | |  _ | |  _ | | k |  _ | s� |  j �  |  _	 n	 | |  _	 | r� t
 | t � r� | |  _ q� i | d 6| d 6|  _ n  d  S(   Ni    i   (   t   floatR   R   t   all_particlest   appendR9   R:   t   selfconjugatet   find_line_typeR8   t
   isinstancet   dictR;   (   R	   R.   R   R/   R0   R1   R2   R3   R4   R5   R6   R8   R9   R7   R:   R;   R   R
   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR   J   s    			c         C   s�   |  j  } |  j } | d k r" d S| d k rR |  j s; d S| d k rK d Sd SnG | d k ru | d k rn d Sd	 Sn$ | d
 k r� d S| d k r� d Sd Sd S(   su    find how we draw a line if not defined
        valid output: dashed/straight/wavy/curly/double/swavy/scurly
        i   t   dashedi   t   straightt   swavyt   scurlyi   t   wavyt   curlyi   t   doublei����t   dottedN(   R0   R1   R?   (   R	   R0   R1   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR@   e   s&    			c         C   s�   |  j  r t d |  j � � n  i  } x: |  j j �  D]) \ } } | |  j k r5 | | | <q5 q5 W|  j d k r} |  j } n
 |  j } t |  j |  j	 |  j |  j
 | |  j |  j |  j |  j |  j |  j |  j |  j | � S(   Ns   %s has no anti particle.i   i   (   i   i   (   R?   t	   ExceptionR   R   t	   iteritemst   require_args_allR1   R-   R.   R/   R0   R2   R3   R5   R4   R6   R8   R9   R:   (   R	   t   outdict   kt   vt   newcolor(    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyt   anti�   s    	
+N(   R   R   R   R   RM   t   Nonet   Truet   FalseR   R@   RR   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR-   C   s   $3	t	   Parameterc           B   s,   e  Z d  d d d d g Z d d d � Z RS(   R   t   naturet   typeR   R4   c   	      C   s�   | | | | | f } t  j |  | � | | | | | f } t j |  � | d  k s_ | d  k r~ | d k r~ t d | � � n  | |  _ | |  _ d  S(   Nt   externals1   Need LHA information for external parameter "%s".(   R   R   t   all_parametersR>   RS   RK   t   lhablockt   lhacode(	   R	   R   RW   RX   R   R4   R[   R\   R
   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR   �   s    $	N(   R   R   R   RS   R   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyRV   �   s   t   CTParameterc           B   s8   e  Z d  d d d d g Z d �  Z d �  Z d �  Z RS(   R   s   nature,RX   R   R4   c         C   sT   | d | | | f } t  j |  | � | d | | | f } d |  _ t j |  � d  S(   Nt   internalt   interal(   R   R   RW   t   all_CTparametersR>   (   R	   R   RX   R   R4   R
   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR   �   s
    	c         C   s(   y |  j  d SWn t k
 r# d SXd  S(   Ni    t   ZERO(   R   t   KeyError(   R	   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyt   finite�   s    c         C   s)   y |  j  | SWn t k
 r$ d SXd  S(   NRa   (   R   Rb   (   R	   t   x(    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyt   pole�   s    (   R   R   R   R   Rc   Re   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR]   �   s   		t   Vertexc           B   s&   e  Z d  d d d d g Z d �  Z RS(   R   t	   particlesR1   t   lorentzt	   couplingsc         K   sK   | | | | | f } t  j |  | | � | | | | f } t j |  � d  S(   N(   R   R   t   all_verticesR>   (   R	   R   Rg   R1   Rh   Ri   t   optR
   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR   �   s    (   R   R   R   R   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyRf   �   s   t   CTVertexc           B   s,   e  Z d  d d d d d d g Z d �  Z RS(   R   Rg   R1   Rh   Ri   RX   t   loop_particlesc   
      K   sW   | | | | | | | f }	 t  j |  |	 | � | | | | | | f }	 t j |  � d  S(   N(   R   R   t   all_CTverticesR>   (
   R	   R   Rg   R1   Rh   Ri   RX   Rm   Rk   R
   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR   �   s    (   R   R   R   R   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyRl   �   s   t   Couplingc           B   sG   e  Z d  d d g Z d  d d d d g Z d �  Z d �  Z d �  Z RS(   R   R   t   orderRm   R7   c         K   s3   | | | f } t  j |  | | � t j |  � d  S(   N(   R   R   t   all_couplingsR>   (   R	   R   R   Rp   Rk   R
   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR   �   s    c         C   s   |  j  d � S(   Ni    (   Re   (   R	   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR   �   s    c         C   sV   t  |  j t � r; | |  j j �  k r4 |  j | Sd Sn  | d k rN |  j Sd Sd S(   s�    the self.value attribute can be a dictionary directly specifying the Laurent serie using normal
        parameter or just a string which can possibly contain CTparameter defining the Laurent serie.Ra   i    N(   RA   R   RB   t   keys(   R	   Rd   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyRe   �   s    (   R   R   R   RM   R   R   Re   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyRo   �   s
   		t   Lorentzc           B   s#   e  Z d  d d g Z d d � Z RS(   R   t   spinst	   structureRY   c         K   s3   | | | f } t  j |  | | � t j |  � d  S(   N(   R   R   t   all_lorentzR>   (   R	   R   Rt   Ru   Rk   R
   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR     s    (   R   R   R   R   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyRs     s   t   Functionc           B   s   e  Z d  �  Z d �  Z RS(   c         C   s,   t  j |  � | |  _ | |  _ | |  _ d  S(   N(   t   all_functionsR>   R   t	   argumentst   expr(   R	   R   Ry   t
   expression(    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR     s    		c         F   sC   x3 e  |  j � D]" \ } } d | | | f d  Uq We |  j � S(   Ns   %s = %s(   R   Ry   t   evalRz   (   R	   Rk   R   t   arg(    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyt   __call__(  s    (   R   R   R   R~   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyRw     s   		t   CouplingOrderc           B   s   e  Z d  d � Z RS(   i    c         C   s5   t  j |  � | |  _ | |  _ | |  _ | |  _ d  S(   N(   t
   all_ordersR>   R   t   expansion_ordert	   hierarchyt   perturbative_expansion(   R	   R   R�   R�   R�   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR   3  s
    			(   R   R   R   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR   1  s   t   Decayc           B   s   e  Z d  d g Z d �  Z RS(   t   particlet   partial_widthsc         K   s9   | | f } t  j |  | | � t j |  � | | _ d  S(   N(   R   R   t
   all_decaysR>   R�   (   R	   R�   R�   Rk   R
   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR   B  s    (   R   R   R   R   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR�   ?  s   t
   FormFactorc           B   s    e  Z d  d d g Z d �  Z RS(   R   RX   R   c         K   s3   | | | f } t  j |  | | � t j |  � d  S(   N(   R   R   t   all_form_factorsR>   (   R	   R   RX   R   Rk   R
   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR   Q  s    (   R   R   R   R   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR�   N  s   t
   Propagatorc           B   s#   e  Z d  d d g Z d d � Z RS(   R   t	   numeratort   denominatorc         K   s3   | | | f } t  j |  | | � t j |  � d  S(   N(   R   R   t   all_propagatorsR>   (   R	   R   R�   R�   Rk   R
   (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR   _  s    N(   R   R   R   RS   R   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyR�   [  s   (   t   cmatht   reRK   R    t   objectR   R=   R-   RZ   RV   R`   R]   Rj   Rf   Rn   Rl   Rq   Ro   Rv   Rs   Rx   Rw   R�   R   R�   R�   R�   R�   R�   R�   (    (    (    sN   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/object_library.pyt   <module>
   s6   0R                                                                                                                                                                                                                                                                      param_card.dat                                                                                      0000644 0276724 0002567 00000015077 13234357560 012167  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     ######################################################################
## PARAM_CARD AUTOMATICALY GENERATED BY THE UFO  #####################
######################################################################

###################################
## INFORMATION FOR SMINPUTS
###################################
Block SMINPUTS 
    1 1.279000e+02 # aEWM1 
    2 1.166370e-05 # Gf 
    3 1.184000e-01 # aS 

###################################
## INFORMATION FOR MASS
###################################
Block MASS 
    5 4.700000e+00 # MB 
    6 1.720000e+02 # MT 
   15 1.777000e+00 # MTA 
   23 9.118760e+01 # MZ 
   25 1.250000e+02 # MH 
  5000001 1.000000e+03 # MY1 
  5000511 1.000000e+01 # MXr 
  5000512 1.000000e+01 # MXc 
  5000521 1.000000e+01 # MXd 
##  Not dependent paramater.
## Those values should be edited following analytical the 
## analytical expression. Some generator could simply ignore 
## those values and use the analytical expression
  22 0.000000 # a : 0.0 
  24 79.824360 # W+ : cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2)))) 
  21 0.000000 # g : 0.0 
  9000001 0.000000 # ghA : 0.0 
  9000003 79.824360 # ghWp : cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2)))) 
  9000004 79.824360 # ghWm : cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2)))) 
  82 0.000000 # ghG : 0.0 
  12 0.000000 # ve : 0.0 
  14 0.000000 # vm : 0.0 
  16 0.000000 # vt : 0.0 
  11 0.000000 # e- : 0.0 
  13 0.000000 # mu- : 0.0 
  2 0.000000 # u : 0.0 
  4 0.000000 # c : 0.0 
  1 0.000000 # d : 0.0 
  3 0.000000 # s : 0.0 
  251 79.824360 # G+ : cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2)))) 
  9000002 91.187600 # ghZ : MZ 
  250 91.187600 # G0 : MZ 

###################################
## INFORMATION FOR DECAY
###################################
DECAY   6 1.508336e+00 
DECAY  23 2.495200e+00 
DECAY  24 2.085000e+00 
DECAY  25 4.070000e-03 
DECAY 5000001 1.000000e+01 
##  Not dependent paramater.
## Those values should be edited following analytical the 
## analytical expression. Some generator could simply ignore 
## those values and use the analytical expression
DECAY  22 0.000000 # a : 0.0 
DECAY  21 0.000000 # g : 0.0 
DECAY  9000001 0.000000 # ghA : 0.0 
DECAY  82 0.000000 # ghG : 0.0 
DECAY  12 0.000000 # ve : 0.0 
DECAY  14 0.000000 # vm : 0.0 
DECAY  16 0.000000 # vt : 0.0 
DECAY  11 0.000000 # e- : 0.0 
DECAY  13 0.000000 # mu- : 0.0 
DECAY  15 0.000000 # ta- : 0.0 
DECAY  2 0.000000 # u : 0.0 
DECAY  4 0.000000 # c : 0.0 
DECAY  1 0.000000 # d : 0.0 
DECAY  3 0.000000 # s : 0.0 
DECAY  5 0.000000 # b : 0.0 
DECAY  5000511 0.000000 # Xr : 0.0 
DECAY  5000512 0.000000 # Xc : 0.0 
DECAY  5000521 0.000000 # Xd : 0.0 
DECAY  9000002 2.495200 # ghZ : WZ 
DECAY  9000003 2.085000 # ghWp : WW 
DECAY  9000004 2.085000 # ghWm : WW 
DECAY  250 2.495200 # G0 : WZ 
DECAY  251 2.085000 # G+ : WW 

###################################
## INFORMATION FOR DMINPUTS
###################################
Block DMINPUTS 
    1 0.000000e+00 # gVXc 
    2 1.000000e+00 # gVXd 
    3 0.000000e+00 # gAXd 
    4 2.500000e-01 # gVd11 
    5 2.500000e-01 # gVu11 
    6 2.500000e-01 # gVd22 
    7 2.500000e-01 # gVu22 
    8 2.500000e-01 # gVd33 
    9 2.500000e-01 # gVu33 
   10 0.000000e+00 # gAd11 
   11 0.000000e+00 # gAu11 
   12 0.000000e+00 # gAd22 
   13 0.000000e+00 # gAu22 
   14 0.000000e+00 # gAd33 
   15 0.000000e+00 # gAu33 
   16 2.500000e-01 # gVu31 
   17 2.500000e-01 # gAu31 
   18 2.500000e-01 # gVd31 
   19 2.500000e-01 # gAd31 

###################################
## INFORMATION FOR LOOP
###################################
Block LOOP 
    1 9.118800e+01 # MU_R 

###################################
## INFORMATION FOR YUKAWA
###################################
Block YUKAWA 
    5 4.700000e+00 # ymb 
    6 1.720000e+02 # ymt 
   15 1.777000e+00 # ymtau 
#===========================================================
# QUANTUM NUMBERS OF NEW STATE(S) (NON SM PDG CODE)
#===========================================================

Block QNUMBERS 9000001  # ghA 
        1 0  # 3 times electric charge
        2 -1  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 9000002  # ghZ 
        1 0  # 3 times electric charge
        2 -1  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 9000003  # ghWp 
        1 3  # 3 times electric charge
        2 -1  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 9000004  # ghWm 
        1 -3  # 3 times electric charge
        2 -1  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 82  # ghG 
        1 0  # 3 times electric charge
        2 -1  # number of spin states (2S+1)
        3 8  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 250  # G0 
        1 0  # 3 times electric charge
        2 1  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 0  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 251  # G+ 
        1 3  # 3 times electric charge
        2 1  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 5000511  # Xr 
        1 0  # 3 times electric charge
        2 1  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 0  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 5000512  # Xc 
        1 0  # 3 times electric charge
        2 1  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 5000521  # Xd 
        1 0  # 3 times electric charge
        2 2  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 1  # Particle/Antiparticle distinction (0=own anti)
Block QNUMBERS 5000001  # Y1 
        1 0  # 3 times electric charge
        2 3  # number of spin states (2S+1)
        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 0  # Particle/Antiparticle distinction (0=own anti)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 parameters.py                                                                                       0000644 0276724 0002567 00000040521 13234357560 012111  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     # This file was automatically created by FeynRules 2.4.46
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Thu 27 Oct 2016 23:02:25



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
gVXc = Parameter(name = 'gVXc',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'g_{\\text{VXc}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 1 ])

gVXd = Parameter(name = 'gVXd',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{VXd}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 2 ])

gAXd = Parameter(name = 'gAXd',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'g_{\\text{AXd}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 3 ])

gVd11 = Parameter(name = 'gVd11',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 4 ])

gVu11 = Parameter(name = 'gVu11',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 5 ])

gVd22 = Parameter(name = 'gVd22',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 6 ])

gVu22 = Parameter(name = 'gVu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 7 ])

gVd33 = Parameter(name = 'gVd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 8 ])

gVu33 = Parameter(name = 'gVu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 9 ])

gVl11 = Parameter(name = 'gVl11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ve}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 10 ])

gVl22 = Parameter(name = 'gVl22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Vmu}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 11 ])

gVl33 = Parameter(name = 'gVl33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Vta}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 12 ])

gAd11 = Parameter(name = 'gAd11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ad11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 13 ])

gAu11 = Parameter(name = 'gAu11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Au11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 14 ])

gAd22 = Parameter(name = 'gAd22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ad22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 15 ])

gAu22 = Parameter(name = 'gAu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Au22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 16 ])

gAd33 = Parameter(name = 'gAd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ad33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 17 ])

gAu33 = Parameter(name = 'gAu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Au33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 18 ])

gAl11 = Parameter(name = 'gAl11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ae}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 19 ])

gAl22 = Parameter(name = 'gAl22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Amu}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 20 ])

gAl33 = Parameter(name = 'gAl33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ata}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 21 ])

gnu11 = Parameter(name = 'gnu11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{nue}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 22 ])

gnu22 = Parameter(name = 'gnu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{num}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 23 ])

gnu33 = Parameter(name = 'gnu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{nut}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 24 ])

gVu31 = Parameter(name = 'gVu31',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu31}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 25 ])

gAu31 = Parameter(name = 'gAu31',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Au31}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 26 ])

gVd31 = Parameter(name = 'gVd31',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd31}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 27 ])

gAd31 = Parameter(name = 'gAd31',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Ad31}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 28 ])

gVh = Parameter(name = 'gVh',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = 'g_{\\text{Vh}}',
                lhablock = 'DMINPUTS',
                lhacode = [ 29 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MXr = Parameter(name = 'MXr',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXr}',
                lhablock = 'MASS',
                lhacode = [ 5000511 ])

MXc = Parameter(name = 'MXc',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXc}',
                lhablock = 'MASS',
                lhacode = [ 5000512 ])

MXd = Parameter(name = 'MXd',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXd}',
                lhablock = 'MASS',
                lhacode = [ 5000521 ])

MY1 = Parameter(name = 'MY1',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MY1}',
                lhablock = 'MASS',
                lhacode = [ 5000001 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WY1 = Parameter(name = 'WY1',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{WY1}',
                lhablock = 'DECAY',
                lhacode = [ 5000001 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I1a33}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I4a33}')

                                                                                                                                                                               parameters.pyo                                                                                      0000644 0276724 0002567 00000017244 13234357560 012276  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc           @   s�  d  d l  m Z m Z d  d l m Z m Z m Z m Z m Z m	 Z	 m
 Z
 m Z e d d d d d d d	 d
 d d � Z e d d d d d d d	 d d d d d d d g � Z e d d d d d d d	 d d d d d d d g � Z e d d d d d d d	 d d d d d d d g � Z e d d d d d d d	 d d d d d d d g � Z e d d  d d d d d	 d! d d" d d d d# g � Z e d d$ d d d d d	 d! d d% d d d d& g � Z e d d' d d d d d	 d! d d( d d d d) g � Z e d d* d d d d d	 d! d d+ d d d d, g � Z e d d- d d d d d	 d! d d. d d d d/ g � Z e d d0 d d d d d	 d! d d1 d d d d2 g � Z e d d3 d d d d d	 d d d4 d d d d5 g � Z e d d6 d d d d d	 d d d7 d d d d8 g � Z e d d9 d d d d d	 d d d: d d d d; g � Z e d d< d d d d d	 d d d= d d d d> g � Z e d d? d d d d d	 d d d@ d d d dA g � Z e d dB d d d d d	 d d dC d d d dD g � Z e d dE d d d d d	 d d dF d d d dG g � Z e d dH d d d d d	 d d dI d d d dJ g � Z e d dK d d d d d	 d d dL d d d dM g � Z e d dN d d d d d	 d d dO d d d dP g � Z  e d dQ d d d d d	 d d dR d d d dS g � Z! e d dT d d d d d	 d d dU d d d dV g � Z" e d dW d d d d d	 d d dX d d d dY g � Z# e d dZ d d d d d	 d d d[ d d d d\ g � Z$ e d d] d d d d d	 d d d^ d d d d_ g � Z% e d d` d d d d d	 d! d da d d d db g � Z& e d dc d d d d d	 d! d dd d d d de g � Z' e d df d d d d d	 d! d dg d d d dh g � Z( e d di d d d d d	 d! d dj d d d dk g � Z) e d dl d d d d d	 d d dm d d d dn g � Z* e d do d d d d d	 dp d dq d dr d d g � Z+ e d ds d d d d d	 dt d du d dr d d g � Z, e d dv d d d d d	 dw d dx d dr d d g � Z- e d dy d d d d d	 dz d d{ d d| d d& g � Z. e d d} d d d d d	 d~ d d d d| d d) g � Z/ e d d� d d d d d	 d� d d� d d| d dD g � Z0 e d d� d d d d d	 d� d d� d d� d d\ g � Z1 e d d� d d d d d	 d� d d� d d� d dD g � Z2 e d d� d d d d d	 d~ d d� d d� d d) g � Z3 e d d� d d d d d	 dz d d� d d� d d& g � Z4 e d d� d d d d d	 d� d d� d d� d db g � Z5 e d d� d d d d d	 d� d d� d d� d d� g � Z6 e d d� d d d d d	 d� d d� d d� d d� g � Z7 e d d� d d d d d	 d� d d� d d� d d� g � Z8 e d d� d d d d d	 d� d d� d d� d d� g � Z9 e d d� d d d d d	 d� d d� d d� d d\ g � Z: e d d� d d d d d	 d� d d� d d� d d_ g � Z; e d d� d d d d d	 d� d d� d d� d d) g � Z< e d d� d d d d d	 d� d d� d d� d db g � Z= e d d� d d d d d	 d� d d� d d� d d� g � Z> e d d� d d d d d	 d� d d� � Z? e d d� d d d d d	 d� d d� � Z@ e d d� d d d d d	 d� d d� � ZA e d d� d d d d d	 d� d d� � ZB e d d� d d d d d	 d� d d� � ZC e d d� d d d d d	 d� d d� � ZD e d d� d d d d d	 d� d d� � ZE e d d� d d d d d	 d� d d� � ZF e d d� d d d d d	 d� d d� � ZG e d d� d d d d d	 d� d d� � ZH e d d� d d d d d	 d� d d� � ZI e d d� d d d d d	 d� d d� � ZJ e d d� d d d d d	 d� d d� � ZK e d d� d d d d d	 d� d d� � ZL e d d� d d d d d	 d� d d� � ZM e d d� d d d d� d	 d� d d� � ZN e d d� d d d d� d	 d� d d� � ZO e d d� d d d d� d	 d� d d� � ZP e d d� d d d d� d	 d� d d� � ZQ d� S(�   i����(   t   all_parameterst	   Parameter(   t   complexconjugatet   ret   imt   csct   sect   acsct   asect   cott   namet   ZEROt   naturet   internalt   typet   realt   values   0.0t   texnamet   0t   MU_Rt   externalgy�&1�V@s   \text{\mu_r}t   lhablockt   LOOPt   lhacodei   t   gVXcg        s   g_{\text{VXc}}t   DMINPUTSt   gVXdg      �?s   g_{\text{VXd}}i   t   gAXds   g_{\text{AXd}}i   t   gVd11g      �?s   g_{\text{Vd11}}i   t   gVu11s   g_{\text{Vu11}}i   t   gVd22s   g_{\text{Vd22}}i   t   gVu22s   g_{\text{Vu22}}i   t   gVd33s   g_{\text{Vd33}}i   t   gVu33s   g_{\text{Vu33}}i	   t   gVl11s   g_{\text{Ve}}i
   t   gVl22s   g_{\text{Vmu}}i   t   gVl33s   g_{\text{Vta}}i   t   gAd11s   g_{\text{Ad11}}i   t   gAu11s   g_{\text{Au11}}i   t   gAd22s   g_{\text{Ad22}}i   t   gAu22s   g_{\text{Au22}}i   t   gAd33s   g_{\text{Ad33}}i   t   gAu33s   g_{\text{Au33}}i   t   gAl11s   g_{\text{Ae}}i   t   gAl22s   g_{\text{Amu}}i   t   gAl33s   g_{\text{Ata}}i   t   gnu11s   g_{\text{nue}}i   t   gnu22s   g_{\text{num}}i   t   gnu33s   g_{\text{nut}}i   t   gVu31s   g_{\text{Vu31}}i   t   gAu31s   g_{\text{Au31}}i   t   gVd31s   g_{\text{Vd31}}i   t   gAd31s   g_{\text{Ad31}}i   t   gVhs   g_{\text{Vh}}i   t   aEWM1g������_@s   \text{aEWM1}t   SMINPUTSt   GfgÅ���u�>t   G_ft   aSg���_vO�?s	   \alpha _st   ymbg������@s
   \text{ymb}t   YUKAWAt   ymti�   s
   \text{ymt}t   ymtaug;�O��n�?s   \text{ymtau}t   MZg�.n��V@s	   \text{MZ}t   MASSt   MTAs
   \text{MTA}t   MTs	   \text{MT}t   MBs	   \text{MB}t   MHi}   s	   \text{MH}t   MXrg      $@s
   \text{MXr}i?ML t   MXcs
   \text{MXc}i@ML t   MXds
   \text{MXd}iIML t   MY1g     @�@s
   \text{MY1}iAKL t   WZgg��j+�@s	   \text{WZ}t   DECAYt   WWg�G�z� @s	   \text{WW}t   WTgj�~q%"�?s	   \text{WT}t   WHg��PN��p?s	   \text{WH}t   WY1s
   \text{WY1}t   aEWs   1/aEWM1s   \alpha _{\text{EW}}t   Gs%   2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)t   MWsU   cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))t   M_Wt   ees&   2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)t   et   sw2s   1 - MW**2/MZ**2s
   \text{sw2}t   cws   cmath.sqrt(1 - sw2)t   c_wt   sws   cmath.sqrt(sw2)t   s_wt   g1s   ee/cwt   g_1t   gws   ee/swt   g_wt   vevs   (2*MW*sw)/ees
   \text{vev}t   lams   MH**2/(2.*vev**2)s
   \text{lam}t   ybs   (ymb*cmath.sqrt(2))/vevs	   \text{yb}t   yts   (ymt*cmath.sqrt(2))/vevs	   \text{yt}t   ytaus   (ymtau*cmath.sqrt(2))/vevs   \text{ytau}t   muHs   cmath.sqrt(lam*vev**2)s   \mut   I1a33t   complexs   \text{I1a33}t   I2a33s   \text{I2a33}t   I3a33s   \text{I3a33}t   I4a33s   \text{I4a33}N(R   t   object_libraryR    R   t   function_libraryR   R   R   R   R   R   R   R	   R   R   R   R   R   R   R   R   R   R    R!   R"   R#   R$   R%   R&   R'   R(   R)   R*   R+   R,   R-   R.   R/   R0   R1   R2   R3   R4   R5   R6   R8   R:   R;   R=   R>   R?   RA   RB   RC   RD   RE   RF   RG   RH   RI   RK   RL   RM   RN   RO   RP   RQ   RS   RU   RV   RX   RZ   R\   R^   R_   R`   Ra   Rb   Rc   Rd   Rf   Rg   Rh   (    (    (    sJ   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/parameters.pyt   <module>   s�  :																			                                                                                                                                                                                                                                                                                                                                                            particles.py                                                                                        0000644 0276724 0002567 00000027417 13234357560 011745  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     # This file was automatically created by FeynRules 2.4.46
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Thu 27 Oct 2016 23:02:25


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

ghA = Particle(pdg_code = 9000001,
               name = 'ghA',
               antiname = 'ghA~',
               spin = -1,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghA',
               antitexname = 'ghA~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghA__tilde__ = ghA.anti()

ghZ = Particle(pdg_code = 9000002,
               name = 'ghZ',
               antiname = 'ghZ~',
               spin = -1,
               color = 1,
               mass = Param.MZ,
               width = Param.WZ,
               texname = 'ghZ',
               antitexname = 'ghZ~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghZ__tilde__ = ghZ.anti()

ghWp = Particle(pdg_code = 9000003,
                name = 'ghWp',
                antiname = 'ghWp~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWp',
                antitexname = 'ghWp~',
                charge = 1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWp__tilde__ = ghWp.anti()

ghWm = Particle(pdg_code = 9000004,
                name = 'ghWm',
                antiname = 'ghWm~',
                spin = -1,
                color = 1,
                mass = Param.MW,
                width = Param.WW,
                texname = 'ghWm',
                antitexname = 'ghWm~',
                charge = -1,
                GhostNumber = 1,
                LeptonNumber = 0,
                Y = 0)

ghWm__tilde__ = ghWm.anti()

ghG = Particle(pdg_code = 82,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1,
               LeptonNumber = 0,
               Y = 0)

ghG__tilde__ = ghG.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 1,
              Y = 0)

vt__tilde__ = vt.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.ZERO,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.ZERO,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       Y = 0)

ta__plus__ = ta__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

b__tilde__ = b.anti()

H = Particle(pdg_code = 25,
             name = 'H',
             antiname = 'H',
             spin = 1,
             color = 1,
             mass = Param.MH,
             width = Param.WH,
             texname = 'H',
             antitexname = 'H',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             Y = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.WZ,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     GhostNumber = 0,
                     LeptonNumber = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

Xr = Particle(pdg_code = 5000511,
              name = 'Xr',
              antiname = 'Xr',
              spin = 1,
              color = 1,
              mass = Param.MXr,
              width = Param.ZERO,
              texname = 'Xr',
              antitexname = 'Xr',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Xc = Particle(pdg_code = 5000512,
              name = 'Xc',
              antiname = 'Xc~',
              spin = 1,
              color = 1,
              mass = Param.MXc,
              width = Param.ZERO,
              texname = 'Xc',
              antitexname = 'Xc~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Xc__tilde__ = Xc.anti()

Xd = Particle(pdg_code = 5000521,
              name = 'Xd',
              antiname = 'Xd~',
              spin = 2,
              color = 1,
              mass = Param.MXd,
              width = Param.ZERO,
              texname = 'Xd',
              antitexname = 'Xd~',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

Xd__tilde__ = Xd.anti()

Y1 = Particle(pdg_code = 5000001,
              name = 'Y1',
              antiname = 'Y1',
              spin = 3,
              color = 1,
              mass = Param.MY1,
              width = Param.WY1,
              texname = 'Y1',
              antitexname = 'Y1',
              charge = 0,
              GhostNumber = 0,
              LeptonNumber = 0,
              Y = 0)

                                                                                                                                                                                                                                                 particles.pyo                                                                                       0000644 0276724 0002567 00000012451 13234357560 012114  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc           @   sv  d  d l  m Z d  d l m Z m Z d  d l Z d  d l Z e d d d d d d d	 d
 d d d e j	 d e j	 d d d d d d d d d d d d � Z
 e d d d d d d d	 d
 d d d e j d e j d d d d d d d d d d d d � Z e d d d d d d d	 d
 d d d e j d e j d d d d d d d d d d d d � Z e j �  Z e d d d d d d d	 d
 d d d e j	 d e j	 d d d d d d d d d d d d � Z e d d d d d d  d	 d  d d d e j	 d e j	 d d d d  d d d d d d d d � Z e j �  Z e d d! d d" d d# d	 d  d d d e j d e j d d" d d# d d d d d d d d � Z e j �  Z e d d$ d d% d d& d	 d  d d d e j d e j d d% d d& d d d d d d d d � Z e j �  Z e d d' d d( d d) d	 d  d d d e j d e j d d( d d) d d  d d d d d d � Z e j �  Z e d d* d d+ d d, d	 d  d d d e j	 d e j	 d d+ d d, d d d d d d d d � Z e j �  Z e d d- d d. d d/ d	 d0 d d d e j	 d e j	 d d. d d/ d d d d d d d d � Z e j �  Z e d d1 d d2 d d3 d	 d0 d d d e j	 d e j	 d d2 d d3 d d d d d d d d � Z  e  j �  Z! e d d4 d d5 d d6 d	 d0 d d d e j	 d e j	 d d5 d d6 d d d d d d d d � Z" e" j �  Z# e d d7 d d8 d d9 d	 d0 d d d e j	 d e j	 d d8 d d9 d d  d d d d d d � Z$ e$ j �  Z% e d d: d d; d d< d	 d0 d d d e j	 d e j	 d d; d d< d d  d d d d d d � Z& e& j �  Z' e d d= d d> d d? d	 d0 d d d e j( d e j	 d d> d d? d d  d d d d d d � Z) e) j �  Z* e d d0 d d@ d dA d	 d0 d d
 d e j	 d e j	 d d@ d dA d da d d d d d d � Z+ e+ j �  Z, e d dB d dC d dD d	 d0 d d
 d e j	 d e j	 d dC d dD d db d d d d d d � Z- e- j �  Z. e d dE d dF d dG d	 d0 d d
 d e j/ d e j0 d dF d dG d dc d d d d d d � Z1 e1 j �  Z2 e d d d dH d dI d	 d0 d d
 d e j	 d e j	 d dH d dI d dd d d d d d d � Z3 e3 j �  Z4 e d d
 d dJ d dK d	 d0 d d
 d e j	 d e j	 d dJ d dK d de d d d d d d � Z5 e5 j �  Z6 e d dL d dM d dN d	 d0 d d
 d e j7 d e j	 d dM d dN d df d d d d d d � Z8 e8 j �  Z9 e d dO d dP d dP d	 d d d d e j: d e j; d dP d dP d d d d d d d d � Z< e d dQ d dR d dR d	 d d d d e j d e j d dR d dR dS e= d d d d d d d d � Z> e d dT d dU d dV d	 d d d d e j d e j d dU d dV dS e= d d d d d d d d � Z? e? j �  Z@ e d dW d dX d dX d	 d d d d e jA d e j	 d dX d dX d d d d d d d d � ZB e d dY d dZ d d[ d	 d d d d e jC d e j	 d dZ d d[ d d d d d d d d � ZD eD j �  ZE e d d\ d d] d d^ d	 d0 d d d e jF d e j	 d d] d d^ d d d d d d d d � ZG eG j �  ZH e d d_ d d` d d` d	 d
 d d d e jI d e jJ d d` d d` d d d d d d d d � ZK d S(g   i����(   t   division(   t   all_particlest   ParticleNt   pdg_codei   t   namet   at   antinamet   spini   t   colori   t   masst   widtht   texnamet   antitexnamet   chargei    t   GhostNumbert   LeptonNumbert   Yi   t   Zi   s   W+s   W-i   t   gi   iAT� t   ghAs   ghA~iBT� t   ghZs   ghZ~iCT� t   ghWps   ghWp~iDT� t   ghWms   ghWm~iR   t   ghGs   ghG~i   t   ves   ve~i   i   t   vms   vm~i   t   vts   vt~i   s   e-s   e+i   s   mu-s   mu+i   s   ta-s   ta+t   us   u~i   t   cs   c~i   t   ts   t~t   ds   d~t   ss   s~i   t   bs   b~i   t   Hi�   t   G0t	   goldstonei�   s   G+s   G-i?ML t   Xri@ML t   Xcs   Xc~iIML t   Xds   Xd~iAKL t   Y1gUUUUUU�?gUUUUUU�?gUUUUUU�?gUUUUUUտgUUUUUUտgUUUUUUտ(L   t
   __future__R    t   object_libraryR   R   t
   parameterst   Paramt   propagatorst   Propt   ZEROR   t   MZt   WZR   t   MWt   WWt	   W__plus__t   antit
   W__minus__R   R   t   ghA__tilde__R   t   ghZ__tilde__R   t   ghWp__tilde__R   t   ghWm__tilde__R   t   ghG__tilde__R   t   ve__tilde__R   t   vm__tilde__R   t   vt__tilde__t
   e__minus__t	   e__plus__t   mu__minus__t
   mu__plus__t   MTAt   ta__minus__t
   ta__plus__R   t
   u__tilde__R   t
   c__tilde__t   MTt   WTR   t
   t__tilde__R   t
   d__tilde__R   t
   s__tilde__t   MBR    t
   b__tilde__t   MHt   WHR!   t   TrueR"   t	   G__plus__t
   G__minus__t   MXrR$   t   MXcR%   t   Xc__tilde__t   MXdR&   t   Xd__tilde__t   MY1t   WY1R'   (    (    (    sI   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/particles.pyt   <module>   s  																																																																																			                                                                                                                                                                                                                       propagators.py                                                                                      0000644 0276724 0002567 00000002507 13234357560 012311  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     # This file was automatically created  by FeynRules 2.0 (static file)
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (November 6, 2010)
# Date: Mon 1 Oct 2012 14:58:26

from object_library import all_propagators, Propagator


# define only once the denominator since this is always the same
denominator = "P('mu', id) * P('mu', id) - Mass(id) * Mass(id) + complex(0,1) * Mass(id) * Width(id)"

# propagator for the scalar
S = Propagator(name = "S",
               numerator = "complex(0,1)",
               denominator = denominator
               )

# propagator for the incoming fermion # the one for the outcomming is computed on the flight
F = Propagator(name = "F",
                numerator = "complex(0,1) * (Gamma('mu', 1, 2) * P('mu', id) + Mass(id) * Identity(1, 2))",
                denominator = denominator
               )

# massive vector in the unitary gauge, can't be use for massless particles
V1 = Propagator(name = "V1",
                numerator = "complex(0,1) * (-1 * Metric(1, 2) + Metric(1,'mu')* P('mu', id) * P(2, id) / Mass(id)**2 ",
                denominator = denominator
               )

# massless vector and massive vector in unitary gauge
V2 = Propagator(name = "V2",
                numerator = "complex(0,-1) * Metric(1, 2)",
                denominator =  "P('mu', id) * P('mu', id)"
               )


                                                                                                                                                                                         propagators.pyo                                                                                     0000644 0276724 0002567 00000001501 13234357560 012461  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc           @   s�   d  d l  m Z m Z d Z e d d d d d e � Z e d d d d	 d e � Z e d d
 d d d e � Z e d d d d d d � Z d S(   i����(   t   all_propagatorst
   PropagatorsU   P('mu', id) * P('mu', id) - Mass(id) * Mass(id) + complex(0,1) * Mass(id) * Width(id)t   namet   St	   numerators   complex(0,1)t   denominatort   FsL   complex(0,1) * (Gamma('mu', 1, 2) * P('mu', id) + Mass(id) * Identity(1, 2))t   V1sY   complex(0,1) * (-1 * Metric(1, 2) + Metric(1,'mu')* P('mu', id) * P(2, id) / Mass(id)**2 t   V2s   complex(0,-1) * Metric(1, 2)s   P('mu', id) * P('mu', id)N(   t   object_libraryR    R   R   R   R   R   R   (    (    (    sK   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/propagators.pyt   <module>   s   			                                                                                                                                                                                               vertices.py                                                                                         0000644 0276724 0002567 00000071461 13234357560 011601  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     # This file was automatically created by FeynRules 2.4.46
# Mathematica version: 10.3.0 for Mac OS X x86 (64-bit) (October 9, 2015)
# Date: Thu 27 Oct 2016 23:02:25


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.G0, P.G0, P.G0, P.G0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_49})

V_2 = Vertex(name = 'V_2',
             particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_47})

V_3 = Vertex(name = 'V_3',
             particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_48})

V_4 = Vertex(name = 'V_4',
             particles = [ P.G0, P.G0, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_47})

V_5 = Vertex(name = 'V_5',
             particles = [ P.G__minus__, P.G__plus__, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_47})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_49})

V_7 = Vertex(name = 'V_7',
             particles = [ P.G0, P.G0, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_75})

V_8 = Vertex(name = 'V_8',
             particles = [ P.G__minus__, P.G__plus__, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_75})

V_9 = Vertex(name = 'V_9',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_76})

V_10 = Vertex(name = 'V_10',
              particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_6})

V_11 = Vertex(name = 'V_11',
              particles = [ P.a, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_3})

V_12 = Vertex(name = 'V_12',
              particles = [ P.ghA, P.ghWm__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV3 ],
              couplings = {(0,0):C.GC_3})

V_13 = Vertex(name = 'V_13',
              particles = [ P.ghA, P.ghWp__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV3 ],
              couplings = {(0,0):C.GC_4})

V_14 = Vertex(name = 'V_14',
              particles = [ P.ghWm, P.ghA__tilde__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_82})

V_15 = Vertex(name = 'V_15',
              particles = [ P.ghWm, P.ghA__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV3 ],
              couplings = {(0,0):C.GC_3})

V_16 = Vertex(name = 'V_16',
              particles = [ P.ghWm, P.ghWm__tilde__, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_77})

V_17 = Vertex(name = 'V_17',
              particles = [ P.ghWm, P.ghWm__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_78})

V_18 = Vertex(name = 'V_18',
              particles = [ P.ghWm, P.ghWm__tilde__, P.a ],
              color = [ '1' ],
              lorentz = [ L.UUV3 ],
              couplings = {(0,0):C.GC_4})

V_19 = Vertex(name = 'V_19',
              particles = [ P.ghWm, P.ghWm__tilde__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.UUV3 ],
              couplings = {(0,0):C.GC_60})

V_20 = Vertex(name = 'V_20',
              particles = [ P.ghWm, P.ghZ__tilde__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_85})

V_21 = Vertex(name = 'V_21',
              particles = [ P.ghWm, P.ghZ__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1, L.UUV2 ],
              couplings = {(0,0):C.GC_59,(0,1):C.GC_59})

V_22 = Vertex(name = 'V_22',
              particles = [ P.ghWp, P.ghA__tilde__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_81})

V_23 = Vertex(name = 'V_23',
              particles = [ P.ghWp, P.ghA__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1, L.UUV2 ],
              couplings = {(0,0):C.GC_4,(0,1):C.GC_4})

V_24 = Vertex(name = 'V_24',
              particles = [ P.ghWp, P.ghWp__tilde__, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_80})

V_25 = Vertex(name = 'V_25',
              particles = [ P.ghWp, P.ghWp__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_78})

V_26 = Vertex(name = 'V_26',
              particles = [ P.ghWp, P.ghWp__tilde__, P.a ],
              color = [ '1' ],
              lorentz = [ L.UUV1, L.UUV2 ],
              couplings = {(0,0):C.GC_3,(0,1):C.GC_3})

V_27 = Vertex(name = 'V_27',
              particles = [ P.ghWp, P.ghWp__tilde__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.UUV1, L.UUV2 ],
              couplings = {(0,0):C.GC_59,(0,1):C.GC_59})

V_28 = Vertex(name = 'V_28',
              particles = [ P.ghWp, P.ghZ__tilde__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_84})

V_29 = Vertex(name = 'V_29',
              particles = [ P.ghWp, P.ghZ__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1, L.UUV2 ],
              couplings = {(0,0):C.GC_60,(0,1):C.GC_60})

V_30 = Vertex(name = 'V_30',
              particles = [ P.ghZ, P.ghWm__tilde__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_86})

V_31 = Vertex(name = 'V_31',
              particles = [ P.ghZ, P.ghWm__tilde__, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1, L.UUV2 ],
              couplings = {(0,0):C.GC_59,(0,1):C.GC_59})

V_32 = Vertex(name = 'V_32',
              particles = [ P.ghZ, P.ghWp__tilde__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_83})

V_33 = Vertex(name = 'V_33',
              particles = [ P.ghZ, P.ghWp__tilde__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.UUV1, L.UUV2 ],
              couplings = {(0,0):C.GC_60,(0,1):C.GC_60})

V_34 = Vertex(name = 'V_34',
              particles = [ P.ghZ, P.ghZ__tilde__, P.H ],
              color = [ '1' ],
              lorentz = [ L.UUS1 ],
              couplings = {(0,0):C.GC_87})

V_35 = Vertex(name = 'V_35',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1, L.UUV2 ],
              couplings = {(0,0):C.GC_10,(0,1):C.GC_10})

V_36 = Vertex(name = 'V_36',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
              couplings = {(0,0):C.GC_10,(0,1):C.GC_12,(0,2):C.GC_12,(0,3):C.GC_10,(0,4):C.GC_10,(0,5):C.GC_12})

V_37 = Vertex(name = 'V_37',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
              couplings = {(1,0):C.GC_14,(0,0):C.GC_14,(2,1):C.GC_14,(0,1):C.GC_13,(2,2):C.GC_13,(1,2):C.GC_13})

V_38 = Vertex(name = 'V_38',
              particles = [ P.t__tilde__, P.b, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3, L.FFS5 ],
              couplings = {(0,0):C.GC_43,(0,1):C.GC_44})

V_39 = Vertex(name = 'V_39',
              particles = [ P.b__tilde__, P.b, P.G0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3, L.FFS5 ],
              couplings = {(0,0):C.GC_89,(0,1):C.GC_91})

V_40 = Vertex(name = 'V_40',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3, L.FFS5 ],
              couplings = {(0,0):C.GC_90,(0,1):C.GC_90})

V_41 = Vertex(name = 'V_41',
              particles = [ P.vt__tilde__, P.ta__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_95})

V_42 = Vertex(name = 'V_42',
              particles = [ P.ta__plus__, P.ta__minus__, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_96})

V_43 = Vertex(name = 'V_43',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS6 ],
              couplings = {(0,0):C.GC_97})

V_44 = Vertex(name = 'V_44',
              particles = [ P.b__tilde__, P.t, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3, L.FFS5 ],
              couplings = {(0,0):C.GC_45,(0,1):C.GC_46})

V_45 = Vertex(name = 'V_45',
              particles = [ P.t__tilde__, P.t, P.G0 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS4 ],
              couplings = {(0,0):C.GC_93})

V_46 = Vertex(name = 'V_46',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS6 ],
              couplings = {(0,0):C.GC_92})

V_47 = Vertex(name = 'V_47',
              particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_62})

V_48 = Vertex(name = 'V_48',
              particles = [ P.a, P.W__minus__, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_61})

V_49 = Vertex(name = 'V_49',
              particles = [ P.a, P.W__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_81})

V_50 = Vertex(name = 'V_50',
              particles = [ P.W__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_55})

V_51 = Vertex(name = 'V_51',
              particles = [ P.W__minus__, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_53})

V_52 = Vertex(name = 'V_52',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV9 ],
              couplings = {(0,0):C.GC_4})

V_53 = Vertex(name = 'V_53',
              particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_62})

V_54 = Vertex(name = 'V_54',
              particles = [ P.a, P.W__plus__, P.G__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_63})

V_55 = Vertex(name = 'V_55',
              particles = [ P.a, P.W__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_82})

V_56 = Vertex(name = 'V_56',
              particles = [ P.W__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_54})

V_57 = Vertex(name = 'V_57',
              particles = [ P.W__plus__, P.G__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_53})

V_58 = Vertex(name = 'V_58',
              particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_50})

V_59 = Vertex(name = 'V_59',
              particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_50})

V_60 = Vertex(name = 'V_60',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_50})

V_61 = Vertex(name = 'V_61',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_79})

V_62 = Vertex(name = 'V_62',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV5 ],
              couplings = {(0,0):C.GC_5})

V_63 = Vertex(name = 'V_63',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV9 ],
              couplings = {(0,0):C.GC_60})

V_64 = Vertex(name = 'V_64',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV5 ],
              couplings = {(0,0):C.GC_51})

V_65 = Vertex(name = 'V_65',
              particles = [ P.Y1, P.Xc__tilde__, P.Xc ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_41})

V_66 = Vertex(name = 'V_66',
              particles = [ P.b__tilde__, P.b, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_18,(0,0):C.GC_33})

V_67 = Vertex(name = 'V_67',
              particles = [ P.d__tilde__, P.b, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_17,(0,0):C.GC_32})

V_68 = Vertex(name = 'V_68',
              particles = [ P.c__tilde__, P.c, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_23,(0,0):C.GC_38})

V_69 = Vertex(name = 'V_69',
              particles = [ P.b__tilde__, P.d, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_17,(0,0):C.GC_32})

V_70 = Vertex(name = 'V_70',
              particles = [ P.d__tilde__, P.d, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_15,(0,0):C.GC_30})

V_71 = Vertex(name = 'V_71',
              particles = [ P.e__plus__, P.e__minus__, P.Y1 ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_19,(0,0):C.GC_34})

V_72 = Vertex(name = 'V_72',
              particles = [ P.mu__plus__, P.mu__minus__, P.Y1 ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_20,(0,0):C.GC_35})

V_73 = Vertex(name = 'V_73',
              particles = [ P.s__tilde__, P.s, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_16,(0,0):C.GC_31})

V_74 = Vertex(name = 'V_74',
              particles = [ P.ta__plus__, P.ta__minus__, P.Y1 ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_21,(0,0):C.GC_36})

V_75 = Vertex(name = 'V_75',
              particles = [ P.t__tilde__, P.t, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_25,(0,0):C.GC_40})

V_76 = Vertex(name = 'V_76',
              particles = [ P.u__tilde__, P.t, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_24,(0,0):C.GC_39})

V_77 = Vertex(name = 'V_77',
              particles = [ P.t__tilde__, P.u, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_24,(0,0):C.GC_39})

V_78 = Vertex(name = 'V_78',
              particles = [ P.u__tilde__, P.u, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_22,(0,0):C.GC_37})

V_79 = Vertex(name = 'V_79',
              particles = [ P.Xd__tilde__, P.Xd, P.Y1 ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_26,(0,0):C.GC_42})

V_80 = Vertex(name = 'V_80',
              particles = [ P.ta__plus__, P.vt, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_94})

V_81 = Vertex(name = 'V_81',
              particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_70})

V_82 = Vertex(name = 'V_82',
              particles = [ P.Z, P.G0, P.H ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_67})

V_83 = Vertex(name = 'V_83',
              particles = [ P.Z, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_68})

V_84 = Vertex(name = 'V_84',
              particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_85 = Vertex(name = 'V_85',
              particles = [ P.W__minus__, P.Z, P.G__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_86 = Vertex(name = 'V_86',
              particles = [ P.W__minus__, P.Z, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_74})

V_87 = Vertex(name = 'V_87',
              particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_88 = Vertex(name = 'V_88',
              particles = [ P.W__plus__, P.Z, P.G__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_89 = Vertex(name = 'V_89',
              particles = [ P.W__plus__, P.Z, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_73})

V_90 = Vertex(name = 'V_90',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_64})

V_91 = Vertex(name = 'V_91',
              particles = [ P.Z, P.Z, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_72})

V_92 = Vertex(name = 'V_92',
              particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_71})

V_93 = Vertex(name = 'V_93',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_72})

V_94 = Vertex(name = 'V_94',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_88})

V_95 = Vertex(name = 'V_95',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV5 ],
              couplings = {(0,0):C.GC_52})

V_96 = Vertex(name = 'V_96',
              particles = [ P.ve__tilde__, P.ve, P.Y1 ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_27})

V_97 = Vertex(name = 'V_97',
              particles = [ P.vm__tilde__, P.vm, P.Y1 ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_28})

V_98 = Vertex(name = 'V_98',
              particles = [ P.vt__tilde__, P.vt, P.Y1 ],
              color = [ '1' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_29})

V_99 = Vertex(name = 'V_99',
              particles = [ P.e__plus__, P.e__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_100 = Vertex(name = 'V_100',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_101 = Vertex(name = 'V_101',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_102 = Vertex(name = 'V_102',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_103 = Vertex(name = 'V_103',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_104 = Vertex(name = 'V_104',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_105 = Vertex(name = 'V_105',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_106 = Vertex(name = 'V_106',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_107 = Vertex(name = 'V_107',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_108 = Vertex(name = 'V_108',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_109 = Vertex(name = 'V_109',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_110 = Vertex(name = 'V_110',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_111 = Vertex(name = 'V_111',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_112 = Vertex(name = 'V_112',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_113 = Vertex(name = 'V_113',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_11})

V_114 = Vertex(name = 'V_114',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_56})

V_115 = Vertex(name = 'V_115',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_56})

V_116 = Vertex(name = 'V_116',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_56})

V_117 = Vertex(name = 'V_117',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_56})

V_118 = Vertex(name = 'V_118',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_56})

V_119 = Vertex(name = 'V_119',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_56})

V_120 = Vertex(name = 'V_120',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_56})

V_121 = Vertex(name = 'V_121',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_56})

V_122 = Vertex(name = 'V_122',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_56})

V_123 = Vertex(name = 'V_123',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_56})

V_124 = Vertex(name = 'V_124',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_56})

V_125 = Vertex(name = 'V_125',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_56})

V_126 = Vertex(name = 'V_126',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_58,(0,1):C.GC_65})

V_127 = Vertex(name = 'V_127',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_58,(0,1):C.GC_65})

V_128 = Vertex(name = 'V_128',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_58,(0,1):C.GC_65})

V_129 = Vertex(name = 'V_129',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_57,(0,1):C.GC_65})

V_130 = Vertex(name = 'V_130',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_57,(0,1):C.GC_65})

V_131 = Vertex(name = 'V_131',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_57,(0,1):C.GC_65})

V_132 = Vertex(name = 'V_132',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_69})

V_133 = Vertex(name = 'V_133',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_69})

V_134 = Vertex(name = 'V_134',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_69})

V_135 = Vertex(name = 'V_135',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_57,(0,1):C.GC_66})

V_136 = Vertex(name = 'V_136',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_57,(0,1):C.GC_66})

V_137 = Vertex(name = 'V_137',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV8 ],
               couplings = {(0,0):C.GC_57,(0,1):C.GC_66})

                                                                                                                                                                                                               vertices.pyo                                                                                        0000644 0276724 0002567 00000046323 13234357560 011757  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc           @   sP,  d  d l  m Z m Z d  d l Z d  d l Z d  d l Z e d d d e j	 e j	 e j	 e j	 g d d g d e j
 g d	 i e j d� 6� Z e d d d e j	 e j	 e j e j g d d g d e j
 g d	 i e j d� 6� Z e d d d e j e j e j e j g d d g d e j
 g d	 i e j d� 6� Z e d d d e j	 e j	 e j e j g d d g d e j
 g d	 i e j d� 6� Z e d d d e j e j e j e j g d d g d e j
 g d	 i e j d� 6� Z e d d d e j e j e j e j g d d g d e j
 g d	 i e j d� 6� Z e d d d e j	 e j	 e j g d d g d e j g d	 i e j d� 6� Z e d d d e j e j e j g d d g d e j g d	 i e j d� 6� Z e d d d e j e j e j g d d g d e j g d	 i e j d� 6� Z e d d d e j e j e j e j g d d g d e j g d	 i e j d� 6� Z  e d d d e j e j e j g d d g d e j! g d	 i e j" d� 6� Z# e d d d e j$ e j% e j& g d d g d e j' g d	 i e j" d� 6� Z( e d d d e j$ e j) e j* g d d g d e j' g d	 i e j+ d� 6� Z, e d d d e j- e j. e j g d d g d e j/ g d	 i e j0 d� 6� Z1 e d d d e j- e j. e j* g d d g d e j' g d	 i e j" d� 6� Z2 e d d d e j- e j% e j	 g d d g d e j/ g d	 i e j3 d� 6� Z4 e d d d e j- e j% e j g d d g d e j/ g d	 i e j5 d� 6� Z6 e d d d e j- e j% e j g d d g d e j' g d	 i e j+ d� 6� Z7 e d d d e j- e j% e j8 g d d g d e j' g d	 i e j9 d� 6� Z: e d d d e j- e j; e j g d d g d e j/ g d	 i e j< d� 6� Z= e d d d e j- e j; e j* g d d g d e j> e j? g d	 i e j@ d� 6e j@ d� 6� ZA e d d  d e jB e j. e j g d d g d e j/ g d	 i e jC d� 6� ZD e d d! d e jB e j. e j& g d d g d e j> e j? g d	 i e j+ d� 6e j+ d� 6� ZE e d d" d e jB e j) e j	 g d d g d e j/ g d	 i e jF d� 6� ZG e d d# d e jB e j) e j g d d g d e j/ g d	 i e j5 d� 6� ZH e d d$ d e jB e j) e j g d d g d e j> e j? g d	 i e j" d� 6e j" d� 6� ZI e d d% d e jB e j) e j8 g d d g d e j> e j? g d	 i e j@ d� 6e j@ d� 6� ZJ e d d& d e jB e j; e j g d d g d e j/ g d	 i e jK d� 6� ZL e d d' d e jB e j; e j& g d d g d e j> e j? g d	 i e j9 d� 6e j9 d� 6� ZM e d d( d e jN e j% e j g d d g d e j/ g d	 i e jO d� 6� ZP e d d) d e jN e j% e j& g d d g d e j> e j? g d	 i e j@ d� 6e j@ d� 6� ZQ e d d* d e jN e j) e j g d d g d e j/ g d	 i e jR d� 6� ZS e d d+ d e jN e j) e j* g d d g d e j> e j? g d	 i e j9 d� 6e j9 d� 6� ZT e d d, d e jN e j; e j g d d g d e j/ g d	 i e jU d� 6� ZV e d d- d e jW e jX e jY g d d. g d e j> e j? g d	 i e jZ d� 6e jZ d� 6� Z[ e d d/ d e jY e jY e jY g d d. g d e j\ e j] e j^ e j_ e j` e ja g d	 i e jZ d� 6e jb d� 6e jb d� 6e jZ d� 6e jZ d� 6e jb d� 6� Zc e d d4 d e jY e jY e jY e jY g d d5 d6 d7 g d e jd e je e jf g d	 i e jg d� 6e jg d� 6e jg d� 6e jh d� 6e jh d� 6e jh d� 6� Zi e d d8 d e jj e jk e j g d d9 g d e jl e jm g d	 i e jn d� 6e jo d� 6� Zp e d d: d e jq e jk e j	 g d d9 g d e jl e jm g d	 i e jr d� 6e js d� 6� Zt e d d; d e jq e jk e j g d d9 g d e jl e jm g d	 i e ju d� 6e ju d� 6� Zv e d d< d e jw e jx e j g d d g d e jl g d	 i e jy d� 6� Zz e d d= d e j{ e jx e j	 g d d g d e j| g d	 i e j} d� 6� Z~ e d d> d e j{ e jx e j g d d g d e j g d	 i e j� d� 6� Z� e d d? d e jq e j� e j g d d9 g d e jl e jm g d	 i e j� d� 6e j� d� 6� Z� e d d@ d e jj e j� e j	 g d d9 g d e j| g d	 i e j� d� 6� Z� e d dA d e jj e j� e j g d d9 g d e j g d	 i e j� d� 6� Z� e d dB d e j e j& e j	 e j g d d g d e j g d	 i e j� d� 6� Z� e d dC d e j e j& e j e j g d d g d e j g d	 i e j� d� 6� Z� e d dD d e j e j& e j g d d g d e j� g d	 i e jC d� 6� Z� e d dE d e j& e j	 e j g d d g d e j! g d	 i e j� d� 6� Z� e d dF d e j& e j e j g d d g d e j! g d	 i e j� d� 6� Z� e d dG d e j e j& e j* g d d g d e j� g d	 i e j+ d� 6� Z� e d dH d e j e j* e j	 e j g d d g d e j g d	 i e j� d� 6� Z� e d dI d e j e j* e j e j g d d g d e j g d	 i e j� d� 6� Z� e d dJ d e j e j* e j g d d g d e j� g d	 i e j0 d� 6� Z� e d dK d e j* e j	 e j g d d g d e j! g d	 i e j� d� 6� Z� e d dL d e j* e j e j g d d g d e j! g d	 i e j� d� 6� Z� e d dM d e j& e j* e j	 e j	 g d d g d e j g d	 i e j� d� 6� Z� e d dN d e j& e j* e j e j g d d g d e j g d	 i e j� d� 6� Z� e d dO d e j& e j* e j e j g d d g d e j g d	 i e j� d� 6� Z� e d dP d e j& e j* e j g d d g d e j� g d	 i e j� d� 6� Z� e d dQ d e j e j e j& e j* g d d g d e j� g d	 i e j� d� 6� Z� e d dR d e j& e j* e j8 g d d g d e j� g d	 i e j9 d� 6� Z� e d dS d e j& e j& e j* e j* g d d g d e j� g d	 i e j� d� 6� Z� e d dT d e j� e j� e j� g d d g d e j! g d	 i e j� d� 6� Z� e d dU d e jq e jk e j� g d d9 g d e j� e j� g d	 i e j� d� 6e j� d� 6� Z� e d dV d e j� e jk e j� g d d9 g d e j� e j� g d	 i e j� d� 6e j� d� 6� Z� e d dW d e j� e j� e j� g d d9 g d e j� e j� g d	 i e j� d� 6e j� d� 6� Z� e d dX d e jq e j� e j� g d d9 g d e j� e j� g d	 i e j� d� 6e j� d� 6� Z� e d dY d e j� e j� e j� g d d9 g d e j� e j� g d	 i e j� d� 6e j� d� 6� Z� e d dZ d e j� e j� e j� g d d g d e j� e j� g d	 i e j� d� 6e j� d 6� Z� e d d[ d e j� e j� e j� g d d g d e j� e j� g d	 i e j� d6e j� d6� Z� e d d\ d e j� e j� e j� g d d9 g d e j� e j� g d	 i e j� d6e j� d6� Z� e d d] d e j{ e jx e j� g d d g d e j� e j� g d	 i e j� d6e j� d6� Z� e d d^ d e jj e j� e j� g d d9 g d e j� e j� g d	 i e j� d6e j� d6� Z� e d d_ d e j� e j� e j� g d d9 g d e j� e j� g d	 i e j� d	6e j� d
6� Z� e d d` d e jj e j� e j� g d d9 g d e j� e j� g d	 i e j� d6e j� d6� Z� e d da d e j� e j� e j� g d d9 g d e j� e j� g d	 i e j� d6e j� d6� Z� e d db d e j� e j� e j� g d d g d e j� e j� g d	 i e j� d6e j� d6� Z� e d dc d e j{ e j� e j g d d g d e jm g d	 i e j� d6� Z� e d dd d e j e j8 e j e j g d d g d e j g d	 i e j� d6� Z� e d de d e j8 e j	 e j g d d g d e j! g d	 i e j� d6� Z� e d df d e j8 e j e j g d d g d e j! g d	 i e j� d6� Z� e d dg d e j& e j8 e j	 e j g d d g d e j g d	 i e j� d6� Z� e d dh d e j& e j8 e j e j g d d g d e j g d	 i e j� d6� Z� e d di d e j& e j8 e j g d d g d e j� g d	 i e j� d6� Z� e d dj d e j* e j8 e j	 e j g d d g d e j g d	 i e j� d6� Z� e d dk d e j* e j8 e j e j g d d g d e j g d	 i e j� d6� Z� e d dl d e j* e j8 e j g d d g d e j� g d	 i e j� d6� Z� e d dm d e j e j& e j* e j8 g d d g d e j� g d	 i e j� d6� Z� e d dn d e j8 e j8 e j	 e j	 g d d g d e j g d	 i e j� d6� Z� e d do d e j8 e j8 e j e j g d d g d e j g d	 i e j� d6� Z� e d dp d e j8 e j8 e j e j g d d g d e j g d	 i e j� d6� Z� e d dq d e j8 e j8 e j g d d g d e j� g d	 i e j d6� Ze d dr d e j& e j* e j8 e j8 g d d g d e j� g d	 i e jd 6� Ze d ds d e je je j� g d d g d e jg d	 i e jd!6� Ze d dt d e j	e j
e j� g d d g d e jg d	 i e jd"6� Ze d du d e jw e j� e j� g d d g d e jg d	 i e jd#6� Ze d dv d e j� e j� e j g d d g d e j� g d	 i e j" d$6� Ze d dw d e j� e j� e j g d d g d e j� g d	 i e j" d%6� Ze d dx d e j{ e jx e j g d d g d e j� g d	 i e j" d&6� Ze d dy d e j� e j� e j g d d9 g d e j� g d	 i e jd'6� Ze d dz d e j� e j� e j g d d9 g d e j� g d	 i e jd(6� Ze d d{ d e jj e j� e j g d d9 g d e j� g d	 i e jd)6� Ze d d| d e j� e j� e j g d d9 g d e j� g d	 i e jd*6� Ze d d} d e j� e j� e j g d d9 g d e j� g d	 i e jd+6� Ze d d~ d e jq e jk e j g d d9 g d e j� g d	 i e jd,6� Ze d d d e j� e j� e jY g d d� g d e j� g d	 i e jd-6� Ze d d� d e j� e j� e jY g d d� g d e j� g d	 i e jd.6� Ze d d� d e jj e j� e jY g d d� g d e j� g d	 i e jd/6� Ze d d� d e j� e j� e jY g d d� g d e j� g d	 i e jd06� Ze d d� d e j� e j� e jY g d d� g d e j� g d	 i e jd16� Ze d d� d e jq e jk e jY g d d� g d e j� g d	 i e jd26� Z e d d� d e j� e j� e j& g d d9 g d e jg d	 i e j!d36� Z"e d d� d e j� e j� e j& g d d9 g d e jg d	 i e j!d46� Z#e d d� d e jq e j� e j& g d d9 g d e jg d	 i e j!d56� Z$e d d� d e j� e j� e j* g d d9 g d e jg d	 i e j!d66� Z%e d d� d e j� e j� e j* g d d9 g d e jg d	 i e j!d76� Z&e d d� d e jj e jk e j* g d d9 g d e jg d	 i e j!d86� Z'e d d� d e j� e je j& g d d g d e jg d	 i e j!d96� Z(e d d� d e j� e j
e j& g d d g d e jg d	 i e j!d:6� Z)e d d� d e j{ e j� e j& g d d g d e jg d	 i e j!d;6� Z*e d d� d e je j� e j* g d d g d e jg d	 i e j!d<6� Z+e d d� d e j	e j� e j* g d d g d e jg d	 i e j!d=6� Z,e d d� d e jw e jx e j* g d d g d e jg d	 i e j!d>6� Z-e d d� d e j� e j� e j8 g d d9 g d e je j.g d	 i e j/d?6e j0d@6� Z1e d d� d e j� e j� e j8 g d d9 g d e je j.g d	 i e j/dA6e j0dB6� Z2e d d� d e jj e j� e j8 g d d9 g d e je j.g d	 i e j/dC6e j0dD6� Z3e d d� d e j� e j� e j8 g d d9 g d e je j4g d	 i e j5dE6e j0dF6� Z6e d d� d e j� e j� e j8 g d d9 g d e je j4g d	 i e j5dG6e j0dH6� Z7e d d� d e jq e jk e j8 g d d9 g d e je j4g d	 i e j5dI6e j0dJ6� Z8e d d� d e je je j8 g d d g d e jg d	 i e j9dK6� Z:e d d� d e j	e j
e j8 g d d g d e jg d	 i e j9dL6� Z;e d d� d e jw e j� e j8 g d d g d e jg d	 i e j9dM6� Z<e d d� d e j� e j� e j8 g d d g d e je j=g d	 i e j5dN6e j>dO6� Z?e d d� d e j� e j� e j8 g d d g d e je j=g d	 i e j5dP6e j>dQ6� Z@e d d� d e j{ e jx e j8 g d d g d e je j=g d	 i e j5dR6e j>dS6� ZAd S(T  i����(   t   all_verticest   VertexNt   namet   V_1t	   particlest   colort   1t   lorentzt	   couplingsi    t   V_2t   V_3t   V_4t   V_5t   V_6t   V_7t   V_8t   V_9t   V_10t   V_11t   V_12t   V_13t   V_14t   V_15t   V_16t   V_17t   V_18t   V_19t   V_20t   V_21i   t   V_22t   V_23t   V_24t   V_25t   V_26t   V_27t   V_28t   V_29t   V_30t   V_31t   V_32t   V_33t   V_34t   V_35s   f(1,2,3)t   V_36i   i   i   i   t   V_37s   f(-1,1,2)*f(3,4,-1)s   f(-1,1,3)*f(2,4,-1)s   f(-1,1,4)*f(2,3,-1)t   V_38s   Identity(1,2)t   V_39t   V_40t   V_41t   V_42t   V_43t   V_44t   V_45t   V_46t   V_47t   V_48t   V_49t   V_50t   V_51t   V_52t   V_53t   V_54t   V_55t   V_56t   V_57t   V_58t   V_59t   V_60t   V_61t   V_62t   V_63t   V_64t   V_65t   V_66t   V_67t   V_68t   V_69t   V_70t   V_71t   V_72t   V_73t   V_74t   V_75t   V_76t   V_77t   V_78t   V_79t   V_80t   V_81t   V_82t   V_83t   V_84t   V_85t   V_86t   V_87t   V_88t   V_89t   V_90t   V_91t   V_92t   V_93t   V_94t   V_95t   V_96t   V_97t   V_98t   V_99t   V_100t   V_101t   V_102t   V_103t   V_104t   V_105t   V_106t   V_107t   V_108s   T(3,2,1)t   V_109t   V_110t   V_111t   V_112t   V_113t   V_114t   V_115t   V_116t   V_117t   V_118t   V_119t   V_120t   V_121t   V_122t   V_123t   V_124t   V_125t   V_126t   V_127t   V_128t   V_129t   V_130t   V_131t   V_132t   V_133t   V_134t   V_135t   V_136t   V_137(   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i   (   i    i    (   i    i    (   i    i   (   i    i    (   i    i    (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i    (   i    i   (   i    i    (   i    i    (   i    i   (   i    i    (   i    i    (   i    i   (   i    i    (   i    i    (   i    i   (   i    i    (   i    i   (   i    i   (   i    i   (   i    i   (   i    i   (   i   i    (   i    i    (   i   i   (   i    i   (   i   i   (   i   i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i    (   i    i    (   i    i    (   i    i   (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i    (   i    i    (   i    i    (   i    i   (   i    i    (   i    i   (   i    i    (   i    i   (B  t   object_libraryR    R   R   t   PR   t   CR   t   Lt   G0t   SSSS1t   GC_49R   t
   G__minus__t	   G__plus__t   GC_47R	   t   GC_48R
   t   HR   R   R   t   SSS1t   GC_75R   R   t   GC_76R   t   at   VVSS1t   GC_6R   t   VSS1t   GC_3R   t   ghAt   ghWm__tilde__t
   W__minus__t   UUV3R   t   ghWp__tilde__t	   W__plus__t   GC_4R   t   ghWmt   ghA__tilde__t   UUS1t   GC_82R   R   t   GC_77R   t   GC_78R   R   t   Zt   GC_60R   t   ghZ__tilde__t   GC_85R   t   UUV1t   UUV2t   GC_59R   t   ghWpt   GC_81R   R   t   GC_80R   R    R!   R"   t   GC_84R#   R$   t   ghZt   GC_86R%   R&   t   GC_83R'   R(   t   GC_87R)   t   ghGt   ghG__tilde__t   gt   GC_10R*   t   VVV3t   VVV4t   VVV5t   VVV6t   VVV7t   VVV8t   GC_12R+   t   VVVV2t   VVVV3t   VVVV4t   GC_14t   GC_13R,   t
   t__tilde__t   bt   FFS3t   FFS5t   GC_43t   GC_44R-   t
   b__tilde__t   GC_89t   GC_91R.   t   GC_90R/   t   vt__tilde__t   ta__minus__t   GC_95R0   t
   ta__plus__t   FFS4t   GC_96R1   t   FFS6t   GC_97R2   t   tt   GC_45t   GC_46R3   t   GC_93R4   t   GC_92R5   t   GC_62R6   t   GC_61R7   t   VVS1R8   t   GC_55R9   t   GC_53R:   t   VVV9R;   R<   t   GC_63R=   R>   t   GC_54R?   R@   t   GC_50RA   RB   RC   t   GC_79RD   t   VVVV5t   GC_5RE   RF   t   GC_51RG   t   Y1t   Xc__tilde__t   Xct   GC_41RH   t   FFV1t   FFV2t   GC_18t   GC_33RI   t
   d__tilde__t   GC_17t   GC_32RJ   t
   c__tilde__t   ct   GC_23t   GC_38RK   t   dRL   t   GC_15t   GC_30RM   t	   e__plus__t
   e__minus__t   GC_19t   GC_34RN   t
   mu__plus__t   mu__minus__t   GC_20t   GC_35RO   t
   s__tilde__t   st   GC_16t   GC_31RP   t   GC_21t   GC_36RQ   t   GC_25t   GC_40RR   t
   u__tilde__t   GC_24t   GC_39RS   t   uRT   t   GC_22t   GC_37RU   t   Xd__tilde__t   Xdt   GC_26t   GC_42RV   t   vtt   GC_94RW   t   GC_70RX   t   GC_67RY   t   GC_68RZ   t   GC_8R[   t   GC_9R\   t   GC_74R]   R^   t   GC_7R_   t   GC_73R`   t   VVVV6t   GC_64Ra   t   GC_72Rb   t   GC_71Rc   Rd   t   GC_88Re   t   GC_52Rf   t   ve__tilde__t   vet   FFV3t   GC_27Rg   t   vm__tilde__t   vmt   GC_28Rh   t   GC_29Ri   Rj   Rk   Rl   t   GC_2Rm   Rn   Ro   t   GC_1Rp   Rq   Rr   t   GC_11Rs   Rt   Ru   Rv   Rw   Rx   t   GC_56Ry   Rz   R{   R|   R}   R~   R   R�   R�   R�   R�   R�   t   FFV9t   GC_58t   GC_65R�   R�   R�   t   FFV5t   GC_57R�   R�   R�   t   GC_69R�   R�   R�   t   FFV8t   GC_66R�   R�   R�   (    (    (    sH   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/vertices.pyt   <module>   s`  																																				*EE																																																																																																				                                                                                                                                                                                                                                                                                                             write_param_card.py                                                                                 0000644 0276724 0002567 00000017425 13234357560 013260  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     
__date__ = "02 Aug 2012"
__author__ = 'olivier.mattelaer@uclouvain.be'

from function_library import *

class ParamCardWriter(object):
    
    header = \
    """######################################################################\n""" + \
    """## PARAM_CARD AUTOMATICALY GENERATED BY THE UFO  #####################\n""" + \
    """######################################################################\n"""   
    
    def __init__(self, filename, list_of_parameters=None, generic=False):
        """write a valid param_card.dat"""
        
        if not list_of_parameters:
            from parameters import all_parameters
            list_of_parameters = [param for param in all_parameters if \
                                                       param.nature=='external']
        
        self.generic_output = generic
        if generic:
            self.define_not_dep_param(list_of_parameters)

        
        self.fsock = open(filename, 'w')
        self.fsock.write(self.header)
        
        self.write_card(list_of_parameters)
        self.fsock.close()
    
    def define_not_dep_param(self, list_of_parameters):
        """define self.dep_mass and self.dep_width in case that they are 
        requested in the param_card.dat"""
        from particles import all_particles
        
        self.dep_mass = [(part, part.mass) for part in all_particles \
                            if part.pdg_code > 0 and \
                                            part.mass not in list_of_parameters]
        self.dep_width = [(part, part.width) for part in all_particles\
                             if part.pdg_code > 0 and \
                                part.width not in list_of_parameters]        
    
    @staticmethod
    def order_param(obj1, obj2):
        """ order parameter of a given block """
        
        maxlen = min([len(obj1.lhacode), len(obj2.lhacode)])
    
        for i in range(maxlen):
            if obj1.lhacode[i] < obj2.lhacode[i]:
                return -1
            elif obj1.lhacode[i] == obj2.lhacode[i]:
                return 0
            else:
                return 1
        #identical up to the first finish
        if len(obj1.lhacode) > len(obj2.lhacode):
            return 1
        elif  len(obj1.lhacode) == len(obj2.lhacode):
            return 0
        else:
            return -1
        
    def write_card(self, all_ext_param):
        """ """
        
        # list all lhablock
        all_lhablock = set([param.lhablock for param in all_ext_param])
        
        # ordonate lhablock alphabeticaly
        all_lhablock = list(all_lhablock)
        all_lhablock.sort()
        # put at the beginning SMINPUT + MASS + DECAY
        for name in ['DECAY', 'MASS','SMINPUTS']:
            if name in all_lhablock:
                all_lhablock.remove(name)
                all_lhablock.insert(0, name)
        
        for lhablock in all_lhablock:
            self.write_block(lhablock)
            need_writing = [ param for param in all_ext_param if \
                                                     param.lhablock == lhablock]
            need_writing.sort(self.order_param)
            [self.write_param(param, lhablock) for param in need_writing]
            
            if self.generic_output:
                if lhablock in ['MASS', 'DECAY']:
                    self.write_dep_param_block(lhablock)

        if self.generic_output:
            self.write_qnumber()
                               
    def write_block(self, name):
        """ write a comment for a block"""
        
        self.fsock.writelines(
        """\n###################################""" + \
        """\n## INFORMATION FOR %s""" % name.upper() +\
        """\n###################################\n"""
         )
        if name!='DECAY':
            self.fsock.write("""Block %s \n""" % name)

    def write_param(self, param, lhablock):
        
        lhacode=' '.join(['%3s' % key for key in param.lhacode])
        if lhablock != 'DECAY':
            text = """  %s %e # %s \n""" % (lhacode, complex(param.value).real, param.name ) 
        else:
            text = '''DECAY %s %e \n''' % (lhacode, complex(param.value).real)
        self.fsock.write(text) 
                    


    
    def write_dep_param_block(self, lhablock):
        import cmath
        from parameters import all_parameters
        from particles import all_particles
        for parameter in all_parameters:
            exec("%s = %s" % (parameter.name, parameter.value))
        text = "##  Not dependent paramater.\n"
        text += "## Those values should be edited following analytical the \n"
        text += "## analytical expression. Some generator could simply ignore \n"
        text += "## those values and use the analytical expression\n"
        
        if lhablock == 'MASS':
            data = self.dep_mass
            prefix = " "
        else:
            data = self.dep_width
            prefix = "DECAY "

        for part, param in data:
            if isinstance(param.value, str):
                value = complex(eval(param.value)).real
            else:
                value = param.value
            
            text += """%s %s %f # %s : %s \n""" %(prefix, part.pdg_code, 
                        value, part.name, param.value)
        # If more than a particles has the same mass/width we need to write it here
        # as well
        if lhablock == 'MASS':
            arg = 'mass'
            done = [part for (part, param) in self.dep_mass]
        else:
            arg = 'width'
            done = [part for (part, param) in self.dep_width]
        for particle in all_particles:
            if particle.pdg_code <0:
                continue
            is_define = True
            if particle not in done:
                if getattr(particle, arg).lhacode[0] != particle.pdg_code:
                    is_define = False                
            if  not is_define:
                value = float(particle.get(arg).value )
                name =  particle.get(arg).name 
                text += """%s %s %f # %s : %s \n""" %(prefix, particle.pdg_code, 
                        value, particle.name, name)




        self.fsock.write(text)    
        
    sm_pdg = [1,2,3,4,5,6,11,12,13,13,14,15,16,21,22,23,24,25]
    data="""Block QNUMBERS %(pdg)d  # %(name)s 
        1 %(charge)d  # 3 times electric charge
        2 %(spin)d  # number of spin states (2S+1)
        3 %(color)d  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 %(antipart)d  # Particle/Antiparticle distinction (0=own anti)\n"""
    
    def write_qnumber(self):
        """ write qnumber """
        from particles import all_particles
        import particles
        print particles.__file__
        text="""#===========================================================\n"""
        text += """# QUANTUM NUMBERS OF NEW STATE(S) (NON SM PDG CODE)\n"""
        text += """#===========================================================\n\n"""
        
        for part in all_particles:
            if part.pdg_code in self.sm_pdg or part.pdg_code < 0:
                continue
            text += self.data % {'pdg': part.pdg_code,
                                 'name': part.name,
                                 'charge': 3 * part.charge,
                                 'spin': part.spin,
                                 'color': part.color,
                                 'antipart': part.name != part.antiname and 1 or 0}
        
        self.fsock.write(text)
        
            
            
            
            
        
            
if '__main__' == __name__:
    ParamCardWriter('./param_card.dat', generic=True)
    print 'write ./param_card.dat'
    
                                                                                                                                                                                                                                           write_param_card.pyo                                                                                0000644 0276724 0002567 00000015636 13234357560 013441  0                                                                                                    ustar   ebhal                           zh                                                                                                                                                                                                                     �
�i�Xc           @   sT   d  Z  d Z d d l Td e f d �  �  YZ d e k rP e d d e �d	 GHn  d
 S(   s   02 Aug 2012s   olivier.mattelaer@uclouvain.bei����(   t   *t   ParamCardWriterc           B   s�   e  Z d  d d  Z d e d � Z d �  Z e d �  � Z d �  Z	 d �  Z
 d �  Z d �  Z d	 d
 d d d d d d d d d d d d d d d d g Z d Z d �  Z RS(   sG   ######################################################################
sG   ## PARAM_CARD AUTOMATICALY GENERATED BY THE UFO  #####################
c         C   s�   | sA d d l  m } g  | D] } | j d k r | ^ q } n  | |  _ | r` |  j | � n  t | d � |  _ |  j j |  j � |  j	 | � |  j j
 �  d S(   s   write a valid param_card.dati����(   t   all_parameterst   externalt   wN(   t
   parametersR   t   naturet   generic_outputt   define_not_dep_paramt   opent   fsockt   writet   headert
   write_cardt   close(   t   selft   filenamet   list_of_parameterst   genericR   t   param(    (    sP   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/write_param_card.pyt   __init__   s    	c         C   s�   d d l  m } g  | D]3 } | j d k r | j | k r | | j f ^ q |  _ g  | D]3 } | j d k rZ | j | k rZ | | j f ^ qZ |  _ d S(   sf   define self.dep_mass and self.dep_width in case that they are 
        requested in the param_card.dati����(   t   all_particlesi    N(   t	   particlesR   t   pdg_codet   masst   dep_masst   widtht	   dep_width(   R   R   R   t   part(    (    sP   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/write_param_card.pyR   !   s    'c         C   s�   t  t |  j � t | j � g � } xT t | � D]F } |  j | | j | k  rU d S|  j | | j | k rs d Sd Sq1 Wt |  j � t | j � k r� d St |  j � t | j � k r� d Sd Sd S(   s"    order parameter of a given block i����i    i   N(   t   mint   lent   lhacodet   range(   t   obj1t   obj2t   maxlent   i(    (    sP   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/write_param_card.pyt   order_param-   s    $c         C   s9  t  g  | D] } | j ^ q
 � } t | � } | j �  xC d d d g D]2 } | | k rH | j | � | j d | � qH qH Wx� | D]� } |  j | � g  | D] } | j | k r� | ^ q� } | j |  j � g  | D] } |  j | | � ^ q� |  j	 r� | d k r|  j
 | � qq� q� W|  j	 r5|  j �  n  d S(   t    t   DECAYt   MASSt   SMINPUTSi    N(   s   MASSs   DECAY(   t   sett   lhablockt   listt   sortt   removet   insertt   write_blockR%   t   write_paramR   t   write_dep_param_blockt   write_qnumber(   R   t   all_ext_paramR   t   all_lhablockt   nameR+   t   need_writing(    (    sP   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/write_param_card.pyR   B   s$    "
#		c         C   sI   |  j  j d d | j �  d � | d k rE |  j  j d | � n  d S(   s    write a comment for a blocks$   
###################################s   
## INFORMATION FOR %ss%   
###################################
R'   s
   Block %s 
N(   R
   t
   writelinest   upperR   (   R   R6   (    (    sP   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/write_param_card.pyR0   _   s
    	c         C   s�   d j  g  | j D] } d | ^ q � } | d k rZ d | t | j � j | j f } n d | t | j � j f } |  j j | � d  S(   NR&   s   %3sR'   s     %s %e # %s 
s   DECAY %s %e 
(   t   joinR   t   complext   valuet   realR6   R
   R   (   R   R   R+   t   keyR   t   text(    (    sP   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/write_param_card.pyR1   j   s
    )%c         B   sE  d d  l  } d d l m } d d l m } x& | D] } d | j | j f d  Uq3 Wd } | d 7} | d 7} | d 7} | d	 k r� |  j } d
 } n |  j } d } xp | D]h \ }	 }
 e	 |
 j e
 � r� e e |
 j � � j } n	 |
 j } | d | |	 j | |	 j |
 j f 7} q� W| d	 k rPd } g  |  j D] \ }	 }
 |	 ^ q5} n( d } g  |  j D] \ }	 }
 |	 ^ q`} x� | D]� } | j d k  r�qn  e } | | k r�e | | � j d | j k r�e } q�n  | se | j | � j � } | j | � j } | d | | j | | j | f 7} qqW|  j j | � d  S(   Ni����(   R   (   R   s   %s = %ss   ##  Not dependent paramater.
s;   ## Those values should be edited following analytical the 
s>   ## analytical expression. Some generator could simply ignore 
s2   ## those values and use the analytical expression
R(   R&   s   DECAY s   %s %s %f # %s : %s 
R   R   i    (   t   cmathR   R   R   R   R6   R<   R   R   t
   isinstancet   strR;   t   evalR=   R   t   Truet   getattrR   t   Falset   floatt   getR
   R   (   R   R+   R@   R   R   t	   parameterR?   t   datat   prefixR   R   R<   t   argt   donet   particlet	   is_defineR6   (    (    sP   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/write_param_card.pyR2   v   sL    


				%"i   i   i   i   i   i   i   i   i   i   i   i   i   i   i   i   i   s  Block QNUMBERS %(pdg)d  # %(name)s 
        1 %(charge)d  # 3 times electric charge
        2 %(spin)d  # number of spin states (2S+1)
        3 %(color)d  # colour rep (1: singlet, 3: triplet, 8: octet)
        4 %(antipart)d  # Particle/Antiparticle distinction (0=own anti)
c         C   s�   d d l  m } d d l  } | j GHd } | d 7} | d 7} x� | D]� } | j |  j k sE | j d k  rr qE n  | |  j i | j d 6| j d	 6d
 | j d 6| j d 6| j	 d 6| j | j
 k r� d p� d d 67} qE W|  j j | � d S(   s    write qnumber i����(   R   Ns=   #===========================================================
s4   # QUANTUM NUMBERS OF NEW STATE(S) (NON SM PDG CODE)
s>   #===========================================================

i    t   pdgR6   i   t   charget   spint   colori   t   antipart(   R   R   t   __file__R   t   sm_pdgRJ   R6   RQ   RR   RS   t   antinameR
   R   (   R   R   R   R?   R   (    (    sP   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/write_param_card.pyR3   �   s     

!


(N(   t   __name__t
   __module__R   t   NoneRF   R   R   t   staticmethodR%   R   R0   R1   R2   RV   RJ   R3   (    (    (    sP   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/write_param_card.pyR      s   					4<t   __main__s   ./param_card.datR   s   write ./param_card.datN(   t   __date__t
   __author__t   function_libraryt   objectR   RX   RD   (    (    (    sP   /group/hepheno/heptools/MG5_aMC_v2_5_2/models/DMsimp_s_spin1/write_param_card.pyt   <module>   s   
�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  