"""Download the StarT GregTech fork sources needed by the extract pipeline into <repo>/gtsrc/ (flat folder of .java files).

Source: https://github.com/StarT-Dev-Team/GTM-StarT-Fork (branch main). The sources are LGPL and are NOT committed
to this repository (gtsrc/ is git-ignored). Uses 'git clone --depth 1' when git is available, else a ZIP via urllib.

Usage: python extract/fetch_gtsrc.py [--zip] [--all]
  --zip  force the ZIP download (no git needed)
  --all  copy every .java file of the repo instead of only the ones the pipeline reads
"""
import os, shutil, subprocess, sys, tempfile, urllib.request, zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import GT_SRC

REPO_URL = "https://github.com/StarT-Dev-Team/GTM-StarT-Fork"
BRANCH = "main"
ZIP_URL = REPO_URL + "/archive/refs/heads/" + BRANCH + ".zip"

WANTED = [
    "AcidRecipes.java",
    "AirScrubberRecipes.java",
    "AlloyBlastRecipeProducer.java",
    "AntidoteRecipes.java",
    "AssemblerRecipeLoader.java",
    "AssemblyLineLoader.java",
    "BatteryRecipes.java",
    "BrewingRecipes.java",
    "ChemicalBathRecipes.java",
    "ChemistryRecipes.java",
    "CircuitRecipes.java",
    "ComponentRecipes.java",
    "ComposterRecipes.java",
    "ComputerRecipes.java",
    "CraftingComponent.java",
    "CraftingRecipeLoader.java",
    "CustomAlloyBlastRecipeProducer.java",
    "CustomToolRecipes.java",
    "DecorationRecipes.java",
    "DistillationRecipes.java",
    "ElementMaterials.java",
    "FirstDegreeMaterials.java",
    "FuelRecipeChains.java",
    "FuelRecipes.java",
    "FusionLoader.java",
    "GCYMBlocks.java",
    "GCYMMachines.java",
    "GCYMRecipes.java",
    "GTBlocks.java",
    "GTCraftingComponents.java",
    "GTMultiMachines.java",
    "GTResearchMachines.java",
    "GemSlurryRecipes.java",
    "GrowthMediumRecipes.java",
    "HigherDegreeMaterials.java",
    "LCRCombined.java",
    "MachineRecipeLoader.java",
    "MaterialRecipeHandler.java",
    "MetaTileEntityLoader.java",
    "MetaTileEntityMachineRecipeLoader.java",
    "MiscRecipeLoader.java",
    "MixerRecipes.java",
    "NaquadahRecipes.java",
    "NuclearRecipes.java",
    "OreRecipeHandler.java",
    "OrganicChemistryMaterials.java",
    "PartsRecipeHandler.java",
    "PetrochemRecipes.java",
    "PlatGroupMetalsRecipes.java",
    "PolarizingRecipeHandler.java",
    "PolymerRecipes.java",
    "ReactorRecipes.java",
    "RecyclingRecipes.java",
    "SecondDegreeMaterials.java",
    "SeparationRecipes.java",
    "StoneMachineRecipes.java",
    "UnknownCompositionMaterials.java",
    "VanillaStandardRecipes.java",
    "WireRecipeHandler.java",
    "WoodMachineRecipes.java",
]


def clone(dst):
    subprocess.run(["git", "clone", "--depth", "1", "--branch", BRANCH, REPO_URL + ".git", dst], check=True)
    return dst


def download_zip(dst):
    zpath = os.path.join(dst, "src.zip")
    print("Downloading", ZIP_URL)
    with urllib.request.urlopen(ZIP_URL, timeout=120) as r, open(zpath, "wb") as f:
        shutil.copyfileobj(r, f)
    with zipfile.ZipFile(zpath) as z:
        z.extractall(os.path.join(dst, "x"))
    return os.path.join(dst, "x")


def main():
    use_zip = "--zip" in sys.argv or shutil.which("git") is None
    take_all = "--all" in sys.argv
    tmp = tempfile.mkdtemp(prefix="gtfork_")
    try:
        if use_zip:
            root = download_zip(tmp)
        else:
            try:
                root = clone(os.path.join(tmp, "repo"))
            except (subprocess.CalledProcessError, OSError) as e:
                print("git clone failed (%s); falling back to ZIP" % e)
                root = download_zip(tmp)
        found = {}
        for d, _, files in os.walk(root):
            if os.sep + ".git" in d:
                continue
            for fn in files:
                if fn.endswith(".java") and (take_all or fn in WANTED):
                    found.setdefault(fn, os.path.join(d, fn))
        os.makedirs(GT_SRC, exist_ok=True)
        for fn, p in sorted(found.items()):
            shutil.copyfile(p, os.path.join(GT_SRC, fn))
        missing = [w for w in WANTED if w not in found]
        print("Copied %d files into %s" % (len(found), GT_SRC))
        if missing:
            print("WARNING: not found in the repo (renamed upstream?): " + ", ".join(missing))
            return 1
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
