from conans import ConanFile, CMake, tools
import os


class DracoConan(ConanFile):
    name = "nifti"
    version = "3.0.1"
    generators = "cmake"
    settings = {"os": None, "arch": ["x86_64", "x86"], "compiler": None, "build_type": None}

    options = {"shared": [True, False]}
    default_options = "shared=True"
    exports_sources = "include*", "src*", "cmake*", "CMakeLists.txt"

    exports = ["CMakeLists.txt"]

    license = "Licensed under the public domain"
    description = "A library for loading nifti files"

    scm = {
        "type": "git",
        "subfolder": "sources",
        "url": "https://github.com/NIFTI-Imaging/nifti_clib.git",
        "revision": "v%s" % version,
    }

    def _cmake_configure(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure()
        return cmake
    
    def build(self):
        cmake = self._cmake_configure()
        cmake.build()

    def package(self):
        cmake = self._cmake_configure()
        cmake.install()
        
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
