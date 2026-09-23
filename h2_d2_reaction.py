"""B3LYP reaction-barrier workflow for H2 + D2 -> 2 HD.

The current MAESTRO geometry model has no isotope-labelled atoms, so D is
represented by H. Consequently, isotope-mass contributions to Delta G are
not included in this approximation.
"""

from maestro import (
    DFT,
    GeometricEngine,
    Maestro,
    PySCFEngine,
    ReactionBarrierTask,
    SystemQM,
)
from maestro.engines.jobspec import Resources


mae = Maestro(mode="slurm", workdir=".", runinfo_path="h2_d2_runinfo.toml")
reactant = SystemQM(geometry="h2_d2_reactant.xyz", charge=0, spin=0)
product = SystemQM(geometry="h2_d2_product.xyz", charge=0, spin=0)
theory = DFT(functional="B3LYP", basis="6-31G(d)")
qm_engine = PySCFEngine(
    optimizer=GeometricEngine(resources=Resources(cores=1, time="02:00:00")),
    resources=Resources(cores=1, time="02:00:00"),
)

result = mae.run(
    rundir="h2_d2_reaction_work",
    task=ReactionBarrierTask(
        system_react=reactant,
        system_prod=product,
        theory=theory,
        temperature=298.15,
        pressure=1.0,
    ),
    engines=qm_engine,
)

print("Delta G activation (Hartree):", result.load("activation_free_energy"))
print("Delta G reaction (Hartree):", result.load("reaction_free_energy"))
print("Delta G reaction (kcal/mol):", result.load("reaction_free_energy", unit="kcal/mol"))
