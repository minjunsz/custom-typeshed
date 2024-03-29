# pylint: disable=all
from __future__ import annotations

from typing import overload

from rdkit.Chem import Mol
from rdkit.Geometry import Point3D

def BuildFeatureFactory(fdef_path: str) -> MolChemicalFeatureFactory: ...

class MolChemicalFeatureFactory:
    def GetNumFeatureDefs(self) -> int: ...
    def GetFeatureDefs(self) -> dict[str, str]: ...
    def GetFeatureFamilies(self) -> tuple[str]: ...
    def GetNumMolFeatures(self, mol: Mol, includeOnly: str = "") -> int: ...
    def GetFeaturesForMol(self, mol: Mol, includeOnly: str = "") -> tuple[MolChemicalFeature]: ...
    def GetMolFeature(
        self, mol: Mol, idx: int, includeOnly: str = "", recompute: bool = True, confId: int = -1
    ) -> MolChemicalFeature: ...

class MolChemicalFeature:
    def GetAtomIds(self) -> tuple[int]: ...
    def GetFamily(self) -> str: ...
    def GetId(self) -> int: ...
    def GetMol(self) -> Mol: ...
    def GetFactory(self) -> MolChemicalFeatureFactory: ...
    @overload
    def GetPos(self) -> Point3D: ...
    @overload
    def GetPos(self, confId: int) -> Point3D: ...
    def GetType(self) -> str: ...
