# pylint: disable=all
from __future__ import annotations

from typing import overload

from rdkit.Chem import Mol

def MolFromSmiles(SMILES: str, sanitize: bool = True, removeHs: bool = True) -> Mol: ...
def MolFromMolBlock(
    molBlock: str, sanitize: bool = True, removeHs: bool = True, strictParsing: bool = True
) -> Mol: ...
def MolFromPDBFile(
    molFileName: str, sanitize: bool = True, removeHs: bool = True, flavor: int = 0, proximityBonding: bool = True
) -> Mol: ...
def MolFromSequence(text: str, sanitize: bool = True, flavor: int = 0) -> Mol: ...
def MolFromSmarts(SMARTS: str, mergeHs: bool = False) -> Mol: ...

class SDMolSupplier:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, fileName: str, sanitize: bool = True, removeHs: bool = True, strictParsing: bool = True
    ) -> None: ...
    def GetItemText(self, index: int) -> str: ...
    def GetProcessPropertyLists(self) -> bool: ...
    def SetData(self, data: str, sanitize: bool = True, removeHs: bool = True, strictParsing: bool = True) -> None: ...
    def SetProcessPropertyLists(self, b: bool) -> None: ...
    def atEnd(self) -> bool: ...
    def reset(self) -> None: ...
    def __next__(self) -> Mol: ...
    def __iter__(self) -> SDMolSupplier: ...
    def __getitem__(self, key: int) -> Mol: ...