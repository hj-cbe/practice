"""DFT single-point electronic energy for a separated H2 + D2 system.

Deuterium is represented by hydrogen in the electronic-structure geometry:
the electronic Hamiltonian is identical, while isotope masses only affect
nuclear-motion calculations.
"""

from maestro import DFT, EnergyTask, Maestro, PySCFEngine, SystemQM
from maestro.engines.jobspec import Resources


mae = Maestro(mode="slurm", workdir=".", runinfo_path="h2_d2_runinfo.toml")
system = SystemQM(geometry="h2_d2.xyz", charge=0, spin=0)
theory = DFT(functional="B3LYP", basis="6-31G(d)")
qm_engine = PySCFEngine(resources=Resources(cores=32))

result = mae.run(
    rundir="h2_d2_energy_work",
    task=EnergyTask(system=system, theory=theory),
    engines=qm_engine,
)

print("QM energy (Hartree):", result.load("qm_energy"))
print("QM energy (kcal/mol):", result.load("qm_energy", unit="kcal/mol"))
