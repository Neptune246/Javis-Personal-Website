import re
from pathlib import Path

mapping = {
    'Lattice Type': 'Physics Note/CMP/Lattice Type.md',
    'Lattice structure': 'Physics Note/CMP/Lattice structure.md',
    'Reciprocal Lattice': 'Physics Note/CMP/Reciprocal Lattice.md',
    'X-ray Diffraction': 'Physics Note/CMP/X-ray Diffraction.md',
    'Bonding': 'Physics Note/CMP/Bonding.md',
    'Lattice vibration': 'Physics Note/CMP/Lattice vibration.md',
    'Heat Capacity': 'Physics Note/CMP/Heat Capacity.md',
    'Debye Model 1': 'Physics Note/Debye Model 1.md',
    'Metal 1': 'Physics Note/Metal 1.md',
    'Metal II': 'Physics Note/Metal II.md',
    'Properties of free electron model (continuous)': 'Physics Note/Properties of free electron model (continuous).md',
    'Band Theory': 'Physics Note/Band Theory.md',
    "Bloch's theorem": "Physics Note/Bloch's theorem.md",
    'Introduction and Bonding': 'Physics Note/Introduction and Bonding.md',
    'Length Scales and Time Scales': 'Physics Note/Length Scales and Time Scales.md',
    'Lattices and Symmetry Operations': 'Physics Note/Lattices and Symmetry Operations.md',
    'Reading Character Tables': 'Physics Note/Reading Character Tables.md',
    'Selection Rules and Properties of Broken Symmetry': 'Physics Note/Selection Rules and Properties of Broken Symmetry.md',
    'Crystallographic Space Groups': 'Physics Note/Crystallographic Space Groups.md',
    'Scattering Techniques': 'Physics Note/Scattering Techniques.md',
    'Measuring Phonons': 'Physics Note/Measuring Phonons.md',
    'Phonon Dispersion Curves': 'Physics Note/Phonon Dispersion Curves.md',
    'Soft Modes and Displacive Phase Transition': 'Physics Note/Soft Modes and Displacive Phase Transition.md',
    'Semiconductor Physics': 'Physics Note/Semiconductor Physics.md',
    'Electronic Transition In Semiconductors': 'Physics Note/Electronic Transition In Semiconductors.md',
    'Landau Theory Of Phase Transition': 'Physics Note/Landau Theory Of Phase Transition.md',
    'Stability and Rigidity': 'Physics Note/Stability and Rigidity.md',
    'Superfluidity': 'Physics Note/Superfluidity.md',
    'Classical Fluids': 'Physics Note/Classical Fluids.md',
    'Excitation': 'Physics Note/Excitation.md',
    'Experimental Significance and Particles': 'Physics Note/Experimental Significance and Particles.md',
    'Amplitude Mode Excitation': 'Physics Note/Amplitude Mode Excitation.md',
    'Mass of Excitation': 'Physics Note/Mass of Excitation.md',
    'Domain Wall and Vortices in Superfluid': 'Physics Note/Domain Wall and Vortices in Superfluid.md',
    'Kink and Topological Objects': 'Physics Note/Kink and Topological Objects.md',
    'Superfluid and Superconductivity': 'Physics Note/Superfluid and Superconductivity.md',
    'Gauge Theory and Higgs Mechanism': 'Physics Note/Gauge Theory and Higgs Mechanism.md',
    'Exchange Interaction and Ferromagnetism': 'Physics Note/Exchange Interaction and Ferromagnetism.md',
    'Antiferromagnetism and Anisotropy': 'Physics Note/Antiferromagnetism and Anisotropy.md',
    'PN Junction - Non-Equilibrium': 'Physics Note/PN Junction - Non-Equilibrium.md',
    'Introduction To Dielectrics': 'Physics Note/Introduction To Dielectrics.md',
    'Dielectric Function': 'Physics Note/Dielectric Function.md',
    'Introduction to Superconductivity': 'Physics Note/Introduction to Superconductivity.md',
    'Meissner Effect': 'Physics Note/Meissner Effect.md',
    'Ginzburg-Landau Theory For Superconductivity': 'Physics Note/Ginzburg-Landau Theory For Superconductivity.md',
    'Condensation Energy and Magnetic Energy': 'Physics Note/Condensation Energy and Magnetic Energy.md',
    'Home': 'Physics Note/Home.md',
}

path = Path("docs/Condensed Matter Physics.md")
text = path.read_text(encoding="utf-8")
for key, target in mapping.items():
    pattern = re.compile(r"\[\[" + re.escape(key) + r"\]\]")
    text = pattern.sub(f"[{key}]({Path(target).as_posix().replace(' ', '%20')})", text)
path.write_text(text, encoding="utf-8")
print(f"Updated {path}")
