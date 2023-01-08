#!/usr/bin/env python3

import os
import re
import sys
import platform
import subprocess

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext

# Parameters
THREAD_NUMBER = 8
USE_NINJA = True


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir="", **kwargs):
        Extension.__init__(self, name, sources=[], **kwargs)
        self.sourcedir = os.path.abspath(sourcedir)  # What is this for?


class CMakeBuild(build_ext):
    def run(self):
        try:
            _ = subprocess.check_output(["cmake", "--version"])
        except OSError:
            raise RuntimeError(
                "CMake must be installed to build the following extensions: "
                + ", ".join(e.name for e in self.extensions)
            )

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(
            os.path.dirname(self.get_ext_fullpath(ext.name))
        )
        # required for auto-detection of auxiliary "native" libs
        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep

        cmake_args = [
            "-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={}".format(extdir),
            "-DPYTHON_EXECUTABLE={}".format(sys.executable),
        ]

        cfg = "Debug" if self.debug else "Release"
        build_args = ["--config", cfg]

        cmake_args += ["-DCMAKE_BUILD_TYPE={}".format(cfg)]
        if USE_NINJA:
            cmake_args += ["-GNinja"]
        build_args += ["--", "-j{}".format(THREAD_NUMBER)]

        env = os.environ.copy()
        env["CXXFLAGS"] = '{} -DVERSION_INFO=\\"{}\\"'.format(
            env.get("CXXFLAGS", ""), self.distribution.get_version()
        )
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(
            ["cmake", ext.sourcedir] + cmake_args,
            cwd=self.build_temp,
            env=env,
        )
        subprocess.check_call(
            ["cmake", "--build", "."] + build_args,
            cwd=self.build_temp,  # call cmake
        )


setup(
    name="np_cv_example",
    version="0.0.1",
    author="Haruya Ishikawa",
    author_email="haru.ishi43@gmail.com",
    description="A test project using pybind11 and CMake",
    long_description="",
    ext_modules=[
        CMakeExtension(
            "example",
        )
    ],
    cmdclass=dict(build_ext=CMakeBuild),
    zip_safe=False,
)
