# -*- coding: utf-8 -*-

name = 'osl'

version = '1.10.9-ta.1.0.0'

authors = [
    'benjamin.skinner',
]

build_requires = [
    'zlib-1.2.11',
    'openexr-2.4.0',
    'oiio-1.8.9',
    'llvm-9.0.1',
]

requires = [
]

@early()
def private_build_requires():
    import sys
    if 'win' in str(sys.platform):
        return ['visual_studio']
    else:
        return ['gcc-6']

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
    #['platform-linux', 'arch-x86_64', 'os-centos-7'],
]

build_system = "cmake"

def commands():

    # Split and store version and package version
    split_versions = str(version).split('+')
    env.OSL_VERSION.set(split_versions[0])
    env.OSL_PACKAGE_VERSION.set(split_versions[1])

    env.OSL_ROOT.set("{root}")
    env.OSL_INCLUDE_DIR.set("{root}/include")
    env.OSL_LIBRARY_DIR.set("{root}/lib")
    env.OSL_BINARY_DIR.set("{root}/bin")

    env.PATH.append( str(env.OSL_BINARY_DIR) )
