# leptoquark-datacards
Datacards for CMS LQ mg5_aMC@NLO production for legacy analyses.

LQ_S3: uses the scalar S3 LQ model from the Leptoquark Toolbox: https://lqnlo.hepforge.org, https://arxiv.org/abs/1801.07641

S3 is a triplet scalar model, with the following resonances:
```
S3p23: +2/3 charge leptoquark
S3m13: -1/3 charge leptoquark
S3m43: -4/3 charge leptoquark
```

The mass of the 3 resonances can be controlled with a single parameter MS3.

So, for example, to make pair production of LQ -> b + mu, you could do:
```
generate p p > S3m43 S3m43* , ( S3m43 > mu- b ) , (S3m43* > mu+ b~)
```
Similarly for LQ -> b + tau:
```
generate p p > S3m43 S3m43* , ( S3m43 > ta- b ) , (S3m43* > ta+ b~)
```
Similarly you could do incusive production of LQ -> b + tau / t + taunu, where you need to use 2 different charged LQs:
```
generate p p > S3m43 S3m43* ,    ( S3m43 > ta- b ) , (S3m43* > ta+ b~)
add process p p > S3m43 S3p23* , ( S3m43 > ta- b ) , (S3p23* > vt~ t~)
add process p p > S3p23 S3m43* , ( S3m43 > vt t ) , (S3m43* > ta+ b~)
add process p p > S3p23 S3p23* , ( S3p23 > vt t ) , (S3p23* > vt t)
```

From these three, all combinations of LQ->l+q decays can be made, as long as charge conservation is obeyed.

The model has the following Yukawa couplings, defined in the run_card:

BLOCK YUKS3LL # 

      1 1 3.000000e-01 # yll1x1
      1 2 3.000000e-01 # yll1x2
      1 3 3.000000e-01 # yll1x3
      2 1 3.000000e-01 # yll2x1
      2 2 3.000000e-01 # yll2x2
      2 3 3.000000e-01 # yll2x3
      3 1 3.000000e-01 # yll3x1
      3 2 3.000000e-01 # yll3x2
      3 3 3.000000e-01 # yll3x3

The format is yll(quark family)x(lepton family). You can set whatever value you like for the decay in question and set the rest to zero. Or you can just leave the others non-zero - as long as you don't allow those decays it shouldn't matter.

For example:
```
yll1x1=u/d + e/nue
yll1x2=u/d + mu/numu
yll1x3=u/d + tau/nutau
yll2x1=c/s + e/nue
etc…..
yll3x3=b/t + tau/nutau
```
The explicit decays and l-q pairings can be found in particles.py:
```
Decay_S3m13 = Decay(name = 'Decay_S3m13',
                    particle = P.S3m13,
                    partial_widths = {(P.b,P.ve):'((-MB**2 + MS3**2)*(-3*MB**2*yLL3x1**2 + 3*MS3**2*yLL3x1**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.b,P.vm):'((-MB**2 + MS3**2)*(-3*MB**2*yLL3x2**2 + 3*MS3**2*yLL3x2**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.b,P.vt):'((-MB**2 + MS3**2)*(-3*MB**2*yLL3x3**2 + 3*MS3**2*yLL3x3**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.c,P.e__minus__):'(MS3**4*yLL2x1**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.c,P.mu__minus__):'(MS3**4*yLL2x2**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.c,P.ta__minus__):'((MS3**2 - MTA**2)*(3*MS3**2*yLL2x3**2 - 3*MTA**2*yLL2x3**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.d,P.ve):'(MS3**4*yLL1x1**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.d,P.vm):'(MS3**4*yLL1x2**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.d,P.vt):'(MS3**4*yLL1x3**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.e__minus__,P.t):'((MS3**2 - MT**2)*(3*MS3**2*yLL3x1**2 - 3*MT**2*yLL3x1**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.e__minus__,P.u):'(MS3**4*yLL1x1**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.mu__minus__,P.t):'((MS3**2 - MT**2)*(3*MS3**2*yLL3x2**2 - 3*MT**2*yLL3x2**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.mu__minus__,P.u):'(MS3**4*yLL1x2**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.s,P.ve):'(MS3**4*yLL2x1**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.s,P.vm):'(MS3**4*yLL2x2**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.s,P.vt):'(MS3**4*yLL2x3**2)/(16.*cmath.pi*abs(MS3)**3)',
                                      (P.t,P.ta__minus__):'((3*MS3**2*yLL3x3**2 - 3*MT**2*yLL3x3**2 - 3*MTA**2*yLL3x3**2)*cmath.sqrt(MS3**4 - 2*MS3**2*MT**2 + MT**4 - 2*MS3**2*MTA**2 - 2*MT**2*MTA**2 + MTA**4))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.ta__minus__,P.u):'((MS3**2 - MTA**2)*(3*MS3**2*yLL1x3**2 - 3*MTA**2*yLL1x3**2))/(48.*cmath.pi*abs(MS3)**3)'})

Decay_S3m43 = Decay(name = 'Decay_S3m43',
                    particle = P.S3m43,
                    partial_widths = {(P.b,P.e__minus__):'((-MB**2 + MS3**2)*(-6*MB**2*yLL3x1**2 + 6*MS3**2*yLL3x1**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.b,P.mu__minus__):'((-MB**2 + MS3**2)*(-6*MB**2*yLL3x2**2 + 6*MS3**2*yLL3x2**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.b,P.ta__minus__):'((-6*MB**2*yLL3x3**2 + 6*MS3**2*yLL3x3**2 - 6*MTA**2*yLL3x3**2)*cmath.sqrt(MB**4 - 2*MB**2*MS3**2 + MS3**4 - 2*MB**2*MTA**2 - 2*MS3**2*MTA**2 + MTA**4))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.d,P.e__minus__):'(MS3**4*yLL1x1**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.d,P.mu__minus__):'(MS3**4*yLL1x2**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.d,P.ta__minus__):'((MS3**2 - MTA**2)*(6*MS3**2*yLL1x3**2 - 6*MTA**2*yLL1x3**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.e__minus__,P.s):'(MS3**4*yLL2x1**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.mu__minus__,P.s):'(MS3**4*yLL2x2**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.s,P.ta__minus__):'((MS3**2 - MTA**2)*(6*MS3**2*yLL2x3**2 - 6*MTA**2*yLL2x3**2))/(48.*cmath.pi*abs(MS3)**3)'})

Decay_S3p23 = Decay(name = 'Decay_S3p23',
                    particle = P.S3p23,
                    partial_widths = {(P.c,P.ve):'(MS3**4*yLL2x1**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.c,P.vm):'(MS3**4*yLL2x2**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.c,P.vt):'(MS3**4*yLL2x3**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.t,P.ve):'((MS3**2 - MT**2)*(6*MS3**2*yLL3x1**2 - 6*MT**2*yLL3x1**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.t,P.vm):'((MS3**2 - MT**2)*(6*MS3**2*yLL3x2**2 - 6*MT**2*yLL3x2**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.t,P.vt):'((MS3**2 - MT**2)*(6*MS3**2*yLL3x3**2 - 6*MT**2*yLL3x3**2))/(48.*cmath.pi*abs(MS3)**3)',
                                      (P.u,P.ve):'(MS3**4*yLL1x1**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.u,P.vm):'(MS3**4*yLL1x2**2)/(8.*cmath.pi*abs(MS3)**3)',
                                      (P.u,P.vt):'(MS3**4*yLL1x3**2)/(8.*cmath.pi*abs(MS3)**3)'})
```
