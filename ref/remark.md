# Adaptive Differential Evolution With Sorting Crossover Rate for Continuous Optimization Problems 



## JARGON 

1. **promising area** 
2. 

## Some views

1. The  performance of DE is strongly affected by the parameter settings or choice of mutation strategies.  



## contributions

1. An adaptive p setting is proposed, instead of a fixed p value in original JADE. Setting the p value larger at the beginning of the iteration can enhance the global search ability, and then adaptively decreasing the value helps to strengthen the local search ability.
2.  Sorting CR mechanism is added. After sorting the CR set and individuals set according to their values and fitness, respectively, the better individual is assigned with smaller CR value, which helps to maintain the better scheme that the better individual contains.
3. A scheme [retention](保留) mechanism is proposed to maintain the components from the mutant vector of the better offspring. It can improve JADE’s local search ability by providing the deep search around the individuals 

## Details of the ADAPTIVE DIFFERENTIAL EVOLUTION ALGORITHM WITH SORTING CR 

1.  DE/Current-to-pbest/1/ Strategy 
2. Archive Set 
3. Parameters Adaption Strategy 
4. CR Sorting Mechanism 
5. Better Scheme Retention Mechanism 

## Experiments

1. 

### comparison Method 

1. jDE [16], SaDE [17], EPSDE [19], JADE [20], and CoDE [30] 

## 例句

1. no fixed parameters setting can be [omnipotent](万能的) for
   all kinds of problems. 
2. [rendering](致使) the mutation operation meaningless in
   this case 
3. the population will not [convergent](adj. [数] 收敛的；会聚性的；趋集于一点的) to the same best individual 
4. 

## 需要找到的CODE

1. SaDE 的 code
2. 