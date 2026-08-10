Binding energy is what responsible for the difference (mass defect) between the mass of an atom and the sum of the number of protons and neutrons in it. The force responsible of it is called the **strong force**. 

Direct calculation of binding energy is not possible because in a nucleus, the particles are tightly bounded (perturbative methods have poor convergence) and it is a many body problem with all particles of the same mass. The nucleons also move at large speeds and need to use relativistic approximation. 

The usual notation for an element is $$^A_ZX$$ where $A$ is the mass number (proton + neutron), $Z$ is the number of proton and $X$ is the elemental symbol.

---

Here we use the liquid drop model to approximate a formula for binding energies: 
$$
\begin{aligned}
B(A, Z) = E_{\text{Volume}} - E_{\text{Surface}} - E_{\text{Coulomb}} - E_{\text{Asymmetry}} \pm E_{\text{Pairing}} \\
= a_V A - a_s A^{2/3} - a_c \frac{Z^2}{A^{1/3}} - a_a \frac{(N - Z)^2}{4A} + \frac{\delta}{A^{1/2}}
\end{aligned}
$$


### Volume term, $E_{\text{Volume}} = a_V A$
The attractive strong force between nucleons implies that it is energetically favourable for a nucleon to surround itself with other surrounding nucleons, inducing a binding energy between them. 

Since $4\pi R^3 / 3 \propto A$, we expect this term to scale with $A$ 


### Surface term, $E_{\text{Surface}} = a_S A^{2/3}$
Here we consider the particle at the edge of the surface where are have less binding energy as compared to the ones at the centre because they are surrounded by less nucleons. 

This term, following from the scaling factor as outlined in volume term, scales with $R^2 = A^{2/3}$ 


### Coulomb term, $E_{\text{Coulomb}} = a_C Z^2/A^{1/3}$
The protons have the same charge so they repel each other, implying a weaker binding energy. 

Coulomb potential scales as $V = a/r$ so we expect this term to be scaling with $1/R = A^{-1/3}$ 


## Asymmetry term, $E_{\text{Asymmetry}} = a_a (N-Z)^2/4A$
This term involves [Pauli exclusion principle](Physics%20Note/Exchange%20Operators%20and%20Pauli%20Exclusion%20Principle.md). Since protons and neutrons are fermions, they cannot lie in the same state. Consider that we have $n$ protons and neutrons and each of them fill $n$ lowest energy state. If we try to replace a neutron with a proton, it has to occupy the upper energy level, hence reducing the binding energy. In other words, the symmetric number of neutrons and protons can be packed tighter.

![Coulomb term diagram](Physics%20Note%20Figures/Pasted%20image%2020260416150415.png)

This term measures the difference between the number of neutrons and protons i.e. it is proportional to $N-Z$ 


### Pairing term, $E_{\text{Pairing}} = \delta/A^{1/2}$
Nuclei with even numbers of protons and neutrons are more stable because two different nucleons with opposite spin can be on the same shell. If we have odd number of protons/neutrons, the third spin has to be in the next shell. 

