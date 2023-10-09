# https://github.com/pybind/cmake_example
import os
from pathlib import Path

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name: str, csrc_dir: str) -> None:
        super().__init__(name, sources=[])
        self.csrc_dir = os.fspath(Path(csrc_dir).resolve())


class CMakeBuild(build_ext):
    def build_extensions(self) -> None:
        cwd = Path().absolute()
        build_temp = Path(self.build_temp)
        print("CWD:", cwd)
        print("Temp build directory:", build_temp)

        for ext in self.extensions:
            build_temp.mkdir(parents=True, exist_ok=True)
            extdir = Path(self.get_ext_fullpath(ext.name))
            print("Extension directory:", extdir)

            config = "Debug" if self.debug else "Release"
            cmake_args = [
                f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir.parent.absolute()}",
                f"-DCMAKE_BUILD_TYPE={config}",
            ]
            build_args = ["--config", config, "--", "-j4"]

            os.chdir(build_temp)  # change current working directory
            self.spawn(["cmake", ext.csrc_dir] + cmake_args)
            self.spawn(["cmake", "--build", "."] + build_args)
            os.chdir(cwd)


setup(
    ext_modules=[CMakeExtension(name="pysample.cpp_impl", csrc_dir="csrc")],
    cmdclass={"build_ext": CMakeBuild},
)
