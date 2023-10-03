# https://github.com/pybind/cmake_example
import os
from pathlib import Path

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name: str, source_dir: str) -> None:
        super().__init__(name, sources=[])
        self.source_dir = os.fspath(Path(source_dir).resolve())


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
            self.spawn(["cmake", ext.source_dir] + cmake_args)
            self.spawn(["cmake", "--build", "."] + build_args)
            print(build_args)
            # Run C++ unit test here.
            # self.spawn([ str('tests/cpp_tests') ])
            # Troubleshooting: if fail on line above then delete all possible
            # temporary CMake files including "CMakeCache.txt" in top level dir.
            os.chdir(cwd)


setup(
    ext_modules=[CMakeExtension(name="myproject.multiply_cpp_impl", source_dir="myproject/cpp")],
    cmdclass={"build_ext": CMakeBuild},
)
