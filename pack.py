from feanor import BaseBuilder

class Builder(BaseBuilder):
    def Setup(self):
        self.addDirectory("src", "src/feanorTempDir")
        self.addAndReplaceByPackageVersion("src/__init__.py", "src/feanorTempDir/__init__.py")
        self.addAndReplaceByPackageVersion("pyproject.toml")
        self.venv().install("build")
        
    def Build(self):
        self.venv().runModule(f"build --outdir {self.distDir} .")