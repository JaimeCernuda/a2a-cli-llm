:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.document role="main" itemscope="itemscope" itemtype="http://schema.org/Article"}
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {itemprop="articleBody"}
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#adios-2-the-adaptable-input-output-system-version-2 .section}
# ADIOS 2: The Adaptable Input/Output System version 2[](#adios-2-the-adaptable-input-output-system-version-2 "Link to this heading"){.headerlink}

Funded by the [Exascale Computing Project
(ECP)](https://www.exascaleproject.org/){.reference .external}, U.S.
Department of Energy

:::::::::::::::: {.toctree-wrapper .compound}
[]{#document-introduction/whatsnew}

::::::: {#what-s-new-in-2-10 .section}
## What's new in 2.10?[](#what-s-new-in-2-10 "Link to this heading"){.headerlink}

This is a major release with new features and lots of bug fixes. The
main new feature is the new Python API.

:::: {#python .section}
### Python[](#python "Link to this heading"){.headerlink}

Before, ADIOS had two separate APIs for Python. The low-level ("Full")
API was written with Pybind11 and directly mimicked the C++ API. The
high-level API was another, smaller, and more pythonesque API that
allowed for easier scripting with Python. The main problems with these
two were that they were independent, and that the high-level API was not
complete. Once a developer needed a feature only available in the full
API, they had to start from scratch writing a script with the full API.

In 2.10, there is officially one Python API, written in Python, which in
turn uses the old Pybind11 classes. The new API combines the high-level
features of the old high-level API -- hopefully in a more consistent and
likeable way, -- and the full feature set of the low-level bindings.

::: {.admonition .note}
Note

Old scripts that used the full API can still run without almost any
modification, just change the import line from [`import`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`adios2`{.docutils .literal .notranslate}]{.pre} to
[`import`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`adios2.bindings`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`as`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`adios2`{.docutils .literal .notranslate}]{.pre}

Old scripts that used the high-level API must be modified to make them
work with the new API, see [[Transition from old API to new API]{.std
.std-ref}](#document-api_python/python_transition_from_high#transition-from-old-api-to-new-api){.reference
.internal}
:::

See [Python API]{.xref .std .std-ref}
::::

::: {#new-updated-features .section}
### New/updated features[](#new-updated-features "Link to this heading"){.headerlink}

> <div>
>
> - BP5 is supported on Windows now
>
> - SST and DataMan staging engines are GPU-Aware now
>
> - SYCL support added for Intel GPUs (besides CUDA and HIP for NVidia
>   and AMD GPUs)
>
> - the SST/libfabric data transport now works on Frontier (besides the
>   MPI data transport)
>
> </div>
:::

::: {#packaging .section}
### Packaging[](#packaging "Link to this heading"){.headerlink}

> <div>
>
> - adios2 package is now on
>   [PyPi](https://pypi.org/project/adios2/){.reference .external}
>
> </div>
:::
:::::::

::::::: {#what-s-new-in-2-9 .section}
## What's new in 2.9?[](#what-s-new-in-2-9 "Link to this heading"){.headerlink}

This is a major release with new features and lots of bug fixes.

::: {#general .section}
### General[](#general "Link to this heading"){.headerlink}

- GPU-Aware I/O enabled by using Kokkos. Device pointers can be passed
  to Put()/Get() calls directly. Kokkos 3.7.x required for this release.
  Works with CUDA, HIP and Kokkos applications.
  [https://adios2.readthedocs.io/en/latest/advanced/gpu_aware.html#gpu-aware-i-o](https://adios2.readthedocs.io/en/latest/advanced/gpu_aware.html#gpu-aware-i-o){.reference
  .external}

- GPU-compression. MGARD and ZFP operators can compress data on GPU if
  they are built for GPU. MGARD operator can be fed with host/device
  pointers and will move data automaticaly. ZFP operator requires
  matching data and compressor location.

- Joined Array concept (besides Global Array and Local Array), which
  lets writers dump Local Arrays (no offsets no global shape) that are
  put together into a Global Array by the reader. One dimension of the
  arrays is selected for this join operation, while other dimensions
  must be the same for all writers.
  [https://adios2.readthedocs.io/en/latest/components/components.html?highlight=Joined#shapes](https://adios2.readthedocs.io/en/latest/components/components.html?highlight=Joined#shapes){.reference
  .external}
:::

::: {#file-i-o .section}
### File I/O[](#file-i-o "Link to this heading"){.headerlink}

- Default File engine is now BP5. If for some reason this causes
  problems, manually specify using "BP4" for your application.

- BP5 engine supports multithreaded reading to accelerate read
  performance for low-core counts.

- BP5 Two level metadata aggregation and reduction reduced memory impact
  of collecting metadata and therefore is more scalable in terms of
  numbers of variables and writers than BP4.

- Uses Blosc-2 instead of Blosc for lossless compression. The new
  compression operator is backward compatible with old files compressed
  with blosc. The name of the operator remains "blosc".
:::

::: {#staging .section}
### Staging[](#staging "Link to this heading"){.headerlink}

- UCX dataplane added for SST staging engine to support networks under
  the UCX consortium

- MPI dataplane added for SST staging engine. It relies on MPI
  intercommunicators to connect multiple independent MPI applications
  for staging purposes. Applications must enable multithreaded MPI for
  this dataplane.
:::

::: {#experimental-features .section}
### Experimental features[](#experimental-features "Link to this heading"){.headerlink}

- Preliminary support for data structs. A struct can have single
  variables of basic types, and 1D fixed size arrays of basic types.
  Supported by BP5, SST and SSC engines.
:::
:::::::

[]{#document-introduction/introduction}

::::: {#introduction .section}
## Introduction[](#introduction "Link to this heading"){.headerlink}

**ADIOS2** is the latest implementation of the [Adaptable Input Output
System](https://csmd.ornl.gov/software/adios2){.reference .external}.
This brand new architecture continues the performance legacy of ADIOS1,
and extends its capabilities to address the extreme challenges of
scientific data IO.

The [ADIOS2 repo is hosted at
GitHub](https://github.com/ornladios/ADIOS2){.reference .external}.

The ADIOS2 infrastructure is developed as a multi-institutional
collaboration between

> <div>
>
> - [Oak Ridge National Laboratory](https://www.ornl.gov){.reference
>   .external}
>
> - [Kitware Inc.](https://www.kitware.com){.reference .external}
>
> - [Lawrence Berkeley National
>   Laboratory](http://www.lbl.gov){.reference .external}
>
> - [Georgia Institute of Technology](http://www.gatech.edu){.reference
>   .external}
>
> - [Rutgers University](http://www.rutgers.edu){.reference .external}
>
> </div>

The key aspects ADIOS2 are

1.  **Modular architecture:** ADIOS2 takes advantage of the major
    features of C++11. The architecture utilizes a balanced combination
    of runtime polymorphism and template meta-programming to expose
    intuitive abstractions for a broad range of IO applications.

2.  **Community:** By maintaining coding standards, collaborative
    workflows, and understandable documentation, ADIOS2 lowers the
    barriers to entry for scientists to meaningfully interact with the
    code.

3.  **Sustainability:** Continuous integration and unit testing ensure
    that ADIOS2 evolves responsibly. Bug reports are triaged and fixed
    in a timely manner and can be reported on
    [GitHub](https://github.com/ornladios/ADIOS2/issues){.reference
    .external}.

4.  **Language Support:** In addition to the native C++, bindings for
    Python, C, Fortran and Matlab are provided.

5.  **Commitment:** ADIOS2 is committed to the HPC community, releasing
    a new version every 6 months.

*ADIOS2 is funded by the Department of Energy as part of the* [Exascale
Computing Project](https://www.exascaleproject.org){.reference
.external}.

::: {#what-adios2-is-and-isn-t .section}
### What ADIOS2 is and isn't[](#what-adios2-is-and-isn-t "Link to this heading"){.headerlink}

**ADIOS2 is:**

- **A Unified High-performance I/O Framework**: using the same
  abstraction API ADIOS2 can transport and transform groups of
  self-describing data variables and attributes across different media
  (file, wide-area-network, in-memory staging, etc.) with performance an
  ease of use as the main goals.

- **MPI-based**: parallel MPI applications as well as serial codes can
  use it

- **Streaming-oriented**: ADIOS2 favors codes transferring a group of
  variables asynchronously wherever possible. Moving one variable at a
  time, in synchronous fashion, is the special case rather than normal.

- **Step-based**: to resemble actual production of data in "steps" of
  variable groups, for either streaming or random-access (file) media

- **Free and open-source**: ADIOS2 is permissibly licensed under the
  OSI-approved Apache 2 license.

- **Extreme scale I/O**: ADIOS2 is being used in supercomputer
  applications that write and read up to several petabytes in a single
  simulation run. ADIOS2 is designed to provide scalable I/O on the
  largest supercomputers in the world.

**ADIOS2 is not**:

- **A file-only I/O library**: Code coupling and in situ analyis is
  possible through files but special engines are available to achieve
  the same thing faster through TCP, RDMA and MPI communication. High
  performance write/read using a file system is a primary goal of ADIOS2
  though.

- **MPI-only**

- **A Hierarchical Model**: Data hierarchies can be built on top of the
  ADIOS2 according to the application, but ADIOS2 sits a layer of
  abstraction beneath this.

- **A Memory Manager Library**: we don't own or manage the application's
  memory
:::

::: {#adaptable-io-beyond-files-in-scientific-data-lifecycles .section}
### Adaptable IO beyond files in Scientific Data Lifecycles[](#adaptable-io-beyond-files-in-scientific-data-lifecycles "Link to this heading"){.headerlink}

Performant and usable tools for data management at scale are essential
in an era where scientific breakthroughs are collaborative,
multidisciplinary, and computational. ADIOS2 is an *adaptable*,
*scalable*, and *unified* framework to aid scientific applications when
data transfer volumes exceed the capabilities of traditional file I/O.

![](https://i.imgur.com/VLSvvjM.png:alt:my-picture1)

ADIOS2 provides

- Custom application management of massive data sets, starting from
  generation, analysis, and movement, as well as short-term and
  long-term storage.

- Self-describing data in binary-packed (.bp) format for rapid metadata
  extraction

- An ability to separate and extract relevant information from large
  data sets

- The capability to make real-time decisions based on in-transit or
  in-situ analytics

- The ability to expand to other transport mechanisms such wide area
  networks, remote direct memory access, and shared memory, with minimal
  overhead

- The ability to utilize the full capabilities of emergent hardware
  technologies, such as high-bandwidth memory and burst buffers
:::
:::::
::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.toctree-wrapper .compound}
[]{#document-setting_up/setting_up}

::::::::::::::::::::::::::::::::: {#install-from-source .section}
## Install from Source[](#install-from-source "Link to this heading"){.headerlink}

ADIOS2 uses [CMake](https://cmake.org/){.reference .external} for
building, testing and installing the library and utilities.

::::::::::::: {#building-testing-and-installing-adios-2 .section}
### Building, Testing, and Installing ADIOS 2[](#building-testing-and-installing-adios-2 "Link to this heading"){.headerlink}

To build ADIOS v2.x, clone the repository and invoke the canonical CMake
build sequence:

:::: {.highlight-bash .notranslate}
::: highlight
    $ git clone https://github.com/ornladios/ADIOS2.git ADIOS2
    $ mkdir adios2-build && cd adios2-build
    $ cmake ../ADIOS2 -DADIOS2_BUILD_EXAMPLES=ON
    -- The C compiler identification is GNU 9.4.0
    -- The CXX compiler identification is GNU 9.4.0
    ...

    ADIOS2 build configuration:
      ADIOS Version: 2.10.0
      C++ Compiler : GNU 9.4.0
        /usr/bin/c++

      Fortran Compiler : GNU 9.4.0
        /usr/bin/f95

      Installation prefix: /usr/local
            bin: bin
           lib: lib
        include: include
         cmake: lib/cmake/adios2
        python: lib/python3/dist-packages

      ...
      Features:
        Library Type: shared
        Build Type:   Release
        Testing: OFF
        Examples: ON
        Build Options:
          DataMan            : ON
          DataSpaces         : OFF
          HDF5               : OFF
          HDF5_VOL           : OFF
          MHS                : ON
          SST                : ON
          Fortran            : ON
          MPI                : ON
          Python             : ON
          PIP                : OFF
          Blosc2             : OFF
          BZip2              : ON
          LIBPRESSIO         : OFF
          MGARD              : OFF
          MGARD_MDR          : OFF
          PNG                : OFF
          SZ                 : OFF
          ZFP                : ON
          DAOS               : OFF
          IME                : OFF
          O_DIRECT           : ON
          Sodium             : ON
          Catalyst           : OFF
          SysVShMem          : ON
          UCX                : OFF
          ZeroMQ             : ON
          Profiling          : ON
          Endian_Reverse     : OFF
          Derived_Variable   : OFF
          AWSSDK             : OFF
          GPU_Support        : OFF
          CUDA               : OFF
          Kokkos             : OFF
          Kokkos_CUDA        : OFF
          Kokkos_HIP         : OFF
          Kokkos_SYCL        : OFF
          Campaign           : OFF
:::
::::

If a desired feature is OFF in the report above, tell cmake where to
find the required dependencies for that feature and manually turn it on.
E.g.:

:::: {.highlight-bash .notranslate}
::: highlight
    $ cmake ... -DADIOS2_USE_Blosc2=ON   -DCMAKE_PREFIX_PATH="<path to c-blosc2 installation>"
:::
::::

Then compile using

:::: {.highlight-bash .notranslate}
::: highlight
    $ make -j 16
:::
::::

Optionally, run the tests (need to configure with
[`-DBUILD_TESTING=ON`{.docutils .literal .notranslate}]{.pre} cmake
flag)

:::: {.highlight-bash .notranslate}
::: highlight
    $ ctest
    Test project /home/wgodoy/workspace/build
            Start   1: ADIOSInterfaceWriteTest.DefineVar_int8_t_1x10
      1/295 Test   #1: ADIOSInterfaceWriteTest.DefineVar_int8_t_1x10 .........................   Passed    0.16 sec
            Start   2: ADIOSInterfaceWriteTest.DefineVar_int16_t_1x10
      2/295 Test   #2: ADIOSInterfaceWriteTest.DefineVar_int16_t_1x10 ........................   Passed    0.06 sec
            Start   3: ADIOSInterfaceWriteTest.DefineVar_int32_t_1x10

          ...

            Start 294: ADIOSBZip2Wrapper.WrongParameterValue
    294/295 Test #294: ADIOSBZip2Wrapper.WrongParameterValue .................................   Passed    0.00 sec
            Start 295: ADIOSBZip2Wrapper.WrongBZip2Name
    295/295 Test #295: ADIOSBZip2Wrapper.WrongBZip2Name ......................................   Passed    0.00 sec

    100% tests passed, 0 tests failed out of 295

    Total Test time (real) =   95.95 sec
:::
::::

And finally, use the standard invocation to install (setting the install
path beforehand):

:::: {.highlight-bash .notranslate}
::: highlight
    $ cmake ../ADIOS2 -DCMAKE_INSTALL_PREFIX=/path/to/where/adios/will/be/installed
    $ make install
:::
::::
:::::::::::::

::::::::: {#cmake-options .section}
### CMake Options[](#cmake-options "Link to this heading"){.headerlink}

The following options can be specified with CMake's
[`-DVAR=VALUE`{.docutils .literal .notranslate}]{.pre} syntax. The
default option is highlighted.

  VAR                                                                    VALUE        Description
  ---------------------------------------------------------------------- ------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`ADIOS2_USE_MPI`{.docutils .literal .notranslate}]{.pre}              **ON**/OFF   MPI or non-MPI (serial) build.
  [`ADIOS2_USE_ZeroMQ`{.docutils .literal .notranslate}]{.pre}           **ON**/OFF   [ZeroMQ](http://zeromq.org/){.reference .external} for the DataMan engine.
  [`ADIOS2_USE_HDF5`{.docutils .literal .notranslate}]{.pre}             **ON**/OFF   [HDF5](https://www.hdfgroup.org){.reference .external} engine. If HDF5 is not on the syspath, it can be set using [`-DHDF5_ROOT=/path/to/hdf5`{.docutils .literal .notranslate}]{.pre}
  [`ADIOS2_USE_Python`{.docutils .literal .notranslate}]{.pre}           **ON**/OFF   Python bindings. Python 3 will be used if found. If you want to specify a particular python version use [`-DPYTHON_EXECUTABLE=/path/to/interpreter/python`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-DPython_FIND_STRATEGY=LOCATION`{.docutils .literal .notranslate}]{.pre}
  [`ADIOS2_USE_Fortran`{.docutils .literal .notranslate}]{.pre}          **ON**/OFF   Bindings for Fortran 90 or above.
  [`ADIOS2_USE_SST`{.docutils .literal .notranslate}]{.pre}              **ON**/OFF   Simplified Staging Engine (SST) and its dependencies, requires MPI. Can optionally use LibFabric/UCX for RDMA transport. You can specify the LibFabric/UCX path manually with the -DLIBFABRIC_ROOT=... or -DUCX_ROOT=... option.
  [`ADIOS2_USE_BZip2`{.docutils .literal .notranslate}]{.pre}            **ON**/OFF   [BZIP2](http://www.bzip.org){.reference .external} compression.
  [`ADIOS2_USE_ZFP`{.docutils .literal .notranslate}]{.pre}              **ON**/OFF   [ZFP](https://github.com/LLNL/zfp){.reference .external} compression (experimental).
  [`ADIOS2_USE_SZ`{.docutils .literal .notranslate}]{.pre}               **ON**/OFF   [SZ](https://github.com/disheng222/SZ){.reference .external} compression (experimental).
  [`ADIOS2_USE_MGARD`{.docutils .literal .notranslate}]{.pre}            **ON**/OFF   [MGARD](https://github.com/CODARcode/MGARD){.reference .external} compression (experimental).
  [`ADIOS2_USE_PNG`{.docutils .literal .notranslate}]{.pre}              **ON**/OFF   [PNG](https://libpng.org){.reference .external} compression (experimental).
  [`ADIOS2_USE_Blosc2`{.docutils .literal .notranslate}]{.pre}           **ON**/OFF   [Blosc](http://blosc.org/){.reference .external} compression (experimental).
  [`ADIOS2_USE_Endian_Reverse`{.docutils .literal .notranslate}]{.pre}   ON/**OFF**   Enable endian conversion if a different endianness is detected between write and read.
  [`ADIOS2_USE_IME`{.docutils .literal .notranslate}]{.pre}              ON/**OFF**   DDN IME transport.

In addition to the [`ADIOS2_USE_Feature`{.docutils .literal
.notranslate}]{.pre} options, the following options are also available
to control how the library gets built:

  CMake VAR Options                                                  Values                                                                     Description \|
  ------------------------------------------------------------------ -------------------------------------------------------------------------- ------------------------------------------------------------
  [`BUILD_SHARED_LIBS`{.docutils .literal .notranslate}]{.pre}       **ON**/OFF                                                                 Build shared libraries.
  [`ADIOS2_BUILD_EXAMPLES`{.docutils .literal .notranslate}]{.pre}   ON/**OFF**                                                                 Build examples.
  [`BUILD_TESTING`{.docutils .literal .notranslate}]{.pre}           ON/**OFF**                                                                 Build test code.
  [`CMAKE_INSTALL_PREFIX`{.docutils .literal .notranslate}]{.pre}    /path/to/install ([`/usr/local`{.docutils .literal .notranslate}]{.pre})   Installation location.
  [`CMAKE_BUILD_TYPE`{.docutils .literal .notranslate}]{.pre}        Debug/**Release**/RelWithDebInfo/MinSizeRel                                Compiler optimization levels.
  [`CMAKE_PREFIX_PATH`{.docutils .literal .notranslate}]{.pre}       Semi-colon separeated list of paths                                        Location of extra dependencies.
  [`ADIOS2_USE_PIP`{.docutils .literal .notranslate}]{.pre}          ON/**OFF**                                                                 ON when installing inside a Python venv or a PyPi package.

Example: Enable Fortran, disable Python bindings and ZeroMQ
functionality

:::: {.highlight-bash .notranslate}
::: highlight
    $ cmake -DADIOS2_USE_Fortran=ON -DADIOS2_USE_Python=OFF -DADIOS2_USE_ZeroMQ=OFF ../ADIOS2
:::
::::

Notes:

> <div>
>
> To provide search paths to CMake for dependency searching:
>
> - Use a [`PackageName_ROOT`{.docutils .literal .notranslate}]{.pre}
>   variable to provide the location of a specific package.
>
> - Add an install prefix to the [`CMAKE_PREFIX_PATH`{.docutils .literal
>   .notranslate}]{.pre} which is searched for all packages.
>
> - Both the [`PackageName_ROOT`{.docutils .literal .notranslate}]{.pre}
>   and [`CMAKE_PREFIX_PATH`{.docutils .literal .notranslate}]{.pre} can
>   be used as either environment variables or CMake variables (passed
>   via -D), where the CMake variable takes prescedence.
>
> </div>

:::: {.highlight-bash .notranslate}
::: highlight
    # Several dependencies are installed under /opt/foo/bar and then a
    # single dependency (HDF5 in this case) is installed in /opt/hdf5/1.13.0
    $ export CMAKE_PREFIX_PATH=/opt/foo/bar
    $ cmake -DHDF5_ROOT=/opt/hdf5/1.13.0 ../ADIOS2
:::
::::

Example: the following configuration will build, test and install under
/opt/adios2/2.9.0 an optimized (Release) version of ADIOS2.

:::: {.highlight-bash .notranslate}
::: highlight
    $ cd build
    $ cmake -DADIOS2_USE_Fortran=ON -DCMAKE_INSTALL_PREFIX=/opt/adios2/2.9.0 -DCMAKE_BUILD_Type=Release ../ADIOS2
    $ make -j16
    $ ctest
    $ make install
:::
::::

For a fully configurable build script, click
[here.](https://github.com/ornladios/ADIOS2/tree/master/scripts/runconf/runconf.sh){.reference
.external}
:::::::::

::::: {#building-on-hpc-systems .section}
[]{#hpcbuild}

### Building on HPC Systems[](#building-on-hpc-systems "Link to this heading"){.headerlink}

1.  **Modules:** Make sure all "module" dependencies are loaded and that
    minimum requirements are satisfied. Load the latest CMake module as
    many HPC systems default to an outdated version. Build with a
    C++11-compliant compiler, such as gcc \>= 4.8.1, Intel \>= 15, and
    PGI \>= 15.

2.  **Static/Dynamic build:** On Cray systems such as
    [Titan](https://www.olcf.ornl.gov/kb_articles/compiling-and-node-types/){.reference
    .external}, the default behavior is static linkage, thus CMake
    builds ADIOS2 creates the static library [`libadios2.a`{.docutils
    .literal .notranslate}]{.pre} by default. Read the system
    documentation to enable dynamic compilation, usually by setting an
    environment variable such as [`CRAYPE_LINK_TYPE=dynamic`{.docutils
    .literal .notranslate}]{.pre}. Click
    [here](https://github.com/ornladios/ADIOS2/tree/master/scripts/runconf/runconf_olcf.sh){.reference
    .external} for a fully configurable script example on OLCF systems.

3.  **Big Endian and 32-bit systems:** ADIOS2 hasn't been tested on big
    endian and generally will not build on 32-bit systems. Please be
    aware before attempting to run.

4.  **PGI compilers and C++11 support:** Version 15 of the PGI compiler
    is C++11 compliant. However it relies on the C++ standard library
    headers supplied by the system version of GCC, which may or may
    support all the C++11 features used in ADIOS2. On many systems
    (Titan at OLCF, for example) even though the PGI compiler supports
    C++11, the configured GCC and its headers do not (4.3.x on Cray
    Linux Environment, and v5 systems like Titan). To configure the PGI
    compiler to use a newer GCC, you must create a configuration file in
    your home directory that overrides the PGI compiler's default
    configuration. On Titan, the following steps will re-configure the
    PGI compiler to use GCC 6.3.0 provided by a module:

:::: {.highlight-bash .notranslate}
::: highlight
    $ module load gcc/6.3.0
    $ makelocalrc $(dirname $(which pgc++)) -gcc $(which gcc) -gpp $(which g++) -g77 $(which gfortran) -o -net 1>${HOME}/.mypgirc 2>/dev/null
:::
::::

1.  **Enabling RDMA for SST data transfers:** The SST engine in ADIOS2
    is capable of using RDMA networks for transfering data between
    writer and reader cohorts, and generally this is the most performant
    data transport. However, SST depends upon libfabric to provide a
    generic interface to the underlying RDMA capabilities of the
    network, and properly configuring libfabric can be a difficult and
    error-prone task. HPC computing resources tend to be one-off custom
    resources with their own idiosyncracies, so this documentation
    cannot offer a definitive guide for every situation, but we can
    provide some general guidance and some recommendations for specific
    machines. If you are unable to configure ADIOS2 and libfabric to use
    RDMA, the best way to get help is to open an issue on the ADIOS2
    github repository.

Pre-build concerns of note:

> <div>
>
> - on some HPC resources, libfabric is available as a loadable module.
>   That should not be taken as an indication that that build of
>   libfabric will work with SST, or even that it is compatible with the
>   system upon which you find it. Your mileage may vary and you may
>   have to build libfabric manually.
>
> - libfabric itself depends upon other libraries like libibverbs and
>   librdmacm. If you build libfabric with a package manager like spack,
>   spack may build custom versions of those libraries as well, which
>   may conflict with the system versions of those libraries.
>
> - MPI on your HPC system may use libfabric itself, and linking your
>   application with a different version of libfabric (or its dependent
>   libraries) may result failure, possibly including opaque error
>   messages from MPI.
>
> - libfabric is structured in such a way that even if it is found
>   during configuration, ADIOS *cannot* determine at compile time what
>   providers will be present at run-time, or what their capabilities
>   are. Therefore even a build that seems to successfully include
>   libfabric and RDMA may be rejected at runtime as unable to support
>   SST data transfer.
>
> </div>

Configuration:

:   ADIOS2 uses the CMake find_package() functionality to locate
    libfabric. CMake will automatically search system libraries, but if
    you need to specify a libfabric location other than in a default
    system location you can add a "-DLIBFABRIC_ROOT=\<directory\>"
    argument to direct CMake to libfabric's location. If CMake finds
    libfabric, you should see the line "RDMA Transport for Staging:
    Available" near the end of the CMake output. This makes the RDMA
    DataTransport the default for SST data movement. (More information
    about SST engine parameters like DataTransport appears in the SST
    engine description.) If instead you see "RDMA Transport for Staging:
    Unconfigured", RDMA will not be available to SST.

Run-time:

:   Generally, if RDMA is configured and the libfabric provider has the
    capabilities that SST needs for RDMA data transfer, SST will use
    RDMA without external acknowledgement. However, if RDMA is
    configured, but the libfabric provider doesn't have the capabilities
    that SST needs, ADIOS will output an error : 'Warning: Preferred
    DataPlane "RDMA" not found.' If you see this warning in a situation
    where you expect RDMA to be used, enabling verbose debugging output
    from SST may provide more information. The SstVerbose environment
    variable can have values from 1 to 5, with 1 being minimal debugging
    info (such as confirming which DataTransport is being used), and 5
    being the most detailed debugging information from all ranks.
:::::

::: {#installing-the-adios2-library-and-the-c-and-c-bindings .section}
### Installing the ADIOS2 library and the C++ and C bindings[](#installing-the-adios2-library-and-the-c-and-c-bindings "Link to this heading"){.headerlink}

By default, ADIOS2 will build the C++11 [`libadios2`{.docutils .literal
.notranslate}]{.pre} library and the C and C++ bindings.

1.  **Minimum requirements:**

    > <div>
    >
    > - A C++11 compliant compiler
    >
    > - An MPI C implementation on the syspath, or in a location
    >   identifiable by CMake.
    >
    > </div>

2.  **Linking** [`make`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`install`{.docutils .literal .notranslate}]{.pre} will
    copy the required headers and libraries into the directory specified
    by [`CMAKE_INSTALL_PREFIX`{.docutils .literal .notranslate}]{.pre}:

    > <div>
    >
    > - Libraries:
    >
    >   - [`lib/libadios2.*`{.docutils .literal .notranslate}]{.pre}
    >     C++11 and C bindings
    >
    > - Headers:
    >
    >   - [`include/adios2.h`{.docutils .literal .notranslate}]{.pre}
    >     C++11 [`namespace`{.docutils .literal
    >     .notranslate}]{.pre}` `{.docutils .literal
    >     .notranslate}[`adios2`{.docutils .literal .notranslate}]{.pre}
    >
    >   - [`include/adios2_c.h`{.docutils .literal .notranslate}]{.pre}
    >     C prefix [`adios2_`{.docutils .literal .notranslate}]{.pre}
    >
    > - Config file: run this command to get installation info
    >
    >   - [`bin/adios2-config`{.docutils .literal .notranslate}]{.pre}
    >
    > </div>
:::

::: {#enabling-the-python-bindings .section}
### Enabling the Python bindings[](#enabling-the-python-bindings "Link to this heading"){.headerlink}

To enable the Python bindings in ADIOS2, based on
[PyBind11](http://pybind11.readthedocs.io/en/stable/){.reference
.external}, make sure to follow these guidelines:

- **Minimum requirements:**

  > <div>
  >
  > - Python 2.7 and above.
  >
  > - numpy
  >
  > - mpi4py
  >
  > </div>

- **Running:** If CMake enables Python compilation, an
  [`adios2.so`{.docutils .literal .notranslate}]{.pre} library
  containing the Python module is generated in the build directory under
  [`lib/pythonX.X/site-packages/`{.docutils .literal
  .notranslate}]{.pre}

  > <div>
  >
  > - make sure your [`PYTHONPATH`{.docutils .literal
  >   .notranslate}]{.pre} environment variable contains the path to
  >   [`adios2.so`{.docutils .literal .notranslate}]{.pre}.
  >
  > - make sure the Python interpreter is compatible with the version
  >   used for compilation via [`python`{.docutils .literal
  >   .notranslate}]{.pre}` `{.docutils .literal
  >   .notranslate}[`--version`{.docutils .literal .notranslate}]{.pre}.
  >
  > - Run the Python tests with [`ctest`{.docutils .literal
  >   .notranslate}]{.pre}` `{.docutils .literal
  >   .notranslate}[`-R`{.docutils .literal
  >   .notranslate}]{.pre}` `{.docutils .literal
  >   .notranslate}[`Python`{.docutils .literal .notranslate}]{.pre}
  >
  > - Run
  >   [helloBPWriter.py](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/bpWriter/helloBPWriter.py){.reference
  >   .external} and
  >   [helloBPTimeWriter.py](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/bpTimeWriter/helloBPTimeWriter.py){.reference
  >   .external} via
  >
  > :::: {.highlight-bash .notranslate}
  > ::: highlight
  >     $ mpirun -n 4 python helloBPWriter.py
  >     $ python helloBPWriter.py
  > :::
  > ::::
  >
  > </div>
:::

::: {#enabling-the-fortran-bindings .section}
### Enabling the Fortran bindings[](#enabling-the-fortran-bindings "Link to this heading"){.headerlink}

1.  **Minimum requirements:**

    > <div>
    >
    > - A Fortran 90 compliant compiler
    >
    > - A Fortran MPI implementation
    >
    > </div>

2.  **Linking the Fortran bindings:** [`make`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`install`{.docutils .literal .notranslate}]{.pre} will
    copy the required library and modules into the directory specified
    by [`CMAKE_INSTALL_PREFIX`{.docutils .literal .notranslate}]{.pre}

    > <div>
    >
    > - Library (note that [`libadios2`{.docutils .literal
    >   .notranslate}]{.pre} must also be linked) -
    >   [`lib/libadios2_f.*`{.docutils .literal .notranslate}]{.pre} -
    >   [`lib/libadios2.*`{.docutils .literal .notranslate}]{.pre}
    >
    > - Modules - [`include/adios2/fortran/*.mod`{.docutils .literal
    >   .notranslate}]{.pre}
    >
    > </div>

3.  **Module adios2:** only module required to be used in an application
    [`use`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`adios`{.docutils .literal .notranslate}]{.pre}
:::

::::::: {#running-tests .section}
### Running Tests[](#running-tests "Link to this heading"){.headerlink}

ADIOS2 uses
[googletest](https://github.com/google/googletest){.reference .external}
to enable automatic testing after a CMake build. To run tests just type
after building with make, run:

:::: {.highlight-bash .notranslate}
::: highlight
    $ ctest
      or
    $ make test
:::
::::

The following screen will appear providing information on the status of
each finalized test:

:::: {.highlight-bash .notranslate}
::: highlight
    Test project /home/wfg/workspace/build
    Start  1: ADIOSInterfaceWriteTest.DefineVarChar1x10
    1/46 Test  #1: ADIOSInterfaceWriteTest.DefineVarChar1x10 .......................   Passed    0.06 sec
    Start  2: ADIOSInterfaceWriteTest.DefineVarShort1x10
    2/46 Test  #2: ADIOSInterfaceWriteTest.DefineVarShort1x10 ......................   Passed    0.04 sec
    Start  3: ADIOSInterfaceWriteTest.DefineVarInt1x10
    3/46 Test  #3: ADIOSInterfaceWriteTest.DefineVarInt1x10 ........................   Passed    0.04 sec
    Start  4: ADIOSInterfaceWriteTest.DefineVarLong1x10
    ...
    128/130 Test #128: ADIOSZfpWrapper.UnsupportedCall ..........................................   Passed    0.05 sec
        Start 129: ADIOSZfpWrapper.MissingMandatoryParameter
    129/130 Test #129: ADIOSZfpWrapper.MissingMandatoryParameter ................................   Passed    0.05 sec
        Start 130: */TestManyVars.DontRedefineVars/*
    130/130 Test #130: */TestManyVars.DontRedefineVars/* ........................................   Passed    0.08 sec

    100% tests passed, 0 tests failed out of 130

    Total Test time (real) = 204.82 sec
:::
::::
:::::::

::: {#running-examples .section}
### Running Examples[](#running-examples "Link to this heading"){.headerlink}

ADIOS2 is best learned by
[examples](https://github.com/ornladios/ADIOS2/tree/master/examples){.reference
.external}.

A few very basic examples are described below:

  Directory                                                                 Description
  ------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------
  [`ADIOS2/examples/hello`{.docutils .literal .notranslate}]{.pre}          very basic "hello world"-style examples for reading and writing .bp files.
  [`ADIOS2/examples/heatTransfer`{.docutils .literal .notranslate}]{.pre}   2D Poisson solver for transients in Fourier's model of heat transfer. Outputs [`bp.dir`{.docutils .literal .notranslate}]{.pre} or HDF5.
  [`ADIOS2/examples/basics`{.docutils .literal .notranslate}]{.pre}         covers different [`Variable`{.docutils .literal .notranslate}]{.pre} use cases classified by the dimension.
:::
:::::::::::::::::::::::::::::::::

::::::: {#as-package .section}
## As Package[](#as-package "Link to this heading"){.headerlink}

::: {#conda .section}
### Conda[](#conda "Link to this heading"){.headerlink}

ADIOS2 can be obtained from anaconda cloud: [conda-forge
adios2](https://anaconda.org/conda-forge/adios2){.reference .external}
:::

::: {#pypi .section}
### PyPI[](#pypi "Link to this heading"){.headerlink}

ADIOS2 pip package can be downloaded with pip3 install adios2 or python3
-m pip install adios2. This is contains the serial build only, so MPI
programs cannot use it. See [adios2 on
PyPi](https://pypi.org/project/adios2/){.reference .external}
:::

::: {#spack .section}
### Spack[](#spack "Link to this heading"){.headerlink}

ADIOS2 is packaged in Spack. See [adios2 spack
package](https://packages.spack.io/package.html?name=adios2){.reference
.external}
:::

::: {#docker .section}
### Docker[](#docker "Link to this heading"){.headerlink}

Docker images including building and installation of dependencies and
ADIOS 2 containers for Ubuntu 20 and CentOS 7 can be found in: under the
directory
[scripts/docker/](https://github.com/ornladios/ADIOS2/tree/master/scripts/docker){.reference
.external}
:::
:::::::

::::::::: {#linking-adios-2 .section}
## Linking ADIOS 2[](#linking-adios-2 "Link to this heading"){.headerlink}

::::: {#from-cmake .section}
### From CMake[](#from-cmake "Link to this heading"){.headerlink}

ADIOS exports a CMake package configuration file that allows its targets
to be directly imported into another CMake project via the
[`find_package`{.docutils .literal .notranslate}]{.pre} command:

:::: {.highlight-cmake .notranslate}
::: highlight
    cmake_minimum_required(VERSION 3.12)
    project(MySimulation C CXX)

    find_package(MPI REQUIRED)
    find_package(ADIOS2 REQUIRED)
    #...
    add_library(my_library src1.cxx src2.cxx)
    target_link_libraries(my_library PRIVATE adios2::cxx11_mpi MPI::MPI_CXX)
:::
::::

When configuring your project you can then set the
[`ADIOS2_ROOT`{.docutils .literal .notranslate}]{.pre} or
[`ADIOS2_DIR`{.docutils .literal .notranslate}]{.pre} environment
variables to the install prefix of ADIOS2.
:::::

::::: {#from-non-cmake-build-systems .section}
### From non-CMake build systems[](#from-non-cmake-build-systems "Link to this heading"){.headerlink}

If you're not using CMake then you can manually get the necessary
compile and link flags for your project using [`adios2-config`{.docutils
.literal .notranslate}]{.pre}:

:::: {.highlight-bash .notranslate}
::: highlight
    $ /path/to/install-prefix/bin/adios2-config --cxxflags
    ADIOS2_DIR: /path/to/install-prefix
    -isystem /path/to/install-prefix/include -isystem /opt/ohpc/pub/mpi/openmpi3-gnu7/3.1.0/include -pthread -std=gnu++11
    $ /path/to/install-prefix/bin/adios2-config --cxxlibs
    ADIOS2_DIR: /path/to/install-prefix
    -Wl,-rpath,/path/to/install-prefix/lib:/opt/ohpc/pub/mpi/openmpi3-gnu7/3.1.0/lib /path/to/install-prefix/lib/libadios2.so.2.4.0 -pthread -Wl,-rpath -Wl,/opt/ohpc/pub/mpi/openmpi3-gnu7/3.1.0/lib -Wl,--enable-new-dtags -pthread /opt/ohpc/pub/mpi/openmpi3-gnu7/3.1.0/lib/libmpi.so -Wl,-rpath-link,/path/to/install-prefix/lib
:::
::::
:::::
:::::::::

:::::::::::: {#use-on-doe-machines .section}
## Use on DOE machines[](#use-on-doe-machines "Link to this heading"){.headerlink}

ADIOS2 is installed as part of the
[E4S](https://e4s-project.github.io/){.reference .external} software
stack and access to adios2 is the same as access to the many other
packages.

::::: {#nersc-perlmutter .section}
### NERSC Perlmutter[](#nersc-perlmutter "Link to this heading"){.headerlink}

To use adios2 on Perlmutter,

- load the e4s module

- pick your compiler environment with spack

- load adios2 with spack

:::: {.highlight-bash .notranslate}
::: highlight
    ~> module load e4s
      _____________________________________________________________________________________
       The Extreme-Scale Scientific Software Stack (E4S) is accessible via the Spack package manager.

       In order to access the production stack, you will need to load a spack
       environment. Here are some tips to get started:


       'spack env list' - List all Spack environments
       'spack env activate gcc' - Activate the "gcc" Spack environment
       'spack env status' - Display the active Spack environment
       'spack load amrex' - Load the "amrex" Spack package into your user environment

       For additional support, please refer to the following references:

         NERSC E4S Documentation: https://docs.nersc.gov/applications/e4s/
         E4S Documentation: https://e4s.readthedocs.io
         Spack Documentation: https://spack.readthedocs.io/en/latest/
         Spack Slack: https://spackpm.slack.com

      _____________________________________________________________________________________

    ~> spack env list
    ==> 4 environments
      cce  cuda  gcc  nvhpc
    ~> spack env activate gcc
    ~> spack load adios2

    ~> which bpls
    /global/common/software/spackecp/perlmutter/e4s-23.08/94543/spack/opt/spack/linux-sles15-zen3/gcc-12.3.0/adios2-2.9.1-iwv5lkkc5gyagr4uqrqr4v2fds7x66pk/bin/bpls

    ~> bpls -Vv
      blps: ADIOS file introspection utility

      Build configuration:
      ADIOS version: 2.9.1
      C++ Compiler:  GNU 12.3.0 (CrayPrgEnv)
      Target OS:     Linux-5.14.21-150400.24.81_12.0.87-cray_shasta_c
      Target Arch:   x86_64
      Available engines = 10: BP3, BP4, BP5, SST, SSC, Inline, MHS,
      ParaViewADIOSInSituEngine, Null, Skeleton
      Available operators = 4: BZip2, SZ, ZFP, PNG
      Available features = 16: BP5, DATAMAN, MHS, SST, FORTRAN, MPI, BZIP2, PNG,
      SZ, ZFP, O_DIRECT, CATALYST, SYSVSHMEM, ZEROMQ, PROFILING, ENDIAN_REVERSE
:::
::::
:::::

::::: {#olcf-frontier .section}
### OLCF Frontier[](#olcf-frontier "Link to this heading"){.headerlink}

OLCF installs the E4S packages in individual modules, hence adios2 is
also available as a module.

:::: {.highlight-bash .notranslate}
::: highlight
    $ module avail adios2
    ----- /sw/frontier/spack-envs/base/modules/spack/cray-sles15-x86_64/cray-mpich/8.1.23-j56azw5/cce/15.0.0 -----
     adios2/2.8.1    adios2/2.8.3 (D)

    Where:
     D:  Default Module

    $ module load adios2
    $ bpls -Vv
      blps: ADIOS file introspection utility

      Build configuration:
      ADIOS version: 2.8.3
      C++ Compiler:  GNU 12.2.0 (CrayPrgEnv)
      Target OS:     Linux-5.14.21-150400.24.11_12.0.57-cray_shasta_c
      Target Arch:   x86_64
:::
::::
:::::

::::: {#alcf-aurora .section}
### ALCF Aurora[](#alcf-aurora "Link to this heading"){.headerlink}

To use adios2 on Aurora,

- Load the default oneAPI (loaded automatically on login)

- module use /soft/modulefiles

- module load spack-pe-oneapi/0.5-rc1

This is a "metamoduile" that makes many software packages from E4S
loadable as modules.

:::: {.highlight-bash .notranslate}
::: highlight
    $ module use /soft/modulefiles
    $ module load spack-pe-oneapi/0.5-rc1
    $ module avail adios2

    ---------- /soft/packaging/spack/oneapi/0.5-rc1/modulefiles/Core -----------
    adios2/2.9.0-oneapi-mpich-testing
:::
::::
:::::
::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.toctree-wrapper .compound}
[]{#document-components/components}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#interface-components .section}
## Interface Components[](#interface-components "Link to this heading"){.headerlink}

:::: {#components-overview .section}
### Components Overview[](#components-overview "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

If you are doing simple tasks where performance is a non-critical aspect
please go to the [[High-Level APIs]{.std
.std-ref}](#document-api_high/api_high#high-level-apis){.reference
.internal} section for a quick start. If you are an HPC application
developer or you want to use ADIOS2 functionality in full please read
this chapter.
:::

The simple way to understand the big picture for the ADIOS2 unified user
interface components is to map each class to the actual definition of
the ADIOS acronym.

+-----------------------+-----------------------+-----------------------+
| Component             | Acronym               | Function              |
+-----------------------+-----------------------+-----------------------+
| **ADIOS**             | ADaptable             | Set MPI comm domain   |
|                       |                       |                       |
|                       |                       | Set runtime settings  |
|                       |                       |                       |
|                       |                       | Own other components  |
+-----------------------+-----------------------+-----------------------+
| **IO**                | I/O                   | Set engine            |
|                       |                       |                       |
|                       |                       | Set                   |
|                       |                       | variables/attributes  |
|                       |                       |                       |
|                       |                       | Set compile-time      |
|                       |                       | settings              |
+-----------------------+-----------------------+-----------------------+
| **Engine**            | System                | Execute heavy IO      |
|                       |                       | tasks                 |
|                       |                       |                       |
|                       |                       | Manage system         |
|                       |                       | resources             |
+-----------------------+-----------------------+-----------------------+

ADIOS2's public APIs are based on the natural choice for each supported
language to represent each ADIOS2 components and its interaction with
application datatypes. Thus,

  **Language**    **Component API**          **Application Data**
  --------------- -------------------------- ---------------------------------
  C++(11/newer)   objects/member functions   pointers/references/std::vector
  C               handler/functions          pointers
  Fortran         handler/subroutines        arrays up to 6D
  Python          objects/member functions   numpy arrays.

The following section provides a common overview to all languages based
on the C++11 APIs. For each specific language go to the [[Full
APIs]{.std .std-ref}](#document-api_full/api_full#full-apis){.reference
.internal} section, but it's highly recommended to read this section as
components map 1-to-1 in other languages.

The following figure depicts the components hierarchy from the
application's point of view.

![](https://i.imgur.com/y7bkQQt.png)

- 

  **ADIOS**: the ADIOS component is the starting point between an application and the ADIOS2 library. Applications provide:

  :   1.  the scope of the ADIOS object through the MPI communicator,

      2.  an optional runtime configuration file (in XML format) to
          allow changing settings without recompiling.

      The ADIOS component serves as a factory of adaptable IO
      components. Each IO must have a unique name within the scope of
      the ADIOS class object that created them with the DeclareIO
      function.

- 

  **IO**: the IO component is the bridge between the application specific settings, transports. It also serves as a factory of:

  :   1.  Variables

      2.  Attributes

      3.  Engines

- **Variable**: Variables are the link between self-describing
  representation in the ADIOS2 library and data from applications.
  Variables are identified by unique names in the scope of the
  particular IO that created them. When the Engine API functions are
  called, a Variable must be provided along with the application data.

- **Attribute**: Attributes add extra information to the overall
  variables dataset defined in the IO class. They can be single or array
  values.

- **Engine**: Engines define the actual system executing the heavy IO
  tasks at Open, BeginStep, Put, Get, EndStep and Close. Due to
  polymorphism, new IO system solutions can be developed quickly reusing
  internal components and reusing the same API. If IO.SetEngine is not
  called, the default engine is the binary-pack bp file reader and
  writer: **BPFile**.

- **Operator**: These define possible operations to be applied on
  adios2-managed data, for example, compression. This higher level
  abstraction is needed to provide support for callbacks, transforms,
  analytics, data models, etc. Any required task will be executed within
  the Engine. One or many operators can be associated with any of the
  adios2 objects or a group of them.
::::

:::::::::::: {#adios .section}
### ADIOS[](#adios "Link to this heading"){.headerlink}

The [`adios2::ADIOS`{.docutils .literal .notranslate}]{.pre} component
is the initial contact point between an application and the ADIOS2
library. Applications can be classified as MPI and non-MPI based. We
start by focusing on MPI applications as their non-MPI equivalent just
removes the MPI communicator.

:::: {.highlight-c++ .notranslate}
::: highlight
    /** ADIOS class factory of IO class objects */
    adios2::ADIOS adios("config.xml", MPI_COMM_WORLD);
:::
::::

This component is created by passing :

> <div>
>
> 1.  **Runtime config file** (optional): ADIOS2 xml runtime config
>     file, see [[Runtime Configuration Files]{.std
>     .std-ref}](#runtime-configuration-files){.reference .internal}.
>
> 2.  **MPI communicator** : which determines the scope of the ADIOS
>     library components in an application.
>
> </div>

[`adios2::ADIOS`{.docutils .literal .notranslate}]{.pre} objects can be
created in MPI and non-MPI (serial) mode. Optionally, a runtime
configuration file can be passed to the constructor indicating the full
file path, name and extension.

**Constructors for MPI applications**

:::: {.highlight-c++ .notranslate}
::: highlight
    /** Constructors */

    // version that accepts an optional runtime adios2 config file
    adios2::ADIOS(const std::string configFile,
                  MPI_COMM mpiComm = MPI_COMM_SELF);

    adios2::ADIOS(MPI_COMM mpiComm = MPI_COMM_SELF);

    /** Examples */
    adios2::ADIOS adios(MPI_COMM_WORLD);
    adios2::ADIOS adios("config.xml", MPI_COMM_WORLD);
:::
::::

**Constructors for non-MPI (serial) applications**

:::: {.highlight-c++ .notranslate}
::: highlight
    /** Constructors */
    adios2::ADIOS(const std::string configFile);

    adios2::ADIOS();

    /** Examples */
    adios2::ADIOS adios("config.xml");
    adios2::ADIOS adios; // Do not use () for empty constructor.
:::
::::

**Factory of IO components**: Multiple IO components (IO tasks) can be
created from within the scope of an ADIOS object by calling the
[`DeclareIO`{.docutils .literal .notranslate}]{.pre} function:

:::: {.highlight-c++ .notranslate}
::: highlight
    /** Signature */
    adios2::IO ADIOS::DeclareIO(const std::string ioName);

    /** Examples */
    adios2::IO bpWriter = adios.DeclareIO("BPWriter");
    adios2::IO bpReader = adios.DeclareIO("BPReader");
:::
::::

This function returns a reference to an existing IO class object that
lives inside the ADIOS object that created it. The [`ioName`{.docutils
.literal .notranslate}]{.pre} string must be unique; declaring two IO
objects with the same name will throw an exception. IO names are used to
identify IO components in the runtime configuration file, [[Runtime
Configuration Files]{.std
.std-ref}](#runtime-configuration-files){.reference .internal}.

As shown in the diagram below, each resulting IO object is self-managed
and independent, thus providing an adaptable way to perform different
kinds of I/O operations. Users must be careful not to create conflicts
between system level unique I/O identifiers: file names, IP address and
port, MPI Send/Receive message rank and tag, etc.

::: {.admonition .tip}
Tip

The ADIOS component is the only one whose memory is owned by the
application. Thus applications must decide on its scope. Any other
component of the ADIOS2 API refers to a component that lives inside the
ADIOS component(e.g. IO, Operator) or indirectly in the IO
component(Variable, Engine)
:::
::::::::::::

::::::::::::::::::::::::::: {#io .section}
### IO[](#io "Link to this heading"){.headerlink}

The [`IO`{.docutils .literal .notranslate}]{.pre} component is the
connection between how applications set up their input/output options by
selecting an [`Engine`{.docutils .literal .notranslate}]{.pre} and its
specific parameters, subscribing variables to data, and setting
supported transport modes to a particular [`Engine`{.docutils .literal
.notranslate}]{.pre}. Think of [`IO`{.docutils .literal
.notranslate}]{.pre} as a control panel for all the user-defined
parameters that applications would like to fine tune. None of the
[`IO`{.docutils .literal .notranslate}]{.pre} operations are heavyweight
until the [`Open`{.docutils .literal .notranslate}]{.pre} function that
generates an [`Engine`{.docutils .literal .notranslate}]{.pre} is
called. Its API allows

- generation of [`Variable`{.docutils .literal .notranslate}]{.pre} and
  [`Attribute`{.docutils .literal .notranslate}]{.pre} components
  containing information about the data in the input output process

- setting [`Engine`{.docutils .literal .notranslate}]{.pre}-specific
  parameters and adding supported modes of transport

- generation of [`Engine`{.docutils .literal .notranslate}]{.pre}
  objects to execute the actual IO tasks.

::: {.admonition .note}
Note

If two different engine types are needed (*e.g.* [`BPFile`{.docutils
.literal .notranslate}]{.pre}, [`SST`{.docutils .literal
.notranslate}]{.pre}), you must define two [`IO`{.docutils .literal
.notranslate}]{.pre} objects. Also, at reading always define separate
IOs to avoid [`Variable`{.docutils .literal .notranslate}]{.pre} name
clashes.
:::

:::::::: {#setting-a-particular-engine-and-its-parameters .section}
#### Setting a Particular Engine and its Parameters[](#setting-a-particular-engine-and-its-parameters "Link to this heading"){.headerlink}

Engines execute the heavy operations in ADIOS2. Each [`IO`{.docutils
.literal .notranslate}]{.pre} may select a type of [`Engine`{.docutils
.literal .notranslate}]{.pre} through the [`SetEngine`{.docutils
.literal .notranslate}]{.pre} function. If [`SetEngine`{.docutils
.literal .notranslate}]{.pre} is not called, then the
[`BPFile`{.docutils .literal .notranslate}]{.pre} engine is used.

:::: {.highlight-c++ .notranslate}
::: highlight
    /** Signature */
    void adios2::IO::SetEngine( const std::string engineType );

    /** Example */
    bpIO.SetEngine("BPFile");
:::
::::

Each [`Engine`{.docutils .literal .notranslate}]{.pre} allows the user
to fine tune execution of buffering and output tasks via parameters
passed to the [`IO`{.docutils .literal .notranslate}]{.pre} object.
These parameters are then propagated to the [`Engine`{.docutils .literal
.notranslate}]{.pre}. For a list of parameters allowed by each engine
see [[Available Engines]{.std .std-ref}](#available-engines){.reference
.internal}.

::: {.admonition .note}
Note

[`adios2::Params`{.docutils .literal .notranslate}]{.pre} is an alias to
[`std::map<std::string,std::string>`{.docutils .literal
.notranslate}]{.pre} to pass parameters as key-value string pairs, which
can be initialized with curly-brace initializer lists.
:::

:::: {.highlight-c++ .notranslate}
::: highlight
    /** Signature */
    /** Passing several parameters at once */
    void SetParameters(const adios2:Params& parameters);
    /** Passing one parameter key-value pair at a time */
    void SetParameter(const std::string key, const std::string value);

    /** Examples */
    io.SetParameters( { {"Threads", "4"},
                        {"ProfilingUnits", "Milliseconds"},
                        {"MaxBufferSize","2Gb"},
                        {"BufferGrowthFactor", "1.5" }
                        {"FlushStepsCount", "5" }
                      } );
    io.SetParameter( "Threads", "4" );
:::
::::
::::::::

::::: {#adding-supported-transports-with-parameters .section}
#### Adding Supported Transports with Parameters[](#adding-supported-transports-with-parameters "Link to this heading"){.headerlink}

The [`AddTransport`{.docutils .literal .notranslate}]{.pre} function
allows the user to specify how data is moved through the system, *e.g.*
RDMA, wide-area networks, or files. It returns an [`unsigned`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`int`{.docutils .literal .notranslate}]{.pre} handler for
each transport that can be used with the [`Engine::Close`{.docutils
.literal .notranslate}]{.pre} function at different times.
[`AddTransport`{.docutils .literal .notranslate}]{.pre} must provide
library specific settings that the low-level system library interface
allows.

:::: {.highlight-c++ .notranslate}
::: highlight
    /** Signature */
    unsigned int AddTransport( const std::string transportType,
                               const adios2::Params& parameters );

    /** Examples */
    const unsigned int file1 = io.AddTransport( "File",
                                                { {"Library", "fstream"},
                                                  {"Name","file1.bp" }
                                                } );

    const unsigned int file2 = io.AddTransport( "File",
                                                { {"Library", "POSIX"},
                                                  {"Name","file2.bp" }
                                                } );

    const unsigned int wan = io.AddTransport( "WAN",
                                              { {"Library", "Zmq"},
                                                {"IP","127.0.0.1" },
                                                {"Port","80"}
                                              } );
:::
::::
:::::

:::::::::::: {#defining-inquiring-and-removing-variables-and-attributes .section}
#### Defining, Inquiring and Removing Variables and Attributes[](#defining-inquiring-and-removing-variables-and-attributes "Link to this heading"){.headerlink}

The template functions [`DefineVariable<T>`{.docutils .literal
.notranslate}]{.pre} allows subscribing to data into ADIOS2 by returning
a reference to a [`Variable`{.docutils .literal .notranslate}]{.pre}
class object whose scope is the same as the [`IO`{.docutils .literal
.notranslate}]{.pre} object that created it. The user must provide a
unique name, the dimensions: MPI global: shape, MPI local: start and
offset, optionally a flag indicating that dimensions are known to be
constant, and a data pointer if defined in the application. Note: data
is not passed at this stage. This is done by the [`Engine`{.docutils
.literal .notranslate}]{.pre} functions [`Put`{.docutils .literal
.notranslate}]{.pre} and [`Get`{.docutils .literal .notranslate}]{.pre}
for Variables. See the [[Variable]{.std .std-ref}](#variable){.reference
.internal} section for supported types and shapes.

::: {.admonition .tip}
Tip

[`adios2::Dims`{.docutils .literal .notranslate}]{.pre} is an alias to
[`std::vector<std::size_t>`{.docutils .literal .notranslate}]{.pre},
while [`adios2::ConstantDims`{.docutils .literal .notranslate}]{.pre} is
an alias to bool [`true`{.docutils .literal .notranslate}]{.pre}. Use
them for code clarity.
:::

:::: {.highlight-c++ .notranslate}
::: highlight
    /** Signature */
    adios2::Variable<T>
        DefineVariable<T>(const std::string name,
                          const adios2::Dims &shape = {}, // Shape of global object
                          const adios2::Dims &start = {}, // Where to begin writing
                          const adios2::Dims &count = {}, // Where to end writing
                          const bool constantDims = false);

    /** Example */
    /** global array of floats with constant dimensions */
    adios2::Variable<float> varFloats =
        io.DefineVariable<float>("bpFloats",
                                 {size * Nx},
                                 {rank * Nx},
                                 {Nx},
                                 adios2::ConstantDims);
:::
::::

Attributes are extra-information associated with the current
[`IO`{.docutils .literal .notranslate}]{.pre} object. The function
[`DefineAttribute<T>`{.docutils .literal .notranslate}]{.pre} allows for
defining single value and array attributes. Keep in mind that Attributes
apply to all Engines created by the [`IO`{.docutils .literal
.notranslate}]{.pre} object and, unlike Variables which are passed to
each [`Engine`{.docutils .literal .notranslate}]{.pre} explicitly, their
definition contains their actual data.

:::: {.highlight-c++ .notranslate}
::: highlight
    /** Signatures */

    /** Single value */
    adios2::Attribute<T> DefineAttribute(const std::string &name,
                                  const T &value);

    /** Arrays */
    adios2::Attribute<T> DefineAttribute(const std::string &name,
                                  const T *array,
                                  const size_t elements);
:::
::::

In situations in which a variable and attribute has been previously
defined: 1) a variable/attribute reference goes out of scope, or 2) when
reading from an incoming stream, the [`IO`{.docutils .literal
.notranslate}]{.pre} can inquire about the status of variables and
attributes. If the inquired variable/attribute is not found, then the
overloaded [`bool()`{.docutils .literal .notranslate}]{.pre} operator of
returns [`false`{.docutils .literal .notranslate}]{.pre}.

:::: {.highlight-c++ .notranslate}
::: highlight
    /** Signature */
    adios2::Variable<T> InquireVariable<T>(const std::string &name) noexcept;
    adios2::Attribute<T> InquireAttribute<T>(const std::string &name) noexcept;

    /** Example */
    adios2::Variable<float> varPressure = io.InquireVariable<float>("pressure");
    if( varPressure ) // it exists
    {
      ...
    }
:::
::::

::: {.admonition .note}
Note

[`adios2::Variable`{.docutils .literal .notranslate}]{.pre} overloads
[`operator`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`bool()`{.docutils .literal .notranslate}]{.pre}
so that we can check for invalid states (e.g. variables haven't arrived
in a stream, weren't previously defined, or weren't written in a file).
:::

::: {.admonition .caution}
Caution

Since [`InquireVariable`{.docutils .literal .notranslate}]{.pre} and
[`InquireAttribute`{.docutils .literal .notranslate}]{.pre} are template
functions, both the name and type must match the data you are looking
for. If you do not know the type of the variable you are inquiring
about, it can be accessed with the [`InquireVariableType`{.docutils
.literal .notranslate}]{.pre} function.
:::
::::::::::::

:::::: {#opening-an-engine .section}
#### Opening an Engine[](#opening-an-engine "Link to this heading"){.headerlink}

The [`IO::Open`{.docutils .literal .notranslate}]{.pre} function creates
a new derived object of the abstract [`Engine`{.docutils .literal
.notranslate}]{.pre} class and returns a reference handler to the user.
A particular [`Engine`{.docutils .literal .notranslate}]{.pre} type is
set to the current [`IO`{.docutils .literal .notranslate}]{.pre}
component with the [`IO::SetEngine`{.docutils .literal
.notranslate}]{.pre} function. Engine polymorphism is handled internally
by the [`IO`{.docutils .literal .notranslate}]{.pre} class, which allows
subclassing future derived [`Engine`{.docutils .literal
.notranslate}]{.pre} types without changing the basic API.

[`Engine`{.docutils .literal .notranslate}]{.pre} objects are created in
various modes. The available modes are [`adios2::Mode::Read`{.docutils
.literal .notranslate}]{.pre},
[`adios2::Mode::ReadRandomAccess`{.docutils .literal
.notranslate}]{.pre}, [`adios2::Mode::Write`{.docutils .literal
.notranslate}]{.pre}, [`adios2::Mode::Append`{.docutils .literal
.notranslate}]{.pre}, [`adios2::Mode::Sync`{.docutils .literal
.notranslate}]{.pre}, [`adios2::Mode::Deferred`{.docutils .literal
.notranslate}]{.pre}, and [`adios2::Mode::Undefined`{.docutils .literal
.notranslate}]{.pre}.

:::: {.highlight-c++ .notranslate}
::: highlight
    /** Signatures */
    /** Provide a new MPI communicator other than from ADIOS->IO->Engine */
    adios2::Engine adios2::IO::Open(const std::string &name,
                                    const adios2::Mode mode,
                                    MPI_Comm mpiComm );

    /** Reuse the MPI communicator from ADIOS->IO->Engine \n or non-MPI serial mode */
    adios2::Engine adios2::IO::Open(const std::string &name,
                                    const adios2::Mode mode);


    /** Examples */

    /** Engine derived class, spawned to start Write operations */
    adios2::Engine bpWriter = io.Open("myVector.bp", adios2::Mode::Write);

    /** Engine derived class, spawned to start Read operations on rank 0 */
    if( rank == 0 )
    {
        adios2::Engine bpReader = io.Open("myVector.bp",
                                           adios2::Mode::Read,
                                           MPI_COMM_SELF);
    }
:::
::::

::: {.admonition .caution}
Caution

Always pass [`MPI_COMM_SELF`{.docutils .literal .notranslate}]{.pre} if
an [`Engine`{.docutils .literal .notranslate}]{.pre} lives in only one
MPI process. [`Open`{.docutils .literal .notranslate}]{.pre} and
[`Close`{.docutils .literal .notranslate}]{.pre} are collective
operations.
:::
::::::
:::::::::::::::::::::::::::

:::::::::::::::: {#variable .section}
### Variable[](#variable "Link to this heading"){.headerlink}

An [`adios2::Variable`{.docutils .literal .notranslate}]{.pre} is the
link between a piece of data coming from an application and its
metadata. This component handles all application variables classified by
data type and shape.

Each [`IO`{.docutils .literal .notranslate}]{.pre} holds a set of
Variables, and each [`Variable`{.docutils .literal .notranslate}]{.pre}
is identified with a unique name. They are created using the reference
from [`IO::DefineVariable<T>`{.docutils .literal .notranslate}]{.pre} or
retrieved using the pointer from [`IO::InquireVariable<T>`{.docutils
.literal .notranslate}]{.pre} functions in [[IO]{.std
.std-ref}](#io){.reference .internal}.

:::::::: {#data-types .section}
#### Data Types[](#data-types "Link to this heading"){.headerlink}

Only primitive types are supported in ADIOS2. Fixed-width types from
[\<cinttypes\> and
\<cstdint\>](https://en.cppreference.com/w/cpp/types/integer){.reference
.external} should be preferred when writing portable code. ADIOS2 maps
primitive types to equivalent fixed-width types (e.g. [`int`{.docutils
.literal .notranslate}]{.pre} -\> [`int32_t`{.docutils .literal
.notranslate}]{.pre}). In C++, acceptable types [`T`{.docutils .literal
.notranslate}]{.pre} in [`Variable<T>`{.docutils .literal
.notranslate}]{.pre} along with their preferred fix-width equivalent in
64-bit platforms are given below:

:::: {.highlight-c++ .notranslate}
::: highlight
    Data types Variables supported by ADIOS2 Variable<T>

    std::string (only used for global and local values, not arrays)
    char                      -> int8_t or uint8_t depending on compiler flags
    signed char               -> int8_t
    unsigned char             -> uint8_t
    short                     -> int16_t
    unsigned short            -> uint16_t
    int                       -> int32_t
    unsigned int              -> uint32_t
    long int                  -> int32_t or int64_t (Linux)
    long long int             -> int64_t
    unsigned long int         -> uint32_t or uint64_t (Linux)
    unsigned long long int    -> uint64_t
    float                     -> always 32-bit = 4 bytes
    double                    -> always 64-bit = 8 bytes
    long double               -> platform dependent
    std::complex<float>       -> always  64-bit = 8 bytes = 2 * float
    std::complex<double>      -> always 128-bit = 16 bytes = 2 * double
:::
::::

::: {.admonition .tip}
Tip

It's recommended to be consistent when using types for portability. If
data is defined as a fixed-width integer, define variables in ADIOS2
using a fixed-width type, *e.g.* for [`int32_t`{.docutils .literal
.notranslate}]{.pre} data types use [`DefineVariable<int32_t>`{.docutils
.literal .notranslate}]{.pre}.
:::

::: {.admonition .note}
Note

C, Fortran APIs: the enum and parameter adios2_type_XXX only provides
fixed-width types.
:::

::: {.admonition .note}
Note

Python APIs: use the equivalent fixed-width types from numpy. If
[`dtype`{.docutils .literal .notranslate}]{.pre} is not specified,
ADIOS2 handles numpy defaults just fine as long as primitive types are
passed.
:::
::::::::

::::::: {#shapes .section}
#### Shapes[](#shapes "Link to this heading"){.headerlink}

ADIOS2 is designed for MPI applications. Thus different application data
shapes must be supported depending on their scope within a particular
MPI communicator. The shape is defined at creation from the
[`IO`{.docutils .literal .notranslate}]{.pre} object by providing the
dimensions: shape, start, count in the
[`IO::DefineVariable<T>`{.docutils .literal .notranslate}]{.pre}. The
supported shapes are described below.

1\. **Global Single Value**: Only a name is required for their
definition. These variables are helpful for storing global information,
preferably managed by only one MPI process, that may or may not change
over steps: *e.g.* total number of particles, collective norm, number of
nodes/cells, etc.

> <div>
>
> :::: {.highlight-c++ .notranslate}
> ::: highlight
>     if( rank == 0 )
>     {
>        adios2::Variable<uint32_t> varNodes = io.DefineVariable<uint32_t>("Nodes");
>        adios2::Variable<std::string> varFlag = io.DefineVariable<std::string>("Nodes flag");
>        // ...
>        engine.Put( varNodes, nodes );
>        engine.Put( varFlag, "increased" );
>        // ...
>     }
> :::
> ::::
>
> ::: {.admonition .note}
> Note
>
> Variables of type [`string`{.docutils .literal .notranslate}]{.pre}
> are defined just like global single values. Multidimensional strings
> are supported for fixed size strings through variables of type
> [`char`{.docutils .literal .notranslate}]{.pre}.
> :::
>
> </div>

2\. **Global Array**: This is the most common shape used for storing
data that lives in several MPI processes. The image below illustrates
the definitions of the dimension components in a global array: shape,
start, and count.

> <div>
>
> ![](https://i.imgur.com/MKwNe5e.png)
>
> ::: {.admonition .warning}
> Warning
>
> Be aware of data ordering in your language of choice (row-major or
> column-major) as depicted in the figure above. Data decomposition is
> done by the application, not by ADIOS2.
> :::
>
> Start and Count local dimensions can be later modified with the
> [`Variable::SetSelection`{.docutils .literal .notranslate}]{.pre}
> function if it is not a constant dimensions variable.
>
> </div>

3\. **Local Value**: Values that are local to the MPI process. They are
defined by passing the [`adios2::LocalValueDim`{.docutils .literal
.notranslate}]{.pre} enum as follows:

> <div>
>
> :::: {.highlight-c++ .notranslate}
> ::: highlight
>     adios2::Variable<int32_t> varProcessID =
>           io.DefineVariable<int32_t>("ProcessID", {adios2::LocalValueDim})
>     //...
>     engine.Put<int32_t>(varProcessID, rank);
> :::
> ::::
>
> </div>

These values become visible on the reader as a single merged 1-D Global
Array whose size is determined by the number of writer ranks.

4\. **Local Array**: Arrays that are local to the MPI process. These are
commonly used to write checkpoint-restart data. Reading, however, needs
to be handled differently: each process' array has to be read
separately, using [`SetSelection`{.docutils .literal
.notranslate}]{.pre} per rank. The size of each process selection should
be discovered by the reading application by inquiring per-block size
information of the variable, and allocate memory accordingly.

> <div>
>
> ![](https://i.imgur.com/XLh2TUG.png)
>
> </div>

::: {.admonition .note}
Note

Constants are not handled separately from step-varying values in ADIOS2.
Simply write them only once from one rank.
:::

5\. **Joined Array**: Joined arrays are a variation of the Local Array
described above. Where LocalArrays are only available to the reader via
their block number, JoinedArrays are merged into a single global array
whose global dimensions are determined by the sum of the contributions
of each writer rank. Specifically: JoinedArrays are N-dimensional arrays
where one (and only one) specific dimension is the Joined dimension.
(The other dimensions must be constant and the same across all
contributions.) When defining a Joined variable, one specifies a shape
parameter that give the dimensionality of the array with the special
constant [`adios2::JoinedDim`{.docutils .literal .notranslate}]{.pre} in
the dimension to be joined. Unlike a Global Array definition, the start
parameter must be an empty Dims value. For example, the definition below
defines a 2-D Joined array where the first dimension is the one along
which blocks will be joined and the 2nd dimension is 5. Here this rank
is contributing two rows to this array.

:::: {.highlight-c++ .notranslate}
::: highlight
    auto var = outIO.DefineVariable<double>("table", {adios2::JoinedDim, 5}, {}, {2, 5});
:::
::::

If each of N writer ranks were to declare a variable like this and do a
single Put() in a timestep, the reader-side GlobalArray would have shape
{2\*N, 5} and all normal reader-side GlobalArray operations would be
applicable to it.

::: {.admonition .note}
Note

JoinedArrays are currently only supported by BP4 and BP5 engines, as
well as the SST engine with BP5 marshalling.
:::
:::::::

:::: {#global-array-capabilities-and-limitations .section}
#### Global Array Capabilities and Limitations[](#global-array-capabilities-and-limitations "Link to this heading"){.headerlink}

ADIOS2 is focusing on writing and reading N-dimensional, distributed,
global arrays of primitive types. The basic idea is that, usually, a
simulation has such a data structure in memory (distributed across
multiple processes) and wants to dump its content regularly as it
progresses. ADIOS2 was designed to:

1.  to do this writing and reading as fast as possible

2.  to enable reading any subsection of the array

[![](https://imgur.com/6nX67yq.png){style="width: 400px;"}](https://imgur.com/6nX67yq.png){.reference
.internal .image-reference}

The figure above shows a parallel application of 12 processes producing
a 2D array. Each process has a 2D array locally and the output is
created by placing them into a 4x3 pattern. A reading application's
individual process then can read any subsection of the entire global
array. In the figure, a 6 process application decomposes the array in a
3x2 pattern and each process reads a 2D array whose content comes from
multiple producer processes.

The figure hopefully helps to understand the basic concept but it can be
also misleading if it suggests limitations that are not there. Global
Array is simply a boundary in N-dimensional space where processes can
place their blocks of data. In the global space:

1.  one process can place multiple blocks

> <div>
>
> [![](https://imgur.com/Pb1s03h.png){style="width: 400px;"}](https://imgur.com/Pb1s03h.png){.reference
> .internal .image-reference}
>
> </div>

2.  does NOT need to be fully covered by the blocks

> <div>
>
> [![](https://imgur.com/qJBXYcQ.png){style="width: 400px;"}](https://imgur.com/qJBXYcQ.png){.reference
> .internal .image-reference}
>
> - at reading, unfilled positions will not change the allocated memory
>
> </div>

3.  blocks can overlap

> <div>
>
> [![](https://imgur.com/GA59lZ2.png){style="width: 300px;"}](https://imgur.com/GA59lZ2.png){.reference
> .internal .image-reference}
>
> - the reader will get values in an overlapping position from one of
>   the block but there is no control over from which block
>
> </div>

4.  each process can put a different size of block, or put multiple
    blocks of different sizes

5.  some process may not contribute anything to the global array

Over multiple output steps

1.  the processes CAN change the size (and number) of blocks in the
    array

> <div>
>
> - E.g. atom table: global size is fixed but atoms wander around
>   processes, so their block size is changing
>
>   [![](https://imgur.com/DorjG2q.png){style="width: 400px;"}](https://imgur.com/DorjG2q.png){.reference
>   .internal .image-reference}
>
> </div>

2.  the global dimensions CAN change over output steps

> <div>
>
> - but then you cannot read multiple steps at once
>
> - E.g. particle table size changes due to particles disappearing or
>   appearing
>
>   [![](https://imgur.com/nkuHeVX.png){style="width: 400px;"}](https://imgur.com/nkuHeVX.png){.reference
>   .internal .image-reference}
>
> </div>

Limitations of the ADIOS global array concept

1.  Indexing starts from 0

2.  Cyclic data patterns are not supported; only blocks can be written
    or read

3.  If Some blocks may fully or partially fall outside of the global
    boundary, the reader will not be able to read those parts

::: {.admonition .note}
Note

Technically, the content of the individual blocks is kept in the BP
format (but not in HDF5 format) and in staging. If you really, really
want to retrieve all the blocks, you need to handle this array as a
Local Array and read the blocks one by one.
:::
::::
::::::::::::::::

::::: {#attribute .section}
### Attribute[](#attribute "Link to this heading"){.headerlink}

Attributes are extra information associated with a particular IO
component. They can be thought of as a very simplified
[`Variable`{.docutils .literal .notranslate}]{.pre}, but with the goal
of adding extra metadata. The most common use is the addition of
human-readable metadata (*e.g.* [`"experiment`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`name"`{.docutils .literal .notranslate}]{.pre},
[`"date`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`and`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`time"`{.docutils .literal .notranslate}]{.pre},
[`"04,27,2017"`{.docutils .literal .notranslate}]{.pre}, or a schema).

Currently, ADIOS2 supports single values and arrays of primitive types
(excluding [`complex<T>`{.docutils .literal .notranslate}]{.pre}) for
the template type in the [`IO::DefineAttribute<T>`{.docutils .literal
.notranslate}]{.pre} and [`IO::InquireAttribute<T>`{.docutils .literal
.notranslate}]{.pre} function (in C++).

The data types supported for ADIOS2 [`Attributes`{.docutils .literal
.notranslate}]{.pre} are

:::: {.highlight-c++ .notranslate}
::: highlight
    std::string
    char
    signed char
    unsigned char
    short
    unsigned short
    int
    unsigned int
    long int
    long long int
    unsigned long int
    unsigned long long int
    float
    double
    long double
:::
::::

The returned object ([`DefineAttribute`{.docutils .literal
.notranslate}]{.pre} or [`InquireAttribute`{.docutils .literal
.notranslate}]{.pre}) only serves the purpose to inspect the current
[`Attribute<T>`{.docutils .literal .notranslate}]{.pre} information
within code.
:::::

:::::::::::::::::::::::::::: {#engine .section}
### Engine[](#engine "Link to this heading"){.headerlink}

The Engine abstraction component serves as the base interface to the
actual IO systems executing the heavy-load tasks performed when
producing and consuming data.

Engine functionality works around two concepts:

1.  Variables are published ([`Put`{.docutils .literal
    .notranslate}]{.pre}) and consumed ([`Get`{.docutils .literal
    .notranslate}]{.pre}) in "steps" in either "File" random-access (all
    steps are available) or "Streaming" (steps are available as they are
    produced in a step-by-step fashion).

2.  Variables are published ([`Put`{.docutils .literal
    .notranslate}]{.pre}) and consumed ([`Get`{.docutils .literal
    .notranslate}]{.pre}) using a "sync" or "deferred" (lazy evaluation)
    policy.

::: {.admonition .caution}
Caution

The ADIOS2 "step" is a logical abstraction that means different things
depending on the application context. Examples: "time step", "iteration
step", "inner loop step", or "interpolation step", "variable section",
etc. It only indicates how the variables were passed into ADIOS2 (e.g.
I/O steps) without the user having to index this information on their
own.
:::

::: {.admonition .tip}
Tip

Publishing and consuming data is a round-trip in ADIOS2.
[`Put`{.docutils .literal .notranslate}]{.pre} and [`Get`{.docutils
.literal .notranslate}]{.pre} APIs for write/append and read modes aim
to be "symmetric", reusing functions, objects, and semantics as much as
possible.
:::

The rest of the section explains the important concepts.

::::: {#beginstep .section}
#### BeginStep[](#beginstep "Link to this heading"){.headerlink}

> <div>
>
> Begins a logical step and return the status (via an enum) of the
> stream to be read/written. In streaming engines [`BeginStep`{.docutils
> .literal .notranslate}]{.pre} is where the receiver tries to acquire a
> new step in the reading process. The full signature allows for a mode
> and timeout parameters. See [[Supported Engines]{.std
> .std-ref}](#document-engines/engines#supported-engines){.reference
> .internal} for more information on what engine allows. A simplified
> signature allows each engine to pick reasonable defaults.
>
> </div>

:::: {.highlight-c++ .notranslate}
::: highlight
    // Full signature
    StepStatus BeginStep(const StepMode mode,
                         const float timeoutSeconds = -1.f);

    // Simplified signature
    StepStatus BeginStep();
:::
::::
:::::

::::: {#endstep .section}
#### EndStep[](#endstep "Link to this heading"){.headerlink}

> <div>
>
> Ends logical step, flush to transports depending on IO parameters and
> engine default behavior.
>
> </div>

::: {.admonition .tip}
Tip

To write portable code for a step-by-step access across ADIOS2 engines
(file and streaming engines) use [`BeginStep`{.docutils .literal
.notranslate}]{.pre} and [`EndStep`{.docutils .literal
.notranslate}]{.pre}.
:::

::: {.admonition .danger}
Danger

Accessing random steps in read mode (e.g.
[`Variable<T>::SetStepSelection`{.docutils .literal .notranslate}]{.pre}
in file engines) will create a conflict with [`BeginStep`{.docutils
.literal .notranslate}]{.pre} and [`EndStep`{.docutils .literal
.notranslate}]{.pre} and will throw an exception. In file engines, data
is either consumed in a random-access or step-by-step mode, but not
both.
:::
:::::

::: {#close .section}
#### Close[](#close "Link to this heading"){.headerlink}

> <div>
>
> Close current engine and underlying transports. An [`Engine`{.docutils
> .literal .notranslate}]{.pre} object can't be used after this call.
>
> </div>
:::

::::: {#put-modes-and-memory-contracts .section}
#### Put: modes and memory contracts[](#put-modes-and-memory-contracts "Link to this heading"){.headerlink}

[`Put`{.docutils .literal .notranslate}]{.pre} publishes data in ADIOS2.
It is unavailable unless the [`Engine`{.docutils .literal
.notranslate}]{.pre} is created in [`Write`{.docutils .literal
.notranslate}]{.pre} or [`Append`{.docutils .literal
.notranslate}]{.pre} mode.

The most common signature is the one that passes a
[`Variable<T>`{.docutils .literal .notranslate}]{.pre} object for the
metadata, a [`const`{.docutils .literal .notranslate}]{.pre} piece of
contiguous memory for the data, and a mode for either
[`Deferred`{.docutils .literal .notranslate}]{.pre} (data may be
collected at Put() or not until EndStep/PerformPuts/Close) or
[`Sync`{.docutils .literal .notranslate}]{.pre} (data is reusable
immediately). This is the most common use case in applications.

1.  Deferred (default) or Sync mode, data is contiguous memory

    :::: {.highlight-c++ .notranslate}
    ::: highlight
        void Put(Variable<T> variable, const T* data, const adios2::Mode = adios2::Mode::Deferred);
    :::
    ::::

ADIOS2 Engines also provide direct access to their buffer memory.
[`Variable<T>::Span`{.docutils .literal .notranslate}]{.pre} is based on
a subset of the upcoming [C++20
std::span](https://en.cppreference.com/w/cpp/container/span){.reference
.external}, which is a non-owning reference to a block of contiguous
memory. Spans act as a 1D container meant to be filled out by the
application. They provide the standard API of an STL container,
providing [`begin()`{.docutils .literal .notranslate}]{.pre} and
[`end()`{.docutils .literal .notranslate}]{.pre} iterators,
[`operator[]`{.docutils .literal .notranslate}]{.pre} and
[`at()`{.docutils .literal .notranslate}]{.pre}, as well as
[`data()`{.docutils .literal .notranslate}]{.pre} and
[`size()`{.docutils .literal .notranslate}]{.pre}.

[`Variable<T>::Span`{.docutils .literal .notranslate}]{.pre} is helpful
in situations in which temporaries are needed to create contiguous
pieces of memory from non-contiguous pieces (*e.g.* tables, arrays
without ghost-cells), or just to save memory as the returned
[`Variable<T>::Span`{.docutils .literal .notranslate}]{.pre} can be used
for computation, thus avoiding an extra copy from user memory into the
ADIOS2 buffer. [`Variable<T>::Span`{.docutils .literal
.notranslate}]{.pre} combines a hybrid [`Sync`{.docutils .literal
.notranslate}]{.pre} and [`Deferred`{.docutils .literal
.notranslate}]{.pre} mode, in which the initial value and memory
allocations are [`Sync`{.docutils .literal .notranslate}]{.pre}, while
data population and metadata collection are done at
EndStep/PerformPuts/Close. Memory contracts are explained later in this
chapter followed by examples.

The following [`Variable<T>::Span`{.docutils .literal
.notranslate}]{.pre} signatures are available:

2.  Return a span setting a default [`T()`{.docutils .literal
    .notranslate}]{.pre} value into a default buffer

    :::: {.highlight-c++ .notranslate}
    ::: highlight
        Variable<T>::Span Put(Variable<T> variable);
    :::
    ::::

3\. Return a span setting an initial fill value into a certain buffer.
If span is not returned then the [`fillValue`{.docutils .literal
.notranslate}]{.pre} is fixed for that block.

> <div>
>
> :::: {.highlight-c++ .notranslate}
> ::: highlight
>     Variable<T>::Span Put(Variable<T> variable, const size_t bufferID, const T fillValue);
> :::
> ::::
>
> </div>

In summary, the following are the current Put signatures for publishing
data in ADIOS 2:

1.  [`Deferred`{.docutils .literal .notranslate}]{.pre} (default) or
    [`Sync`{.docutils .literal .notranslate}]{.pre} mode, data is
    contiguous memory put in an ADIOS2 buffer.

    :::: {.highlight-c++ .notranslate}
    ::: highlight
        void Put(Variable<T> variable, const T* data, const adios2::Mode = adios2::Mode::Deferred);
    :::
    ::::

2\. Return a span setting a default [`T()`{.docutils .literal
.notranslate}]{.pre} value into a default ADIOS2 buffer. If span is not
returned then the default [`T()`{.docutils .literal .notranslate}]{.pre}
is fixed for that block (e.g. zeros).

> <div>
>
> :::: {.highlight-c++ .notranslate}
> ::: highlight
>     Variable<T>::Span Put(Variable<T> variable);
> :::
> ::::
>
> </div>

3\. Return a span setting an initial fill value into a certain buffer.
If span is not returned then the [`fillValue`{.docutils .literal
.notranslate}]{.pre} is fixed for that block.

> <div>
>
> :::: {.highlight-c++ .notranslate}
> ::: highlight
>     Variable<T>::Span Put(Variable<T> variable, const size_t bufferID, const T fillValue);
> :::
> ::::
>
> </div>

The following table summarizes the memory contracts required by ADIOS2
engines between [`Put`{.docutils .literal .notranslate}]{.pre}
signatures and the data memory coming from an application:

+-----------------------+-----------------------+---------------------------+
| Put                   | Data Memory           | Contract                  |
+-----------------------+-----------------------+---------------------------+
| Deferred              | Pointer               | do not modify until       |
|                       |                       | PerformPuts/EndStep/Close |
|                       | Contents              |                           |
|                       |                       | consumed at Put or        |
|                       |                       | PerformPuts/EndStep/Close |
+-----------------------+-----------------------+---------------------------+
| Sync                  | Pointer               | modify after Put          |
|                       |                       |                           |
|                       | Contents              | consumed at Put           |
+-----------------------+-----------------------+---------------------------+
| Span                  | Pointer               | modified by new Spans,    |
|                       |                       | updated span              |
|                       | Contents              | iterators/data            |
|                       |                       |                           |
|                       |                       | consumed at               |
|                       |                       | PerformPuts/EndStep/Close |
+-----------------------+-----------------------+---------------------------+

::: {.admonition .note}
Note

In Fortran (array) and Python (numpy array) avoid operations that modify
the internal structure of an array (size) to preserve the address.
:::

Each [`Engine`{.docutils .literal .notranslate}]{.pre} will give a
concrete meaning to each functions signatures, but all of them must
follow the same memory contracts to the "data pointer": the memory
address itself, and the "data contents": memory bits (values).

1.  **Put in Deferred or lazy evaluation mode (default)**: this is the
    preferred mode as it allows [`Put`{.docutils .literal
    .notranslate}]{.pre} calls to be "grouped" before potential data
    transport at the first encounter of [`PerformPuts`{.docutils
    .literal .notranslate}]{.pre}, [`EndStep`{.docutils .literal
    .notranslate}]{.pre} or [`Close`{.docutils .literal
    .notranslate}]{.pre}.

    > <div>
    >
    > :::: {.highlight-c++ .notranslate}
    > ::: highlight
    >     Put(variable, data);
    >     Put(variable, data, adios2::Mode::Deferred);
    > :::
    > ::::
    >
    > </div>

    Deferred memory contracts:

    - "data pointer" do not modify (e.g. resize) until first call to
      [`PerformPuts`{.docutils .literal .notranslate}]{.pre},
      [`EndStep`{.docutils .literal .notranslate}]{.pre} or
      [`Close`{.docutils .literal .notranslate}]{.pre}.

    - "data contents" may be consumed immediately or at first call to
      [`PerformPuts`{.docutils .literal .notranslate}]{.pre},
      [`EndStep`{.docutils .literal .notranslate}]{.pre} or
      [`Close`{.docutils .literal .notranslate}]{.pre}. Do not modify
      data contents after Put.

    Usage:

    > <div>
    >
    > :::: {.highlight-c++ .notranslate}
    > ::: highlight
    >     // recommended use:
    >     // set "data pointer" and "data contents"
    >     // before Put
    >     data[0] = 10;
    >
    >     // Puts data pointer into adios2 engine
    >     // associated with current variable metadata
    >     engine.Put(variable, data);
    >
    >     // Modifying data after Put(Deferred) may result in different
    >     // results with different engines
    >     // Any resize of data after Put(Deferred) may result in
    >     // memory corruption or segmentation faults
    >     data[1] = 10;
    >
    >     // "data contents" must not have been changed
    >     // "data pointer" must be the same as in Put
    >     engine.EndStep();
    >     //engine.PerformPuts();
    >     //engine.Close();
    >
    >     // now data pointer can be reused or modified
    > :::
    > ::::
    >
    > </div>

    ::: {.admonition .tip}
    Tip

    It's recommended practice to set all data contents before
    [`Put`{.docutils .literal .notranslate}]{.pre} in deferred mode to
    minimize the risk of modifying the data pointer (not just the
    contents) before PerformPuts/EndStep/Close.
    :::

2\. **Put in Sync mode**: this is the special case, data pointer becomes
reusable right after [`Put`{.docutils .literal .notranslate}]{.pre}.
Only use it if absolutely necessary (*e.g.* memory bound application or
out of scope data, temporary).

> <div>
>
> > <div>
> >
> > :::: {.highlight-c++ .notranslate}
> > ::: highlight
> >     Put(variable, *data, adios2::Mode::Sync);
> > :::
> > ::::
> >
> > </div>
>
> Sync memory contracts:
>
> - "data pointer" and "data contents" can be modified after this call.
>
> Usage:
>
> > <div>
> >
> > :::: {.highlight-c++ .notranslate}
> > ::: highlight
> >     // set "data pointer" and "data contents"
> >     // before Put in Sync mode
> >     data[0] = 10;
> >
> >     // Puts data pointer into adios2 engine
> >     // associated with current variable metadata
> >     engine.Put(variable, data, adios2::Mode::Sync);
> >
> >     // data pointer and contents can be reused
> >     // in application
> > :::
> > ::::
> >
> > </div>
>
> </div>

3.  **Put returning a Span**: signature that allows access to adios2
    internal buffer.

    Use cases:

    - population from non-contiguous memory structures

    - memory-bound applications

    Limitations:

    - does not allow operations (compression)

    - must keep engine and variables within scope of span usage

    Span memory contracts:

    - "data pointer" provided by the engine and returned by
      [`span.data()`{.docutils .literal .notranslate}]{.pre}, might
      change with the generation of a new span. It follows iterator
      invalidation rules from std::vector. Use span.data() or iterators,
      span.begin(), span.end() to keep an updated data pointer.

    - span "data contents" are published at the first call to
      [`PerformPuts`{.docutils .literal .notranslate}]{.pre},
      [`EndStep`{.docutils .literal .notranslate}]{.pre} or
      [`Close`{.docutils .literal .notranslate}]{.pre}

    Usage:

    > <div>
    >
    > :::: {.highlight-c++ .notranslate}
    > ::: highlight
    >     // return a span into a block of memory
    >     // set memory to default T()
    >     adios2::Variable<int32_t>::Span span1 = Put(var1);
    >
    >     // just like with std::vector::data()
    >     // iterator invalidation rules
    >     // dataPtr might become invalid
    >     // always use span1.data() directly
    >     T* dataPtr = span1.data();
    >
    >     // set memory value to -1 in buffer 0
    >     adios2::Variable<float>::Span span2 = Put(var2, 0, -1);
    >
    >     // not returning a span just sets a constant value
    >     Put(var3);
    >     Put(var4, 0, 2);
    >
    >     // fill span1
    >     span1[0] = 0;
    >     span1[1] = 1;
    >     span1[2] = 2;
    >
    >     // fill span2
    >     span2[1] = 1;
    >     span2[2] = 2;
    >
    >     // here collect all spans
    >     // they become invalid
    >     engine.EndStep();
    >     //engine.PerformPuts();
    >     //engine.Close();
    >
    >     // var1 = { 0, 1, 2 };
    >     // var2 = { -1., 1., 2.};
    >     // var3 = { 0, 0, 0};
    >     // var4 = { 2, 2, 2};
    > :::
    > ::::
    >
    > </div>

The [`data`{.docutils .literal .notranslate}]{.pre} fed to the
[`Put`{.docutils .literal .notranslate}]{.pre} function is assumed to be
allocated on the Host (default mode). In order to use data allocated on
the device, the memory space of the variable needs to be set to Cuda.

> <div>
>
> :::: {.highlight-c++ .notranslate}
> ::: highlight
>     variable.SetMemorySpace(adios2::MemorySpace::CUDA);
>     engine.Put(variable, gpuData, mode);
> :::
> ::::
>
> </div>

::: {.admonition .note}
Note

Only CUDA allocated buffers are supported for device data. Only the BP4
and BP5 engines are capable of receiving device allocated buffers.
:::
:::::

:::: {#performputs .section}
#### PerformPuts[](#performputs "Link to this heading"){.headerlink}

> <div>
>
> Executes all pending [`Put`{.docutils .literal .notranslate}]{.pre}
> calls in deferred mode and collects span data. Specifically this call
> copies Put(Deferred) data into internal ADIOS buffers, as if Put(Sync)
> had been used instead.
>
> </div>

::: {.admonition .note}
Note

This call allows the reuse of user buffers, but may negatively impact
performance on some engines.
:::
::::

:::: {#performdatawrite .section}
#### PerformDataWrite[](#performdatawrite "Link to this heading"){.headerlink}

> <div>
>
> If supported by the engine, moves data from prior [`Put`{.docutils
> .literal .notranslate}]{.pre} calls to disk
>
> </div>

::: {.admonition .note}
Note

- Currently only supported by the [`BP5`{.docutils .literal
  .notranslate}]{.pre} file engine.

- This is a [`collective`{.docutils .literal .notranslate}]{.pre}
  function.
:::
::::

:::: {#get-modes-and-memory-contracts .section}
#### Get: modes and memory contracts[](#get-modes-and-memory-contracts "Link to this heading"){.headerlink}

[`Get`{.docutils .literal .notranslate}]{.pre} is the function for
consuming data in ADIOS2. It is available when an Engine is created
using [`Read`{.docutils .literal .notranslate}]{.pre} mode at
[`IO::Open`{.docutils .literal .notranslate}]{.pre}. ADIOS2
[`Put`{.docutils .literal .notranslate}]{.pre} and [`Get`{.docutils
.literal .notranslate}]{.pre} semantics are as symmetric as possible
considering that they are opposite operations (*e.g.* [`Put`{.docutils
.literal .notranslate}]{.pre} passes [`const`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`T*`{.docutils
.literal .notranslate}]{.pre}, while [`Get`{.docutils .literal
.notranslate}]{.pre} populates a non-const [`T*`{.docutils .literal
.notranslate}]{.pre}).

The [`Get`{.docutils .literal .notranslate}]{.pre} signatures are
described below.

1.  [`Deferred`{.docutils .literal .notranslate}]{.pre} (default) or
    [`Sync`{.docutils .literal .notranslate}]{.pre} mode, data is
    contiguous pre-allocated memory:

    :::: {.highlight-c++ .notranslate}
    ::: highlight
        Get(Variable<T> variable, const T* data, const adios2::Mode = adios2::Mode::Deferred);
    :::
    ::::

2.  In this signature, [`dataV`{.docutils .literal .notranslate}]{.pre}
    is automatically resized by ADIOS2 based on the
    [`Variable`{.docutils .literal .notranslate}]{.pre} selection:

    :::: {.highlight-c++ .notranslate}
    ::: highlight
        Get(Variable<T> variable, std::vector<T>& dataV, const adios2::Mode = adios2::Mode::Deferred);
    :::
    ::::

The following table summarizes the memory contracts required by ADIOS2
engines between [`Get`{.docutils .literal .notranslate}]{.pre}
signatures and the pre-allocated (except when using C++11
[`std::vector`{.docutils .literal .notranslate}]{.pre}) data memory
coming from an application:

+-----------------------+-----------------------+---------------------------+
| Get                   | Data Memory           | Contract                  |
+-----------------------+-----------------------+---------------------------+
| Deferred              | Pointer               | do not modify until       |
|                       |                       | PerformGets/EndStep/Close |
|                       | Contents              |                           |
|                       |                       | populated at Get or       |
|                       |                       | PerformGets/EndStep/Close |
+-----------------------+-----------------------+---------------------------+
| Sync                  | Pointer               | modify after Get          |
|                       |                       |                           |
|                       | Contents              | populated at Get          |
+-----------------------+-----------------------+---------------------------+

1.  **Get in Deferred or lazy evaluation mode (default)**: this is the
    preferred mode as it allows [`Get`{.docutils .literal
    .notranslate}]{.pre} calls to be "grouped" before potential data
    transport at the first encounter of [`PerformPuts`{.docutils
    .literal .notranslate}]{.pre}, [`EndStep`{.docutils .literal
    .notranslate}]{.pre} or [`Close`{.docutils .literal
    .notranslate}]{.pre}.

    > <div>
    >
    > :::: {.highlight-c++ .notranslate}
    > ::: highlight
    >     Get(variable, data);
    >     Get(variable, data, adios2::Mode::Deferred);
    > :::
    > ::::
    >
    > </div>

    Deferred memory contracts:

    - "data pointer": do not modify (e.g. resize) until first call to
      [`PerformPuts`{.docutils .literal .notranslate}]{.pre},
      [`EndStep`{.docutils .literal .notranslate}]{.pre} or
      [`Close`{.docutils .literal .notranslate}]{.pre}.

    - "data contents": populated at [`Put`{.docutils .literal
      .notranslate}]{.pre}, or at first call to [`PerformPuts`{.docutils
      .literal .notranslate}]{.pre}, [`EndStep`{.docutils .literal
      .notranslate}]{.pre} or [`Close`{.docutils .literal
      .notranslate}]{.pre}.

    Usage:\`

    > <div>
    >
    > :::: {.highlight-c++ .notranslate}
    > ::: highlight
    >     std::vector<double> data;
    >
    >     // resize memory to expected size
    >     data.resize(varBlockSize);
    >     // valid if all memory is populated
    >     // data.reserve(varBlockSize);
    >
    >     // Gets data pointer to adios2 engine
    >     // associated with current variable metadata
    >     engine.Get(variable, data.data() );
    >
    >     // optionally pass data std::vector
    >     // leave resize to adios2
    >     //engine.Get(variable, data);
    >
    >     // "data pointer" must be the same as in Get
    >     engine.EndStep();
    >     // "data contents" are now ready
    >     //engine.PerformPuts();
    >     //engine.Close();
    >
    >     // now data pointer can be reused or modified
    > :::
    > ::::
    >
    > </div>

2\. **Put in Sync mode**: this is the special case, data pointer becomes
reusable right after Put. Only use it if absolutely necessary (*e.g.*
memory bound application or out of scope data, temporary).

> <div>
>
> > <div>
> >
> > :::: {.highlight-c++ .notranslate}
> > ::: highlight
> >     Get(variable, *data, adios2::Mode::Sync);
> > :::
> > ::::
> >
> > </div>
>
> Sync memory contracts:
>
> - "data pointer" and "data contents" can be modified after this call.
>
> Usage:
>
> > <div>
> >
> > :::: {.highlight-c++ .notranslate}
> > ::: highlight
> >     .. code-block:: c++
> >
> >     std::vector<double> data;
> >
> >     // resize memory to expected size
> >     data.resize(varBlockSize);
> >     // valid if all memory is populated
> >     // data.reserve(varBlockSize);
> >
> >     // Gets data pointer to adios2 engine
> >     // associated with current variable metadata
> >     engine.Get(variable, data.data() );
> >
> >     // "data contents" are ready
> >     // "data pointer" can be reused by the application
> > :::
> > ::::
> >
> > </div>
>
> </div>

::: {.admonition .note}
Note

[`Get`{.docutils .literal .notranslate}]{.pre} doesn't support returning
spans.
:::
::::

::: {#performgets .section}
#### PerformGets[](#performgets "Link to this heading"){.headerlink}

> <div>
>
> Executes all pending [`Get`{.docutils .literal .notranslate}]{.pre}
> calls in deferred mode.
>
> </div>
:::

::::::: {#engine-usage-example .section}
#### Engine usage example[](#engine-usage-example "Link to this heading"){.headerlink}

The following example illustrates the basic API usage in write mode for
data generated at each application step:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::Engine engine = io.Open("file.bp", adios2::Mode::Write);

    for( size_t i = 0; i < steps; ++i )
    {
       // ... Application *data generation

       engine.BeginStep(); //next "logical" step for this application

       engine.Put(varT, dataT, adios2::Mode::Sync);
       // dataT memory already consumed by engine
       // Application can modify dataT address and contents

       // deferred functions return immediately (lazy evaluation),
       // dataU, dataV and dataW pointers and contents must not be modified
       // until PerformPuts, EndStep or Close.
       // 1st batch
       engine.Put(varU, dataU);
       engine.Put(varV, dataV);

       // in this case adios2::Mode::Deferred is redundant,
       // as this is the default option
       engine.Put(varW, dataW, adios2::Mode::Deferred);

       // effectively dataU, dataV, dataW are "deferred"
       // possibly until the first call to PerformPuts, EndStep or Close.
       // Application MUST NOT modify the data pointer (e.g. resize
       // memory) or change data contents.
       engine.PerformPuts();

       // dataU, dataV, dataW pointers/values can now be reused

       // ... Application modifies dataU, dataV, dataW

       //2nd batch
       dataU[0] = 10
       dataV[0] = 10
       dataW[0] = 10
       engine.Put(varU, dataU);
       engine.Put(varV, dataV);
       engine.Put(varW, dataW);
       // Application MUST NOT modify dataU, dataV and dataW pointers (e.g. resize),
       // Contents should also not be modified after Put() and before
       // PerformPuts() because ADIOS may access the data immediately
       // or not until PerformPuts(), depending upon the engine
       engine.PerformPuts();

       // dataU, dataV, dataW pointers/values can now be reused

       // Puts a varP block of zeros
       adios2::Variable<double>::Span spanP = Put<double>(varP);

       // Not recommended mixing static pointers,
       // span follows
       // the same pointer/iterator invalidation
       // rules as std::vector
       T* p = spanP.data();

       // Puts a varMu block of 1e-6
       adios2::Variable<double>::Span spanMu = Put<double>(varMu, 0, 1e-6);

       // p might be invalidated
       // by a new span, use spanP.data() again
       foo(spanP.data());

       // Puts a varRho block with a constant value of 1.225
       Put<double>(varMu, 0, 1.225);

       // it's preferable to start modifying spans
       // after all of them are created
       foo(spanP.data());
       bar(spanMu.begin(), spanMu.end());


       engine.EndStep();
       // spanP, spanMu are consumed by the library
       // end of current logical step,
       // default behavior: transport data
    }

    engine.Close();
    // engine is unreachable and all data should be transported
    ...
:::
::::

::: {.admonition .tip}
Tip

Prefer default [`Deferred`{.docutils .literal .notranslate}]{.pre} (lazy
evaluation) functions as they have the potential to group several
variables with the trade-off of not being able to reuse the pointers
memory space until [`EndStep`{.docutils .literal .notranslate}]{.pre},
[`PerformPuts`{.docutils .literal .notranslate}]{.pre},
[`PerformGets`{.docutils .literal .notranslate}]{.pre}, or
[`Close`{.docutils .literal .notranslate}]{.pre}. Only use
[`Sync`{.docutils .literal .notranslate}]{.pre} if you really have to
(*e.g.* reuse memory space from pointer). ADIOS2 prefers a step-based IO
in which everything is known ahead of time when writing an entire step.
:::

::: {.admonition .danger}
Danger

The default behavior of ADIOS2 [`Put`{.docutils .literal
.notranslate}]{.pre} and [`Get`{.docutils .literal .notranslate}]{.pre}
calls IS NOT synchronized, but rather deferred. It's actually the
opposite of [`MPI_Put`{.docutils .literal .notranslate}]{.pre} and more
like [`MPI_rPut`{.docutils .literal .notranslate}]{.pre}. Do not assume
the data pointer is usable after a [`Put`{.docutils .literal
.notranslate}]{.pre} and [`Get`{.docutils .literal .notranslate}]{.pre},
before [`EndStep`{.docutils .literal .notranslate}]{.pre},
[`Close`{.docutils .literal .notranslate}]{.pre} or the corresponding
[`PerformPuts`{.docutils .literal
.notranslate}]{.pre}/[`PerformGets`{.docutils .literal
.notranslate}]{.pre}. Avoid using temporaries, r-values, and
out-of-scope variables in [`Deferred`{.docutils .literal
.notranslate}]{.pre} mode. Use [`adios2::Mode::Sync`{.docutils .literal
.notranslate}]{.pre} in these cases.
:::
:::::::

::: {#available-engines .section}
#### Available Engines[](#available-engines "Link to this heading"){.headerlink}

A particular engine is set within the [`IO`{.docutils .literal
.notranslate}]{.pre} object that creates it with the
[`IO::SetEngine`{.docutils .literal .notranslate}]{.pre} function in a
case insensitive manner. If the [`SetEngine`{.docutils .literal
.notranslate}]{.pre} function is not invoked the default engine is the
[`BPFile`{.docutils .literal .notranslate}]{.pre}.

+-----------------------+-----------------------+-----------------------+
| Application           | Engine                | Description           |
+-----------------------+-----------------------+-----------------------+
| File                  | BP5                   | DEFAULT write/read    |
|                       |                       | ADIOS2 native bp      |
|                       | HDF5                  | files                 |
|                       |                       |                       |
|                       |                       | write/read            |
|                       |                       | interoperability with |
|                       |                       | HDF5 files            |
+-----------------------+-----------------------+-----------------------+
| Wide-Area-Network     | DataMan               | write/read TCP/IP     |
| (WAN)                 |                       | streams               |
+-----------------------+-----------------------+-----------------------+
| Staging               | SST                   | write/read to a       |
|                       |                       | "staging" area:       |
|                       |                       | *e.g.* RDMA           |
+-----------------------+-----------------------+-----------------------+

[`Engine`{.docutils .literal .notranslate}]{.pre} polymorphism has two
goals:

1.  Each [`Engine`{.docutils .literal .notranslate}]{.pre} implements an
    orthogonal IO scenario targeting a use case (e.g. Files, WAN, InSitu
    MPI, etc) using a simple, unified API.

2\. Allow developers to build their own custom system solution based on
their particular requirements in the own playground space. Reusable
toolkit objects are available inside ADIOS2 for common tasks: bp
buffering, transport management, transports, etc.

A class that extends [`Engine`{.docutils .literal .notranslate}]{.pre}
must be thought of as a solution to a range of IO applications. Each
engine must provide a list of supported parameters, set in the IO object
creating this engine using [`IO::SetParameters`{.docutils .literal
.notranslate}]{.pre}, and supported transports (and their parameters) in
[`IO::AddTransport`{.docutils .literal .notranslate}]{.pre}. Each
Engine's particular options are documented in [[Supported Engines]{.std
.std-ref}](#document-engines/engines#supported-engines){.reference
.internal}.
:::
::::::::::::::::::::::::::::

:::::::: {#operator .section}
### Operator[](#operator "Link to this heading"){.headerlink}

The Operator abstraction allows ADIOS2 to act upon the user application
data, either from a [`adios2::Variable`{.docutils .literal
.notranslate}]{.pre} or a set of Variables in an [`adios2::IO`{.docutils
.literal .notranslate}]{.pre} object. Current supported operations are:

1.  Data compression/decompression, lossy and lossless.

2.  Callback functions (C++11 bindings only) supported by specific
    engines

ADIOS2 enables the use of third-party libraries to execute these tasks.

Operators can be attached onto a variable in two modes: private or
shared. In most situations, it is recommended to add an operator as a
private one, which means it is owned by a certain variable. A simple
example code is as follows.

:::: {.highlight-c++ .notranslate}
::: highlight
    #include <vector>
    #include <adios2.h>
    int main(int argc, char *argv[])
    {
        std::vector<double> myData = {
            0.0001, 1.0001, 2.0001, 3.0001, 4.0001, 5.0001, 6.0001, 7.0001, 8.0001, 9.0001,
            1.0001, 2.0001, 3.0001, 4.0001, 5.0001, 6.0001, 7.0001, 8.0001, 9.0001, 8.0001,
            2.0001, 3.0001, 4.0001, 5.0001, 6.0001, 7.0001, 8.0001, 9.0001, 8.0001, 7.0001,
            3.0001, 4.0001, 5.0001, 6.0001, 7.0001, 8.0001, 9.0001, 8.0001, 7.0001, 6.0001,
            4.0001, 5.0001, 6.0001, 7.0001, 8.0001, 9.0001, 8.0001, 7.0001, 6.0001, 5.0001,
            5.0001, 6.0001, 7.0001, 8.0001, 9.0001, 8.0001, 7.0001, 6.0001, 5.0001, 4.0001,
            6.0001, 7.0001, 8.0001, 9.0001, 8.0001, 7.0001, 6.0001, 5.0001, 4.0001, 3.0001,
            7.0001, 8.0001, 9.0001, 8.0001, 7.0001, 6.0001, 5.0001, 4.0001, 3.0001, 2.0001,
            8.0001, 9.0001, 8.0001, 7.0001, 6.0001, 5.0001, 4.0001, 3.0001, 2.0001, 1.0001,
            9.0001, 8.0001, 7.0001, 6.0001, 5.0001, 4.0001, 3.0001, 2.0001, 1.0001, 0.0001,
        };
        adios2::ADIOS adios;
        auto io = adios.DeclareIO("TestIO");
        auto varDouble = io.DefineVariable<double>("varDouble", {10,10}, {0,0}, {10,10}, adios2::ConstantDims);

        // add operator
        varDouble.AddOperation("mgard",{{"accuracy","0.01"}});
        // end add operator

        auto engine = io.Open("hello.bp", adios2::Mode::Write);
        engine.Put<double>(varDouble, myData.data());
        engine.Close();
        return 0;
    }
:::
::::

For users who need to attach a single operator onto multiple variables,
a shared operator can be defined using the adios2::ADIOS object, and
then attached to multiple variables using the reference to the operator
object. Note that in this mode, all variables sharing this operator will
also share the same configuration map. It should be only used when a
number of variables need *exactly* the same operation. In real world use
cases this is rarely seen, so please use this mode with caution.

:::: {.highlight-c++ .notranslate}
::: highlight
    #include <vector>
    #include <adios2.h>
    int main(int argc, char *argv[])
    {
        std::vector<double> myData = {
            0.0001, 1.0001, 2.0001, 3.0001, 4.0001, 5.0001, 6.0001, 7.0001, 8.0001, 9.0001,
            1.0001, 2.0001, 3.0001, 4.0001, 5.0001, 6.0001, 7.0001, 8.0001, 9.0001, 8.0001,
            2.0001, 3.0001, 4.0001, 5.0001, 6.0001, 7.0001, 8.0001, 9.0001, 8.0001, 7.0001,
            3.0001, 4.0001, 5.0001, 6.0001, 7.0001, 8.0001, 9.0001, 8.0001, 7.0001, 6.0001,
            4.0001, 5.0001, 6.0001, 7.0001, 8.0001, 9.0001, 8.0001, 7.0001, 6.0001, 5.0001,
            5.0001, 6.0001, 7.0001, 8.0001, 9.0001, 8.0001, 7.0001, 6.0001, 5.0001, 4.0001,
            6.0001, 7.0001, 8.0001, 9.0001, 8.0001, 7.0001, 6.0001, 5.0001, 4.0001, 3.0001,
            7.0001, 8.0001, 9.0001, 8.0001, 7.0001, 6.0001, 5.0001, 4.0001, 3.0001, 2.0001,
            8.0001, 9.0001, 8.0001, 7.0001, 6.0001, 5.0001, 4.0001, 3.0001, 2.0001, 1.0001,
            9.0001, 8.0001, 7.0001, 6.0001, 5.0001, 4.0001, 3.0001, 2.0001, 1.0001, 0.0001,
        };
        adios2::ADIOS adios;
        auto io = adios.DeclareIO("TestIO");
        auto varDouble = io.DefineVariable<double>("varDouble", {10,10}, {0,0}, {10,10}, adios2::ConstantDims);

        // define operator
        auto op = adios.DefineOperator("SharedCompressor","mgard",{{"accuracy","0.01"}});
        // add operator
        varDouble.AddOperation(op);
        // end add operator

        auto engine = io.Open("hello.bp", adios2::Mode::Write);
        engine.Put<double>(varDouble, myData.data());
        engine.Close();
        return 0;
    }
:::
::::

::: {.admonition .warning}
Warning

Make sure your ADIOS2 library installation used for writing and reading
was linked with a compatible version of a third-party dependency when
working with operators. ADIOS2 will issue an exception if an operator
library dependency is missing.
:::
::::::::

:::::::::::: {#runtime-configuration-files .section}
### Runtime Configuration Files[](#runtime-configuration-files "Link to this heading"){.headerlink}

ADIOS2 supports passing an optional runtime configuration file to the
[[ADIOS]{.std .std-ref}](#adios){.reference .internal} component
constructor ([`adios2_init`{.docutils .literal .notranslate}]{.pre} in
C, Fortran).

This file contains key-value pairs equivalent to the compile time
[`IO::SetParameters`{.docutils .literal .notranslate}]{.pre}
([`adios2_set_parameter`{.docutils .literal .notranslate}]{.pre} in C,
Fortran), and [`IO::AddTransport`{.docutils .literal
.notranslate}]{.pre} ([`adios2_set_transport_parameter`{.docutils
.literal .notranslate}]{.pre} in C, Fortran).

Each [`Engine`{.docutils .literal .notranslate}]{.pre} and
[`Operator`{.docutils .literal .notranslate}]{.pre} must provide a set
of available parameters as described in the [[Supported Engines]{.std
.std-ref}](#document-engines/engines#supported-engines){.reference
.internal} section. Prior to version v2.6.0 only XML is supported;
v2.6.0 and later support both XML and YAML.

::: {.admonition .warning}
Warning

Configuration files must have the corresponding format extension
[`.xml`{.docutils .literal .notranslate}]{.pre}, [`.yaml`{.docutils
.literal .notranslate}]{.pre}: [`config.xml`{.docutils .literal
.notranslate}]{.pre}, [`config.yaml`{.docutils .literal
.notranslate}]{.pre}, etc.
:::

::::: {#xml .section}
#### XML[](#xml "Link to this heading"){.headerlink}

:::: {.highlight-xml .notranslate}
::: highlight
    <?xml version="1.0"?>
    <adios-config>
      <io name="IONAME_1">

        <engine type="ENGINE_TYPE">

          <!-- Equivalent to IO::SetParameters-->
          <parameter key="KEY_1" value="VALUE_1"/>
          <parameter key="KEY_2" value="VALUE_2"/>
          <!-- ... -->
          <parameter key="KEY_N" value="VALUE_N"/>

        </engine>

        <!-- Equivalent to IO::AddTransport -->
        <transport type="TRANSPORT_TYPE">
          <!-- Equivalent to IO::SetParameters-->
          <parameter key="KEY_1" value="VALUE_1"/>
          <parameter key="KEY_2" value="VALUE_2"/>
          <!-- ... -->
          <parameter key="KEY_N" value="VALUE_N"/>
        </transport>
      </io>

      <io name="IONAME_2">
        <!-- ... -->
      </io>
    </adios-config>
:::
::::
:::::

::::::: {#yaml .section}
#### YAML[](#yaml "Link to this heading"){.headerlink}

Starting with v2.6.0, ADIOS supports YAML configuration files. The
syntax follows strict use of the YAML node keywords mapping to the
ADIOS2 components hierarchy. If a keyword is unknown ADIOS2 simply
ignores it. For an example file refer to [adios2 config file example in
our
repo.](https://github.com/ornladios/ADIOS2/tree/master/testing/adios2/yaml/proto.yaml){.reference
.external}

:::: {.highlight-yaml .notranslate}
::: highlight
    ---
    # adios2 config.yaml
    # IO YAML Sequence (-) Nodes to allow for multiple IO nodes
    # IO name referred in code with DeclareIO is mandatory

    - IO: "IOName"

      Engine:
         # If Type is missing or commented out, default Engine is picked up
         Type: "BP5"
         # optional engine parameters
         key1: value1
         key2: value2
         key3: value3

      Variables:

          # Variable Name is Mandatory
        - Variable: "VariableName1"
          Operations:
              # Operation Type is mandatory (zfp, sz, etc.)
            - Type: operatorType
              key1: value1
              key2: value2

        - Variable: "VariableName2"
          Operations:
              # Operations sequence of maps
            - {Type: operatorType, key1: value1}
            - {Type: z-checker, key1: value1, key2: value2}

      Transports:
          # Transport sequence of maps
        - {Type: file, Library: fstream}
        - {Type: rdma, Library: ibverbs}

      ...
:::
::::

::: {.admonition .caution}
Caution

YAML is case sensitive, make sure the node identifiers follow strictly
the keywords: IO, Engine, Variables, Variable, Operations, Transports,
Type.
:::

::: {.admonition .tip}
Tip

Run a YAML validator or use a YAML editor to make sure the provided file
is YAML compatible.
:::
:::::::
::::::::::::

::::::::::::::: {#anatomy-of-an-adios-program .section}
[]{#sec-basics-interface-components-anatomy}

### Anatomy of an ADIOS Program[](#anatomy-of-an-adios-program "Link to this heading"){.headerlink}

:::::: {#anatomy-of-an-adios-output .section}
#### Anatomy of an ADIOS Output[](#anatomy-of-an-adios-output "Link to this heading"){.headerlink}

:::: {.highlight-C++ .notranslate}
::: highlight
    ADIOS adios("config.xml", MPI_COMM_WORLD);
    |
    |   IO io = adios.DeclareIO(...);
    |   |
    |   |   Variable<...> var = io.DefineVariable<...>(...)
    |   |   Attribute<...> attr = io.DefineAttribute<...>(...)
    |   |   Engine e = io.Open("OutputFileName.bp", adios2::Mode::Write);
    |   |   |
    |   |   |   e.BeginStep()
    |   |   |   |
    |   |   |   |   e.Put(var, datapointer);
    |   |   |   |
    |   |   |   e.EndStep()
    |   |   |
    |   |   e.Close();
    |   |
    |   |--> IO goes out of scope
    |
    |--> ADIOS goes out of scope or adios2_finalize()
:::
::::

The pseudo code above depicts the basic structure of performing output.
The [`ADIOS`{.docutils .literal .notranslate}]{.pre} object is necessary
to hold all other objects. It is initialized with an MPI communicator in
a parallel program or without in a serial program. Additionally, a
config file (XML or YAML format) can be specified here to load runtime
configuration. Only one ADIOS object is needed throughout the entire
application but you can create as many as you want (e.g. if you need to
separate IO objects using the same name in a program that reads similar
input from an ensemble of multiple applications).

The [`IO`{.docutils .literal .notranslate}]{.pre} object is required to
hold the variable and attribute definitions, and runtime options for a
particular input or output stream. The IO object has a name, which is
used only to refer to runtime options in the configuration file. One IO
object can only be used in one output or input stream. The only
exception where an IO object can be used twice is one input stream plus
one output stream where the output is reusing the variable definitions
loaded during input.

[`Variable`{.docutils .literal .notranslate}]{.pre} and
[`Attribute`{.docutils .literal .notranslate}]{.pre} definitions belong
to one IO object, which means, they can only be used in one output. You
need to define new ones for other outputs. Just because a Variable is
defined, it will not appear in the output unless an associated Put()
call provides the content.

A stream is opened and closed once. The [`Engine`{.docutils .literal
.notranslate}]{.pre} object implements the data movement for the stream.
It depends on the runtime options of the IO object that what type of an
engine is created in the Open() call. One output step is denoted by a
pair of BeginStep..EndStep block.

An output step consist of variables and attributes. Variables are just
definitions without content, so one must call a Put() function to
provide the application data pointer that contains the data content one
wants to write out. Attributes have their content in their definitions
so there is no need for an extra call.

Some rules:

- Variables can be defined any time, before the corresponding Put() call

- Attributes can be defined any time before EndStep

- The following functions must be treated as Collective operations

> <div>
>
> - ADIOS
>
> - Open
>
> - BeginStep
>
> - EndStep
>
> - Close
>
> </div>

::: {.admonition .note}
Note

If there is only one output step, and we only want to write it to a file
on disk, never stream it to other application, then BeginStep and
EndStep are not required but it does not make any difference if they are
called.
:::
::::::

::::: {#anatomy-of-an-adios-input .section}
#### Anatomy of an ADIOS Input[](#anatomy-of-an-adios-input "Link to this heading"){.headerlink}

:::: {.highlight-C++ .notranslate}
::: highlight
    ADIOS adios("config.xml", MPI_COMM_WORLD);
    |
    |   IO io = adios.DeclareIO(...);
    |   |
    |   |   Engine e = io.Open("InputFileName.bp", adios2::Mode::Read);
    |   |   |
    |   |   |   e.BeginStep()
    |   |   |   |
    |   |   |   |   varlist = io.AvailableVariables(...)
    |   |   |   |   Variable var = io.InquireVariable(...)
    |   |   |   |   Attribute attr = io.InquireAttribute(...)
    |   |   |   |   |
    |   |   |   |   |   e.Get(var, datapointer);
    |   |   |   |   |
    |   |   |   |
    |   |   |   e.EndStep()
    |   |   |
    |   |   e.Close();
    |   |
    |   |--> IO goes out of scope
    |
    |--> ADIOS goes out of scope or adios2_finalize()
:::
::::

The difference between input and output is that while we have to define
the variables and attributes for an output, we have to retrieve the
available variables in an input first as definitions (Variable and
Attribute objects).

If we know the particular variable (name and type) in the input stream,
we can get the definition using InquireVariable(). Generic tools that
process any input must use other functions to retrieve the list of
variable names and their types first and then get the individual
Variable objects. The same is true for Attributes.
:::::

::::::: {#anatomy-of-an-adios-file-only-input .section}
#### Anatomy of an ADIOS File-only Input[](#anatomy-of-an-adios-file-only-input "Link to this heading"){.headerlink}

Previously we explored how to read using the input mode
adios2::Mode::Read. Nonetheless, ADIOS has another input mode named
adios2::Mode::ReadRandomAccess. adios2::Mode::Read mode allows data
access only timestep by timestep using BeginStep/EndStep, but generally
it is more memory efficient as ADIOS is only required to load metadata
for the current timestep. ReadRandomAccess can only be used with file
engines and involves loading all the file metadata at once. So it can be
more memory intensive than adios2::Mode::Read mode, but allows reading
data from any timestep using SetStepSelection(). If you use
adios2::Mode::ReadRandomAccess mode, be sure to allocate enough memory
to hold multiple steps of the variable content. Note that ADIOS
streaming engines (like SST, DataMan, etc.) do not support
ReadRandomAccess mode. Also newer file Engines like BP5 to not allow
BeginStep/EndStep calls in ReadRandomAccess mode.

:::: {.highlight-C++ .notranslate}
::: highlight
    ADIOS adios("config.xml", MPI_COMM_WORLD);
    |
    |   IO io = adios.DeclareIO(...);
    |   |
    |   |   Engine e = io.Open("InputFileName.bp", adios2::Mode::ReadRandomAccess);
    |   |   |
    |   |   |   Variable var = io.InquireVariable(...)
    |   |   |   |   var.SetStepSelection()
    |   |   |   |   e.Get(var, datapointer);
    |   |   |   |
    |   |   |
    |   |   e.Close();
    |   |
    |   |--> IO goes out of scope
    |
    |--> ADIOS goes out of scope or adios2_finalize()
:::
::::

Previously we explored how to read using the input mode
adios2::Mode::Read. Nonetheless, ADIOS has another input mode named
adios2::Mode::ReadRandomAccess. adios2::Mode::Read mode allows data
access only timestep by timestep using BeginStep/EndStep, but generally
it is more memory efficient as ADIOS is only required to load metadata
for the current timestep. ReadRandomAccess can only be used with file
engines and involves loading all the file metadata at once. So it can be
more memory intensive than adios2::Mode::Read mode, but allows reading
data from any timestep using SetStepSelection(). If you use
adios2::Mode::ReadRandomAccess mode, be sure to allocate enough memory
to hold multiple steps of the variable content. Note that ADIOS
streaming engines (like SST, DataMan, etc.) do not support
ReadRandomAccess mode. Also newer file Engines like BP5 to not allow
BeginStep/EndStep calls in ReadRandomAccess mode.

:::: {.highlight-C++ .notranslate}
::: highlight
    ADIOS adios("config.xml", MPI_COMM_WORLD);
    |
    |   IO io = adios.DeclareIO(...);
    |   |
    |   |   Engine e = io.Open("InputFileName.bp", adios2::Mode::ReadRandomAccess);
    |   |   |
    |   |   |   Variable var = io.InquireVariable(...)
    |   |   |   |   var.SetStepSelection()
    |   |   |   |   e.Get(var, datapointer);
    |   |   |   |
    |   |   |
    |   |   e.Close();
    |   |
    |   |--> IO goes out of scope
    |
    |--> ADIOS goes out of scope or adios2_finalize()
:::
::::
:::::::
:::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

[]{#document-engines/virtual_engines}

:::: {#supported-virtual-engine-names .section}
## Supported Virtual Engine Names[](#supported-virtual-engine-names "Link to this heading"){.headerlink}

This section provides a description of the Virtual Engines that can be
used to set up an actual Engine with specific parameters. These virtual
names are used for beginner users to simplify the selection of an engine
and its parameters. The following I/O uses cases are supported by
virtual engine names:

1.  [`File`{.docutils .literal .notranslate}]{.pre}: File I/O (Default
    engine).

    This sets up the I/O for files. If the file name passed in Open()
    ends with ".bp", then the BP5 engine will be used starting in
    v2.9.0. If it ends with ".h5", the HDF5 engine will be used. For old
    .bp files (BP version 3 format), the BP3 engine will be used for
    reading (v2.4.0 and below).

2.  [`FileStream`{.docutils .literal .notranslate}]{.pre}: Online
    processing via files.

    This allows a Consumer to concurrently read the data while the
    Producer is writing new output steps into it. The Consumer will wait
    for the appearance of the file itself in Open() (for up to one hour)
    and wait for the appearance of new steps in the file (in BeginStep()
    up to the specificed timeout in that function).

3.  [`InSituAnalysis`{.docutils .literal .notranslate}]{.pre}: Streaming
    data to another application.

    This sets up ADIOS for transferring data from a Producer to a
    Consumer application. The Producer and Consumer are synchronized at
    Open(). The Consumer will receive every single output step from the
    Producer, therefore, the Producer will block on output if the
    Consumer is slow.

4.  [`InSituVisualization`{.docutils .literal .notranslate}]{.pre}::
    Streaming data to another application without waiting for
    consumption.

    This sets up ADIOS for transferring data from a Producer to a
    Consumer without ever blocking the Producer. The Producer will throw
    away all output steps that are not immediately requested by a
    Consumer. It will also not wait for a Consumer to connect. This kind
    of streaming is great for an interactive visualization session where
    the user wants to see the most current state of the application.

5.  [`CodeCoupling`{.docutils .literal .notranslate}]{.pre}:: Streaming
    data between two applications for code coupling.

    Producer and Consumer are waiting for each other in Open() and every
    step must be consumed. Currently, this is the same as in situ
    analysis.

These virtual engine names are used to select a specific engine and its
parameters. In practice, after selecting the virtual engine name, one
can modify the settings by adding/overwriting parameters. Eventually, a
seasoned user would use the actual Engine names and parameterize it for
the specific run.

::: {#virtual-engine-setups .section}
### Virtual Engine Setups[](#virtual-engine-setups "Link to this heading"){.headerlink}

These are the actual settings in ADIOS when a virtual engine is
selected. The parameters below can be modified before the Open call.

1.  [`File`{.docutils .literal .notranslate}]{.pre}. Refer to the
    parameter settings for these engines of [`BP5`{.docutils .literal
    .notranslate}]{.pre}, [`BP4`{.docutils .literal
    .notranslate}]{.pre}, [`BP3`{.docutils .literal .notranslate}]{.pre}
    and [`HDF5`{.docutils .literal .notranslate}]{.pre} engines earlier
    in this section.

2.  [`FileStream`{.docutils .literal .notranslate}]{.pre}. The engine is
    [`BP5`{.docutils .literal .notranslate}]{.pre}. The parameters are
    set to:

  **Key**                         **Value Format**   **Default** and Examples
  ------------------------------- ------------------ -----------------------------------------------------
  OpenTimeoutSecs                 float              **3600** (wait for up to an hour)
  BeginStepPollingFrequencySecs   float              **1** (poll the file system with 1 second frequency

3.  [`InSituAnalysis`{.docutils .literal .notranslate}]{.pre}. The
    engine is [`SST`{.docutils .literal .notranslate}]{.pre}. The
    parameters are set to:

  **Key**                       **Value Format**   **Default** and Examples
  ----------------------------- ------------------ -----------------------------------------------------
  RendezvousReaderCount         integer            **1** (Producer waits for the Consumer in Open)
  QueueLimit                    integer            **1** (only buffer one step)
  QueueFullPolicy               string             **Block** (wait for the Consumer to get every step)
  FirstTimestepPrecious         bool               false (SST default)
  AlwaysProvideLatestTimestep   bool               false (SST default)

4.  [`InSituVisualization`{.docutils .literal .notranslate}]{.pre}. The
    engine is [`SST`{.docutils .literal .notranslate}]{.pre}. The
    parameters are set to:

  **Key**                       **Value Format**   **Default** and Examples
  ----------------------------- ------------------ ---------------------------------------------------------
  RendezvousReaderCount         integer            **0** (Producer does NOT wait for Consumer in Open)
  QueueLimit                    integer            **3** (buffer first step + last two steps)
  QueueFullPolicy               string             **Discard** (slow Consumer will miss out on steps)
  FirstTimestepPrecious         bool               **true** (First step is kept around for late Consumers)
  AlwaysProvideLatestTimestep   bool               false (SST default)

5.  [`Code`{.docutils .literal .notranslate}]{.pre}` `{.docutils
    .literal .notranslate}[`Coupling`{.docutils .literal
    .notranslate}]{.pre}. The engine is [`SST`{.docutils .literal
    .notranslate}]{.pre}. The parameters are set to:

  **Key**                       **Value Format**   **Default** and Examples
  ----------------------------- ------------------ -----------------------------------------------------
  RendezvousReaderCount         integer            **1** (Producer waits for the Consumer in Open)
  QueueLimit                    integer            **1** (only buffer one step)
  QueueFullPolicy               string             **Block** (wait for the Consumer to get every step)
  FirstTimestepPrecious         bool               false (SST default)
  AlwaysProvideLatestTimestep   bool               false (SST default)
:::
::::

[]{#document-engines/engines}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#supported-engines .section}
## Supported Engines[](#supported-engines "Link to this heading"){.headerlink}

This section provides a description of the [[Available Engines]{.std
.std-ref}](#document-components/components#available-engines){.reference
.internal} in ADIOS2 and their specific parameters to allow
extra-control from the user. Parameters are passed in key-value pairs
for:

1.  Engine specific parameters

2.  Engine supported transports and parameters

Parameters are passed at:

1.  Compile time [`IO::SetParameters`{.docutils .literal
    .notranslate}]{.pre} ([`adios2_set_parameter`{.docutils .literal
    .notranslate}]{.pre} in C, Fortran)

2.  Compile time [`IO::AddTransport`{.docutils .literal
    .notranslate}]{.pre} ([`adios2_set_transport_parameter`{.docutils
    .literal .notranslate}]{.pre} in C, Fortran)

3.  [[Runtime Configuration Files]{.std
    .std-ref}](#document-components/components#runtime-configuration-files){.reference
    .internal} in the [[ADIOS]{.std
    .std-ref}](#document-components/components#adios){.reference
    .internal} component.

::::::::: {#bp5 .section}
### BP5[](#bp5 "Link to this heading"){.headerlink}

The BP5 Engine writes and reads files in ADIOS2 native binary-pack (bp
version 5) format. This was a new format for ADIOS 2.8, improving on the
metadata operations and the memory consumption of the older BP4/BP3
formats. BP5 is the default file format as of ADIOS 2.9. As compared to
the older format, BP5 provides three main advantages:

> <div>
>
> - **Lower memory** consumption. Deferred Puts will use user buffer for
>   I/O wherever possible thus saving on a memory copy. Aggregation uses
>   a fixed-size shared-memory segment on each compute node instead of
>   using MPI to send data from one process to another. Memory
>   consumption can get close to half of BP4 in some cases.
>
> - **Faster metadata** management improves write/read performance where
>   hundreds or more variables are added to the output.
>
> - Improved functionality around **appending** many output steps into
>   the same file. Better performance than writing new files each step.
>   Restart can append to an existing series by truncating unwanted
>   steps. Readers can filter out unwanted steps to only see and process
>   a limited set of steps. Just like as in BP4, existing steps cannot
>   be corrupted by appending new steps.
>
> </div>

In 2.8 BP5 was a brand new file format and engine. It still does **NOT**
support some functionality of BP4:

> <div>
>
> - **Burst buffer support** for writing data.
>
> </div>

BP5 files have the following structure given a "name" string passed as
the first argument of [`IO::Open`{.docutils .literal
.notranslate}]{.pre}:

:::: {.highlight-c++ .notranslate}
::: highlight
    io.SetEngine("BP5");
    adios2::Engine bpFile = io.Open("name", adios2::Mode::Write);
:::
::::

will generate:

:::: {.highlight-bash .notranslate}
::: highlight
    % BP5 datasets are always a directory
    name.bp/

    % data and metadata files
    name.bp/
            data.0
            data.1
            ...
            data.M
            md.0
            md.idx
            mmd.0
:::
::::

::: {.admonition .note}
Note

BP5 file names are compatible with the Unix ([`/`{.docutils .literal
.notranslate}]{.pre}) and Windows ([`\\`{.docutils .literal
.notranslate}]{.pre}) file system naming convention for directories and
files.
:::

::: {.admonition .note}
Note

BP5 has an [`mmd.0`{.docutils .literal .notranslate}]{.pre} file in the
directory, which BP4 does not have.
:::

This engine allows the user to fine tune the buffering operations
through the following optional parameters:

1.  Streaming through file

    1.  **OpenTimeoutSecs**: (Streaming mode) Reader may want to wait
        for the creation of the file in [`io.Open()`{.docutils .literal
        .notranslate}]{.pre}. By default the Open() function returns
        with an error if file is not found.

    2.  **BeginStepPollingFrequencySecs**: (Streaming mode) Reader can
        set how frequently to check the file (and file system) for new
        steps. Default is 1 seconds which may be stressful for the file
        system and unnecessary for the application.

2.  Aggregation

    1.  **AggregationType**: *TwoLevelShm*, *EveryoneWritesSerial* and
        *EveryoneWrites* are three data aggregation strategies. See
        [[Aggregation in BP5]{.std
        .std-ref}](#document-advanced/aggregation#aggregation-in-bp5){.reference
        .internal}. The default is *TwoLevelShm*.

    2.  **NumAggregators**: The number of processes that will ever write
        data directly to storage. The default is set to the number of
        compute nodes the application is running on (i.e. one process
        per compute node). TwoLevelShm will select a fixed number of
        processes *per compute-node* to get close to the intention of
        the user but does not guarantee the exact number of aggregators.

    3.  **AggregatorRatio**: An alternative option to NumAggregators to
        pick every nth process as aggregator. The number of aggregators
        will be automatically kept to be within 1 and total number of
        processes no matter what bad number is supplied here. Moreover,
        TwoLevelShm will select an fixed number of processes *per
        compute-node* to get close to the intention of this ratio but
        does not guarantee the exact number of aggregators.

    4.  **NumSubFiles**: The number of data files to write to in the
        *.bp/* directory. Only used by *TwoLevelShm* aggregator, where
        the number of files can be smaller then the number of
        aggregators. The default is set to *NumAggregators*.

    5.  **StripeSize**: The data blocks of different processes are
        aligned to this size (default is 4096 bytes) in the files. Its
        purpose is to avoid multiple processes to write to the same file
        system block and potentially slow down the write.

    6.  **MaxShmSize**: Upper limit for how much shared memory an
        aggregator process in *TwoLevelShm* can allocate. For optimum
        performance, this should be at least *2xM +1KB* where *M* is the
        maximum size any process writes in a single step. However, there
        is no point in allowing for more than 4GB. The default is 4GB.

    7.  **UseSelectiveMetadataAggregation**: There are two metadata
        aggregation strategies in BP5. If this parameter is true (the
        default), SelectiveMetadataAggregation is employed, which uses a
        multi-phase approach to limit the amount of data exchanged. If
        false, a less complex two-level metadata aggregation is
        performed. In most cases the default is more efficient.

    8.  **OneLevelGatherRankLimit**: For the
        SelectiveMetadataAggregation method, this parameter specifies an
        MPI cohort size above which it resorts to a two-stage
        aggregation process rather than gathering all metadata to rank 0
        in one MPI collective operation. Some HPC machines have
        unpredictable behaviour with gatherv at both large numbers of
        ranks and large amounts of data. The default value (6000) avoids
        this behaviour on ORNL's Frontier. Higher or lower values may be
        useful on other machines.

3.  Buffering

    1.  **BufferVType**: *chunk* or *malloc*, default is chunking.
        Chunking maintains the buffer as a list of memory blocks, either
        ADIOS-owned for sync-ed Puts and small Puts, and user-owned
        pointers of deferred Puts. Malloc maintains a single memory
        block and extends it (reallocates) whenever more data is
        buffered. Chunking incurs extra cost in I/O by having to write
        data in chunks (multiple write system calls), which can be
        helped by increasing *BufferChunkSize* and *MinDeferredSize*.
        Malloc incurs extra cost by reallocating memory whenever more
        data is buffered (by Put()), which can be helped by increasing
        *InitialBufferSize*.

    2.  **BufferChunkSize**: (for *chunk* buffer type) The size of each
        memory buffer chunk, default is 128MB but it is worth increasing
        up to 2147381248 (a bit less than 2GB) if possible for maximum
        write performance.

    3.  **MinDeferredSize**: (for *chunk* buffer type) Small user
        variables are always buffered, default is 4MB.

    4.  **InitialBufferSize**: (for *malloc* buffer type) initial memory
        provided for buffering (default and minimum is 16Kb). To avoid
        reallocations, it is worth increasing this size to the expected
        maximum total size of data any process would write in any step
        (not counting deferred Puts).

    5.  **GrowthFactor**: (for *malloc* buffer type) exponential growth
        factor for initial buffer \> 1, default = 1.05.

4.  Managing steps

    1.  **AppendAfterSteps**: BP5 enables overwriting some existing
        steps by opening in *adios2::Mode::Append* mode and specifying
        how many existing steps to keep. Default value is MAX_INT, so it
        always appends after the last step. -1 would achieve the same
        thing. If you have 10 steps in the file,

        - value 0 means starting from the beginning, truncating all
          existing data

        - value 1 means appending after the first step, so overwrite
          2,3...10

        - value 10 means appending after all existing steps

        - value \>10 means the same, append after all existing steps
          (gaps in steps are impossible)

        - -1 means appending after the last step, i.e. same as 10 or
          higher

        - -2 means removing the last step, i.e. starting from the 10th

        - -11 (and \<-11) means truncating all existing data

    2.  **SelectSteps**: BP5 reading allows for only seeing selected
        steps. This is a string of space-separated list of range
        definitions in the form of "start:end:step". Indexing starts
        from 0. If 'end' is 'n' or 'N', then it is an unlimited range
        expression. Range definitions are adding up. Note that in the
        reading functions, counting the steps is *always* *0* to *s-1*
        where *s* steps are presented, so even after applying this
        selection, the selected steps are presented as *0* to *s-1*.
        Examples:

        - "0 6 3 2" selects four steps indexed 0,2,3 and 6 (presented in
          reading as 0,1,2,3)

        - "1:5" selects 5 consecutive steps, skipping step 0, and
          starting from 1

        - "2:n" selects all steps from step 2

        - "0:n:2" selects every other steps from the beginning
          (0,2,4,6...)

        - "0:n:3 10:n:5" selects every third step from the beginning and
          additionally every fifth steps from step 10.

5.  Asynchronous writing I/O

    1.  **AsyncOpen**: *true/false* Call the open function
        asynchronously. It decreases I/O overhead when creating lots of
        subfiles (*NumAggregators* is large) and one calls *io.Open()*
        well ahead of the first write step. Only implemented for
        writing. Default is *true*.

    2.  **AsyncWrite**: *true/false* Perform data writing operations
        asynchronously after *EndStep()*. Default is *false*. If the
        application calls
        *EnterComputationBlock()/ExitComputationBlock()* to indicate
        phases where no communication is happening, ADIOS will try to
        perform all data writing during those phases, otherwise it will
        write immediately and eagerly after *EndStep()*.

6.  Direct I/O. Experimental, see discussion on
    [GitHub](https://github.com/ornladios/ADIOS2/issues/3029){.reference
    .external}.

    1.  **DirectIO**: Turn on O_DIRECT when using POSIX transport. Do
        not use this on parallel file systems.

    2.  **DirectIOAlignOffset**: Alignment for file offsets. Default is
        512 which is usually

    3.  **DirectIOAlignBuffer**: Alignment for memory pointers. Default
        is to be same as *DirectIOAlignOffset*.

7.  Miscellaneous

    1.  **StatsLevel**: 1 turns on *Min/Max* calculation for every
        variable, 0 turns this off. Default is 1. It has some cost to
        generate this metadata so it can be turned off if there is no
        need for this information.

    2.  **MaxOpenFilesAtOnce**: Specify how many subfiles a process can
        keep open at once. Default is unlimited. If a dataset contains
        more subfiles than how many open file descriptors the system
        allows (see *ulimit -n*) then one can either try to raise that
        system limit (set it with *ulimit -n*), or set this parameter to
        force the reader to close some subfiles to stay within the
        limits.

    3.  **Threads**: Read side: Specify how many threads one process can
        use to speed up reading. The default value is *0*, to let the
        engine estimate the number of threads based on how many
        processes are running on the compute node and how many hardware
        threads are available on the compute node but it will use
        maximum 16 threads. Value *1* forces the engine to read
        everything within the main thread of the process. Other values
        specify the exact number of threads the engine can use. Although
        multithreaded reading works in a single
        *Get(adios2::Mode::Sync)* call if the read selection spans
        multiple data blocks in the file, the best parallelization is
        achieved by using deferred mode and reading everything in
        *PerformGets()/EndStep()*.

    4.  **FlattenSteps**: This is a writer-side parameter specifies that
        the reader should interpret multiple writer-created timesteps as
        a single timestep, essentially flattening all Put()s into a
        single step.

    5.  **IgnoreFlattenSteps**: This is a reader-side parameter that
        tells the reader to ignore any FlattenSteps parameter supplied
        to the writer.

Only file transport types are supported. Optional parameters for
[`IO::AddTransport`{.docutils .literal .notranslate}]{.pre} or in
runtime config file transport field:

**Transport type: File**

  **Key**   **Value Format**   **Default** and Examples
  --------- ------------------ -----------------------------------------------------
  Library   string             **POSIX** (UNIX), **FStream** (Windows), stdio, IME

The IME transport directly reads and writes files stored on DDN's IME
burst buffer using the IME native API. To use the IME transport, IME
must be avaiable on the target system and ADIOS2 needs to be configured
with [`ADIOS2_USE_IME`{.docutils .literal .notranslate}]{.pre}. By
default, data written to the IME is automatically flushed to the
parallel filesystem at every [`EndStep()`{.docutils .literal
.notranslate}]{.pre} call. You can disable this automatic flush by
setting the transport parameter [`SyncToPFS`{.docutils .literal
.notranslate}]{.pre} to [`OFF`{.docutils .literal .notranslate}]{.pre}.
:::::::::

:::::::: {#bp4 .section}
### BP4[](#bp4 "Link to this heading"){.headerlink}

The BP4 Engine writes and reads files in ADIOS2 native binary-pack (bp
version 4) format. This was a new format for ADIOS 2.5 and improved on
the metadata operations of the older BP3 format. Compared to the older
format, BP4 provides three main advantages:

> <div>
>
> - Fast and safe **appending** of multiple output steps into the same
>   file. Better performance than writing new files each step. Existing
>   steps cannot be corrupted by appending new steps.
>
> - **Streaming** through files (i.e. online processing). Consumer apps
>   can read existing steps while the Producer is still writing new
>   steps. Reader's loop can block (with timeout) and wait for new steps
>   to arrive. Same reader code can read the entire data in post or in
>   situ. No restrictions on the Producer.
>
> - **Burst buffer support** for writing data. It can write the output
>   to a local file system on each compute node and drain the data to
>   the parallel file system in a separate asynchronous thread.
>   Streaming read from the target file system are still supported when
>   data goes through the burst buffer. Appending to an existing file on
>   the target file system is NOT supported currently.
>
> </div>

BP4 files have the following structure given a "name" string passed as
the first argument of [`IO::Open`{.docutils .literal
.notranslate}]{.pre}:

:::: {.highlight-c++ .notranslate}
::: highlight
    io.SetEngine("BP4");
    adios2::Engine bpFile = io.Open("name", adios2::Mode::Write);
:::
::::

will generate:

:::: {.highlight-bash .notranslate}
::: highlight
    % BP4 datasets are always a directory
    name.bp/

    % data and metadata files
    name.bp/
            data.0
            data.1
            ...
            data.M
            md.0
            md.idx
:::
::::

::: {.admonition .note}
Note

BP4 file names are compatible with the Unix ([`/`{.docutils .literal
.notranslate}]{.pre}) and Windows ([`\\`{.docutils .literal
.notranslate}]{.pre}) file system naming convention for directories and
files.
:::

This engine allows the user to fine tune the buffering operations
through the following optional parameters:

1.  **Profile**: turns ON/OFF profiling information right after a run

2.  **ProfileUnits**: set profile units according to the required
    measurement scale for intensive operations

3.  **Threads**: number of threads provided from the application for
    buffering, use this for very large variables in data size

4.  **InitialBufferSize**: initial memory provided for buffering
    (minimum is 16Kb)

5.  **BufferGrowthFactor**: exponential growth factor for initial buffer
    \> 1, default = 1.05.

6.  **MaxBufferSize**: maximum allowable buffer size (must be larger
    than 16Kb). If too large adios2 will throw an exception.

7.  **FlushStepsCount**: users can select how often to produce the more
    expensive collective metadata file in terms of steps: default is 1.
    Increase to reduce adios2 collective operations footprint, with the
    trade-off of reducing checkpoint frequency. Buffer size will
    increase until first steps count if [`MaxBufferSize`{.docutils
    .literal .notranslate}]{.pre} is not set.

8.  **NumAggregators** (or **SubStreams**): Users can select how many
    sub-files ([`M`{.docutils .literal .notranslate}]{.pre}) are
    produced during a run, ranges between 1 and the number of mpi
    processes from [`MPI_Size`{.docutils .literal .notranslate}]{.pre}
    ([`N`{.docutils .literal .notranslate}]{.pre}), adios2 will
    internally aggregate data buffers ([`N-to-M`{.docutils .literal
    .notranslate}]{.pre}) to output the required number of sub-files.
    Default is 0, which will let adios2 to group processes per
    shared-memory-access (i.e. one per compute node) and use one process
    per node as an aggregator. If NumAggregators is larger than the
    number of processes then it will be set to the number of processes.

9.  **AggregatorRatio**: An alternative option to NumAggregators to pick
    every Nth process as aggregator. An integer divider of the number of
    processes is required, otherwise a runtime exception is thrown.

10. **OpenTimeoutSecs**: (Streaming mode) Reader may want to wait for
    the creation of the file in [`io.Open()`{.docutils .literal
    .notranslate}]{.pre}. By default the Open() function returns with an
    error if file is not found.

11. **BeginStepPollingFrequencySecs**: (Streaming mode) Reader can set
    how frequently to check the file (and file system) for new steps.
    Default is 1 seconds which may be stressful for the file system and
    unnecessary for the application.

12. **StatsLevel**: Turn on/off calculating statistics for every
    variable (Min/Max). Default is On. It has some cost to generate this
    metadata so it can be turned off if there is no need for this
    information.

13. **StatsBlockSize**: Calculate Min/Max for a given size of each
    process output. Default is one Min/Max per writer. More fine-grained
    min/max can be useful for querying the data.

14. **NodeLocal** or **Node-Local**: For distributed file system. Every
    writer process must make sure the .bp/ directory is created on the
    local file system. Required when writing to local disk/SSD/NVMe in a
    cluster. Note: the BurstBuffer\* parameters are newer and should be
    used for using the local storage as temporary instead of this
    parameter.

15. **BurstBufferPath**: Redirect output file to another location and
    drain it to the original target location in an asynchronous thread.
    It requires to be able to launch one thread per aggregator (see
    SubStreams) on the system. This feature can be used on machines that
    have local NVMe/SSDs on each node to accelerate the output writing
    speed. On Summit at OLCF, use "/mnt/bb/\<username\>" for the path
    where \<username\> is your user account name. Temporary files on the
    accelerated storage will be automatically deleted after the
    application closes the output and ADIOS drains all data to the file
    system, unless draining is turned off (see the next parameter).
    Note: at this time, this feature cannot be used to append data to an
    existing dataset on the target system.

16. **BurstBufferDrain**: To write only to the accelerated storage but
    to not drain it to the target file system, set this flag to false.
    Data will NOT be deleted from the accelerated storage on close. By
    default, setting the BurstBufferPath will turn on draining.

17. **BurstBufferVerbose**: Verbose level 1 will cause each draining
    thread to print a one line report at the end (to standard output)
    about where it has spent its time and the number of bytes moved.
    Verbose level 2 will cause each thread to print a line for each
    draining operation (file creation, copy block, write block from
    memory, etc).

18. **StreamReader**: By default the BP4 engine parses all available
    metadata in Open(). An application may turn this flag on to parse a
    limited number of steps at once, and update metadata when those
    steps have been processed. If the flag is ON, reading only works in
    streaming mode (using BeginStep/EndStep); file reading mode will not
    work as there will be zero steps processed in Open().

  **Key**                         **Value Format**       **Default** and Examples
  ------------------------------- ---------------------- ---------------------------------------------------------------------------------------------------------------
  Profile                         string On/Off          **On**, Off
  ProfileUnits                    string                 **Microseconds**, Milliseconds, Seconds, Minutes, Hours
  Threads                         integer \> 1           **1**, 2, 3, 4, 16, 32, 64
  InitialBufferSize               float+units \>= 16Kb   **16Kb**, 10Mb, 0.5Gb
  MaxBufferSize                   float+units \>= 16Kb   **at EndStep**, 10Mb, 0.5Gb
  BufferGrowthFactor              float \> 1             **1.05**, 1.01, 1.5, 2
  FlushStepsCount                 integer \> 1           **1**, 5, 1000, 50000
  NumAggregators                  integer \>= 1          **0 (one file per compute node)**, [`MPI_Size`{.docutils .literal .notranslate}]{.pre}/2, ... , 2, (N-to-1) 1
  AggregatorRatio                 integer \>= 1          not used unless set, [`MPI_Size`{.docutils .literal .notranslate}]{.pre}/N must be an integer value
  OpenTimeoutSecs                 float                  **0**, [`10.0`{.docutils .literal .notranslate}]{.pre}, [`5`{.docutils .literal .notranslate}]{.pre}
  BeginStepPollingFrequencySecs   float                  **1**, [`10.0`{.docutils .literal .notranslate}]{.pre}
  StatsLevel                      integer, 0 or 1        **1**, [`0`{.docutils .literal .notranslate}]{.pre}
  StatsBlockSize                  integer \> 0           **a very big number**, [`1073741824`{.docutils .literal .notranslate}]{.pre} for blocks with 1M elements
  NodeLocal                       string On/Off          **Off**, On
  Node-Local                      string On/Off          **Off**, On
  BurstBufferPath                 string                 **""**, /mnt/bb/norbert, /ssd
  BurstBufferDrain                string On/Off          **On**, Off
  BurstBufferVerbose              integer, 0-2           **0**, [`1`{.docutils .literal .notranslate}]{.pre}, [`2`{.docutils .literal .notranslate}]{.pre}
  StreamReader                    string On/Off          On, **Off**

Only file transport types are supported. Optional parameters for
[`IO::AddTransport`{.docutils .literal .notranslate}]{.pre} or in
runtime config file transport field:

**Transport type: File**

  **Key**   **Value Format**   **Default** and Examples
  --------- ------------------ -----------------------------------------------------
  Library   string             **POSIX** (UNIX), **FStream** (Windows), stdio, IME

The IME transport directly reads and writes files stored on DDN's IME
burst buffer using the IME native API. To use the IME transport, IME
must be avaiable on the target system and ADIOS2 needs to be configured
with [`ADIOS2_USE_IME`{.docutils .literal .notranslate}]{.pre}. By
default, data written to the IME is automatically flushed to the
parallel filesystem at every [`EndStep()`{.docutils .literal
.notranslate}]{.pre} call. You can disable this automatic flush by
setting the transport parameter [`SyncToPFS`{.docutils .literal
.notranslate}]{.pre} to [`OFF`{.docutils .literal .notranslate}]{.pre}.
::::::::

::::::::: {#bp3 .section}
### BP3[](#bp3 "Link to this heading"){.headerlink}

The BP3 Engine writes and reads files in ADIOS2 native binary-pack (bp)
format. BP files are backwards compatible with ADIOS1.x and have the
following structure given a "name" string passed as the first argument
of [`IO::Open`{.docutils .literal .notranslate}]{.pre}:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::Engine bpFile = io.Open("name", adios2::Mode::Write);
:::
::::

will generate:

:::: {.highlight-bash .notranslate}
::: highlight
    % collective metadata file
    name.bp

    % data directory and files
    name.bp.dir/
                name.bp.0
                name.bp.1
                ...
                name.bp.M
:::
::::

::: {.admonition .note}
Note

BP3 file names are compatible with the Unix ([`/`{.docutils .literal
.notranslate}]{.pre}) and Windows ([`\\`{.docutils .literal
.notranslate}]{.pre}) file system naming convention for directories and
files.
:::

::: {.admonition .caution}
Caution

The default BP3 engine will check if the [`.bp`{.docutils .literal
.notranslate}]{.pre} is the extension of the first argument of
[`IO::Open`{.docutils .literal .notranslate}]{.pre} and will add
[`.bp`{.docutils .literal .notranslate}]{.pre} and [`.bp.dir`{.docutils
.literal .notranslate}]{.pre} if not.
:::

This engine allows the user to fine tune the buffering operations
through the following optional parameters:

1.  **Profile**: turns ON/OFF profiling information right after a run

2.  **ProfileUnits**: set profile units according to the required
    measurement scale for intensive operations

3.  **CollectiveMetadata**: turns ON/OFF forming collective metadata
    during run (used by large scale HPC applications)

4.  **Threads**: number of threads provided from the application for
    buffering, use this for very large variables in data size

5.  **InitialBufferSize**: initial memory provided for buffering
    (minimum is 16Kb)

6.  **BufferGrowthFactor**: exponential growth factor for initial buffer
    \> 1, default = 1.05.

7.  **MaxBufferSize**: maximum allowable buffer size (must be larger
    than 16Kb). If too large adios2 will throw an exception.

8.  **FlushStepsCount**: users can select how often to produce the more
    expensive collective metadata file in terms of steps: default is 1.
    Increase to reduce adios2 collective operations footprint, with the
    trade-off of reducing checkpoint frequency. Buffer size will
    increase until first steps count if [`MaxBufferSize`{.docutils
    .literal .notranslate}]{.pre} is not set.

9.  **NumAggregators** (or **SubStreams**): Users can select how many
    sub-files ([`M`{.docutils .literal .notranslate}]{.pre}) are
    produced during a run, ranges between 1 and the number of mpi
    processes from [`MPI_Size`{.docutils .literal .notranslate}]{.pre}
    ([`N`{.docutils .literal .notranslate}]{.pre}), adios2 will
    internally aggregate data buffers ([`N-to-M`{.docutils .literal
    .notranslate}]{.pre}) to output the required number of sub-files.
    Default is 0, which will let adios2 to group processes per
    shared-memory-access (i.e. one per compute node) and use one process
    per node as an aggregator. If NumAggregators is larger than the
    number of processes then it will be set to the number of processes.

10. **AggregatorRatio**: An alternative option to NumAggregators to pick
    every Nth process as aggregator. An integer divider of the number of
    processes is required, otherwise a runtime exception is thrown.

11. **Node-Local**: For distributed file system. Every writer process
    must make sure the .bp/ directory is created on the local file
    system. Required for using local disk/SSD/NVMe in a cluster.

  **Key**              **Value Format**       **Default** and Examples
  -------------------- ---------------------- ---------------------------------------------------------------------------------------------------------------
  Profile              string On/Off          **On**, Off
  ProfileUnits         string                 **Microseconds**, Milliseconds, Seconds, Minutes, Hours
  CollectiveMetadata   string On/Off          **On**, Off
  Threads              integer \> 1           **1**, 2, 3, 4, 16, 32, 64
  InitialBufferSize    float+units \>= 16Kb   **16Kb**, 10Mb, 0.5Gb
  MaxBufferSize        float+units \>= 16Kb   **at EndStep**, 10Mb, 0.5Gb
  BufferGrowthFactor   float \> 1             **1.05**, 1.01, 1.5, 2
  FlushStepsCount      integer \> 1           **1**, 5, 1000, 50000
  NumAggregators       integer \>= 1          **0 (one file per compute node)**, [`MPI_Size`{.docutils .literal .notranslate}]{.pre}/2, ... , 2, (N-to-1) 1
  AggregatorRatio      integer \>= 1          not used unless set, [`MPI_Size`{.docutils .literal .notranslate}]{.pre}/N must be an integer value
  Node-Local           string On/Off          **Off**, On

Only file transport types are supported. Optional parameters for
[`IO::AddTransport`{.docutils .literal .notranslate}]{.pre} or in
runtime config file transport field:

**Transport type: File**

  **Key**   **Value Format**   **Default** and Examples
  --------- ------------------ -----------------------------------------------------
  Library   string             **POSIX** (UNIX), **FStream** (Windows), stdio, IME
:::::::::

::::::::: {#hdf5 .section}
### HDF5[](#hdf5 "Link to this heading"){.headerlink}

In ADIOS2, the default engine for reading and writing HDF5 files is
called *"HDF5"*. To use this engine, you can either specify it in your
xml config file, with tag [`<engine`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`type=HDF5>`{.docutils .literal .notranslate}]{.pre} or,
set it in client code. For example, here is how to create a hdf5 reader:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::IO h5IO = adios.DeclareIO("SomeName");
    h5IO.SetEngine("HDF5");
    adios2::Engine h5Reader = h5IO.Open(filename, adios2::Mode::Read);
:::
::::

To read back the h5 files generated with VDS to ADIOS2, one can use the
HDF5 engine. Please make sure you are using the HDF5 library that has
version greater than or equal to 1.11 in ADIOS2.

The h5 file generated by ADIOS2 has two levels of groups: The top Group,
[`/`{.docutils .literal .notranslate}]{.pre} and its subgroups:
[`Step0`{.docutils .literal .notranslate}]{.pre} ... [`StepN`{.docutils
.literal .notranslate}]{.pre}, where [`N`{.docutils .literal
.notranslate}]{.pre} is number of steps. All datasets belong to the
subgroups.

Any other h5 file can be read back to ADIOS as well. To be consistent,
when reading back to ADIOS2, we assume a default Step0, and all datasets
from the original h5 file belong to that subgroup. The full path of a
dataset (from the original h5 file) is used when represented in ADIOS2.

We can pass options to HDF5 API from ADIOS xml configuration. Currently
we support CollectionIO (default false), and chunk specifications. The
chunk specification uses space to seperate values, and by default, if a
valid H5ChunkDim exists, it applies to all variables, unless H5ChunkVar
is specified. Examples:

:::: {.highlight-xml .notranslate}
::: highlight
    <parameter key="H5CollectiveMPIO" value="yes"/>
    <parameter key="H5ChunkDim" value="200 200"/>
    <parameter key="H5ChunkVar" value="VarName1 VarName2"/>
:::
::::

We suggest to read HDF5 documentation before appling these options.

After the subfile feature is introduced in HDF5 version 1.14, the ADIOS2
HDF5 engine will use subfiles as the default h5 format as it improves
I/O in general (for example, see
[https://escholarship.org/uc/item/6fs7s3jb](https://escholarship.org/uc/item/6fs7s3jb){.reference
.external})

To use the subfile feature, client needs to support MPI_Init_thread with
MPI_THREAD_MULTIPLE.

Useful parameters from the HDF library to tune subfiles are:

:::: {.highlight-xml .notranslate}
::: highlight
    H5FD_SUBFILING_IOC_PER_NODE (num of subfiles per node)
      set H5FD_SUBFILING_IOC_PER_NODE to 0 if the regular h5 file is preferred, before using ADIOS2 HDF5 engine.
    H5FD_SUBFILING_STRIPE_SIZE
    H5FD_IOC_THREAD_POOL_SIZE
:::
::::
:::::::::

::::::: {#sst-sustainable-staging-transport .section}
### SST Sustainable Staging Transport[](#sst-sustainable-staging-transport "Link to this heading"){.headerlink}

In ADIOS2, the Sustainable Staging Transport (SST) is an engine that
allows direct connection of data producers and consumers via the ADIOS2
write/read APIs. This is a classic streaming data architecture where the
data passed to ADIOS on the write side (via Put() deferred and sync, and
similar calls) is made directly available to a reader (via Get(),
deferred and sync, and similar calls).

SST is designed for use in HPC environments and can take advantage of
RDMA network interconnects to speed the transfer of data between
communicating HPC applications; however, it is also capable of operating
in a Wide Area Networking environment over standard sockets. SST
supports full MxN data distribution, where the number of reader ranks
can differ from the number of writer ranks. SST also allows multiple
reader cohorts to get access to a writer's data simultaneously.

To use this engine, you can either specify it in your xml config file,
with tag [`<engine`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`type=SST>`{.docutils .literal
.notranslate}]{.pre} or, set it in client code. For example, here is how
to create an SST reader:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::IO sstIO = adios.DeclareIO("SomeName");
    sstIO.SetEngine("SST");
    adios2::Engine sstReader = sstIO.Open(filename, adios2::Mode::Read);
:::
::::

and a sample code for SST writer is:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::IO sstIO = adios.DeclareIO("SomeName");
    sstIO.SetEngine("SST");
    adios2::Engine sstWriter = sstIO.Open(filename, adios2::Mode::Write);
:::
::::

The general goal of ADIOS2 is to ease the conversion of a file-based
application to instead use a non-file streaming interconnect, for
example, data producers such as computational physics codes and
consumers such as analysis applications. However, there are some uses of
ADIOS2 APIs that work perfectly well with the ADIOS2 file engines, but
which will not work or will perform badly with streaming. For example,
SST is based upon the *"step"* concept and ADIOS2 applications that use
SST must call [`BeginStep()`{.docutils .literal .notranslate}]{.pre} and
[`EndStep()`{.docutils .literal .notranslate}]{.pre}. On the writer
side, the [`Put()`{.docutils .literal .notranslate}]{.pre} calls between
[`BeginStep`{.docutils .literal .notranslate}]{.pre} and
[`EndStep`{.docutils .literal .notranslate}]{.pre} are the unit of
communication and represent the data that will be available between the
corresponding [`Begin`{.docutils .literal
.notranslate}]{.pre}/[`EndStep`{.docutils .literal .notranslate}]{.pre}
calls on the reader.

Also, it is recommended that SST-based applications not use the ADIOS2
Get() sync method unless there is only one data item to be read per
step. This is because SST implements MxN data transfer (and avoids
having to deliver all data to every reader), by queueing data on the
writer ranks until it is known which reader rank requires it. Normally
this data fetch stage is initiated by [`PerformGets()`{.docutils
.literal .notranslate}]{.pre} or [`EndStep()`{.docutils .literal
.notranslate}]{.pre}, both of which fulfill any pending
[`Get()`{.docutils .literal .notranslate}]{.pre} deferred operations.
However, unlike [`Get()`{.docutils .literal .notranslate}]{.pre}
deferred, the semantics of [`Get()`{.docutils .literal
.notranslate}]{.pre} sync require the requested data to be fetched from
the writers before the call can return. If there are multiple calls to
[`Get()`{.docutils .literal .notranslate}]{.pre} sync per step, each one
may require a communication with many writers, something that would have
only had to happen once if [`Get()`{.docutils .literal
.notranslate}]{.pre} differed were used instead. Thus the use of
[`Get()`{.docutils .literal .notranslate}]{.pre} sync is likely to incur
a substantial performance penalty.

On the writer side, depending upon the chosen data marshaling option
there may be some (relatively small) performance differences between
[`Put()`{.docutils .literal .notranslate}]{.pre} sync and
[`Put()`{.docutils .literal .notranslate}]{.pre} deferred, but they are
unlikely to be as substantial as between [`Get()`{.docutils .literal
.notranslate}]{.pre} sync and [`Get()`{.docutils .literal
.notranslate}]{.pre} deferred.

Note that SST readers and writers do not necessarily move in lockstep,
but depending upon the queue length parameters and queueing policies
specified, differing reader and writer speeds may cause one or the other
side to wait for data to be produced or consumed, or data may be dropped
if allowed by the queueing policy. However, steps themselves are atomic
and no step will be partially dropped, delivered to a subset of ranks,
or otherwise divided.

The SST engine allows the user to customize the streaming operations
through the following optional parameters:

1\. [`RendezvousReaderCount`{.docutils .literal .notranslate}]{.pre}:
Default **1**. This integer value specifies the number of readers for
which the writer should wait before the writer-side Open() returns. The
default of 1 implements an ADIOS1/flexpath style "rendezvous", in which
an early-starting reader will wait for the writer to start, or vice
versa. A number \>1 will cause the writer to wait for more readers and a
value of 0 will allow the writer to proceed without any readers present.
This value is interpreted by SST Writer engines only.

2\. [`RegistrationMethod`{.docutils .literal .notranslate}]{.pre}:
Default **"File"**. By default, SST reader and writer engines
communicate network contact information via files in a shared
filesystem. Specifically, the [`"filename"`{.docutils .literal
.notranslate}]{.pre} parameter in the [`Open()`{.docutils .literal
.notranslate}]{.pre} call is interpreted as a path which the writer uses
as the name of a file to which contact information is written, and from
which a reader will attempt to read contact information. As with other
file-based engines, file creation and access is subject to the usual
considerations (directory components are interpreted, but must exist and
be traversable, writer must be able to create the file and the reader
must be able to read it). Generally the file so created will exist only
for as long as the writer keeps the stream Open(), but abnormal process
termination may leave "stale" files in those locations. These stray
".sst" files should be deleted to avoid confusing future readers. SST
also offers a **"Screen"** registration method in which writers and
readers send their contact information to, and read it from, stdout and
stdin respectively. The "screen" registration method doesn't support
batch mode operations in any way, but may be useful when manually
starting jobs on machines in a WAN environment that don't share a
filesystem. A future release of SST will also support a **"Cloud"**
registration method where contact information is registered to and
retrieved from a network-based third-party server so that both the
shared filesystem and interactivity can be avoided. This value is
interpreted by both SST Writer and Reader engines.

3\. [`QueueLimit`{.docutils .literal .notranslate}]{.pre}: Default
**0**. This integer value specifies the number of steps which the writer
will allow to be queued before taking specific action (such as
discarding data or waiting for readers to consume the data). The default
value of 0 is interpreted as no limit. This value is interpreted by SST
Writer engines only.

4\. [`QueueFullPolicy`{.docutils .literal .notranslate}]{.pre}: Default
**"Block"**. This value controls what policy is invoked if a non-zero
**QueueLimit** has been specified and new data would cause the queue
limit to be reached. Essentially, the **"Block"** option ensures data
will not be discarded and if the queue fills up the writer will block on
**EndStep** until the data has been read. If there is one active reader,
**EndStep** will block until data has been consumed off the front of the
queue to make room for newly arriving data. If there is more than one
active reader, it is only removed from the queue when it has been read
by all readers, so the slowest reader will dictate progress. **NOTE THAT
THE NO READERS SITUATION IS A SPECIAL CASE**: If there are no active
readers, new timesteps are considered to have completed their active
queueing immediately upon submission. They may be retained in the
"reserve queue" if the ReserveQueueLimit is non-zero. However, if that
ReserveQueueLimit parameter is zero, timesteps submitted when there are
no active readers will be immediately discarded.

Besides **"Block"**, the other acceptable value for **QueueFullPolicy**
is **"Discard"**. When **"Discard"** is specified, and an **EndStep**
operation would add more than the allowed number of steps to the queue,
some step is discarded. If there are no current readers connected to the
stream, the *oldest* data in the queue is discarded. If there are
current readers, then the *newest* data (I.E. the just-created step) is
discarded. (The differential treatment is because SST sends metadata for
each step to the readers as soon as the step is accepted and cannot
reliably prevent that use of that data without a costly all-to-all
synchronization operation. Discarding the *newest* data instead is less
satisfying, but has a similar long-term effect upon the set of steps
delivered to the readers.) This value is interpreted by SST Writer
engines only.

5\. [`ReserveQueueLimit`{.docutils .literal .notranslate}]{.pre}:
Default **0**. This integer value specifies the number of steps which
the writer will keep in the queue for the benefit of late-arriving
readers. This may consist of timesteps that have already been consumed
by any readers, as well as timesteps that have not yet been consumed. In
some sense this is target queue minimum size, while QueueLimit is a
maximum size. This value is interpreted by SST Writer engines only.

6\. [`DataTransport`{.docutils .literal .notranslate}]{.pre}: Default
**varies**. This string value specifies the underlying network
communication mechanism to use for exchanging data in SST. Generally
this is chosen by SST based upon what is available on the current
platform. However, specifying this engine parameter allows overriding
SST's choice. Current allowed values are **"UCX"**, **"MPI"**,
**"RDMA"**, and **"WAN"**. (**ib** and **fabric** are accepted as
equivalent to **RDMA** and **evpath** is equivalent to **WAN**.)
Generally both the reader and writer should be using the same network
transport, and the network transport chosen may be dictated by the
situation. For example, the RDMA transport generally operates only
between applications running on the same high-performance interconnect
(e.g. on the same HPC machine). If communication is desired between
applications running on different interconnects, the Wide Area Network
(WAN) option should be chosen. This value is interpreted by both SST
Writer and Reader engines.

7\. [`WANDataTransport`{.docutils .literal .notranslate}]{.pre}: Default
**sockets**. If the SST **DataTransport** parameter is **"WAN**, this
string value specifies the EVPath-level data transport to use for
exchanging data. The value must be a data transport known to EVPath,
such as **"sockets"**, **"enet"**, or **"ib"**. Generally both the
reader and writer should be using the same EVPath-level data transport.
This value is interpreted by both SST Writer and Reader engines.

8\. [`ControlTransport`{.docutils .literal .notranslate}]{.pre}: Default
**tcp**. This string value specifies the underlying network
communication mechanism to use for performing control operations in SST.
SST can be configured to standard TCP sockets, which are very reliable
and efficient, but which are limited in their scalability.
Alternatively, SST can use a reliable UDP protocol, that is more
scalable, but as of ADIOS2 Release 2.4.0 still suffers from some
reliability problems. (**sockets** is accepted as equivalent to **tcp**
and **udp**, **rudp**, and **enet** are equivalent to **scalable**.
Generally both the reader and writer should be using the same control
transport. This value is interpreted by both SST Writer and Reader
engines.

9\. [`NetworkInterface`{.docutils .literal .notranslate}]{.pre}: Default
**NULL**. In situations in which there are multiple possible network
interfaces available to SST, this string value specifies which should be
used to generate SST's contact information for writers. Generally this
should *NOT* be specified except for narrow sets of circumstances. It
has no effect if specified on Reader engines. If specified, the string
value should correspond to a name of a network interface, such as are
listed by commands like "netstat -i". For example, on most Unix systems,
setting the NetworkInterface parameter to "lo" (or possibly "lo0") will
result in SST generating contact information that uses the network
address associated with the loopback interface (127.0.0.1). This value
is interpreted by only by the SST Writer engine.

10\. [`ControlInterface`{.docutils .literal .notranslate}]{.pre}:
Default **NULL**. This value is similar to the NetworkInterface
parameter, but only applies to the SST layer which does messaging for
control (open, close, flow and timestep management, but not actual data
transfer). Generally the NetworkInterface parameter can be used to
control this, but that also aplies to the Data Plane. Use
ControlInterface in the event of conflicting specifications.

11\. [`DataInterface`{.docutils .literal .notranslate}]{.pre}: Default
**NULL**. This value is similar to the NetworkInterface parameter, but
only applies to the SST layer which does messaging for data transfer,
not control (open, close, flow and timestep management). Generally the
NetworkInterface parameter can be used to control this, but that also
aplies to the Control Plane. Use DataInterface in the event of
conflicting specifications. In the case of the RDMA data plane, this
parameter controls the libfabric interface choice.

12\. [`FirstTimestepPrecious`{.docutils .literal .notranslate}]{.pre}:
Default **FALSE**. FirstTimestepPrecious is a boolean parameter that
affects the queueing of the first timestep presented to the SST Writer
engine. If FirstTimestepPrecious is **TRUE**, then the first timestep is
effectively never removed from the output queue and will be presented as
a first timestep to any reader that joins at a later time. This can be
used to convey run parameters or other information that every reader may
need despite joining later in a data stream. Note that this queued first
timestep does count against the QueueLimit parameter above, so if a
QueueLimit is specified, it should be a value larger than 1. Further
note while specifying this parameter guarantees that the preserved first
timestep will be made available to new readers, other reader-side
operations (like requesting the LatestAvailable timestep in Engine
parameters) might still cause the timestep to be skipped. This value is
interpreted by only by the SST Writer engine.

13\. [`AlwaysProvideLatestTimestep`{.docutils .literal
.notranslate}]{.pre}: Default **FALSE**. AlwaysProvideLatestTimestep is
a boolean parameter that affects what of the available timesteps will be
provided to the reader engine. If AlwaysProvideLatestTimestep is
**TRUE**, then if there are multiple timesteps available to the reader,
older timesteps will be skipped and the reader will see only the newest
available upon BeginStep. This value is interpreted by only by the SST
Reader engine.

14\. [`OpenTimeoutSecs`{.docutils .literal .notranslate}]{.pre}: Default
**60**. OpenTimeoutSecs is an integer parameter that specifies the
number of seconds SST is to wait for a peer connection on Open().
Currently this is only implemented on the Reader side of SST, and is a
timeout for locating the contact information file created by Writer-side
Open, not for completing the entire Open() handshake. Currently value is
interpreted by only by the SST Reader engine.

15\. [`SpeculativePreloadMode`{.docutils .literal .notranslate}]{.pre}:
Default **AUTO**. In some circumstances, SST eagerly sends all data from
writers to every readers without first waiting for read requests.
Generally this improves performance if every reader needs all the data,
but can be very detrimental otherwise. The value **AUTO** for this
engine parameter instructs SST to apply its own heuristic for
determining if data should be eagerly sent. The value **OFF** disables
this feature and the value **ON** causes eager sending regardless of
heuristic. Currently SST's heuristic is simple. If the size of the
reader cohort is less than or equal to the value of the
[`SpecAutoNodeThreshold`{.docutils .literal .notranslate}]{.pre} engine
parameter (Default value 1), eager sending is initiated. Currently value
is interpreted by only by the SST Reader engine.

16\. [`SpecAutoNodeThreshold`{.docutils .literal .notranslate}]{.pre}:
Default **1**. If the size of the reader cohort is less than or equal to
this value *and* the [`SpeculativePreloadMode`{.docutils .literal
.notranslate}]{.pre} parameter is **AUTO**, SST will initiate eager data
sending of all data from each writer to all readers. Currently value is
interpreted by only by the SST Reader engine.

17\. [`StepDistributionMode`{.docutils .literal .notranslate}]{.pre}:
Default **"AllToAll"**. This value controls how steps are distributed,
particularly when there are multiple readers. By default, the value is
**"AllToAll"**, which means that all timesteps are to be delivered to
all readers (subject to discard rules, etc.). In other distribution
modes, this is not the case. For example, in **"RoundRobin"**, each step
is delivered only to a single reader, determined in a round-robin
fashion based upon the number or readers who have opened the stream at
the time the step is submitted. In **"OnDemand"** each step is delivered
to a single reader, but only upon request (with a request being
initiated by the reader doing BeginStep()). Normal reader-side rules
(like BeginStep timeouts) and writer-side rules (like queue limit
behavior) apply.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Key**                                                                                                                                                                                                                                                                                                              **Value Format**                                                                                                                **Default** and Examples
  RendezvousReaderCount RegistrationMethod QueueLimit QueueFullPolicy ReserveQueueLimit DataTransport WANDataTransport ControlTransport MarshalMethod NetworkInterface ControlInterface DataInterface FirstTimestepPrecious AlwaysProvideLatestTimestep OpenTimeoutSecs SpeculativePreloadMode SpecAutoNodeThreshold   integer string integer string integer string string string string string string string boolean boolean integer string integer   **1** **File**, Screen **0** (no queue limits) **Block**, Discard **0** (no queue limits) **default varies by platform**, UCX, MPI, RDMA, WAN **sockets**, enet, ib **TCP**, Scalable **BP5**, BP, FFS **NULL** **NULL** **NULL** **FALSE**, true, no, yes **FALSE**, true, no, yes **60** **AUTO**, ON, OFF **1**
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::::::

::: {#ssc-strong-staging-coupler .section}
### SSC Strong Staging Coupler[](#ssc-strong-staging-coupler "Link to this heading"){.headerlink}

The SSC engine is designed specifically for strong code coupling.
Currently SSC only supports fixed IO pattern, which means once the first
step is finished, users are not allowed to write or read a data block
with a *start* and *count* that have not been written or read in the
first step. SSC uses a combination of one sided MPI and two sided MPI
methods. In any cases, all user applications are required to be launched
within a single mpirun or mpiexec command, using the MPMD mode.

The SSC engine takes the following parameters:

1.  [`OpenTimeoutSecs`{.docutils .literal .notranslate}]{.pre}: Default
    **10**. Timeout in seconds for opening a stream. The SSC engine's
    open function will block until the RendezvousAppCount is reached, or
    timeout, whichever comes first. If it reaches the timeout, SSC will
    throw an exception.

2.  [`Threading`{.docutils .literal .notranslate}]{.pre}: Default
    **False**. SSC will use threads to hide the time cost for metadata
    manipulation and data transfer when this parameter is set to
    **true**. SSC will check if MPI is initialized with multi-thread
    enabled, and if not, then SSC will force this parameter to be
    **false**. Please do NOT enable threading when multiple I/O streams
    are opened in an application, as it will cause unpredictable errors.
    This parameter is only effective when writer definitions and reader
    selections are NOT locked. For cases definitions and reader
    selections are locked, SSC has a more optimized way to do data
    transfers, and thus it will not use this parameter.

  **Key**           **Value Format**   **Default** and Examples
  ----------------- ------------------ --------------------------
  OpenTimeoutSecs   integer            **10**, 2, 20, 200
  Threading         bool               **false**, true
:::

::: {#dataman-for-wide-area-network-data-staging .section}
### DataMan for Wide Area Network Data Staging[](#dataman-for-wide-area-network-data-staging "Link to this heading"){.headerlink}

The DataMan engine is designed for data staging over the wide area
network. It is supposed to be used in cases where a few writers send
data to a few readers over long distance.

DataMan supports compression operators such as ZFP lossy compression and
BZip2 lossless compression. Please refer to the operator section for
usage.

The DataMan engine takes the following parameters:

1.  [`IPAddress`{.docutils .literal .notranslate}]{.pre}: No default
    value. The IP address of the host where the writer application runs.
    This parameter is compulsory in wide area network data staging.

2.  [`Port`{.docutils .literal .notranslate}]{.pre}: Default **50001**.
    The port number on the writer host that will be used for data
    transfers.

3.  [`Timeout`{.docutils .literal .notranslate}]{.pre}: Default **5**.
    Timeout in seconds to wait for every send / receive operation.
    Packages not sent or received within this time are considered lost.

4.  [`RendezvousReaderCount`{.docutils .literal .notranslate}]{.pre}:
    Default **1**. This integer value specifies the number of readers
    for which the writer should wait before the writer-side Open()
    returns. By default, an early-starting writer will wait for the
    reader to start, or vice versa. A number \>1 will cause the writer
    to wait for more readers, and a value of 0 will allow the writer to
    proceed without any readers present. This value is interpreted by
    DataMan Writer engines only.

5.  [`Threading`{.docutils .literal .notranslate}]{.pre}: Default
    **true** for reader, **false** for writer. Whether to use threads
    for send and receive operations. Enabling threading will cause extra
    overhead for managing threads and buffer queues, but will improve
    the continuity of data steps for readers, and help overlap data
    transfers with computations for writers.

6.  [`TransportMode`{.docutils .literal .notranslate}]{.pre}: Default
    **fast**. Only DataMan writers take this parameter. Readers are
    automatically synchronized at runtime to match writers' transport
    mode. The fast mode is optimized for latency-critical applications.
    It enforces readers to only receive the latest step. Therefore, in
    cases where writers are faster than readers, readers will skip some
    data steps. The reliable mode ensures that all steps are received by
    readers, by sacrificing performance compared to the fast mode.

7.  [`MaxStepBufferSize`{.docutils .literal .notranslate}]{.pre}:
    Default **128000000**. In order to bring down the latency in wide
    area network staging use cases, DataMan uses a fixed receiver buffer
    size. This saves an extra communication operation to sync the buffer
    size for each step, before sending actual data. The default buffer
    size is 128 MB, which is sufficient for most use cases. However, in
    case 128 MB is not enough, this parameter must be set correctly,
    otherwise DataMan will fail.

  **Key**                 **Value Format**   **Default** and Examples
  ----------------------- ------------------ -------------------------------------------
  IPAddress               string             **N/A**, 22.195.18.29
  Port                    integer            **50001**, 22000, 33000
  Timeout                 integer            **5**, 10, 30
  RendezvousReaderCount   integer            **1**, 0, 3
  Threading               bool               **true** for reader, **false** for writer
  TransportMode           string             **fast**, reliable
  MaxStepBufferSize       integer            **128000000**, 512000000, 1024000000
:::

::::::::: {#dataspaces .section}
### DataSpaces[](#dataspaces "Link to this heading"){.headerlink}

The DataSpaces engine for ADIOS2 is experimental. DataSpaces is an
asynchronous I/O transfer method within ADIOS that enables low-overhead,
high-throughput data extraction from a running simulation. DataSpaces is
designed for use in HPC environments and can take advantage of RDMA
network interconnects to speed the transfer of data between
communicating HPC applications. DataSpaces supports full MxN data
distribution, where the number of reader ranks can differ from the
number of writer ranks. In addition, this engine supports multiple
reader and writer applications, which must be distinguished by unique
values of [`AppID`{.docutils .literal .notranslate}]{.pre} for different
applications. It can be set in the xml config file with tag
[`<parameter`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`key="AppID"`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`value="2"/>`{.docutils .literal .notranslate}]{.pre}. The
value should be unique for each applications or clients.

To use this engine, you can either specify it in your xml config file,
with tag [`<engine`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`type=DATASPACES>`{.docutils .literal
.notranslate}]{.pre} or, set it in client code. For example, here is how
to create an DataSpaces reader:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::IO dspacesIO = adios.DeclareIO("SomeName");
    dspacesIO.SetEngine("DATASPACES");
    adios2::Engine dspacesReader = dspacesIO.Open(filename, adios2::Mode::Read);
:::
::::

and a sample code for DataSpaces writer is:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::IO dspacesIO = adios.DeclareIO("SomeName");
    dspacesIO.SetEngine("DATASPACES");
    adios2::Engine dspacesWriter = dspacesIO.Open(filename, adios2::Mode::Write);
:::
::::

To make use of the DataSpaces engine, an application job needs to also
run the dataspaces_server component together with the application. The
server should be configured and started before the application as a
separate job in the system. For example:

[`aprun`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`-n`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`$SPROC`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`./dataspaces_server`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-s`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`$SPROC`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`&>`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`log.server`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`&`{.docutils
.literal .notranslate}]{.pre}

The variable [`$SPROC`{.docutils .literal .notranslate}]{.pre}
represents the number of server instances to run. The [`&`{.docutils
.literal .notranslate}]{.pre} character at the end of the line would
place the [`aprun`{.docutils .literal .notranslate}]{.pre} command in
the background, and will allow the job script to continue and run the
other applications. The server processes produce a configuration file,
i.e., [`conf.0`{.docutils .literal .notranslate}]{.pre} that is used by
the application to connect to the servers. This file contains
identifying information of the master server, which coordinates the
client registration and discovery process. The job script should wait
for the servers to start-up and produce the [`conf.0`{.docutils .literal
.notranslate}]{.pre} file before starting the client application
processes.

The server also needs a user configuration read from a text file called
[`dataspaces.conf`{.docutils .literal .notranslate}]{.pre}. How many
output timesteps of the same dataset (called versions) should be kept in
the server's memory and served to readers should be specified in the
file. If this file does not exist in the current directory, the server
will assume default values (only 1 timestep stored). .. code-block:

:::: {.highlight-default .notranslate}
::: highlight
    ## Config file for DataSpaces
    max_versions = 5
    lock_type = 3
:::
::::

The dataspaces_server module is a stand-alone service that runs
independently of a simulation on a set of dedicated nodes in the staging
area. It transfers data from the application through RDMA, and can save
it to local storage system, e.g., the Lustre file system, stream it to
remote sites, e.g., auxilliary clusters, or serve it directly from the
staging area to other applications. One instance of the
dataspaces_server can service multiple applications in parallel.
Further, the server can run in cooperative mode (i.e., multiple
instances of the server cooperate to service the application in parallel
and to balance load). The dataspaces_server receives notification
messages from the transport method, schedules the requests, and
initiates the data transfers in parallel. The server schedules and
prioritizes the data transfers while the simulation is computing in
order to overlap data transfers with computations, to maximize data
throughput, and to minimize the overhead on the application.
:::::::::

:::::::::: {#inline-for-zero-copy .section}
### Inline for zero-copy[](#inline-for-zero-copy "Link to this heading"){.headerlink}

The [`Inline`{.docutils .literal .notranslate}]{.pre} engine provides
in-process communication between the writer and reader, avoiding the
copy of data buffers.

This engine is focused on the N → N case: N writers share a process with
N readers, and the analysis happens 'inline' without writing the data to
a file or copying to another buffer. It is similar to the streaming SST
engine, since analysis must happen per step.

To use this engine, you can either add [`<engine`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`type=Inline>`{.docutils .literal .notranslate}]{.pre} to
your XML config file, or set it in your application code:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::IO io = adios.DeclareIO("ioName");
    io.SetEngine("Inline");
    adios2::Engine inlineWriter = io.Open("inline_write", adios2::Mode::Write);
    adios2::Engine inlineReader = io.Open("inline_read", adios2::Mode::Read);
:::
::::

Notice that unlike other engines, the reader and writer share an IO
instance. Both the writer and reader must be opened before either tries
to call [`BeginStep()`{.docutils .literal
.notranslate}]{.pre}/[`PerformPuts()`{.docutils .literal
.notranslate}]{.pre}/[`PerformGets()`{.docutils .literal
.notranslate}]{.pre}. There must be exactly one writer, and exactly one
reader.

For successful operation, the writer will perform a step, then the
reader will perform a step in the same process. When the reader starts
its step, the only data it has available is that written by the writer
in its process. The reader then can retrieve whatever data was written
by the writer by using the double-pointer [`Get`{.docutils .literal
.notranslate}]{.pre} call:

:::: {.highlight-c++ .notranslate}
::: highlight
    void Engine::Get<T>(Variable<T>, T**) const;
:::
::::

This version of [`Get`{.docutils .literal .notranslate}]{.pre} is only
used for the inline engine. See the example below for details.

::: {.admonition .note}
Note

Since the inline engine does not copy any data, the writer should avoid
changing the data before the reader has read it.
:::

Typical access pattern:

:::: {.highlight-c++ .notranslate}
::: highlight
    // ... Application data generation

    inlineWriter.BeginStep();
    inlineWriter.Put(var, in_data); // always use deferred mode
    inlineWriter.EndStep();
    // Unlike other engines, data should not be reused at this point (since ADIOS
    // does not copy the data), though ADIOS cannot enforce this.
    // Must wait until reader is finished using the data.

    inlineReader.BeginStep();
    double* out_data;
    inlineReader.Get(var, &data);
    // Now in_data == out_data.
    inlineReader.EndStep();
:::
::::
::::::::::

::::::::::: {#null .section}
### Null[](#null "Link to this heading"){.headerlink}

The [`Null`{.docutils .literal .notranslate}]{.pre} Engine performs no
internal work and no I/O. It was created for testing applications that
have ADIOS2 output in it by turning off the I/O easily. The runtime
difference between a run with the Null engine and another engine tells
us the IO overhead of that particular output with that particular
engine.

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::IO io = adios.DeclareIO("Output");
    io.SetEngine("Null");
:::
::::

or using the XML config file:

:::: {.highlight-xml .notranslate}
::: highlight
    <adios-config>
        <io name="Output">
            <engine type="Null">
            </engine>
        </io>
    </adios-config>
:::
::::

Although there is a reading engine as well, which will not fail, any
variable/attribute inquiry returns nullptr and any subsequent Get()
calls will throw an exception in C++/Python or return an error in
C/Fortran.

Note that there is also a Null transport that can be used by a BP engine
instead of the default File transport. In that case, the BP engine will
perform all internal work including buffering and aggregation but no
data will be output at all. A run like this can be used to assess the
overhead of the internal work of the BP engine.

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::IO io = adios.DeclareIO("Output");
    io.SetEngine("BP5");
    io.AddTransport("Null", {});
:::
::::

or using the XML config file

:::: {.highlight-xml .notranslate}
::: highlight
    <adios-config>
        <io name="Output">
            <engine type="BP5">
            </engine>
            <transport type="Null">
            </transport>
        </io>
    </adios-config>
:::
::::
:::::::::::

::: {#plugin-engine .section}
### Plugin Engine[](#plugin-engine "Link to this heading"){.headerlink}

For details on using the Plugin Engine, see the [[Plugins]{.std
.std-ref}](#document-advanced/plugins#plugins){.reference .internal}
documentation.
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

[]{#document-operators/operators}

:::::::::: {#supported-operators .section}
## Supported Operators[](#supported-operators "Link to this heading"){.headerlink}

The Operator abstraction allows ADIOS2 to act upon the user application
data, either from a [`adios2::Variable`{.docutils .literal
.notranslate}]{.pre} or a set of Variables in an [`adios2::IO`{.docutils
.literal .notranslate}]{.pre} object. Current supported operations are:

1.  Data compression/decompression, lossy and lossless.

This section provides a description of the supported operators in ADIOS2
and their specific parameters to allow extra-control from the user.
Parameters are passed in key-value pairs for:

1.  Operator general supported parameters.

2.  Operator specific supported parameters.

Parameters are passed at:

1.  Compile time: using the second parameter of the method
    [`ADIOS2::DefineOperator`{.docutils .literal .notranslate}]{.pre}

2.  [[Runtime Configuration Files]{.std
    .std-ref}](#document-components/components#runtime-configuration-files){.reference
    .internal} in the [[ADIOS]{.std
    .std-ref}](#document-components/components#adios){.reference
    .internal} component.

::::::: {#compressorzfp .section}
### CompressorZFP[](#compressorzfp "Link to this heading"){.headerlink}

The [`CompressorZFP`{.docutils .literal .notranslate}]{.pre} Operator is
compressor that uses a lossy but optionally error-bounded compression to
achieve high compression ratios.

ZFP provides compressed-array classes that support high throughput read
and write random access to individual array elements. ZFP also supports
serial and parallel (OpenMP and CUDA) compression of whole arrays, e.g.,
for applications that read and write large data sets to and from disk.

ADIOS2 provides a [`CompressorZFP`{.docutils .literal
.notranslate}]{.pre} operator that lets you compress an decompress
variables. Below there is an example of how to invoke
[`CompressorZFP`{.docutils .literal .notranslate}]{.pre} operator:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::IO io = adios.DeclareIO("Output");
    auto ZFPOp    = adios.DefineOperator("CompressorZFP", adios2::ops::LossyZFP);

    auto var_r32 = io.DefineVariable<float>("r32", shape, start, count);
    var_r32.AddOperation(ZFPOp, {{adios2::ops::zfp::key::rate, rate}});
:::
::::

::: {#compressorzfp-specific-parameters .section}
#### CompressorZFP Specific parameters[](#compressorzfp-specific-parameters "Link to this heading"){.headerlink}

The [`CompressorZFP`{.docutils .literal .notranslate}]{.pre} operator
accepts the following operator specific parameters:

+---------------------------------------------------------------------+
| [`CompressorZFP`{.docutils .literal .notranslate}]{.pre} available  |
| parameters                                                          |
+==================================+==================================+
| [`accuracy`{.docutils .literal   | Fixed absolute error tolerance   |
| .notranslate}]{.pre}             |                                  |
+----------------------------------+----------------------------------+
| [`rate`{.docutils .literal       | Fixed number of bits in a        |
| .notranslate}]{.pre}             | compression unit                 |
+----------------------------------+----------------------------------+
| [`precision`{.docutils .literal  | Fixed number of uncompressed     |
| .notranslate}]{.pre}             | bits per value                   |
+----------------------------------+----------------------------------+
| [`backend`{.docutils .literal    | Backend device:                  |
| .notranslate}]{.pre}             | [`cuda`{.docutils .literal       |
|                                  | .notranslate}]{.pre}             |
|                                  | [`omp`{.docutils .literal        |
|                                  | .notranslate}]{.pre}             |
|                                  | [`serial`{.docutils .literal     |
|                                  | .notranslate}]{.pre}             |
+----------------------------------+----------------------------------+
:::

::: {#compressorzfp-execution-policy .section}
#### CompressorZFP Execution Policy[](#compressorzfp-execution-policy "Link to this heading"){.headerlink}

[`CompressorZFP`{.docutils .literal .notranslate}]{.pre} can run in
multiple backend devices: GPUs (CUDA), OpenMP, and in the host CPU. By
default [`CompressorZFP`{.docutils .literal .notranslate}]{.pre} will
choose its backend following the above order upon the availability of
the device adapter.

Exceptionally, if its corresponding ADIOS2 variable contains a CUDA
memory address, this is a CUDA buffer, the CUDA backend will be called
if available.

In any case, the user can manually set the backend using the ZFPOperator
specific parameter [`backend`{.docutils .literal .notranslate}]{.pre}.
:::
:::::::

::: {#plugin-operator .section}
### Plugin Operator[](#plugin-operator "Link to this heading"){.headerlink}

For details on using the Plugin Operator, see the [[Plugins]{.std
.std-ref}](#document-advanced/plugins#plugins){.reference .internal}
documentation.
:::

::: {#encryption .section}
### Encryption[](#encryption "Link to this heading"){.headerlink}

The Encryption Operator uses the [[Plugins]{.std
.std-ref}](#document-advanced/plugins#plugins){.reference .internal}
interface. This operator uses
[libsodium](https://doc.libsodium.org/){.reference .external} for
encrypting and decrypting data. If ADIOS can find libsodium at configure
time, this plugin will be built.

This operator will generate a secret key and encrypts the data with the
key and a nonce as described in the libsodium [secret key cryptography
docs](https://doc.libsodium.org/secret-key_cryptography/secretbox){.reference
.external}. The key is saved to the specified [`SecretKeyFile`{.docutils
.literal .notranslate}]{.pre} and will be used for decryption. The key
should be kept confidential since it is used to both encrypt and decrypt
the data.

Parameters to use with the Encryption operator:

  **Key**         **Value Format**   **Explanation**
  --------------- ------------------ -------------------------------------------------------------------------------------------------
  PluginName      string             Required. Name to refer to plugin, e.g., [`MyOperator`{.docutils .literal .notranslate}]{.pre}
  PluginLibrary   string             Required. Name of shared library, [`EncryptionOperator`{.docutils .literal .notranslate}]{.pre}
  SecretKeyFile   string             Required. Path to secret key file
:::
::::::::::

[]{#document-api_full/api_full}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#full-apis .section}
## Full APIs[](#full-apis "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

Application developers who desire fine-grained control of IO tasks
should use the Full APIs. In simple cases (e.g. reading a file for
analysis, interactive Python, or saving some data for a small project or
tests) please refer to the [[High-Level APIs]{.std
.std-ref}](#document-api_high/api_high#high-level-apis){.reference
.internal}.
:::

Currently ADIOS2 support bindings for the following languages and their
minimum standards:

+-----------------------+-----------------------+--------------------------------------+
| Language              | Standard              | Interface                            |
+-----------------------+-----------------------+--------------------------------------+
| C++                   | 11/newer              | [`#include`{.docutils .literal       |
|                       |                       | .notranslate}]{.pre}` `{.docutils    |
|                       | older                 | .literal                             |
|                       |                       | .notranslate}[`adios2.h`{.docutils   |
|                       |                       | .literal .notranslate}]{.pre}        |
|                       |                       |                                      |
|                       |                       | use C bindings                       |
+-----------------------+-----------------------+--------------------------------------+
| C                     | 99                    | [`#include`{.docutils .literal       |
|                       |                       | .notranslate}]{.pre}` `{.docutils    |
|                       |                       | .literal                             |
|                       |                       | .notranslate}[`adios2_c.h`{.docutils |
|                       |                       | .literal .notranslate}]{.pre}        |
+-----------------------+-----------------------+--------------------------------------+
| Fortran               | 90                    | [`use`{.docutils .literal            |
|                       |                       | .notranslate}]{.pre}` `{.docutils    |
|                       |                       | .literal                             |
|                       |                       | .notranslate}[`adios2`{.docutils     |
|                       |                       | .literal .notranslate}]{.pre}        |
+-----------------------+-----------------------+--------------------------------------+
| Python                | 2.7                   | [`import`{.docutils .literal         |
|                       |                       | .notranslate}]{.pre}` `{.docutils    |
|                       | 3                     | .literal                             |
|                       |                       | .notranslate}[`adios2`{.docutils     |
|                       |                       | .literal .notranslate}]{.pre}        |
|                       |                       |                                      |
|                       |                       | [`import`{.docutils .literal         |
|                       |                       | .notranslate}]{.pre}` `{.docutils    |
|                       |                       | .literal                             |
|                       |                       | .notranslate}[`adios2`{.docutils     |
|                       |                       | .literal .notranslate}]{.pre}        |
+-----------------------+-----------------------+--------------------------------------+

::: {.admonition .tip}
Tip

Prefer the C++11 bindings if your application C++ compiler supports the
2011 (or later) standard. For code using previous C++ standards (98 or
03) use the C bindings for ABI compatibility.
:::

::: {.admonition .caution}
Caution

Statically linked libraries ([`*.a`{.docutils .literal
.notranslate}]{.pre}) might result in conflicting ABIs between an older
C++ project, the C bindings, and the adios native C++11 library. Test to
make sure it works for your platform.
:::

The current interaction flow for each language binding API with the
ADIOS2 library is specified as follows

The following sections provide a summary of the API calls on each
language and links to Write and Read examples to put it all together.

:::::::::::::::::::::::::::::::: {#c-11-bindings .section}
### C++11 bindings[](#c-11-bindings "Link to this heading"){.headerlink}

::: {.admonition .caution}
Caution

DO NOT use the clause [`using`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`namespace`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`adios2`{.docutils .literal .notranslate}]{.pre} in your
code. This is in general a bad practices that creates potential name
conflicts. Always use [`adios2::`{.docutils .literal
.notranslate}]{.pre} explicitly, *e.g.* [`adios2::ADIOS`{.docutils
.literal .notranslate}]{.pre}, [`adios2::IO`{.docutils .literal
.notranslate}]{.pre}.
:::

::: {.admonition .tip}
Tip

Prefer the C++11 bindings to take advantage of added functionality
(*e.g.* move semantics, lambdas, etc.). If you must use an older C++
standard (98 or 03) to avoid application binary interface (ABI)
incompatibilities use the C bindings.
:::

::::: {#adios2-components-classes .section}
#### ADIOS2 components classes[](#adios2-components-classes "Link to this heading"){.headerlink}

ADIOS2 C++ bindings objects are mapped 1-to-1 to the ADIOS components
described in the [[Components Overview]{.std
.std-ref}](#document-components/components#components-overview){.reference
.internal} section. Only the [`adios2::ADIOS`{.docutils .literal
.notranslate}]{.pre} object is "owned" by the developer's program using
adios2, all other components are light-weight objects that point
internally to a component that lives inside the
[`adios2::ADIOS`{.docutils .literal .notranslate}]{.pre} "factory"
object.

:::: {.highlight-c++ .notranslate}
::: highlight
    c++11
    adios2::ADIOS
    adios2::IO
    adios2::Variable<T>
    adios2::Attribute<T>
    adios2::Engine
    adios2::Operator
:::
::::

The following section provides a summary of the available functionality
for each class.
:::::

::: {#adios-class .section}
#### [[ADIOS]{.std .std-ref}](#document-components/components#adios){.reference .internal} class[](#adios-class "Link to this heading"){.headerlink}

[]{#_CPPv3N6adios25ADIOSE}[]{#_CPPv2N6adios25ADIOSE}[]{#adios2::ADIOS}[]{#classadios2_1_1ADIOS .target}[[class]{.pre}]{.k}[ ]{.w}[[[ADIOS]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios25ADIOSE "Link to this definition"){.headerlink}\

:   ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N6adios25ADIOS5ADIOSE8MPI_Comm}[]{#_CPPv2N6adios25ADIOS5ADIOSE8MPI_Comm}[]{#adios2::ADIOS::ADIOS__MPI_Comm}[]{#classadios2_1_1ADIOS_1a80ac429ddbe2df4a20bfb23397250805 .target}[[[ADIOS]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[MPI_Comm]{.pre}]{.n}[ ]{.w}[[comm]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios25ADIOS5ADIOSE8MPI_Comm "Link to this definition"){.headerlink}\

    :   Starting point for MPI apps. Creates an [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} object. MPI Collective Operation as it call
        MPI_Comm_dup

        Parameters[:]{.colon}

        :   **comm** -- defines domain scope from application

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if user input is incorrect

    <!-- -->

    []{#_CPPv3N6adios25ADIOS5ADIOSERKNSt6stringE8MPI_Comm}[]{#_CPPv2N6adios25ADIOS5ADIOSERKNSt6stringE8MPI_Comm}[]{#adios2::ADIOS::ADIOS__ssCR.MPI_Comm}[]{#classadios2_1_1ADIOS_1a2ef99b719f59c63c8cfb20299b4837f7 .target}[[[ADIOS]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[configFile]{.pre}]{.n .sig-param}, [[MPI_Comm]{.pre}]{.n}[ ]{.w}[[comm]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios25ADIOS5ADIOSERKNSt6stringE8MPI_Comm "Link to this definition"){.headerlink}\

    :   Starting point for MPI apps. Creates an [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} object allowing a runtime config file. MPI collective
        and it calls MPI_Comm_dup and MPI_Bcast to pass the configFile
        contents

        Parameters[:]{.colon}

        :   - **configFile** -- runtime config file

            - **comm** -- defines domain scope from application

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if user input is incorrect

    <!-- -->

    []{#_CPPv3N6adios25ADIOS5ADIOSERKNSt6stringE8MPI_CommRKNSt6stringE}[]{#_CPPv2N6adios25ADIOS5ADIOSERKNSt6stringE8MPI_CommRKNSt6stringE}[]{#adios2::ADIOS::ADIOS__ssCR.MPI_Comm.ssCR}[]{#classadios2_1_1ADIOS_1a30319f51d3a1181834ee7174e51720cb .target}[[[ADIOS]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[configFile]{.pre}]{.n .sig-param}, [[MPI_Comm]{.pre}]{.n}[ ]{.w}[[comm]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[hostLanguage]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios25ADIOS5ADIOSERKNSt6stringE8MPI_CommRKNSt6stringE "Link to this definition"){.headerlink}\

    :   extra constructor for R and other languages that use the public
        C++ API but has data in column-major. Pass "" for configfile if
        there is no config file. Last bool argument exist only to ensure
        matching this signature by having different number of arguments.
        Supported languages are "R", "Matlab", "Fortran", all these
        names mean the same thing: treat all arrays column-major e.g.
        [[adios2::ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal}("", comm, "Fortran", false);

    <!-- -->

    []{#_CPPv3N6adios25ADIOS5ADIOSERKNSt6stringE}[]{#_CPPv2N6adios25ADIOS5ADIOSERKNSt6stringE}[]{#adios2::ADIOS::ADIOS__ssCR}[]{#classadios2_1_1ADIOS_1adf0138952b31cfc9df4c8372df3f20f4 .target}[[[ADIOS]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[configFile]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios25ADIOS5ADIOSERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Starting point for non-MPI serial apps. Creates an [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} object allowing a runtime config file.

        Parameters[:]{.colon}

        :   **configFile** -- runtime config file

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if user input is incorrect

    <!-- -->

    []{#_CPPv3N6adios25ADIOS5ADIOSEv}[]{#_CPPv2N6adios25ADIOS5ADIOSEv}[]{#adios2::ADIOS::ADIOS}[]{#classadios2_1_1ADIOS_1a868d23ab4c6475bd82e3adceeb56cde6 .target}[[[ADIOS]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios25ADIOS5ADIOSEv "Link to this definition"){.headerlink}\

    :   Starting point for non-MPI apps. Creates an [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} object

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if user input is incorrect

    <!-- -->

    []{#_CPPv3N6adios25ADIOS5ADIOSERKNSt6stringERKNSt6stringE}[]{#_CPPv2N6adios25ADIOS5ADIOSERKNSt6stringERKNSt6stringE}[]{#adios2::ADIOS::ADIOS__ssCR.ssCR}[]{#classadios2_1_1ADIOS_1a982225656ed6697c9c550c8165fb4394 .target}[[[ADIOS]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[configFile]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[hostLanguage]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios25ADIOS5ADIOSERKNSt6stringERKNSt6stringE "Link to this definition"){.headerlink}\

    :   extra constructor for R and other languages that use the public
        C++ API but has data in column-major. Pass "" for configfile if
        there is no config file. Last bool argument exist only to ensure
        matching this signature by having different number of arguments.
        Supported languages are "R", "Matlab", "Fortran", all these
        names mean the same thing: treat all arrays column-major e.g.
        [[adios2::ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal}("", "Fortran", false);

    <!-- -->

    []{#_CPPv3NK6adios25ADIOScvbEv}[]{#_CPPv2NK6adios25ADIOScvbEv}[]{#adios2::ADIOS::castto-b-operatorC}[]{#classadios2_1_1ADIOS_1a5c377afbd2748a9aea329237cbd78c7e .target}[[explicit]{.pre}]{.k}[ ]{.w}[[[operator]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4NK6adios25ADIOScvbEv "Link to this definition"){.headerlink}\

    :   object inspection true: valid object, false: invalid object

    <!-- -->

    []{#_CPPv3N6adios25ADIOS5ADIOSERK5ADIOS}[]{#_CPPv2N6adios25ADIOS5ADIOSERK5ADIOS}[]{#adios2::ADIOS::ADIOS__ADIOSCR}[]{#classadios2_1_1ADIOS_1a95829e7cfbfed30fc4898dfbeb386b69 .target}[[[ADIOS]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[[ADIOS]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios25ADIOS5ADIOSERK5ADIOS "adios2::ADIOS::ADIOS"){.reference .internal}[[&]{.pre}]{.p}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[delete]{.pre}]{.k}[](#_CPPv4N6adios25ADIOS5ADIOSERK5ADIOS "Link to this definition"){.headerlink}\

    :   DELETED Copy Constructor. [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} is the only object that manages its own memory.
        Create a separate object for independent tasks

    <!-- -->

    []{#_CPPv3N6adios25ADIOS5ADIOSERR5ADIOS}[]{#_CPPv2N6adios25ADIOS5ADIOSERR5ADIOS}[]{#adios2::ADIOS::ADIOS__ADIOSRR}[]{#classadios2_1_1ADIOS_1acb7079fa38e8e77b81400dde53c9a16a .target}[[[ADIOS]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[ADIOS]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios25ADIOS5ADIOSERR5ADIOS "adios2::ADIOS::ADIOS"){.reference .internal}[[&]{.pre}]{.p}[[&]{.pre}]{.p}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[default]{.pre}]{.k}[](#_CPPv4N6adios25ADIOS5ADIOSERR5ADIOS "Link to this definition"){.headerlink}\

    :   default move constructor exists to allow for auto ad =
        ADIOS(...) initialization

    <!-- -->

    []{#_CPPv3N6adios25ADIOSD0Ev}[]{#_CPPv2N6adios25ADIOSD0Ev}[]{#adios2::ADIOS::~ADIOS}[]{#classadios2_1_1ADIOS_1a85fbbfacf0296693bc156a2499a52ffc .target}[[[\~ADIOS]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[default]{.pre}]{.k}[](#_CPPv4N6adios25ADIOSD0Ev "Link to this definition"){.headerlink}\

    :   MPI Collective calls MPI_Comm_free Uses RAII for all other
        members

    <!-- -->

    []{#_CPPv3N6adios25ADIOSaSERK5ADIOS}[]{#_CPPv2N6adios25ADIOSaSERK5ADIOS}[]{#adios2::ADIOS::assign-operator__ADIOSCR}[]{#classadios2_1_1ADIOS_1a7e3a5bfd5bcc113aae56927b73b5ac4b .target}[[[ADIOS]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios25ADIOSE "adios2::ADIOS"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[[operator]{.pre}]{.k}[[=]{.pre}]{.o}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[[ADIOS]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios25ADIOSE "adios2::ADIOS"){.reference .internal}[[&]{.pre}]{.p}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[delete]{.pre}]{.k}[](#_CPPv4N6adios25ADIOSaSERK5ADIOS "Link to this definition"){.headerlink}\

    :   copy assignment is forbidden for the same reason as copy
        constructor

    <!-- -->

    []{#_CPPv3N6adios25ADIOSaSERR5ADIOS}[]{#_CPPv2N6adios25ADIOSaSERR5ADIOS}[]{#adios2::ADIOS::assign-operator__ADIOSRR}[]{#classadios2_1_1ADIOS_1a843ff15b8936e39df61ceb20b25c887c .target}[[[ADIOS]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios25ADIOSE "adios2::ADIOS"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[[operator]{.pre}]{.k}[[=]{.pre}]{.o}]{.sig-name .descname}[(]{.sig-paren}[[[ADIOS]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios25ADIOSE "adios2::ADIOS"){.reference .internal}[[&]{.pre}]{.p}[[&]{.pre}]{.p}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[default]{.pre}]{.k}[](#_CPPv4N6adios25ADIOSaSERR5ADIOS "Link to this definition"){.headerlink}\

    :   move assignment is allowed, though, to be consistent with move
        constructor

    <!-- -->

    []{#_CPPv3N6adios25ADIOS9DeclareIOEKNSt6stringEK13ArrayOrdering}[]{#_CPPv2N6adios25ADIOS9DeclareIOEKNSt6stringEK13ArrayOrdering}[]{#adios2::ADIOS::DeclareIO__ssC.ArrayOrderingC}[]{#classadios2_1_1ADIOS_1a07a8931e4e0750db29cffb121a08258f .target}[[[IO]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios22IOE "adios2::IO"){.reference .internal}[ ]{.w}[[[DeclareIO]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[ArrayOrdering]{.pre}]{.n}[ ]{.w}[[ArrayOrder]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[ArrayOrdering]{.pre}]{.n}[[::]{.pre}]{.p}[[Auto]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4N6adios25ADIOS9DeclareIOEKNSt6stringEK13ArrayOrdering "Link to this definition"){.headerlink}\

    :   Declares a new [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} class object

        Parameters[:]{.colon}

        :   **name** -- unique [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal} name identifier within current [[ADIOS]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
            .internal} object

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal} with unique name is already declared

        Returns[:]{.colon}

        :   reference to newly created [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal} object inside current [[ADIOS]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
            .internal} object

    <!-- -->

    []{#_CPPv3N6adios25ADIOS4AtIOEKNSt6stringE}[]{#_CPPv2N6adios25ADIOS4AtIOEKNSt6stringE}[]{#adios2::ADIOS::AtIO__ssC}[]{#classadios2_1_1ADIOS_1a38a6a877c12be672fd7f6e795dc823aa .target}[[[IO]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios22IOE "adios2::IO"){.reference .internal}[ ]{.w}[[[AtIO]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios25ADIOS4AtIOEKNSt6stringE "Link to this definition"){.headerlink}\

    :   Retrieve an existing [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} object previously created with DeclareIO.

        Parameters[:]{.colon}

        :   **name** -- [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal} unique identifier key in current [[ADIOS]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
            .internal} object

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal} was not created with DeclareIO

        Returns[:]{.colon}

        :   if [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal} exists returns a reference to existing [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal} object inside [[ADIOS]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
            .internal}, else throws an exception. [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal} objects can't be invalid.

    <!-- -->

    []{#_CPPv3N6adios25ADIOS14DefineOperatorEKNSt6stringEKNSt6stringERK6Params}[]{#_CPPv2N6adios25ADIOS14DefineOperatorEKNSt6stringEKNSt6stringERK6Params}[]{#adios2::ADIOS::DefineOperator__ssC.ssC.ParamsCR}[]{#classadios2_1_1ADIOS_1a1f5b8c1252daac0d034063630fb471a4 .target}[[[Operator]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios28OperatorE "adios2::Operator"){.reference .internal}[ ]{.w}[[[DefineOperator]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Params]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[parameters]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Params]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv4N6adios25ADIOS14DefineOperatorEKNSt6stringEKNSt6stringERK6Params "Link to this definition"){.headerlink}\

    :   Defines an adios2 supported operator by its type.

        Parameters[:]{.colon}

        :   - **name** -- unique operator name identifier within current
              [[ADIOS]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
              .internal} object

            - **type** -- supported ADIOS2 operator type: zfp, sz

            - **parameters** -- key/value parameters at the operator
              object level

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if adios2 can't support current
            operator due to missing dependency or unsupported type

        Returns[:]{.colon}

        :   [[Operator]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Operator){.reference
            .internal} object

    <!-- -->

    []{#_CPPv3I0DpEN6adios25ADIOS14DefineOperatorEKNSt6stringERKNSt8functionIF1RDp4ArgsEEERK6Params}[]{#_CPPv2I0DpEN6adios25ADIOS14DefineOperatorEKNSt6stringERKNSt8functionIF1RDp4ArgsEEERK6Params}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[R]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[class]{.pre}]{.k}[ ]{.w}[[\...]{.pre}]{.p}[[[Args]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1ADIOS_1a7530f0911887ee92de57cab5919233a5 .target}[[[Operator]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios28OperatorE "adios2::Operator"){.reference .internal}[ ]{.w}[[[DefineOperator]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[function]{.pre}]{.n}[[\<]{.pre}]{.p}[[[R]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0DpEN6adios25ADIOS14DefineOperatorE8OperatorKNSt6stringERKNSt8functionIF1RDp4ArgsEEERK6Params "adios2::ADIOS::DefineOperator::R"){.reference .internal}[[(]{.pre}]{.p}[[[Args]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0DpEN6adios25ADIOS14DefineOperatorE8OperatorKNSt6stringERKNSt8functionIF1RDp4ArgsEEERK6Params "adios2::ADIOS::DefineOperator::Args"){.reference .internal}[[\...]{.pre}]{.p}[[)]{.pre}]{.p}[[\>]{.pre}]{.p}[ ]{.w}[[&]{.pre}]{.p}[[function]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Params]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[parameters]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Params]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv4I0DpEN6adios25ADIOS14DefineOperatorE8OperatorKNSt6stringERKNSt8functionIF1RDp4ArgsEEERK6Params "Link to this definition"){.headerlink}\

    :   Defines an adios2 supported operator by its type. Variadic
        template version for Operators of type Callback function with
        signatures suported in ADIOS2. For new signature support open an
        issue on github.

        Parameters[:]{.colon}

        :   - **name** -- unique operator name within [[ADIOS]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
              .internal} object

            - **function** -- C++11 callable target

            - **parameters** -- key/value parameters at the operator
              level

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if adios2 can't support current
            operator due to missing dependency or unsupported type

        Returns[:]{.colon}

        :   [[Operator]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Operator){.reference
            .internal} object

    <!-- -->

    []{#_CPPv3N6adios25ADIOS15InquireOperatorEKNSt6stringE}[]{#_CPPv2N6adios25ADIOS15InquireOperatorEKNSt6stringE}[]{#adios2::ADIOS::InquireOperator__ssC}[]{#classadios2_1_1ADIOS_1a05a9fa4cd4cd82e16002c1308ac04a24 .target}[[[Operator]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios28OperatorE "adios2::Operator"){.reference .internal}[ ]{.w}[[[InquireOperator]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios25ADIOS15InquireOperatorEKNSt6stringE "Link to this definition"){.headerlink}\

    :   Retrieve an existing [[Operator]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Operator){.reference
        .internal} object in current [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} object

        Parameters[:]{.colon}

        :   **name** -- [[Operator]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Operator){.reference
            .internal} unique identifier key in current [[ADIOS]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
            .internal} object

        Returns[:]{.colon}

        :   object to an existing operator in current [[ADIOS]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
            .internal} object, [[Operator]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Operator){.reference
            .internal} object is false if name is not found

    <!-- -->

    []{#_CPPv3N6adios25ADIOS8FlushAllEv}[]{#_CPPv2N6adios25ADIOS8FlushAllEv}[]{#adios2::ADIOS::FlushAll}[]{#classadios2_1_1ADIOS_1af42aa13fdf9e28bc7043eafd9cde4265 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[FlushAll]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios25ADIOS8FlushAllEv "Link to this definition"){.headerlink}\

    :   Flushes all engines in write mode in all IOs created with the
        current [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} object. If no [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} or [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} exist, it does nothing.

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[runtime_error]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if any engine Flush fails

    <!-- -->

    []{#_CPPv3N6adios25ADIOS8RemoveIOEKNSt6stringE}[]{#_CPPv2N6adios25ADIOS8RemoveIOEKNSt6stringE}[]{#adios2::ADIOS::RemoveIO__ssC}[]{#classadios2_1_1ADIOS_1a9ea488223cfe308ce13d1500a96a1cea .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[RemoveIO]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios25ADIOS8RemoveIOEKNSt6stringE "Link to this definition"){.headerlink}\

    :   DANGER ZONE: removes a particular [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal}. This will effectively eliminate any parameter from
        the config.xml file

        Parameters[:]{.colon}

        :   **name** -- io input name

        Returns[:]{.colon}

        :   true: [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal} was found and removed, false: [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal} not found and not removed

    <!-- -->

    []{#_CPPv3N6adios25ADIOS12RemoveAllIOsEv}[]{#_CPPv2N6adios25ADIOS12RemoveAllIOsEv}[]{#adios2::ADIOS::RemoveAllIOs}[]{#classadios2_1_1ADIOS_1a6df0835b3e72cffa744ea083b8d65fe7 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[RemoveAllIOs]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4N6adios25ADIOS12RemoveAllIOsEv "Link to this definition"){.headerlink}\

    :   DANGER ZONE: removes all IOs created with DeclareIO. This will
        effectively eliminate any parameter from the config.xml file
        also.

    <!-- -->

    []{#_CPPv3N6adios25ADIOS21EnterComputationBlockEv}[]{#_CPPv2N6adios25ADIOS21EnterComputationBlockEv}[]{#adios2::ADIOS::EnterComputationBlock}[]{#classadios2_1_1ADIOS_1ad480f67987812d8654455aa862fa2c86 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[EnterComputationBlock]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4N6adios25ADIOS21EnterComputationBlockEv "Link to this definition"){.headerlink}\

    :   Inform [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} about entering communication-free computation block
        in main thread. Useful when using Async [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal}

    <!-- -->

    []{#_CPPv3N6adios25ADIOS20ExitComputationBlockEv}[]{#_CPPv2N6adios25ADIOS20ExitComputationBlockEv}[]{#adios2::ADIOS::ExitComputationBlock}[]{#classadios2_1_1ADIOS_1a8df10ae92e7bcb64d0ad8b55e2f49be3 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[ExitComputationBlock]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4N6adios25ADIOS20ExitComputationBlockEv "Link to this definition"){.headerlink}\

    :   Inform [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} about exiting communication-free computation block in
        main thread. Useful when using Async [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal}
    :::
:::

::: {#io-class .section}
#### [[IO]{.std .std-ref}](#document-components/components#io){.reference .internal} class[](#io-class "Link to this heading"){.headerlink}

[]{#_CPPv3N6adios22IOE}[]{#_CPPv2N6adios22IOE}[]{#adios2::IO}[]{#classadios2_1_1IO .target}[[class]{.pre}]{.k}[ ]{.w}[[[IO]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios22IOE "Link to this definition"){.headerlink}\

:   ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N6adios22IO2IOEv}[]{#_CPPv2N6adios22IO2IOEv}[]{#adios2::IO::IO}[]{#classadios2_1_1IO_1a71f49fbe3f5250d9752e53084dc006ea .target}[[[IO]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[default]{.pre}]{.k}[](#_CPPv4N6adios22IO2IOEv "Link to this definition"){.headerlink}\

    :   Empty (default) constructor, use it as a placeholder for future
        [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} objects from ADIOS::IO functions. Can be used with
        STL containers.

    <!-- -->

    []{#_CPPv3N6adios22IOD0Ev}[]{#_CPPv2N6adios22IOD0Ev}[]{#adios2::IO::~IO}[]{#classadios2_1_1IO_1a7362e44331f6d812b15d8f5e8ac72802 .target}[[[\~IO]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[default]{.pre}]{.k}[](#_CPPv4N6adios22IOD0Ev "Link to this definition"){.headerlink}\

    :   Use RAII

    <!-- -->

    []{#_CPPv3NK6adios22IOcvbEv}[]{#_CPPv2NK6adios22IOcvbEv}[]{#adios2::IO::castto-b-operatorC}[]{#classadios2_1_1IO_1ad5169b890cb5033a6d93045e5879f451 .target}[[explicit]{.pre}]{.k}[ ]{.w}[[[operator]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4NK6adios22IOcvbEv "Link to this definition"){.headerlink}\

    :   true: valid object, false: invalid object

    <!-- -->

    []{#_CPPv3NK6adios22IO4NameEv}[]{#_CPPv2NK6adios22IO4NameEv}[]{#adios2::IO::NameC}[]{#classadios2_1_1IO_1ae986a59c014c5e1e929786c3714d607b .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[Name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios22IO4NameEv "Link to this definition"){.headerlink}\

    :   Inspects [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} name

        Returns[:]{.colon}

        :   name

    <!-- -->

    []{#_CPPv3NK6adios22IO12InConfigFileEv}[]{#_CPPv2NK6adios22IO12InConfigFileEv}[]{#adios2::IO::InConfigFileC}[]{#classadios2_1_1IO_1aabbd73fe20b7821261e5d16a0def7070 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[InConfigFile]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios22IO12InConfigFileEv "Link to this definition"){.headerlink}\

    :   Checks if [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} exists in a config file passed to [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} object that created this [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal}.

        Returns[:]{.colon}

        :   true: in config file, false: not in config file

    <!-- -->

    []{#_CPPv3N6adios22IO9SetEngineEKNSt6stringE}[]{#_CPPv2N6adios22IO9SetEngineEKNSt6stringE}[]{#adios2::IO::SetEngine__ssC}[]{#classadios2_1_1IO_1ab82422e9f57672943053e6cf02a59e0c .target}[[void]{.pre}]{.kt}[ ]{.w}[[[SetEngine]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[engineType]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios22IO9SetEngineEKNSt6stringE "Link to this definition"){.headerlink}\

    :   Sets the engine type for current [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} object.

        Parameters[:]{.colon}

        :   **engineType** -- predefined engine type, default is bpfile

    <!-- -->

    []{#_CPPv3N6adios22IO12SetParameterEKNSt6stringEKNSt6stringE}[]{#_CPPv2N6adios22IO12SetParameterEKNSt6stringEKNSt6stringE}[]{#adios2::IO::SetParameter__ssC.ssC}[]{#classadios2_1_1IO_1a6f59501b5054cd50c63778232240dd3a .target}[[void]{.pre}]{.kt}[ ]{.w}[[[SetParameter]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[key]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios22IO12SetParameterEKNSt6stringEKNSt6stringE "Link to this definition"){.headerlink}\

    :   Sets a single parameter. Overwrites value if key exists;.

        Parameters[:]{.colon}

        :   - **key** -- parameter key

            - **value** -- parameter value

    <!-- -->

    []{#_CPPv3N6adios22IO13SetParametersERKN6adios26ParamsE}[]{#_CPPv2N6adios22IO13SetParametersERKN6adios26ParamsE}[]{#adios2::IO::SetParameters__adios2::ParamsCR}[]{#classadios2_1_1IO_1a7b7145cd6eec6e5e2ad95da94181b041 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[SetParameters]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Params]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[parameters]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Params]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv4N6adios22IO13SetParametersERKN6adios26ParamsE "Link to this definition"){.headerlink}\

    :   Version that passes a map to fill out parameters initializer
        list = { "param1", "value1" }, {"param2", "value2"}, Replaces
        any existing parameter. Otherwise use SetParameter for adding
        new parameters.

        Parameters[:]{.colon}

        :   **parameters** -- adios::Params = std::map\<std::string,
            std::string\> key/value parameters

    <!-- -->

    []{#_CPPv3N6adios22IO13SetParametersERKNSt6stringE}[]{#_CPPv2N6adios22IO13SetParametersERKNSt6stringE}[]{#adios2::IO::SetParameters__ssCR}[]{#classadios2_1_1IO_1a6139de04465fe9113d00b08ee9702ee5 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[SetParameters]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[parameters]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios22IO13SetParametersERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Version that passes a single string to fill out many parameters.
        Replaces any existing parameter. initializer string =
        "param1=value1 , param2 = value2".

    <!-- -->

    []{#_CPPv3N6adios22IO15ClearParametersEv}[]{#_CPPv2N6adios22IO15ClearParametersEv}[]{#adios2::IO::ClearParameters}[]{#classadios2_1_1IO_1a17892076c616b9b6399ba6cdee08ecc2 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[ClearParameters]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios22IO15ClearParametersEv "Link to this definition"){.headerlink}\

    :   Remove all existing parameters. Replaces any existing parameter.
        initializer string = "param1=value1 , param2 = value2".

    <!-- -->

    []{#_CPPv3NK6adios22IO10ParametersEv}[]{#_CPPv2NK6adios22IO10ParametersEv}[]{#adios2::IO::ParametersC}[]{#classadios2_1_1IO_1af7d36bd115182880d2ff77aa504fce40 .target}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Params]{.pre}]{.n}[ ]{.w}[[[Parameters]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios22IO10ParametersEv "Link to this definition"){.headerlink}\

    :   Return current parameters set from either
        SetParameters/SetParameter functions or from config XML for
        currrent [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} object

        Returns[:]{.colon}

        :   string key/value map of current parameters (not modifiable)

    <!-- -->

    []{#_CPPv3N6adios22IO12AddTransportEKNSt6stringERKN6adios26ParamsE}[]{#_CPPv2N6adios22IO12AddTransportEKNSt6stringERKN6adios26ParamsE}[]{#adios2::IO::AddTransport__ssC.adios2::ParamsCR}[]{#classadios2_1_1IO_1ad8490bb670d635728509cc35740a75a2 .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[AddTransport]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Params]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[parameters]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Params]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv4N6adios22IO12AddTransportEKNSt6stringERKN6adios26ParamsE "Link to this definition"){.headerlink}\

    :   Adds a transport and its parameters to current [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal}. Must be supported by current [[EngineType()]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO_1a8761214bb6268541d53e5b0bb6f5b3c8){.reference
        .internal}.

        Parameters[:]{.colon}

        :   - **type** -- must be a supported transport type for a
              particular [[Engine]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
              .internal}. CAN'T use the keywords "Transport" or
              "transport"

            - **parameters** -- acceptable parameters for a particular
              transport

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if type=transport

        Returns[:]{.colon}

        :   transportIndex handler

    <!-- -->

    []{#_CPPv3N6adios22IO21SetTransportParameterEK6size_tKNSt6stringEKNSt6stringE}[]{#_CPPv2N6adios22IO21SetTransportParameterEK6size_tKNSt6stringEKNSt6stringE}[]{#adios2::IO::SetTransportParameter__sC.ssC.ssC}[]{#classadios2_1_1IO_1a7dd486b3b4395d22f0e3e572e109619f .target}[[void]{.pre}]{.kt}[ ]{.w}[[[SetTransportParameter]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[transportIndex]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[key]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios22IO21SetTransportParameterEK6size_tKNSt6stringEKNSt6stringE "Link to this definition"){.headerlink}\

    :   Sets a single parameter to an existing transport identified with
        a transportIndex handler from AddTransport. Overwrites existing
        parameter with the same key.

        Parameters[:]{.colon}

        :   - **transportIndex** -- index handler from AddTransport

            - **key** -- parameter key

            - **value** -- parameter value

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if transportIndex not valid, e.g. not a
            handler from AddTransport.

    <!-- -->

    []{#_CPPv3I0EN6adios22IO14DefineVariableERKNSt6stringERK4DimsRK4DimsRK4DimsKb}[]{#_CPPv2I0EN6adios22IO14DefineVariableERKNSt6stringERK4DimsRK4DimsRK4DimsKb}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1IO_1ade9b780ce1420167fb870612a6e0f14f .target}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios22IO14DefineVariableE8VariableI1TERKNSt6stringERK4DimsRK4DimsRK4DimsKb "adios2::IO::DefineVariable::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[DefineVariable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[shape]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Dims]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[start]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Dims]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[count]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Dims]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[constantDims]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[false]{.pre}]{.k}[)]{.sig-paren}[](#_CPPv4I0EN6adios22IO14DefineVariableE8VariableI1TERKNSt6stringERK4DimsRK4DimsRK4DimsKb "Link to this definition"){.headerlink}\

    :   Define a [[Variable\<T\>]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} object within [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal}

        Parameters[:]{.colon}

        :   - **name** -- unique variable identifier

            - **shape** -- global dimension

            - **start** -- local offset

            - **count** -- local dimension

            - **constantDims** -- true: shape, start, count won't
              change, false: shape, start, count will change after
              definition

        Returns[:]{.colon}

        :   [[Variable\<T\>]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
            .internal} object

    <!-- -->

    []{#_CPPv3I0EN6adios22IO15InquireVariableERKNSt6stringE}[]{#_CPPv2I0EN6adios22IO15InquireVariableERKNSt6stringE}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1IO_1a2abac19c9ede16e8955550444c1b2e70 .target}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios22IO15InquireVariableE8VariableI1TERKNSt6stringE "adios2::IO::InquireVariable::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[InquireVariable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4I0EN6adios22IO15InquireVariableE8VariableI1TERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Retrieve a [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} object within current [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} object

        Parameters[:]{.colon}

        :   **name** -- unique variable identifier within [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal} object

        Returns[:]{.colon}

        :   if found [[Variable]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
            .internal} object is true and has functionality, else false
            and has no functionality

    <!-- -->

    []{#_CPPv3NK6adios22IO19InquireVariableTypeERKNSt6stringE}[]{#_CPPv2NK6adios22IO19InquireVariableTypeERKNSt6stringE}[]{#adios2::IO::InquireVariableType__ssCRC}[]{#classadios2_1_1IO_1a18c579a1609fa358ace4d01fd5ee0f1d .target}[[DataType]{.pre}]{.n}[ ]{.w}[[[InquireVariableType]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4NK6adios22IO19InquireVariableTypeERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Returns the type of an existing variable as an string.

        Parameters[:]{.colon}

        :   **name** -- input variable name

        Returns[:]{.colon}

        :   type primitive type

    <!-- -->

    []{#_CPPv3I0EN6adios22IO15DefineAttributeERKNSt6stringEPK1TK6size_tRKNSt6stringEKNSt6stringEKb}[]{#_CPPv2I0EN6adios22IO15DefineAttributeERKNSt6stringEPK1TK6size_tRKNSt6stringEKNSt6stringEKb}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1IO_1ab750e7c7b8a89f24352d68c399e6aefd .target}[[[Attribute]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios29AttributeE "adios2::Attribute"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios22IO15DefineAttributeE9AttributeI1TERKNSt6stringEPK1TK6size_tRKNSt6stringEKNSt6stringEKb "adios2::IO::DefineAttribute::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[DefineAttribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios22IO15DefineAttributeE9AttributeI1TERKNSt6stringEPK1TK6size_tRKNSt6stringEKNSt6stringEKb "adios2::IO::DefineAttribute::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"\"]{.pre}]{.s}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[separator]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"/\"]{.pre}]{.s}, [[const]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[allowModification]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[false]{.pre}]{.k}[)]{.sig-paren}[](#_CPPv4I0EN6adios22IO15DefineAttributeE9AttributeI1TERKNSt6stringEPK1TK6size_tRKNSt6stringEKNSt6stringEKb "Link to this definition"){.headerlink}\

    :   Define attribute inside io. Array input version.

        Parameters[:]{.colon}

        :   - **name** -- unique attribute identifier [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal} object or for a [[Variable]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
              .internal} if variableName is not empty (associated to a
              variable)

            - **data** -- pointer to user data

            - **size** -- number of data elements

            - **variableName** -- default is empty, if not empty
              attributes is associated to a variable

            - **separator** -- default is "/", hierarchy between
              variable name and attribute, e.g. variableName/attribute1,
              variableName::attribute1. Not used if variableName is
              empty.

            - **allowModification** -- true allows redefining existing
              attribute

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if [[Attribute]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Attribute){.reference
            .internal} with unique name (in [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal} or [[Variable]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
            .internal}) is already defined

        Returns[:]{.colon}

        :   object reference to internal [[Attribute]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Attribute){.reference
            .internal} in [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal}

    <!-- -->

    []{#_CPPv3I0EN6adios22IO15DefineAttributeERKNSt6stringERK1TRKNSt6stringEKNSt6stringEKb}[]{#_CPPv2I0EN6adios22IO15DefineAttributeERKNSt6stringERK1TRKNSt6stringEKNSt6stringEKb}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1IO_1a9951d59babbb0974619a602fb5979021 .target}[[[Attribute]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios29AttributeE "adios2::Attribute"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios22IO15DefineAttributeE9AttributeI1TERKNSt6stringERK1TRKNSt6stringEKNSt6stringEKb "adios2::IO::DefineAttribute::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[DefineAttribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios22IO15DefineAttributeE9AttributeI1TERKNSt6stringERK1TRKNSt6stringEKNSt6stringEKb "adios2::IO::DefineAttribute::T"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"\"]{.pre}]{.s}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[separator]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"/\"]{.pre}]{.s}, [[const]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[allowModification]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[false]{.pre}]{.k}[)]{.sig-paren}[](#_CPPv4I0EN6adios22IO15DefineAttributeE9AttributeI1TERKNSt6stringERK1TRKNSt6stringEKNSt6stringEKb "Link to this definition"){.headerlink}\

    :   Define single value attribute.

        Parameters[:]{.colon}

        :   - **name** -- must be unique for the [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal} object or for a [[Variable]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
              .internal} if variableName is not empty (associated to a
              variable)

            - **value** -- single data value

            - **variableName** -- default is empty, if not empty
              attributes is associated to a variable

            - **separator** -- default is "/", hierarchy between
              variable name and attribute, e.g. variableName/attribute1,
              variableName::attribute1. Not used if variableName is
              empty.

            - **allowModification** -- true allows redefining existing
              attribute

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if [[Attribute]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Attribute){.reference
            .internal} with unique name (in [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal} or [[Variable]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
            .internal}) is already defined

        Returns[:]{.colon}

        :   object reference to internal [[Attribute]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Attribute){.reference
            .internal} in [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal}

    <!-- -->

    []{#_CPPv3I0EN6adios22IO16InquireAttributeERKNSt6stringERKNSt6stringEKNSt6stringE}[]{#_CPPv2I0EN6adios22IO16InquireAttributeERKNSt6stringERKNSt6stringEKNSt6stringE}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1IO_1ad5b9717f951e35936defba8941b97b09 .target}[[[Attribute]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios29AttributeE "adios2::Attribute"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios22IO16InquireAttributeE9AttributeI1TERKNSt6stringERKNSt6stringEKNSt6stringE "adios2::IO::InquireAttribute::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[InquireAttribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"\"]{.pre}]{.s}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[separator]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"/\"]{.pre}]{.s}[)]{.sig-paren}[](#_CPPv4I0EN6adios22IO16InquireAttributeE9AttributeI1TERKNSt6stringERKNSt6stringEKNSt6stringE "Link to this definition"){.headerlink}\

    :   Retrieve an existing attribute.

        Parameters[:]{.colon}

        :   - **name** -- must be unique for the [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal} object or for a [[Variable]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
              .internal} if variableName is not empty (associated to a
              variable)

            - **variableName** -- default is empty, if not empty
              attributes is expected to be associated to a variable

            - **separator** -- default is "/", hierarchy between
              variable name and attribute, e.g. variableName/attribute1,
              variableName::attribute1. Not used if variableName is
              empty.

        Returns[:]{.colon}

        :   object reference to internal [[Attribute]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Attribute){.reference
            .internal} in [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal}, object is false if [[Attribute]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Attribute){.reference
            .internal} is not found

    <!-- -->

    []{#_CPPv3N6adios22IO14RemoveVariableERKNSt6stringE}[]{#_CPPv2N6adios22IO14RemoveVariableERKNSt6stringE}[]{#adios2::IO::RemoveVariable__ssCR}[]{#classadios2_1_1IO_1a9c391896f863f0e79be14482e10d4cd6 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[RemoveVariable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios22IO14RemoveVariableERKNSt6stringE "Link to this definition"){.headerlink}\

    :   DANGEROUS! Removes an existing [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} in current [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} object. Might create dangling objects.

        Parameters[:]{.colon}

        :   **name** -- unique [[Variable]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
            .internal} input

        Returns[:]{.colon}

        :   true: found and removed variable, false: not found, nothing
            to remove

    <!-- -->

    []{#_CPPv3N6adios22IO18RemoveAllVariablesEv}[]{#_CPPv2N6adios22IO18RemoveAllVariablesEv}[]{#adios2::IO::RemoveAllVariables}[]{#classadios2_1_1IO_1aff75d34ad8a6f9a5f8226698b08c2538 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[RemoveAllVariables]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios22IO18RemoveAllVariablesEv "Link to this definition"){.headerlink}\

    :   DANGEROUS! Removes all existing variables in current [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} object. Might create dangling objects.

    <!-- -->

    []{#_CPPv3N6adios22IO15RemoveAttributeERKNSt6stringE}[]{#_CPPv2N6adios22IO15RemoveAttributeERKNSt6stringE}[]{#adios2::IO::RemoveAttribute__ssCR}[]{#classadios2_1_1IO_1a3b7affcc38b5990b09d33038a3c1562c .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[RemoveAttribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios22IO15RemoveAttributeERKNSt6stringE "Link to this definition"){.headerlink}\

    :   DANGEROUS! Removes an existing [[Attribute]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Attribute){.reference
        .internal} in current [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} object. Might create dangling objects.

        Parameters[:]{.colon}

        :   **name** -- unique [[Attribute]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Attribute){.reference
            .internal} identifier

        Returns[:]{.colon}

        :   true: found and removed attribute, false: not found, nothing
            to remove

    <!-- -->

    []{#_CPPv3N6adios22IO19RemoveAllAttributesEv}[]{#_CPPv2N6adios22IO19RemoveAllAttributesEv}[]{#adios2::IO::RemoveAllAttributes}[]{#classadios2_1_1IO_1aa042e4da432d78c9059216355ce56a5f .target}[[void]{.pre}]{.kt}[ ]{.w}[[[RemoveAllAttributes]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios22IO19RemoveAllAttributesEv "Link to this definition"){.headerlink}\

    :   DANGEROUS! Removes all existing attributes in current [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} object. Might create dangling objects.

    <!-- -->

    []{#_CPPv3N6adios22IO4OpenERKNSt6stringEK4Mode}[]{#_CPPv2N6adios22IO4OpenERKNSt6stringEK4Mode}[]{#adios2::IO::Open__ssCR.ModeC}[]{#classadios2_1_1IO_1ade38c0fe4015f31be62accb881d96284 .target}[[[Engine]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios26EngineE "adios2::Engine"){.reference .internal}[ ]{.w}[[[Open]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[mode]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios22IO4OpenERKNSt6stringEK4Mode "Link to this definition"){.headerlink}\

    :   Open an [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} to start heavy-weight input/output operations.

        Parameters[:]{.colon}

        :   - **name** -- unique engine identifier

            - **mode** -- adios2::Mode::Write, adios2::Mode::Read,
              adios2::Mode::ReadStreaming, or adios2::Mode::Append (BP4
              only)

        Returns[:]{.colon}

        :   engine object

    <!-- -->

    []{#_CPPv3N6adios22IO12InquireGroupEc}[]{#_CPPv2N6adios22IO12InquireGroupEc}[]{#adios2::IO::InquireGroup__c}[]{#classadios2_1_1IO_1a568f069475b32b18dbeb0e1b5b1965e0 .target}[[[Group]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios25GroupE "adios2::Group"){.reference .internal}[ ]{.w}[[[InquireGroup]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[delimiter]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\'/\']{.pre}]{.sc}[)]{.sig-paren}[](#_CPPv4N6adios22IO12InquireGroupEc "Link to this definition"){.headerlink}\

    :   Return a [[Group]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Group){.reference
        .internal} object for hierarchical reading.

        Parameters[:]{.colon}

        :   - **name** -- starting path

            - **a** -- delimiter to separate groups in a string
              representation

        Returns[:]{.colon}

        :   [[Group]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Group){.reference
            .internal} object

    <!-- -->

    []{#_CPPv3N6adios22IO4OpenERKNSt6stringEK4Mode8MPI_Comm}[]{#_CPPv2N6adios22IO4OpenERKNSt6stringEK4Mode8MPI_Comm}[]{#adios2::IO::Open__ssCR.ModeC.MPI_Comm}[]{#classadios2_1_1IO_1a68a96849a826ecf5fdebaaeae6ec0438 .target}[[[Engine]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios26EngineE "adios2::Engine"){.reference .internal}[ ]{.w}[[[Open]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[MPI_Comm]{.pre}]{.n}[ ]{.w}[[comm]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios22IO4OpenERKNSt6stringEK4Mode8MPI_Comm "Link to this definition"){.headerlink}\

    :   Open an [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} to start heavy-weight input/output operations. This
        version allows passing a MPI communicator different from the one
        used in the [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} object contructor MPI Collective function as it calls
        MPI_Comm_dup

        Parameters[:]{.colon}

        :   - **name** -- unique engine identifier within [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal}

            - **mode** -- adios2::Mode::Write, adios2::Mode::Read, or
              adios2::Mode::Append (BP4 only)

            - **comm** -- new communicator other than [[ADIOS]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
              .internal} object's communicator

        Returns[:]{.colon}

        :   engine object

    <!-- -->

    []{#_CPPv3N6adios22IO4OpenERKNSt6stringEPKcK6size_t}[]{#_CPPv2N6adios22IO4OpenERKNSt6stringEPKcK6size_t}[]{#adios2::IO::Open__ssCR.cCP.sC}[]{#classadios2_1_1IO_1a1ba268d4106d6d7b4be746d4441b3a81 .target}[[[Engine]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios26EngineE "adios2::Engine"){.reference .internal}[ ]{.w}[[[Open]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[md]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[mdsize]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios22IO4OpenERKNSt6stringEPKcK6size_t "Link to this definition"){.headerlink}\

    :   Overloaded version that is specifically for a serial program
        opening a file (not stream) with ReadRandomAccess mode and
        supplying the metadata already in memory. The metadata should be
        retrieved by another program calling engine.GetMetadata() after
        opening the file.

        Parameters[:]{.colon}

        :   - **name** -- unique engine identifier within [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal} object (file name in case of File transports)

            - **md** -- file metadata residing in memory

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if [[Engine]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
            .internal} with unique name is already created with another
            Open

        Returns[:]{.colon}

        :   a reference to a derived object of the [[Engine]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
            .internal} class

    <!-- -->

    []{#_CPPv3N6adios22IO8FlushAllEv}[]{#_CPPv2N6adios22IO8FlushAllEv}[]{#adios2::IO::FlushAll}[]{#classadios2_1_1IO_1a5562a56a8748c2de5cda536ced1979bd .target}[[void]{.pre}]{.kt}[ ]{.w}[[[FlushAll]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios22IO8FlushAllEv "Link to this definition"){.headerlink}\

    :   Flushes all engines created with this [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} with the Open function

    <!-- -->

    []{#_CPPv3N6adios22IO18AvailableVariablesEb}[]{#_CPPv2N6adios22IO18AvailableVariablesEb}[]{#adios2::IO::AvailableVariables__b}[]{#classadios2_1_1IO_1a88e52883f3c8285d9605da6d75bcbe55 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[map]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[,]{.pre}]{.p}[ ]{.w}[[Params]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[[AvailableVariables]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[bool]{.pre}]{.kt}[ ]{.w}[[namesOnly]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[false]{.pre}]{.k}[)]{.sig-paren}[](#_CPPv4N6adios22IO18AvailableVariablesEb "Link to this definition"){.headerlink}\

    :   Returns a map with variable information.

        - key: variable name

        - value: Params is a map\<string,string\>

          - key: "Type", "Shape", "AvailableStepsCount", "Min", "Max",
            "SingleValue"

        value: variable info value as string

        Parameters[:]{.colon}

        :   **namesOnly** -- returns a map with the variable names but
            with no Parameters. Use this if you only need the list of
            variable names and call [[VariableType()]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO_1a59d80a865b4c41981b50e35213680980){.reference
            .internal} and [[InquireVariable()]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO_1a2abac19c9ede16e8955550444c1b2e70){.reference
            .internal} on the names individually.

        Returns[:]{.colon}

        :   map\<string, map\<string, string\>\>

    <!-- -->

    []{#_CPPv3N6adios22IO19AvailableAttributesERKNSt6stringEKNSt6stringEKb}[]{#_CPPv2N6adios22IO19AvailableAttributesERKNSt6stringEKNSt6stringEKb}[]{#adios2::IO::AvailableAttributes__ssCR.ssC.bC}[]{#classadios2_1_1IO_1a03cff6c437ee9c8d84650a82a2f08e46 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[map]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[,]{.pre}]{.p}[ ]{.w}[[Params]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[[AvailableAttributes]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"\"]{.pre}]{.s}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[separator]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"/\"]{.pre}]{.s}, [[const]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[fullNameKeys]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[false]{.pre}]{.k}[)]{.sig-paren}[](#_CPPv4N6adios22IO19AvailableAttributesERKNSt6stringEKNSt6stringEKb "Link to this definition"){.headerlink}\

    :   Returns a map with available attributes information associated
        to a particular variableName

        Parameters[:]{.colon}

        :   - **variableName** -- unique variable name associated with
              resulting attributes, if empty (default) return all
              attributes

            - **separator** -- optional name hierarchy separator (/, ::,
              \_, -, \\, etc.)

            - **fullNameKeys** -- true: return full attribute names in
              keys, false (default): return attribute names relative to
              variableName

        Returns[:]{.colon}

        :   map:

    <!-- -->

    []{#_CPPv3NK6adios22IO12VariableTypeERKNSt6stringE}[]{#_CPPv2NK6adios22IO12VariableTypeERKNSt6stringE}[]{#adios2::IO::VariableType__ssCRC}[]{#classadios2_1_1IO_1a59d80a865b4c41981b50e35213680980 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[VariableType]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios22IO12VariableTypeERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Inspects variable type. This function can be used in conjunction
        with MACROS in an else if (type == adios2::GetType\<T\>() ) {}
        loop

        Parameters[:]{.colon}

        :   **name** -- unique variable name identifier in current
            [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal}

        Returns[:]{.colon}

        :   type as in adios2::GetType\<T\>() (e.g. "double", "float"),
            empty std::string if variable not found

    <!-- -->

    []{#_CPPv3NK6adios22IO13AttributeTypeERKNSt6stringE}[]{#_CPPv2NK6adios22IO13AttributeTypeERKNSt6stringE}[]{#adios2::IO::AttributeType__ssCRC}[]{#classadios2_1_1IO_1a9deb6d7552955ee0be65db7ccea5f35d .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[AttributeType]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios22IO13AttributeTypeERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Inspects attribute type. This function can be used in
        conjunction with MACROS in an else if (type ==
        adios2::GetType\<T\>() ) {} loop

        Parameters[:]{.colon}

        :   **name** -- unique attribute name identifier in current
            [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal}

        Returns[:]{.colon}

        :   type as in adios2::GetType\<T\>() (e.g. "double", "float"),
            empty std::string if attribute not found

    <!-- -->

    []{#_CPPv3N6adios22IO12AddOperationERKNSt6stringERKNSt6stringERK6Params}[]{#_CPPv2N6adios22IO12AddOperationERKNSt6stringERKNSt6stringERK6Params}[]{#adios2::IO::AddOperation__ssCR.ssCR.ParamsCR}[]{#classadios2_1_1IO_1aadb1449d12940f04258ee94fef11e5a4 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[AddOperation]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[operatorType]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Params]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[parameters]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Params]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv4N6adios22IO12AddOperationERKNSt6stringERKNSt6stringERK6Params "Link to this definition"){.headerlink}\

    :   Adds operation and parameters to current [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} object

        Parameters[:]{.colon}

        :   - **variable** -- variable to add operator to

            - **operatorType** -- operator type to define

            - **parameters** -- key/value settings particular to the
              [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal}, not to be confused by op own parameters

    <!-- -->

    []{#_CPPv3NK6adios22IO10EngineTypeEv}[]{#_CPPv2NK6adios22IO10EngineTypeEv}[]{#adios2::IO::EngineTypeC}[]{#classadios2_1_1IO_1a8761214bb6268541d53e5b0bb6f5b3c8 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[EngineType]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios22IO10EngineTypeEv "Link to this definition"){.headerlink}\

    :   Inspect current engine type from SetEngine

        Returns[:]{.colon}

        :   current engine type
    :::
:::

::: {#variable-t-class .section}
#### [[Variable]{.std .std-ref}](#document-components/components#variable){.reference .internal} [`<T>`{.docutils .literal .notranslate}]{.pre} class[](#variable-t-class "Link to this heading"){.headerlink}

[]{#_CPPv3I0EN6adios28VariableE}[]{#_CPPv2I0EN6adios28VariableE}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
[]{#classadios2_1_1Variable .target}[[class]{.pre}]{.k}[ ]{.w}[[[Variable]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4I0EN6adios28VariableE "Link to this definition"){.headerlink}\

:   ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N6adios28Variable8VariableEv}[]{#_CPPv2N6adios28Variable8VariableEv}[]{#adios2::Variable::Variable}[]{#classadios2_1_1Variable_1abb0729e60e97a019d8eabca0789747ae .target}[[[Variable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[default]{.pre}]{.k}[](#_CPPv4N6adios28Variable8VariableEv "Link to this definition"){.headerlink}\

    :   Empty (default) constructor, use it as a placeholder for future
        variables from [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal}:DefineVariable\<T\> or [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal}:InquireVariable\<T\>. Can be used with STL
        containers.

    <!-- -->

    []{#_CPPv3N6adios28VariableD0Ev}[]{#_CPPv2N6adios28VariableD0Ev}[]{#adios2::Variable::~Variable}[]{#classadios2_1_1Variable_1a31eab2267c20c0823922dbb89fb82e10 .target}[[[\~Variable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[default]{.pre}]{.k}[](#_CPPv4N6adios28VariableD0Ev "Link to this definition"){.headerlink}\

    :   Default, using RAII STL containers

    <!-- -->

    []{#_CPPv3NK6adios28VariablecvbEv}[]{#_CPPv2NK6adios28VariablecvbEv}[]{#adios2::Variable::castto-b-operatorC}[]{#classadios2_1_1Variable_1a0a13469c8f0721a912f8c1cb3dd7997d .target}[[explicit]{.pre}]{.k}[ ]{.w}[[[operator]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4NK6adios28VariablecvbEv "Link to this definition"){.headerlink}\

    :   Checks if object is valid, e.g. if( variable ) { //..valid }

    <!-- -->

    []{#_CPPv3N6adios28Variable14StoreStatsOnlyEKb}[]{#_CPPv2N6adios28Variable14StoreStatsOnlyEKb}[]{#adios2::Variable::StoreStatsOnly__bC}[]{#classadios2_1_1Variable_1a39c536dc457bceb1da4a85089c799d4c .target}[[void]{.pre}]{.kt}[ ]{.w}[[[StoreStatsOnly]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[mode]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios28Variable14StoreStatsOnlyEKb "Link to this definition"){.headerlink}\

    :   Set the write mode of a variable

        Parameters[:]{.colon}

        :   **false** -- - write data; true - write only stats

    <!-- -->

    []{#_CPPv3N6adios28Variable14SetMemorySpaceEK11MemorySpace}[]{#_CPPv2N6adios28Variable14SetMemorySpaceEK11MemorySpace}[]{#adios2::Variable::SetMemorySpace__MemorySpaceC}[]{#classadios2_1_1Variable_1a19ac71d459a1c6e7e5867c5cf93ca62c .target}[[void]{.pre}]{.kt}[ ]{.w}[[[SetMemorySpace]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[MemorySpace]{.pre}]{.n}[ ]{.w}[[mem]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios28Variable14SetMemorySpaceEK11MemorySpace "Link to this definition"){.headerlink}\

    :   Sets the memory space for all following Puts/Gets to either host
        (default) or device

        Parameters[:]{.colon}

        :   **mem** -- memory space where Put/Get buffers are allocated

    <!-- -->

    []{#_CPPv3N6adios28Variable14GetMemorySpaceEv}[]{#_CPPv2N6adios28Variable14GetMemorySpaceEv}[]{#adios2::Variable::GetMemorySpace}[]{#classadios2_1_1Variable_1aab9f40ac5760fe9592bf863beb7f1a56 .target}[[MemorySpace]{.pre}]{.n}[ ]{.w}[[[GetMemorySpace]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios28Variable14GetMemorySpaceEv "Link to this definition"){.headerlink}\

    :   Get the memory space that was set by the application

        Returns[:]{.colon}

        :   the memory space stored in the [[Variable]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
            .internal} object

    <!-- -->

    []{#_CPPv3N6adios28Variable8SetShapeERKN6adios24DimsE}[]{#_CPPv2N6adios28Variable8SetShapeERKN6adios24DimsE}[]{#adios2::Variable::SetShape__adios2::DimsCR}[]{#classadios2_1_1Variable_1a0e30f045a7aa69fad9af79df02a1d5bb .target}[[void]{.pre}]{.kt}[ ]{.w}[[[SetShape]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[shape]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios28Variable8SetShapeERKN6adios24DimsE "Link to this definition"){.headerlink}\

    :   Set new shape, care must be taken when reading back the variable
        for different steps. Only applies to Global arrays.

        Parameters[:]{.colon}

        :   **shape** -- new shape dimensions array

    <!-- -->

    []{#_CPPv3N6adios28Variable17SetBlockSelectionEK6size_t}[]{#_CPPv2N6adios28Variable17SetBlockSelectionEK6size_t}[]{#adios2::Variable::SetBlockSelection__sC}[]{#classadios2_1_1Variable_1acbafeb3cb7c41578c8adf608efb30239 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[SetBlockSelection]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[blockID]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios28Variable17SetBlockSelectionEK6size_t "Link to this definition"){.headerlink}\

    :   Read mode only. Required for reading local variables,
        [[ShapeID()]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable_1a66deb42481e9ce88d3c58e6550abe16a){.reference
        .internal} = ShapeID::LocalArray or ShapeID::LocalValue. For
        Global Arrays it will Set the appropriate Start and Count
        Selection for the global array coordinates.

        Parameters[:]{.colon}

        :   **blockID** -- variable block index defined at write time.
            Blocks can be inspected with bpls -D variableName

    <!-- -->

    []{#_CPPv3N6adios28Variable12SetSelectionERKN6adios23BoxIN6adios24DimsEEE}[]{#_CPPv2N6adios28Variable12SetSelectionERKN6adios23BoxIN6adios24DimsEEE}[]{#adios2::Variable::SetSelection__adios2::Box:adios2::Dims:CR}[]{#classadios2_1_1Variable_1a0983b49d2675159f9159234c8aa57aa4 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[SetSelection]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Box]{.pre}]{.n}[[\<]{.pre}]{.p}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[&]{.pre}]{.p}[[selection]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios28Variable12SetSelectionERKN6adios23BoxIN6adios24DimsEEE "Link to this definition"){.headerlink}\

    :   Sets a variable selection modifying current {start, count} Count
        is the dimension from Start point

        Parameters[:]{.colon}

        :   **selection** -- input {start, count}

    <!-- -->

    []{#_CPPv3N6adios28Variable18SetMemorySelectionERKN6adios23BoxIN6adios24DimsEEE}[]{#_CPPv2N6adios28Variable18SetMemorySelectionERKN6adios23BoxIN6adios24DimsEEE}[]{#adios2::Variable::SetMemorySelection__adios2::Box:adios2::Dims:CR}[]{#classadios2_1_1Variable_1a1f9b159e3bbd4b1806d639d0aff89043 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[SetMemorySelection]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Box]{.pre}]{.n}[[\<]{.pre}]{.p}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[&]{.pre}]{.p}[[memorySelection]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[{]{.pre}]{.p}[[{]{.pre}]{.p}[[}]{.pre}]{.p}[[,]{.pre}]{.p}[ ]{.w}[[{]{.pre}]{.p}[[}]{.pre}]{.p}[[}]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv4N6adios28Variable18SetMemorySelectionERKN6adios23BoxIN6adios24DimsEEE "Link to this definition"){.headerlink}\

    :   Set the local start (offset) point to the memory pointer passed
        at Put and the memory local dimensions (count). Used for
        non-contiguous memory writes and reads (e.g. multidimensional
        ghost-cells). Currently Get only works for formats based on BP3.

        Parameters[:]{.colon}

        :   **memorySelection** -- {memoryStart, memoryCount}

    <!-- -->

    []{#_CPPv3N6adios28Variable16SetStepSelectionERKN6adios23BoxI6size_tEE}[]{#_CPPv2N6adios28Variable16SetStepSelectionERKN6adios23BoxI6size_tEE}[]{#adios2::Variable::SetStepSelection__adios2::Box:s:CR}[]{#classadios2_1_1Variable_1a884416d19586476ae7e6868229f374bd .target}[[void]{.pre}]{.kt}[ ]{.w}[[[SetStepSelection]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Box]{.pre}]{.n}[[\<]{.pre}]{.p}[[size_t]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[&]{.pre}]{.p}[[stepSelection]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios28Variable16SetStepSelectionERKN6adios23BoxI6size_tEE "Link to this definition"){.headerlink}\

    :   Sets a step selection modifying current startStep, countStep
        countStep is the number of steps from startStep point

        Parameters[:]{.colon}

        :   **stepSelection** -- input {startStep, countStep}

    <!-- -->

    []{#_CPPv3N6adios28Variable11SetAccuracyERKN6adios28AccuracyE}[]{#_CPPv2N6adios28Variable11SetAccuracyERKN6adios28AccuracyE}[]{#adios2::Variable::SetAccuracy__adios2::AccuracyCR}[]{#classadios2_1_1Variable_1aeb55f5a68adb7fadaf31b69caed7a673 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[SetAccuracy]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Accuracy]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[a]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios28Variable11SetAccuracyERKN6adios28AccuracyE "Link to this definition"){.headerlink}\

    :   Sets the requested accuracy for the next read operation. The
        actual accuracy after the read is provided in
        [[GetAccuracy()]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable_1a97b478ba49f2feb478b9d98fa78922bb){.reference
        .internal}

    <!-- -->

    []{#_CPPv3NK6adios28Variable13SelectionSizeEv}[]{#_CPPv2NK6adios28Variable13SelectionSizeEv}[]{#adios2::Variable::SelectionSizeC}[]{#classadios2_1_1Variable_1afa1e345352a2f5d8fade0c31bf9d2b06 .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[SelectionSize]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable13SelectionSizeEv "Link to this definition"){.headerlink}\

    :   Returns the number of elements required for pre-allocation based
        on current count and stepsCount

        Returns[:]{.colon}

        :   elements of type T required for pre-allocation

    <!-- -->

    []{#_CPPv3NK6adios28Variable4NameEv}[]{#_CPPv2NK6adios28Variable4NameEv}[]{#adios2::Variable::NameC}[]{#classadios2_1_1Variable_1adc9285b4ed7f5bfb50e13224d3e9001c .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[Name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable4NameEv "Link to this definition"){.headerlink}\

    :   Inspects [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} name

        Returns[:]{.colon}

        :   name

    <!-- -->

    []{#_CPPv3NK6adios28Variable4TypeEv}[]{#_CPPv2NK6adios28Variable4TypeEv}[]{#adios2::Variable::TypeC}[]{#classadios2_1_1Variable_1a50ec327dd1f6aab62cede3bb084a1d55 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[Type]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable4TypeEv "Link to this definition"){.headerlink}\

    :   Inspects [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} type

        Returns[:]{.colon}

        :   type string literal containing the type: double, float,
            unsigned int, etc.

    <!-- -->

    []{#_CPPv3NK6adios28Variable6SizeofEv}[]{#_CPPv2NK6adios28Variable6SizeofEv}[]{#adios2::Variable::SizeofC}[]{#classadios2_1_1Variable_1ae47a04ee1e260de586b99df19fa9911f .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[Sizeof]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable6SizeofEv "Link to this definition"){.headerlink}\

    :   Inspects size of the current element type, sizeof(T)

        Returns[:]{.colon}

        :   sizeof(T) for current system

    <!-- -->

    []{#_CPPv3NK6adios28Variable7ShapeIDEv}[]{#_CPPv2NK6adios28Variable7ShapeIDEv}[]{#adios2::Variable::ShapeIDC}[]{#classadios2_1_1Variable_1a66deb42481e9ce88d3c58e6550abe16a .target}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[ShapeID]{.pre}]{.n}[ ]{.w}[[[ShapeID]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable7ShapeIDEv "Link to this definition"){.headerlink}\

    :   Inspects shape id for current variable

        Returns[:]{.colon}

        :   from enum adios2::ShapeID

    <!-- -->

    []{#_CPPv3NK6adios28Variable5ShapeEK6size_t}[]{#_CPPv2NK6adios28Variable5ShapeEK6size_t}[]{#adios2::Variable::Shape__sCC}[]{#classadios2_1_1Variable_1a797ad613135d888b22d77a5417ea1f3a .target}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[[Shape]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[step]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[EngineCurrentStep]{.pre}]{.n}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable5ShapeEK6size_t "Link to this definition"){.headerlink}\

    :   Inspects shape in global variables

        Parameters[:]{.colon}

        :   **step** -- input for a particular Shape if changing over
            time. If default, either return absolute or in streaming
            mode it returns the shape for the current engine step

        Returns[:]{.colon}

        :   shape vector

    <!-- -->

    []{#_CPPv3NK6adios28Variable5StartEv}[]{#_CPPv2NK6adios28Variable5StartEv}[]{#adios2::Variable::StartC}[]{#classadios2_1_1Variable_1a071154ecb7390af228c48942d110352d .target}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[[Start]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable5StartEv "Link to this definition"){.headerlink}\

    :   Inspects current start point

        Returns[:]{.colon}

        :   start vector

    <!-- -->

    []{#_CPPv3NK6adios28Variable5CountEv}[]{#_CPPv2NK6adios28Variable5CountEv}[]{#adios2::Variable::CountC}[]{#classadios2_1_1Variable_1a3ffa347b832a121bd2d564c71da39035 .target}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[[Count]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable5CountEv "Link to this definition"){.headerlink}\

    :   Inspects current count from start

        Returns[:]{.colon}

        :   count vector

    <!-- -->

    []{#_CPPv3NK6adios28Variable5StepsEv}[]{#_CPPv2NK6adios28Variable5StepsEv}[]{#adios2::Variable::StepsC}[]{#classadios2_1_1Variable_1af4ae9612210c508c2e6b79a033a9f99a .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[Steps]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable5StepsEv "Link to this definition"){.headerlink}\

    :   For readRandomAccess mode, inspect the number of available steps

        Returns[:]{.colon}

        :   available steps

    <!-- -->

    []{#_CPPv3NK6adios28Variable10StepsStartEv}[]{#_CPPv2NK6adios28Variable10StepsStartEv}[]{#adios2::Variable::StepsStartC}[]{#classadios2_1_1Variable_1aaaf3d2d4f03195f99b82698ca11f6a23 .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[StepsStart]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable10StepsStartEv "Link to this definition"){.headerlink}\

    :   For readRandomAccess mode, inspect the start step for available
        steps

        Returns[:]{.colon}

        :   available start step

    <!-- -->

    []{#_CPPv3NK6adios28Variable7BlockIDEv}[]{#_CPPv2NK6adios28Variable7BlockIDEv}[]{#adios2::Variable::BlockIDC}[]{#classadios2_1_1Variable_1a5c40df2cc22863129692b1c0af10635e .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[BlockID]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable7BlockIDEv "Link to this definition"){.headerlink}\

    :   For read mode, retrieve current BlockID, default = 0 if not set
        with SetBlockID

        Returns[:]{.colon}

        :   current block id

    <!-- -->

    []{#_CPPv3N6adios28Variable12AddOperationEK8OperatorRKN6adios26ParamsE}[]{#_CPPv2N6adios28Variable12AddOperationEK8OperatorRKN6adios26ParamsE}[]{#adios2::Variable::AddOperation__OperatorC.adios2::ParamsCR}[]{#classadios2_1_1Variable_1aa9b262af15bbdf2f9dd450525a77813e .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[AddOperation]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[[Operator]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios28OperatorE "adios2::Operator"){.reference .internal}[ ]{.w}[[op]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Params]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[parameters]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Params]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}[)]{.sig-paren}[](#_CPPv4N6adios28Variable12AddOperationEK8OperatorRKN6adios26ParamsE "Link to this definition"){.headerlink}\

    :   Adds operation and parameters to current [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} object

        Parameters[:]{.colon}

        :   - **op** -- operator to be added

            - **parameters** -- key/value settings particular to the
              [[Variable]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
              .internal}, not to be confused by op own parameters

        Returns[:]{.colon}

        :   operation index handler in [[Operations()]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Variable_1a6986336139f374ea00ba62bcb6ca9dd2){.reference
            .internal}

    <!-- -->

    []{#_CPPv3NK6adios28Variable10OperationsEv}[]{#_CPPv2NK6adios28Variable10OperationsEv}[]{#adios2::Variable::OperationsC}[]{#classadios2_1_1Variable_1a6986336139f374ea00ba62bcb6ca9dd2 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[[Operator]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios28OperatorE "adios2::Operator"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[Operations]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable10OperationsEv "Link to this definition"){.headerlink}\

    :   Inspects current operators added with AddOperator

        Returns[:]{.colon}

        :   vector of Variable\<T\>::OperatorInfo

    <!-- -->

    []{#_CPPv3N6adios28Variable16RemoveOperationsEv}[]{#_CPPv2N6adios28Variable16RemoveOperationsEv}[]{#adios2::Variable::RemoveOperations}[]{#classadios2_1_1Variable_1af24226fb188a693e3c3ff0c38bed89ff .target}[[void]{.pre}]{.kt}[ ]{.w}[[[RemoveOperations]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios28Variable16RemoveOperationsEv "Link to this definition"){.headerlink}\

    :   Removes all current Operations associated with AddOperation.
        Provides the posibility to apply or not operators on a block
        basis.

    <!-- -->

    []{#_CPPv3NK6adios28Variable6MinMaxEK6size_t}[]{#_CPPv2NK6adios28Variable6MinMaxEK6size_t}[]{#adios2::Variable::MinMax__sCC}[]{#classadios2_1_1Variable_1a9adf35b65d6e2b3f7edbe733fc35b87c .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[pair]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable::T"){.reference .internal}[[,]{.pre}]{.p}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[MinMax]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[step]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[DefaultSizeT]{.pre}]{.n}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable6MinMaxEK6size_t "Link to this definition"){.headerlink}\

    :   Read mode only: return minimum and maximum values for current
        variable at a step. For streaming mode (BeginStep/EndStep): use
        default (leave empty) for current [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} Step At random access mode (File Engines only):
        default = absolute MinMax

        Parameters[:]{.colon}

        :   **step** -- input step

        Returns[:]{.colon}

        :   pair.first = min pair.second = max

    <!-- -->

    []{#_CPPv3NK6adios28Variable3MinEK6size_t}[]{#_CPPv2NK6adios28Variable3MinEK6size_t}[]{#adios2::Variable::Min__sCC}[]{#classadios2_1_1Variable_1a41f7dbaedeeb6bdde10cdccecdd5f050 .target}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable::T"){.reference .internal}[ ]{.w}[[[Min]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[step]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[DefaultSizeT]{.pre}]{.n}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable3MinEK6size_t "Link to this definition"){.headerlink}\

    :   Read mode only: return minimum values for current variable at a
        step. For streaming mode (within BeginStep/EndStep): use default
        (leave empty) for current [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} Step At random access mode (File Engines only):
        default = absolute MinMax

        Parameters[:]{.colon}

        :   **step** -- input step

        Returns[:]{.colon}

        :   variable minimum

    <!-- -->

    []{#_CPPv3NK6adios28Variable3MaxEK6size_t}[]{#_CPPv2NK6adios28Variable3MaxEK6size_t}[]{#adios2::Variable::Max__sCC}[]{#classadios2_1_1Variable_1a15c30f543fbbab774369aa3ac87c3468 .target}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable::T"){.reference .internal}[ ]{.w}[[[Max]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[step]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[DefaultSizeT]{.pre}]{.n}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable3MaxEK6size_t "Link to this definition"){.headerlink}\

    :   Read mode only: return minimum values for current variable at a
        step. For streaming mode (within BeginStep/EndStep): use default
        (leave empty) for current [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} Step At random access mode (File Engines only):
        default = absolute MinMax

        Parameters[:]{.colon}

        :   **step** -- input step

        Returns[:]{.colon}

        :   variable minimum

    <!-- -->

    []{#_CPPv3N6adios28Variable11GetAccuracyEv}[]{#_CPPv2N6adios28Variable11GetAccuracyEv}[]{#adios2::Variable::GetAccuracy}[]{#classadios2_1_1Variable_1a97b478ba49f2feb478b9d98fa78922bb .target}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Accuracy]{.pre}]{.n}[ ]{.w}[[[GetAccuracy]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios28Variable11GetAccuracyEv "Link to this definition"){.headerlink}\

    :   Get the provided accuracy for the last read operation. Most
        operations provide data as it was written, meaning that error is
        reported as 0.0

    <!-- -->

    []{#_CPPv3N6adios28Variable18AllStepsBlocksInfoEv}[]{#_CPPv2N6adios28Variable18AllStepsBlocksInfoEv}[]{#adios2::Variable::AllStepsBlocksInfo}[]{#classadios2_1_1Variable_1a26e7a07d1708d805338121aa5c9a25ac .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[Info]{.pre}]{.n}[[\>]{.pre}]{.p}[[\>]{.pre}]{.p}[ ]{.w}[[[AllStepsBlocksInfo]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios28Variable18AllStepsBlocksInfoEv "Link to this definition"){.headerlink}\

    :   Read mode only and random-access (no BeginStep/EndStep) with
        file engines only. Allows inspection of variable info on a per
        relative step (returned vector index) basis

        Returns[:]{.colon}

        :   first vector: relative steps, second vector: blocks info
            within a step
    :::

    []{#_CPPv3N6adios28Variable4InfoE}[]{#_CPPv2N6adios28Variable4InfoE}[]{#adios2::Variable::Info}[]{#structadios2_1_1Variable_1_1Info .target}[[struct]{.pre}]{.k}[ ]{.w}[[[Info]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios28Variable4InfoE "Link to this definition"){.headerlink}\

    :   Contains block information for a particular Variable\<T\>

        ::: {.breathe-sectiondef .docutils .container}
        Public Functions

        []{#_CPPv3NK6adios28Variable4Info4DataEv}[]{#_CPPv2NK6adios28Variable4Info4DataEv}[]{#adios2::Variable::Info::DataC}[]{#structadios2_1_1Variable_1_1Info_1a67af3e361be14bdf053c2cca51d1f676 .target}[[const]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[[Data]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Variable4Info4DataEv "Link to this definition"){.headerlink}\

        :   reference to internal block data (used by inline
            [[Engine]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
            .internal}). For deferred variables, valid pointer is not
            returned until EndStep/PerformGets has been called.
        :::

        ::: {.breathe-sectiondef .docutils .container}
        Public Members

        []{#_CPPv3N6adios28Variable4Info5StartE}[]{#_CPPv2N6adios28Variable4Info5StartE}[]{#adios2::Variable::Info::Start__adios2::Dims}[]{#structadios2_1_1Variable_1_1Info_1ad2f0f28a5db955c73f2f1b1ef76d221c .target}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[[Start]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios28Variable4Info5StartE "Link to this definition"){.headerlink}\

        :   block start

        <!-- -->

        []{#_CPPv3N6adios28Variable4Info5CountE}[]{#_CPPv2N6adios28Variable4Info5CountE}[]{#adios2::Variable::Info::Count__adios2::Dims}[]{#structadios2_1_1Variable_1_1Info_1aa4ec8292e2dd93e597810da5c2d6632f .target}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[[Count]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios28Variable4Info5CountE "Link to this definition"){.headerlink}\

        :   block count

        <!-- -->

        []{#_CPPv3N6adios28Variable4Info3MinE}[]{#_CPPv2N6adios28Variable4Info3MinE}[]{#adios2::Variable::Info::Min__IOType}[]{#structadios2_1_1Variable_1_1Info_1a187994c28437c53cb6a3e52d137d28eb .target}[[IOType]{.pre}]{.n}[ ]{.w}[[[Min]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[IOType]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}[](#_CPPv4N6adios28Variable4Info3MinE "Link to this definition"){.headerlink}\

        :   block Min, if IsValue is false

        <!-- -->

        []{#_CPPv3N6adios28Variable4Info3MaxE}[]{#_CPPv2N6adios28Variable4Info3MaxE}[]{#adios2::Variable::Info::Max__IOType}[]{#structadios2_1_1Variable_1_1Info_1a78c2ad44120addbc02d631bd515dbe56 .target}[[IOType]{.pre}]{.n}[ ]{.w}[[[Max]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[IOType]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}[](#_CPPv4N6adios28Variable4Info3MaxE "Link to this definition"){.headerlink}\

        :   block Max, if IsValue is false

        <!-- -->

        []{#_CPPv3N6adios28Variable4Info5ValueE}[]{#_CPPv2N6adios28Variable4Info5ValueE}[]{#adios2::Variable::Info::Value__IOType}[]{#structadios2_1_1Variable_1_1Info_1a7bde8f84811ccf2b9704a6f364d3ca7c .target}[[IOType]{.pre}]{.n}[ ]{.w}[[[Value]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[IOType]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}[](#_CPPv4N6adios28Variable4Info5ValueE "Link to this definition"){.headerlink}\

        :   block Value, if IsValue is true

        <!-- -->

        []{#_CPPv3N6adios28Variable4Info8WriterIDE}[]{#_CPPv2N6adios28Variable4Info8WriterIDE}[]{#adios2::Variable::Info::WriterID__i}[]{#structadios2_1_1Variable_1_1Info_1a3a6d9799ce340f18a54a8a00d6fdd819 .target}[[int]{.pre}]{.kt}[ ]{.w}[[[WriterID]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[](#_CPPv4N6adios28Variable4Info8WriterIDE "Link to this definition"){.headerlink}\

        :   WriterID, source for stream ID that produced this block

        <!-- -->

        []{#_CPPv3N6adios28Variable4Info7BlockIDE}[]{#_CPPv2N6adios28Variable4Info7BlockIDE}[]{#adios2::Variable::Info::BlockID__s}[]{#structadios2_1_1Variable_1_1Info_1a06dbc4cbbde3614ed53e0811df08a98a .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[BlockID]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[](#_CPPv4N6adios28Variable4Info7BlockIDE "Link to this definition"){.headerlink}\

        :   blockID for Block Selection

        <!-- -->

        []{#_CPPv3N6adios28Variable4Info4StepE}[]{#_CPPv2N6adios28Variable4Info4StepE}[]{#adios2::Variable::Info::Step__s}[]{#structadios2_1_1Variable_1_1Info_1a083d28a20e9315d9932a5964a55cd76a .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[Step]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[](#_CPPv4N6adios28Variable4Info4StepE "Link to this definition"){.headerlink}\

        :   block corresponding step

        <!-- -->

        []{#_CPPv3N6adios28Variable4Info13IsReverseDimsE}[]{#_CPPv2N6adios28Variable4Info13IsReverseDimsE}[]{#adios2::Variable::Info::IsReverseDims__b}[]{#structadios2_1_1Variable_1_1Info_1a09dd6d2c680a381b3f3c205f356fa2a2 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[IsReverseDims]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[false]{.pre}]{.k}[](#_CPPv4N6adios28Variable4Info13IsReverseDimsE "Link to this definition"){.headerlink}\

        :   true: Dims were swapped from column-major, false: not
            swapped

        <!-- -->

        []{#_CPPv3N6adios28Variable4Info7IsValueE}[]{#_CPPv2N6adios28Variable4Info7IsValueE}[]{#adios2::Variable::Info::IsValue__b}[]{#structadios2_1_1Variable_1_1Info_1a26fdc83fd425ef0feea5a86dec20ba15 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[IsValue]{.pre}]{.n}]{.sig-name .descname}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[false]{.pre}]{.k}[](#_CPPv4N6adios28Variable4Info7IsValueE "Link to this definition"){.headerlink}\

        :   true: value, false: array
        :::
:::

::: {#attribute-t-class .section}
#### [[Attribute]{.std .std-ref}](#document-components/components#attribute){.reference .internal} [`<T>`{.docutils .literal .notranslate}]{.pre} class[](#attribute-t-class "Link to this heading"){.headerlink}

[]{#_CPPv3I0EN6adios29AttributeE}[]{#_CPPv2I0EN6adios29AttributeE}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
[]{#classadios2_1_1Attribute .target}[[class]{.pre}]{.k}[ ]{.w}[[[Attribute]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4I0EN6adios29AttributeE "Link to this definition"){.headerlink}\

:   ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N6adios29Attribute9AttributeEv}[]{#_CPPv2N6adios29Attribute9AttributeEv}[]{#adios2::Attribute::Attribute}[]{#classadios2_1_1Attribute_1a8e0a86e056f28644b2bd9f710f2661bf .target}[[[Attribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[default]{.pre}]{.k}[](#_CPPv4N6adios29Attribute9AttributeEv "Link to this definition"){.headerlink}\

    :   Empty (default) constructor, use it as a placeholder for future
        attributes from [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal}:DefineAttribute\<T\> or [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal}:InquireAttribute\<T\>. Can be used with STL
        containers.

    <!-- -->

    []{#_CPPv3NK6adios29AttributecvbEv}[]{#_CPPv2NK6adios29AttributecvbEv}[]{#adios2::Attribute::castto-b-operatorC}[]{#classadios2_1_1Attribute_1ad14fe55d34dcecf128e362ee047bc84a .target}[[explicit]{.pre}]{.k}[ ]{.w}[[[operator]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4NK6adios29AttributecvbEv "Link to this definition"){.headerlink}\

    :   Checks if object is valid, e.g. if( attribute ) { //..valid }

    <!-- -->

    []{#_CPPv3NK6adios29Attribute4NameEv}[]{#_CPPv2NK6adios29Attribute4NameEv}[]{#adios2::Attribute::NameC}[]{#classadios2_1_1Attribute_1a1e2f8897cecc787f89da32c1547f0691 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[Name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios29Attribute4NameEv "Link to this definition"){.headerlink}\

    :   Inspect attribute name

        Returns[:]{.colon}

        :   unique name identifier

    <!-- -->

    []{#_CPPv3NK6adios29Attribute4TypeEv}[]{#_CPPv2NK6adios29Attribute4TypeEv}[]{#adios2::Attribute::TypeC}[]{#classadios2_1_1Attribute_1a871f38829e0e49ed0316b6769f1ff386 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[Type]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios29Attribute4TypeEv "Link to this definition"){.headerlink}\

    :   Inspect attribute type

        Returns[:]{.colon}

        :   type

    <!-- -->

    []{#_CPPv3NK6adios29Attribute4DataEv}[]{#_CPPv2NK6adios29Attribute4DataEv}[]{#adios2::Attribute::DataC}[]{#classadios2_1_1Attribute_1ae6463f21ded9bfda6df8fd177e19e671 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios29AttributeE "adios2::Attribute::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[Data]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios29Attribute4DataEv "Link to this definition"){.headerlink}\

    :   Inspect attribute data

        Returns[:]{.colon}

        :   data

    <!-- -->

    []{#_CPPv3NK6adios29Attribute7IsValueEv}[]{#_CPPv2NK6adios29Attribute7IsValueEv}[]{#adios2::Attribute::IsValueC}[]{#classadios2_1_1Attribute_1aa8f0ad58fce8e36c41bf202da76e72ea .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[IsValue]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios29Attribute7IsValueEv "Link to this definition"){.headerlink}\

    :   Distinguish single-value attributes from vector attributes

        Returns[:]{.colon}

        :   true if single-value, false otherwise
    :::
:::

::: {#engine-class .section}
[]{#c-11-engine-class}

#### [[Engine]{.std .std-ref}](#document-components/components#engine){.reference .internal} class[](#engine-class "Link to this heading"){.headerlink}

[]{#_CPPv3N6adios26EngineE}[]{#_CPPv2N6adios26EngineE}[]{#adios2::Engine}[]{#classadios2_1_1Engine .target}[[class]{.pre}]{.k}[ ]{.w}[[[Engine]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios26EngineE "Link to this definition"){.headerlink}\

:   ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N6adios26Engine6EngineEv}[]{#_CPPv2N6adios26Engine6EngineEv}[]{#adios2::Engine::Engine}[]{#classadios2_1_1Engine_1a90002eff2300e6c59436227a8c92dcfa .target}[[[Engine]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[default]{.pre}]{.k}[](#_CPPv4N6adios26Engine6EngineEv "Link to this definition"){.headerlink}\

    :   Empty (default) constructor, use it as a placeholder for future
        engines from [[IO::Open]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO_1ade38c0fe4015f31be62accb881d96284){.reference
        .internal}. Can be used with STL containers.

    <!-- -->

    []{#_CPPv3N6adios26EngineD0Ev}[]{#_CPPv2N6adios26EngineD0Ev}[]{#adios2::Engine::~Engine}[]{#classadios2_1_1Engine_1af0f72835f2433e003f3a641763bedd84 .target}[[[\~Engine]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[default]{.pre}]{.k}[](#_CPPv4N6adios26EngineD0Ev "Link to this definition"){.headerlink}\

    :   Using RAII STL containers only

    <!-- -->

    []{#_CPPv3NK6adios26EnginecvbEv}[]{#_CPPv2NK6adios26EnginecvbEv}[]{#adios2::Engine::castto-b-operatorC}[]{#classadios2_1_1Engine_1a4c9c75e103562eb9395fe3ace748b909 .target}[[explicit]{.pre}]{.k}[ ]{.w}[[[operator]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4NK6adios26EnginecvbEv "Link to this definition"){.headerlink}\

    :   true: valid engine, false: invalid, not created with
        [[IO::Open]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO_1ade38c0fe4015f31be62accb881d96284){.reference
        .internal} or post IO::Close

    <!-- -->

    []{#_CPPv3NK6adios26Engine4NameEv}[]{#_CPPv2NK6adios26Engine4NameEv}[]{#adios2::Engine::NameC}[]{#classadios2_1_1Engine_1ab8cdbaf522e7b47adb72a6723e169a59 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[Name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios26Engine4NameEv "Link to this definition"){.headerlink}\

    :   Inspect engine name

        Returns[:]{.colon}

        :   name from [[IO::Open]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO_1ade38c0fe4015f31be62accb881d96284){.reference
            .internal}

    <!-- -->

    []{#_CPPv3NK6adios26Engine4TypeEv}[]{#_CPPv2NK6adios26Engine4TypeEv}[]{#adios2::Engine::TypeC}[]{#classadios2_1_1Engine_1a1420251bf58831e7deae210c8970b36a .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[Type]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios26Engine4TypeEv "Link to this definition"){.headerlink}\

    :   From ADIOS2 engine type: "bpfile", "sst", "dataman",
        "insitumpi", "hdf5"

        Returns[:]{.colon}

        :   engine type as lower case string

    <!-- -->

    []{#_CPPv3NK6adios26Engine8OpenModeEv}[]{#_CPPv2NK6adios26Engine8OpenModeEv}[]{#adios2::Engine::OpenModeC}[]{#classadios2_1_1Engine_1a7ef4a2ad3b7a8db35b626d8419e46d29 .target}[[Mode]{.pre}]{.n}[ ]{.w}[[[OpenMode]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios26Engine8OpenModeEv "Link to this definition"){.headerlink}\

    :   Returns the Mode used at Open for current [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal}

        Returns[:]{.colon}

        :   

    <!-- -->

    []{#_CPPv3NK6adios26Engine11GetMetadataEPPcP6size_t}[]{#_CPPv2NK6adios26Engine11GetMetadataEPPcP6size_t}[]{#adios2::Engine::GetMetadata__cPP.sPC}[]{#classadios2_1_1Engine_1a9f676c8665a72e2eafae623dac4f0fef .target}[[void]{.pre}]{.kt}[ ]{.w}[[[GetMetadata]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[md]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios26Engine11GetMetadataEPPcP6size_t "Link to this definition"){.headerlink}\

    :   Serialize all metadata right after engine is created, which can
        be delivered to other processes to open the same file for
        reading without opening and reading in metadata again.

        Returns[:]{.colon}

        :   metadata (pointer to allocated memory) and size of metadata
            the pointer must be deallocated by user using free()

    <!-- -->

    []{#_CPPv3N6adios26Engine9BeginStepEv}[]{#_CPPv2N6adios26Engine9BeginStepEv}[]{#adios2::Engine::BeginStep}[]{#classadios2_1_1Engine_1ac7b3af5c0cdd728bc4050d5d9de18ff9 .target}[[StepStatus]{.pre}]{.n}[ ]{.w}[[[BeginStep]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios26Engine9BeginStepEv "Link to this definition"){.headerlink}\

    :   Begin a logical adios2 step, overloaded version with
        timeoutSeconds = 0 and mode = Read Check each engine
        documentation for MPI collective/non-collective behavior.

        Returns[:]{.colon}

        :   current step status

    <!-- -->

    []{#_CPPv3N6adios26Engine9BeginStepEK8StepModeKf}[]{#_CPPv2N6adios26Engine9BeginStepEK8StepModeKf}[]{#adios2::Engine::BeginStep__StepModeC.floatC}[]{#classadios2_1_1Engine_1aba34392ebedef0fd4b3c1336aeee8a55 .target}[[StepStatus]{.pre}]{.n}[ ]{.w}[[[BeginStep]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[StepMode]{.pre}]{.n}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[float]{.pre}]{.kt}[ ]{.w}[[timeoutSeconds]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[-]{.pre}]{.o}[[1.f]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4N6adios26Engine9BeginStepEK8StepModeKf "Link to this definition"){.headerlink}\

    :   Begin a logical adios2 step, overloaded version for advanced
        stream control Check each engine documentation for MPI
        collective/non-collective behavior.

        Parameters[:]{.colon}

        :   - **mode** -- see enum adios2::StepMode for options, Read is
              the common use case

            - **timeoutSeconds** --

        Returns[:]{.colon}

        :   current step status

    <!-- -->

    []{#_CPPv3NK6adios26Engine11CurrentStepEv}[]{#_CPPv2NK6adios26Engine11CurrentStepEv}[]{#adios2::Engine::CurrentStepC}[]{#classadios2_1_1Engine_1a112d0048c7ae6a6c8d88b88d8a0db776 .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[CurrentStep]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios26Engine11CurrentStepEv "Link to this definition"){.headerlink}\

    :   Inspect current logical step

        Returns[:]{.colon}

        :   current logical step

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3PutE8VariableI1TEKbRK1T}[]{#_CPPv2I0EN6adios26Engine3PutE8VariableI1TEKbRK1T}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a5ef864459e5ab96f57680f0648049d91 .target}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3PutEN8VariableI1TE4SpanE8VariableI1TEKbRK1T "adios2::Engine::Put::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[Span]{.pre}]{.n}[ ]{.w}[[[Put]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3PutEN8VariableI1TE4SpanE8VariableI1TEKbRK1T "adios2::Engine::Put::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[initialize]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3PutEN8VariableI1TE4SpanE8VariableI1TEKbRK1T "adios2::Engine::Put::T"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3PutEN8VariableI1TE4SpanE8VariableI1TEKbRK1T "Link to this definition"){.headerlink}\

    :   Put signature that provides access to the internal engine buffer
        for a pre-allocated variable including a fill value. Returns a
        fixed size Span (based on C++20 std::span) so applications can
        populate data value after this Put and before
        PerformPuts/EndStep. Requires a call to PerformPuts, EndStep, or
        Close to extract the Min/Max bounds.

        Parameters[:]{.colon}

        :   - **variable** -- input variable

            - **initialize** -- bool flag indicating if allocated memory
              should be initialized with the provided value. Some
              engines (BP3/BP4) may initialize the allocated memory
              anyway to zero if this flag is false.

            - **value** -- provide an initial fill value

        Returns[:]{.colon}

        :   span to variable data in engine internal buffer

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3PutE8VariableI1TE}[]{#_CPPv2I0EN6adios26Engine3PutE8VariableI1TE}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a701a9d0c594329c31572f5fd49730b83 .target}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3PutEN8VariableI1TE4SpanE8VariableI1TE "adios2::Engine::Put::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[Span]{.pre}]{.n}[ ]{.w}[[[Put]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3PutEN8VariableI1TE4SpanE8VariableI1TE "adios2::Engine::Put::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3PutEN8VariableI1TE4SpanE8VariableI1TE "Link to this definition"){.headerlink}\

    :   Put signature that provides access to an internal engine buffer
        (decided by the engine) for a pre-allocated variable. Allocated
        buffer may or may not be initialized to zero by the engine (e.g.
        BP3/BP4 does, BP5 does not).

        Parameters[:]{.colon}

        :   **variable** -- input variable

        Returns[:]{.colon}

        :   span to variable data in engine internal buffer

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3PutE8VariableI1TEPK1TK4Mode}[]{#_CPPv2I0EN6adios26Engine3PutE8VariableI1TEPK1TK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a3ea393bfd27acfa72b5c1a2d0e613a81 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Put]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3PutEv8VariableI1TEPK1TK4Mode "adios2::Engine::Put::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3PutEv8VariableI1TEPK1TK4Mode "adios2::Engine::Put::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3PutEv8VariableI1TEPK1TK4Mode "Link to this definition"){.headerlink}\

    :   Put data associated with a [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} in the [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal}

        Parameters[:]{.colon}

        :   - **variable** -- contains variable metadata information

            - **data** -- user data to be associated with a variable

            - **launch** -- mode policy

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- for invalid variable or nullptr data

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3PutERKNSt6stringEPK1TK4Mode}[]{#_CPPv2I0EN6adios26Engine3PutERKNSt6stringEPK1TK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a3e5b343300989a947e8a169b17a25f64 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Put]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3PutEvRKNSt6stringEPK1TK4Mode "adios2::Engine::Put::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3PutEvRKNSt6stringEPK1TK4Mode "Link to this definition"){.headerlink}\

    :   Put data associated with a [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} in the [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} Overloaded version that accepts a variable name
        string.

        Parameters[:]{.colon}

        :   - **variableName** -- find variable by name inside
              [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal} that created this [[Engine]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
              .internal} with Open

            - **data** -- user data to be associated with a variable

            - **launch** -- mode policy

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if variable not found or nullptr data

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3PutE8VariableI1TERK1TK4Mode}[]{#_CPPv2I0EN6adios26Engine3PutE8VariableI1TERK1TK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1aa15b5bec35113a6138aeb5a0f349b540 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Put]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3PutEv8VariableI1TERK1TK4Mode "adios2::Engine::Put::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3PutEv8VariableI1TERK1TK4Mode "adios2::Engine::Put::T"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[datum]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3PutEv8VariableI1TERK1TK4Mode "Link to this definition"){.headerlink}\

    :   Put data associated with a [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} in the [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} Overloaded version that accepts r-values and single
        variable data.

        Parameters[:]{.colon}

        :   - **variable** -- contains variable metadata information

            - **datum** -- user data to be associated with a variable,
              r-value or single data value

            - **launch** -- mode policy, optional for API consistency,
              internally is always sync

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if variable is invalid or nullptr
            &datum

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3PutERKNSt6stringERK1TK4Mode}[]{#_CPPv2I0EN6adios26Engine3PutERKNSt6stringERK1TK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a3246189b25c013d13aa6a38b137e5b05 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Put]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3PutEvRKNSt6stringERK1TK4Mode "adios2::Engine::Put::T"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[datum]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3PutEvRKNSt6stringERK1TK4Mode "Link to this definition"){.headerlink}\

    :   Put data associated with a [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} in the [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} Overloaded version that accepts variables names, and
        r-values and single variable data.

        Parameters[:]{.colon}

        :   - **variableName** -- find variable by name inside
              [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal} that created this [[Engine]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
              .internal} with Open

            - **datum** -- user data to be associated with a variable
              r-value or single data value

            - **launch** -- mode policy, optional for API consistency,
              internally is always sync

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if variable is invalid or nullptr
            &datum

    <!-- -->

    []{#_CPPv3I000EN6adios26Engine3PutE8VariableI1TERK1UK4Mode}[]{#_CPPv2I000EN6adios26Engine3PutE8VariableI1TERK1UK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[[U]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[class]{.pre}]{.k}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[is_convertible]{.pre}]{.n}[[\<]{.pre}]{.p}[[[U]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I000EN6adios26Engine3PutEv8VariableI1TERK1UK4Mode "adios2::Engine::Put::U"){.reference .internal}[[,]{.pre}]{.p}[ ]{.w}[[AdiosView]{.pre}]{.n}[[\<]{.pre}]{.p}[[[U]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I000EN6adios26Engine3PutEv8VariableI1TERK1UK4Mode "adios2::Engine::Put::U"){.reference .internal}[[\>]{.pre}]{.p}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a775d6ad0c7b23acd82be2972a3473c07 .target}[[inline]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[Put]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I000EN6adios26Engine3PutEv8VariableI1TERK1UK4Mode "adios2::Engine::Put::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}, [[[U]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I000EN6adios26Engine3PutEv8VariableI1TERK1UK4Mode "adios2::Engine::Put::U"){.reference .internal}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[&]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I000EN6adios26Engine3PutEv8VariableI1TERK1UK4Mode "Link to this definition"){.headerlink}\

    :   The next two Put functions are used to accept a variable, and an
        AdiosViews which is a placeholder for Kokkos::View

        Parameters[:]{.colon}

        :   - **variable** -- contains variable metadata information

            - **data** -- represents any user defined object that is not
              a vector (used for an AdiosView)

            - **launch** -- mode policy, optional for API consistency,
              internally is always sync

    <!-- -->

    []{#_CPPv3N6adios26Engine11PerformPutsEv}[]{#_CPPv2N6adios26Engine11PerformPutsEv}[]{#adios2::Engine::PerformPuts}[]{#classadios2_1_1Engine_1abb88f0bc1cb32b2fc71ec752ce51a950 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[PerformPuts]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios26Engine11PerformPutsEv "Link to this definition"){.headerlink}\

    :   Perform all Put calls in Deferred mode up to this point.
        Specifically, this causes Deferred data to be copied into
        [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} internal buffers as if the Put had been done in Sync
        mode.

    <!-- -->

    []{#_CPPv3N6adios26Engine16PerformDataWriteEv}[]{#_CPPv2N6adios26Engine16PerformDataWriteEv}[]{#adios2::Engine::PerformDataWrite}[]{#classadios2_1_1Engine_1ad081f69b58946a6bc5a57c8d3024f32f .target}[[void]{.pre}]{.kt}[ ]{.w}[[[PerformDataWrite]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios26Engine16PerformDataWriteEv "Link to this definition"){.headerlink}\

    :   Write already-Put() array data to disk. If supported by the
        engine, this may relieve memory pressure by clearing
        [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} buffers. It is a collective call and can only be
        called between Begin/EndStep pairs.

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3GetE8VariableI1TEP1TK4Mode}[]{#_CPPv2I0EN6adios26Engine3GetE8VariableI1TEP1TK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1aa44d071e7aeeccc3761503b77321e8a2 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3GetEv8VariableI1TEP1TK4Mode "adios2::Engine::Get::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}, [[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3GetEv8VariableI1TEP1TK4Mode "adios2::Engine::Get::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3GetEv8VariableI1TEP1TK4Mode "Link to this definition"){.headerlink}\

    :   Get data associated with a [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} from the [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal}

        Parameters[:]{.colon}

        :   - **variable** -- contains variable metadata information

            - **data** -- user data to be associated with a variable, it
              must be pre-allocated

            - **launch** -- mode policy

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- for invalid variable or nullptr data

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3GetERKNSt6stringEP1TK4Mode}[]{#_CPPv2I0EN6adios26Engine3GetERKNSt6stringEP1TK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a5a622817e5bab9d8809b49041205efd9 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}, [[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3GetEvRKNSt6stringEP1TK4Mode "adios2::Engine::Get::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3GetEvRKNSt6stringEP1TK4Mode "Link to this definition"){.headerlink}\

    :   Get data associated with a [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} from the [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal}. Overloaded version to get variable by name.

        Parameters[:]{.colon}

        :   - **variableName** -- find variable by name inside
              [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal} that created this [[Engine]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
              .internal} with Open

            - **data** -- user data to be associated with a variable. It
              must be pre-allocated

            - **launch** -- mode policy

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- for invalid variableName (variable
            doesn't exist in [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal}) or nullptr data

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3GetE8VariableI1TER1TK4Mode}[]{#_CPPv2I0EN6adios26Engine3GetE8VariableI1TER1TK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a3dff56ff0f5219b93de04ce51dc746ca .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3GetEv8VariableI1TER1TK4Mode "adios2::Engine::Get::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}, [[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3GetEv8VariableI1TER1TK4Mode "adios2::Engine::Get::T"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[datum]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3GetEv8VariableI1TER1TK4Mode "Link to this definition"){.headerlink}\

    :   Get single value data associated with a [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} from the [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} Overloaded version that accepts r-values and single
        variable data.

        Parameters[:]{.colon}

        :   - **variable** -- contains variable metadata information

            - **datum** -- user data to be populated, r-value or single
              data value

            - **launch** -- mode policy, optional for API consistency,
              internally is always sync

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- if variable is invalid or nullptr
            &datum

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3GetERKNSt6stringER1TK4Mode}[]{#_CPPv2I0EN6adios26Engine3GetERKNSt6stringER1TK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a13e981bc7cb7b4abdac6639b69943de2 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}, [[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3GetEvRKNSt6stringER1TK4Mode "adios2::Engine::Get::T"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[datum]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3GetEvRKNSt6stringER1TK4Mode "Link to this definition"){.headerlink}\

    :   Get single value data associated with a [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} from the [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} Overloaded version that accepts r-values and single
        variable data.

        Parameters[:]{.colon}

        :   - **variableName** -- find variable by name inside
              [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal} that created this [[Engine]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
              .internal} with Open

            - **datum** -- user data to be populated, r-value or single
              data value

            - **launch** -- mode policy, optional for API consistency,
              internally is always sync

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- for invalid variableName (variable
            doesn't exist in [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal}) or nullptr data

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3GetE8VariableI1TERNSt6vectorI1TEEK4Mode}[]{#_CPPv2I0EN6adios26Engine3GetE8VariableI1TERNSt6vectorI1TEEK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a0aa96156b880ea968ddf97ce3e5a082c .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3GetEv8VariableI1TERNSt6vectorI1TEEK4Mode "adios2::Engine::Get::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}, [[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3GetEv8VariableI1TERNSt6vectorI1TEEK4Mode "adios2::Engine::Get::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[&]{.pre}]{.p}[[dataV]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3GetEv8VariableI1TERNSt6vectorI1TEEK4Mode "Link to this definition"){.headerlink}\

    :   Get data associated with a [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} from the [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal}. Overloaded version that accepts a std::vector
        without pre-allocation.

        Parameters[:]{.colon}

        :   - **variable** -- contains variable metadata information

            - **dataV** -- user data vector to be associated with a
              variable, it doesn't need to be pre-allocated.
              [[Engine]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
              .internal} will resize.

            - **launch** -- mode policy

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- for invalid variable

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3GetERKNSt6stringERNSt6vectorI1TEEK4Mode}[]{#_CPPv2I0EN6adios26Engine3GetERKNSt6stringERNSt6vectorI1TEEK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a28514c2c335e0956f29669ecb80e5ecd .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}, [[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3GetEvRKNSt6stringERNSt6vectorI1TEEK4Mode "adios2::Engine::Get::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[&]{.pre}]{.p}[[dataV]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3GetEvRKNSt6stringERNSt6vectorI1TEEK4Mode "Link to this definition"){.headerlink}\

    :   Get data associated with a [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} from the [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal}. Overloaded version that accepts a std::vector
        without pre-allocation.

        Parameters[:]{.colon}

        :   - **variableName** -- find variable by name inside
              [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal} that created this [[Engine]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
              .internal} with Open or BeginStep (streaming mode)

            - **dataV** -- user data vector to be associated with a
              variable, it doesn't need to be pre-allocated.
              [[Engine]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
              .internal} will resize.

            - **launch** -- mode policy

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- for invalid variableName (variable
            doesn't exist in [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal})

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3GetE8VariableI1TERN8VariableI1TE4InfoEK4Mode}[]{#_CPPv2I0EN6adios26Engine3GetE8VariableI1TERN8VariableI1TE4InfoEK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a1d8b3448b601f2e4cb4d76bb206e277b .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3GetEv8VariableI1TERN8VariableI1TE4InfoEK4Mode "adios2::Engine::Get::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}, [[typename]{.pre}]{.k}[ ]{.w}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3GetEv8VariableI1TERN8VariableI1TE4InfoEK4Mode "adios2::Engine::Get::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[Info]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[info]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3GetEv8VariableI1TERN8VariableI1TE4InfoEK4Mode "Link to this definition"){.headerlink}\

    :   Get data associated with a [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} from the [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal}. Data is associated with a block selection, and data
        is retrieved from variable's BlockInfo.

        ::: {.admonition .note}
        Note

        Preliminary, experimental API, may change soon.
        :::

        Parameters[:]{.colon}

        :   - **variable** -- contains variable metadata information

            - **info** -- block info struct associated with block
              selection, call will link with implementation's block
              info.

            - **launch** -- mode policy

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- for invalid variable or nullptr data

    <!-- -->

    []{#_CPPv3I0EN6adios26Engine3GetERKNSt6stringERN8VariableI1TE4InfoEK4Mode}[]{#_CPPv2I0EN6adios26Engine3GetERKNSt6stringERN8VariableI1TE4InfoEK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a605c4e3dd62c8673a379c2e9905cc4f7 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}, [[typename]{.pre}]{.k}[ ]{.w}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios26Engine3GetEvRKNSt6stringERN8VariableI1TE4InfoEK4Mode "adios2::Engine::Get::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[Info]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[info]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I0EN6adios26Engine3GetEvRKNSt6stringERN8VariableI1TE4InfoEK4Mode "Link to this definition"){.headerlink}\

    :   Get data associated with a [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal} from the [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal}. Data is associated with a block selection, and data
        is retrieved from variable's BlockInfo. Overloaded version to
        get variable by name.

        ::: {.admonition .note}
        Note

        Preliminary, experimental API, may change soon.
        :::

        Parameters[:]{.colon}

        :   - **variableName** -- find variable by name inside
              [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal} that created this [[Engine]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
              .internal} with Open or BeginStep (streaming mode)

            - **info** -- block info struct associated with block
              selection, call will link with implementation's block
              info.

            - **launch** -- mode policy

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- for invalid variableName (variable
            doesn't exist in [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal})

    <!-- -->

    []{#_CPPv3I0ENK6adios26Engine3GetE8VariableI1TEPP1T}[]{#_CPPv2I0ENK6adios26Engine3GetE8VariableI1TEPP1T}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a87c58e37c340c78b2598646713068107 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0ENK6adios26Engine3GetEv8VariableI1TEPP1T "adios2::Engine::Get::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}, [[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0ENK6adios26Engine3GetEv8VariableI1TEPP1T "adios2::Engine::Get::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4I0ENK6adios26Engine3GetEv8VariableI1TEPP1T "Link to this definition"){.headerlink}\

    :   Assign the value of data to the start of the internal
        [[ADIOS]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS){.reference
        .internal} buffer for variable variable. The value is
        immediately available.

    <!-- -->

    []{#_CPPv3I000EN6adios26Engine3GetE8VariableI1TERK1UK4Mode}[]{#_CPPv2I000EN6adios26Engine3GetE8VariableI1TERK1UK4Mode}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[[U]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[class]{.pre}]{.k}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[is_convertible]{.pre}]{.n}[[\<]{.pre}]{.p}[[[U]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I000EN6adios26Engine3GetEv8VariableI1TERK1UK4Mode "adios2::Engine::Get::U"){.reference .internal}[[,]{.pre}]{.p}[ ]{.w}[[AdiosView]{.pre}]{.n}[[\<]{.pre}]{.p}[[[U]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I000EN6adios26Engine3GetEv8VariableI1TERK1UK4Mode "adios2::Engine::Get::U"){.reference .internal}[[\>]{.pre}]{.p}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1ac97fb999d09ad608f0bdf14ce6e71de8 .target}[[inline]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[Get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I000EN6adios26Engine3GetEv8VariableI1TERK1UK4Mode "adios2::Engine::Get::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}, [[[U]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I000EN6adios26Engine3GetEv8VariableI1TERK1UK4Mode "adios2::Engine::Get::U"){.reference .internal}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[&]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[Mode]{.pre}]{.n}[[::]{.pre}]{.p}[[Deferred]{.pre}]{.n}[)]{.sig-paren}[](#_CPPv4I000EN6adios26Engine3GetEv8VariableI1TERK1UK4Mode "Link to this definition"){.headerlink}\

    :   The next two Get functions are used to accept a variable, and an
        AdiosViews which is a placeholder for Kokkos::View

        Parameters[:]{.colon}

        :   - **variable** -- contains variable metadata information

            - **data** -- represents any user defined object that is not
              a vector (used for an AdiosView)

            - **launch** -- mode policy, optional for API consistency,
              internally is always sync

    <!-- -->

    []{#_CPPv3N6adios26Engine11PerformGetsEv}[]{#_CPPv2N6adios26Engine11PerformGetsEv}[]{#adios2::Engine::PerformGets}[]{#classadios2_1_1Engine_1a26b8bcd4d05f4fab4f946b13279d455c .target}[[void]{.pre}]{.kt}[ ]{.w}[[[PerformGets]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios26Engine11PerformGetsEv "Link to this definition"){.headerlink}\

    :   Perform all Get calls in Deferred mode up to this point

    <!-- -->

    []{#_CPPv3N6adios26Engine7EndStepEv}[]{#_CPPv2N6adios26Engine7EndStepEv}[]{#adios2::Engine::EndStep}[]{#classadios2_1_1Engine_1af499292975bbce91be42b7462ce46688 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[EndStep]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios26Engine7EndStepEv "Link to this definition"){.headerlink}\

    :   Ends current step, by default calls PerformsPut/Get internally
        Check each engine documentation for MPI
        collective/non-collective behavior.

    <!-- -->

    []{#_CPPv3N6adios26Engine16BetweenStepPairsEv}[]{#_CPPv2N6adios26Engine16BetweenStepPairsEv}[]{#adios2::Engine::BetweenStepPairs}[]{#classadios2_1_1Engine_1a4b9519d5e0725d04b5d35a5f52e9a861 .target}[[bool]{.pre}]{.kt}[ ]{.w}[[[BetweenStepPairs]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios26Engine16BetweenStepPairsEv "Link to this definition"){.headerlink}\

    :   Returns True if engine status is between [[BeginStep()]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine_1ac7b3af5c0cdd728bc4050d5d9de18ff9){.reference
        .internal}/EndStep() pair, False otherwise.

    <!-- -->

    []{#_CPPv3N6adios26Engine5FlushEKi}[]{#_CPPv2N6adios26Engine5FlushEKi}[]{#adios2::Engine::Flush__iC}[]{#classadios2_1_1Engine_1a26397c8d4aef722b22757c5ff9733226 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Flush]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[transportIndex]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[-]{.pre}]{.o}[[1]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4N6adios26Engine5FlushEKi "Link to this definition"){.headerlink}\

    :   Manually flush to underlying transport to guarantee data is
        moved

        Parameters[:]{.colon}

        :   **transportIndex** --

    <!-- -->

    []{#_CPPv3N6adios26Engine5CloseEKi}[]{#_CPPv2N6adios26Engine5CloseEKi}[]{#adios2::Engine::Close__iC}[]{#classadios2_1_1Engine_1abd74cb7c2544dd72a2be18ab8be239a4 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[Close]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[transportIndex]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[-]{.pre}]{.o}[[1]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4N6adios26Engine5CloseEKi "Link to this definition"){.headerlink}\

    :   Closes current engine, after this call an engine becomes invalid
        MPI Collective, calls MPI_Comm_free for duplicated communicator
        at Open

        Parameters[:]{.colon}

        :   **transportIndex** --

    <!-- -->

    []{#_CPPv3I0ENK6adios26Engine18AllStepsBlocksInfoEK8VariableI1TE}[]{#_CPPv2I0ENK6adios26Engine18AllStepsBlocksInfoEK8VariableI1TE}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a9c4691f9ff25275e60a14c29ec8bfee4 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[map]{.pre}]{.n}[[\<]{.pre}]{.p}[[size_t]{.pre}]{.n}[[,]{.pre}]{.p}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0ENK6adios26Engine18AllStepsBlocksInfoENSt3mapI6size_tNSt6vectorIN8VariableI1TE4InfoEEEEEK8VariableI1TE "adios2::Engine::AllStepsBlocksInfo::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[Info]{.pre}]{.n}[[\>]{.pre}]{.p}[[\>]{.pre}]{.p}[ ]{.w}[[[AllStepsBlocksInfo]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0ENK6adios26Engine18AllStepsBlocksInfoENSt3mapI6size_tNSt6vectorIN8VariableI1TE4InfoEEEEEK8VariableI1TE "adios2::Engine::AllStepsBlocksInfo::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4I0ENK6adios26Engine18AllStepsBlocksInfoENSt3mapI6size_tNSt6vectorIN8VariableI1TE4InfoEEEEEK8VariableI1TE "Link to this definition"){.headerlink}\

    :   Extracts all available blocks information for a particular
        variable. This can be an expensive function, memory scales up
        with metadata: steps and blocks per step Valid in read mode
        only.

        Parameters[:]{.colon}

        :   **variable** --

        Returns[:]{.colon}

        :   map with all variable blocks information

    <!-- -->

    []{#_CPPv3I0ENK6adios26Engine10BlocksInfoEK8VariableI1TEK6size_t}[]{#_CPPv2I0ENK6adios26Engine10BlocksInfoEK8VariableI1TEK6size_t}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1ad81e2cafe78c1f4187f63dc00f20e819 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0ENK6adios26Engine10BlocksInfoENSt6vectorIN8VariableI1TE4InfoEEEK8VariableI1TEK6size_t "adios2::Engine::BlocksInfo::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[Info]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[[BlocksInfo]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0ENK6adios26Engine10BlocksInfoENSt6vectorIN8VariableI1TE4InfoEEEK8VariableI1TEK6size_t "adios2::Engine::BlocksInfo::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[step]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4I0ENK6adios26Engine10BlocksInfoENSt6vectorIN8VariableI1TE4InfoEEEK8VariableI1TEK6size_t "Link to this definition"){.headerlink}\

    :   Extracts all available blocks information for a particular
        variable and step. Valid in read mode only.

        Parameters[:]{.colon}

        :   - **variable** -- input variable

            - **step** -- input from which block information is
              extracted

        Returns[:]{.colon}

        :   vector of blocks with info for each block per step, if step
            not found it returns an empty vector

    <!-- -->

    []{#_CPPv3I0ENK6adios26Engine16GetAbsoluteStepsEK8VariableI1TE}[]{#_CPPv2I0ENK6adios26Engine16GetAbsoluteStepsEK8VariableI1TE}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Engine_1a0c31ba13b7bc232e2c91f111f2c320b4 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[size_t]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[[GetAbsoluteSteps]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0ENK6adios26Engine16GetAbsoluteStepsENSt6vectorI6size_tEEK8VariableI1TE "adios2::Engine::GetAbsoluteSteps::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4I0ENK6adios26Engine16GetAbsoluteStepsENSt6vectorI6size_tEEK8VariableI1TE "Link to this definition"){.headerlink}\

    :   Get the absolute steps of a variable in a file. This is for
        information purposes only, because absolute steps cannot be used
        in any ADIOS2 calls.

    <!-- -->

    []{#_CPPv3NK6adios26Engine5StepsEv}[]{#_CPPv2NK6adios26Engine5StepsEv}[]{#adios2::Engine::StepsC}[]{#classadios2_1_1Engine_1aad2ace717ba024dc5c7ad0e0a2fa0269 .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[Steps]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios26Engine5StepsEv "Link to this definition"){.headerlink}\

    :   Inspect total number of available steps, use for file engines in
        read mode only

        Returns[:]{.colon}

        :   available steps in engine

    <!-- -->

    []{#_CPPv3N6adios26Engine21LockWriterDefinitionsEv}[]{#_CPPv2N6adios26Engine21LockWriterDefinitionsEv}[]{#adios2::Engine::LockWriterDefinitions}[]{#classadios2_1_1Engine_1a3565987e14962f8793c43fb97b158ed9 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LockWriterDefinitions]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios26Engine21LockWriterDefinitionsEv "Link to this definition"){.headerlink}\

    :   Promise that no more definitions or changes to defined variables
        will occur. Useful information if called before the first
        [[EndStep()]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine_1af499292975bbce91be42b7462ce46688){.reference
        .internal} of an output [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal}, as it will know that the definitions are complete
        and constant for the entire lifetime of the output and may
        optimize metadata handling.

    <!-- -->

    []{#_CPPv3N6adios26Engine20LockReaderSelectionsEv}[]{#_CPPv2N6adios26Engine20LockReaderSelectionsEv}[]{#adios2::Engine::LockReaderSelections}[]{#classadios2_1_1Engine_1ac046bbd5efe3d1ca52ac4d2638c99600 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[LockReaderSelections]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios26Engine20LockReaderSelectionsEv "Link to this definition"){.headerlink}\

    :   Promise that the reader data selections of are fixed and will
        not change in future timesteps. This information, provided
        before the [[EndStep()]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine_1af499292975bbce91be42b7462ce46688){.reference
        .internal} representing a fixed read pattern, may be utilized by
        the input [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} to optimize data flow.
    :::
:::

::::::::::::::::::::: {#operator-class .section}
#### [[Operator]{.std .std-ref}](#document-components/components#operator){.reference .internal} class[](#operator-class "Link to this heading"){.headerlink}

[]{#_CPPv3N6adios28OperatorE}[]{#_CPPv2N6adios28OperatorE}[]{#adios2::Operator}[]{#classadios2_1_1Operator .target}[[class]{.pre}]{.k}[ ]{.w}[[[Operator]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios28OperatorE "Link to this definition"){.headerlink}\

:   ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N6adios28Operator8OperatorEv}[]{#_CPPv2N6adios28Operator8OperatorEv}[]{#adios2::Operator::Operator}[]{#classadios2_1_1Operator_1a764a574c5047577b24fedc693bed0c60 .target}[[[Operator]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[default]{.pre}]{.k}[](#_CPPv4N6adios28Operator8OperatorEv "Link to this definition"){.headerlink}\

    :   Empty (default) constructor, use it as a placeholder for future
        operators from [[ADIOS::DefineOperator]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1ADIOS_1a1f5b8c1252daac0d034063630fb471a4){.reference
        .internal} functions. Can be used with STL containers.

    <!-- -->

    []{#_CPPv3NK6adios28OperatorcvbEv}[]{#_CPPv2NK6adios28OperatorcvbEv}[]{#adios2::Operator::castto-b-operatorC}[]{#classadios2_1_1Operator_1a72659d4b8043ae92771fdfd296d1fc13 .target}[[explicit]{.pre}]{.k}[ ]{.w}[[[operator]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4NK6adios28OperatorcvbEv "Link to this definition"){.headerlink}\

    :   true: valid object, false: invalid object

    <!-- -->

    []{#_CPPv3NK6adios28Operator4TypeEv}[]{#_CPPv2NK6adios28Operator4TypeEv}[]{#adios2::Operator::TypeC}[]{#classadios2_1_1Operator_1a5ab76077cced33de99b1c45e1b65f52f .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[Type]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4NK6adios28Operator4TypeEv "Link to this definition"){.headerlink}\

    :   Inspect current [[Operator]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Operator){.reference
        .internal} type

        Returns[:]{.colon}

        :   type as string, if invalid returns an empty std::string

    <!-- -->

    []{#_CPPv3N6adios28Operator12SetParameterEKNSt6stringEKNSt6stringE}[]{#_CPPv2N6adios28Operator12SetParameterEKNSt6stringEKNSt6stringE}[]{#adios2::Operator::SetParameter__ssC.ssC}[]{#classadios2_1_1Operator_1a65379ea742a22b0351d58fa3a07de1d7 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[SetParameter]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[key]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios28Operator12SetParameterEKNSt6stringEKNSt6stringE "Link to this definition"){.headerlink}\

    :   Set a key/value parameters associated with this operator (global
        parameter from the object it's applied to: [[Variable]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
        .internal}, [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal}). If key exists, it replace the current value.

        Parameters[:]{.colon}

        :   - **key** -- parameter key

            - **value** -- parameter value

    <!-- -->

    []{#_CPPv3NK6adios28Operator10ParametersEv}[]{#_CPPv2NK6adios28Operator10ParametersEv}[]{#adios2::Operator::ParametersC}[]{#classadios2_1_1Operator_1a93852b837e30c070986e43d010378e52 .target}[[Params]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[[Parameters]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios28Operator10ParametersEv "Link to this definition"){.headerlink}\

    :   Inspect current operator parameters

        Returns[:]{.colon}

        :   map of key/value parameters
    :::

**Debugging**

For debugging, ADIOS2 C++11 class instances and enums can be passed
directly to ostreams, as well as converted to human-readable strings via
the ubiquitous [`ToString(object)`{.docutils .literal
.notranslate}]{.pre} member variable. You can also directly pass objects
to an [`ostream`{.docutils .literal .notranslate}]{.pre}.

Example:

:::: {.highlight-c++ .notranslate}
::: highlight
    auto myVar = io.DefineVariable<double>("myVar");
    std::cout << myVar << " has shape id " << myVar.ShapeID() << std::endl;

    // will print:
    // Variable<double>(Name: "myVar") has shape id ShapeID::GlobalValue

    if (myVar.ShapeID() != adios2::ShapeID::GlobalArray)
    {
        throw std::invalid_argument("can't handle " +
                                    ToString(myVar.ShapeID()) + " in " +
                                    ToString(myVar));
    }

    // will throw exception like this:
    // C++ exception with description "can't handle ShapeID::GlobalValue
    // in Variable<double>(Name: "myVar")" thrown
:::
::::

**Group API**

[]{#_CPPv3N6adios25GroupE}[]{#_CPPv2N6adios25GroupE}[]{#adios2::Group}[]{#classadios2_1_1Group .target}[[class]{.pre}]{.k}[ ]{.w}[[[Group]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios25GroupE "Link to this definition"){.headerlink}\

:   ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N6adios25Group15AvailableGroupsEv}[]{#_CPPv2N6adios25Group15AvailableGroupsEv}[]{#adios2::Group::AvailableGroups}[]{#classadios2_1_1Group_1aec361175fa18add0ee74eb149714d447 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[[AvailableGroups]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios25Group15AvailableGroupsEv "Link to this definition"){.headerlink}\

    :   returns available groups on the path set

        return vector of strings

        Param [:]{.colon}

        :   

    <!-- -->

    []{#_CPPv3N6adios25Group18AvailableVariablesEv}[]{#_CPPv2N6adios25Group18AvailableVariablesEv}[]{#adios2::Group::AvailableVariables}[]{#classadios2_1_1Group_1a0564c2ce610f91ee681e7d0949258c1e .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[[AvailableVariables]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios25Group18AvailableVariablesEv "Link to this definition"){.headerlink}\

    :   returns available variables on the path set

        return vector of strings

        Param [:]{.colon}

        :   

    <!-- -->

    []{#_CPPv3N6adios25Group19AvailableAttributesEv}[]{#_CPPv2N6adios25Group19AvailableAttributesEv}[]{#adios2::Group::AvailableAttributes}[]{#classadios2_1_1Group_1a4a6d288fe1f00efab9aca7d13466d87e .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[[\>]{.pre}]{.p}[ ]{.w}[[[AvailableAttributes]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios25Group19AvailableAttributesEv "Link to this definition"){.headerlink}\

    :   returns available attributes on the path set

        return vector of strings

        Param [:]{.colon}

        :   

    <!-- -->

    []{#_CPPv3N6adios25Group11InquirePathEv}[]{#_CPPv2N6adios25Group11InquirePathEv}[]{#adios2::Group::InquirePath}[]{#classadios2_1_1Group_1aa677d856f3a31ad15f46213428eac4c2 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[[InquirePath]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios25Group11InquirePathEv "Link to this definition"){.headerlink}\

    :   returns the current path

        return current path as a string

        Param [:]{.colon}

        :   

    <!-- -->

    []{#_CPPv3N6adios25Group7setPathENSt6stringE}[]{#_CPPv2N6adios25Group7setPathENSt6stringE}[]{#adios2::Group::setPath__ss}[]{#classadios2_1_1Group_1ac7602e682494f95c59b55350853df1c0 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[setPath]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[path]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios25Group7setPathENSt6stringE "Link to this definition"){.headerlink}\

    :   set the path, points to a particular node on the tree

        Parameters[:]{.colon}

        :   **next** -- possible path extension

    <!-- -->

    []{#_CPPv3N6adios25Group12InquireGroupENSt6stringE}[]{#_CPPv2N6adios25Group12InquireGroupENSt6stringE}[]{#adios2::Group::InquireGroup__ss}[]{#classadios2_1_1Group_1aca960e713d3c577a1e91e4e5bdf93ca9 .target}[[[Group]{.pre}]{.n}](#document-api_full/api_full#_CPPv4N6adios25GroupE "adios2::Group"){.reference .internal}[ ]{.w}[[[InquireGroup]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[group_name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios25Group12InquireGroupENSt6stringE "Link to this definition"){.headerlink}\

    :   returns a new group object

        Parameters[:]{.colon}

        :   **name** -- of the group

        Returns[:]{.colon}

        :   new group object

    <!-- -->

    []{#_CPPv3I0EN6adios25Group15InquireVariableERKNSt6stringE}[]{#_CPPv2I0EN6adios25Group15InquireVariableERKNSt6stringE}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Group_1a20f10c69bfde9276517bb55596bea816 .target}[[[Variable]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios28VariableE "adios2::Variable"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios25Group15InquireVariableE8VariableI1TERKNSt6stringE "adios2::Group::InquireVariable::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[InquireVariable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4I0EN6adios25Group15InquireVariableE8VariableI1TERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Gets an existing variable of primitive type by name. A wrapper
        for the corresponding function of the [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} class.

        Parameters[:]{.colon}

        :   **name** -- of variable to be retrieved

        Returns[:]{.colon}

        :   pointer to an existing variable in current [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal}, nullptr if not found

    <!-- -->

    []{#_CPPv3I0EN6adios25Group16InquireAttributeERKNSt6stringERKNSt6stringEKNSt6stringE}[]{#_CPPv2I0EN6adios25Group16InquireAttributeERKNSt6stringERKNSt6stringEKNSt6stringE}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1Group_1a7d745ca34e133d699f0238e2c5b15f4b .target}[[[Attribute]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios29AttributeE "adios2::Attribute"){.reference .internal}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_full/api_full#_CPPv4I0EN6adios25Group16InquireAttributeE9AttributeI1TERKNSt6stringERKNSt6stringEKNSt6stringE "adios2::Group::InquireAttribute::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[InquireAttribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"\"]{.pre}]{.s}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[separator]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"/\"]{.pre}]{.s}[)]{.sig-paren}[](#_CPPv4I0EN6adios25Group16InquireAttributeE9AttributeI1TERKNSt6stringERKNSt6stringEKNSt6stringE "Link to this definition"){.headerlink}\

    :   Gets an existing attribute of primitive type by name. A wrapper
        for the corresponding function of the [[IO]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
        .internal} class

        Parameters[:]{.colon}

        :   **name** -- of attribute to be retrieved

        Returns[:]{.colon}

        :   pointer to an existing attribute in current [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal}, nullptr if not found

    <!-- -->

    []{#_CPPv3NK6adios25Group12VariableTypeERKNSt6stringE}[]{#_CPPv2NK6adios25Group12VariableTypeERKNSt6stringE}[]{#adios2::Group::VariableType__ssCRC}[]{#classadios2_1_1Group_1a6ceb55985f530df6b246ebf1fde910c9 .target}[[DataType]{.pre}]{.n}[ ]{.w}[[[VariableType]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios25Group12VariableTypeERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Inspects variable type. This function can be used in conjunction
        with MACROS in an else if (type == adios2::GetType\<T\>() ) {}
        loop

        Parameters[:]{.colon}

        :   **name** -- unique variable name identifier in current
            [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal}

        Returns[:]{.colon}

        :   type as in adios2::GetType\<T\>() (e.g. "double", "float"),
            empty std::string if variable not found

    <!-- -->

    []{#_CPPv3NK6adios25Group13AttributeTypeERKNSt6stringE}[]{#_CPPv2NK6adios25Group13AttributeTypeERKNSt6stringE}[]{#adios2::Group::AttributeType__ssCRC}[]{#classadios2_1_1Group_1a82325644d4fcb69c635fbc6adc620f26 .target}[[DataType]{.pre}]{.n}[ ]{.w}[[[AttributeType]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[](#_CPPv4NK6adios25Group13AttributeTypeERKNSt6stringE "Link to this definition"){.headerlink}\

    :   Inspects attribute type. This function can be used in
        conjunction with MACROS in an else if (type ==
        adios2::GetType\<T\>() ) {} loop

        Parameters[:]{.colon}

        :   **name** -- unique attribute name identifier in current
            [[IO]{.std
            .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
            .internal}

        Returns[:]{.colon}

        :   type as in adios2::GetType\<T\>() (e.g. "double", "float"),
            empty std::string if attribute not found
    :::

The Group API can be used for inquiring other group objects, variables,
and attributes by reading, provided that variable and attribute names
were written in a tree-like way similar that is used in a file system:

:::: {.highlight-bash .notranslate}
::: highlight
    "group1/group2/group3/variable1"
    "group1/group2/group3/attribute1"
:::
::::

A group object containing the tree structure is obtained by the
[`InquireGroup`{.docutils .literal .notranslate}]{.pre} function of the
[`IO`{.docutils .literal .notranslate}]{.pre} object.

:::: {.highlight-c++ .notranslate}
::: highlight
    Group g = io.InquireGroup("group1");
:::
::::

Another group object can be generated by the predecessor group object.

:::: {.highlight-c++ .notranslate}
::: highlight
    Group g1 = g.InquireGroup("group2");
:::
::::

The absolute path can be inquired or set explicitly

:::: {.highlight-c++ .notranslate}
::: highlight
    std::string path =  g.InquirePath();
    g.setPath("group1/group2/group3");
:::
::::

Names of available groups, variables and attributes could be inquired:

:::: {.highlight-c++ .notranslate}
::: highlight
    std::vector<std::string> groups = g.AvailableGroups();
    std::vector<std::string> variables = g.AvailableVariables();
    std::vector<std::string> attributes = g.AvailableVariables();
:::
::::

Finally, variables can be inquired

:::: {.highlight-c++ .notranslate}
::: highlight
    auto var = g.InquireVariable("variable1");
:::
::::

An extra function is provided that returns a type of a variable

:::: {.highlight-c++ .notranslate}
::: highlight
    DataType varType  = g.VariableType("variable1");
:::
::::

**Step selection**

Steps for reading can be selected using a pre-set parameter with as a
file name as a key and a list of selected steps separated by comma as a
value.

:::: {.highlight-c++ .notranslate}
::: highlight
    io.SetParameter(filename, "1,3");
:::
::::
:::::::::::::::::::::
::::::::::::::::::::::::::::::::

:::::::::::::::::: {#fortran-bindings .section}
### Fortran bindings[](#fortran-bindings "Link to this heading"){.headerlink}

The Fortran API is a collection of subroutine calls. The first argument
is usually a Fortran type (struct) to an ADIOS2 component, while the
last argument is an error integer flag, [`integer `{.code .highlight
.fortran .docutils .literal .highlight-fortran}]{.kt}[`ierr`{.code
.highlight .fortran .docutils .literal .highlight-fortran}]{.n}.
[`ierr==0`{.docutils .literal .notranslate}]{.pre} represents successful
execution whereas a non-zero value represents an error or a different
state. ADIOS2 Fortran bindings provide a list of possible errors coming
from the C++ standardized error exception library:

:::: {.highlight-fortran .notranslate}
::: highlight
    ! error possible values for ierr
    integer, parameter :: adios2_error_none = 0
    integer, parameter :: adios2_error_invalid_argument = 1,
    integer, parameter :: adios2_error_system_error = 2,
    integer, parameter :: adios2_error_runtime_error = 3,
    integer, parameter :: adios2_error_exception = 4
:::
::::

Click here for a [Fortran write and read
example](https://github.com/ornladios/ADIOS2/blob/master/testing/adios2/bindings/fortran/TestBPWriteReadHeatMap3D.F90){.reference
.external} to illustrate the use of the APIs calls. This test will
compile under your build/bin/ directory.

The following subsections describe the overall components and
subroutines in the Fortran bindings API.

:::::: {#adios2-typed-handlers .section}
#### ADIOS2 typed handlers[](#adios2-typed-handlers "Link to this heading"){.headerlink}

ADIOS2 Fortran bindings handlers are mapped 1-to-1 to the ADIOS2
components described in the [[Components Overview]{.std
.std-ref}](#document-components/components#components-overview){.reference
.internal} section. For convenience, each type handler contains
descriptive components used for read-only inspection.

:::: {.highlight-fortran .notranslate}
::: highlight
    type(adios2_adios)     :: adios
    type(adios2_io)        :: io
    type(adios2_variable)  :: variable
    type(adios2_attribute) :: attribute
    type(adios2_engine)    :: engine

    !Read-only components for inspection and ( = defaults)

    type adios2_adios
         logical :: valid = .false.
     end type

     type adios2_io
         logical :: valid = .false.
         character(len=15):: engine_type = 'BPFile'
     end type

     type adios2_variable
         logical :: valid = .false.
         character(len=4095):: name = ''
         integer :: type = -1
         integer :: ndims = -1
     end type

     type adios2_attribute
         logical :: valid = .false.
         character(len=4095):: name = ''
         integer :: type = -1
         integer :: length = 0
     end type

     type adios2_engine
         logical :: valid = .false.
         character(len=63):: name = ''
         character(len=15):: type = ''
         integer :: mode = adios2_mode_undefined
     end type

     type adios2_operator
         logical :: valid = .false.
         character(len=63):: name = ''
         character(len=63):: type = ''
     end type
:::
::::

::: {.admonition .caution}
Caution

Use the type read-only components for information purposes only.
Changing their values directly, *e.g.* [`variable%name`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`new_name`{.docutils .literal
.notranslate}]{.pre} does not have any effect inside the ADIOS2 library
:::
::::::

:::: {#adios-subroutines .section}
#### [[ADIOS]{.std .std-ref}](#document-components/components#adios){.reference .internal} subroutines[](#adios-subroutines "Link to this heading"){.headerlink}

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_init`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} starting point for the
  ADIOS2 library

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     ! MPI versions
  >     subroutine adios2_init(adios, comm, ierr)
  >     subroutine adios2_init(adios, config_file, comm, ierr)
  >
  >     ! Non-MPI serial versions
  >     subroutine adios2_init(adios, ierr)
  >     subroutine adios2_init(adios, config_file, ierr)
  >
  >     ! WHERE:
  >
  >     ! ADIOS2 handler to allocate
  >     type(adios2_adios), intent(out):: adios
  >
  >     ! MPI Communicator
  >     integer, intent(in):: comm
  >
  >     ! Optional runtime configuration file (*.xml), see Runtime Configuration Files
  >     character*(*), intent(in) :: config_file
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_declare_io`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} spawn/create an IO
  component

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_declare_io(io, adios, io_name, ierr)
  >
  >     ! WHERE:
  >
  >     ! output ADIOS2 IO handler
  >     type(adios2_io), intent(out):: io
  >
  >     ! ADIOS2 component from adios2_init spawning io tasks
  >     type(adios2_adios), intent(in):: adios
  >
  >     ! unique name associated with this IO component inside ADIOS2
  >     character*(*), intent(in):: io_name
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_at_io`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} retrieve an existing io
  component. Useful when the original IO handler goes out of scope

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_at_io(io, adios, io_name, ierr)
  >
  >     ! WHERE:
  >
  >     ! output IO handler
  >     type(adios2_io), intent(out):: io
  >
  >     ! ADIOS2 component from adios2_init that owns IO tasks
  >     type(adios2_adios), intent(in):: adios
  >
  >     ! unique name associated with an existing IO component (created with adios2_declare_io)
  >     character*(*), intent(in):: io_name
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_define_operator`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} define an ADIOS2
  data compression/reduction operator

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_define_operator(op, adios, op_name, op_type, ierr)
  >
  >     ! WHERE
  >
  >     ! Operator handler
  >     type(adios2_operator), intent(out) :: op
  >
  >     ! ADIOS2 handler
  >     type(adios2_adios), intent(in) :: adios
  >
  >     ! Operator name
  >     character*(*), intent(in)  :: op_name
  >
  >     ! Operator type
  >     character*(*), intent(in)  :: op_type
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_inquire_operator`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} inquire an ADIOS2
  data compression/reduction operator

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_inquire_operator(op, adios, op_name, ierr)
  >
  >     ! WHERE
  >
  >     ! Operator handler
  >     type(adios2_operator), intent(out) :: op
  >
  >     ! ADIOS2 handler
  >     type(adios2_adios), intent(in) :: adios
  >
  >     ! Operator name
  >     character*(*), intent(in)  :: op_name
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_flush_all`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} flush all current engines
  in all IO objects

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_flush_all(adios, ierr)
  >
  >     ! WHERE:
  >
  >     ! ADIOS2 component from adios2_init owning IO objects and engines
  >     type(adios2_adios), intent(in):: adios
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_remove_io`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} DANGER ZONE: remove an IO
  object. This will effectively eliminate any parameter from the config
  xml file

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_remove_io(result, adios, name, ierr)
  >
  >     ! WHERE
  >
  >     ! Returns True if IO was found, False otherwise
  >     logical, intent(out):: result
  >
  >     ! ADIOS2 handler
  >     type(adios2_adios), intent(in) :: adios
  >
  >     ! IO input name
  >     character*(*), intent(in):: name
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_remove_all_ios`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} DANGER ZONE:
  remove all IO objects created for this ADIOS2 handler. This will
  effectively eliminate any parameter from the config xml file as well.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_remove_all_ios(adios, ierr)
  >
  >     ! WHERE
  >
  >     ! ADIOS2 handler
  >     type(adios2_adios), intent(in) :: adios
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_finalize`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} final point for the ADIOS2
  component

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_finalize(adios, ierr)
  >
  >     ! WHERE:
  >
  >     ! ADIOS2 handler to be deallocated
  >     type(adios2_adios), intent(in):: adios
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

::: {.admonition .caution}
Caution

Make sure that for every call to [`adios2_init`{.docutils .literal
.notranslate}]{.pre} there is a call to [`adios2_finalize`{.docutils
.literal .notranslate}]{.pre} for the same ADIOS2 handler. Not doing so
will result in memory leaks.
:::

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_enter_computation_block`{.code
  .highlight .fortran .docutils .literal .highlight-fortran}]{.n} inform
  ADIOS2 about entering communication-free computation block in main
  thread. Useful when using Async IO.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_enter_computation_block(adios, ierr)
  >
  >     ! WHERE
  >
  >     ! ADIOS2 handler
  >     type(adios2_adios), intent(in) :: adios
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_exit_computation_block`{.code
  .highlight .fortran .docutils .literal .highlight-fortran}]{.n} inform
  ADIOS2 about exiting communication-free computation block in main
  thread. Useful when using Async IO.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_exit_computation_block(adios, ierr)
  >
  >     ! WHERE
  >
  >     ! ADIOS2 handler
  >     type(adios2_adios), intent(in) :: adios
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>
::::

::: {#io-subroutines .section}
#### [[IO]{.std .std-ref}](#document-components/components#io){.reference .internal} subroutines[](#io-subroutines "Link to this heading"){.headerlink}

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_set_engine`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} set the engine type, see
  [[Supported Engines]{.std
  .std-ref}](#document-engines/engines#supported-engines){.reference
  .internal} for a list of available engines

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_set_engine(io, engine_type, ierr)
  >
  >     ! WHERE:
  >
  >     ! IO component
  >     type(adios2_io), intent(in):: io
  >
  >     ! engine_type: BP (default), HDF5, DataMan, SST, SSC
  >     character*(*), intent(in):: engine_type
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_in_config_file`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} checks if an IO
  object exists in a config file passed to ADIOS2.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_in_config_file(result, io, ierr)
  >
  >     ! WHERE
  >
  >     ! Output result to indicate whether IO exists
  >     logical, intent(out):: result
  >
  >     ! IO handler
  >     type(adios2_io), intent(in):: io
  >
  >     ! error code
  >     integer, intent(out):: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_set_parameter`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} set IO key/value
  pair parameter in an IO object, see [[Supported Engines]{.std
  .std-ref}](#document-engines/engines#supported-engines){.reference
  .internal} for a list of available parameters for each engine type

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_set_parameter(io, key, value, ierr)
  >
  >     ! WHERE:
  >
  >     ! IO component owning the attribute
  >     type(adios2_io), intent(in):: io
  >
  >     ! key in the key/value pair parameter
  >     character*(*), intent(in):: key
  >
  >     ! value in the key/value pair parameter
  >     character*(*), intent(in):: value
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_set_parameters`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} set a map of
  key/value parameters in an IO object. Replaces any existing
  parameters. Otherwise use set_parameter for adding single parameters.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_set_parameters(io, parameters, ierr)
  >
  >     ! WHERE
  >
  >     ! IO handler
  >     type(adios2_io), intent(in) :: io
  >
  >     ! Comma-separated parameter list. E.g. "Threads=2, CollectiveMetadata=OFF"
  >     character*(*), intent(in) :: parameters
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_get_parameter`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} get parameter
  value from IO object for a given parameter name

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_get_parameter(value, io, key, ierr)
  >
  >     ! WHERE
  >
  >     ! parameter value
  >     character(len=:), allocatable, intent(out) :: value
  >
  >     ! IO handler
  >     type(adios2_io), intent(in) :: io
  >
  >     ! parameter key to look for in the IO object
  >     character*(*), intent(in) :: key
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_clear_parameters`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} clear all
  parameters from the IO object

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_clear_parameters(io, ierr)
  >
  >     ! WHERE
  >
  >     ! IO handler
  >     type(adios2_io), intent(in) :: io
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_add_transport`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} add a transport
  to current IO. Must be supported by the currently used engine.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_add_transport(transport_index, io, type, ierr)
  >
  >     ! WHERE
  >
  >     ! returns a transport_index handler
  >     integer, intent(out):: transport_index
  >
  >     ! IO handler
  >     type(adios2_io), intent(in) :: io
  >
  >     ! transport type. must be supported by the engine. CAN’T use the keywords “Transport” or “transport”
  >     character*(*), intent(in) :: type
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_set_transport_parameter`{.code
  .highlight .fortran .docutils .literal .highlight-fortran}]{.n} set a
  parameter for a transport. Overwrites existing parameter with the same
  key.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_set_transport_parameter(io, transport_index, key, value, ierr)
  >
  >     ! WHERE
  >
  >     ! IO handler
  >     type(adios2_io), intent(in):: io
  >
  >     ! transport_index handler
  >     integer, intent(in):: transport_index
  >
  >     ! transport key
  >     character*(*), intent(in) :: key
  >
  >     ! transport value
  >     character*(*), intent(in) :: value
  >
  >     ! error code
  >     integer, intent(out):: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_available_variables`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} get a list of
  available variables

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_available_variables(io, namestruct, ierr)
  >
  >     ! WHERE
  >
  >     ! IO handler
  >     type(adios2_io), intent(in) :: io
  >
  >     ! name struct handler
  >     type(adios2_namestruct), intent(out) :: namestruct
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_retrieve_names`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} retrieve variable
  names from namestruct obtained from
  [`adios2_available_variables`{.docutils .literal .notranslate}]{.pre}.
  namelist must be pre-allocated.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_retrieve_names(namestruct, namelist, ierr)
  >
  >     ! WHERE
  >
  >     ! namestruct obtained from adios2_available_variables
  >     type(adios2_namestruct), intent(inout) :: namestruct
  >
  >     ! namelist that will contain variable names
  >     character(*), dimension(*), intent(inout) :: namelist
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_available_attributes`{.code
  .highlight .fortran .docutils .literal .highlight-fortran}]{.n} get
  list of attributes in the IO object

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_available_attributes(io, namestruct, ierr)
  >
  >     ! WHERE
  >
  >     ! IO handler
  >     type(adios2_io), intent(in) :: io
  >
  >     ! list of available attributes
  >     type(adios2_namestruct), intent(out) :: namestruct
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_flush_all_engines`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} flush all
  existing engines opened by this IO object

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_flush_all_engines(io, ierr)
  >
  >     ! WHERE:
  >
  >     ! IO in which search and flush for all engines is performed
  >     type(adios2_io), intent(in) :: io
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_remove_variable`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} remove an
  existing variable from an IO object

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_remove_variable(io, name, result, ierr)
  >
  >     ! WHERE:
  >
  >     ! IO in which search and removal for variable is performed
  >     type(adios2_io), intent(in) :: io
  >
  >     ! unique key name to search for variable
  >     character*(*), intent(in) :: name
  >
  >     ! true: variable removed, false: variable not found, not removed
  >     logical, intent(out) :: result
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_remove_all_variables`{.code
  .highlight .fortran .docutils .literal .highlight-fortran}]{.n} remove
  all existing variables from an IO object

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_remove_all_variables(io, ierr)
  >
  >     ! WHERE:
  >
  >     ! IO in which search and removal for all variables is performed
  >     type(adios2_io), intent(in) :: io
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_remove_attribute`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} remove existing
  attribute by its unique name

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_remove_attribute(io, name, result, ierr)
  >
  >     ! WHERE:
  >
  >     ! IO in which search and removal for attribute is performed
  >     type(adios2_io), intent(in) :: io
  >
  >     ! unique key name to search for attribute
  >     character*(*), intent(in) :: name
  >
  >     ! true: attribute removed, false: attribute not found, not removed
  >     logical, intent(out) :: result
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_remove_all_attributes`{.code
  .highlight .fortran .docutils .literal .highlight-fortran}]{.n} remove
  all existing attributes

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_remove_all_attributes(io, ierr)
  >
  >     ! WHERE:
  >
  >     ! IO in which search and removal for all attributes is performed
  >     type(adios2_io), intent(in) :: io
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>
:::

:::: {#variable-subroutines .section}
#### [[Variable]{.std .std-ref}](#document-components/components#variable){.reference .internal} subroutines[](#variable-subroutines "Link to this heading"){.headerlink}

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_define_variable`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} define/create a
  new variable

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     ! Global array variables
  >     subroutine adios2_define_variable(variable, io, variable_name, adios2_type, &
  >                                       ndims, shape_dims, start_dims, count_dims, &
  >                                       adios2_constant_dims, ierr)
  >     ! Global single value variables
  >     subroutine adios2_define_variable(variable, io, variable_name, adios2_type, ierr)
  >
  >     ! WHERE:
  >
  >     ! handler to newly defined variable
  >     type(adios2_variable), intent(out):: variable
  >
  >     ! IO component owning the variable
  >     type(adios2_io), intent(in):: io
  >
  >     ! unique variable identifier within io
  >     character*(*), intent(in):: variable_name
  >
  >     ! defines variable type from adios2 parameters, see next
  >     integer, intent(in):: adios2_type
  >
  >     ! number of dimensions
  >     integer, value, intent(in):: ndims
  >
  >     ! variable shape, global size, dimensions
  >     ! to create local variables optional pass adios2_null_dims
  >     integer(kind=8), dimension(:), intent(in):: shape_dims
  >
  >     ! variable start, local offset, dimensions
  >     ! to create local variables optional pass adios2_null_dims
  >     integer(kind=8), dimension(:), intent(in):: start_dims
  >
  >     ! variable count, local size, dimensions
  >     integer(kind=8), dimension(:), intent(in):: count_dims
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  >
  >     ! .true. : constant dimensions, shape, start and count won't change
  >     !          (mesh sizes, number of nodes)
  >     !          adios2_constant_dims = .true. use for code clarity
  >     ! .false. : variable dimensions, shape, start and count could change
  >     !           (number of particles)
  >     !           adios2_variable_dims = .false. use for code clarity
  >     logical, value, intent(in):: adios2_constant_dims
  > :::
  > ::::
  >
  > </div>

- available [`adios2_type`{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.n} parameters in [`subroutine `{.code .highlight
  .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_define_variable`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n}

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     integer, parameter :: adios2_type_character = 0
  >     integer, parameter :: adios2_type_real = 2
  >     integer, parameter :: adios2_type_dp = 3
  >     integer, parameter :: adios2_type_complex = 4
  >     integer, parameter :: adios2_type_complex_dp = 5
  >
  >     integer, parameter :: adios2_type_integer1 = 6
  >     integer, parameter :: adios2_type_integer2 = 7
  >     integer, parameter :: adios2_type_integer4 = 8
  >     integer, parameter :: adios2_type_integer8 = 9
  >
  >     integer, parameter :: adios2_type_string = 10
  >     integer, parameter :: adios2_type_string_array = 11
  > :::
  > ::::
  >
  > </div>

::: {.admonition .tip}
Tip

Always prefer using [`adios2_type_xxx`{.docutils .literal
.notranslate}]{.pre} parameters explicitly rather than raw numbers.
*e.g.* use [`adios2_type_dp`{.docutils .literal .notranslate}]{.pre}
instead of [`3`{.docutils .literal .notranslate}]{.pre}
:::

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_inquire_variable`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} inquire and get a
  variable. See variable%valid to check if variable exists.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_inquire_variable(variable, io, name, ierr)
  >
  >     ! WHERE:
  >
  >     ! output variable handler:
  >     ! variable%valid = .true. points to valid found variable
  >     ! variable%valid = .false. variable not found
  >     type(adios2_variable), intent(out) :: variable
  >
  >     ! IO in which search for variable is performed
  >     type(adios2_io), intent(in) :: io
  >
  >     ! unique key name to search for variable
  >     character*(*), intent(in) :: name
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_set_shape`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} set new
  [`shape_dims`{.docutils .literal .notranslate}]{.pre} for a variable
  if its dims are marked as varying in the define call
  [`adios2_define_variable`{.docutils .literal .notranslate}]{.pre}

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_set_shape(variable, ndims, shape_dims, ierr)
  >
  >     ! WHERE
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! number of dimensions in shape_dims
  >     integer, intent(in) :: ndims
  >
  >     ! new shape_dims
  >     integer(kind=8), dimension(:), intent(in):: shape_dims
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_set_selection`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} selects part of a
  variable through start_dims and count_dims

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_set_selection(variable, ndims, start_dims, count_dims, ierr)
  >
  >     ! WHERE
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! number of dimensions in start_dims and count_dims
  >     integer, intent(in) :: ndims
  >
  >     ! new start_dims
  >     integer(kind=8), dimension(:), intent(in):: start_dims
  >
  >     ! new count_dims
  >     integer(kind=8), dimension(:), intent(in):: count_dims
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_set_step_selection`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} set a list of
  steps by specifying the starting step and the step count

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_set_step_selection(variable, step_start, step_count, ierr)
  >
  >     ! WHERE
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! new step_start
  >     integer(kind=8), intent(in):: step_start
  >
  >     ! new step_count (or number of steps to read from step_start)
  >     integer(kind=8), intent(in):: step_count
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_variable_max`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} get the maximum
  value in the variable array

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_variable_max(maximum, variable, ierr)
  >
  >     ! WHERE
  >
  >     ! scalar variable that will contain the maximum value
  >     Generic Fortran types, intent(out) :: maximum
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_variable_min`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} get the minimum
  value in the variable array

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_variable_min(minimum, variable, ierr)
  >
  >     ! WHERE
  >
  >     ! scalar variable that will contain the minimum value
  >     Generic Fortran types, intent(out) :: minimum
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_add_operation`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} add an operation
  to a variable

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_add_operation(operation_index, variable, op, key, value, ierr)
  >
  >     ! WHERE
  >
  >     ! reference to the operator handle that will be created
  >     integer, intent(out):: operation_index
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in):: variable
  >
  >     ! Operator handler
  >     type(adios2_operator), intent(in):: op
  >
  >     ! Operator key
  >     character*(*), intent(in):: key
  >
  >     ! Operator value
  >     character*(*), intent(in):: value
  >
  >     ! error code
  >     integer, intent(out):: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_set_operation_parameter`{.code
  .highlight .fortran .docutils .literal .highlight-fortran}]{.n} set a
  parameter for a operator. Replaces value if parameter already exists.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_set_operation_parameter(variable, operation_index, key, value, ierr)
  >
  >     ! WHERE
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in):: variable
  >
  >     ! Operation index handler
  >     integer, intent(in):: operation_index
  >
  >     ! parameter key
  >     character*(*), intent(in):: key
  >
  >     ! parameter value
  >     character*(*), intent(in):: value
  >
  >     ! error code
  >     integer, intent(out):: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_variable_name`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} retrieve variable
  name

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_variable_name(name, variable, ierr)
  >
  >     ! WHERE
  >
  >     ! variable name
  >     character(len=:), allocatable, intent(out) :: name
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_variable_type`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} retrieve variable
  datatype

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_variable_type(type, variable, ierr)
  >
  >     ! WHERE
  >
  >     ! variable type
  >     integer, intent(out) :: type
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_variable_ndims`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} retrieve number
  of dimensions for a variable

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_variable_ndims(ndims, variable, ierr)
  >
  >     ! WHERE
  >
  >     ! No. of dimensions
  >     integer, intent(out) :: ndims
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_variable_shape`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} retrieve the
  shape of a variable

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_variable_shape(shape_dims, ndims, variable, ierr)
  >
  >     ! WHERE
  >
  >     ! array that contains the shape
  >     integer(kind=8), dimension(:), allocatable, intent(out) :: shape_dims
  >
  >     ! no. of dimensions
  >     integer, intent(out) :: ndims
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_variable_steps`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} retrieve the
  number of available steps

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_variable_steps(steps, variable, ierr)
  >
  >     ! WHERE
  >
  >     ! no. of steps
  >     integer(kind=8), intent(out) :: steps
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_set_block_selection`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} Read mode only.
  Required for reading local variables. For global arrays it will set
  the appropriate Start and Count selection for the global array
  coordinates.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_set_block_selection(variable, block_id, ierr)
  >
  >     ! WHERE
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! variable block index defined at write time. Blocks can be inspected with `bpls -D variableName`
  >     integer(kind=8), intent(in) :: block_id
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_set_memory_selection`{.code
  .highlight .fortran .docutils .literal .highlight-fortran}]{.n} set
  the local start (offset) point to the memory pointer passed at
  adios2_put and the memory local dimensions (count). Used for
  non-contiguous memory writes and reads (e.g. multidimensional
  ghost-cells). Currently Get only works for formats based on BP.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_set_memory_selection(variable, ndims, memory_start_dims, memory_count_dims, ierr)
  >
  >     ! WHERE
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! no. of dimensions of the variable
  >     integer, intent(in) :: ndims
  >
  >     ! memory start offsets
  >     integer(kind=8), dimension(:), intent(in) :: memory_start_dims
  >
  >     ! no. of elements in each dimension
  >     integer(kind=8), dimension(:), intent(in) :: memory_count_dims
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_set_step_selection`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} set a step
  selection modifying current step_start, step_count. step_count is the
  number of steps from step_start

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_set_step_selection(variable, step_start, step_count, ierr)
  >
  >     ! WHERE
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! starting step
  >     integer(kind=8), intent(in) :: step_start
  >
  >     ! no. of steps from start
  >     integer(kind=8), intent(in) :: step_count
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_remove_operations`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} remove all
  current operations associated with the variable. Provides the
  posibility to apply operators on a block basis.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_remove_operations(variable, ierr)
  >
  >     ! WHERE
  >
  >     ! variable handler
  >     type(adios2_variable), intent(in):: variable
  >
  >     ! error code
  >     integer, intent(out):: ierr
  > :::
  > ::::
  >
  > </div>
::::

::: {#engine-subroutines .section}
#### [[Engine]{.std .std-ref}](#document-components/components#engine){.reference .internal} subroutines[](#engine-subroutines "Link to this heading"){.headerlink}

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_open`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} opens an engine to execute
  IO tasks

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     ! MPI version: duplicates communicator from adios2_init
  >     ! Non-MPI serial version
  >     subroutine adios2_open(engine, io, name, adios2_mode, ierr)
  >
  >     ! MPI version only to pass a communicator other than the one from adios_init
  >     subroutine adios2_open(engine, io, name, adios2_mode, comm, ierr)
  >
  >     ! WHERE:
  >
  >     ! handler to newly opened adios2 engine
  >     type(adios2_engine), intent(out) :: engine
  >
  >     ! IO that spawns an engine based on its configuration
  >     type(adios2_io), intent(in) :: io
  >
  >     ! unique engine identifier within io, file name for default BPFile engine
  >     character*(*), intent(in) :: name
  >
  >     ! Optional MPI communicator, only in MPI library
  >     integer, intent(in) :: comm
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  >
  >     ! open mode parameter:
  >     !                      adios2_mode_write,
  >     !                      adios2_mode_append,
  >     !                      adios2_mode_read,
  >     integer, intent(in):: adios2_mode
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_begin_step`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} begin a new step or
  progress to the next step. Starts from 0

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_begin_step(engine, adios2_step_mode, timeout_seconds, status, ierr)
  >     ! Default Timeout = -1.    (block until step available)
  >     subroutine adios2_begin_step(engine, adios2_step_mode, ierr)
  >     ! Default step_mode for read and write
  >     subroutine adios2_begin_step(engine, ierr)
  >
  >     ! WHERE
  >
  >     ! engine handler
  >     type(adios2_engine), intent(in) :: engine
  >
  >     ! step_mode parameter:
  >     !     adios2_step_mode_read (read mode default)
  >     !     adios2_step_mode_append (write mode default)
  >     integer, intent(in):: adios2_step_mode
  >
  >     ! optional
  >     ! engine timeout (if supported), in seconds
  >     real, intent(in):: timeout_seconds
  >
  >     ! status of the stream from adios2_step_status_* parameters
  >     integer, intent(out):: status
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_current_step`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} extracts current
  step number

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_current_step(current_step, engine, ierr)
  >
  >     ! WHERE:
  >
  >     ! engine handler
  >     type(adios2_engine), intent(in) :: engine
  >
  >     ! populated with current_step value
  >     integer(kind=8), intent(out) :: current_step
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_steps`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} inspect total number of
  available steps, use for file engines in read mode only

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_steps(steps, engine, ierr)
  >
  >     ! WHERE:
  >
  >     ! engine handler
  >     type(adios2_engine), intent(in) :: engine
  >
  >     ! populated with steps value
  >     integer(kind=8), intent(out) :: steps
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_end_step`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} end current step and
  execute transport IO (flush or read).

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_end_step(engine, ierr)
  >
  >     ! WHERE:
  >
  >     ! engine handler
  >     type(adios2_engine), intent(in) :: engine
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_put`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} put variable data and
  metadata into adios2 for IO operations. Default is deferred mode. For
  optional sync mode, see [[Put: modes and memory contracts]{.std
  .std-ref}](#document-components/components#put-modes-and-memory-contracts){.reference
  .internal}. Variable and data types must match.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_put(engine, variable, data, adios2_mode, ierr)
  >
  >     ! Default adios2_mode_deferred
  >     subroutine adios2_put(engine, variable, data, ierr)
  >
  >     ! WHERE:
  >
  >     ! engine handler
  >     type(adios2_engine), intent(in) :: engine
  >
  >     ! variable handler containing metadata information
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! Fortran bindings supports data types from adios2_type in variables,
  >     ! up to 6 dimensions
  >     ! Generic Fortran type from adios2_type
  >     Generic Fortran types, intent(in):: data
  >     Generic Fortran types, dimension(:), intent(in):: data
  >     Generic Fortran types, dimension(:,:), intent(in):: data
  >     Generic Fortran types, dimension(:,:,:), intent(in):: data
  >     Generic Fortran types, dimension(:,:,:,:), intent(in):: data
  >     Generic Fortran types, dimension(:,:,:,:,:), intent(in):: data
  >     Generic Fortran types, dimension(:,:,:,:,:,:), intent(in):: data
  >
  >     ! mode:
  >     ! adios2_mode_deferred: won't execute until adios2_end_step, adios2_perform_puts or adios2_close
  >     ! adios2_mode_sync: special case, put data immediately, can be reused after this call
  >     integer, intent(in):: adios2_mode
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_perform_puts`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} execute deferred
  calls to [`adios2_put`{.docutils .literal .notranslate}]{.pre}

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_perform_puts(engine, ierr)
  >
  >     ! WHERE:
  >
  >     ! engine handler
  >     type(adios2_engine), intent(in) :: engine
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_get`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} get variable data into
  ADIOS2 for IO operations. Default is deferred mode. For optional sync
  mode, see [[Get: modes and memory contracts]{.std
  .std-ref}](#document-components/components#get-modes-and-memory-contracts){.reference
  .internal}. Variable and data types must match, variable can be
  obtained from [`adios2_inquire_variable`{.docutils .literal
  .notranslate}]{.pre}. Memory for data must be pre-allocated.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_get(engine, variable, data, adios2_mode, ierr)
  >
  >     ! Default adios2_mode_deferred
  >     subroutine adios2_get(engine, variable, data, ierr)
  >
  >     ! WHERE:
  >
  >     ! engine handler
  >     type(adios2_engine), intent(in) :: engine
  >
  >     ! variable handler containing metadata information
  >     type(adios2_variable), intent(in) :: variable
  >
  >     ! Fortran bindings supports data types from adios2_type in variables,
  >     ! up to 6 dimensions. Must be pre-allocated
  >     ! Generic Fortran type from adios2_type
  >     Generic Fortran types, intent(out):: data
  >     Generic Fortran types, dimension(:), intent(out):: data
  >     Generic Fortran types, dimension(:,:), intent(out):: data
  >     Generic Fortran types, dimension(:,:,:), intent(out):: data
  >     Generic Fortran types, dimension(:,:,:,:), intent(out):: data
  >     Generic Fortran types, dimension(:,:,:,:,:), intent(out):: data
  >     Generic Fortran types, dimension(:,:,:,:,:,:), intent(out):: data
  >
  >     ! mode:
  >     ! adios2_mode_deferred: won't execute until adios2_end_step, adios2_perform_gets or adios2_close
  >     ! adios2_mode_sync: special case, get data immediately, can be reused after this call
  >     integer, intent(in):: adios2_mode
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_perform_gets`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} execute deferred
  calls to [`adios2_get`{.docutils .literal .notranslate}]{.pre}

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_perform_gets(engine, ierr)
  >
  >     ! WHERE:
  >
  >     ! engine handler
  >     type(adios2_engine), intent(in) :: engine
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_close`{.code .highlight .fortran
  .docutils .literal .highlight-fortran}]{.n} close engine. May re-open.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_close(engine, ierr)
  >
  >     ! WHERE:
  >
  >     ! engine handler
  >     type(adios2_engine), intent(in) :: engine
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_io_engine_type`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} get current
  engine type

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_io_engine_type(type, io, ierr)
  >
  >     ! WHERE
  >
  >     ! engine type (BP, SST, SSC, HDF5, DataMan)
  >     character(len=:), allocatable, intent(out) :: type
  >
  >     ! IO handler
  >     type(adios2_io), intent(in) :: io
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_lock_writer_definitions`{.code
  .highlight .fortran .docutils .literal .highlight-fortran}]{.n}
  promise that no more definitions or changes to defined variables will
  occur. Useful information if called before the first EndStep() of an
  output Engine, as it will know that the definitions are complete and
  constant for the entire lifetime of the output and may optimize
  metadata handling.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_lock_writer_definitions(engine, ierr)
  >
  >     ! WHERE
  >
  >     ! adios2 engine handler
  >       type(adios2_engine), intent(in) :: engine
  >
  >     ! error code
  >       integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_lock_reader_selections`{.code
  .highlight .fortran .docutils .literal .highlight-fortran}]{.n}
  promise that the reader data selections of are fixed and will not
  change in future timesteps. This information, provided before the
  end_step() representing a fixed read pattern, may be utilized by the
  input Engine to optimize data flow.

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_lock_reader_selections(engine, ierr)
  >
  >     ! WHERE
  >
  >     ! adios2 engine handler
  >       type(adios2_engine), intent(in) :: engine
  >
  >     ! error code
  >       integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>
:::

::: {#operator-subroutines .section}
#### [[Operator]{.std .std-ref}](#document-components/components#operator){.reference .internal} subroutines[](#operator-subroutines "Link to this heading"){.headerlink}

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_operator_type`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} get current
  Operator type

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_operator_type(type, op, ierr)
  >
  >     ! WHERE
  >
  >     ! Operator type name. See list of supported operator types.
  >     character(len=:), allocatable, intent(out) :: type
  >
  >     ! Operator handler
  >     type(adios2_operator), intent(in) :: op
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>
:::

:::: {#attribute-subroutines .section}
#### [[Attribute]{.std .std-ref}](#document-components/components#attribute){.reference .internal} subroutines[](#attribute-subroutines "Link to this heading"){.headerlink}

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_define_attribute`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} define/create a
  new user attribute

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     ! Single value attributes
  >     subroutine adios2_define_attribute(attribute, io, attribute_name, data, ierr)
  >
  >     ! 1D array attributes
  >     subroutine adios2_define_attribute(attribute, io, attribute_name, data, elements, ierr)
  >
  >     ! WHERE:
  >
  >     ! handler to newly defined attribute
  >     type(adios2_attribute), intent(out):: attribute
  >
  >     ! IO component owning the attribute
  >     type(adios2_io), intent(in):: io
  >
  >     ! unique attribute identifier within io
  >     character*(*), intent(in):: attribute_name
  >
  >     ! overloaded subroutine allows for multiple attribute data types
  >     ! they can be single values or 1D arrays
  >     Generic Fortran types, intent(in):: data
  >     Generic Fortran types, dimension(:), intent(in):: data
  >
  >     ! number of elements if passing a 1D array in data argument
  >     integer, intent(in):: elements
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_inquire_attribute`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} inquire for
  existing attribute by its unique name

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_inquire_attribute(attribute, io, name, ierr)
  >
  >     ! WHERE:
  >
  >     ! output attribute handler:
  >     ! attribute%valid = .true. points to valid found attribute
  >     ! attribute%valid = .false. attribute not found
  >     type(adios2_attribute), intent(out) :: attribute
  >
  >     ! IO in which search for attribute is performed
  >     type(adios2_io), intent(in) :: io
  >
  >     ! unique key name to search for attribute
  >     character*(*), intent(in) :: name
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

::: {.admonition .caution}
Caution

Use the [`adios2_remove_*`{.docutils .literal .notranslate}]{.pre}
subroutines with extreme CAUTION. They create outdated dangling
information in the [`adios2_type`{.docutils .literal
.notranslate}]{.pre} handlers. If you don't need them, don't use them.
:::

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_attribute_data`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} retrieve
  attribute data

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_attribute_data(data, attribute, ierr)
  >
  >     ! WHERE
  >
  >     ! data handler
  >     character*(*), intent(out):: data
  >     real, intent(out):: data
  >     real(kind=8), intent(out):: data
  >     integer(kind=1), intent(out):: data
  >     integer(kind=2), intent(out):: data
  >     integer(kind=4), intent(out):: data
  >     integer(kind=8), intent(out):: data
  >     character*(*), dimension(:), intent(out):: data
  >     real, dimension(:), intent(out):: data
  >     real(kind=8), dimension(:), intent(out):: data
  >     integer(kind=2), dimension(:), intent(out):: data
  >     integer(kind=4), dimension(:), intent(out):: data
  >     integer(kind=8), dimension(:), intent(out):: data
  >
  >
  >     ! attribute
  >     type(adios2_attribute), intent(in):: attribute
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_attribute_name`{.code .highlight
  .fortran .docutils .literal .highlight-fortran}]{.n} inspect attribute
  name

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_attribute_name(name, attribute, ierr)
  >
  >     ! WHERE
  >
  >     ! name to be output
  >     character(len=:), allocatable, intent(out) :: name
  >
  >     ! attribute handler
  >     type(adios2_attribute), intent(in) :: attribute
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>

- [`subroutine `{.code .highlight .fortran .docutils .literal
  .highlight-fortran}]{.k}[`adios2_inquire_variable_attribute`{.code
  .highlight .fortran .docutils .literal .highlight-fortran}]{.n}
  retrieve a handler to a previously defined attribute associated to a
  variable

  > <div>
  >
  > :::: {.highlight-fortran .notranslate}
  > ::: highlight
  >     subroutine adios2_inquire_variable_attribute(attribute, io, attribute_name, variable_name, separator, ierr)
  >
  >     ! WHERE
  >
  >     ! attribute handler
  >     type(adios2_attribute), intent(out) :: attribute
  >
  >     ! IO handler
  >     type(adios2_io), intent(in) :: io
  >
  >     ! attribute name
  >     character*(*), intent(in) :: attribute_name
  >
  >     ! variable name
  >     character*(*), intent(in) :: variable_name
  >
  >     ! hierarchy separator (e.g. “/” in variable/attribute )
  >     character*(*), intent(in) :: separator
  >
  >     ! error code
  >     integer, intent(out) :: ierr
  > :::
  > ::::
  >
  > </div>
::::
::::::::::::::::::

::::::::::::::::::::::: {#c-bindings .section}
### C bindings[](#c-bindings "Link to this heading"){.headerlink}

The C bindings are specifically designed for C applications and those
using an older C++ standard (98 and 03). If you are using a C++11 or
more recent standard, please use the C++11 bindings.

The C bindings are based on opaque pointers to the components described
in the [[Components Overview]{.std
.std-ref}](#document-components/components#components-overview){.reference
.internal} section.

C API handlers:

:::: {.highlight-c .notranslate}
::: highlight
    adios2_adios*
    adios2_io*
    adios2_variable*
    adios2_attribute*
    adios2_engine*
    adios2_operator*
:::
::::

Every ADIOS2 function that generates a new [`adios2_*`{.docutils
.literal .notranslate}]{.pre} unique handler returns the latter
explicitly. Therefore, checks can be applied to know if the resulting
handler is NULL. Other functions used to manipulate these valid handlers
will return a value of type [`enum`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`adios2_error`{.docutils .literal .notranslate}]{.pre}
explicitly. These possible errors are based on the [C++ standardized
exceptions](https://en.cppreference.com/w/cpp/error/exception){.reference
.external} . Each error will issue a more detailed description in the
standard error output: [`stderr`{.docutils .literal
.notranslate}]{.pre}.

[`adios2_error`{.docutils .literal .notranslate}]{.pre} possible values:

:::: {.highlight-C .notranslate}
::: highlight
    typedef enum {
        /** success */
        adios2_error_none = 0,

        /**
         * user input error
         */
        adios2_error_invalid_argument = 1,

        /** low-level system error, e.g. system IO error */
        adios2_error_system_error = 2,

        /** runtime errors other than system errors, e.g. memory overflow */
        adios2_error_runtime_error = 3,

        /** any other error exception */
        adios2_error_exception = 4
    } adios2_error;
:::
::::

Usage:

:::: {.highlight-C .notranslate}
::: highlight
    adios2_variable* var = adios2_define_variable(io, ...)
    if(var == NULL )
    {
        // ... something went wrong with adios2_define_variable
        // ... check stderr
    }
    else
    {
        adios2_type type;
        adios2_error errio = adios2_variable_type(&type, var)
        if(errio){
          // ... something went wrong with adios2_variable_type
          if( errio == adios2_error_invalid_argument)
          {
              // ... user input error
              // ... check stderr
          }
        }
    }
:::
::::

::: {.admonition .note}
Note

Use [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`"adios2_c.h"`{.docutils .literal
.notranslate}]{.pre} for the C bindings, [`adios2.h`{.docutils .literal
.notranslate}]{.pre} is the C++11 header.
:::

::::: {#adios2-adios-handler-functions .section}
#### [`adios2_adios`{.docutils .literal .notranslate}]{.pre} handler functions[](#adios2-adios-handler-functions "Link to this heading"){.headerlink}

::: {.breathe-sectiondef .docutils .container}
Defines

[]{#adios2__c__adios_8h_1a17ae2b684c3869f2baf053f43ca64947 .target}[[[adios2_init]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[comm]{.pre}]{.n}[)]{.sig-paren}[](#c.adios2_init "Link to this definition"){.headerlink}\

:   

<!-- -->

[]{#adios2__c__adios_8h_1a96cc68bf049d9a10b88f34affce03587 .target}[[[adios2_init_config]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[config_file]{.pre}]{.n}, [[comm]{.pre}]{.n}[)]{.sig-paren}[](#c.adios2_init_config "Link to this definition"){.headerlink}\

:   
:::

::: {.breathe-sectiondef .docutils .container}
Functions

[]{#_CPPv315adios2_init_mpi8MPI_Comm}[]{#_CPPv215adios2_init_mpi8MPI_Comm}[]{#adios2_init_mpi__MPI_Comm}[]{#adios2__c__adios_8h_1af93e373c6fd791856eee8f86aa444a3d .target}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_init_mpi]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[MPI_Comm]{.pre}]{.n}[ ]{.w}[[comm]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv415adios2_init_mpi8MPI_Comm "Link to this definition"){.headerlink}\

:   Starting point for MPI apps. Creates an ADIOS handler. MPI
    collective and it calls MPI_Comm_dup

    Parameters[:]{.colon}

    :   **comm** -- defines domain scope from application

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv322adios2_init_config_mpiPKc8MPI_Comm}[]{#_CPPv222adios2_init_config_mpiPKc8MPI_Comm}[]{#adios2_init_config_mpi__cCP.MPI_Comm}[]{#adios2__c__adios_8h_1a640577f0ae95ff5d344418d5834d242d .target}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_init_config_mpi]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[config_file]{.pre}]{.n .sig-param}, [[MPI_Comm]{.pre}]{.n}[ ]{.w}[[comm]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv422adios2_init_config_mpiPKc8MPI_Comm "Link to this definition"){.headerlink}\

:   Starting point for MPI apps. Creates an ADIOS handler allowing a
    runtime config file. MPI collective and it calls MPI_Comm_dup and
    MPI_Bcast to pass the configFile contents

    Parameters[:]{.colon}

    :   - **config_file** -- runtime configuration file in xml format

        - **comm** -- defines domain scope from application

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv318adios2_init_serialv}[]{#_CPPv218adios2_init_serialv}[]{#adios2_init_serial__void}[]{#adios2__c__adios_8h_1a905d87db9a68bf6c0b6dc32568eb77dd .target}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_init_serial]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[)]{.sig-paren}[](#_CPPv418adios2_init_serialv "Link to this definition"){.headerlink}\

:   Initialize an ADIOS struct pointer handler in a serial, non-MPI
    application. Doesn't require a runtime config file.

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv325adios2_init_config_serialPKc}[]{#_CPPv225adios2_init_config_serialPKc}[]{#adios2_init_config_serial__cCP}[]{#adios2__c__adios_8h_1a7c6057c85d923b491a6c79bb67bd67c0 .target}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_init_config_serial]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[config_file]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv425adios2_init_config_serialPKc "Link to this definition"){.headerlink}\

:   Initialize an ADIOS struct pointer handler in a serial, non-MPI
    application. Doesn't require a runtime config file.

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv317adios2_declare_ioP12adios2_adiosPKc}[]{#_CPPv217adios2_declare_ioP12adios2_adiosPKc}[]{#adios2_declare_io__adios2_adiosP.cCP}[]{#adios2__c__adios_8h_1a87baa13a71fbcb3131cc14de05bc1495 .target}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_declare_io]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[adios]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv417adios2_declare_ioP12adios2_adiosPKc "Link to this definition"){.headerlink}\

:   Declares a new io handler

    Parameters[:]{.colon}

    :   - **adios** -- owner the io handler

        - **name** -- unique io identifier within current adios handler

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv323adios2_declare_io_orderP12adios2_adiosPKc20adios2_arrayordering}[]{#_CPPv223adios2_declare_io_orderP12adios2_adiosPKc20adios2_arrayordering}[]{#adios2_declare_io_order__adios2_adiosP.cCP.adios2_arrayordering}[]{#adios2__c__adios_8h_1a1dd5ba71556965dd54676f33c211de49 .target}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_declare_io_order]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[adios]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[adios2_arrayordering]{.pre}]{.n}[ ]{.w}[[order]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv423adios2_declare_io_orderP12adios2_adiosPKc20adios2_arrayordering "Link to this definition"){.headerlink}\

:   Declares a new io handler with specific array ordering

    Parameters[:]{.colon}

    :   - **adios** -- owner the io handler

        - **name** -- unique io identifier within current adios handler

        - **order** -- array ordering

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv312adios2_at_ioP12adios2_adiosPKc}[]{#_CPPv212adios2_at_ioP12adios2_adiosPKc}[]{#adios2_at_io__adios2_adiosP.cCP}[]{#adios2__c__adios_8h_1aed1894457244464fabeb6efe4909e08f .target}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_at_io]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[adios]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv412adios2_at_ioP12adios2_adiosPKc "Link to this definition"){.headerlink}\

:   Retrieves a previously declared io handler by name

    Parameters[:]{.colon}

    :   - **adios** -- owner the io handler

        - **name** -- unique name for the previously declared io handler

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv322adios2_define_operatorP12adios2_adiosPKcPKc}[]{#_CPPv222adios2_define_operatorP12adios2_adiosPKcPKc}[]{#adios2_define_operator__adios2_adiosP.cCP.cCP}[]{#adios2__c__adios_8h_1a84ad683d45a22bf511b5c56a0235adc5 .target}[[adios2_operator]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_define_operator]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[adios]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[type]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv422adios2_define_operatorP12adios2_adiosPKcPKc "Link to this definition"){.headerlink}\

:   Defines an adios2 supported operator by its type.

    Parameters[:]{.colon}

    :   - **adios** -- owner the op handler

        - **name** -- unique operator name identifier within current
          ADIOS object

        - **type** -- supported ADIOS2 operator type: zfp, sz

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv323adios2_inquire_operatorP12adios2_adiosPKc}[]{#_CPPv223adios2_inquire_operatorP12adios2_adiosPKc}[]{#adios2_inquire_operator__adios2_adiosP.cCP}[]{#adios2__c__adios_8h_1a443b363878f6a1da011fbe2ac7881a66 .target}[[adios2_operator]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_inquire_operator]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[adios]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv423adios2_inquire_operatorP12adios2_adiosPKc "Link to this definition"){.headerlink}\

:   Retrieves a previously defined operator handler

    Parameters[:]{.colon}

    :   - **adios** -- owner the op handler

        - **name** -- unique name for the previously defined op handler

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv316adios2_flush_allP12adios2_adios}[]{#_CPPv216adios2_flush_allP12adios2_adios}[]{#adios2_flush_all__adios2_adiosP}[]{#adios2__c__adios_8h_1a6fe9fdd4b89f12175ee5f0b3c0559b71 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_flush_all]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[adios]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv416adios2_flush_allP12adios2_adios "Link to this definition"){.headerlink}\

:   Flushes all adios2_engine in write mode in all adios2_io handlers.
    If no adios2_io or adios2_engine exists it does nothing.

    Parameters[:]{.colon}

    :   **adios** -- owner of all io and engines to be flushed

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv315adios2_finalizeP12adios2_adios}[]{#_CPPv215adios2_finalizeP12adios2_adios}[]{#adios2_finalize__adios2_adiosP}[]{#adios2__c__adios_8h_1ac136b6e39a667d886bfefeec7fc81127 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_finalize]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[adios]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv415adios2_finalizeP12adios2_adios "Link to this definition"){.headerlink}\

:   Final point for adios handler. Deallocates adios pointer. Required
    to avoid memory leaks. MPI collective and it calls MPI_Comm_free

    Parameters[:]{.colon}

    :   **adios** -- handler to be deallocated, must be initialized with
        adios2_init or adios2_init_config

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv316adios2_remove_ioP11adios2_boolP12adios2_adiosPKc}[]{#_CPPv216adios2_remove_ioP11adios2_boolP12adios2_adiosPKc}[]{#adios2_remove_io__adios2_boolP.adios2_adiosP.cCP}[]{#adios2__c__adios_8h_1afdcbe4ddfe392322ec8645489f23106a .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_remove_io]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_bool]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[result]{.pre}]{.n .sig-param}, [[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[adios]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv416adios2_remove_ioP11adios2_boolP12adios2_adiosPKc "Link to this definition"){.headerlink}\

:   DANGER ZONE: removes an io created with adios2_declare_io. Will
    create dangling pointers for all the handlers inside removed io.
    NOTE: Use result, not adios2_error to check if the IO was removed.

    Parameters[:]{.colon}

    :   - **result** -- output adios2_true: io not found and not
          removed, adios2_false: io not found and not removed

        - **adios** -- owner of io to be removed

        - **name** -- input unique identifier for io to be removed

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv321adios2_remove_all_iosP12adios2_adios}[]{#_CPPv221adios2_remove_all_iosP12adios2_adios}[]{#adios2_remove_all_ios__adios2_adiosP}[]{#adios2__c__adios_8h_1a36639f866f00be22643ee42cdb495a31 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_remove_all_ios]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[adios]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_remove_all_iosP12adios2_adios "Link to this definition"){.headerlink}\

:   DANGER ZONE: removes all ios created with adios2_declare_io. Will
    create dangling pointers for all the handlers inside all removed io.

    Parameters[:]{.colon}

    :   **adios** -- owner of all ios to be removed

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv330adios2_enter_computation_blockP12adios2_adios}[]{#_CPPv230adios2_enter_computation_blockP12adios2_adios}[]{#adios2_enter_computation_block__adios2_adiosP}[]{#adios2__c__adios_8h_1ac560a20149bfee3a0204133aae5ac2b1 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_enter_computation_block]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[adios]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv430adios2_enter_computation_blockP12adios2_adios "Link to this definition"){.headerlink}\

:   Inform ADIOS about entering communication-free computation block in
    main thread. Useful when using Async IO

<!-- -->

[]{#_CPPv329adios2_exit_computation_blockP12adios2_adios}[]{#_CPPv229adios2_exit_computation_blockP12adios2_adios}[]{#adios2_exit_computation_block__adios2_adiosP}[]{#adios2__c__adios_8h_1a3ee25eec5f0798715ea75174fdd77f66 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_exit_computation_block]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_adios]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[adios]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv429adios2_exit_computation_blockP12adios2_adios "Link to this definition"){.headerlink}\

:   Inform ADIOS about exiting communication-free computation block in
    main thread. Useful when using Async IO
:::
:::::

:::: {#adios2-io-handler-functions .section}
#### [`adios2_io`{.docutils .literal .notranslate}]{.pre} handler functions[](#adios2-io-handler-functions "Link to this heading"){.headerlink}

::: {.breathe-sectiondef .docutils .container}
Functions

[]{#_CPPv321adios2_in_config_fileP11adios2_boolPK9adios2_io}[]{#_CPPv221adios2_in_config_fileP11adios2_boolPK9adios2_io}[]{#adios2_in_config_file__adios2_boolP.adios2_ioCP}[]{#adios2__c__io_8h_1ac8781dd85d88680510f67e26c2edb589 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_in_config_file]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_bool]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[result]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_in_config_fileP11adios2_boolPK9adios2_io "Link to this definition"){.headerlink}\

:   Check if io exists in a config file passed to the adios handler that
    created this io.

    Parameters[:]{.colon}

    :   - **result** -- output adios2_true=1: in config file,
          adios2_false=0: not in config file

        - **io** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv317adios2_set_engineP9adios2_ioPKc}[]{#_CPPv217adios2_set_engineP9adios2_ioPKc}[]{#adios2_set_engine__adios2_ioP.cCP}[]{#adios2__c__io_8h_1a5c121afefc8aa3c83c05dbd73249c99c .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_set_engine]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[engine_type]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv417adios2_set_engineP9adios2_ioPKc "Link to this definition"){.headerlink}\

:   Set the engine type for current io handler.

    Parameters[:]{.colon}

    :   - **io** -- handler

        - **engine_type** -- predefined engine type, default is bpfile

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv321adios2_set_parametersP9adios2_ioPKc}[]{#_CPPv221adios2_set_parametersP9adios2_ioPKc}[]{#adios2_set_parameters__adios2_ioP.cCP}[]{#adios2__c__io_8h_1a88d50b55f535e98b13338445a2e282ce .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_set_parameters]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[parameters]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_set_parametersP9adios2_ioPKc "Link to this definition"){.headerlink}\

:   Set several parameters at once.

    Parameters[:]{.colon}

    :   - **io** -- handler

        - **string** -- parameters in the format "param1=value1 , param2
          = value2"

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv320adios2_set_parameterP9adios2_ioPKcPKc}[]{#_CPPv220adios2_set_parameterP9adios2_ioPKcPKc}[]{#adios2_set_parameter__adios2_ioP.cCP.cCP}[]{#adios2__c__io_8h_1a154871e4ec1cf1034cda0a7ee9b04915 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_set_parameter]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[key]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420adios2_set_parameterP9adios2_ioPKcPKc "Link to this definition"){.headerlink}\

:   Set a single parameter. Overwrites value if key exists.

    Parameters[:]{.colon}

    :   - **io** -- handler

        - **key** -- parameter key

        - **value** -- parameter value

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv320adios2_get_parameterPcP6size_tPK9adios2_ioPKc}[]{#_CPPv220adios2_get_parameterPcP6size_tPK9adios2_ioPKc}[]{#adios2_get_parameter__cP.sP.adios2_ioCP.cCP}[]{#adios2__c__io_8h_1a90a57845b4688040fc2026cdff460577 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_get_parameter]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[key]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420adios2_get_parameterPcP6size_tPK9adios2_ioPKc "Link to this definition"){.headerlink}\

:   Return IO parameter value string and length without '\\0\\ character
    For safe use, call this function first with NULL name parameter to
    get the size, then preallocate the buffer (with room for '\\0' if
    desired), then call the function again with the buffer. Then '\\0'
    terminate it if desired.

    Parameters[:]{.colon}

    :   - **value** -- output

        - **size** -- output, value size without '\\0'

        - **io** -- input handler

        - **key** -- input parameter key, if not found return size = 0
          and value is untouched

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv323adios2_clear_parametersP9adios2_io}[]{#_CPPv223adios2_clear_parametersP9adios2_io}[]{#adios2_clear_parameters__adios2_ioP}[]{#adios2__c__io_8h_1a4deedae85a8cb25e04ad1073c5ae6a44 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_clear_parameters]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv423adios2_clear_parametersP9adios2_io "Link to this definition"){.headerlink}\

:   Clear all parameters.

    Parameters[:]{.colon}

    :   **io** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv320adios2_add_transportP6size_tP9adios2_ioPKc}[]{#_CPPv220adios2_add_transportP6size_tP9adios2_ioPKc}[]{#adios2_add_transport__sP.adios2_ioP.cCP}[]{#adios2__c__io_8h_1a3508cfda3d8ed9c718d0eb14af79accd .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_add_transport]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[transport_index]{.pre}]{.n .sig-param}, [[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[type]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420adios2_add_transportP6size_tP9adios2_ioPKc "Link to this definition"){.headerlink}\

:   Add a transport to current io handler. Must be supported by current
    engine type.

    Parameters[:]{.colon}

    :   - **transport_index** -- handler used for setting transport
          parameters or at adios2_close

        - **io** -- handler

        - **type** -- must be a supported transport type for a
          particular Engine. CAN'T use the keywords "Transport" or
          "transport"

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv330adios2_set_transport_parameterP9adios2_ioK6size_tPKcPKc}[]{#_CPPv230adios2_set_transport_parameterP9adios2_ioK6size_tPKcPKc}[]{#adios2_set_transport_parameter__adios2_ioP.sC.cCP.cCP}[]{#adios2__c__io_8h_1a04c15c5ac137979ef2d5896db18cd077 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_set_transport_parameter]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[transport_index]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[key]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv430adios2_set_transport_parameterP9adios2_ioK6size_tPKcPKc "Link to this definition"){.headerlink}\

:   Set a single parameter to an existing transport identified with a
    transport_index handler from adios2_add_transport. Overwrites
    existing parameter with the same key.

    Parameters[:]{.colon}

    :   - **io** -- handler

        - **transport_index** -- handler from adios2_add_transport

        - **key** -- parameter key

        - **value** -- parameter value

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv322adios2_define_variableP9adios2_ioPKcK11adios2_typeK6size_tPK6size_tPK6size_tPK6size_tK20adios2_constant_dims}[]{#_CPPv222adios2_define_variableP9adios2_ioPKcK11adios2_typeK6size_tPK6size_tPK6size_tPK6size_tK20adios2_constant_dims}[]{#adios2_define_variable__adios2_ioP.cCP.adios2_typeC.sC.sCP.sCP.sCP.adios2_constant_dimsC}[]{#adios2__c__io_8h_1a52d4db791bc94e29bc881f4f5baf3a0a .target}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_define_variable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_type]{.pre}]{.n}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[ndims]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[shape]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[start]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[count]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_constant_dims]{.pre}]{.n}[ ]{.w}[[constant_dims]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv422adios2_define_variableP9adios2_ioPKcK11adios2_typeK6size_tPK6size_tPK6size_tPK6size_tK20adios2_constant_dims "Link to this definition"){.headerlink}\

:   Define a variable within io.

    Parameters[:]{.colon}

    :   - **io** -- handler that owns the variable

        - **name** -- unique variable identifier

        - **type** -- primitive type from enum adios2_type in
          adios2_c_types.h

        - **ndims** -- number of dimensions

        - **shape** -- global dimension

        - **start** -- local offset

        - **count** -- local dimension

        - **constant_dims** -- adios2_constant_dims_true:: shape, start,
          count won't change; adios2_constant_dims_false: shape, start,
          count will change after definition

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv323adios2_inquire_variableP9adios2_ioPKc}[]{#_CPPv223adios2_inquire_variableP9adios2_ioPKc}[]{#adios2_inquire_variable__adios2_ioP.cCP}[]{#adios2__c__io_8h_1a474a908aae87875e64b1da6cf83c9429 .target}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_inquire_variable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv423adios2_inquire_variableP9adios2_ioPKc "Link to this definition"){.headerlink}\

:   Retrieve a variable handler within current io handler.

    Parameters[:]{.colon}

    :   - **io** -- handler to variable io owner

        - **name** -- unique variable identifier within io handler

    Returns[:]{.colon}

    :   found: handler, not found: NULL

<!-- -->

[]{#_CPPv328adios2_inquire_all_variablesPPP15adios2_variableP6size_tP9adios2_io}[]{#_CPPv228adios2_inquire_all_variablesPPP15adios2_variableP6size_tP9adios2_io}[]{#adios2_inquire_all_variables__adios2_variablePPP.sP.adios2_ioP}[]{#adios2__c__io_8h_1a312267da07ad6ac89eb7ed08a139259b .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_inquire_all_variables]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[variables]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv428adios2_inquire_all_variablesPPP15adios2_variableP6size_tP9adios2_io "Link to this definition"){.headerlink}\

:   Returns an array of variable handlers for all variable present in
    the io group

    Parameters[:]{.colon}

    :   - **variables** -- output array of variable pointers (pointer to
          an adios2_variable\*\*)

        - **size** -- output number of variables

        - **io** -- handler to variables io owner

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv330adios2_inquire_group_variablesPPP15adios2_variablePKcP6size_tP9adios2_io}[]{#_CPPv230adios2_inquire_group_variablesPPP15adios2_variablePKcP6size_tP9adios2_io}[]{#adios2_inquire_group_variables__adios2_variablePPP.cCP.sP.adios2_ioP}[]{#adios2__c__io_8h_1a1ffc69f4a29ea445a26024ff7bb8c021 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_inquire_group_variables]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[variables]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[full_group_name]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv430adios2_inquire_group_variablesPPP15adios2_variablePKcP6size_tP9adios2_io "Link to this definition"){.headerlink}\

:   

<!-- -->

[]{#_CPPv323adios2_define_attributeP9adios2_ioPKcK11adios2_typePKv}[]{#_CPPv223adios2_define_attributeP9adios2_ioPKcK11adios2_typePKv}[]{#adios2_define_attribute__adios2_ioP.cCP.adios2_typeC.voidCP}[]{#adios2__c__io_8h_1a64651d6689204335ea875f6859edfef0 .target}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_define_attribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_type]{.pre}]{.n}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv423adios2_define_attributeP9adios2_ioPKcK11adios2_typePKv "Link to this definition"){.headerlink}\

:   Define an attribute value inside io.

    Parameters[:]{.colon}

    :   - **io** -- handler that owns the attribute

        - **name** -- unique attribute name inside IO handler

        - **type** -- primitive type from enum adios2_type in
          adios2_c_types.h

        - **value** -- attribute single value

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv329adios2_define_attribute_arrayP9adios2_ioPKcK11adios2_typePKvK6size_t}[]{#_CPPv229adios2_define_attribute_arrayP9adios2_ioPKcK11adios2_typePKvK6size_t}[]{#adios2_define_attribute_array__adios2_ioP.cCP.adios2_typeC.voidCP.sC}[]{#adios2__c__io_8h_1a2fb94cf2b32a454b1191ba58a459d3e7 .target}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_define_attribute_array]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_type]{.pre}]{.n}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[size]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv429adios2_define_attribute_arrayP9adios2_ioPKcK11adios2_typePKvK6size_t "Link to this definition"){.headerlink}\

:   Define an attribute array inside io.

    Parameters[:]{.colon}

    :   - **io** -- handler that owns the attribute

        - **name** -- unique attribute name inside IO handler

        - **type** -- primitive type from enum adios2_type in
          adios2_c_types.h

        - **data** -- attribute data array

        - **size** -- number of elements of data array

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv332adios2_define_variable_attributeP9adios2_ioPKcK11adios2_typePKvPKcPKc}[]{#_CPPv232adios2_define_variable_attributeP9adios2_ioPKcK11adios2_typePKvPKcPKc}[]{#adios2_define_variable_attribute__adios2_ioP.cCP.adios2_typeC.voidCP.cCP.cCP}[]{#adios2__c__io_8h_1a7da97c460365e0135e82d5a9e170413c .target}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_define_variable_attribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_type]{.pre}]{.n}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[variable_name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[separator]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv432adios2_define_variable_attributeP9adios2_ioPKcK11adios2_typePKvPKcPKc "Link to this definition"){.headerlink}\

:   Define an attribute single value associated to an existing variable
    by its name

    Parameters[:]{.colon}

    :   - **io** -- handler that owns the variable and attribute

        - **name** -- unique attribute name inside a variable in io
          handler

        - **type** -- primitive type from enum adios2_type in
          adios2_c_types.h

        - **value** -- attribute single value

        - **variable_name** -- unique variable identifier in io handler.
          If variable doesn't exist adios2_error is
          adios2_error_invalid_argument.

        - **separator** -- hierarchy separator (e.g. "/" in
          variable_name/name )

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv338adios2_define_variable_attribute_arrayP9adios2_ioPKcK11adios2_typePKvK6size_tPKcPKc}[]{#_CPPv238adios2_define_variable_attribute_arrayP9adios2_ioPKcK11adios2_typePKvK6size_tPKcPKc}[]{#adios2_define_variable_attribute_array__adios2_ioP.cCP.adios2_typeC.voidCP.sC.cCP.cCP}[]{#adios2__c__io_8h_1a59fcdfa0f45df9bac067aa55443e6ba3 .target}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_define_variable_attribute_array]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_type]{.pre}]{.n}[ ]{.w}[[type]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[variable_name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[separator]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv438adios2_define_variable_attribute_arrayP9adios2_ioPKcK11adios2_typePKvK6size_tPKcPKc "Link to this definition"){.headerlink}\

:   Define an attribute array associated to an existing variable by its
    name

    Parameters[:]{.colon}

    :   - **io** -- handler that owns the variable and attribute

        - **name** -- unique attribute name inside a variable in io
          handler

        - **type** -- primitive type from enum adios2_type in
          adios2_c_types.h

        - **data** -- attribute data single value or array

        - **size** -- number of elements of data array

        - **variable_name** -- unique variable identifier in io handler.
          If variable doesn't exist adios2_error is true.

        - **separator** -- hierarchy separator (e.g. "/" in
          variable/attribute )

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv324adios2_inquire_attributeP9adios2_ioPKc}[]{#_CPPv224adios2_inquire_attributeP9adios2_ioPKc}[]{#adios2_inquire_attribute__adios2_ioP.cCP}[]{#adios2__c__io_8h_1a6bfbeaaee1c3fac00d6d5acbd8b8afa7 .target}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_inquire_attribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv424adios2_inquire_attributeP9adios2_ioPKc "Link to this definition"){.headerlink}\

:   Returns a handler to a previously defined attribute by name

    Parameters[:]{.colon}

    :   - **io** -- handler to attribute io owner

        - **name** -- unique attribute identifier within io handler

    Returns[:]{.colon}

    :   found: handler, not found: NULL

<!-- -->

[]{#_CPPv333adios2_inquire_variable_attributeP9adios2_ioPKcPKcPKc}[]{#_CPPv233adios2_inquire_variable_attributeP9adios2_ioPKcPKcPKc}[]{#adios2_inquire_variable_attribute__adios2_ioP.cCP.cCP.cCP}[]{#adios2__c__io_8h_1af6962d17a6cf30f8f358ff4f20064d36 .target}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_inquire_variable_attribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[variable_name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[separator]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv433adios2_inquire_variable_attributeP9adios2_ioPKcPKcPKc "Link to this definition"){.headerlink}\

:   Retrieve a handler to a previously defined attribute associated to a
    variable

    Parameters[:]{.colon}

    :   - **io** -- handler to attribute and variable io owner

        - **name** -- unique attribute name inside a variable in io
          handler

        - **variable_name** -- name of the variable associate with this
          attribute

        - **separator** -- hierarchy separator (e.g. "/" in
          variable/attribute )

    Returns[:]{.colon}

    :   found: handler, not found: NULL

<!-- -->

[]{#_CPPv329adios2_inquire_all_attributesPPP16adios2_attributeP6size_tP9adios2_io}[]{#_CPPv229adios2_inquire_all_attributesPPP16adios2_attributeP6size_tP9adios2_io}[]{#adios2_inquire_all_attributes__adios2_attributePPP.sP.adios2_ioP}[]{#adios2__c__io_8h_1ad7d7cccbd0417d0c85096a56d79d5dc1 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_inquire_all_attributes]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[attributes]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv429adios2_inquire_all_attributesPPP16adios2_attributeP6size_tP9adios2_io "Link to this definition"){.headerlink}\

:   Returns an array of attribute handlers for all attribute present in
    the io group

    Parameters[:]{.colon}

    :   - **attributes** -- output array of attribute pointers (pointer
          to an adios2_attribute\*\*)

        - **size** -- output number of attributes

        - **io** -- handler to attributes io owner

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv331adios2_inquire_group_attributesPPP16adios2_attributePKcP6size_tP9adios2_io}[]{#_CPPv231adios2_inquire_group_attributesPPP16adios2_attributePKcP6size_tP9adios2_io}[]{#adios2_inquire_group_attributes__adios2_attributePPP.cCP.sP.adios2_ioP}[]{#adios2__c__io_8h_1a1cd2995bdcc44868855efbf2a2a83bf2 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_inquire_group_attributes]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[attributes]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[full_prefix]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv431adios2_inquire_group_attributesPPP16adios2_attributePKcP6size_tP9adios2_io "Link to this definition"){.headerlink}\

:   

<!-- -->

[]{#_CPPv324adios2_inquire_subgroupsPPPcPKcP6size_tP9adios2_io}[]{#_CPPv224adios2_inquire_subgroupsPPPcPKcP6size_tP9adios2_io}[]{#adios2_inquire_subgroups__cPPP.cCP.sP.adios2_ioP}[]{#adios2__c__io_8h_1aeedeeda6b8acfc111042a39aed0fbec5 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_inquire_subgroups]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[subGroupNames]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[full_prefix]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv424adios2_inquire_subgroupsPPPcPKcP6size_tP9adios2_io "Link to this definition"){.headerlink}\

:   Return a list of list sub group names

<!-- -->

[]{#_CPPv322adios2_remove_variableP11adios2_boolP9adios2_ioPKc}[]{#_CPPv222adios2_remove_variableP11adios2_boolP9adios2_ioPKc}[]{#adios2_remove_variable__adios2_boolP.adios2_ioP.cCP}[]{#adios2__c__io_8h_1ac25000351825d642e605be15d7b66513 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_remove_variable]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_bool]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[result]{.pre}]{.n .sig-param}, [[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv422adios2_remove_variableP11adios2_boolP9adios2_ioPKc "Link to this definition"){.headerlink}\

:   DANGEROUS! Removes a variable identified by name. Might create
    dangling pointers.

    Parameters[:]{.colon}

    :   - **result** -- output adios2_true(1): found and removed
          variable, adios2_false(0): not found, nothing to remove

        - **io** -- handler variable io owner

        - **name** -- unique variable name within io handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv327adios2_remove_all_variablesP9adios2_io}[]{#_CPPv227adios2_remove_all_variablesP9adios2_io}[]{#adios2_remove_all_variables__adios2_ioP}[]{#adios2__c__io_8h_1a99e39d64f33ae8d7686bf76f29033496 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_remove_all_variables]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv427adios2_remove_all_variablesP9adios2_io "Link to this definition"){.headerlink}\

:   DANGEROUS! Removes all existing variables in current IO object.
    Might create dangling pointers.

    Parameters[:]{.colon}

    :   **io** -- handler variables io owner

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv326adios2_available_variablesP9adios2_ioP6size_t}[]{#_CPPv226adios2_available_variablesP9adios2_ioP6size_t}[]{#adios2_available_variables__adios2_ioP.sP}[]{#adios2__c__io_8h_1a588ef29bc80d4aeb2d100d891ae73d9d .target}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[[adios2_available_variables]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv426adios2_available_variablesP9adios2_ioP6size_t "Link to this definition"){.headerlink}\

:   returns an array or c strings for names of available variables Might
    create dangling pointers

    Parameters[:]{.colon}

    :   - **io** -- handler variables io owner

        - **length** -- of array of strings

    Returns[:]{.colon}

    :   names of variables as an array of strings

<!-- -->

[]{#_CPPv327adios2_available_attributesP9adios2_ioP6size_t}[]{#_CPPv227adios2_available_attributesP9adios2_ioP6size_t}[]{#adios2_available_attributes__adios2_ioP.sP}[]{#adios2__c__io_8h_1a7722e0425af0f1c7178acae30fcfa5ce .target}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[[adios2_available_attributes]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv427adios2_available_attributesP9adios2_ioP6size_t "Link to this definition"){.headerlink}\

:   returns an array or c strings for names of available attributes
    Might create dangling pointers

    Parameters[:]{.colon}

    :   - **io** -- handler variables io owner

        - **length** -- of array of strings

    Returns[:]{.colon}

    :   names of variables as an array of strings

<!-- -->

[]{#_CPPv323adios2_remove_attributeP11adios2_boolP9adios2_ioPKc}[]{#_CPPv223adios2_remove_attributeP11adios2_boolP9adios2_ioPKc}[]{#adios2_remove_attribute__adios2_boolP.adios2_ioP.cCP}[]{#adios2__c__io_8h_1a1d99e1f5999058029acfa0a72f5f4fff .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_remove_attribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_bool]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[result]{.pre}]{.n .sig-param}, [[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv423adios2_remove_attributeP11adios2_boolP9adios2_ioPKc "Link to this definition"){.headerlink}\

:   DANGEROUS! Removes an attribute identified by name. Might create
    dangling pointers.

    Parameters[:]{.colon}

    :   - **result** -- output adios2_true(1): found and removed
          attribute, adios2_false(0): not found, nothing to remove

        - **io** -- handler attribute io owner

        - **name** -- unique attribute name within io handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv328adios2_remove_all_attributesP9adios2_io}[]{#_CPPv228adios2_remove_all_attributesP9adios2_io}[]{#adios2_remove_all_attributes__adios2_ioP}[]{#adios2__c__io_8h_1a85197f0a90cc726ac4d101e65a0b9086 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_remove_all_attributes]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv428adios2_remove_all_attributesP9adios2_io "Link to this definition"){.headerlink}\

:   DANGEROUS! Removes all existing attributes in current IO object.
    Might create dangling pointers.

    Parameters[:]{.colon}

    :   **io** -- handler attributes io owner

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv311adios2_openP9adios2_ioPKcK11adios2_mode}[]{#_CPPv211adios2_openP9adios2_ioPKcK11adios2_mode}[]{#adios2_open__adios2_ioP.cCP.adios2_modeC}[]{#adios2__c__io_8h_1ad62726c408b5e67c5ab87e50c41d0f9d .target}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_open]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_mode]{.pre}]{.n}[ ]{.w}[[mode]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv411adios2_openP9adios2_ioPKcK11adios2_mode "Link to this definition"){.headerlink}\

:   Open an Engine to start heavy-weight input/output operations. In MPI
    version reuses the communicator from adios2_init or
    adios2_init_config MPI Collective function as it calls MPI_Comm_dup

    Parameters[:]{.colon}

    :   - **io** -- engine owner

        - **name** -- unique engine identifier

        - **mode** -- adios2_mode_write, adios2_mode_read,
          adios2_mode_append and adios2_mode_readRandomAccess

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv325adios2_open_with_metadataP9adios2_ioPKcPKcK6size_t}[]{#_CPPv225adios2_open_with_metadataP9adios2_ioPKcPKcK6size_t}[]{#adios2_open_with_metadata__adios2_ioP.cCP.cCP.sC}[]{#adios2__c__io_8h_1aa6c20cab82f029807572f609053f677b .target}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_open_with_metadata]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[md]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[mdsize]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv425adios2_open_with_metadataP9adios2_ioPKcPKcK6size_t "Link to this definition"){.headerlink}\

:   Open an Engine to start heavy-weight input/output operations. This
    function is for opening a file (not stream) with ReadRandomAccess
    mode and supplying the metadata already in memory. The metadata
    should be retrieved by another program calling
    [[adios2_engine_get_metadata()]{.std
    .std-ref}](#document-api_full/api_full#adios2__c__engine_8h_1a6411f972c86be15b1d5e6d00c5970cca){.reference
    .internal} after opening the file.

    Parameters[:]{.colon}

    :   - **io** -- engine owner

        - **name** -- unique engine identifier

        - **md** -- file metadata residing in memory

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv320adios2_open_new_commP9adios2_ioPKcK11adios2_mode8MPI_Comm}[]{#_CPPv220adios2_open_new_commP9adios2_ioPKcK11adios2_mode8MPI_Comm}[]{#adios2_open_new_comm__adios2_ioP.cCP.adios2_modeC.MPI_Comm}[]{#adios2__c__io_8h_1a8fbd0470266f6cdc8c19bb9305596c73 .target}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_open_new_comm]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_mode]{.pre}]{.n}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[MPI_Comm]{.pre}]{.n}[ ]{.w}[[comm]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420adios2_open_new_commP9adios2_ioPKcK11adios2_mode8MPI_Comm "Link to this definition"){.headerlink}\

:   Open an Engine to start heavy-weight input/output operations. MPI
    Collective function as it calls MPI_Comm_dup

    Parameters[:]{.colon}

    :   - **io** -- engine owner

        - **name** -- unique engine identifier

        - **mode** -- adios2_mode_write, adios2_mode_read,
          adios2_mode_append and adios2_mode_readRandomAccess

        - **comm** -- communicator other than adios' handler comm. MPI
          only.

    Returns[:]{.colon}

    :   success: handler, failure: NULL

<!-- -->

[]{#_CPPv324adios2_flush_all_enginesP9adios2_io}[]{#_CPPv224adios2_flush_all_enginesP9adios2_io}[]{#adios2_flush_all_engines__adios2_ioP}[]{#adios2__c__io_8h_1a3e7240f758f6fcdea1a07d69ad7a64f4 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_flush_all_engines]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv424adios2_flush_all_enginesP9adios2_io "Link to this definition"){.headerlink}\

:   Flushes all engines created with current io handler using
    adios2_open

    Parameters[:]{.colon}

    :   **io** -- handler whose engine will be flushed

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv318adios2_engine_typePcP6size_tPK9adios2_io}[]{#_CPPv218adios2_engine_typePcP6size_tPK9adios2_io}[]{#adios2_engine_type__cP.sP.adios2_ioCP}[]{#adios2__c__io_8h_1ae8646494064d98decf9a86dd11c9ca86 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_engine_type]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[engine_type]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv418adios2_engine_typePcP6size_tPK9adios2_io "Link to this definition"){.headerlink}\

:   return engine type string and length without null character For safe
    use, call this function first with NULL name parameter to get the
    size, then preallocate the buffer (with room for '\\0' if desired),
    then call the function again with the buffer. Then '\\0' terminate
    it if desired.

    Parameters[:]{.colon}

    :   - **engine_type** -- output, string without trailing '\\0', NULL
          or preallocated buffer

        - **size** -- output, engine_type size without '\\0'

        - **io** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv317adios2_get_engineP9adios2_ioPKc}[]{#_CPPv217adios2_get_engineP9adios2_ioPKc}[]{#adios2_get_engine__adios2_ioP.cCP}[]{#adios2__c__io_8h_1aac7a52ec78d41fc20518775a721c6232 .target}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_get_engine]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_io]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[io]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv417adios2_get_engineP9adios2_ioPKc "Link to this definition"){.headerlink}\

:   
:::
::::

:::: {#adios2-variable-handler-functions .section}
#### [`adios2_variable`{.docutils .literal .notranslate}]{.pre} handler functions[](#adios2-variable-handler-functions "Link to this heading"){.headerlink}

::: {.breathe-sectiondef .docutils .container}
Functions

[]{#_CPPv316adios2_set_shapeP15adios2_variableK6size_tPK6size_t}[]{#_CPPv216adios2_set_shapeP15adios2_variableK6size_tPK6size_t}[]{#adios2_set_shape__adios2_variableP.sC.sCP}[]{#adios2__c__variable_8h_1a1a1a6fa4cc19e42aa34316fe5cc692e1 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_set_shape]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[ndims]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[shape]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv416adios2_set_shapeP15adios2_variableK6size_tPK6size_t "Link to this definition"){.headerlink}\

:   Set new shape, care must be taken when reading back the variable for
    different steps. Only applies to Global arrays.

    Parameters[:]{.colon}

    :   - **variable** -- handler for which new selection will be
          applied to

        - **ndims** -- number of dimensions for start and count

        - **shape** -- new shape dimensions array

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv323adios2_store_stats_onlyP15adios2_variableK11adios2_bool}[]{#_CPPv223adios2_store_stats_onlyP15adios2_variableK11adios2_bool}[]{#adios2_store_stats_only__adios2_variableP.adios2_boolC}[]{#adios2__c__variable_8h_1a770d7051ff4d7e9e132ac70321c3d34c .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_store_stats_only]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_bool]{.pre}]{.n}[ ]{.w}[[mode]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv423adios2_store_stats_onlyP15adios2_variableK11adios2_bool "Link to this definition"){.headerlink}\

:   Set the write mode of a variable

    Parameters[:]{.colon}

    :   **false** -- - write data; true - write only stats

<!-- -->

[]{#_CPPv323adios2_set_memory_spaceP15adios2_variableK19adios2_memory_space}[]{#_CPPv223adios2_set_memory_spaceP15adios2_variableK19adios2_memory_space}[]{#adios2_set_memory_space__adios2_variableP.adios2_memory_spaceC}[]{#adios2__c__variable_8h_1a5473bdbf37bfc70b6f3a5496664a433b .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_set_memory_space]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_memory_space]{.pre}]{.n}[ ]{.w}[[mem]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv423adios2_set_memory_spaceP15adios2_variableK19adios2_memory_space "Link to this definition"){.headerlink}\

:   Sets the memory space for all following Puts/Gets to either host
    (default) or device

    Parameters[:]{.colon}

    :   **mem** -- memory space where Put/Get buffers are allocated

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv323adios2_get_memory_spaceP19adios2_memory_spaceP15adios2_variable}[]{#_CPPv223adios2_get_memory_spaceP19adios2_memory_spaceP15adios2_variable}[]{#adios2_get_memory_space__adios2_memory_spaceP.adios2_variableP}[]{#adios2__c__variable_8h_1a8e14f1e540e3bcc80a24f2adc3f23efe .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_get_memory_space]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_memory_space]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[mem]{.pre}]{.n .sig-param}, [[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv423adios2_get_memory_spaceP19adios2_memory_spaceP15adios2_variable "Link to this definition"){.headerlink}\

:   Get the memory space that was set by the application for a given
    variable

    Parameters[:]{.colon}

    :   - **memory** -- space output, the variable memory space

        - **variable** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv326adios2_set_block_selectionP15adios2_variableK6size_t}[]{#_CPPv226adios2_set_block_selectionP15adios2_variableK6size_t}[]{#adios2_set_block_selection__adios2_variableP.sC}[]{#adios2__c__variable_8h_1a357eb3e9e3c2bdd4e23b9ef4a576e0f0 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_set_block_selection]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[block_id]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv426adios2_set_block_selectionP15adios2_variableK6size_t "Link to this definition"){.headerlink}\

:   Read mode only. Required for reading local variables. For Global
    Arrays it will Set the appropriate Start and Count Selection for the
    global array coordinates.

    Parameters[:]{.colon}

    :   - **variable** -- handler for which new selection will be
          applied to

        - **block_id** -- variable block index defined at write time.
          Blocks can be inspected with bpls -D variableName

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv320adios2_set_selectionP15adios2_variableK6size_tPK6size_tPK6size_t}[]{#_CPPv220adios2_set_selectionP15adios2_variableK6size_tPK6size_tPK6size_t}[]{#adios2_set_selection__adios2_variableP.sC.sCP.sCP}[]{#adios2__c__variable_8h_1a5477eff43e41a2ada3b899e1d02bdac3 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_set_selection]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[ndims]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[start]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[count]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420adios2_set_selectionP15adios2_variableK6size_tPK6size_tPK6size_t "Link to this definition"){.headerlink}\

:   Set new start and count dimensions

    Parameters[:]{.colon}

    :   - **variable** -- handler for which new selection will be
          applied to

        - **ndims** -- number of dimensions for start and count

        - **start** -- new start dimensions array

        - **count** -- new count dimensions array

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv327adios2_set_memory_selectionP15adios2_variableK6size_tPK6size_tPK6size_t}[]{#_CPPv227adios2_set_memory_selectionP15adios2_variableK6size_tPK6size_tPK6size_t}[]{#adios2_set_memory_selection__adios2_variableP.sC.sCP.sCP}[]{#adios2__c__variable_8h_1ae12ec5f2f22340e749913e9f633d283a .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_set_memory_selection]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[ndims]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[memory_start]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[memory_count]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv427adios2_set_memory_selectionP15adios2_variableK6size_tPK6size_tPK6size_t "Link to this definition"){.headerlink}\

:   Set the local start (offset) point to the memory pointer passed at
    Put and the memory local dimensions (count). Used for non-contiguous
    memory writes and reads (e.g. multidimensional ghost-cells).
    Currently not working for calls to Get.

    Parameters[:]{.colon}

    :   - **variable** -- handler for which new memory selection will be
          applied to

        - **ndims** -- number of dimensions for memory_start and
          memory_count

        - **memory_start** -- relative local offset of variable.start to
          the contiguous memory pointer passed at Put from which data
          starts. e.g. if variable start = {rank\*Ny,0} and there is 1
          ghost cell per dimension, then memory_start = {1,1}

        - **memory_count** -- local dimensions for the contiguous memory
          pointer passed at adios2_put, e.g. if there is 1 ghost cell
          per dimension and variable count = {Ny,Nx}, then memory_count
          = {Ny+2,Nx+2}

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv325adios2_set_step_selectionP15adios2_variableK6size_tK6size_t}[]{#_CPPv225adios2_set_step_selectionP15adios2_variableK6size_tK6size_t}[]{#adios2_set_step_selection__adios2_variableP.sC.sC}[]{#adios2__c__variable_8h_1a96b107073f66bab664694ccd10c04f7c .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_set_step_selection]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[step_start]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[step_count]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv425adios2_set_step_selectionP15adios2_variableK6size_tK6size_t "Link to this definition"){.headerlink}\

:   Set new step selection using step_start and step_count. Used mostly
    for reading from file-based engines (e.g. bpfile, hdf5)

    Parameters[:]{.colon}

    :   - **variable** -- handler for which new selection will be
          applied to

        - **step_start** -- starting step for reading

        - **step_count** -- number of steps to read from step start

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv320adios2_variable_namePcP6size_tPK15adios2_variable}[]{#_CPPv220adios2_variable_namePcP6size_tPK15adios2_variable}[]{#adios2_variable_name__cP.sP.adios2_variableCP}[]{#adios2__c__variable_8h_1a98790c109926b79ba98df3518036fc01 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_variable_name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420adios2_variable_namePcP6size_tPK15adios2_variable "Link to this definition"){.headerlink}\

:   Retrieve variable name For safe use, call this function first with
    NULL name parameter to get the size, then preallocate the buffer
    (with room for '\\0' if desired), then call the function again with
    the buffer. Then '\\0' terminate it if desired.

    Parameters[:]{.colon}

    :   - **name** -- output, string without trailing '\\0', NULL or
          preallocated buffer

        - **size** -- output, name size without '\\0'

        - **variable** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv320adios2_variable_typeP11adios2_typePK15adios2_variable}[]{#_CPPv220adios2_variable_typeP11adios2_typePK15adios2_variable}[]{#adios2_variable_type__adios2_typeP.adios2_variableCP}[]{#adios2__c__variable_8h_1a6f48f2fec9defa64f214232ca2f38d2a .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_variable_type]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_type]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[type]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420adios2_variable_typeP11adios2_typePK15adios2_variable "Link to this definition"){.headerlink}\

:   Retrieve variable type

    Parameters[:]{.colon}

    :   - **type** -- output, from enum adios2_type

        - **variable** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv327adios2_variable_type_stringPcP6size_tPK15adios2_variable}[]{#_CPPv227adios2_variable_type_stringPcP6size_tPK15adios2_variable}[]{#adios2_variable_type_string__cP.sP.adios2_variableCP}[]{#adios2__c__variable_8h_1ab45ec627e34623a216f7dcd7040a584c .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_variable_type_string]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[type]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv427adios2_variable_type_stringPcP6size_tPK15adios2_variable "Link to this definition"){.headerlink}\

:   Retrieve variable type in string form "char", "unsigned long", etc.
    For safe use, call this function first with NULL name parameter to
    get the size, then preallocate the buffer (with room for '\\0' if
    desired), then call the function again with the buffer. Then '\\0'
    terminate it if desired.

    Parameters[:]{.colon}

    :   - **type** -- output, string without trailing '\\0', NULL or
          preallocated buffer

        - **size** -- output, type size without '\\0'

        - **variable** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv323adios2_variable_shapeidP14adios2_shapeidPK15adios2_variable}[]{#_CPPv223adios2_variable_shapeidP14adios2_shapeidPK15adios2_variable}[]{#adios2_variable_shapeid__adios2_shapeidP.adios2_variableCP}[]{#adios2__c__variable_8h_1ac7be4ef229312127dd8712b5ca2b500a .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_variable_shapeid]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_shapeid]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[shapeid]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv423adios2_variable_shapeidP14adios2_shapeidPK15adios2_variable "Link to this definition"){.headerlink}\

:   Retrieve variable shapeid

    Parameters[:]{.colon}

    :   - **shapeid** -- output, from enum adios2_shapeid

        - **variable** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv321adios2_variable_ndimsP6size_tPK15adios2_variable}[]{#_CPPv221adios2_variable_ndimsP6size_tPK15adios2_variable}[]{#adios2_variable_ndims__sP.adios2_variableCP}[]{#adios2__c__variable_8h_1aefbce6aadbb0e19b596f4c4b4c350570 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_variable_ndims]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[ndims]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_variable_ndimsP6size_tPK15adios2_variable "Link to this definition"){.headerlink}\

:   Retrieve current variable number of dimensions

    Parameters[:]{.colon}

    :   - **ndims** -- output

        - **variable** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv321adios2_variable_shapeP6size_tPK15adios2_variable}[]{#_CPPv221adios2_variable_shapeP6size_tPK15adios2_variable}[]{#adios2_variable_shape__sP.adios2_variableCP}[]{#adios2__c__variable_8h_1a6ba190f47e2a77e4f4e1fb3ea557ef29 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_variable_shape]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[shape]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_variable_shapeP6size_tPK15adios2_variable "Link to this definition"){.headerlink}\

:   Retrieve current variable shape

    Parameters[:]{.colon}

    :   - **shape** -- output, must be pre-allocated with ndims

        - **variable** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv339adios2_variable_shape_with_memory_spaceP6size_tPK15adios2_variableK19adios2_memory_space}[]{#_CPPv239adios2_variable_shape_with_memory_spaceP6size_tPK15adios2_variableK19adios2_memory_space}[]{#adios2_variable_shape_with_memory_space__sP.adios2_variableCP.adios2_memory_spaceC}[]{#adios2__c__variable_8h_1a897fb3f448f21cf3568cd7b3cd59eb0e .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_variable_shape_with_memory_space]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[shape]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_memory_space]{.pre}]{.n}[ ]{.w}[[mem]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv439adios2_variable_shape_with_memory_spaceP6size_tPK15adios2_variableK19adios2_memory_space "Link to this definition"){.headerlink}\

:   Retrieve current variable shape for a given memory space

    Parameters[:]{.colon}

    :   - **shape** -- output, must be pre-allocated with ndims

        - **variable** -- handler

        - **memory** -- space

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv321adios2_variable_startP6size_tPK15adios2_variable}[]{#_CPPv221adios2_variable_startP6size_tPK15adios2_variable}[]{#adios2_variable_start__sP.adios2_variableCP}[]{#adios2__c__variable_8h_1a9da02a33cdfe623c5c04387405662f0d .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_variable_start]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[start]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_variable_startP6size_tPK15adios2_variable "Link to this definition"){.headerlink}\

:   Retrieve current variable start

    Parameters[:]{.colon}

    :   - **start** -- output, single value

        - **variable** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv321adios2_variable_countP6size_tPK15adios2_variable}[]{#_CPPv221adios2_variable_countP6size_tPK15adios2_variable}[]{#adios2_variable_count__sP.adios2_variableCP}[]{#adios2__c__variable_8h_1ae453363240d31f72b69cf7b7b073b31f .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_variable_count]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[count]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_variable_countP6size_tPK15adios2_variable "Link to this definition"){.headerlink}\

:   Retrieve current variable start

    Parameters[:]{.colon}

    :   - **count** -- output, must be pre-allocated with ndims

        - **variable** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv327adios2_variable_steps_startP6size_tPK15adios2_variable}[]{#_CPPv227adios2_variable_steps_startP6size_tPK15adios2_variable}[]{#adios2_variable_steps_start__sP.adios2_variableCP}[]{#adios2__c__variable_8h_1a88414bbf52936e639cc0c532bdc56217 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_variable_steps_start]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[steps_start]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv427adios2_variable_steps_startP6size_tPK15adios2_variable "Link to this definition"){.headerlink}\

:   Read API, get available steps start from available steps count (e.g.
    in a file for a variable).

    Parameters[:]{.colon}

    :   - **steps_start** -- output absolute first available step, don't
          use with adios2_set_step_selection as inputs are relative, use
          0 instead.

        - **variable** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv321adios2_variable_stepsP6size_tPK15adios2_variable}[]{#_CPPv221adios2_variable_stepsP6size_tPK15adios2_variable}[]{#adios2_variable_steps__sP.adios2_variableCP}[]{#adios2__c__variable_8h_1a89cd0af54d34751b96da197620fd1204 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_variable_steps]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[steps]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_variable_stepsP6size_tPK15adios2_variable "Link to this definition"){.headerlink}\

:   Read API, get available steps count from available steps count (e.g.
    in a file for a variable). Not necessarily contiguous.

    Parameters[:]{.colon}

    :   - **steps** -- output available steps, single value

        - **variable** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv321adios2_selection_sizeP6size_tPK15adios2_variable}[]{#_CPPv221adios2_selection_sizeP6size_tPK15adios2_variable}[]{#adios2_selection_size__sP.adios2_variableCP}[]{#adios2__c__variable_8h_1a7ef1c09116114294000993c5f99e9778 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_selection_size]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_selection_sizeP6size_tPK15adios2_variable "Link to this definition"){.headerlink}\

:   Returns the minimum required allocation (in number of elements of a
    certain type, not bytes) for the current selection

    Parameters[:]{.colon}

    :   - **size** -- number of elements of current type to be allocated
          by a pointer/vector to read current selection

        - **variable** -- handler for which data size will be inspected
          from

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv320adios2_add_operationP6size_tP15adios2_variableP15adios2_operatorPKcPKc}[]{#_CPPv220adios2_add_operationP6size_tP15adios2_variableP15adios2_operatorPKcPKc}[]{#adios2_add_operation__sP.adios2_variableP.adios2_operatorP.cCP.cCP}[]{#adios2__c__variable_8h_1a5afac7fe1b0f9119239b062030ceefe9 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_add_operation]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[operation_index]{.pre}]{.n .sig-param}, [[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[adios2_operator]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[op]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[key]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420adios2_add_operationP6size_tP15adios2_variableP15adios2_operatorPKcPKc "Link to this definition"){.headerlink}\

:   Adds an operation to a variable (e.g. compression)

    Parameters[:]{.colon}

    :   - **operation_index** -- output handler to be used with
          adios2_add_operation_param

        - **variable** -- handler on which operation is applied to

        - **op** -- handler to adios2_operator associated to current
          operation

        - **key** -- parameter key supported by the operation, empty if
          none

        - **value** -- parameter value supported by the operation, empty
          if none

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv330adios2_set_operation_parameterP15adios2_variableK6size_tPKcPKc}[]{#_CPPv230adios2_set_operation_parameterP15adios2_variableK6size_tPKcPKc}[]{#adios2_set_operation_parameter__adios2_variableP.sC.cCP.cCP}[]{#adios2__c__variable_8h_1a736746eb00b039765b8432ab249110f1 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_set_operation_parameter]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[operation_id]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[key]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv430adios2_set_operation_parameterP15adios2_variableK6size_tPKcPKc "Link to this definition"){.headerlink}\

:   Adds a parameter to an operation created with adios2_add_operation

    Parameters[:]{.colon}

    :   - **variable** -- handler on which operation is applied to

        - **operation_id** -- handler returned from adios2_add_operation

        - **key** -- parameter key supported by the operation

        - **value** -- parameter value supported by the operation

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv324adios2_remove_operationsP15adios2_variable}[]{#_CPPv224adios2_remove_operationsP15adios2_variable}[]{#adios2_remove_operations__adios2_variableP}[]{#adios2__c__variable_8h_1a1eb285c3ef46735a7e06cc577d4d2c74 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_remove_operations]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv424adios2_remove_operationsP15adios2_variable "Link to this definition"){.headerlink}\

:   Removes all current Operations associated with AddOperation.
    Provides the posibility to apply or not operators on a block basis.

    Parameters[:]{.colon}

    :   **variable** -- handler on which operation is applied to

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv319adios2_variable_minPvPK15adios2_variable}[]{#_CPPv219adios2_variable_minPvPK15adios2_variable}[]{#adios2_variable_min__voidP.adios2_variableCP}[]{#adios2__c__variable_8h_1a207fba966e8e4ef66598a274c223d531 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_variable_min]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[min]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419adios2_variable_minPvPK15adios2_variable "Link to this definition"){.headerlink}\

:   Read mode only: return the absolute minimum for current variable

    Parameters[:]{.colon}

    :   - **min** -- output: variable minimum, must be of the same type
          as the variable handler

        - **variable** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv319adios2_variable_maxPvPK15adios2_variable}[]{#_CPPv219adios2_variable_maxPvPK15adios2_variable}[]{#adios2_variable_max__voidP.adios2_variableCP}[]{#adios2__c__variable_8h_1aee8ebf3a43b79fdb2d8d75a354162eef .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_variable_max]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[max]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419adios2_variable_maxPvPK15adios2_variable "Link to this definition"){.headerlink}\

:   Read mode only: return the absolute maximum for current variable

    Parameters[:]{.colon}

    :   - **max** -- output: variable minimum, must be of the same type
          as the variable handler

        - **variable** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors
:::
::::

:::: {#adios2-attribute-handler-functions .section}
#### [`adios2_attribute`{.docutils .literal .notranslate}]{.pre} handler functions[](#adios2-attribute-handler-functions "Link to this heading"){.headerlink}

::: {.breathe-sectiondef .docutils .container}
Functions

[]{#_CPPv321adios2_attribute_namePcP6size_tPK16adios2_attribute}[]{#_CPPv221adios2_attribute_namePcP6size_tPK16adios2_attribute}[]{#adios2_attribute_name__cP.sP.adios2_attributeCP}[]{#adios2__c__attribute_8h_1afc69319ec2b4a5452a33b1f78fa00a5e .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_attribute_name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[attribute]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_attribute_namePcP6size_tPK16adios2_attribute "Link to this definition"){.headerlink}\

:   Retrieve attribute name For safe use, call this function first with
    NULL name parameter to get the size, then preallocate the buffer
    (with room for '\\0' if desired), then call the function again with
    the buffer. Then '\\0' terminate it if desired.

    Parameters[:]{.colon}

    :   - **name** -- output, string without trailing '\\0', NULL or
          preallocated buffer

        - **size** -- output, name size without '\\0'

        - **attribute** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv321adios2_attribute_typeP11adios2_typePK16adios2_attribute}[]{#_CPPv221adios2_attribute_typeP11adios2_typePK16adios2_attribute}[]{#adios2_attribute_type__adios2_typeP.adios2_attributeCP}[]{#adios2__c__attribute_8h_1a5eb4c132a47caaf15110fcc9001b32a8 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_attribute_type]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_type]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[type]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[attribute]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_attribute_typeP11adios2_typePK16adios2_attribute "Link to this definition"){.headerlink}\

:   Retrieve attribute type

    Parameters[:]{.colon}

    :   - **type** --

        - **attribute** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv328adios2_attribute_type_stringPcP6size_tPK16adios2_attribute}[]{#_CPPv228adios2_attribute_type_stringPcP6size_tPK16adios2_attribute}[]{#adios2_attribute_type_string__cP.sP.adios2_attributeCP}[]{#adios2__c__attribute_8h_1aedc91c9bb911e02465418431bcc205d3 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_attribute_type_string]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[type]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[attribute]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv428adios2_attribute_type_stringPcP6size_tPK16adios2_attribute "Link to this definition"){.headerlink}\

:   Retrieve attribute type in string form "char", "unsigned long", etc.
    For safe use, call this function first with NULL name parameter to
    get the size, then preallocate the buffer (with room for '\\0' if
    desired), then call the function again with the buffer. Then '\\0'
    terminate it if desired.

    Parameters[:]{.colon}

    :   - **type** -- output, string without trailing '\\0', NULL or
          preallocated buffer

        - **size** -- output, type size without '\\0'

        - **attribute** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv325adios2_attribute_is_valueP11adios2_boolPK16adios2_attribute}[]{#_CPPv225adios2_attribute_is_valueP11adios2_boolPK16adios2_attribute}[]{#adios2_attribute_is_value__adios2_boolP.adios2_attributeCP}[]{#adios2__c__attribute_8h_1a32330f8cfd9492a2ff1f631f5aac8306 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_attribute_is_value]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_bool]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[result]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[attribute]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv425adios2_attribute_is_valueP11adios2_boolPK16adios2_attribute "Link to this definition"){.headerlink}\

:   Checks if attribute is a single value or an array

    Parameters[:]{.colon}

    :   - **result** -- output, adios2_true: single value, adios2_false:
          array

        - **attribute** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv321adios2_attribute_sizeP6size_tPK16adios2_attribute}[]{#_CPPv221adios2_attribute_sizeP6size_tPK16adios2_attribute}[]{#adios2_attribute_size__sP.adios2_attributeCP}[]{#adios2__c__attribute_8h_1afcf1d3ab2dcba21434c94f1c41e1e3af .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_attribute_size]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[attribute]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_attribute_sizeP6size_tPK16adios2_attribute "Link to this definition"){.headerlink}\

:   Returns the number of elements (as in C++ STL size() function) if
    attribute is a 1D array. If single value returns 1

    Parameters[:]{.colon}

    :   - **size** -- output, number of elements in attribute

        - **attribute** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv321adios2_attribute_dataPvP6size_tPK16adios2_attribute}[]{#_CPPv221adios2_attribute_dataPvP6size_tPK16adios2_attribute}[]{#adios2_attribute_data__voidP.sP.adios2_attributeCP}[]{#adios2__c__attribute_8h_1a7379b71d2be634bfe53ebaa0016ad817 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_attribute_data]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_attribute]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[attribute]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_attribute_dataPvP6size_tPK16adios2_attribute "Link to this definition"){.headerlink}\

:   Retrieve attribute data pointer (read-only)

    Parameters[:]{.colon}

    :   - **data** -- output attribute values, must be pre-allocated

        - **size** -- data size

        - **attribute** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors
:::
::::

:::: {#adios2-engine-handler-functions .section}
#### [`adios2_engine`{.docutils .literal .notranslate}]{.pre} handler functions[](#adios2-engine-handler-functions "Link to this heading"){.headerlink}

::: {.breathe-sectiondef .docutils .container}
Functions

[]{#_CPPv318adios2_engine_namePcP6size_tPK13adios2_engine}[]{#_CPPv218adios2_engine_namePcP6size_tPK13adios2_engine}[]{#adios2_engine_name__cP.sP.adios2_engineCP}[]{#adios2__c__engine_8h_1acbd4dc2dd032fc6d07525b74d5eea350 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_engine_name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv418adios2_engine_namePcP6size_tPK13adios2_engine "Link to this definition"){.headerlink}\

:   Return engine name string and length without '\\0\\ character For
    safe use, call this function first with NULL name parameter to get
    the size, then preallocate the buffer (with room for '\\0' if
    desired), then call the function again with the buffer. Then '\\0'
    terminate it if desired.

    Parameters[:]{.colon}

    :   - **name** -- output, string without trailing '\\0', NULL or
          preallocated buffer

        - **size** -- output, engine_type size without '\\0'

        - **engine** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv322adios2_engine_get_typePcP6size_tPK13adios2_engine}[]{#_CPPv222adios2_engine_get_typePcP6size_tPK13adios2_engine}[]{#adios2_engine_get_type__cP.sP.adios2_engineCP}[]{#adios2__c__engine_8h_1abdfc35e7ce3d0f4d909d43a2e3390a0d .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_engine_get_type]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[type]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv422adios2_engine_get_typePcP6size_tPK13adios2_engine "Link to this definition"){.headerlink}\

:   Return engine type string and length without '\\0\\ character For
    safe use, call this function first with NULL name parameter to get
    the size, then preallocate the buffer (with room for '\\0' if
    desired), then call the function again with the buffer. Then '\\0'
    terminate it if desired.

    Parameters[:]{.colon}

    :   - **type** -- output, string without trailing '\\0', NULL or
          preallocated buffer

        - **size** -- output, engine_type size without '\\0'

        - **engine** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv322adios2_engine_openmodeP11adios2_modePK13adios2_engine}[]{#_CPPv222adios2_engine_openmodeP11adios2_modePK13adios2_engine}[]{#adios2_engine_openmode__adios2_modeP.adios2_engineCP}[]{#adios2__c__engine_8h_1af67494757e8a8743570b17ff3d4a4e27 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_engine_openmode]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_mode]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[mode]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv422adios2_engine_openmodeP11adios2_modePK13adios2_engine "Link to this definition"){.headerlink}\

:   Return the engine's Open mode.

    Parameters[:]{.colon}

    :   - **mode** -- output, adios2_mode parameter used in
          [[adios2_open()]{.std
          .std-ref}](#document-api_full/api_full#adios2__c__io_8h_1ad62726c408b5e67c5ab87e50c41d0f9d){.reference
          .internal}

        - **engine** -- handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv326adios2_engine_get_metadataP13adios2_enginePPcP6size_t}[]{#_CPPv226adios2_engine_get_metadataP13adios2_enginePPcP6size_t}[]{#adios2_engine_get_metadata__adios2_engineP.cPP.sP}[]{#adios2__c__engine_8h_1a6411f972c86be15b1d5e6d00c5970cca .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_engine_get_metadata]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}, [[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[\*]{.pre}]{.p}[[md]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv426adios2_engine_get_metadataP13adios2_enginePPcP6size_t "Link to this definition"){.headerlink}\

:   Serialize all metadata right after engine is created, which can be
    delivered to other processes to open the same file for reading
    without opening and reading in metadata again.

    Returns[:]{.colon}

    :   metadata (pointer to allocated memory) and size of metadata the
        pointer must be deallocated by user using free()

<!-- -->

[]{#_CPPv317adios2_begin_stepP13adios2_engineK16adios2_step_modeKfP18adios2_step_status}[]{#_CPPv217adios2_begin_stepP13adios2_engineK16adios2_step_modeKfP18adios2_step_status}[]{#adios2_begin_step__adios2_engineP.adios2_step_modeC.floatC.adios2_step_statusP}[]{#adios2__c__engine_8h_1addcba1f987c4ecb5315057899dcf273f .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_begin_step]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_step_mode]{.pre}]{.n}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[float]{.pre}]{.kt}[ ]{.w}[[timeout_seconds]{.pre}]{.n .sig-param}, [[adios2_step_status]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[status]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv417adios2_begin_stepP13adios2_engineK16adios2_step_modeKfP18adios2_step_status "Link to this definition"){.headerlink}\

:   Begin a logical adios2 step stream Check each engine documentation
    for MPI collective/non-collective behavior.

    Parameters[:]{.colon}

    :   - **engine** -- handler

        - **mode** -- see enum adios2_step_mode in adios2_c_types.h for
          options, read is the common use case

        - **timeout_seconds** -- provide a time out in Engine opened in
          read mode

        - **status** -- output from enum adios2_step_status in
          adios2_c_types.h

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv319adios2_current_stepP6size_tPK13adios2_engine}[]{#_CPPv219adios2_current_stepP6size_tPK13adios2_engine}[]{#adios2_current_step__sP.adios2_engineCP}[]{#adios2__c__engine_8h_1a3238e7f8b99c2a2bec0aef0dedc607db .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_current_step]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[current_step]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419adios2_current_stepP6size_tPK13adios2_engine "Link to this definition"){.headerlink}\

:   Inspect current logical step

    Parameters[:]{.colon}

    :   - **current_step** -- output

        - **engine** -- input handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv325adios2_between_step_pairsP6size_tPK13adios2_engine}[]{#_CPPv225adios2_between_step_pairsP6size_tPK13adios2_engine}[]{#adios2_between_step_pairs__sP.adios2_engineCP}[]{#adios2__c__engine_8h_1ad752bf9fd087651b5eb8733a4598ff0a .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_between_step_pairs]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[between_step_pairs]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv425adios2_between_step_pairsP6size_tPK13adios2_engine "Link to this definition"){.headerlink}\

:   Inspect current between step status

    Parameters[:]{.colon}

    :   - **between_step_pairs** -- output boolean

        - **engine** -- input handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv312adios2_stepsP6size_tPK13adios2_engine}[]{#_CPPv212adios2_stepsP6size_tPK13adios2_engine}[]{#adios2_steps__sP.adios2_engineCP}[]{#adios2__c__engine_8h_1aa5f48f32717400d5127476e45cdc4ef8 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_steps]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[steps]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv412adios2_stepsP6size_tPK13adios2_engine "Link to this definition"){.headerlink}\

:   Inspect total number of available steps, use for file engines in
    read mode only

    Parameters[:]{.colon}

    :   - **steps** -- output available steps in engine

        - **engine** -- input handler

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv310adios2_putP13adios2_engineP15adios2_variablePKvK11adios2_mode}[]{#_CPPv210adios2_putP13adios2_engineP15adios2_variablePKvK11adios2_mode}[]{#adios2_put__adios2_engineP.adios2_variableP.voidCP.adios2_modeC}[]{#adios2__c__engine_8h_1a3a16a08bb32ce05de16d8de0c1985d75 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_put]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}, [[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv410adios2_putP13adios2_engineP15adios2_variablePKvK11adios2_mode "Link to this definition"){.headerlink}\

:   Put data associated with a Variable in an engine, used for engines
    with adios2_mode_write at adios2_open

    Parameters[:]{.colon}

    :   - **engine** -- handler for a particular engine where data will
          be put

        - **variable** -- contains variable metadata information

        - **data** -- user data to be associated with a variable, must
          be the same type passed to adios2_define_variable

        - **launch** -- mode launch policy

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv318adios2_put_by_nameP13adios2_enginePKcPKvK11adios2_mode}[]{#_CPPv218adios2_put_by_nameP13adios2_enginePKcPKvK11adios2_mode}[]{#adios2_put_by_name__adios2_engineP.cCP.voidCP.adios2_modeC}[]{#adios2__c__engine_8h_1a0edb4c5f751d58428adbd7eab3452b63 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_put_by_name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[variable_name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv418adios2_put_by_nameP13adios2_enginePKcPKvK11adios2_mode "Link to this definition"){.headerlink}\

:   Put data associated with a Variable in an engine, used for engines
    with adios2_mode_write at adios2_open. This is the name string
    version

    Parameters[:]{.colon}

    :   - **engine** -- handler for a particular engine where data will
          be put

        - **variable_name** -- variable with this name must exists in
          adios2_io that opened the engine handler (1st parameter)

        - **data** -- user data to be associated with a variable, must
          be the same type passed to adios2_define_variable

        - **launch** -- mode launch policy

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv319adios2_perform_putsP13adios2_engine}[]{#_CPPv219adios2_perform_putsP13adios2_engine}[]{#adios2_perform_puts__adios2_engineP}[]{#adios2__c__engine_8h_1ab312c90d358452cf6cbf3c355ea8758d .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_perform_puts]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419adios2_perform_putsP13adios2_engine "Link to this definition"){.headerlink}\

:   Performs all the adios2_put and adios2_put_by_name called with mode
    adios2_mode_deferred, up to this point, by copying user data into
    internal ADIOS buffers. User data can be reused after this point.

    Parameters[:]{.colon}

    :   **engine** -- handler for a particular engine where data will be
        put

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv325adios2_perform_data_writeP13adios2_engine}[]{#_CPPv225adios2_perform_data_writeP13adios2_engine}[]{#adios2_perform_data_write__adios2_engineP}[]{#adios2__c__engine_8h_1a980fd541d3d1a6d2efe61125869d2613 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_perform_data_write]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv425adios2_perform_data_writeP13adios2_engine "Link to this definition"){.headerlink}\

:   Write array data to disk. This may relieve memory pressure by
    clearing ADIOS buffers. It is a collective call. User data can be
    reused after this point.

    Parameters[:]{.colon}

    :   **engine** -- handler for a particular engine where data will be
        put

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv310adios2_getP13adios2_engineP15adios2_variablePvK11adios2_mode}[]{#_CPPv210adios2_getP13adios2_engineP15adios2_variablePvK11adios2_mode}[]{#adios2_get__adios2_engineP.adios2_variableP.voidP.adios2_modeC}[]{#adios2__c__engine_8h_1aea5950560897326ebd5b3f6b93b70802 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_get]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}, [[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv410adios2_getP13adios2_engineP15adios2_variablePvK11adios2_mode "Link to this definition"){.headerlink}\

:   Gets data associated with a Variable from an engine, used for
    engines with adios2_mode_read at adios2_open. This is the name
    string version

    Parameters[:]{.colon}

    :   - **engine** -- handler for a particular engine where data will
          be put

        - **variable** -- handler must exists in adios2_io that opened
          the engine handler (1st parameter). Typically from
          adios2_inquire_variable

        - **data** -- user data to be associated with a variable, must
          be the same type passed to adios2_define_variable. Must be
          pre-allocated for the required variable selection.

        - **launch** -- mode launch policy

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv318adios2_get_by_nameP13adios2_enginePKcPvK11adios2_mode}[]{#_CPPv218adios2_get_by_nameP13adios2_enginePKcPvK11adios2_mode}[]{#adios2_get_by_name__adios2_engineP.cCP.voidP.adios2_modeC}[]{#adios2__c__engine_8h_1ac36bc3e149bf46afcc10602080bdd4a2 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_get_by_name]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[variable_name]{.pre}]{.n .sig-param}, [[void]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_mode]{.pre}]{.n}[ ]{.w}[[launch]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv418adios2_get_by_nameP13adios2_enginePKcPvK11adios2_mode "Link to this definition"){.headerlink}\

:   Gets data associated with a Variable from an engine, used for
    engines with adios2_mode_read at adios2_open. This is the name
    string version

    Parameters[:]{.colon}

    :   - **engine** -- handler for a particular engine where data will
          be put

        - **variable_name** -- variable with this name must exists in
          adios2_io that opened the engine handler (1st parameter).

        - **data** -- user data to be associated with a variable, must
          be the same type passed to adios2_define_variable. Must be
          pre-allocated for the required variable selection.

        - **launch** -- mode launch policy

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv319adios2_perform_getsP13adios2_engine}[]{#_CPPv219adios2_perform_getsP13adios2_engine}[]{#adios2_perform_gets__adios2_engineP}[]{#adios2__c__engine_8h_1a6be6eaa1b32c2efe386c5bf9bd0300fc .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_perform_gets]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv419adios2_perform_getsP13adios2_engine "Link to this definition"){.headerlink}\

:   Performs all the adios2_get and adios2_get_by_name called with mode
    adios2_mode_deferred up to this point by getting the data from the
    Engine. User data can be reused after this point.

    Parameters[:]{.colon}

    :   **engine** -- handler for a particular engine where data will be
        obtained

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv315adios2_end_stepP13adios2_engine}[]{#_CPPv215adios2_end_stepP13adios2_engine}[]{#adios2_end_step__adios2_engineP}[]{#adios2__c__engine_8h_1a7ce97dee3c0e977e8f7fc607e75e1ef8 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_end_step]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv415adios2_end_stepP13adios2_engine "Link to this definition"){.headerlink}\

:   Terminates interaction with current step. By default puts/gets data
    to/from all transports Check each engine documentation for MPI
    collective/non-collective behavior.

    Parameters[:]{.colon}

    :   **engine** -- handler executing IO tasks

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv312adios2_flushP13adios2_engine}[]{#_CPPv212adios2_flushP13adios2_engine}[]{#adios2_flush__adios2_engineP}[]{#adios2__c__engine_8h_1a161a07d679829e3756e3b9bd5b1569a4 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_flush]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv412adios2_flushP13adios2_engine "Link to this definition"){.headerlink}\

:   Explicit engine buffer flush to transports

    Parameters[:]{.colon}

    :   **engine** -- input

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv321adios2_flush_by_indexP13adios2_engineKi}[]{#_CPPv221adios2_flush_by_indexP13adios2_engineKi}[]{#adios2_flush_by_index__adios2_engineP.iC}[]{#adios2__c__engine_8h_1a93e4acd4bdcb0b60a42d3f4041e9d8f3 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_flush_by_index]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[transport_index]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_flush_by_indexP13adios2_engineKi "Link to this definition"){.headerlink}\

:   Explicit engine buffer flush to transport index

    Parameters[:]{.colon}

    :   - **engine** -- input

        - **transport_index** -- index to be flushed

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv312adios2_closeP13adios2_engine}[]{#_CPPv212adios2_closeP13adios2_engine}[]{#adios2_close__adios2_engineP}[]{#adios2__c__engine_8h_1a739d5ce696b2e77805d5a7302b97e4fa .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_close]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv412adios2_closeP13adios2_engine "Link to this definition"){.headerlink}\

:   Close all transports in adios2_Engine. Call is required to close
    system resources. MPI Collective, calls MPI_Comm_free for duplicated
    communicator at Open

    Parameters[:]{.colon}

    :   **engine** -- handler containing all transports to be closed.
        NOTE: engines NEVER become NULL after this function is called.

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv321adios2_close_by_indexP13adios2_engineKi}[]{#_CPPv221adios2_close_by_indexP13adios2_engineKi}[]{#adios2_close_by_index__adios2_engineP.iC}[]{#adios2__c__engine_8h_1a82c0086dc85f15f51a2e18c21dc37565 .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_close_by_index]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[transport_index]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_close_by_indexP13adios2_engineKi "Link to this definition"){.headerlink}\

:   Close a particular transport from the index returned by
    adios2_add_transport

    Parameters[:]{.colon}

    :   - **engine** -- handler containing all transports to be closed.
          NOTE: engines NEVER become NULL due to this function.

        - **transport_index** -- handler from adios2_add_transport

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors

<!-- -->

[]{#_CPPv330adios2_lock_writer_definitionsP13adios2_engine}[]{#_CPPv230adios2_lock_writer_definitionsP13adios2_engine}[]{#adios2_lock_writer_definitions__adios2_engineP}[]{#adios2__c__engine_8h_1abc305184570316904c9b12bd2b6bb20f .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_lock_writer_definitions]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv430adios2_lock_writer_definitionsP13adios2_engine "Link to this definition"){.headerlink}\

:   Promise that no more definitions or changes to defined variables
    will occur. Useful information if called before the first
    [[adios2_end_step()]{.std
    .std-ref}](#document-api_full/api_full#adios2__c__engine_8h_1a7ce97dee3c0e977e8f7fc607e75e1ef8){.reference
    .internal} of an output Engine, as it will know that the definitions
    are complete and constant for the entire lifetime of the output and
    may optimize metadata handling.

    Parameters[:]{.colon}

    :   **engine** -- handler

<!-- -->

[]{#_CPPv329adios2_lock_reader_selectionsP13adios2_engine}[]{#_CPPv229adios2_lock_reader_selectionsP13adios2_engine}[]{#adios2_lock_reader_selections__adios2_engineP}[]{#adios2__c__engine_8h_1a404de73cdb98f12f9ddf1c8b2787679c .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_lock_reader_selections]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv429adios2_lock_reader_selectionsP13adios2_engine "Link to this definition"){.headerlink}\

:   Promise that the reader data selections of are fixed and will not
    change in future timesteps. This information, provided before the
    EndStep() representing a fixed read pattern, may be utilized by the
    input Engine to optimize data flow.

    Parameters[:]{.colon}

    :   **engine** -- handler

<!-- -->

[]{#_CPPv324adios2_inquire_blockinfoP13adios2_engineP15adios2_variableK6size_t}[]{#_CPPv224adios2_inquire_blockinfoP13adios2_engineP15adios2_variableK6size_t}[]{#adios2_inquire_blockinfo__adios2_engineP.adios2_variableP.sC}[]{#adios2__c__engine_8h_1a403784317a69d8f480ff9702c8ae7e4b .target}[[adios2_varinfo]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[[adios2_inquire_blockinfo]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_engine]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[engine]{.pre}]{.n .sig-param}, [[adios2_variable]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[variable]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[step]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv424adios2_inquire_blockinfoP13adios2_engineP15adios2_variableK6size_t "Link to this definition"){.headerlink}\

:   Get the list of blocks for a variable in a given step. In Streaming
    mode, step is unused, always the current step is processed.

    Returns[:]{.colon}

    :   Newly allocated adios2_varinfo structure, NULL pointer if step
        does not exist. The memory must be freed by the
        adios2_free_blockinfo function

<!-- -->

[]{#_CPPv321adios2_free_blockinfoP14adios2_varinfo}[]{#_CPPv221adios2_free_blockinfoP14adios2_varinfo}[]{#adios2_free_blockinfo__adios2_varinfoP}[]{#adios2__c__engine_8h_1a9ddddd82b9be9fae8c13195e27eba7f4 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[adios2_free_blockinfo]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2_varinfo]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[data_blocks]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv421adios2_free_blockinfoP14adios2_varinfo "Link to this definition"){.headerlink}\

:   free adios2_varinfo structure

    Parameters[:]{.colon}

    :   **data_blocks** --

    Returns[:]{.colon}

    :   void
:::
::::

:::: {#adios2-operator-handler-functions .section}
#### [`adios2_operator`{.docutils .literal .notranslate}]{.pre} handler functions[](#adios2-operator-handler-functions "Link to this heading"){.headerlink}

::: {.breathe-sectiondef .docutils .container}
Functions

[]{#_CPPv320adios2_operator_typePcP6size_tPK15adios2_operator}[]{#_CPPv220adios2_operator_typePcP6size_tPK15adios2_operator}[]{#adios2_operator_type__cP.sP.adios2_operatorCP}[]{#adios2__c__operator_8h_1a3016a712081407fe3f146a245cfeec8d .target}[[adios2_error]{.pre}]{.n}[ ]{.w}[[[adios2_operator_type]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[char]{.pre}]{.kt}[ ]{.w}[[\*]{.pre}]{.p}[[type]{.pre}]{.n .sig-param}, [[size_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2_operator]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[op]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv420adios2_operator_typePcP6size_tPK15adios2_operator "Link to this definition"){.headerlink}\

:   Retrieve operator type For safe use, call this function first with
    NULL name parameter to get the size, then preallocate the buffer
    (with room for '\\0' if desired), then call the function again with
    the buffer. Then '\\0' terminate it if desired.

    Parameters[:]{.colon}

    :   - **type** -- output, string without trailing '\\0', NULL or
          preallocated buffer

        - **size** -- output, type size without '\\0'

        - **op** -- operator handler to be inspected

    Returns[:]{.colon}

    :   adios2_error 0: success, see enum adios2_error for errors
:::
::::
:::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

[]{#document-api_high/api_high}

:::::::::::::::::::::: {#high-level-apis .section}
## High-Level APIs[](#high-level-apis "Link to this heading"){.headerlink}

The high-level APIs are designed for simple tasks for which performance
is not critical. Unlike the [[Full APIs]{.std
.std-ref}](#document-api_full/api_full#full-apis){.reference .internal},
the high-level APIs only require a single object handler resembling a
C++ fstream or a Python file I/O idiom. The high-level APIs are
recommended to both first-time and advanced users; the low-level APIs
being recommended only when performance testing identifies a bottleneck
or when more control is needed.

Typical scenarios for using the simple high-level APIs are:

- Reading a file to perform data analysis with libraries (matplotlib,
  scipy, etc.)

- Interactive: few calls make interactive usage easier.

- Saving data to files is small or personal projects

- Online frameworks: *e.g.* Jupyter notebooks, see python-mpi examples
  running on
  [MyBinder](https://mybinder.org/v2/gh/ornladios/ADIOS2-Jupyter.git/python-mpi){.reference
  .external}

The designed functionality syntax is closely related to the native
language IO bindings for formatted text files *e.g.* C++
[`fstream`{.docutils .literal .notranslate}]{.pre} [`getline`{.docutils
.literal .notranslate}]{.pre}, and Python file IO. The main function
calls are: [`open`{.docutils .literal .notranslate}]{.pre} (or
constructor in C++), [`write`{.docutils .literal .notranslate}]{.pre},
[`read`{.docutils .literal .notranslate}]{.pre} and [`close`{.docutils
.literal .notranslate}]{.pre} (or destructor in C++). In addition,
ADIOS2 borrows the corresponding language native syntax for advancing
lines to advance the step in write mode, and for a "step-by-step"
streaming basis in read mode. See each language section in this chapter
for a write/read example.

::: {.admonition .note}
Note

The simplified APIs are based on language native file IO interface.
Hence [`write`{.docutils .literal .notranslate}]{.pre} and
[`read`{.docutils .literal .notranslate}]{.pre} calls are always
synchronized and variables data memory is ready to use immediately after
these calls.
:::

Currently ADIOS2 support bindings for the following languages and their
minimum standards:

  ---------- ---------- -------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------
  Language   Standard   Interface                                                                                                                                    Based on
  C++        11/newer   [`#include`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`adios2.h`{.docutils .literal .notranslate}]{.pre}   [`fstream`{.docutils .literal .notranslate}]{.pre}
  Matlab                                                                                                                                                             
  ---------- ---------- -------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------

The following sections provide a summary of the API calls on each
language and links to Write and Read examples to put it all together.

::::::::::: {#c-high-level-api .section}
### C++ High-Level API[](#c-high-level-api "Link to this heading"){.headerlink}

C++11 High-Level APIs are based on a single object adios2::fstream

::: {.admonition .caution}
Caution

DO NOT place [`use`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`namespace`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`adios2`{.docutils .literal .notranslate}]{.pre} in your
C++ code. Use [`adios2::fstream`{.docutils .literal .notranslate}]{.pre}
directly to prevent conflicts with [`std::fstream`{.docutils .literal
.notranslate}]{.pre}.
:::

::::: {#c-11-write-example .section}
#### C++11 Write example[](#c-11-write-example "Link to this heading"){.headerlink}

:::: {.highlight-c++ .notranslate}
::: highlight
    #include <adios2.h>
    ...

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Nx, Ny from application, std::size_t
    const adios2::Dims shape{Nx, Ny * static_cast<std::size_t>(size)};
    const adios2::Dims start{0, Ny * static_cast<std::size_t>(rank)};
    const adios2::Dims count{Nx, Ny};

    adios2::fstream oStream("cfd.bp", adios2::fstream::out, MPI_COMM_WORLD);

    // NSteps from application
    for (std::size_t step = 0; step < NSteps; ++step)
    {
        if(rank == 0 && step == 0) // global variable
        {
            oStream.write<int32_t>("size", size);
        }

        // physicalTime double, <double> is optional
        oStream.write<double>( "physicalTime", physicalTime );
        // T and P are std::vector<float>
        oStream.write( "temperature", T.data(), shape, start, count );
        // adios2::endl will advance the step after writing pressure
        oStream.write( "pressure", P.data(), shape, start, count, adios2::end_step );

    }

    // Calling close is mandatory!
    oStream.close();
:::
::::
:::::

::::: {#c-11-read-step-by-step-example .section}
#### C++11 Read "step-by-step" example[](#c-11-read-step-by-step-example "Link to this heading"){.headerlink}

:::: {.highlight-c++ .notranslate}
::: highlight
    #include <adios2.h>
    ...

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Selection Window from application, std::size_t
    const adios2::Dims start{0, 0};
    const adios2::Dims count{SelX, SelY};

    if( rank == 0)
    {
       // if only one rank is active use MPI_COMM_SELF
       adios2::fstream iStream("cfd.bp", adios2::fstream::in, MPI_COMM_SELF);

       adios2::fstep iStep;
       while (adios2::getstep(iStream, iStep))
       {
           if( iStep.currentstep() == 0 )
           {
               const std::size_t sizeOriginal = iStep.read<std::size_t>("size");
           }
           const double physicalTime = iStream.read<double>( "physicalTime");
           const std::vector<float> temperature = iStream.read<float>( "temperature", start, count );
           const std::vector<float> pressure = iStream.read<float>( "pressure", start, count );
       }
       // Don't forget to call close!
       iStream.close();
    }
:::
::::
:::::

::: {#adios2-fstream-api-documentation .section}
#### [`adios2::fstream`{.docutils .literal .notranslate}]{.pre} API documentation[](#adios2-fstream-api-documentation "Link to this heading"){.headerlink}

[]{#_CPPv3N6adios27fstreamE}[]{#_CPPv2N6adios27fstreamE}[]{#adios2::fstream}[]{#classadios2_1_1fstream .target}[[class]{.pre}]{.k}[ ]{.w}[[[fstream]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios27fstreamE "Link to this definition"){.headerlink}\

:   ::: {.breathe-sectiondef .docutils .container}
    Public Types

    []{#_CPPv3N6adios27fstream8openmodeE}[]{#_CPPv2N6adios27fstream8openmodeE}[]{#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778 .target}[[enum]{.pre}]{.k}[ ]{.w}[[[openmode]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios27fstream8openmodeE "Link to this definition"){.headerlink}\

    :   Available open modes for [[adios2::fstream]{.std
        .std-ref}](#document-api_high/api_high#classadios2_1_1fstream){.reference
        .internal} constructor or open calls

        *Values:*

        []{#_CPPv3N6adios27fstream8openmode3outE}[]{#_CPPv2N6adios27fstream8openmode3outE}[]{#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a5f6580d512d031c2cb1a73b5fc588f19 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[out]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios27fstream8openmode3outE "Link to this definition"){.headerlink}\

        :   write

        []{#_CPPv3N6adios27fstream8openmode2inE}[]{#_CPPv2N6adios27fstream8openmode2inE}[]{#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a3976d416b45edb2af5088ba11608e081 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[in]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios27fstream8openmode2inE "Link to this definition"){.headerlink}\

        :   read

        []{#_CPPv3N6adios27fstream8openmode16in_random_accessE}[]{#_CPPv2N6adios27fstream8openmode16in_random_accessE}[]{#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778acad624b0d914980c233eb8c0541fd182 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[in_random_access]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios27fstream8openmode16in_random_accessE "Link to this definition"){.headerlink}\

        :   read_random_access

        []{#_CPPv3N6adios27fstream8openmode3appE}[]{#_CPPv2N6adios27fstream8openmode3appE}[]{#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a9a735db3e465ea6da68f022da6eb6a52 .target}[[enumerator]{.pre}]{.k}[ ]{.w}[[[app]{.pre}]{.n}]{.sig-name .descname}[](#_CPPv4N6adios27fstream8openmode3appE "Link to this definition"){.headerlink}\

        :   append, not yet supported
    :::

    ::: {.breathe-sectiondef .docutils .container}
    Public Functions

    []{#_CPPv3N6adios27fstream7fstreamERKNSt6stringEN6adios27fstream8openmodeE8MPI_CommKNSt6stringE}[]{#_CPPv2N6adios27fstream7fstreamERKNSt6stringEN6adios27fstream8openmodeE8MPI_CommKNSt6stringE}[]{#adios2::fstream::fstream__ssCR.adios2::fstream::openmode.MPI_Comm.ssC}[]{#classadios2_1_1fstream_1a935016ba85216f6160d469e9b258ab37 .target}[[[fstream]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[[fstream]{.pre}]{.n}](#document-api_high/api_high#_CPPv4N6adios27fstreamE "adios2::fstream"){.reference .internal}[[::]{.pre}]{.p}[[[openmode]{.pre}]{.n}](#document-api_high/api_high#_CPPv4N6adios27fstream8openmodeE "adios2::fstream::openmode"){.reference .internal}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[MPI_Comm]{.pre}]{.n}[ ]{.w}[[comm]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[engineType]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"BPFile\"]{.pre}]{.s}[)]{.sig-paren}[](#_CPPv4N6adios27fstream7fstreamERKNSt6stringEN6adios27fstream8openmodeE8MPI_CommKNSt6stringE "Link to this definition"){.headerlink}\

    :   High-level API MPI constructor, based on C++11 fstream. Allows
        for passing parameters in source code.

        Parameters[:]{.colon}

        :   - **name** -- stream name

            - **mode** -- [[fstream::in]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a3976d416b45edb2af5088ba11608e081){.reference
              .internal} (Read), [[fstream::out]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a5f6580d512d031c2cb1a73b5fc588f19){.reference
              .internal} (Write), [[fstream::app]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a9a735db3e465ea6da68f022da6eb6a52){.reference
              .internal} (Append)

            - **comm** -- MPI communicator establishing domain for
              fstream

            - **engineType** -- available adios2 engine

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- (user input error) or
            std::runtime_error (system error)

    <!-- -->

    []{#_CPPv3N6adios27fstream7fstreamERKNSt6stringEKN6adios27fstream8openmodeE8MPI_CommRKNSt6stringEKNSt6stringE}[]{#_CPPv2N6adios27fstream7fstreamERKNSt6stringEKN6adios27fstream8openmodeE8MPI_CommRKNSt6stringEKNSt6stringE}[]{#adios2::fstream::fstream__ssCR.adios2::fstream::openmodeC.MPI_Comm.ssCR.ssC}[]{#classadios2_1_1fstream_1aface56cfd786cc837e9040192c67b47d .target}[[[fstream]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[[fstream]{.pre}]{.n}](#document-api_high/api_high#_CPPv4N6adios27fstreamE "adios2::fstream"){.reference .internal}[[::]{.pre}]{.p}[[[openmode]{.pre}]{.n}](#document-api_high/api_high#_CPPv4N6adios27fstream8openmodeE "adios2::fstream::openmode"){.reference .internal}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[MPI_Comm]{.pre}]{.n}[ ]{.w}[[comm]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[configFile]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[ioInConfigFile]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios27fstream7fstreamERKNSt6stringEKN6adios27fstream8openmodeE8MPI_CommRKNSt6stringEKNSt6stringE "Link to this definition"){.headerlink}\

    :   High-level API MPI constructor, based on C++11 fstream. Allows
        for runtime config file.

        Parameters[:]{.colon}

        :   - **name** -- stream name

            - **mode** -- [[fstream::in]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a3976d416b45edb2af5088ba11608e081){.reference
              .internal} (Read), [[fstream::out]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a5f6580d512d031c2cb1a73b5fc588f19){.reference
              .internal} (Write), [[fstream::app]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a9a735db3e465ea6da68f022da6eb6a52){.reference
              .internal} (Append)

            - **comm** -- MPI communicator establishing domain for
              fstream

            - **configFile** -- adios2 runtime configuration file

            - **ioInConfigFile** -- specific io name in configFile

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- (user input error) or
            std::runtime_error (system error)

    <!-- -->

    []{#_CPPv3N6adios27fstream7fstreamERKNSt6stringEKN6adios27fstream8openmodeEKNSt6stringE}[]{#_CPPv2N6adios27fstream7fstreamERKNSt6stringEKN6adios27fstream8openmodeEKNSt6stringE}[]{#adios2::fstream::fstream__ssCR.adios2::fstream::openmodeC.ssC}[]{#classadios2_1_1fstream_1a6d6a9408cf79d6dfeccc22b3eadeb5ef .target}[[[fstream]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[[fstream]{.pre}]{.n}](#document-api_high/api_high#_CPPv4N6adios27fstreamE "adios2::fstream"){.reference .internal}[[::]{.pre}]{.p}[[[openmode]{.pre}]{.n}](#document-api_high/api_high#_CPPv4N6adios27fstream8openmodeE "adios2::fstream::openmode"){.reference .internal}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[engineType]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"BPFile\"]{.pre}]{.s}[)]{.sig-paren}[](#_CPPv4N6adios27fstream7fstreamERKNSt6stringEKN6adios27fstream8openmodeEKNSt6stringE "Link to this definition"){.headerlink}\

    :   High-level API non-MPI constructor, based on C++11 fstream.
        Allows for passing parameters in source code.

        Parameters[:]{.colon}

        :   - **name** -- stream name

            - **mode** -- [[fstream::in]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a3976d416b45edb2af5088ba11608e081){.reference
              .internal} (Read), [[fstream::out]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a5f6580d512d031c2cb1a73b5fc588f19){.reference
              .internal} (Write), [[fstream::app]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a9a735db3e465ea6da68f022da6eb6a52){.reference
              .internal} (Append)

            - **engineType** -- available adios2 engine

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- (user input error) or
            std::runtime_error (system error)

    <!-- -->

    []{#_CPPv3N6adios27fstream7fstreamERKNSt6stringEKN6adios27fstream8openmodeERKNSt6stringEKNSt6stringE}[]{#_CPPv2N6adios27fstream7fstreamERKNSt6stringEKN6adios27fstream8openmodeERKNSt6stringEKNSt6stringE}[]{#adios2::fstream::fstream__ssCR.adios2::fstream::openmodeC.ssCR.ssC}[]{#classadios2_1_1fstream_1a72863a8901bd29235cd60b73c7634ed6 .target}[[[fstream]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[[fstream]{.pre}]{.n}](#document-api_high/api_high#_CPPv4N6adios27fstreamE "adios2::fstream"){.reference .internal}[[::]{.pre}]{.p}[[[openmode]{.pre}]{.n}](#document-api_high/api_high#_CPPv4N6adios27fstream8openmodeE "adios2::fstream::openmode"){.reference .internal}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[configFile]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[ioInConfigFile]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios27fstream7fstreamERKNSt6stringEKN6adios27fstream8openmodeERKNSt6stringEKNSt6stringE "Link to this definition"){.headerlink}\

    :   High-level API MPI constructor, based on C++11 fstream. Allows
        for runtime config file.

        Parameters[:]{.colon}

        :   - **name** -- stream name

            - **mode** -- [[fstream::in]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a3976d416b45edb2af5088ba11608e081){.reference
              .internal} (Read), [[fstream::out]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a5f6580d512d031c2cb1a73b5fc588f19){.reference
              .internal} (Write), [[fstream::app]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a9a735db3e465ea6da68f022da6eb6a52){.reference
              .internal} (Append)

            - **configFile** -- adios2 runtime configuration file

            - **ioInConfigFile** -- specific io name in configFile

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- (user input error) or
            std::runtime_error (system error)

    <!-- -->

    []{#_CPPv3N6adios27fstream7fstreamEv}[]{#_CPPv2N6adios27fstream7fstreamEv}[]{#adios2::fstream::fstream}[]{#classadios2_1_1fstream_1a26e52fc3c4d708b5c5acd4ba85fbcbb2 .target}[[[fstream]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[default]{.pre}]{.k}[](#_CPPv4N6adios27fstream7fstreamEv "Link to this definition"){.headerlink}\

    :   Empty constructor, allows the use of open later in the code

    <!-- -->

    []{#_CPPv3N6adios27fstreamD0Ev}[]{#_CPPv2N6adios27fstreamD0Ev}[]{#adios2::fstream::~fstream}[]{#classadios2_1_1fstream_1ae8b2001459f4e97152cc285104d9bbe2 .target}[[[\~fstream]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[default]{.pre}]{.k}[](#_CPPv4N6adios27fstreamD0Ev "Link to this definition"){.headerlink}\

    :   Using RAII STL containers only

    <!-- -->

    []{#_CPPv3NK6adios27fstreamcvbEv}[]{#_CPPv2NK6adios27fstreamcvbEv}[]{#adios2::fstream::castto-b-operatorC}[]{#classadios2_1_1fstream_1a945c86397953dd740fc1eaa38e0288cb .target}[[explicit]{.pre}]{.k}[ ]{.w}[[[operator]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4NK6adios27fstreamcvbEv "Link to this definition"){.headerlink}\

    :   Checks if fstream object is valid

    <!-- -->

    []{#_CPPv3N6adios27fstream4openERKNSt6stringEK8openmode8MPI_CommKNSt6stringE}[]{#_CPPv2N6adios27fstream4openERKNSt6stringEK8openmode8MPI_CommKNSt6stringE}[]{#adios2::fstream::open__ssCR.openmodeC.MPI_Comm.ssC}[]{#classadios2_1_1fstream_1a5e7e3688c38dd98c8a19e61eda6eeec1 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[open]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[openmode]{.pre}]{.n}](#document-api_high/api_high#_CPPv4N6adios27fstream8openmodeE "adios2::fstream::openmode"){.reference .internal}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[MPI_Comm]{.pre}]{.n}[ ]{.w}[[comm]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[engineType]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"BPFile\"]{.pre}]{.s}[)]{.sig-paren}[](#_CPPv4N6adios27fstream4openERKNSt6stringEK8openmode8MPI_CommKNSt6stringE "Link to this definition"){.headerlink}\

    :   High-level API MPI open, based on C++11 fstream. Allows for
        passing parameters in source code. Used after empty constructor.

        Parameters[:]{.colon}

        :   - **name** -- stream name

            - **mode** -- [[adios2::fstream::in]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a3976d416b45edb2af5088ba11608e081){.reference
              .internal} (Read), [[adios2::fstream::out]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a5f6580d512d031c2cb1a73b5fc588f19){.reference
              .internal} (Write), [[adios2::fstream::app]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a9a735db3e465ea6da68f022da6eb6a52){.reference
              .internal} (Append)

            - **comm** -- MPI communicator establishing domain for
              fstream

            - **engineType** -- available adios2 engine

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- (user input error) or
            std::runtime_error (system error)

    <!-- -->

    []{#_CPPv3N6adios27fstream4openERKNSt6stringEK8openmode8MPI_CommKNSt6stringEKNSt6stringE}[]{#_CPPv2N6adios27fstream4openERKNSt6stringEK8openmode8MPI_CommKNSt6stringEKNSt6stringE}[]{#adios2::fstream::open__ssCR.openmodeC.MPI_Comm.ssC.ssC}[]{#classadios2_1_1fstream_1a804c9382ee9c916b2302157f6641bed1 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[open]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[openmode]{.pre}]{.n}](#document-api_high/api_high#_CPPv4N6adios27fstream8openmodeE "adios2::fstream::openmode"){.reference .internal}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[MPI_Comm]{.pre}]{.n}[ ]{.w}[[comm]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[configFile]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[ioInConfigFile]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios27fstream4openERKNSt6stringEK8openmode8MPI_CommKNSt6stringEKNSt6stringE "Link to this definition"){.headerlink}\

    :   High-level API MPI constructor, based on C++11 fstream. Allows
        for runtime config file. Used after empty constructor.

        Parameters[:]{.colon}

        :   - **name** -- stream name

            - **mode** -- [[fstream::in]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a3976d416b45edb2af5088ba11608e081){.reference
              .internal} (Read), [[fstream::out]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a5f6580d512d031c2cb1a73b5fc588f19){.reference
              .internal} (Write), [[fstream::app]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a9a735db3e465ea6da68f022da6eb6a52){.reference
              .internal} (Append)

            - **comm** -- MPI communicator establishing domain for
              fstream

            - **configFile** -- adios2 runtime configuration file

            - **ioInConfigFile** -- specific io name in configFile

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- (user input error) or
            std::runtime_error (system error)

    <!-- -->

    []{#_CPPv3N6adios27fstream4openERKNSt6stringEK8openmodeKNSt6stringE}[]{#_CPPv2N6adios27fstream4openERKNSt6stringEK8openmodeKNSt6stringE}[]{#adios2::fstream::open__ssCR.openmodeC.ssC}[]{#classadios2_1_1fstream_1a57cb72e50138b1c74b57b3afe81b4a00 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[open]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[openmode]{.pre}]{.n}](#document-api_high/api_high#_CPPv4N6adios27fstream8openmodeE "adios2::fstream::openmode"){.reference .internal}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[engineType]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"BPFile\"]{.pre}]{.s}[)]{.sig-paren}[](#_CPPv4N6adios27fstream4openERKNSt6stringEK8openmodeKNSt6stringE "Link to this definition"){.headerlink}\

    :   High-level API non-MPI open, based on C++11 fstream. Allows for
        passing parameters in source code. Used after empty constructor.

        Parameters[:]{.colon}

        :   - **name** -- stream name

            - **mode** -- [[fstream::in]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a3976d416b45edb2af5088ba11608e081){.reference
              .internal} (Read), [[fstream::out]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a5f6580d512d031c2cb1a73b5fc588f19){.reference
              .internal} (Write), [[fstream::app]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a9a735db3e465ea6da68f022da6eb6a52){.reference
              .internal} (Append)

            - **engineType** -- available adios2 engine

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- (user input error) or
            std::runtime_error (system error)

    <!-- -->

    []{#_CPPv3N6adios27fstream4openERKNSt6stringEK8openmodeKNSt6stringEKNSt6stringE}[]{#_CPPv2N6adios27fstream4openERKNSt6stringEK8openmodeKNSt6stringEKNSt6stringE}[]{#adios2::fstream::open__ssCR.openmodeC.ssC.ssC}[]{#classadios2_1_1fstream_1a16bc6ec2ebdff2b1748f930e1cebd544 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[open]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[openmode]{.pre}]{.n}](#document-api_high/api_high#_CPPv4N6adios27fstream8openmodeE "adios2::fstream::openmode"){.reference .internal}[ ]{.w}[[mode]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[configFile]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[ioInConfigFile]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios27fstream4openERKNSt6stringEK8openmodeKNSt6stringEKNSt6stringE "Link to this definition"){.headerlink}\

    :   High-level API non-MPI constructor, based on C++11 fstream.
        Allows for runtime config file. Used after empty constructor.

        Parameters[:]{.colon}

        :   - **name** -- stream name

            - **mode** -- [[fstream::in]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a3976d416b45edb2af5088ba11608e081){.reference
              .internal} (Read), [[fstream::out]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a5f6580d512d031c2cb1a73b5fc588f19){.reference
              .internal} (Write), [[fstream::app]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream_1ae25d1b25ce8e039180571962df806778a9a735db3e465ea6da68f022da6eb6a52){.reference
              .internal} (Append)

            - **configFile** -- adios2 runtime configuration file

            - **ioInConfigFile** -- specific io name in configFile

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- (user input error) or
            std::runtime_error (system error)

    <!-- -->

    []{#_CPPv3N6adios27fstream13set_parameterEKNSt6stringEKNSt6stringE}[]{#_CPPv2N6adios27fstream13set_parameterEKNSt6stringEKNSt6stringE}[]{#adios2::fstream::set_parameter__ssC.ssC}[]{#classadios2_1_1fstream_1ae938cc15eed3d3be8b6c7201bcc1b283 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[set_parameter]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[key]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[value]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4N6adios27fstream13set_parameterEKNSt6stringEKNSt6stringE "Link to this definition"){.headerlink}\

    :   Set a single stream parameter based on [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} supported parameters. MUST be passed before the first
        call to write or read. See:
        [https://adios2.readthedocs.io/en/latest/engines/engines.html](https://adios2.readthedocs.io/en/latest/engines/engines.html){.reference
        .external}

        Parameters[:]{.colon}

        :   - **key** -- input parameter key

            - **value** -- input parameter value

    <!-- -->

    []{#_CPPv3N6adios27fstream14set_parametersERKN6adios26ParamsE}[]{#_CPPv2N6adios27fstream14set_parametersERKN6adios26ParamsE}[]{#adios2::fstream::set_parameters__adios2::ParamsCR}[]{#classadios2_1_1fstream_1ad9ec6188651c0c058ce7a8ffbf5de5a0 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[set_parameters]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Params]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[parameters]{.pre}]{.n .sig-param}[)]{.sig-paren}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4N6adios27fstream14set_parametersERKN6adios26ParamsE "Link to this definition"){.headerlink}\

    :   Set stream parameters based on [[Engine]{.std
        .std-ref}](#document-api_full/api_full#classadios2_1_1Engine){.reference
        .internal} supported parameters. MUST be passed before the first
        call to write or read. See:
        [https://adios2.readthedocs.io/en/latest/engines/engines.html](https://adios2.readthedocs.io/en/latest/engines/engines.html){.reference
        .external}

        Parameters[:]{.colon}

        :   **parameters** -- input key/value parameters

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream15write_attributeERKNSt6stringERK1TRKNSt6stringEKNSt6stringEKb}[]{#_CPPv2I0EN6adios27fstream15write_attributeERKNSt6stringERK1TRKNSt6stringEKNSt6stringEKb}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1af97010f90722802b7b71116130f3fdc2 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[write_attribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream15write_attributeEvRKNSt6stringERK1TRKNSt6stringEKNSt6stringEKb "adios2::fstream::write_attribute::T"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"\"]{.pre}]{.s}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[separator]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"/\"]{.pre}]{.s}, [[const]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[endStep]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[false]{.pre}]{.k}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream15write_attributeEvRKNSt6stringERK1TRKNSt6stringEKNSt6stringEKb "Link to this definition"){.headerlink}\

    :   Define attribute inside fstream or for a variable after write.
        Single value input version.

        Parameters[:]{.colon}

        :   - **name** -- unique attribute identifier [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal} object or for a [[Variable]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
              .internal} if variableName is not empty (associated to a
              variable)

            - **value** -- single data value

            - **variableName** -- default is empty, if not empty
              attributes is associated to a variable after a write

            - **separator** -- default is "/", hierarchy between
              variable name and attribute, e.g. variableName/attribute1,
              variableName::attribute1. Not used if variableName is
              empty.

            - **endStep** -- similar to std::endStep, end current step
              and flush (default). Use adios2::endStep for true.

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream15write_attributeERKNSt6stringEPK1TK6size_tRKNSt6stringEKNSt6stringEKb}[]{#_CPPv2I0EN6adios27fstream15write_attributeERKNSt6stringEPK1TK6size_tRKNSt6stringEKNSt6stringEKb}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1a4821b6cbd9b667b52dd1176433f1024f .target}[[void]{.pre}]{.kt}[ ]{.w}[[[write_attribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream15write_attributeEvRKNSt6stringEPK1TK6size_tRKNSt6stringEKNSt6stringEKb "adios2::fstream::write_attribute::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[size]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"\"]{.pre}]{.s}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[separator]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"/\"]{.pre}]{.s}, [[const]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[endStep]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[false]{.pre}]{.k}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream15write_attributeEvRKNSt6stringEPK1TK6size_tRKNSt6stringEKNSt6stringEKb "Link to this definition"){.headerlink}\

    :   Define attribute inside fstream or for a variable after write.
        Array input version.

        Parameters[:]{.colon}

        :   - **name** -- unique attribute identifier [[IO]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1IO){.reference
              .internal} object or for a [[Variable]{.std
              .std-ref}](#document-api_full/api_full#classadios2_1_1Variable){.reference
              .internal} if variableName is not empty (associated to a
              variable)

            - **data** -- pointer to user data

            - **size** -- number of data elements

            - **variableName** -- default is empty, if not empty
              attributes is associated to a variable after a write

            - **separator** -- default is "/", hierarchy between
              variable name and attribute, e.g. variableName/attribute1,
              variableName::attribute1. Not used if variableName is
              empty.

            - **endStep** -- similar to std::endStep, end current step
              and flush (default). Use adios2::endStep for true.

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream5writeERKNSt6stringEPK1TRKN6adios24DimsERKN6adios24DimsERKN6adios24DimsEKb}[]{#_CPPv2I0EN6adios27fstream5writeERKNSt6stringEPK1TRKN6adios24DimsERKN6adios24DimsERKN6adios24DimsEKb}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1a42a0fe31b13a134bc7970553ad0787de .target}[[void]{.pre}]{.kt}[ ]{.w}[[[write]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream5writeEvRKNSt6stringEPK1TRKN6adios24DimsERKN6adios24DimsERKN6adios24DimsEKb "adios2::fstream::write::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[shape]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[start]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[count]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[[(]{.pre}]{.p}[[)]{.pre}]{.p}, [[const]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[endStep]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[false]{.pre}]{.k}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream5writeEvRKNSt6stringEPK1TRKN6adios24DimsERKN6adios24DimsERKN6adios24DimsEKb "Link to this definition"){.headerlink}\

    :   writes a self-describing array variable

        Parameters[:]{.colon}

        :   - **name** -- variable name

            - **data** -- variable data data

            - **shape** -- variable global MPI dimensions. Pass empty
              for local variables.

            - **start** -- variable offset for current MPI rank. Pass
              empty for local variables.

            - **count** -- variable dimension for current MPI rank.
              Local variables only have count.

            - **endStep** -- similar to std::endStep, end current step
              and flush (default). Use adios2::endStep if true.

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- (user input error) or
            std::runtime_error (system error)

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream5writeERKNSt6stringEPK1TRKN6adios24DimsERKN6adios24DimsERKN6adios24DimsERKN6adios27vParamsEKb}[]{#_CPPv2I0EN6adios27fstream5writeERKNSt6stringEPK1TRKN6adios24DimsERKN6adios24DimsERKN6adios24DimsERKN6adios27vParamsEKb}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1adfa14eaee4ad3c164b78e6d46aefc9c3 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[write]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream5writeEvRKNSt6stringEPK1TRKN6adios24DimsERKN6adios24DimsERKN6adios24DimsERKN6adios27vParamsEKb "adios2::fstream::write::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[shape]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[start]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[count]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[vParams]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[operations]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[endStep]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[false]{.pre}]{.k}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream5writeEvRKNSt6stringEPK1TRKN6adios24DimsERKN6adios24DimsERKN6adios24DimsERKN6adios27vParamsEKb "Link to this definition"){.headerlink}\

    :   write overload that allows passing supported operations (e.g.
        lossy compression "zfp", "mgard", "sz") to a self-described
        array variable

        Parameters[:]{.colon}

        :   - **name** -- variable name

            - **data** -- variable data data

            - **shape** -- variable global MPI dimensions. Pass empty
              for local variables.

            - **start** -- variable offset for current MPI rank. Pass
              empty for local variables.

            - **count** -- variable dimension for current MPI rank.
              Local variables only have count.

            - **operations** -- vector of operations, each entry is a
              std::pair:

            - **endStep** -- similar to std::endStep, end current step
              and flush (default). Use adios2::endStep if true.

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- (user input error) or
            std::runtime_error (system error)

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream5writeERKNSt6stringERK1TKbKb}[]{#_CPPv2I0EN6adios27fstream5writeERKNSt6stringERK1TKbKb}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1a43d12b1380bfbb3d88da2a621880e120 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[write]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream5writeEvRKNSt6stringERK1TKbKb "adios2::fstream::write::T"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[isLocalValue]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[false]{.pre}]{.k}, [[const]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[endStep]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[false]{.pre}]{.k}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream5writeEvRKNSt6stringERK1TKbKb "Link to this definition"){.headerlink}\

    :   Write a self-describing single-value variable

        Parameters[:]{.colon}

        :   - **name** -- variable name

            - **value** -- variable data value (can be r-value)

            - **isLocalValue** -- true: local value (returned as
              GlobalArray), false: global value (returned as global
              value)

            - **endStep** -- similar to std::endStep, end current step
              and flush (default). Use adios2::endStep for true.

        Throws[:]{.colon}

        :   [[std]{.n}[::]{.p}[invalid_argument]{.n}]{.cpp-expr .sig
            .sig-inline .cpp} -- (user input error) or
            std::runtime_error (system error)

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream4readERKNSt6stringEP1TK6size_t}[]{#_CPPv2I0EN6adios27fstream4readERKNSt6stringEP1TK6size_t}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1a8c10673426a95fd72bcd27634d668bf9 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[read]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream4readEvRKNSt6stringEP1TK6size_t "adios2::fstream::read::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[blockID]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream4readEvRKNSt6stringEP1TK6size_t "Link to this definition"){.headerlink}\

    :   Reads into a pre-allocated pointer. When used with
        adios2::getstep reads current step

        Parameters[:]{.colon}

        :   - **name** -- variable name

            - **data** -- pre-allocated pointer to hold read data

            - **blockID** -- required for local variables, specify
              current block to be selected

        Throws[:]{.colon}

        :   [[throws]{.n}]{.cpp-expr .sig .sig-inline .cpp} -- exception
            if variable name, dimensions or step not found

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream4readERKNSt6stringER1TK6size_t}[]{#_CPPv2I0EN6adios27fstream4readERKNSt6stringER1TK6size_t}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1aa60c383de15133690451f2bac31ce69d .target}[[void]{.pre}]{.kt}[ ]{.w}[[[read]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream4readEvRKNSt6stringER1TK6size_t "adios2::fstream::read::T"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[blockID]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream4readEvRKNSt6stringER1TK6size_t "Link to this definition"){.headerlink}\

    :   Reads a value. When used with adios2::getstep reads current step
        value

        Parameters[:]{.colon}

        :   - **name** -- variable name

            - **value** -- output value, if variable is not found (name
              and type don't match) the returned value address becomes
              nullptr

            - **blockID** -- required for local variables, specify
              current block to be selected

        Throws[:]{.colon}

        :   [[throws]{.n}]{.cpp-expr .sig .sig-inline .cpp} -- exception
            if variable name, dimensions or step not found

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream4readERKNSt6stringEP1TK6size_tK6size_tK6size_t}[]{#_CPPv2I0EN6adios27fstream4readERKNSt6stringEP1TK6size_tK6size_tK6size_t}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1ae459742145734c9dca9cc28a3e27163a .target}[[void]{.pre}]{.kt}[ ]{.w}[[[read]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream4readEvRKNSt6stringEP1TK6size_tK6size_tK6size_t "adios2::fstream::read::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[stepsStart]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[stepsCount]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[1]{.pre}]{.m}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[blockID]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream4readEvRKNSt6stringEP1TK6size_tK6size_tK6size_t "Link to this definition"){.headerlink}\

    :   Read accessing steps in random access mode. Not be used with
        adios2::getstep as it throw an exception when reading in
        stepping mode.

        Parameters[:]{.colon}

        :   - **name** -- variable name

            - **data** -- pre-allocated pointer to hold read data, if
              variable is not found (name and type don't match) it
              becomes nullptr

            - **stepsStart** -- variable initial step (relative to the
              variable first appearance, not absolute step in stream)

            - **stepsCount** -- variable number of steps form
              step_start, don't have to be contiguous, necessarily

            - **blockID** -- required for local variables, specify
              current block to be selected

        Throws[:]{.colon}

        :   [[throws]{.n}]{.cpp-expr .sig .sig-inline .cpp} -- exception
            if variable name, dimensions or step not found

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream4readERKNSt6stringER1TK6size_tK6size_t}[]{#_CPPv2I0EN6adios27fstream4readERKNSt6stringER1TK6size_tK6size_t}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1af9d88d1013966249ad5abd08b2ac6cf1 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[read]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream4readEvRKNSt6stringER1TK6size_tK6size_t "adios2::fstream::read::T"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[value]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[step]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[blockID]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream4readEvRKNSt6stringER1TK6size_tK6size_t "Link to this definition"){.headerlink}\

    :   Reads into a single value for a single step. Not be used with
        adios2::getstep as it throws an exception when reading in
        stepping mode.

        Parameters[:]{.colon}

        :   - **name** -- variable name

            - **value** -- filled with value, if variable is not found
              (name, type and step don't match) the returned value
              address becomes nullptr

            - **step** -- selected single step

            - **blockID** -- required for local variables, specify
              current block to be selected

        Throws[:]{.colon}

        :   [[throws]{.n}]{.cpp-expr .sig .sig-inline .cpp} -- exception
            if variable name, dimensions or step not found

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream4readERKNSt6stringEP1TRKN6adios24DimsERKN6adios24DimsEK6size_t}[]{#_CPPv2I0EN6adios27fstream4readERKNSt6stringEP1TRKN6adios24DimsERKN6adios24DimsEK6size_t}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1aa83a3e7effce6cccdd7e85812c867de7 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[read]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream4readEvRKNSt6stringEP1TRKN6adios24DimsERKN6adios24DimsEK6size_t "adios2::fstream::read::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[start]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[count]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[blockID]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream4readEvRKNSt6stringEP1TRKN6adios24DimsERKN6adios24DimsEK6size_t "Link to this definition"){.headerlink}\

    :   Reads into a pre-allocated pointer a selection piece in
        dimension. When used with adios2::getstep reads current step

        Parameters[:]{.colon}

        :   - **name** -- variable name

            - **data** -- pre-allocated pointer to hold read data, if
              variable is not found (name and type don't match) it
              becomes nullptr

            - **start** -- variable local offset selection

            - **count** -- variable local dimension selection from start

            - **blockID** -- required for local variables, specify
              current block to be selected

        Throws[:]{.colon}

        :   [[throws]{.n}]{.cpp-expr .sig .sig-inline .cpp} -- exception
            if variable name, dimensions or step not found

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream4readERKNSt6stringEP1TRKN6adios24DimsERKN6adios24DimsEK6size_tK6size_tK6size_t}[]{#_CPPv2I0EN6adios27fstream4readERKNSt6stringEP1TRKN6adios24DimsERKN6adios24DimsEK6size_tK6size_tK6size_t}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1accd539bd79f1c1e97f2d43078330cd08 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[read]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream4readEvRKNSt6stringEP1TRKN6adios24DimsERKN6adios24DimsEK6size_tK6size_tK6size_t "adios2::fstream::read::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[start]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[count]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[stepsStart]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[stepsCount]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[blockID]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream4readEvRKNSt6stringEP1TRKN6adios24DimsERKN6adios24DimsEK6size_tK6size_tK6size_t "Link to this definition"){.headerlink}\

    :   Reads into a pre-allocated pointer a selection piece in
        dimensions and steps. Not be used with adios2::getstep as it
        throws an exception when reading in stepping mode.

        Parameters[:]{.colon}

        :   - **name** -- variable name

            - **data** -- pre-allocated pointer to hold read data, if
              variable is not found (name and type don't match) it
              becomes a nullptr

            - **start** -- variable local offset selection

            - **count** -- variable local dimension selection from start

            - **stepsStart** -- variable initial step (relative to the
              variable first appearance, not absolute step in stream)

            - **stepsCount** -- variable number of steps form
              step_start, don't have to be necessarily contiguous

            - **blockID** -- required for local variables, specify
              current block to be selected

        Throws[:]{.colon}

        :   [[throws]{.n}]{.cpp-expr .sig .sig-inline .cpp} -- exception
            if variable name, dimensions or step not found

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream4readERKNSt6stringEK6size_t}[]{#_CPPv2I0EN6adios27fstream4readERKNSt6stringEK6size_t}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1a04d0f5db3a9e021fa5d404f79e75275f .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream4readENSt6vectorI1TEERKNSt6stringEK6size_t "adios2::fstream::read::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[read]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[blockID]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream4readENSt6vectorI1TEERKNSt6stringEK6size_t "Link to this definition"){.headerlink}\

    :   Reads entire variable for current step (streaming mode: step by
        step)

        Parameters[:]{.colon}

        :   - **name** -- variable name

            - **blockID** -- required for local variables, specify
              current block to be selected

        Throws[:]{.colon}

        :   [[throws]{.n}]{.cpp-expr .sig .sig-inline .cpp} -- exception
            if variable name, dimensions or step not found

        Returns[:]{.colon}

        :   data of variable name for current step. Single data will
            have a size=1 vector

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream4readERKNSt6stringEK6size_tK6size_tK6size_t}[]{#_CPPv2I0EN6adios27fstream4readERKNSt6stringEK6size_tK6size_tK6size_t}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1a8222ea4b1c02e156e4d2e14fdf8142a5 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream4readENSt6vectorI1TEERKNSt6stringEK6size_tK6size_tK6size_t "adios2::fstream::read::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[read]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[stepsStart]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[stepsCount]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[1]{.pre}]{.m}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[blockID]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream4readENSt6vectorI1TEERKNSt6stringEK6size_tK6size_tK6size_t "Link to this definition"){.headerlink}\

    :   Returns a vector with full variable dimensions for the current
        step selection. Not be used with adios2::getstep as it throw an
        exception when reading in stepping mode.

        Parameters[:]{.colon}

        :   - **name** -- variable name

            - **stepsStart** -- variable initial step (relative to the
              variable first appearance, not absolute step in stream)

            - **stepsCount** -- variable number of steps form
              step_start, don't have to be contiguous, necessarily

            - **blockID** -- required for local variables, specify
              current block to be selected

        Throws[:]{.colon}

        :   [[throws]{.n}]{.cpp-expr .sig .sig-inline .cpp} -- exception
            if variable name, dimensions or step not found

        Returns[:]{.colon}

        :   data of variable name for current step, empty if exception
            is thrown

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream4readERKNSt6stringERK4DimsRK4DimsK6size_t}[]{#_CPPv2I0EN6adios27fstream4readERKNSt6stringERK4DimsRK4DimsK6size_t}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1a149aa26f664e5e6763b20e7fcecdc17b .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream4readENSt6vectorI1TEERKNSt6stringERK4DimsRK4DimsK6size_t "adios2::fstream::read::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[read]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[start]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[count]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[blockID]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream4readENSt6vectorI1TEERKNSt6stringERK4DimsRK4DimsK6size_t "Link to this definition"){.headerlink}\

    :   Reads a selection piece in dimension for current step (streaming
        mode: step by step)

        Parameters[:]{.colon}

        :   - **name** -- variable name

            - **start** -- variable local offset selection

            - **count** -- variable local dimension selection from start

            - **blockID** -- required for local variables, specify
              current block to be selected

        Throws[:]{.colon}

        :   [[throws]{.n}]{.cpp-expr .sig .sig-inline .cpp} -- exception
            if variable name, dimensions or step not found

        Returns[:]{.colon}

        :   data of variable name for current step, empty if exception
            is thrown

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream4readERKNSt6stringERK4DimsRK4DimsK6size_tK6size_tK6size_t}[]{#_CPPv2I0EN6adios27fstream4readERKNSt6stringERK4DimsRK4DimsK6size_tK6size_tK6size_t}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1a4d74ea4436df28b59490e2e51a3bcaf9 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream4readENSt6vectorI1TEERKNSt6stringERK4DimsRK4DimsK6size_tK6size_tK6size_t "adios2::fstream::read::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[read]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[start]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[Dims]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[count]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[stepsStart]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[stepsCount]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[size_t]{.pre}]{.n}[ ]{.w}[[blockID]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[0]{.pre}]{.m}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream4readENSt6vectorI1TEERKNSt6stringERK4DimsRK4DimsK6size_tK6size_tK6size_t "Link to this definition"){.headerlink}\

    :   Reads a selection piece in dimension and a selection piece in
        steps (non-streaming mode). Not be used with adios2::getstep as
        it throw an exception when reading in stepping mode.

        Parameters[:]{.colon}

        :   - **name** -- variable name

            - **start** -- variable local offset selection

            - **count** -- variable local dimension selection from start

            - **stepsStart** -- variable initial step (relative to the
              variable first appearance, not absolute step in stream)

            - **stepsCount** -- variable number of steps form
              step_start, don't have to be contiguous, necessarily

            - **blockID** -- required for local variables, specify
              current block to be selected

        Throws[:]{.colon}

        :   [[throws]{.n}]{.cpp-expr .sig .sig-inline .cpp} -- exception
            if variable name, dimensions or step not found

        Returns[:]{.colon}

        :   variable data, empty if exception is thrown

    <!-- -->

    []{#_CPPv3I0EN6adios27fstream14read_attributeERKNSt6stringERKNSt6stringEKNSt6stringE}[]{#_CPPv2I0EN6adios27fstream14read_attributeERKNSt6stringERKNSt6stringEKNSt6stringE}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[class]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[\>]{.pre}]{.p}\
    []{#classadios2_1_1fstream_1a97656f482e6fa2be0c05f96320fba6b2 .target}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[vector]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#document-api_high/api_high#_CPPv4I0EN6adios27fstream14read_attributeENSt6vectorI1TEERKNSt6stringERKNSt6stringEKNSt6stringE "adios2::fstream::read_attribute::T"){.reference .internal}[[\>]{.pre}]{.p}[ ]{.w}[[[read_attribute]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[name]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[variableName]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"\"]{.pre}]{.s}, [[const]{.pre}]{.k}[ ]{.w}[[std]{.pre}]{.n}[[::]{.pre}]{.p}[[string]{.pre}]{.n}[ ]{.w}[[separator]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[\"/\"]{.pre}]{.s}[)]{.sig-paren}[](#_CPPv4I0EN6adios27fstream14read_attributeENSt6vectorI1TEERKNSt6stringERKNSt6stringEKNSt6stringE "Link to this definition"){.headerlink}\

    :   Reads an attribute returning a vector For single data vector
        size = 1

        Parameters[:]{.colon}

        :   - **name** -- attribute name

            - **variableName** -- default is empty, if not empty look
              for an attribute associated to a variable

            - **separator** -- default is "/", hierarchy between
              variable name and attribute, e.g. variableName/attribute1,
              variableName::attribute1. Not used if variableName is
              empty.

        Returns[:]{.colon}

        :   vector containing attribute data

    <!-- -->

    []{#_CPPv3N6adios27fstream8end_stepEv}[]{#_CPPv2N6adios27fstream8end_stepEv}[]{#adios2::fstream::end_step}[]{#classadios2_1_1fstream_1ae570c9c8dafd27569e388061e1499481 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[end_step]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios27fstream8end_stepEv "Link to this definition"){.headerlink}\

    :   At write: ends the current step At read: use it in streaming
        mode to inform the writer that the reader is done consuming the
        step. No effect for file engines.

    <!-- -->

    []{#_CPPv3N6adios27fstream5closeEv}[]{#_CPPv2N6adios27fstream5closeEv}[]{#adios2::fstream::close}[]{#classadios2_1_1fstream_1a64bc3f741a8f25b774191ad3b6fa92f9 .target}[[void]{.pre}]{.kt}[ ]{.w}[[[close]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[](#_CPPv4N6adios27fstream5closeEv "Link to this definition"){.headerlink}\

    :   close current stream becoming inaccessible

    <!-- -->

    []{#_CPPv3NK6adios27fstream12current_stepEv}[]{#_CPPv2NK6adios27fstream12current_stepEv}[]{#adios2::fstream::current_stepC}[]{#classadios2_1_1fstream_1a74b99dfb1518de0568f94d2d9be1d0b6 .target}[[size_t]{.pre}]{.n}[ ]{.w}[[[current_step]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[)]{.sig-paren}[ ]{.w}[[const]{.pre}]{.k}[ ]{.w}[[noexcept]{.pre}]{.k}[](#_CPPv4NK6adios27fstream12current_stepEv "Link to this definition"){.headerlink}\

    :   Return current step when getstep is called in a loop, read mode
        only

        Returns[:]{.colon}

        :   current step
    :::

    ::: {.breathe-sectiondef .docutils .container}
    Friends

    []{#_CPPv3N6adios27fstream7getstepERN6adios27fstreamERN6adios25fstepE}[]{#_CPPv2N6adios27fstream7getstepERN6adios27fstreamERN6adios25fstepE}[]{#adios2::fstream::getstep__adios2::fstreamR.adios2::fstepR}[]{#classadios2_1_1fstream_1aa2d1f861055d3d753e5d28e17d72137b .target}[[friend]{.pre}]{.k}[ ]{.w}[[bool]{.pre}]{.kt}[ ]{.w}[[[getstep]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[[fstream]{.pre}]{.n}](#document-api_high/api_high#_CPPv4N6adios27fstreamE "adios2::fstream"){.reference .internal}[ ]{.w}[[&]{.pre}]{.p}[[stream]{.pre}]{.n .sig-param}, [[adios2]{.pre}]{.n}[[::]{.pre}]{.p}[[fstep]{.pre}]{.n}[ ]{.w}[[&]{.pre}]{.p}[[step]{.pre}]{.n .sig-param}[)]{.sig-paren}[](#_CPPv4N6adios27fstream7getstepERN6adios27fstreamERN6adios25fstepE "Link to this definition"){.headerlink}\

    :   Gets step from stream Based on std::getline, enables reading on
        a step-by-step basis in a while or for loop. Read mode only

        Parameters[:]{.colon}

        :   - **stream** -- input stream containing steps

            - **step** -- output object current step, adios2::fstep in
              an alias to [[adios2::fstream]{.std
              .std-ref}](#document-api_high/api_high#classadios2_1_1fstream){.reference
              .internal} with scope narrowed to one step

        Returns[:]{.colon}

        :   true: step is valid, false: step is invalid (end of stream).
    :::
:::
:::::::::::

::::::::::: {#matlab-simple-bindings .section}
### Matlab simple bindings[](#matlab-simple-bindings "Link to this heading"){.headerlink}

The ADIOS Matlab API supports reading data from ADIOS BP files with a
simplified API that consists of three functions:

> <div>
>
> - [`ADIOSOPEN`{.docutils .literal .notranslate}]{.pre} returns a
>   structure with information on an ADIOS BP File (variables and
>   attributes).
>
> - [`ADIOSREAD`{.docutils .literal .notranslate}]{.pre} reads in a
>   variable from the file. It expects the info structure returned by
>   [`ADIOSOPEN`{.docutils .literal .notranslate}]{.pre}.
>
> - [`ADIOSCLOSE`{.docutils .literal .notranslate}]{.pre} closes the
>   file.
>
> </div>

::: {#organization-of-an-adios-bp-file .section}
#### Organization of an ADIOS BP file[](#organization-of-an-adios-bp-file "Link to this heading"){.headerlink}

An ADIOS BP file contains a set of variables and attributes. Each
variable in the group has a path, which defines a logical hierarchy of
the variables within the file.
:::

::: {#time-dimension-of-a-variable .section}
#### Time dimension of a variable[](#time-dimension-of-a-variable "Link to this heading"){.headerlink}

Variables can be written several times from a program, if they have a
time dimension. The reader exposes the variables with an extra
dimension, i.e. a 2D variable written over time is seen as a 3D
variable. In MATLAB, the extra dimension is the last dimension (the
slowest changing dimension). Since the reader allows reading an
arbitrary slice of a variable, data for one timestep can be read in with
slicing.
:::

::::: {#min-max-of-arrays .section}
#### Min/max of arrays[](#min-max-of-arrays "Link to this heading"){.headerlink}

The ADIOS BP format stores the min/max values in each variable. The info
structure therefore contains these min/max values. There is practically
no overhead to provide this information (along with the values of all
attributes) even for file sizes of several terabytes.

In the Matlab console use help for these functions

:::: {.highlight-matlabsession .notranslate}
::: highlight
    >>> help adiosopen
    >>> help adiosread
    >>> help adiosclose
:::
::::
:::::

::: {#adiosopen .section}
#### [`ADIOSOPEN`{.docutils .literal .notranslate}]{.pre}[](#adiosopen "Link to this heading"){.headerlink}

[`FILE`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`adiosopen(PATH)`{.docutils .literal .notranslate}]{.pre}

:   Open a file for reading pointed by [`PATH`{.docutils .literal
    .notranslate}]{.pre} and return an information structure
    ([`FILE`{.docutils .literal .notranslate}]{.pre}).

The returned FILE structure contains the following information

> <div>
>
> :::: {.highlight-matlab .notranslate}
> ::: highlight
>     Name              File path
>
>     Handlers          Object handlers to pass on to ADIOS functions
>       FileHandler        uint64 file handler
>       GroupHandler       uint64 IO group object handler
>       ADIOSHandler       uint64 ADIOS object handler
>
>     Variables         Structure array of variables
>          Name            Path of variable
>          Type            Matlab type class of data
>          Dims            Array of dimensions
>          StepsStart      First step's index for this variable in file, always at least 1
>          StepsCount      Number of steps for this variable in file, always at least 1
>          GlobalMin       Global minimum  of the variable (1-by-1 mxArray)
>          GlobalMax       Global maximum of the variable
>
>     Attribute         Structure array of attributes
>          Name            Path of attribute
>          Type            Matlab type class of data
>          Value           Attribute value
> :::
> ::::
>
> </div>
:::

::: {#adiosread .section}
#### [`ADIOSREAD`{.docutils .literal .notranslate}]{.pre}[](#adiosread "Link to this heading"){.headerlink}

Read data from a BP file opened with [`adiosopen`{.docutils .literal
.notranslate}]{.pre}. Provide the structure returned by
[`adiosopen`{.docutils .literal .notranslate}]{.pre} as the first input
argument, and the path to a variable. Inspect
[`file.Variables`{.docutils .literal .notranslate}]{.pre} and
[`file.Attributes`{.docutils .literal .notranslate}]{.pre} for the list
of variables and attributes available in a file.

[`data`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`adiosread(file,`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`VARPATH)`{.docutils .literal .notranslate}]{.pre}

Read the entire variable [`VARPATH`{.docutils .literal
.notranslate}]{.pre} from a BP file. [`file`{.docutils .literal
.notranslate}]{.pre} is the output of [`ADIOSOPEN`{.docutils .literal
.notranslate}]{.pre}. [`VARPATH`{.docutils .literal .notranslate}]{.pre}
is a string to a variable or attribute. If an N-dimensional array
variable has multiple steps in the file this function reads all steps
and returns an N+1 dimensional array where the last dimension equals the
number of steps.

[`data`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`adiosread(file,`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`INDEX)`{.docutils .literal .notranslate}]{.pre}

Read the entire variable from a BP file. [`INDEX`{.docutils .literal
.notranslate}]{.pre} points to a variable in the
[`file.Variables`{.docutils .literal .notranslate}]{.pre} array.

[`data`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`adiosread(...,`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`START,`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`COUNT,`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`STEPSTART,`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`STEPCOUNT)`{.docutils .literal .notranslate}]{.pre}

Read a portion of a variable.

> <div>
>
> :::: {.highlight-matlab .notranslate}
> ::: highlight
>     START and COUNT:
>     A slice is defined as two arrays of N integers, where N is the
>     number of dimensions of the variable, describing the
>     "start" and "count" values. The "start" values start from 1.
>         E.g. [1 5], [10 2] reads the first 10 values in the first dimension
>     and 2 values from the 5th position in the second dimension resulting in
>     a 10-by-2 array.
>         You can use negative numbers to index from the end of the array
>     as in python. -1 refers to the last element of the array, -2 the one
>     before and so on.
>         E.g. [-1], [1] reads in the last value of a 1D array.
>              [1], [-1] reads in the complete 1D array.
>
>     STEPSTART and STEPCOUNT:
>     Similarly, the number of steps from a specific step can be read instead
>     of all data. Steps start from 1. Negative index can be used as well.
>         E.g. -1, 1  will read in the last step from the file
>              n, -1  will read all steps from 'n' to the last one
> :::
> ::::
>
> </div>
:::

::: {#adiosclose .section}
#### [`ADIOSCLOSE`{.docutils .literal .notranslate}]{.pre}[](#adiosclose "Link to this heading"){.headerlink}

[`adiosclose(file)`{.docutils .literal .notranslate}]{.pre}

:   Close file and free internal data structures. [`file`{.docutils
    .literal .notranslate}]{.pre} is the structure returned by
    [`adiosopen`{.docutils .literal .notranslate}]{.pre}.
:::
:::::::::::
::::::::::::::::::::::

[]{#document-api_python/api_python}

:::::::::::::::::::::::::::::::::::: {#python-apis .section}
## Python APIs[](#python-apis "Link to this heading"){.headerlink}

::::::::::::::::::: {#python-example-code .section}
### Python Example Code[](#python-example-code "Link to this heading"){.headerlink}

The Python APIs follows closely Python style directives. They rely on
numpy and, optionally, on [`mpi4py`{.docutils .literal
.notranslate}]{.pre}, if the underlying ADIOS2 library is compiled with
MPI.

For online examples on MyBinder :

- [Python-MPI
  Notebooks](https://mybinder.org/v2/gh/ornladios/ADIOS2-Jupyter.git/python-mpi){.reference
  .external}

- [Python-noMPI
  Notebooks](https://mybinder.org/v2/gh/ornladios/ADIOS2-Jupyter.git/python-nompi){.reference
  .external}

::: {#examples-in-the-adios2-repository .section}
#### Examples in the ADIOS2 repository[](#examples-in-the-adios2-repository "Link to this heading"){.headerlink}

- 

  Simple file-based examples

  :   - examples/hello/helloWorld/hello-world.py

      - examples/hello/bpReader/bpReaderHeatMap2D.py

      - examples/hello/bpWriter/bpWriter.py

- 

  Staging examples using staging engines SST and DataMan

  :   - examples/hello/sstWriter/sstWriter.py

      - examples/hello/sstReader/sstReader.py

      - examples/hello/datamanWriter/dataManWriter.py

      - examples/hello/datamanReader/dataManReader.py
:::

::::::: {#python-write-example .section}
#### Python Write example[](#python-write-example "Link to this heading"){.headerlink}

:::: {.highlight-python .notranslate}
::: highlight
    from mpi4py import MPI
    import numpy as np
    from adios2 import Stream

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    nx = 10
    shape = [size * nx]
    start = [rank * nx]
    count = [nx]

    temperature = np.zeros(nx, dtype=np.double)
    pressure = np.ones(nx, dtype=np.double)
    delta_time = 0.01
    physical_time = 0.0
    nsteps = 5

    with Stream("cfd.bp", "w", comm) as s:
       # NSteps from application
       for _ in s.steps(nsteps):
          if rank == 0 and s.current_step() == 0:
             # write a Python integer
             s.write("nproc", size)

          # write a Python floating point value
          s.write("physical_time", physical_time)
          # temperature and pressure are numpy arrays
          s.write("temperature", temperature, shape, start, count)
          s.write_attribute("temperature/unit", "K")
          s.write("pressure", pressure, shape, start, count)
          s.write_attribute("pressure/unit", "Pa")
          physical_time += delta_time
:::
::::

:::: {.highlight-bash .notranslate}
::: highlight
    $ mpirun -n 4 python3 ./adios2-doc-write.py
    $ bpls -la cfd.bp
      int64_t  nproc             scalar = 4
      double   physical_time     5*scalar = 0 / 0.04
      double   pressure          5*{40} = 1 / 1
      string   pressure/unit     attr   = "Pa"
      double   temperature       5*{40} = 0 / 0
      string   temperature/unit  attr   = "K"
:::
::::
:::::::

::::::: {#python-read-step-by-step-example .section}
#### Python Read "step-by-step" example[](#python-read-step-by-step-example "Link to this heading"){.headerlink}

:::: {.highlight-python .notranslate}
::: highlight
    import numpy as np
    from adios2 import Stream

    with Stream("cfd.bp", "r") as s:
        # steps comes from the stream
        for _ in s.steps():

            # track current step
            print(f"Current step is {s.current_step()}")

            # inspect variables in current step
            for name, info in s.available_variables().items():
                print("variable_name: " + name, end=" ")
                for key, value in info.items():
                    print("\t" + key + ": " + value, end=" ")
                print()

            if s.current_step() == 0:
                nproc = s.read("nproc")
                print(f"nproc is {nproc} of type {type(nproc)}")

            # read variables return a numpy array with corresponding selection
            physical_time = s.read("physical_time")
            print(f"physical_time is {physical_time} of type {type(physical_time)}")
            temperature = s.read("temperature")
            temp_unit = s.read_attribute("temperature/unit")
            print(f"temperature array size is {temperature.size} of shape {temperature.shape}")
            print(f"temperature unit is {temp_unit} of type {type(temp_unit)}")
            pressure = s.read("pressure")
            press_unit = s.read_attribute("pressure/unit")
            print(f"pressure unit is {press_unit} of type {type(press_unit)}")
            print()
:::
::::

:::: {.highlight-bash .notranslate}
::: highlight
    $ python3 adios2-doc-read.py
    Current step is 0
    variable_name: nproc    AvailableStepsCount: 1  Max: 4  Min: 4  Shape:          SingleValue: true       Type: int64_t
    variable_name: physical_time    AvailableStepsCount: 1  Max: 0  Min: 0  Shape:          SingleValue: true       Type: double
    variable_name: pressure         AvailableStepsCount: 1  Max: 1  Min: 1  Shape: 40       SingleValue: false      Type: double
    variable_name: temperature      AvailableStepsCount: 1  Max: 0  Min: 0  Shape: 40       SingleValue: false      Type: double
    nproc is 4 of type <class 'numpy.ndarray'>
    physical_time is 0.0 of type <class 'numpy.ndarray'>
    temperature array size is 40 of shape (40,)
    temperature unit is K of type <class 'str'>
    pressure unit is Pa of type <class 'str'>

    Current step is 1
    variable_name: physical_time    AvailableStepsCount: 1  Max: 0.01       Min: 0.01       Shape:          SingleValue: true   Type: double
    variable_name: pressure         AvailableStepsCount: 1  Max: 1  Min: 1  Shape: 40       SingleValue: false      Type: double
    variable_name: temperature      AvailableStepsCount: 1  Max: 0  Min: 0  Shape: 40       SingleValue: false      Type: double
    physical_time is 0.01 of type <class 'numpy.ndarray'>
    temperature array size is 40 of shape (40,)
    temperature unit is K of type <class 'str'>
    pressure unit is Pa of type <class 'str'>

    ...
:::
::::
:::::::

::::::: {#python-read-random-access-example .section}
#### Python Read Random Access example[](#python-read-random-access-example "Link to this heading"){.headerlink}

:::: {.highlight-python .notranslate}
::: highlight
    import numpy as np
    from adios2 import FileReader

    with FileReader("cfd.bp") as s:
        # inspect variables
        vars = s.available_variables()
        for name, info in vars.items():
            print("variable_name: " + name, end=" ")
            for key, value in info.items():
                print("\t" + key + ": " + value, end=" ")
            print()
        print()

        nproc = s.read("nproc")
        print(f"nproc is {nproc} of type {type(nproc)} with ndim {nproc.ndim}")

        # read variables return a numpy array with corresponding selection
        steps = int(vars['physical_time']['AvailableStepsCount'])
        physical_time = s.read("physical_time", step_selection=[0, steps])
        print(
            f"physical_time is {physical_time} of type {type(physical_time)} with "
            f"ndim {physical_time.ndim} shape = {physical_time.shape}"
        )

        steps = int(vars['temperature']['AvailableStepsCount'])
        temperature = s.read("temperature", step_selection=[0, steps])
        temp_unit = s.read_attribute("temperature/unit")
        print(f"temperature array size is {temperature.size} of shape {temperature.shape}")
        print(f"temperature unit is {temp_unit} of type {type(temp_unit)}")

        steps = int(vars['pressure']['AvailableStepsCount'])
        pressure = s.read("pressure", step_selection=[0, steps])
        press_unit = s.read_attribute("pressure/unit")
        print()
:::
::::

:::: {.highlight-bash .notranslate}
::: highlight
    $ python3 adios2-doc-read-filereader.py
    variable_name: nproc    AvailableStepsCount: 1  Max: 4  Min: 4  Shape:          SingleValue: true       Type: int64_t
    variable_name: physical_time    AvailableStepsCount: 5  Max: 0.04       Min: 0  Shape:          SingleValue: true       Type: double
    variable_name: pressure         AvailableStepsCount: 5  Max: 1  Min: 1  Shape: 40       SingleValue: false      Type: double
    variable_name: temperature      AvailableStepsCount: 5  Max: 0  Min: 0  Shape: 40       SingleValue: false      Type: double

    nproc is 4 of type <class 'numpy.ndarray'> with ndim 0
    physical_time is [0.   0.01 0.02 0.03 0.04] of type <class 'numpy.ndarray'> with ndim 1 shape = (5,)
    temperature array size is 200 of shape (200,)
    temperature unit is K of type <class 'str'>
:::
::::
:::::::
:::::::::::::::::::

::: {#adios2-classes-for-python .section}
### adios2 classes for Python[](#adios2-classes-for-python "Link to this heading"){.headerlink}

[`Stream`{.docutils .literal .notranslate}]{.pre} is a high-level class
that can perform most of the ADIOS functionality.
[`FileReader`{.docutils .literal .notranslate}]{.pre} is just a
convenience class and is the same as Stream with "rra"
(ReadRandomAccess) mode. FileReaders do not work with for loops as
opposed to Streams that work step-by-step, rather one can access any
step of any variable at will. The other classes, [`Adios`{.docutils
.literal .notranslate}]{.pre}, [`IO`{.docutils .literal
.notranslate}]{.pre}, [`Engine`{.docutils .literal .notranslate}]{.pre},
[`Variable`{.docutils .literal .notranslate}]{.pre},
[`Attribute`{.docutils .literal .notranslate}]{.pre} and
[`Operator`{.docutils .literal .notranslate}]{.pre} correspond to the
C++ classes. One needs to use them to extend the capabilities of the
[`Stream`{.docutils .literal .notranslate}]{.pre} class (e.g. using an
external XML file for runtime configuration, changing the engine for the
run, setting up a compression operator for an output variable, etc.)
:::

:::::::::::::: {#python-bindings-to-c .section}
### Python bindings to C++[](#python-bindings-to-c "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

The bindings to the C++ functions is the basis of the native Python API
described before. It is still accessible to users who used the "Full
Python API" pre-2.10. In order to make old scripts working with 2.10 and
later versions, change the import line in the python script.
:::

:::: {.highlight-python .notranslate}
::: highlight
    import adios2.bindings as adios2
:::
::::

The full Python APIs follows very closely the full C++11 API interface.
All of its functionality is now in the native API as well, so its use is
discouraged for future scripts.

::: {#examples-using-the-python-bindings-in-the-adios2-repository .section}
#### Examples using the Python bindings in the ADIOS2 repository[](#examples-using-the-python-bindings-in-the-adios2-repository "Link to this heading"){.headerlink}

- 

  Simple file-based examples

  :   - examples/hello/helloWorld/hello-world-bindings.py

      - examples/hello/bpReader/bpReaderHeatMap2D-bindings.py

      - examples/hello/bpWriter/bpWriter-bindings.py

- 

  Staging examples using staging engines SST and DataMan

  :   - examples/hello/sstWriter/sstWriter-bindings.py

      - examples/hello/sstReader/sstReader-bindings.py
:::

::: {#adios-class .section}
#### ADIOS class[](#adios-class "Link to this heading"){.headerlink}
:::

::: {#io-class .section}
#### IO class[](#io-class "Link to this heading"){.headerlink}
:::

::: {#variable-class .section}
#### Variable class[](#variable-class "Link to this heading"){.headerlink}
:::

::: {#attribute-class .section}
#### Attribute class[](#attribute-class "Link to this heading"){.headerlink}
:::

::: {#engine-class .section}
#### Engine class[](#engine-class "Link to this heading"){.headerlink}
:::

::: {#operator-class .section}
#### Operator class[](#operator-class "Link to this heading"){.headerlink}
:::

::: {#query-class .section}
#### Query class[](#query-class "Link to this heading"){.headerlink}
:::
::::::::::::::

::::: {#transition-from-old-api-to-new-api .section}
### Transition from old API to new API[](#transition-from-old-api-to-new-api "Link to this heading"){.headerlink}

A python script using the high-level API of 2.9 and earlier needs to be
modified to work with 2.10 and later.

- adios2.open() is replaced with adios2.Stream(), and does not have 4th
  and 5th optional arguments for external xml and IO name.

- the [`for`{.docutils .literal .notranslate}]{.pre}` `{.docutils
  .literal .notranslate}[`in`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`file`{.docutils .literal .notranslate}]{.pre} is
  replaced with [`for`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`_`{.docutils
  .literal .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`in`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`file.steps()`{.docutils .literal .notranslate}]{.pre}
  but it works for both writing (by specifying the number of output
  steps) and reading (for the number of available steps in a
  stream/file).

:::: {.highlight-python .notranslate}
::: highlight
    # OLD API
    import adios2

    # NEW API
    from adios2 import Adios, Stream

    # NEW API: this still works
    import adios2


    # OLD API
    fr = adios2.open(args.instream, "r", mpi.comm_app,"adios2.xml", "SimulationOutput")

    # NEW API
    adios = Adios("adios2.xml", mpi.comm_app)
    io = adios.declare_io("SimulationOutput")
    fr = Stream(io, args.instream, "r", mpi.comm_app)


    # OLD API
    for fr_step in fr:
        fr_step....

    # NEW API 1
    for _ in fr.steps():
        fr....

    # NEW API 2
    for fr_step in fr.steps():
        fr_step....
:::
::::
:::::
::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.toctree-wrapper .compound}
[]{#document-advanced/aggregation}

:::: {#aggregation .section}
## Aggregation[](#aggregation "Link to this heading"){.headerlink}

The basic problem of large-scale I/O is that the N-to-1 and N-to-N
(process-to-file) patterns do not scale and one must set the number of
files in an output to the capability of the file system, not the size of
the application. Hence, *N* processes need to write to *M* files to

> <div>
>
> 1.  utilize the bandwidth of the file system and to
>
> 2.  minimize the cost of multiple process writing to a single file,
>     while
>
> 3.  not overwhelming the file system with too many files.
>
> </div>

::: {#aggregation-in-bp5 .section}
### Aggregation in BP5[](#aggregation-in-bp5 "Link to this heading"){.headerlink}

There are two implementations of aggregation in BP5, none of them is the
same as the one in BP4. The aggregation setup in ADIOS2 consist of: a)
*NumAggregators*, which processes do write to disk (others will send
data to them), and b) *NumSubFiles*, how many files they will write.

**EveryoneWritesSerial** is a simple aggregation strategy. Every process
is writing its own data to disk, to one particular file only, and the
processes are serialized over each particular file. In this aggregator,
*NumAggregators* = *NumSubFiles* (= *M*). This approach should scale
well with application size. On Summit's GPFS though we observe that a
single writer per compute node is better than multiple process writing
to the file system, hence this aggregation method performs poorly there.

**EveryoneWrites** is the same strategy as the previous except that
every process immediately writes its own data to its designated file.
Since it basically implements an N-to-N write pattern, this method does
not scale, so only use it up to a moderate number of processes (1-4
process \* number of file system servers). At small scale, as long as
the file system can deal with the on-rush of the write requests, this
method can provide the fastest I/O.

**TwoLevelShm** has a subset of processes that actually write to disk
(*NumAggregators*). There must be at least one process per compute node,
which creates a shared-memory segment for other processes on the node to
send their data. The aggregator process basically serializes the writing
of data from this subset of processes (itself and the processes that
send data to it). TwoLevelShm performs similarly to EveryoneWritesSerial
on Lustre, and is the only good option on Summit's GPFS.

The number of files (*NumSubFiles*) can be smaller than
*NumAggregators*, and then multiple aggregators will write to one file
concurrently. Such a setup becomes useful when the number of nodes is
many times more than the number of file servers.

TwoLevelShm works best if each process's output data fits into the
shared-memory segment, which holds two pages. Since POSIX writes are
limited to about 2GB, the best setup is to use 4GB shared-memory size by
each aggregator. This is the default size, but you can use the
*MaxShmSize* parameter to set this lower if necessary. At runtime, BP5
will only allocate twice the maximum size of the largest data size any
process has, but up to MaxShmSize. If the data from two processes does
not fit into the shared-memory segment, BP5 will need to perfom multiple
iterations of copy and disk-write, which is generally slower than
writing large data blocks at once.

The **default setup** is *TwoLevelShm*, where *NumAggregators* is the
number of compute nodes the application is running on, and the number of
files is the same. This setup is good for Summit's GPFS and good for
Lustre at large scale. However, the default setup leaves potential
performance on the table when running applications at smaller scale,
where the one process per node setup cannot utilize the full bandwidth
of a large parallel file system.
:::
::::

[]{#document-advanced/memory_management}

::::::: {#memory-management .section}
## Memory Management[](#memory-management "Link to this heading"){.headerlink}

::: {#bp4-buffering .section}
### BP4 buffering[](#bp4-buffering "Link to this heading"){.headerlink}

BP4 has a simple buffering mechanism to provide ultimate performance at
the cost of high memory usage: all user data (passed in Put() calls) is
buffered in one contiguous memory allocation and writing/aggregation is
done with this large buffer in EndStep(). Aggregation in BP4 uses MPI to
send this buffer to the aggregator and hence maintaining two such large
buffers. Basically, if an application writes N bytes of data in a step,
then BP4 needs approximately 2xN bytes extra memory for buffering.

A potential performance problem is that BP4 needs to extend the buffer
occasionally to fit more incoming data (more Put() calls). At large
sizes the reallocation may need to move the buffer into a different
place in memory, which requires copying the entire existing buffer. When
there are GBs of data already buffered, this copy will noticably
decrease the overall observed write performance. This situation can be
avoided if one can guess a usable upper limit to how much data each
process is going to write, and telling this to the BP4 engine through
the **InitialBufferSize** parameter before Open().

Another potential problem is that reallocation may fail at some point,
well before the limits of memory, since it needs a single contiguous
allocation be available.
:::

:::: {#bp5-buffering .section}
### BP5 buffering[](#bp5-buffering "Link to this heading"){.headerlink}

BP5 is designed to use less memory than BP4. The buffer it manages is a
list of large chunks. The advantages of the list of chunks is that no
reallocation of existing buffer is needed, and that BP5 can potentially
allocate more buffer than BP4 since it requests many smaller chunks
instead of a large contiguous buffer. In general, chunks should be as
big as the system/application can afford, up to **2147381248** bytes
(almost but less than 2GB, the actual size limit POSIX write() calls
have). Each chunk will result in a separate write call, hence minimizing
the number of chunks is preferred. The current default is set to 128MB,
so please increase this on large computers if you can and if you write
more than that amount of data per process, using the parameter
**BufferChunkSize**.

Second, BP5 can add a large user variable as a chunk to this list
without copying it at all and use it directly to write (or send to
aggregator). Put(..., adios2::Mode::Deferred) will handle the user data
directly, unless its size is below a threshold (see parameter
**MinDeferredSize**).

::: {.admonition .note}
Note

Do not call PerformPuts() when using BP5, because this call forces
copying all user data into the internal buffer before writing,
eliminating all benefits of zero-copy that BP5 provides when operating
with large buffers. Instead, consider using Put() with the Sync option
if you want to force ADIOS to copy data immediately. Alternatively, BP5
offers PerformDataWrite(), an collective operation that actually moves
data to storage, potentially freeing up buffer and application memory.
:::

Third, BP5 is using a shared memory segment on each compute node for
aggregation, instead of MPI. The best settings for the shared memory is
4GB (see parameter **MaxShmSize**), enough place for two chunks with the
POSIX write limit. More is useless but can be smaller if a
system/application cannot allow this much space for aggregation (but
there will be more write calls to disk as a result).
::::

::: {#span-object-in-internal-buffer .section}
### Span object in internal buffer[](#span-object-in-internal-buffer "Link to this heading"){.headerlink}

Another option to decrease memory consumption is to pre-allocate space
in the BP4/BP5 buffer and then prepare output variables directly in that
space. This will avoid a copy and the need for doubling memory for
temporary variables that are only created for output purposes. This Span
feature is only available in C++. See the Span() function in [[Engine
class]{.std
.std-ref}](#document-api_full/api_full#c-11-engine-class){.reference
.internal} ../api_full/api_full.html#engine-class
:::
:::::::

[]{#document-advanced/gpu_aware}

::::::::::::::::::::::::::: {#gpu-aware-i-o .section}
## GPU-aware I/O[](#gpu-aware-i-o "Link to this heading"){.headerlink}

The [`Put`{.docutils .literal .notranslate}]{.pre} and [`Get`{.docutils
.literal .notranslate}]{.pre} functions in the default file engine (BP5)
and some streaming engines (SST, DataMan) can receive user buffers
allocated on the host or the device in both Sync and Deferred modes.

::: {.admonition .note}
Note

Buffers allocated on the device with CUDA, HIP and SYCL are supported.
:::

If ADIOS2 is built without GPU support, only buffers allocated on the
host are supported. When GPU support is enabled, the default behavior is
for ADIOS2 to automatically detect where the buffer memory physically
resides.

Users can also provide information about where the buffer was allocated
by using the [`SetMemorySpace`{.docutils .literal .notranslate}]{.pre}
function within each variable.

:::: {.highlight-c++ .notranslate}
::: highlight
    enum class MemorySpace
    {
        Detect, ///< Detect the memory space automatically
        Host,   ///< Host memory space (default)
        GPU     ///< GPU memory spaces
    };
:::
::::

If ADIOS2 is built without GPU support, the available MemorySpace values
are only [`Detect`{.docutils .literal .notranslate}]{.pre} and
[`Host`{.docutils .literal .notranslate}]{.pre}.

ADIOS2 can use a CUDA or Kokkos backend for enabling GPU support. Only
one backend can be active at a given time based on how ADIOS2 is build.

:::::: {#building-adios2-with-a-gpu-backend .section}
### Building ADIOS2 with a GPU backend[](#building-adios2-with-a-gpu-backend "Link to this heading"){.headerlink}

By default both backends are [`OFF`{.docutils .literal
.notranslate}]{.pre} even if CUDA or Kokkos are installed and available
to avoid a possible conflict between if both backends are enabled at the
same time.

::: {#building-with-cuda-enabled .section}
#### Building with CUDA enabled[](#building-with-cuda-enabled "Link to this heading"){.headerlink}

The ADIOS2 default behavior is to turn [`OFF`{.docutils .literal
.notranslate}]{.pre} the CUDA backend. Building with the CUDA backend
requires [`-DADIOS2_USE_CUDA=ON`{.docutils .literal .notranslate}]{.pre}
and an available CUDA toolkit on the system.

When building ADIOS2 with CUDA enabled, the user is responsible with
setting the correct [`CMAKE_CUDA_ARCHITECTURES`{.docutils .literal
.notranslate}]{.pre} (e.g. for Summit the
[`CMAKE_CUDA_ARCHITECTURES`{.docutils .literal .notranslate}]{.pre}
needs to be set to 70 to match the NVIDIA Volta V100).
:::

:::: {#building-with-kokkos-enabled .section}
#### Building with Kokkos enabled[](#building-with-kokkos-enabled "Link to this heading"){.headerlink}

The Kokkos library can be used to enable GPU within ADIOS2. Based on how
Kokkos is build, either the CUDA, HIP or SYCL backend will be enabled.
Building with Kokkos requires [`-DADIOS2_USE_Kokkos=ON`{.docutils
.literal .notranslate}]{.pre}. The [`CMAKE_CUDA_ARCHITECTURES`{.docutils
.literal .notranslate}]{.pre} is set automanically to point to the same
architecture used when configuring the Kokkos library.

::: {.admonition .note}
Note

Kokkos version \>= 3.7 is required to enable the GPU backend in ADIOS2
:::
::::
::::::

:::::::::::: {#writing-gpu-buffers .section}
### Writing GPU buffers[](#writing-gpu-buffers "Link to this heading"){.headerlink}

The ADIOS2 API for Device pointers is identical to using Host buffers
for both the read and write logic. Internally each ADIOS2 variable holds
a memory space for the data it receives. Once the memory space is set
(eithr directly by the user through calls to [`SetMemorySpace`{.docutils
.literal .notranslate}]{.pre} or after detecting the buffer memory space
the first [`Put`{.docutils .literal .notranslate}]{.pre} or
[`Get`{.docutils .literal .notranslate}]{.pre} call) to either Host or
Device, it cannot be changed.

The [`examples/hello`{.docutils .literal .notranslate}]{.pre} folder contains several codes that use Device buffers:

:   - bpStepsWriteRead{Cuda\|Hip} show CUDA and HIP codes using BP5 with
      GPU pointers

    - bpStepsWriteReadKokkos contains Fortran and C++ codes using
      [`Kokkos::View`{.docutils .literal .notranslate}]{.pre} with
      different memory spaces and a Kokkos code using different layouts
      on Host buffers

    - datamanKokkos shows an example of streaming a
      [`Kokkos::View`{.docutils .literal .notranslate}]{.pre} with
      DataMan using different memory spaces

    - sstKokkos shows an example of streaming a
      [`Kokkos::View`{.docutils .literal .notranslate}]{.pre} with SST
      using different memory spaces

:::::::: {#example-using-a-device-buffer .section}
#### Example using a Device buffer[](#example-using-a-device-buffer "Link to this heading"){.headerlink}

The following is a simple example of writing data to storage directly
from a GPU buffer allocated with CUDA relying on the automatic detection
of device pointers in ADIOS2.

:::: {.highlight-c++ .notranslate}
::: highlight
    float *gpuSimData;
    cudaMalloc(&gpuSimData, N * sizeof(float));
    cudaMemset(gpuSimData, 0, N);
    auto data = io.DefineVariable<float>("data", shape, start, count);

    io.SetEngine("BP5");
    adios2::Engine bpWriter = io.Open(fname, adios2::Mode::Write);
    // Simulation steps
    for (size_t step = 0; step < nSteps; ++step)
    {
        bpWriter.BeginStep();
        bpWriter.Put(data, gpuSimData, adios2::Mode::Deferred); // or Sync
        bpWriter.EndStep();
    }
:::
::::

If the [`SetMemorySpace`{.docutils .literal .notranslate}]{.pre}
function is used, the ADIOS2 library will not detect automatically where
the buffer was allocated and will use the information provided by the
user for all subsequent Puts or Gets. Example:

:::: {.highlight-c++ .notranslate}
::: highlight
    data.SetMemorySpace(adios2::MemorySpace::GPU);
    for (size_t step = 0; step < nSteps; ++step)
    {
        bpWriter.BeginStep();
        bpWriter.Put(data, gpuSimData, adios2::Mode::Deferred); // or Sync
        bpWriter.EndStep();
    }
:::
::::

Underneath, ADIOS2 relies on the backend used at build time to transfer
the data. If ADIOS2 was build with CUDA, only CUDA buffers can be
provided. If ADIOS2 was build with Kokkos (with CUDA enabled) only CUDA
buffers can be provided. If ADIOS2 was build with Kokkos (with HIP
enabled) only HIP buffers can be provided.

::: {.admonition .note}
Note

The SYCL backend in Kokkos can be used to run on Nvida, AMD and Intel
GPUs, but we recommand using SYCL for Intel, HIP for AMD and CUDA for
Nvidia.
:::
::::::::

::::: {#kokkos-applications .section}
#### Kokkos applications[](#kokkos-applications "Link to this heading"){.headerlink}

ADIOS2 supports GPU buffers provided in the form of
[`Kokkos::View`{.docutils .literal .notranslate}]{.pre} directly in the
Put/Get calls. The memory space is automatically detected from the View
information. In addition to the memory space, for
[`Kokkos::View`{.docutils .literal .notranslate}]{.pre} ADIOS2 also
extracts the layout of the array and adjust the variable dimensions to
be able to build the global shape (across ranks) of the array.

:::: {.highlight-c++ .notranslate}
::: highlight
    Kokkos::View<float *, Kokkos::CudaSpace> gpuSimData("data", N);
    bpWriter.Put(data, gpuSimData);
:::
::::

If the CUDA backend is being used (and not Kokkos) to enable GPU support
in ADIOS2, Kokkos applications can still directly pass
[`Kokkos::View`{.docutils .literal .notranslate}]{.pre} as long as the
correct external header is included: [`#include`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`<adios2/cxx11/KokkosView.h>`{.docutils .literal
.notranslate}]{.pre}.
:::::
::::::::::::

::::::: {#reading-gpu-buffers .section}
### Reading GPU buffers[](#reading-gpu-buffers "Link to this heading"){.headerlink}

The GPU-aware backend allows different layouts for global arrays without
requiring the user to update the code for each case. The user defines
the shape of the global array and ADIOS2 adjusts the dimensions for each
rank according to the buffer layout and memory space.

The following example shows a global array of shape (4, 3) when running
with 2 ranks, each contributing half of it.

:::: {.highlight-text .notranslate}
::: highlight
    Write on LayoutRight, read on LayoutRight
    1 1 1  // rank 0
    2 2 2
    3 3 3  // rank 1
    4 4 4
    Write on LayoutRight, read on LayoutLeft
    1 2 3 4
    1 2 3 4
    1 2 3 4
:::
::::

On the read side, the Shape function can take a memory space or a layout
to return the correct dimensions of the variable. For the previous
example, if a C++ code using two ranks wants to read the data into a GPU
buffer, the Shape of the local array should be (3, 2). If the same data
will be read on CPU buffers, the shape should be (2, 3). Both of the
following code would give acceptable answers:

:::: {.highlight-c++ .notranslate}
::: highlight
    auto dims_host = data.Shape(adios2::MemorySpace::Host);
    auto dims_device = data.Shape(adios2::ArrayOrdering::ColumnMajor);
:::
::::
:::::::

:::: {#build-scripts .section}
### Build scripts[](#build-scripts "Link to this heading"){.headerlink}

The scripts/build_scripts folder contains scripts for building ADIOS2
with CUDA or Kokkos backends for several DOE system: Summit (OLCF
Nvidia), Crusher (OLCFi AMD), Perlmutter (NERSC Nvidia), Polaris (ALCF
Nvidia).

::: {.admonition .note}
Note

Perlmutter requires Kokkos \>= 4.0
:::
::::
:::::::::::::::::::::::::::

[]{#document-advanced/query}

:::::::::::::::: {#adios2-query-api .section}
## ADIOS2 query API[](#adios2-query-api "Link to this heading"){.headerlink}

The query API in ADIOS2 allows a client to pass a query in XML or json
format, and get back a list of blocks or sub-blocks that contains hits.
Both BP4 and BP5 engines are supported.

:::::::: {#the-interface .section}
### The interface[](#the-interface "Link to this heading"){.headerlink}

User is expected to pass a query file (configFile), and init a read
engine (engine) to construct a query and evaluate using the engine.
(note that the engine and query should be using the same ADIOS IO)

:::: {.highlight-c++ .notranslate}
::: highlight
    class QueryWorker
    {
    public:
        // configFile has query, can be either xml or json
        QueryWorker(const std::string &configFile, adios2::Engine &engine);

             // touched_blocks is a list of regions specified by (start, count),
             // that contains data that satisfies the query file
        void GetResultCoverage(std::vector<adios2::Box<adios2::Dims>> &touched_blocks);
    ...
    }
:::
::::

::::: {#a-sample-compound-query .section}
#### A Sample Compound Query[](#a-sample-compound-query "Link to this heading"){.headerlink}

This query targets a 1D variable "doubleV", data of interest is (x \>
6.6) or (x \< -0.17) or (2.8 \< x \< 2.9) In addition, this query also
specied an output region \[start=5,count=80\].

:::: {.highlight-xml .notranslate}
::: highlight
    <adios-query>
      <io name="query">
      <var name="doubleV">
        <boundingbox  start="5" count="80"/>
        <op value="OR">
          <range  compare="GT" value="6.6"/>
          <range  compare="LT" value="-0.17"/>
          <op value="AND">
             <range  compare="LT" value="2.9"/>
             <range  compare="GT" value="2.8"/>
          </op>
        </op>
      </var>
      </io>
    </adios-query>
:::
::::
:::::
::::::::

::::::::: {#code-examples .section}
### Code EXAMPLES:[](#code-examples "Link to this heading"){.headerlink}

::::: {#c .section}
#### C++:[](#c "Link to this heading"){.headerlink}

:::: {.highlight-c++ .notranslate}
::: highlight
    while (reader.BeginStep() == adios2::StepStatus::OK)
    {
        adios2::QueryWorker w = adios2::QueryWorker(queryFile, reader);
        w.GetResultCoverage(touched_blocks);

        std::cout << " ... now can read out touched blocks ... size=" << touched_blocks.size()
                  << std::endl;
    }
:::
::::

The Full C++ example is here:

:   [https://github.com/ornladios/ADIOS2/blob/master/examples/query/test.cpp](https://github.com/ornladios/ADIOS2/blob/master/examples/query/test.cpp){.reference
    .external}
:::::

::::: {#python .section}
#### Python:[](#python "Link to this heading"){.headerlink}

:::: {.highlight-python .notranslate}
::: highlight
    while (reader.BeginStep() == adios2.StepStatus.OK):
    # say only rank 0 wants to process result
    var = [queryIO.InquireVariable("T")]

    if (rank == 0):
        touched_blocks = w.GetResult()
        doAnalysis(reader, touched_blocks, var)
:::
::::

Full python example is here:

:   [https://github.com/ornladios/ADIOS2/blob/master/testing/adios2/bindings/python/TestQuery.py](https://github.com/ornladios/ADIOS2/blob/master/testing/adios2/bindings/python/TestQuery.py){.reference
    .external}

    This example generates data, the query file (in xml) and runs the
    query, all in python.
:::::
:::::::::
::::::::::::::::

[]{#document-advanced/plugins}

:::::::::::::::::::::::::::::: {#plugins .section}
## Plugins[](#plugins "Link to this heading"){.headerlink}

ADIOS now has the ability for users to load their own engines and
operators through the plugin interface. The basic steps for doing this
are:

1.  Write your plugin class, which needs to inherit from the appropriate
    [`Plugin*Interface`{.docutils .literal .notranslate}]{.pre} class.

2.  Build as a shared library and add the path to your shared library to
    the [`ADIOS2_PLUGIN_PATH`{.docutils .literal .notranslate}]{.pre}
    environment variable.

3.  Start using your plugin in your application.

These steps are discussed in further detail below.

::::::::: {#writing-your-plugin-class .section}
### Writing Your Plugin Class[](#writing-your-plugin-class "Link to this heading"){.headerlink}

::::: {#engine-plugin .section}
#### Engine Plugin[](#engine-plugin "Link to this heading"){.headerlink}

Your engine plugin class needs to inherit from the
[`PluginEngineInterface`{.docutils .literal .notranslate}]{.pre} class
in the [`adios2/engine/plugin/PluginEngineInterface.h`{.docutils
.literal .notranslate}]{.pre} header. Depending on the type of engine
you want to implement, you'll need to override a number of methods that
are inherited from the [`adios2::core::Engine`{.docutils .literal
.notranslate}]{.pre} class. These are briefly described in the following
table. More detailed documentation can be found in
[`adios2/core/Engine.h`{.docutils .literal .notranslate}]{.pre}.

  **Method**                                                    **Engine Type**   **Description**
  ------------------------------------------------------------- ----------------- -----------------------------------------------------------------------------------
  [`BeginStep()`{.docutils .literal .notranslate}]{.pre}        Read/Write        Indicates the beginning of a step
  [`EndStep()`{.docutils .literal .notranslate}]{.pre}          Read/Write        Indicates the end of a step
  [`CurrentStep()`{.docutils .literal .notranslate}]{.pre}      Read/Write        Returns current step info
  [`DoClose()`{.docutils .literal .notranslate}]{.pre}          Read/Write        Close a particular transport
  [`Init()`{.docutils .literal .notranslate}]{.pre}             Read/Write        Engine initialization
  [`InitParameters()`{.docutils .literal .notranslate}]{.pre}   Read/Write        Initialize parameters
  [`InitTransports()`{.docutils .literal .notranslate}]{.pre}   Read/Write        Initialize transports
  [`PerformPuts()`{.docutils .literal .notranslate}]{.pre}      Write             Execute all deferred mode [`Put`{.docutils .literal .notranslate}]{.pre}
  [`Flush()`{.docutils .literal .notranslate}]{.pre}            Write             Flushes data and metadata to a transport
  [`DoPut()`{.docutils .literal .notranslate}]{.pre}            Write             Implementation for [`Put`{.docutils .literal .notranslate}]{.pre}
  [`DoPutSync()`{.docutils .literal .notranslate}]{.pre}        Write             Implementation for [`Put`{.docutils .literal .notranslate}]{.pre} (Sync mode)
  [`DoPutDeferred()`{.docutils .literal .notranslate}]{.pre}    Write             Implementation for [`Put`{.docutils .literal .notranslate}]{.pre} (Deferred Mode)
  [`PerformGets()`{.docutils .literal .notranslate}]{.pre}      Read              Execute all deferred mode [`Get`{.docutils .literal .notranslate}]{.pre}
  [`DoGetSync()`{.docutils .literal .notranslate}]{.pre}        Read              Implementation for [`Get`{.docutils .literal .notranslate}]{.pre} (Sync mode)
  [`DoGetDeferred()`{.docutils .literal .notranslate}]{.pre}    Read              Implementation for [`Get`{.docutils .literal .notranslate}]{.pre} (Deferred Mode)

Examples showing how to implement an engine plugin can be found in
[`examples/plugins/engine`{.docutils .literal .notranslate}]{.pre}. An
example write engine is [`ExampleWritePlugin.h`{.docutils .literal
.notranslate}]{.pre}, while an example read engine is in
[`ExampleReadPlugin.h`{.docutils .literal .notranslate}]{.pre}. The
writer is a simple file writing engine that creates a directory (called
[`ExamplePlugin`{.docutils .literal .notranslate}]{.pre} by default) and
writes variable information to vars.txt and actual data to data.txt. The
reader example reads the files output by the writer example.

In addition to implementing the methods above, you'll need to implement
[`EngineCreate()`{.docutils .literal .notranslate}]{.pre} and
[`EngineDestroy()`{.docutils .literal .notranslate}]{.pre} functions so
ADIOS can create/destroy the engine object. Because of C++ name
mangling, you'll need to use [`extern`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"C"`{.docutils
.literal .notranslate}]{.pre}. Looking at
[`ExampleWritePlugin.h`{.docutils .literal .notranslate}]{.pre}, this
looks like:

:::: {.highlight-c++ .notranslate}
::: highlight
    extern "C" {

    adios2::plugin::ExampleWritePlugin *
    EngineCreate(adios2::core::IO &io, const std::string &name,
                 const adios2::Mode mode, adios2::helper::Comm comm)
    {
        return new adios2::plugin::ExampleWritePlugin(io, name, mode,
                                                            comm.Duplicate());
    }

    void EngineDestroy(adios2::plugin::ExampleWritePlugin * obj)
    {
        delete obj;
    }

    }
:::
::::
:::::

::::: {#operator-plugin .section}
#### Operator Plugin[](#operator-plugin "Link to this heading"){.headerlink}

Your operator plugin class needs to inherit from the
[`PluginOperatorInterface`{.docutils .literal .notranslate}]{.pre} class
in the [`adios2/operator/plugin/PluginOperatorInterface.h`{.docutils
.literal .notranslate}]{.pre} header. There's three methods that you'll
need to override from the [`adios2::core::Operator`{.docutils .literal
.notranslate}]{.pre} class, which are described below.

  **Method**                                                     **Description**
  -------------------------------------------------------------- -------------------------------------------------------
  [`Operate()`{.docutils .literal .notranslate}]{.pre}           Performs the operation, e.g., compress data
  [`InverseOperate()`{.docutils .literal .notranslate}]{.pre}    Performs the inverse operation, e.g., decompress data
  [`IsDataTypeValid()`{.docutils .literal .notranslate}]{.pre}   Checks that a given data type can be processed

An example showing how to implement an operator plugin can be found at
[`plugins/EncryptionOperator.h`{.docutils .literal .notranslate}]{.pre}
and [`plugins/EncryptionOperator.cpp`{.docutils .literal
.notranslate}]{.pre}. This operator uses
[libsodium](https://doc.libsodium.org/){.reference .external} for
encrypting and decrypting data.

In addition to implementing the methods above, you'll need to implement
[`OperatorCreate()`{.docutils .literal .notranslate}]{.pre} and
[`OperatorDestroy()`{.docutils .literal .notranslate}]{.pre} functions
so ADIOS can create/destroy the operator object. Because of C++ name
mangling, you'll need to use [`extern`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`"C"`{.docutils
.literal .notranslate}]{.pre}. Looking at
[`EncryptionOperator`{.docutils .literal .notranslate}]{.pre}, this
looks like:

:::: {.highlight-c++ .notranslate}
::: highlight
    extern "C" {

    adios2::plugin::EncryptionOperator *
    OperatorCreate(const adios2::Params &parameters)
    {
        return new adios2::plugin::EncryptionOperator(parameters);
    }

    void OperatorDestroy(adios2::plugin::EncryptionOperator * obj)
    {
        delete obj;
    }

    }
:::
::::
:::::
:::::::::

:::::::::: {#build-shared-library .section}
### Build Shared Library[](#build-shared-library "Link to this heading"){.headerlink}

To build your plugin, your CMake should look something like the
following (using the plugin engine example described above):

:::: {.highlight-cmake .notranslate}
::: highlight
    find_package(ADIOS2 REQUIRED)
    set(BUILD_SHARED_LIBS ON)
    add_library(PluginEngineWrite
      ExampleWritePlugin.cpp
    )
    target_link_libraries(PluginEngineWrite adios2::cxx11 adios2::core)
:::
::::

When using the Plugin Engine, ADIOS will check for your plugin at the
path specified in the [`ADIOS2_PLUGIN_PATH`{.docutils .literal
.notranslate}]{.pre} environment variable. If
[`ADIOS2_PLUGIN_PATH`{.docutils .literal .notranslate}]{.pre} is not
set, and a path is not specified when loading your plugin (see below
steps for using a plugin in your application), then the usual
[`dlopen`{.docutils .literal .notranslate}]{.pre} search is performed
(see the [dlopen man
page](https://man7.org/linux/man-pages/man3/dlopen.3.html){.reference
.external}).

::: {.admonition .note}
Note

The [`ADIOS2_PLUGIN_PATH`{.docutils .literal .notranslate}]{.pre}
environment variable can contain multiple paths, which must be separated
with a [`:`{.docutils .literal .notranslate}]{.pre}.
:::

When building on Windows, you will likely need to explicitly export the
Create and Destroy symbols for your plugin, as symbols are invisible by
default on Windows. To do this in a portable way across platforms, you
can add something similar to the following lines to your CMakeLists.txt:

:::: {.highlight-cmake .notranslate}
::: highlight
    include(GenerateExportHeader)
    generate_export_header(PluginEngineWrite BASE_NAME plugin_engine_write)
    target_include_directories(PluginEngineWrite PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
        $<INSTALL_INTERFACE:include>)
:::
::::

Then in your plugin header, you'll need to [`#include`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`"plugin_engine_write_export.h"`{.docutils .literal
.notranslate}]{.pre}. Then edit your function defintions as follows:

:::: {.highlight-c++ .notranslate}
::: highlight
    extern "C" {

    PLUGIN_ENGINE_WRITE_EXPORT adios2::plugin::ExampleWritePlugin *
        EngineCreate(adios2::core::IO &io, const std::string &name,
                 const adios2::Mode mode, adios2::helper::Comm comm);

    PLUGIN_ENGINE_WRITE_EXPORT void
        EngineDestroy(adios2::plugin::ExampleWritePlugin * obj);

    }
:::
::::
::::::::::

:::::::::::::: {#using-your-plugin-in-an-application .section}
### Using Your Plugin in an Application[](#using-your-plugin-in-an-application "Link to this heading"){.headerlink}

For both types of plugins, loading the plugin is done by setting the
[`PluginName`{.docutils .literal .notranslate}]{.pre} and
[`PluginLibrary`{.docutils .literal .notranslate}]{.pre} parameters in
an [`adios2::Params`{.docutils .literal .notranslate}]{.pre} object or
[`<parameter>`{.docutils .literal .notranslate}]{.pre} XML tag.

::::::: {#engine-plugins .section}
#### Engine Plugins[](#engine-plugins "Link to this heading"){.headerlink}

For engine plugins, this looks like:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::ADIOS adios;
    adios2::IO io = adios.DeclareIO("writer");
    io.SetEngine("Plugin");
    adios2::Params params;
    params["PluginName"] = "WritePlugin";
    params["PluginLibrary"] = "PluginEngineWrite";
    // If the engine plugin has any other parameters, these can be added to
    // the same params object and they will be forwarded to the engine
    io.SetParameters(params);
:::
::::

Where "WritePlugin" is the name that ADIOS will use to keep track of the
plugin, and "PluginEngineWrite" is the shared library name. At this
point you can open the engine and use it as you would any other ADIOS
engine. You also shouldn't need to make any changes to your CMake files
for your application.

The second option is using an ADIOS XML config file. If you'd like to
load your plugins through an XML config file, the following shows an
example XML when using Engine Plugins:

:::: {.highlight-xml .notranslate}
::: highlight
    <adios-config>
        <io name="writer">
            <engine type="Plugin">
                <parameter key="PluginName" value="WritePlugin" />
                <parameter key="PluginLibrary" value="PluginEngineWrite" />
                <!-- any parameters needed for your plugin can be added here in the parameter tag -->
            </engine>
        </io>
        <io name="reader">
            <engine type="Plugin">
                <parameter key="PluginName" value="ReadPlugin" />
                <parameter key="PluginLibrary" value="PluginEngineRead" />
                <!-- any parameters needed for your plugin can be added here in the parameter tag -->
            </engine>
        </io>
    </adios-config>
:::
::::

The examples
[`examples/plugins/engine/examplePluginEngine_write.cpp`{.docutils
.literal .notranslate}]{.pre} and
[`examples/plugins/engine/examplePluginEngine_read.cpp`{.docutils
.literal .notranslate}]{.pre} are an example of how to use the engine
plugins described above.
:::::::

:::::::: {#operator-plugins .section}
#### Operator Plugins[](#operator-plugins "Link to this heading"){.headerlink}

For operator plugins, the code to use your plugin looks like:

:::: {.highlight-c++ .notranslate}
::: highlight
    // for an adios2::Variable<T> var
    adios2::Params params;
    params["PluginName"] = "MyOperator";
    params["PluginLibrary"] = "EncryptionOperator";
    // example param required for the EncryptionOperator
    params["SecretKeyFile"] = "test-key";
    var.AddOperation("plugin", params);
:::
::::

If you'd like to load your operator plugin through an XML config file,
the following shows an example:

:::: {.highlight-xml .notranslate}
::: highlight
    <adios-config>
        <io name="writer">
            <variable name="data">
                <operation type="plugin">
                    <parameter key="PluginName" value="OperatorPlugin"/>
                    <parameter key="PluginLibrary" value="EncryptionOperator" />
                    <parameter key="SecretKeyFile" value="test-key" />
                </operation>
            </variable>
            <engine type="BP5">
            </engine>
        </io>
    </adios-config>
:::
::::

The examples
[`examples/plugins/operator/examplePluginOperator_write.cpp`{.docutils
.literal .notranslate}]{.pre} and
[`examples/plugins/engine/examplePluginOperator_read.cpp`{.docutils
.literal .notranslate}]{.pre} show an example of how to use the
[`EncryptionOperator`{.docutils .literal .notranslate}]{.pre} plugin
described above.

::: {.admonition .note}
Note

You don't need to add the [`lib`{.docutils .literal .notranslate}]{.pre}
prefix or the shared library ending (e.g., [`.so`{.docutils .literal
.notranslate}]{.pre}, [`.dll`{.docutils .literal .notranslate}]{.pre},
etc.) when setting [`PluginLibrary`{.docutils .literal
.notranslate}]{.pre}. ADIOS will add these when searching for your
plugin library. If you do add the prefix/suffix, ADIOS will still be
able to find your plugin. It's also possible to put the full path to the
shared library here, instead of using [`ADIOS2_PLUGIN_PATH`{.docutils
.literal .notranslate}]{.pre}.
:::
::::::::
::::::::::::::
::::::::::::::::::::::::::::::

[]{#document-advanced/campaign_management}

:::::::::::::::::: {#campaign-management .section}
## Campaign Management[](#campaign-management "Link to this heading"){.headerlink}

The campaign management in ADIOS2 is for collecting basic information
and metadata about a collection of ADIOS2 output files, from a single
application run or multiple runs. The campaign archive is a single file
(.ACA) that can be transferred to other locations. The campaign file can
be opened by ADIOS2 and all the metadata can be processed (including the
values of GlobalValue and LocalValue variables, or min/max of each
Arrays at each step and decomposition/min/max of each block in an Array
at each step). However, Get() operations will only succeed to read
actual data of the arrays, if the data belonging to the campaign is
either local or some mechanism for remote data access to the location of
the data is set up in advance.

::: {.admonition .warning}
Warning

In 2.10, Campaign Management is just a first prototype and is included
only for evaluation purposes. It will change substantially in the future
and campaign files produced by this version will unlikely to be
supported going forward.
:::

:::::: {#the-idea .section}
### The idea[](#the-idea "Link to this heading"){.headerlink}

Applications produce one or more output files in a single run.
Subsequent analysis and visualization runs produce more output files.
Campaign is a data organization concept one step higher than a file. A
campaign archive includes information about multiple files, including
the scalar variable's values and the min/max of arrays and the location
of the data files (host and directory information). A science project
can agree on how to organize their campaigns, i.e., how to name them,
what files to include in a single campaign archive, how to distribute
them, how to name the hosts where the actual data resides.

::::: {#example .section}
#### Example[](#example "Link to this heading"){.headerlink}

The Gray-Scott example, that is included with ADIOS2, in
examples/simulation/gray-scott, has two programs, Gray-Scott and
PDF-Calc. The first one produces the main output gs.bp which includes
the main 3D variables U and V, and a checkpoint file ckpt.bp with a
single step in it. PDF-Calc processes the main output and produces
histograms on 2D slices of U and V (U/bins and U/pdf) in pdf.bp. A
campaign can include all the three output files as they logically belong
together.

:::: {.highlight-bash .notranslate}
::: highlight
    # run application as usual
    $ mpirun -n 4 adios2_simulations_gray-scott settings-files.json
    $ ls -d *.bp
    ckpt.bp gs.bp

    $ adios2_campaign_manager.py create demoproject/frontier_gray-scott_100

    $ mpirun -n 3 adios2_simulations_gray-scott_pdf-calc gs.bp pdf.bp 1000
    $ ls -d *.bp
    ckpt.bp gs.bp pdf.bp

    $ adios2_campaign_manager.py update demoproject/frontier_gray-scott_100

    $ adios2_campaign_manager.py info  demoproject/frontier_gray-scott_100
    info archive
    ADIOS Campaign Archive, version 1.0, created on 2024-04-01 10:44:11.644942
    hostname = OLCF   longhostname = frontier.olcf.ornl.gov
        dir = /lustre/orion/csc143/proj-shared/demo/gray-scott
            dataset = ckpt.bp     created on 2024-04-01 10:38:19
            dataset = gs.bp     created on 2024-04-01 10:38:17
            dataset = pdf.bp     created on 2024-04-01 10:38:08

    # The campaign archive is small compared to the data it points to
    $ du -sh *bp
    7.9M    ckpt.bp
    40M     gs.bp
    9.9M    pdf.bp

    $ du -sh /lustre/orion/csc143/proj-shared/adios-campaign-store/demoproject/frontier_gray-scott_100.aca
    97K     /lustre/orion/csc143/proj-shared/adios-campaign-store/demoproject/frontier_gray-scott_100.aca

    # ADIOS can list the content of the campaign archive
    $ bpls -l demoproject/frontier_gray-scott_100
        double   ckpt.bp/U      {4, 34, 34, 66} = 0.171103 / 1
        double   ckpt.bp/V      {4, 34, 34, 66} = 1.71085e-19 / 0.438921
        int32_t  ckpt.bp/step   scalar = 700
        double   gs.bp/U        10*{64, 64, 64} = 0.090778 / 1
        double   gs.bp/V        10*{64, 64, 64} = 8.24719e-63 / 0.515145
        int32_t  gs.bp/step     10*scalar = 100 / 1000
        double   pdf.bp/U/bins  10*{1000} = 0.0908158 / 0.999938
        double   pdf.bp/U/pdf   10*{64, 1000} = 0 / 4096
        double   pdf.bp/V/bins  10*{1000} = 8.24719e-63 / 0.514267
        double   pdf.bp/V/pdf   10*{64, 1000} = 0 / 4096
        int32_t  pdf.bp/step    10*scalar = 100 / 1000

    # scalar over steps is available in metadata
    $ bpls -l demoproject/frontier_gray-scott_100 -d pdf.bp/step -n 10
      int32_t  pdf.bp/step    10*scalar = 100 / 1000
        (0)    100 200 300 400 500 600 700 800 900 1000

    # Array decomposition including min/max are available in metadata
    $ bpls -l demoproject/frontier_gray-scott_100 -D gs.bp/V
      double   gs.bp/V        10*{64, 64, 64} = 8.24719e-63 / 0.515145
        step 0:
          block 0: [ 0:63,  0:31,  0:31] = 8.24719e-63 / 0.410653
          block 1: [ 0:63, 32:63,  0:31] = 8.24719e-63 / 0.410652
          block 2: [ 0:63,  0:31, 32:63] = 8.24719e-63 / 0.410653
          block 3: [ 0:63, 32:63, 32:63] = 8.24719e-63 / 0.410653
        ...
        step 9:
          block 0: [ 0:63,  0:31,  0:31] = 3.99908e-09 / 0.441847
          block 1: [ 0:63, 32:63,  0:31] = 3.99931e-09 / 0.44192
          block 2: [ 0:63,  0:31, 32:63] = 3.99928e-09 / 0.441813
          block 3: [ 0:63, 32:63, 32:63] = 3.99899e-09 / 0.441796

    # Array data is only available if data is local
    $ ./bin/bpls -l demoproject/frontier_gray-scott_100 -d pdf.bp/U/bins
      double   pdf.bp/U/bins  10*{1000} = 0.0908158 / 0.999938
        (0,  0)    0.93792 0.937982 0.938044 0.938106 0.938168 0.93823 0.938292 0.938354 0.938416 0.938479
        ...
        (9,990)    0.990306 0.991157 0.992007 0.992858 0.993708 0.994559 0.995409 0.99626 0.99711 0.997961
:::
::::
:::::
::::::

::::: {#setup .section}
### Setup[](#setup "Link to this heading"){.headerlink}

There are three paths/names important in the campaign setup.

- hostname is the name detected by the adios2_campaign_manager when
  creating a campaign archive, however, it is better to define a
  specific name the project agrees upon (e.g. OLCF, NERSC, ALCF) that
  identifies the generic location of the data and then use that name
  later to specify the modes of remote data access (not available in
  this release).

- campaignstorepath is the directory where all the campaign archives are
  stored. This should be shared between project members in a center, and
  a private one on every member's laptop. It is up to the project to
  determine what file sharing / synchronization mechanism to use to sync
  this directories. [Rclone is a great command-line
  tool](https://rclone.org){.reference .external} to sync the campaign
  store with many cloud-based file sharing services and cloud instances.

- cachepath is the directory where ADIOS can unpack metadata from the
  campaign archive so that ADIOS engines can read them as if they were
  entirely local datasets. The cache only contains the metadata for now
  but in the future data that have already been retrieved by previous
  read requests will be stored here as well.

Use \~/.config/adios2/adios2.yaml to specify these options.

:::: {.highlight-bash .notranslate}
::: highlight
    $ cat ~/.config/adios2/adios2.yaml

    Campaign:
      active: true
      hostname: OLCF
      campaignstorepath: /lustre/orion/csc143/proj-shared/adios-campaign-store
      cachepath: /lustre/orion/csc143/proj-shared/campaign-cache
      verbose: 0

    $ ls -R ~/dropbox/adios-campaign-store
    /lustre/orion/csc143/proj-shared/adios-campaign-store/demoproject:
    frontier_gray-scott_100.aca

    $ adios2_campaign_manager.py list
    demoproject/frontier_gray-scott_100.aca
:::
::::
:::::

::::::: {#remote-access .section}
### Remote access[](#remote-access "Link to this heading"){.headerlink}

For now, we have one way to access data, through SSH port forwarding and
running a remote server program to read in data on the remote host and
to send back the data to the local ADIOS program. adios2_remote_server
is included in the adios installation. You need to use the one built on
the host.

Launch the server by SSH-ing to the remote machine, and specifying the
26200 port for fowarding. For example:

:::: {.highlight-bash .notranslate}
::: highlight
    $ ssh -L 26200:dtn.olcf.ornl.gov:26200 -l <username> dtn.olcf.ornl.gov "<path_to_adios_install>/bin/adios2_remote_server -v "
:::
::::

Assuming the campaign archive was synced to a local machine's campaign
store under csc143/demoproject, now we can retrieve data:

:::: {.highlight-bash .notranslate}
::: highlight
    $ adios2_campaign_manager.py list
    csc143/demoproject/frontier_gray-scott_100.aca

    $ bpls -l csc143/demoproject/frontier_gray-scott_100
      double   ckpt.bp/U      {4, 34, 34, 66} = 0.171103 / 1
      ...
      double   pdf.bp/U/bins  10*{1000} = 0.0908158 / 0.999938

    # metadata is extracted to the local cachepath
    $ du -sh /tmp/campaign/OLCF/csc143/demoproject/frontier_gray-scott_100.aca/*
    20K     /tmp/campaign/OLCF/csc143/demoproject/frontier_gray-scott_100.aca/ckpt.bp
    40K     /tmp/campaign/OLCF/csc143/demoproject/frontier_gray-scott_100.aca/gs.bp
    32K     /tmp/campaign/OLCF/csc143/demoproject/frontier_gray-scott_100.aca/pdf.bp

    # data is requested from the remote server
    # read 16 values (4x4x4) from U from last step, from offset 30,30,30
    $ bpls -l csc143/demoproject/frontier_gray-scott_100  -d gs.bp/U -s "-1,30,30,30" -c "1,4,4,4" -n 4
    double   gs.bp/U        10*{64, 64, 64}
      slice (9:9, 30:33, 30:33, 30:33)
      (9,30,30,30)    0.89189 0.899854 0.899854 0.891891
      (9,30,31,30)    0.899851 0.908278 0.908278 0.899852
      (9,30,32,30)    0.899849 0.908276 0.908277 0.899851
      (9,30,33,30)    0.891885 0.899848 0.899849 0.891886
      (9,31,30,30)    0.89985 0.908276 0.908276 0.899849
      (9,31,31,30)    0.908274 0.916977 0.916977 0.908274
      (9,31,32,30)    0.908273 0.916976 0.916976 0.908273
      (9,31,33,30)    0.899844 0.908271 0.908271 0.899844
      (9,32,30,30)    0.89985 0.908276 0.908275 0.899848
      (9,32,31,30)    0.908274 0.916976 0.916976 0.908272
      (9,32,32,30)    0.908272 0.916975 0.916974 0.908271
      (9,32,33,30)    0.899844 0.90827 0.90827 0.899842
      (9,33,30,30)    0.89189 0.899851 0.899851 0.891886
      (9,33,31,30)    0.89985 0.908275 0.908275 0.899847
      (9,33,32,30)    0.899848 0.908274 0.908273 0.899845
      (9,33,33,30)    0.891882 0.899845 0.899844 0.89188
:::
::::
:::::::

::: {#requirements .section}
### Requirements[](#requirements "Link to this heading"){.headerlink}

The Campaign Manager uses SQlite3 and ZLIB for its operations, and
Python3 3.8 or higher for the adios2_campaign_manager tool. Check bpls
-Vv to see if CAMPAIGN is in the list of "Available features".
:::

::: {#limitations .section}
### Limitations[](#limitations "Link to this heading"){.headerlink}

- The Campaign Reader engine only supports ReadRandomAccess mode, not
  step-by-step reading. Campaign management will need to change in the
  future to support sorting the steps from different outputs to a
  coherent order.

- Updates to moving data for other location is not supported yet
:::
::::::::::::::::::

[]{#document-advanced/ecp_hardware}

::::::::: {#adios2-in-ecp-hardware .section}
## ADIOS2 in ECP hardware[](#adios2-in-ecp-hardware "Link to this heading"){.headerlink}

ADIOS2 is widely used in ECP (Exascale Computing Project) HPC (high
performance computing) systems, some particular ADIOS2 features needs
from specifics workarounds to run successfully.

:::::::: {#olcf-crusher .section}
### OLCF CRUSHER[](#olcf-crusher "Link to this heading"){.headerlink}

::::::: {#sst-mpi-data-transport .section}
#### SST MPI Data Transport[](#sst-mpi-data-transport "Link to this heading"){.headerlink}

MPI Data Transport relies on client-server features of MPI which are
currently supported in Cray-MPI implementations with some caveats. Here
are some of the observed issues and what its workaround (if any) are:

**MPI_Finalize** will block the system process in the "Writer/Producer"
ADIOS2 instance. The reason is that the Producer ADIOS instance
internally calls MPI_Open_port which somehow even after calling
MPI_Close_port MPI_Finalize still consider its port to be in used, hence
blocking the process. The workaround is to use a
MPI_Barrier(MPI_COMM_WORLD) instead of MPI_Finalize() call.

**srun does not understand mpmd instructions** Simply disable them with
the flag -DADIOS2_RUN_MPI_MPMD_TESTS=OFF

**Tests timeout** Since we launch every tests with srun the scheduling
times can exceed the test default timeout. Use a large timeout (5mins)
for running your tests.

Examples of launching ADIOS2 SST unit tests using MPI DP:

:::: {.highlight-bash .notranslate}
::: highlight
    # We omit some of the srun (SLURM) arguments which are specific of the project
    # you are working on. Note that you could avoid calling srun directly by
    # setting the CMAKE variable `MPIEXEC_EXECUTABLE`.

    # Launch simple writer test instance
    srun {PROJFLAGS } -N 1 /gpfs/alpine/proj-shared/csc331/vbolea/ADIOS2-build/bin/TestCommonWrite SST mpi_dp_test CPCommPattern=Min,MarshalMethod=BP5

    # On another terminal launch multiple instances of the Reader test
    srun {PROJFLAGS} -N 2 /gpfs/alpine/proj-shared/csc331/vbolea/ADIOS2-build/bin/TestCommonRead SST mpi_dp_test
:::
::::

Alternatively, you can configure your CMake build to use srun directly:

:::: {.highlight-bash .notranslate}
::: highlight
    cmake . -DMPIEXEC_EXECUTABLE:FILEPATH="/usr/bin/srun" \
         -DMPIEXEC_EXTRA_FLAGS:STRING="-A{YourProject} -pbatch -t10" \
         -DMPIEXEC_NUMPROC_FLAG:STRING="-N" \
         -DMPIEXEC_MAX_NUMPROCS:STRING="-8" \
         -DADIOS2_RUN_MPI_MPMD_TESTS=OFF

    cmake --build .
    ctest

    # monitor your jobs
    watch -n1 squeue -l -u $USER
:::
::::
:::::::
::::::::
:::::::::

[]{#document-advanced/derived_variables}

::::::::::::::: {#derived-variables .section}
## Derived variables[](#derived-variables "Link to this heading"){.headerlink}

Derived quantities are obtained by mathematical transformations of
primary data, and they typically allow researchers to focus on specific
aspects of the simulation. For instance, in combustion simulations that
generate velocity data, calculating the magnitude of the velocity
creates a derived variable that effectively identifies areas of high
interest, such as regions with intense burning. Applications can offload
the computation of derived variables to ADIOS2.

::: {.admonition .note}
Note

Examples for defining and storing derived variables can be found in
examples/hello/bpStepsWriteReadDerived folder
:::

The API to define a derived variable on the write side requires
providing a math expression over primary variables and the desired type
of derived variable.

The math expression defines aliases for ADIOS2 variables that will be
used in the expression and math operations over the aliases (example
provided below). A list of supported math operations is provided at the
bottom of this page.

:::: {.highlight-c++ .notranslate}
::: highlight
    enum class DerivedVarType
    {
        StatsOnly, // only stats are saved
        StoreData     // data is stored in addition to metadata
    }
:::
::::

There are currently two types of derived variables accepted by ADIOS2,
one that saves only stats about the variables (min/max for each block)
and one that saves data in addition to the stats, just like a primary
variable.

:::: {.highlight-c++ .notranslate}
::: highlight
    auto Ux = bpOut.DefineVariable<float>("var/Ux", {Nx, Ny}, {0, 0}, {Nx, Ny});
    auto Uy = bpOut.DefineVariable<float>("var/Uy", {Nx, Ny}, {0, 0}, {Nx, Ny});
    bpOut.DefineDerivedVariable("derived/magnitude,
                                "x = var/Ux \n"
                                "y = var/Uy \n"
                                "magnitude(x, y)",
                                adios2::DerivedVarType::StatsOnly);
:::
::::

Derived variables can be defined at any time and are computed (and
potentially stored) during the [`EndStep`{.docutils .literal
.notranslate}]{.pre} operation.

The [`bpls`{.docutils .literal .notranslate}]{.pre} utility can identify
derived variables and show the math expression when the
[`--show-derived`{.docutils .literal .notranslate}]{.pre} option.
Derived variables that store data become primary data once the write
operation is done, so they are not identified as derive variables by
bpls.

:::: {.highlight-text .notranslate}
::: highlight
      $ bpls StepsWriteReadDerived.bp --show-derived -l
    float    var/Ux          10*{60000} = 0 / 45
    float    var/Uy          10*{60000} = 0 / 90
    float    derived/magnitude  10*{60000} = 0 / 100.623
      Derived variable with expression: MAGNITUDE({var/Ux},{var/Uy})
:::
::::

::: {.admonition .note}
Note

Derived variables are currently supported only by the BP5 engine
:::

::: {#build-adios2-with-support-for-derived-variables .section}
### Build ADIOS2 with support for derived variables[](#build-adios2-with-support-for-derived-variables "Link to this heading"){.headerlink}

By default the derived variables are [`OFF`{.docutils .literal
.notranslate}]{.pre}. Building ADIOS2 with derived variables turned on
requires [`-DADIOS2_USE_Derived_Variables=ON`{.docutils .literal
.notranslate}]{.pre}.
:::

::::: {#supported-derived-operations .section}
### Supported derived operations[](#supported-derived-operations "Link to this heading"){.headerlink}

In the current implementation, all input variables for a derived
operation need to have the same type.

  Operation                                         Input                                                                              Output                                                                                                                                                                                                                                                                                                                                                                                                                                                   Expression
  ------------------------------------------------- ---------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------
  Addition, Subtraction, Multiplication, Division   All inputs must have the same dimension. Can work on multiple variables at once.   Output variables will have the same type and dimension as the input variables.                                                                                                                                                                                                                                                                                                                                                                           a+b, add(a,b), a-b, subtract(a,b), a\*b, multily(a,b), a/b, divide(a,b)
  Sqrt, Power                                       Can only be applied on single variables.                                           Return variables of the same dimension as the input variable, but of type [`long`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`double`{.docutils .literal .notranslate}]{.pre} (for [`long`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`double`{.docutils .literal .notranslate}]{.pre} input variable) or [`double`{.docutils .literal .notranslate}]{.pre} (for the anything else).   sqrt(a), pow(a)
  Magnitude                                         All inputs must have the same dimension. Can work on multiple variables at once.   Output variables will have the same type and dimension as the input variables.                                                                                                                                                                                                                                                                                                                                                                           magnitude(a, b)
  Curl3D                                            All inputs must have the same dimension. Must receive 3 variables.                 Output variables will have the same type and dimension as the input variables. The shape of the variable will have an extra dimension equal to 3 (e.g. for inputs of shape (d1, d2, d3), the curl variable will have shape (d1, d2, d3, 3))                                                                                                                                                                                                              curl(a, b, c)

  : [Supported derived
  operations]{.caption-text}[](#id1 "Link to this table"){.headerlink}
  {#id1}

The math operations in the table above can be combined to create complex
derived expressions that are evaluated one by one. The dimensions and
types need to correspond to the requirements of each operation (like in
the following example).

:::: {.highlight-text .notranslate}
::: highlight
    expression= "sqrt(curl(a,b,c)) + y"
:::
::::

The variables corresponding to a, b and c need to have the same shape
and same type (example [`<int>(d1,`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`d2,`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`d3)`{.docutils .literal .notranslate}]{.pre}). The curl
operation will generate a variable of shape (d1, d2, d3, 3) and the sqrt
will generate a double typed variable of shape (d1, d2, d3, 3). For the
add operation to be applied, the y variable needs to be of type double
and shape (d1, d2, d3, 3).
:::::
:::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.toctree-wrapper .compound}
[]{#document-tutorials/overview}

::: {#overview .section}
## Overview[](#overview "Link to this heading"){.headerlink}

In this tutorial we will learn about how to build ADIOS2, and go through
several tutorials explaining basic topics.

More specifically, we will go through the following examples:

1.  [[Download And Build]{.std
    .std-ref}](#document-tutorials/downloadAndBuild#sec-tutorials-download-and-build){.reference
    .internal}

2.  Basic tutorials:

    1.  [[Hello World]{.std
        .std-ref}](#document-tutorials/helloWorld#sec-tutorials-basics-hello-world){.reference
        .internal}

    2.  [[Array Variables]{.std
        .std-ref}](#document-tutorials/variables#sec-tutorials-basics-variables){.reference
        .internal}

    3.  [[Attributes]{.std
        .std-ref}](#document-tutorials/attributes#sec-tutorials-basics-attributes){.reference
        .internal}

    4.  [[Operators]{.std
        .std-ref}](#document-tutorials/operators#sec-tutorials-basics-operators){.reference
        .internal}

    5\. [[Steps]{.std
    .std-ref}](#document-tutorials/steps#sec-tutorials-basics-steps){.reference
    .internal} 5. [[Running the staging engine]{.std
    .std-ref}](#document-tutorials/sst#sec-tutorials-sst){.reference
    .internal}

More advance tutorials that cover more information related to:

- Running ADIOS2 at scale (through files or streaming) with hands-on
  excercises: [Exascale I/O
  tutorial](http://tinyurl.com/adios-eied){.reference .external}

- Using ADIOS2 with Paraview, TAU, Catalyst, FIDES, VTK-M: [ADIOS2
  tutorial at SC23](http://tinyurl.com/adios-sc2023){.reference
  .external}
:::

[]{#document-tutorials/downloadAndBuild}

::::::::::: {#download-and-build .section}
## Download And Build[](#download-and-build "Link to this heading"){.headerlink}

First, you need to clone the ADIOS2 repository. You can do this by
running the following command:

:::: {.highlight-bash .notranslate}
::: highlight
    git clone https://github.com/ornladios/ADIOS2.git ADIOS2
:::
::::

::: {.admonition .note}
Note

ADIOS2 uses [CMake](https://cmake.org/){.reference .external} for
building, testing and installing the library and utilities. So you need
to have CMake installed on your system.
:::

Then, create a build directory, run CMake, and build ADIOS2:

:::: {.highlight-bash .notranslate}
::: highlight
    cd ADIOS2
    mkdir build
    cd build
    cmake -DADIOS2_USE_MPI=ON ..
    cmake --build .
:::
::::

::: {.admonition .note}
Note

If you want to know more about the ADIOS2's CMake options, see section
[[CMake Options]{.std
.std-ref}](#document-setting_up/setting_up#sec-source-cmake-options){.reference
.internal}.
:::

All the tutorials that we will explore are existing ADIOS2 examples
located in the [`ADIOS2/examples`{.docutils .literal
.notranslate}]{.pre} directory.

To build any of the examples, e.g. the [`helloWorld`{.docutils .literal
.notranslate}]{.pre} example, you can run the following commands:

:::: {.highlight-bash .notranslate}
::: highlight
    cd Path-To-ADIOS2/examples/hello/helloWorld
    mkdir build
    cd build
    cmake -DADIOS2_DIR=Path-To-ADIOS2/build/ ..
    cmake --build .
:::
::::
:::::::::::

[]{#document-tutorials/basicTutorials}

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#basic-tutorials .section}
## Basic Tutorials[](#basic-tutorials "Link to this heading"){.headerlink}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {.toctree-wrapper .compound}
[]{#document-tutorials/helloWorld}

:::::::::::::::::::::::::::::: {#hello-world .section}
### Hello World[](#hello-world "Link to this heading"){.headerlink}

Like in any language, the first program you write is the "Hello World"
program.

In this tutorial, we will see how to write "Hello World from ADIOS2" and
read it back with ADIOS2. So let's dig in!

Start editing the skeleton file
[ADIOS2/examples/hello/helloWorld/hello-world_tutorialSkeleton.cpp](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/helloWorld/hello-world_tutorialSkeleton.cpp){.reference
.external}.

1.  We create an ADIOS instance, and define the greeting message in our
    main function as follows:

:::: {.highlight-c++ .notranslate}
::: highlight
    int main()
    {
      adios2::ADIOS adios();
      const std::string greeting("Hello World from ADIOS2");
      ...
      return 0;
    }
:::
::::

2.  Then we create a writer function in which we pass the adios
    instance, and the greeting message as follows:

:::: {.highlight-c++ .notranslate}
::: highlight
    void writer(adios2::ADIOS& adios, const std::string& greeting)
    {
      ...
    }
:::
::::

3.  In this writer function, we define an IO object, a string variable
    for the message as follows:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::IO io = adios.DeclareIO("hello-world-writer");
    adios2::Variable<std::string> varGreeting = io.DefineVariable<std::string>("Greeting");
:::
::::

::: {.admonition .note}
Note

Using the IO object, we can define the engine type that we want to
utilize using the *io.SetEngine()* function. If *SetEngine()* is not
used, the default engine type is *BPFile* which is an alias for the
latest version of the BP engine of the ADIOS2 library. See [[Available
Engines]{.std
.std-ref}](#document-components/components#available-engines){.reference
.internal} and [[Supported Engines]{.std
.std-ref}](#document-engines/engines#supported-engines){.reference
.internal} for more information. It's important to note that the file
extension of an output file, although it's not a good practice, it can
differ from the engine type, e.g. write a foo.h5 file with the BPFile
engine. When reading foo.h5 you should explicitly specify the engine
type as BPFile to read it properly.
:::

4.  Then we open a file with the name "hello-world-cpp.bp" and write the
    greeting message to it as follows:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::Engine writer = io.Open("hello-world-cpp.bp", adios2::Mode::Write);
    writer.BeginStep();
    writer.Put(varGreeting, greeting);
    writer.EndStep();
    writer.Close();
:::
::::

::: {.admonition .note}
Note

The [`BeginStep`{.docutils .literal .notranslate}]{.pre} and
[`EndStep`{.docutils .literal .notranslate}]{.pre} calls are optional
when **writing** one step, but they are required for multiple steps, so
it is a good practice to always use them.
:::

5.  Now we create a reader function in which we pass the adios instance,
    and get the greeting message back as follows:

:::: {.highlight-c++ .notranslate}
::: highlight
    std::string reader(adios2::ADIOS& adios)
    {
      ...
    }
:::
::::

6.  In this reader function, we define an IO object and inquire a string
    variable for the message as follows:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::IO io = adios.DeclareIO("hello-world-reader");
    reader.BeginStep();
    adios2::Variable<std::string> varGreeting = io.InquireVariable<std::string>("Greeting");
:::
::::

7.  Then we open the file with the name "hello-world-cpp.bp", read the
    greeting message from it and return it as follows:

:::: {.highlight-c++ .notranslate}
::: highlight
    adios2::Engine reader = io.Open("hello-world-cpp.bp", adios2::Mode::Read);
    std::string greeting;
    reader.BeginStep();
    reader.Get(varGreeting, greeting);
    reader.EndStep();
    reader.Close();
    return greeting;
:::
::::

::: {.admonition .note}
Note

In Mode::Read, the [`BeginStep`{.docutils .literal .notranslate}]{.pre}
and [`EndStep`{.docutils .literal .notranslate}]{.pre} calls are
required when **reading** one step and multiple steps. We will see in
another tutorial how to read multiple steps. It's important to note that
the [`BeginStep`{.docutils .literal .notranslate}]{.pre} should be
called **before** all [`Inquire*`{.docutils .literal
.notranslate}]{.pre} / [`Available*`{.docutils .literal
.notranslate}]{.pre} function calls.
:::

8.  Finally, we call the writer and reader functions in our main
    function as follows:

:::: {.highlight-c++ .notranslate}
::: highlight
    int main()
    {
      adios2::ADIOS adios();
      const std::string greeting("Hello World from ADIOS2");
      writer(adios, greeting);
      std::string message = reader(adios);
      std::cout << message << std::endl;
      return 0;
    }
:::
::::

9.  The final code should look as follows (excluding try/catch and the
    optional usage of MPI), and it was derived from the example
    [ADIOS2/examples/hello/helloWorld/hello-world.cpp](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/helloWorld/hello-world.cpp){.reference
    .external}.

:::: {.highlight-cpp .notranslate}
::: highlight
    /*
     * Distributed under the OSI-approved Apache License, Version 2.0.  See
     * accompanying file Copyright.txt for details.
     *
     * hello-world.cpp : adios2 low-level API example to write and read a
     *                   std::string Variable with a greeting
     *
     *  Created on: Nov 14, 2019
     *      Author: William F Godoy godoywf@ornl.gov
     */

    #include <iostream>
    #include <stdexcept>

    #include <adios2.h>
    #if ADIOS2_USE_MPI
    #include <mpi.h>
    #endif

    void writer(adios2::ADIOS &adios, const std::string &greeting)
    {
        adios2::IO io = adios.DeclareIO("hello-world-writer");
        adios2::Variable<std::string> varGreeting = io.DefineVariable<std::string>("Greeting");

        adios2::Engine writer = io.Open("hello-world-cpp.bp", adios2::Mode::Write);
        writer.BeginStep();
        writer.Put(varGreeting, greeting);
        writer.EndStep();
        writer.Close();
    }

    std::string reader(adios2::ADIOS &adios)
    {
        adios2::IO io = adios.DeclareIO("hello-world-reader");
        adios2::Engine reader = io.Open("hello-world-cpp.bp", adios2::Mode::Read);
        reader.BeginStep();
        adios2::Variable<std::string> varGreeting = io.InquireVariable<std::string>("Greeting");
        std::string greeting;
        reader.Get(varGreeting, greeting);
        reader.EndStep();
        reader.Close();
        return greeting;
    }

    int main(int argc, char *argv[])
    {
    #if ADIOS2_USE_MPI
        MPI_Init(&argc, &argv);
    #endif

        try
        {
    #if ADIOS2_USE_MPI
            adios2::ADIOS adios(MPI_COMM_WORLD);
    #else
            adios2::ADIOS adios;
    #endif

            const std::string greeting = "Hello World from ADIOS2";
            writer(adios, greeting);

            const std::string message = reader(adios);
            std::cout << message << "\n";
        }
        catch (std::exception &e)
        {
            std::cout << "ERROR: ADIOS2 exception: " << e.what() << "\n";
    #if ADIOS2_USE_MPI
            MPI_Abort(MPI_COMM_WORLD, -1);
    #endif
        }

    #if ADIOS2_USE_MPI
        MPI_Finalize();
    #endif

        return 0;
    }
:::
::::

10. You can compile and run it as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    cd Path-To-ADIOS2/examples/hello/helloWorld
    mkdir build
    cd build
    cmake -DADIOS2_DIR=Path-To-ADIOS2/build/ ..
    cmake --build .
    ./adios2_hello_helloWorld
:::
::::

11. You can check the content of the output file "hello-world-cpp.bp"
    using *bpls* as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    Path-To-ADIOS2/build/bin/bpls ./hello-world-cpp.bp

       string   Greeting  scalar
:::
::::

12. The Python version of this tutorial can be found at
    [ADIOS2/examples/hello/helloWorld/hello-world.py](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/helloWorld/hello-world.py){.reference
    .external}. and it looks as follows:

:::: {.highlight-python .notranslate}
::: highlight
    #
    # Distributed under the OSI-approved Apache License, Version 2.0.  See
    # accompanying file Copyright.txt for details.
    #
    # hello-world.py : adios2 Python API example to write and read a
    #                   string Variable with a greeting
    #
    #  Created on: 2/2/2021
    #      Author: Dmitry Ganyushin ganyushindi@ornl.gov
    #
    import sys
    from mpi4py import MPI
    from adios2 import Stream, FileReader

    DATA_FILENAME = "hello-world-py.bp"
    # MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()


    def writer(greeting):
        """write a string to a bp file"""
        with Stream(DATA_FILENAME, "w", comm) as fh:
            fh.write("Greeting", greeting)
        return 0


    def reader():
        """read a string from a bp file as Stream"""
        message = f"variable Greeting not found in {DATA_FILENAME}"
        with Stream(DATA_FILENAME, "r", comm) as fh:
            for _ in fh.steps():
                message = fh.read("Greeting")
        return message


    def filereader():
        """read a string from a bp file using random access read mode"""
        with FileReader(DATA_FILENAME, comm) as fh:
            message = fh.read("Greeting")
        return message


    def main():
        """driver function"""
        greeting = "Hello World from ADIOS2"
        writer(greeting)
        message = reader()
        print("As read from adios2.Stream: {}".format(message))
        message2 = filereader()
        print("As read from adios2.FileReader: {}".format(message2))
        return 0


    if __name__ == "__main__":
        sys.exit(main())
:::
::::
::::::::::::::::::::::::::::::

[]{#document-tutorials/variables}

::::::::::::::::::::::::::::::::::::: {#variables .section}
### Variables[](#variables "Link to this heading"){.headerlink}

In the previous tutorial we learned how to define a simple string
variable, write it, and read it back.

In this tutorial we will go two steps further:

1.  We will define variables which include arrays, and we will write
    them and read them back.

2.  We will use MPI to write and read the above variables in parallel.

Let's start with the writing part.

Start editing the skeleton file
[ADIOS2/examples/hello/bpWriter/bpWriter_tutorialSkeleton.cpp](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/bpWriter/bpWriter_tutorialSkeleton.cpp){.reference
.external}.

1.  In an MPI application first we need to always initialize MPI. We do
    that with the following lines:

:::: {.highlight-cpp .notranslate}
::: highlight
    int rank, size;
    int provided;

    // MPI_THREAD_MULTIPLE is only required if you enable the SST MPI_DP
    MPI_Init_thread(&argc, &argv, MPI_THREAD_MULTIPLE, &provided);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
:::
::::

2.  Now we need to create some application variables which will be used
    to define ADIOS2 variables.

:::: {.highlight-cpp .notranslate}
::: highlight
    // Application variable
    std::vector<float> myFloats = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::vector<int> myInts = {0, -1, -2, -3, -4, -5, -6, -7, -8, -9};
    const std::size_t Nx = myFloats.size();
    const std::string myString("Hello Variable String from rank " + std::to_string(rank));
:::
::::

3.  Now we need to define an ADIOS2 instance and the ADIOS2 variables.

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::ADIOS adios(MPI_COMM_WORLD);
    adios2::IO bpIO = adios.DeclareIO("BPFile_N2N");

    adios2::Variable<float> bpFloats = bpIO.DefineVariable<float>(
        "bpFloats", {size * Nx}, {rank * Nx}, {Nx}, adios2::ConstantDims);

    adios2::Variable<int> bpInts = bpIO.DefineVariable<int>("bpInts", {size * Nx}, {rank * Nx},
                                                            {Nx}, adios2::ConstantDims);

    // For the sake of the tutorial we create an unused variable
    adios2::Variable<std::string> bpString = bpIO.DefineVariable<std::string>("bpString");
:::
::::

::: {.admonition .note}
Note

The above int/float variables are global arrays. The 1st argument of the
[`DefineVariable`{.docutils .literal .notranslate}]{.pre} function is
the variable name, the 2nd are the global dimensions, the 3rd is the
start index for a rank, the 4th are the rank/local dimensions, and the
5th is a boolean variable to indicate if the dimensions are constant or
not over multiple steps, where [`adios2::ConstantDims`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`==`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`true`{.docutils .literal .notranslate}]{.pre} We
will explore other tutorials that don't use constant dimensions.
:::

4.  Now we need to open the ADIOS2 engine and write the variables.

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::Engine bpWriter = bpIO.Open("myVector_cpp.bp", adios2::Mode::Write);

    bpWriter.BeginStep();
    bpWriter.Put(bpFloats, myFloats.data());
    bpWriter.Put(bpInts, myInts.data());
    // bpWriter.Put(bpString, myString);
    bpWriter.EndStep();

    bpWriter.Close();
:::
::::

5.  Finally we need to finalize MPI.

:::: {.highlight-cpp .notranslate}
::: highlight
    MPI_Finalize();
:::
::::

6.  The final code should look as follows (excluding try/catch and the
    optional usage of MPI), and it was derived from the example
    [ADIOS2/examples/hello/bpWriter/bpWriter.cpp](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/bpWriter/bpWriter.cpp){.reference
    .external}.

:::: {.highlight-cpp .notranslate}
::: highlight
    /*
     * Distributed under the OSI-approved Apache License, Version 2.0.  See
     * accompanying file Copyright.txt for details.
     *
     * bpWriter.cpp: Simple self-descriptive example of how to write a variable
     * to a BP File that lives in several MPI processes.
     *
     *  Created on: Feb 16, 2017
     *      Author: William F Godoy godoywf@ornl.gov
     */

    #include <ios>       //std::ios_base::failure
    #include <iostream>  //std::cout
    #include <stdexcept> //std::invalid_argument std::exception
    #include <vector>

    #include <adios2.h>
    #if ADIOS2_USE_MPI
    #include <mpi.h>
    #endif

    int main(int argc, char *argv[])
    {
        int rank, size;
    #if ADIOS2_USE_MPI
        int provided;

        // MPI_THREAD_MULTIPLE is only required if you enable the SST MPI_DP
        MPI_Init_thread(&argc, &argv, MPI_THREAD_MULTIPLE, &provided);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        MPI_Comm_size(MPI_COMM_WORLD, &size);
    #else
        rank = 0;
        size = 1;
    #endif

        /** Application variable */
        std::vector<float> myFloats = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        std::vector<int> myInts = {0, -1, -2, -3, -4, -5, -6, -7, -8, -9};
        const std::size_t Nx = myFloats.size();

        const std::string myString("Hello Variable String from rank " + std::to_string(rank));

        try
        {
            /** ADIOS class factory of IO class objects */
    #if ADIOS2_USE_MPI
            adios2::ADIOS adios(MPI_COMM_WORLD);
    #else
            adios2::ADIOS adios;
    #endif

            /*** IO class object: settings and factory of Settings: Variables,
             * Parameters, Transports, and Execution: Engines */
            adios2::IO bpIO = adios.DeclareIO("BPFile_N2N");

            /** global array : name, { shape (total) }, { start (local) }, {
             * count
             * (local) }, all are constant dimensions */
            adios2::Variable<float> bpFloats = bpIO.DefineVariable<float>(
                "bpFloats", {size * Nx}, {rank * Nx}, {Nx}, adios2::ConstantDims);

            adios2::Variable<int> bpInts = bpIO.DefineVariable<int>("bpInts", {size * Nx}, {rank * Nx},
                                                                    {Nx}, adios2::ConstantDims);

            adios2::Variable<std::string> bpString = bpIO.DefineVariable<std::string>("bpString");
            (void)bpString; // For the sake of the example we create an unused
                            // variable

            std::string filename = "myVector_cpp.bp";
            /** Engine derived class, spawned to start IO operations */
            adios2::Engine bpWriter = bpIO.Open(filename, adios2::Mode::Write);

            bpWriter.BeginStep();
            /** Put variables for buffering, template type is optional */
            bpWriter.Put(bpFloats, myFloats.data());
            bpWriter.Put(bpInts, myInts.data());
            // bpWriter.Put(bpString, myString);
            bpWriter.EndStep();

            /** Create bp file, engine becomes unreachable after this*/
            bpWriter.Close();
            if (rank == 0)
            {
                std::cout << "Wrote file " << filename
                          << " to disk. It can now be read by running "
                             "./bin/adios2_hello_bpReader.\n";
            }
        }
        catch (std::invalid_argument &e)
        {
            std::cerr << "Invalid argument exception: " << e.what() << "\n";
    #if ADIOS2_USE_MPI
            std::cerr << "STOPPING PROGRAM from rank " << rank << "\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
    #endif
        }
        catch (std::ios_base::failure &e)
        {
            std::cerr << "IO System base failure exception: " << e.what() << "\n";
    #if ADIOS2_USE_MPI
            std::cerr << "STOPPING PROGRAM from rank " << rank << "\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
    #endif
        }
        catch (std::exception &e)
        {
            std::cerr << "Exception: " << e.what() << "\n";
    #if ADIOS2_USE_MPI
            std::cerr << "STOPPING PROGRAM from rank " << rank << "\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
    #endif
        }

    #if ADIOS2_USE_MPI
        MPI_Finalize();
    #endif

        return 0;
    }
:::
::::

7.  You can compile and run it as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    cd Path-To-ADIOS2/examples/hello/bpWriter
    mkdir build
    cd build
    cmake -DADIOS2_DIR=Path-To-ADIOS2/build/ ..
    cmake --build .
    mpirun -np 2 ./adios2_hello_bpWriter_mpi
:::
::::

8.  You can check the content of the output file "myVector_cpp.bp" using
    *bpls* as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    Path-To-ADIOS2/build/bin/bpls ./myVector_cpp.bp

      float    bpFloats  {10}
      int32_t  bpInts    {10}
:::
::::

Now let's move to the reading part.

Start editing the skeleton file
[ADIOS2/examples/hello/bpReader/bpReader_tutorialSkeleton.cpp](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/bpReader/bpReader_tutorialSkeleton.cpp){.reference
.external}.

9.  In an MPI application first we need to always initialize MPI. We do
    that with the following line:

:::: {.highlight-cpp .notranslate}
::: highlight
    int rank, size;
    int provided;

    // MPI_THREAD_MULTIPLE is only required if you enable the SST MPI_DP
    MPI_Init_thread(&argc, &argv, MPI_THREAD_MULTIPLE, &provided);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
:::
::::

10. Now we need to define an ADIOS2 instance and open the ADIOS2 engine.

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::ADIOS adios(MPI_COMM_WORLD);

    adios2::IO bpIO = adios.DeclareIO("BPFile_N2N");

    adios2::Engine bpReader = bpIO.Open("myVector_cpp.bp", adios2::Mode::Read);
:::
::::

11. Now we need to read the variables. In this case we know the
    variables that we need to inquire, so we can use the
    [`InquireVariable`{.docutils .literal .notranslate}]{.pre} function
    immediately. But let's explore how to check the available variables
    in a file first, and then we will use the
    [`InquireVariable`{.docutils .literal .notranslate}]{.pre} function.

:::: {.highlight-cpp .notranslate}
::: highlight
    bpReader.BeginStep();
    const std::map<std::string, adios2::Params> variables = bpIO.AvailableVariables();

    for (const auto &variablePair : variables)
    {
        std::cout << "Name: " << variablePair.first;
        for (const auto &parameter : variablePair.second)
        {
            std::cout << "\t" << parameter.first << ": " << parameter.second << "\n";
        }
    }

    adios2::Variable<float> bpFloats = bpIO.InquireVariable<float>("bpFloats");
    adios2::Variable<int> bpInts = bpIO.InquireVariable<int>("bpInts");
:::
::::

12. Now we need to read the variables from each rank. We will use the
    [`SetSelection`{.docutils .literal .notranslate}]{.pre} to set the
    start index and rank dimensions, then [`Get`{.docutils .literal
    .notranslate}]{.pre} function to read the variables, and print the
    contents from rank 0.

:::: {.highlight-cpp .notranslate}
::: highlight
    const std::size_t Nx = 10;
    if (bpFloats) // means found
    {
       std::vector<float> myFloats;

       // read only the chunk corresponding to our rank
       bpFloats.SetSelection({{Nx * rank}, {Nx}});
       bpReader.Get(bpFloats, myFloats, adios2::Mode::Sync);

       if (rank == 0)
       {
           std::cout << "MyFloats: \n";
           for (const auto number : myFloats)
           {
               std::cout << number << " ";
           }
           std::cout << "\n";
       }
    }

    if (bpInts) // means not found
    {
       std::vector<int> myInts;
       // read only the chunk corresponding to our rank
       bpInts.SetSelection({{Nx * rank}, {Nx}});

       bpReader.Get(bpInts, myInts, adios2::Mode::Sync);

       if (rank == 0)
       {
           std::cout << "myInts: \n";
           for (const auto number : myInts)
           {
               std::cout << number << " ";
           }
           std::cout << "\n";
       }
    }
:::
::::

::: {.admonition .note}
Note

While using the [`Get`{.docutils .literal .notranslate}]{.pre} function,
we used the third parameter named [`Mode`{.docutils .literal
.notranslate}]{.pre}. The mode parameter can also be used for the
[`Put`{.docutils .literal .notranslate}]{.pre} function.

For the [`Put`{.docutils .literal .notranslate}]{.pre} function, there
are three modes: [`Deferred`{.docutils .literal .notranslate}]{.pre}
(default), [`Sync`{.docutils .literal .notranslate}]{.pre}, and
[`Span`{.docutils .literal .notranslate}]{.pre}. and for the
[`Get`{.docutils .literal .notranslate}]{.pre} there are two modes:
[`Deferred`{.docutils .literal .notranslate}]{.pre} (default) and
[`Sync`{.docutils .literal .notranslate}]{.pre}.

1.  The [`Deferred`{.docutils .literal .notranslate}]{.pre} mode is the
    default mode, because it is the fastest mode, as it allows
    [`Put`{.docutils .literal .notranslate}]{.pre} / [`Get`{.docutils
    .literal .notranslate}]{.pre} to be grouped before potential data
    transport at the first encounter of [`PerformPuts`{.docutils
    .literal .notranslate}]{.pre} / [`PerformGets`{.docutils .literal
    .notranslate}]{.pre}, [`EndStep`{.docutils .literal
    .notranslate}]{.pre} or [`Close`{.docutils .literal
    .notranslate}]{.pre}.

2.  The [`Sync`{.docutils .literal .notranslate}]{.pre} mode forces
    [`Put`{.docutils .literal .notranslate}]{.pre} / [`Get`{.docutils
    .literal .notranslate}]{.pre} to be performed immediately so that
    the data are available immediately.

3.  The [`Span`{.docutils .literal .notranslate}]{.pre} mode is special
    mode of [`Deferred`{.docutils .literal .notranslate}]{.pre} that
    allows population from non-contiguous memory structures.

For more information about the [`Mode`{.docutils .literal
.notranslate}]{.pre} parameter for both [`Put`{.docutils .literal
.notranslate}]{.pre} and [`Get`{.docutils .literal .notranslate}]{.pre}
functions, and when you should use each option see [[Basics: Interface
Components: Engine]{.std
.std-ref}](#document-components/components#sec-basics-interface-components-engine){.reference
.internal}.
:::

13. Now we need close the ADIOS2 engine.

:::: {.highlight-cpp .notranslate}
::: highlight
    bpReader.EndStep();
    bpReader.Close();
:::
::::

14. Finally we need to finalize MPI.

:::: {.highlight-cpp .notranslate}
::: highlight
    MPI_Finalize();
:::
::::

15. The final code should look as follows (excluding try/catch), and it
    was derived from the example
    [ADIOS2/examples/hello/bpWriter/bpWriter.cpp](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/bpWriter/bpWriter.cpp){.reference
    .external}.

:::: {.highlight-cpp .notranslate}
::: highlight
    /*
     * Distributed under the OSI-approved Apache License, Version 2.0.  See
     * accompanying file Copyright.txt for details.
     *
     * bpReader.cpp: Simple self-descriptive example of how to read a variable
     * from a BP File.
     *
     *  Created on: Feb 16, 2017
     *      Author: William F Godoy godoywf@ornl.gov
     */
    #include <ios>      //std::ios_base::failure
    #include <iostream> //std::cout
    #if ADIOS2_USE_MPI
    #include <mpi.h>
    #endif
    #include <stdexcept> //std::invalid_argument std::exception
    #include <vector>

    #include <adios2.h>

    int main(int argc, char *argv[])
    {
        int rank, size;

    #if ADIOS2_USE_MPI
        int provided;
        // MPI_THREAD_MULTIPLE is only required if you enable the SST MPI_DP
        MPI_Init_thread(&argc, &argv, MPI_THREAD_MULTIPLE, &provided);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        MPI_Comm_size(MPI_COMM_WORLD, &size);
    #else
        rank = 0;
        size = 1;
    #endif
        std::cout << "rank " << rank << " size " << size << "\n";
        try
        {
    #if ADIOS2_USE_MPI
            /** ADIOS class factory of IO class objects */
            adios2::ADIOS adios(MPI_COMM_WORLD);
    #else
            adios2::ADIOS adios;
    #endif

            /*** IO class object: settings and factory of Settings: Variables,
             * Parameters, Transports, and Execution: Engines */
            adios2::IO bpIO = adios.DeclareIO("BPFile_N2N");

            /** Engine derived class, spawned to start IO operations */
            adios2::Engine bpReader = bpIO.Open("myVector_cpp.bp", adios2::Mode::Read);

            bpReader.BeginStep();
            const std::map<std::string, adios2::Params> variables = bpIO.AvailableVariables();

            for (const auto &variablePair : variables)
            {
                std::cout << "Name: " << variablePair.first;

                for (const auto &parameter : variablePair.second)
                {
                    std::cout << "\t" << parameter.first << ": " << parameter.second << "\n";
                }
            }

            /** Write variable for buffering */
            adios2::Variable<float> bpFloats = bpIO.InquireVariable<float>("bpFloats");
            adios2::Variable<int> bpInts = bpIO.InquireVariable<int>("bpInts");

            const std::size_t Nx = 10;
            if (bpFloats) // means found
            {
                std::vector<float> myFloats;

                // read only the chunk corresponding to our rank
                bpFloats.SetSelection({{Nx * rank}, {Nx}});
                // myFloats.data is pre-allocated
                bpReader.Get(bpFloats, myFloats, adios2::Mode::Sync);

                if (rank == 0)
                {
                    std::cout << "MyFloats: \n";
                    for (const auto number : myFloats)
                    {
                        std::cout << number << " ";
                    }
                    std::cout << "\n";
                }
            }

            if (bpInts) // means not found
            {
                std::vector<int> myInts;
                // read only the chunk corresponding to our rank
                bpInts.SetSelection({{Nx * rank}, {Nx}});

                bpReader.Get(bpInts, myInts, adios2::Mode::Sync);

                if (rank == 0)
                {
                    std::cout << "myInts: \n";
                    for (const auto number : myInts)
                    {
                        std::cout << number << " ";
                    }
                    std::cout << "\n";
                }
            }
            bpReader.EndStep();

            /** Close bp file, engine becomes unreachable after this*/
            bpReader.Close();
        }
        catch (std::invalid_argument &e)
        {
            if (rank == 0)
            {
                std::cerr << "Invalid argument exception, STOPPING PROGRAM from rank " << rank << "\n";
                std::cerr << e.what() << "\n";
            }
    #if ADIOS2_USE_MPI
            MPI_Abort(MPI_COMM_WORLD, 1);
    #endif
        }
        catch (std::ios_base::failure &e)
        {
            if (rank == 0)
            {
                std::cerr << "IO System base failure exception, STOPPING PROGRAM "
                             "from rank "
                          << rank << "\n";
                std::cerr << e.what() << "\n";
                std::cerr << "The file myVector_cpp.bp does not exist."
                          << " Presumably this is because adios2_hello_bpWriter has not "
                             "been run."
                          << " Run ./adios2_hello_bpWriter before running this program.\n";
            }
    #if ADIOS2_USE_MPI
            MPI_Abort(MPI_COMM_WORLD, 1);
    #endif
        }
        catch (std::exception &e)
        {
            if (rank == 0)
            {
                std::cerr << "Exception, STOPPING PROGRAM from rank " << rank << "\n";
                std::cerr << e.what() << "\n";
            }
    #if ADIOS2_USE_MPI
            MPI_Abort(MPI_COMM_WORLD, 1);
    #endif
        }

    #if ADIOS2_USE_MPI
        MPI_Finalize();
    #endif

        return 0;
    }
:::
::::

16. You can compile and run it as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    cd Path-To-ADIOS2/examples/hello/bpReader
    mkdir build
    cd build
    cmake -DADIOS2_DIR=Path-To-ADIOS2/build/ ..
    cmake --build .
    mpirun -np 2 ./adios2_hello_bpReader_mpi
:::
::::
:::::::::::::::::::::::::::::::::::::

[]{#document-tutorials/attributes}

:::::::::::::::::::::::::::::::::::::::::::: {#attributes .section}
### Attributes[](#attributes "Link to this heading"){.headerlink}

In the previous tutorial, we learned how to write/read variables.

In this tutorial, we will explore how to write/read attributes.
Attributes are metadata related to the whole dataset or to a specific
variable. In this tutorial, we will only focus on attributes related to
the whole dataset, but we will explain how variable's attributes can be
used too.

Start editing the skeleton file
[ADIOS2/examples/hello/bpAttributeWriteRead/bpAttributeWriteRead_tutorialSkeleton.cpp](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/bpAttributeWriteRead/bpAttributeWriteRead_tutorialSkeleton.cpp){.reference
.external}.

1.  In an MPI application first we need to always initialize MPI. We do
    that with the following lines:

:::: {.highlight-cpp .notranslate}
::: highlight
    int rank, size;
    int provided;

    // MPI_THREAD_MULTIPLE is only required if you enable the SST MPI_DP
    MPI_Init_thread(&argc, &argv, MPI_THREAD_MULTIPLE, &provided);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
:::
::::

2.  Now we need to create a application variable which will be used to
    define an ADIOS2 variable.

:::: {.highlight-cpp .notranslate}
::: highlight
    std::vector<float> myFloats = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
:::
::::

3.  Then, we need to create an ADIOS2 instance.

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::ADIOS adios(MPI_COMM_WORLD);
:::
::::

4.  Then, we create the following writer function:

:::: {.highlight-cpp .notranslate}
::: highlight
    void writer(adios2::ADIOS &adios, int rank, int size, std::vector<float> &myFloats)
    {
       ...
    }
:::
::::

5.  In this writer function, we define an IO object, and a float vector
    variable as follows:

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::IO bpIO = adios.DeclareIO("BPFile_N2N");

    const std::size_t Nx = myFloats.size();
    adios2::Variable<float> bpFloats = bpIO.DefineVariable<float>(
      "bpFloats", {size * Nx}, {rank * Nx}, {Nx}, adios2::ConstantDims);
:::
::::

6.  Now, we will define various types of attributes as follows:

:::: {.highlight-cpp .notranslate}
::: highlight
    bpIO.DefineAttribute<std::string>("Single_String", "File generated with ADIOS2");

    std::vector<std::string> myStrings = {"one", "two", "three"};
    bpIO.DefineAttribute<std::string>("Array_of_Strings", myStrings.data(), myStrings.size());

    bpIO.DefineAttribute<double>("Attr_Double", 0.f);
    std::vector<double> myDoubles = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    bpIO.DefineAttribute<double>("Array_of_Doubles", myDoubles.data(), myDoubles.size());
:::
::::

::::: {.admonition .note}
Note

if we want to define an attribute for a specific variable, we can use
one of the following API:

:::: {.highlight-cpp .notranslate}
::: highlight
    template <class T>
    Attribute<T> DefineAttribute(const std::string &name, const T *data, const size_t size,
                                 const std::string &variableName = "", const std::string separator = "/",
                                 const bool allowModification = false);

    template <class T>
    Attribute<T> DefineAttribute(const std::string &name, const T &value,
                                 const std::string &variableName = "", const std::string separator = "/",
                                 const bool allowModification = false);
:::
::::

As we can see, by default the attributes don't change over multiple
steps, but we can change that by setting [`allowModification`{.docutils
.literal .notranslate}]{.pre} to [`true`{.docutils .literal
.notranslate}]{.pre}.
:::::

7.  Then, we open a file for writing:

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::Engine bpWriter = bpIO.Open("fileAttributes.bp", adios2::Mode::Write);
:::
::::

8.  Now, we write the data and close the file:

:::: {.highlight-cpp .notranslate}
::: highlight
    bpWriter.BeginStep();
    bpWriter.Put<float>(bpFloats, myFloats.data());
    bpWriter.EndStep();
    bpWriter.Close();
:::
::::

9.  Steps 1-8 are used for writing, we will define a reader function in
    the rest of the steps:

:::: {.highlight-cpp .notranslate}
::: highlight
    void reader(adios2::ADIOS &adios, int rank, int size)
    {
       ...
    }
:::
::::

10. In this reader function, we define an IO object, and open the file
    for reading:

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::IO bpIO = adios.DeclareIO("BPFile_N2N");
    adios2::Engine bpReader = bpIO.Open("fileAttributes.bp", adios2::Mode::Read);
:::
::::

11. Now, we check the available attributes as follows:

:::: {.highlight-cpp .notranslate}
::: highlight
    bpReader.BeginStep();
    const auto attributesInfo = bpIO.AvailableAttributes();

    for (const auto &attributeInfoPair : attributesInfo)
    {
      std::cout << "Attribute: " << attributeInfoPair.first;
      for (const auto &attributePair : attributeInfoPair.second)
      {
          std::cout << "\tKey: " << attributePair.first << "\tValue: " << attributePair.second
                    << "\n";
      }
      std::cout << "\n";
    }
:::
::::

12. Now we will inquire and get the attributes as follows:

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::Attribute<float> singleString = bpIO.InquireAttribute<float>("Single_String");
    if (singleString)
    {
        std::cout << singleString.Name() << ": " << singleString.Data()[0] << "\n";
    }
    adios2::Attribute<std::string> arrayOfStrings =
        bpIO.InquireAttribute<std::string>("Array_of_Strings");
    if (arrayOfStrings)
    {
        std::cout << arrayOfStrings.Name() << ": ";
        for (const auto &value : arrayOfStrings.Data())
        {
            std::cout << value << " ";
        }
        std::cout << "\n";
    }
    adios2::Attribute<double> attrDouble = bpIO.InquireAttribute<double>("Attr_Double");
    if (attrDouble)
    {
        std::cout << attrDouble.Name() << ": " << attrDouble.Data()[0] << "\n";
    }
    adios2::Attribute<double> arrayOfDoubles = bpIO.InquireAttribute<double>("Array_of_Doubles");
    if (arrayOfDoubles)
    {
        std::cout << arrayOfDoubles.Name() << ": ";
        for (const auto &value : arrayOfDoubles.Data())
        {
            std::cout << value << " ";
        }
        std::cout << "\n";
    }
:::
::::

13. Afterward, we will inquire and get the variable as follows:

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::Variable<float> bpFloats = bpIO.InquireVariable<float>("bpFloats");
    const std::size_t Nx = 10;
    std::vector<float> myFloats(Nx);
    if (bpFloats)
    {
        bpFloats.SetSelection({{Nx * rank}, {Nx}});
        bpReader.Get(bpFloats, myFloats.data());
    }
    bpReader.EndStep();
:::
::::

14. Finally, we close the file:

:::: {.highlight-cpp .notranslate}
::: highlight
    bpReader.Close();
:::
::::

15. In the main function, we call the writer and reader functions as
    follows:

:::: {.highlight-cpp .notranslate}
::: highlight
    writer(adios, rank, size, myFloats);
    reader(adios, rank, size);
:::
::::

16. Finally, we finalize MPI:

:::: {.highlight-cpp .notranslate}
::: highlight
    MPI_Finalize();
:::
::::

17. The final code should look as follows (excluding try/catch and
    optional usage MPI), and it was derived from the example
    [ADIOS2/examples/hello/bpAttributeWriteRead/bpAttributeWriteRead.cpp](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/bpAttributeWriteRead/bpAttributeWriteRead.cpp){.reference
    .external}.

:::: {.highlight-cpp .notranslate}
::: highlight
    /*
     * Distributed under the OSI-approved Apache License, Version 2.0.  See
     * accompanying file Copyright.txt for details.
     *
     * bpAttributeWriteRead.cpp: Simple self-descriptive example of how to write/read attributes and
     * a variable to a BP File that lives in several MPI processes.
     *
     *  Created on: Feb 16, 2017
     *      Author: William F Godoy godoywf@ornl.gov
     */

    #include <ios>      //std::ios_base::failure
    #include <iostream> //std::cout
    #if ADIOS2_USE_MPI
    #include <mpi.h>
    #endif
    #include <stdexcept> //std::invalid_argument std::exception
    #include <string>
    #include <vector>

    #include <adios2.h>

    void writer(adios2::ADIOS &adios, int rank, int size, std::vector<float> &myFloats)
    {
        /*** IO class object: settings and factory of Settings: Variables,
         * Parameters, Transports, and Execution: Engines */
        adios2::IO bpIO = adios.DeclareIO("BPFile_N2N");

        const std::size_t Nx = myFloats.size();

        /** global array : name, { shape (total) }, { start (local) }, { count
         * (local) }, all are constant dimensions */
        adios2::Variable<float> bpFloats = bpIO.DefineVariable<float>(
            "bpFloats", {size * Nx}, {rank * Nx}, {Nx}, adios2::ConstantDims);

        bpIO.DefineAttribute<std::string>("Single_String", "File generated with ADIOS2");

        std::vector<std::string> myStrings = {"one", "two", "three"};
        bpIO.DefineAttribute<std::string>("Array_of_Strings", myStrings.data(), myStrings.size());

        bpIO.DefineAttribute<double>("Attr_Double", 0.f);
        std::vector<double> myDoubles = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        bpIO.DefineAttribute<double>("Array_of_Doubles", myDoubles.data(), myDoubles.size());

        /** Engine derived class, spawned to start IO operations */
        adios2::Engine bpWriter = bpIO.Open("fileAttributes.bp", adios2::Mode::Write);

        bpWriter.BeginStep();

        /** Write variable for buffering */
        bpWriter.Put<float>(bpFloats, myFloats.data());

        bpWriter.EndStep();

        /** Create bp file, engine becomes unreachable after this*/
        bpWriter.Close();
    }

    void reader(adios2::ADIOS &adios, int rank, int /*size*/)
    {
        adios2::IO bpIO = adios.DeclareIO("BPReader");

        adios2::Engine bpReader = bpIO.Open("fileAttributes.bp", adios2::Mode::Read);

        bpReader.BeginStep();
        const auto attributesInfo = bpIO.AvailableAttributes();

        for (const auto &attributeInfoPair : attributesInfo)
        {
            std::cout << "Attribute: " << attributeInfoPair.first;
            for (const auto &attributePair : attributeInfoPair.second)
            {
                std::cout << "\tKey: " << attributePair.first << "\tValue: " << attributePair.second
                          << "\n";
            }
            std::cout << "\n";
        }

        adios2::Attribute<float> singleString = bpIO.InquireAttribute<float>("Single_String");
        if (singleString)
        {
            std::cout << singleString.Name() << ": " << singleString.Data()[0] << "\n";
        }
        adios2::Attribute<std::string> arrayOfStrings =
            bpIO.InquireAttribute<std::string>("Array_of_Strings");
        if (arrayOfStrings)
        {
            std::cout << arrayOfStrings.Name() << ": ";
            for (const auto &value : arrayOfStrings.Data())
            {
                std::cout << value << " ";
            }
            std::cout << "\n";
        }
        adios2::Attribute<double> attrDouble = bpIO.InquireAttribute<double>("Attr_Double");
        if (attrDouble)
        {
            std::cout << attrDouble.Name() << ": " << attrDouble.Data()[0] << "\n";
        }
        adios2::Attribute<double> arrayOfDoubles = bpIO.InquireAttribute<double>("Array_of_Doubles");
        if (arrayOfDoubles)
        {
            std::cout << arrayOfDoubles.Name() << ": ";
            for (const auto &value : arrayOfDoubles.Data())
            {
                std::cout << value << " ";
            }
            std::cout << "\n";
        }

        adios2::Variable<float> bpFloats = bpIO.InquireVariable<float>("bpFloats");
        const std::size_t Nx = 10;
        std::vector<float> myFloats(Nx);
        if (bpFloats)
        {
            bpFloats.SetSelection({{Nx * rank}, {Nx}});
            bpReader.Get(bpFloats, myFloats.data());
        }

        bpReader.EndStep();

        bpReader.Close();
    }

    int main(int argc, char *argv[])
    {
        int rank, size;
    #if ADIOS2_USE_MPI
        int provided;

        // MPI_THREAD_MULTIPLE is only required if you enable the SST MPI_DP
        MPI_Init_thread(&argc, &argv, MPI_THREAD_MULTIPLE, &provided);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        MPI_Comm_size(MPI_COMM_WORLD, &size);
    #else
        rank = 0;
        size = 1;
    #endif

        /** Application variable */
        std::vector<float> myFloats = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        try
        {
            /** ADIOS class factory of IO class objects */
    #if ADIOS2_USE_MPI
            adios2::ADIOS adios(MPI_COMM_WORLD);
    #else
            adios2::ADIOS adios;
    #endif

            writer(adios, rank, size, myFloats);
            reader(adios, rank, size);
        }
        catch (std::invalid_argument &e)
        {
            std::cout << "Invalid argument exception, STOPPING PROGRAM from rank " << rank << "\n";
            std::cout << e.what() << "\n";
    #if ADIOS2_USE_MPI
            std::cerr << "STOPPING PROGRAM from rank " << rank << "\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
    #endif
        }
        catch (std::ios_base::failure &e)
        {
            std::cout << "IO System base failure exception, STOPPING PROGRAM from rank " << rank
                      << "\n";
            std::cout << e.what() << "\n";
    #if ADIOS2_USE_MPI
            std::cerr << "STOPPING PROGRAM from rank " << rank << "\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
    #endif
        }
        catch (std::exception &e)
        {
            std::cout << "Exception, STOPPING PROGRAM from rank " << rank << "\n";
            std::cout << e.what() << "\n";
    #if ADIOS2_USE_MPI
            std::cerr << "STOPPING PROGRAM from rank " << rank << "\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
    #endif
        }

    #if ADIOS2_USE_MPI
        MPI_Finalize();
    #endif

        return 0;
    }
:::
::::

18. You can compile and run it as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    cd Path-To-ADIOS2/examples/hello/bpAttributeWriteRead
    mkdir build
    cd build
    cmake -DADIOS2_DIR=Path-To-ADIOS2/build/ ..
    cmake --build .
    mpirun -np 2 ./adios2_hello_bpAttributeWriteRead_mpi
:::
::::

19. You can check the content of the output file "fileAttributes.bp"
    using *bpls* as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    Path-To-ADIOS2/build/bin/bpls ./fileAttributes.bp

      float    bpFloats  {20}
:::
::::
::::::::::::::::::::::::::::::::::::::::::::

[]{#document-tutorials/operators}

:::::::::::::::::::::::::::::::::: {#operators .section}
### Operators[](#operators "Link to this heading"){.headerlink}

In the previous tutorial we learned how to write and read attributes.

For this example to work, you would need to have the SZ compression
library installed, which ADIOS automatically detects. The easiest way to
install SZ is with Spack, and you can do that as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    git clone https://github.com/spack/spack.git ~/spack
    cd ~/spack
    . share/spack/setup-env.sh
    spack install sz
    spack load sz
:::
::::

In this tutorial we will learn how to use operators. Operators are used
for Data compression/decompression, lossy and lossless. They act upon
the user application data, either from a variable or a set of variables
in a IO object.

Additionally, we will explore how to simply write variables across
multiple steps.

So, let's dig in!

Start editing the skeleton file
[ADIOS2/examples/hello/bpOperatorSZWriter/bpOperatorSZWriter_tutorialSkeleton.cpp](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/bpOperatorSZWriter/bpOperatorSZWriter_tutorialSkeleton.cpp){.reference
.external}.

1.  In an MPI application first we need to always initialize MPI. We do
    that with the following lines:

:::: {.highlight-cpp .notranslate}
::: highlight
    int rank, size;
    int rank, size;
    int provided;

    // MPI_THREAD_MULTIPLE is only required if you enable the SST MPI_DP
    MPI_Init_thread(&argc, &argv, MPI_THREAD_MULTIPLE, &provided);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
:::
::::

2.  This application has command line arguments for the size of the
    data, and the compression accuracy, which we can read as follows:

:::: {.highlight-cpp .notranslate}
::: highlight
    const std::size_t Nx = static_cast<std::size_t>(std::stoull(argv[1]));
    const double accuracy = std::stod(argv[2]);
:::
::::

3.  Now we need to create some application variables which will be used
    to define ADIOS2 variables.

:::: {.highlight-cpp .notranslate}
::: highlight
    std::vector<float> myFloats(Nx);
    std::vector<double> myDoubles(Nx);
    std::iota(myFloats.begin(), myFloats.end(), 0.);
    std::iota(myDoubles.begin(), myDoubles.end(), 0.);
:::
::::

4.  Now we need to create an ADIOS2 instance and IO object.

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::ADIOS adios(MPI_COMM_WORLD);
    adios2::IO bpIO = adios.DeclareIO("BPFile_SZ");
:::
::::

5.  Now we need to define the variables we want to write.

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::Variable<float> bpFloats = bpIO.DefineVariable<float>(
        "bpFloats", {size * Nx}, {rank * Nx}, {Nx}, adios2::ConstantDims);
    adios2::Variable<double> bpDoubles = bpIO.DefineVariable<double>(
        "bpDoubles", {size * Nx}, {rank * Nx}, {Nx}, adios2::ConstantDims);
:::
::::

6.  Now we need to define the compression operator we want to use. In
    this case we will use the SZ compressor.

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::Operator op = bpIO.DefineOperator("SZCompressor", "sz");
    varFloats.AddOperation(op, {{"accuracy", std::to_string(accuracy)}});
    varDoubles.AddOperation(op, {{"accuracy", std::to_string(accuracy)}});
:::
::::

::: {.admonition .note}
Note

[`DefineOperator()'`{.docutils .literal .notranslate}]{.pre} s second
parameter can be either zfp or sz. For more information regarding
operators and their properties you can look at [[Basics: Interface
Components: Operator]{.std
.std-ref}](#document-components/components#sec-basics-interface-components-operator){.reference
.internal}.
:::

7.  Let's also create an attribute to store the accuracy value.

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::Attribute<double> attribute = bpIO.DefineAttribute<double>("accuracy", accuracy);
:::
::::

8.  Now we need to open the file for writing.

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::Engine bpWriter = bpIO.Open("SZexample.bp", adios2::Mode::Write);
:::
::::

9.  Now we need to write the data. We will write the data for 3 steps,
    and edit them in between.

:::: {.highlight-cpp .notranslate}
::: highlight
    for (unsigned int step = 0; step < 3; ++step)
    {
        bpWriter.BeginStep();

        bpWriter.Put<double>(bpDoubles, myDoubles.data());
        bpWriter.Put<float>(bpFloats, myFloats.data());

        bpWriter.EndStep();

        // here you can modify myFloats, myDoubles per step
        std::transform(myFloats.begin(), myFloats.end(), myFloats.begin(),
                       [&](float v) -> float { return 2 * v; });
        std::transform(myDoubles.begin(), myDoubles.end(), myDoubles.begin(),
                       [&](double v) -> double { return 3 * v; });
    }
:::
::::

10. Now we need to close the file.

:::: {.highlight-cpp .notranslate}
::: highlight
    bpWriter.Close();
:::
::::

11. Finally we need to finalize MPI.

:::: {.highlight-cpp .notranslate}
::: highlight
    MPI_Finalize();
:::
::::

12. The final code should look as follows (excluding try/catch and
    optional usage of MPI), and it was derived from the example
    [ADIOS2/examples/hello/bpOperatorSZWriter/bpOperatorSZWriter.cpp](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/bpOperatorSZWriter/bpOperatorSZWriter.cpp){.reference
    .external}.

:::: {.highlight-cpp .notranslate}
::: highlight
    /*
     * Distributed under the OSI-approved Apache License, Version 2.0.  See
     * accompanying file Copyright.txt for details.
     *
     * bpOperatorSZWriter.cpp : example using operator by passing compression arguments
     *
     *  Created on: Aug 3, 2018
     *      Author: William F Godoy godoywf@ornl.gov
     */

    #include <algorithm> //std::transform
    #include <ios>       //std::ios_base::failure
    #include <iostream>  //std::cout
    #include <numeric>   //std::iota
    #include <stdexcept> //std::invalid_argument std::exception
    #include <vector>

    #include "adios2.h"
    #if ADIOS2_USE_MPI
    #include <mpi.h>
    #endif

    void Usage()
    {
        std::cout << "\n";
        std::cout << "USAGE:\n";
        std::cout << "./adios2_hello_bpOperatorSZWriter Nx sz_accuracy\n";
        std::cout << "\t Nx: size of float and double arrays to be compressed\n";
        std::cout << "\t sz_accuracy: absolute accuracy e.g. 0.1, 0.001, to skip "
                     "compression: -1\n\n";
    }

    int main(int argc, char *argv[])
    {
        if (argc != 3)
        {
            Usage();
            return EXIT_SUCCESS;
        }

        int rank, size;
    #if ADIOS2_USE_MPI
        int provided;

        // MPI_THREAD_MULTIPLE is only required if you enable the SST MPI_DP
        MPI_Init_thread(&argc, &argv, MPI_THREAD_MULTIPLE, &provided);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        MPI_Comm_size(MPI_COMM_WORLD, &size);
    #else
        rank = 0;
        size = 1;
    #endif

        try
        {
            const std::size_t Nx = static_cast<std::size_t>(std::stoull(argv[1]));
            const double accuracy = std::stod(argv[2]);

            /** Application variable */
            std::vector<float> myFloats(Nx);
            std::vector<double> myDoubles(Nx);
            std::iota(myFloats.begin(), myFloats.end(), 0.);
            std::iota(myDoubles.begin(), myDoubles.end(), 0.);

            /** ADIOS class factory of IO class objects */
    #if ADIOS2_USE_MPI
            adios2::ADIOS adios(MPI_COMM_WORLD);
    #else
            adios2::ADIOS adios;
    #endif

            /*** IO class object: settings and factory of Settings: Variables,
             * Parameters, Transports, and Execution: Engines */
            adios2::IO bpIO = adios.DeclareIO("BPFile_SZ");

            adios2::Variable<float> varFloats = bpIO.DefineVariable<float>(
                "bpFloats", {size * Nx}, {rank * Nx}, {Nx}, adios2::ConstantDims);

            adios2::Variable<double> varDoubles = bpIO.DefineVariable<double>(
                "bpDoubles", {size * Nx}, {rank * Nx}, {Nx}, adios2::ConstantDims);

            if (accuracy > 1E-16)
            {
                adios2::Operator op = adios.DefineOperator("SZCompressor", "sz");
                varFloats.AddOperation(op, {{"accuracy", std::to_string(accuracy)}});
                varDoubles.AddOperation(op, {{"accuracy", std::to_string(accuracy)}});
            }

            adios2::Attribute<double> attribute = bpIO.DefineAttribute<double>("SZ_accuracy", accuracy);

            // To avoid compiling warnings
            (void)attribute;

            /** Engine derived class, spawned to start IO operations */
            adios2::Engine bpWriter = bpIO.Open("SZexample.bp", adios2::Mode::Write);

            for (unsigned int step = 0; step < 3; ++step)
            {
                bpWriter.BeginStep();

                bpWriter.Put(varFloats, myFloats.data());
                bpWriter.Put(varDoubles, myDoubles.data());

                bpWriter.EndStep();

                // here you can modify myFloats, myDoubles per step
                std::transform(myFloats.begin(), myFloats.end(), myFloats.begin(),
                               [&](float v) -> float { return 2 * v; });
                std::transform(myDoubles.begin(), myDoubles.end(), myDoubles.begin(),
                               [&](double v) -> double { return 3 * v; });
            }

            /** Create bp file, engine becomes unreachable after this*/
            bpWriter.Close();
        }
        catch (std::invalid_argument &e)
        {
            std::cerr << "Invalid argument exception: " << e.what() << "\n";
    #if ADIOS2_USE_MPI
            std::cerr << "STOPPING PROGRAM from rank " << rank << "\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
    #endif
        }
        catch (std::ios_base::failure &e)
        {
            std::cerr << "IO System base failure exception: " << e.what() << "\n";
    #if ADIOS2_USE_MPI
            std::cerr << "STOPPING PROGRAM from rank " << rank << "\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
    #endif
        }
        catch (std::exception &e)
        {
            std::cerr << "Exception: " << e.what() << "\n";
    #if ADIOS2_USE_MPI
            std::cerr << "STOPPING PROGRAM from rank " << rank << "\n";
            MPI_Abort(MPI_COMM_WORLD, 1);
    #endif
        }

    #if ADIOS2_USE_MPI
        MPI_Finalize();
    #endif

        return 0;
    }
:::
::::

13. You can compile and run it as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    cd Path-To-ADIOS2/examples/hello/bpOperatorSZWriter
    mkdir build
    cd build
    cmake -DADIOS2_DIR=Path-To-ADIOS2/build/ ..
    cmake --build .
    mpirun -np 2 ./adios2_hello_bpOperatorSZWriter_mpi 20 0.000001
:::
::::

12. You can check the content of the output file "SZexample.bp" using
    *bpls* as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    Path-To-ADIOS2/build/bin/bpls ./SZexample.bp

      double   bpDoubles  3*{40}
      float    bpFloats   3*{40}
:::
::::
::::::::::::::::::::::::::::::::::

[]{#document-tutorials/steps}

:::::::::::::::::::::::::::::::::::::::::::::::: {#steps .section}
### Steps[](#steps "Link to this heading"){.headerlink}

In the previous tutorial, we introduced the concept of operators, and
briefly touched upon the concept of steps.

In this tutorial, we will explore how to write data for multiple steps,
and how to read them back.

So let's dig in!

Start editing the skeleton file
[ADIOS2/examples/hello/bpStepsWriteRead/bpStepsWriteRead_tutorialSkeleton.cpp](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/bpStepsWriteRead/bpStepsWriteRead_tutorialSkeleton.cpp){.reference
.external}.

1.  In an MPI application first we need to always initialize MPI. We do
    that with the following lines:

:::: {.highlight-cpp .notranslate}
::: highlight
    int rank, size;
    int rank, size;
    int provided;

    // MPI_THREAD_MULTIPLE is only required if you enable the SST MPI_DP
    MPI_Init_thread(&argc, &argv, MPI_THREAD_MULTIPLE, &provided);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
:::
::::

2.  This application has an optional command line argument for engine
    being used. If no argument is provided, the default engine is
    BPFile.

:::: {.highlight-cpp .notranslate}
::: highlight
    const std::string engine = argv[1] ? argv[1] : "BPFile";
:::
::::

3.  We will define the number of steps and the size of the data that we
    will create.

:::: {.highlight-cpp .notranslate}
::: highlight
    const std::string filename = engine + "StepsWriteRead.bp";
    const unsigned int nSteps = 10;
    const unsigned int Nx = 60000;
:::
::::

4.  Now we need to create an ADIOS2 instance.

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::ADIOS adios(MPI_COMM_WORLD);
:::
::::

5.  Now we will populate the writer function with the following
    signature:

:::: {.highlight-default .notranslate}
::: highlight
    void writer(adios2::ADIOS &adios, const std::string &engine, const std::string &fname,
              const size_t Nx, unsigned int nSteps, int rank, int size)
    {
      ...
    }
:::
::::

6.  Let's create some simulation data. We will create a 1D array of size
    Nx, and fill it with 0.block

:::: {.highlight-cpp .notranslate}
::: highlight
    std::vector<double> simData(Nx, 0.0);
:::
::::

7.  Now we will create an IO object and set the engine type.block

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::IO bpIO = adios.DeclareIO("SimulationOutput");
    io.SetEngine(engine);
:::
::::

::: {.admonition .note}
Note

The beauty of ADIOS2 is that you write the same code for all engines.
The only thing that changes is the engine name. The underlying engine
handles all the intricacies of the engine's format, and the user enjoys
the API's simplicity.
:::

8.  Now we will create a variable for the simulation data and the step.

:::: {.highlight-cpp .notranslate}
::: highlight
    const adios2::Dims shape{static_cast<size_t>(size * Nx)};
    const adios2::Dims start{static_cast<size_t>(rank * Nx)};
    const adios2::Dims count{Nx};
    auto bpFloats = bpIO.DefineVariable<float>("bpFloats", shape, start, count);

    auto bpStep = bpIO.DefineVariable<unsigned int>("bpStep");
:::
::::

9.  Now we will open the file for writing.

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::Engine bpWriter = bpIO.Open(fname, adios2::Mode::Write);
:::
::::

10. Now we will write the data for each step.

:::: {.highlight-cpp .notranslate}
::: highlight
    for (unsigned int step = 0; step < nSteps; ++step)
    {
        const adios2::Box<adios2::Dims> sel({0}, {Nx});
        bpFloats.SetSelection(sel);

        bpWriter.BeginStep();
        bpWriter.Put(bpFloats, simData.data());
        bpWriter.Put(bpStep, step);
        bpWriter.EndStep();

        // Update values in the simulation data
        update_array(simData, 10);
    }
:::
::::

11. Now we will close the file.

:::: {.highlight-cpp .notranslate}
::: highlight
    bpWriter.Close();
:::
::::

12. Now we will populate the reader function with the following
    signature:

:::: {.highlight-cpp .notranslate}
::: highlight
    void reader(adios2::ADIOS &adios, const std::string &engine, const std::string &fname,
                const size_t Nx, unsigned int /*nSteps*/, int rank, int /*size*/)
    {
      ...
    }
:::
::::

13. Now we will create an IO object and set the engine type.

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::IO bpIO = adios.DeclareIO("SimulationOutput");
    io.SetEngine(engine);
:::
::::

14. Now we will open the file for reading.

:::: {.highlight-cpp .notranslate}
::: highlight
    adios2::Engine bpReader = bpIO.Open(fname, adios2::Mode::Read);
:::
::::

15. Now we will create a vector to store simData and a variable for the
    step.

:::: {.highlight-cpp .notranslate}
::: highlight
    std::vector<float> simData(Nx, 0);
    unsigned int inStep = 0;
:::
::::

16. Now we will read the data for each step.

:::: {.highlight-cpp .notranslate}
::: highlight
    for (unsigned int step = 0; bpReader.BeginStep() == adios2::StepStatus::OK; ++step)
    {
        auto bpFloats = bpIO.InquireVariable<float>("bpFloats");
        if (bpFloats)
        {
            const adios2::Box<adios2::Dims> sel({{Nx * rank}, {Nx}});
            bpFloats.SetSelection(sel);
            bpReader.Get(bpFloats, simData.data());
        }
        auto bpStep = bpIO.InquireVariable<unsigned int>("bpStep");
        if (bpStep)
        {
            bpReader.Get(bpStep, &inStep);
        }

        bpReader.EndStep();
    }
:::
::::

17. Now we will close the file.

:::: {.highlight-cpp .notranslate}
::: highlight
    bpReader.Close();
:::
::::

18. Now we will call the writer and reader functions:

:::: {.highlight-cpp .notranslate}
::: highlight
    writer(adios, engine, filename, Nx, nSteps, rank, size);
    reader(adios, engine, filename, Nx, nSteps, rank, size);
:::
::::

19. Finally we need to finalize MPI.

:::: {.highlight-cpp .notranslate}
::: highlight
    MPI_Finalize();
:::
::::

20. The final code should look as follows (excluding try/catch and
    optional usage of MPI), and it was derived from the example
    [ADIOS2/examples/hello/bpStepsWriteRead/bpStepsWriteRead.cpp](https://github.com/ornladios/ADIOS2/blob/master/examples/hello/bpStepsWriteRead/bpStepsWriteRead.cpp){.reference
    .external}.

:::: {.highlight-cpp .notranslate}
::: highlight
    /*
     * Distributed under the OSI-approved Apache License, Version 2.0.  See
     * accompanying file Copyright.txt for details.
     *
     * bpStepsWriteRead.cpp  Simple example of writing and reading data through ADIOS2 BP engine with
     * multiple simulations steps for every IO step.
     *
     *  Created on: Feb 16, 2017
     *      Author: William F Godoy godoywf@ornl.gov
     */

    #include <algorithm> // std::for_each
    #include <ios>       // std::ios_base::failure
    #include <iostream>  // std::cout
    #if ADIOS2_USE_MPI
    #include <mpi.h>
    #endif
    #include <stdexcept> //std::invalid_argument std::exception
    #include <vector>

    #include <adios2.h>

    void update_array(std::vector<float> &array, int val)
    {
        std::transform(array.begin(), array.end(), array.begin(),
                       [val](float v) -> float { return v + static_cast<float>(val); });
    }

    void writer(adios2::ADIOS &adios, const std::string &engine, const std::string &fname,
                const size_t Nx, unsigned int nSteps, int rank, int size)
    {
        std::vector<float> simData(Nx, 0);

        adios2::IO bpIO = adios.DeclareIO("WriteIO");
        bpIO.SetEngine(engine);

        const adios2::Dims shape{static_cast<size_t>(size * Nx)};
        const adios2::Dims start{static_cast<size_t>(rank * Nx)};
        const adios2::Dims count{Nx};
        auto bpFloats = bpIO.DefineVariable<float>("bpFloats", shape, start, count);

        auto bpStep = bpIO.DefineVariable<unsigned int>("bpStep");

        adios2::Engine bpWriter = bpIO.Open(fname, adios2::Mode::Write);

        for (unsigned int step = 0; step < nSteps; ++step)
        {
            const adios2::Box<adios2::Dims> sel({0}, {Nx});
            bpFloats.SetSelection(sel);

            bpWriter.BeginStep();
            bpWriter.Put(bpFloats, simData.data());
            bpWriter.Put(bpStep, step);
            bpWriter.EndStep();

            // Update values in the simulation data
            update_array(simData, 10);
        }

        bpWriter.Close();
    }

    void reader(adios2::ADIOS &adios, const std::string &engine, const std::string &fname,
                const size_t Nx, unsigned int /*nSteps*/, int rank, int /*size*/)
    {
        adios2::IO bpIO = adios.DeclareIO("ReadIO");
        bpIO.SetEngine(engine);

        adios2::Engine bpReader = bpIO.Open(fname, adios2::Mode::Read);

        std::vector<float> simData(Nx, 0);
        unsigned int inStep = 0;
        for (unsigned int step = 0; bpReader.BeginStep() == adios2::StepStatus::OK; ++step)
        {
            auto bpFloats = bpIO.InquireVariable<float>("bpFloats");
            if (bpFloats)
            {
                const adios2::Box<adios2::Dims> sel({{Nx * rank}, {Nx}});
                bpFloats.SetSelection(sel);
                bpReader.Get(bpFloats, simData.data());
            }
            auto bpStep = bpIO.InquireVariable<unsigned int>("bpStep");
            if (bpStep)
            {
                bpReader.Get(bpStep, &inStep);
            }

            bpReader.EndStep();
            if (inStep != step)
            {
                std::cout << "ERROR: step mismatch\n";
                return;
            }
        }
        bpReader.Close();
    }

    int main(int argc, char *argv[])
    {
        int rank, size;

    #if ADIOS2_USE_MPI
        int provided;
        // MPI_THREAD_MULTIPLE is only required if you enable the SST MPI_DP
        MPI_Init_thread(&argc, &argv, MPI_THREAD_MULTIPLE, &provided);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        MPI_Comm_size(MPI_COMM_WORLD, &size);
    #else
        rank = 0;
        size = 1;
    #endif

        const std::string engine = argv[1] ? argv[1] : "BPFile";
        std::cout << "Using engine " << engine << std::endl;

        const std::string filename = engine + "StepsWriteRead.bp";
        const unsigned int nSteps = 10;
        const unsigned int Nx = 60000;
        try
        {
            /** ADIOS class factory of IO class objects */
    #if ADIOS2_USE_MPI
            adios2::ADIOS adios(MPI_COMM_WORLD);
    #else
            adios2::ADIOS adios;
    #endif

            writer(adios, engine, filename, Nx, nSteps, rank, size);
            reader(adios, engine, filename, Nx, nSteps, rank, size);
        }
        catch (std::invalid_argument &e)
        {
            std::cout << "Invalid argument exception, STOPPING PROGRAM from rank " << rank << "\n";
            std::cout << e.what() << "\n";
        }
        catch (std::ios_base::failure &e)
        {
            std::cout << "IO System base failure exception, STOPPING PROGRAM "
                         "from rank "
                      << rank << "\n";
            std::cout << e.what() << "\n";
        }
        catch (std::exception &e)
        {
            std::cout << "Exception, STOPPING PROGRAM from rank " << rank << "\n";
            std::cout << e.what() << "\n";
        }

    #if ADIOS2_USE_MPI
        MPI_Finalize();
    #endif

        return 0;
    }
:::
::::

21. You can compile and run it as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    cd Path-To-ADIOS2/examples/hello/bpStepsWriteRead
    mkdir build
    cd build
    cmake -DADIOS2_DIR=Path-To-ADIOS2/build/ ..
    cmake --build .
    mpirun -np 2 ./adios2_hello_bpStepsWriteRead_mpi
:::
::::

22. You can check the content of the output file
    "BPFileStepsWriteRead.bp" using *bpls* as follows:

:::: {.highlight-bash .notranslate}
::: highlight
    Path-To-ADIOS2/build/bin/bpls ./BPFileStepsWriteRead.bp

      float     bpFloats  10*{120000}
      uint32_t  bpStep    10*scalar
:::
::::
::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::::: {.toctree-wrapper .compound}
[]{#document-ecosystem/h5vol}

::::::::::: {#hdf5-api-support-through-vol .section}
## HDF5 API Support through VOL[](#hdf5-api-support-through-vol "Link to this heading"){.headerlink}

We have developed a HDF5 VOL in order to comply with the ECP request to
support HDF5 API. Through this VOL the HDF5 clients can read and write
general ADIOS files.

:::: {#disclaimer .section}
### Disclaimer[](#disclaimer "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

The Virtual Object Layer (VOL) is a feature introduced in recent release
of HDF5 1.12
([https://hdf5.wiki/index.php/New_Features_in_HDF5_Release_1.12](https://hdf5.wiki/index.php/New_Features_in_HDF5_Release_1.12){.reference
.external}).

So please do make sure your HDF5 version supports the latest VOL.
:::

Once the ADIOS VOL is compiled, There are two ways to apply it:

- externally (through dynamic library, no code change)

- internally (through client code).
::::

::::: {#external .section}
### External[](#external "Link to this heading"){.headerlink}

- Set the following environment parameters:

:::: {.highlight-c++ .notranslate}
::: highlight
    HDF5_VOL_CONNECTOR=ADIOS2_VOL
    HDF5_PLUGIN_PATH=/replace/with/your/adios2_vol/lib/path/
:::
::::

Without code change, ADIOS2 VOL will be loaded at runtime by HDF5, to
access ADIOS files without changing user code.
:::::

::::: {#internal .section}
### Internal[](#internal "Link to this heading"){.headerlink}

- include adios header

- call the function to set VOL when H5F is initiated

- call the function to unset VOL when H5F is closed

:::: {.highlight-c++ .notranslate}
::: highlight
    // other includes
    #include <adios2/h5vol/H5Vol.h> // ADD THIS LINE TO INCLUDE ADIOS VOL

    hid_t  pid = H5Pcreate(H5P_FILE_ACCESS);
    // other declarations
    hid_t fid = H5Fopen(filename, mode, pid);

    H5VL_ADIOS2_set(pid); // ADD THIS LINE TO USE ADIOS VOL

    H5Fclose(fid);

    H5VL_ADIOS2_unset();  // ADD THIS LINE TO EXIT ADIOS VOL
:::
::::

**Note:** The following features are not supported in this VOL:

> <div>
>
> - hyperslab support
>
> - HDF5 parameters are not passed down. e.g. compression/decompression
>
> - ADIOS2 parameters is not setup.
>
> - user defined types
>
> - change of variable extent is not supported in ADIOS2.
>
> </div>
:::::
:::::::::::

[]{#document-ecosystem/utilities}

:::::::::::::::::::::::: {#command-line-utilities .section}
## Command Line Utilities[](#command-line-utilities "Link to this heading"){.headerlink}

ADIOS 2 provides a set of command line utilities for quick data
exploration and manipulation that builds on top of the library. The are
located in the inside the [`adios2-install-location/bin`{.docutils
.literal .notranslate}]{.pre} directory after a [`make`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`install`{.docutils .literal .notranslate}]{.pre}

::: {.admonition .tip}
Tip

Optionally the [`adios2-install-location/bin`{.docutils .literal
.notranslate}]{.pre} location can be added to your PATH to avoid
absolute paths when using adios2 command line utilities
:::

Currently supported tools are:

- [`bpls`{.docutils .literal .notranslate}]{.pre} : exploration of
  bp/hdf5 files data and metadata in human readable formats

- [`adios_reorganize`{.docutils .literal .notranslate}]{.pre}

- [`adios2-config`{.docutils .literal .notranslate}]{.pre}

- [`sst_conn_tool`{.docutils .literal .notranslate}]{.pre} : SST staging
  engine connectivity diagnostic tool

::::::::: {#bpls-inspecting-data .section}
### bpls : Inspecting Data[](#bpls-inspecting-data "Link to this heading"){.headerlink}

The [`bpls`{.docutils .literal .notranslate}]{.pre} utility is for
examining and pretty-printing the content of ADIOS output files (BP and
HDF5 files). By default, it lists the variables in the file including
the type, name, and dimensionality.

Let's assume we run the Heat Transfer tutorial example and produce the
output by

:::: {.highlight-bash .notranslate}
::: highlight
    $ mpirun -n 12 ./heatSimulation  sim.bp  3 4   5 4   3 1
    Process decomposition  : 3 x 4
    Array size per process : 5 x 4
    Number of output steps : 3
    Iterations per step    : 1

    $ mpirun -n 3 ./heatAnalysis sim.bp a.bp 3 1

    $ bpls a.bp
      double   T     3*{15, 16}
      double   dT    3*{15, 16}
:::
::::

In our example, we have two arrays, [`T`{.docutils .literal
.notranslate}]{.pre} and [`dT`{.docutils .literal .notranslate}]{.pre}.
Both are 2-dimensional [`double`{.docutils .literal .notranslate}]{.pre}
arrays, their global size is [`15x16`{.docutils .literal
.notranslate}]{.pre} and the file contains [`3`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`output`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`steps`{.docutils .literal .notranslate}]{.pre} of these
arrays.

::: {.admonition .note}
Note

bpls is written in C++ and therefore sees the order of the dimensions in
*row major*. If the data was written from Fortran in column-major order,
you will see the dimension order flipped when listing with bpls, just as
a code written in C++ or python would see the data.
:::

Here is the description of the most used options (use [`bpls`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`-h`{.docutils .literal .notranslate}]{.pre} to print help
on all options for this utility).

- [`-l`{.docutils .literal .notranslate}]{.pre}

  Print the min/max of the arrays and the values of scalar values

  :::: {.highlight-bash .notranslate}
  ::: highlight
      $ bpls -l a.bp
        double   T     3*{15, 16} = 0 / 200
        double   dT    3*{15, 16} = -53.1922 / 49.7861
  :::
  ::::

- [`-a`{.docutils .literal .notranslate}]{.pre} [`-A`{.docutils .literal
  .notranslate}]{.pre}

  List the attributes along with the variables. [`-A`{.docutils .literal
  .notranslate}]{.pre} will print the attributes only.

  :::: {.highlight-bash .notranslate}
  ::: highlight
      $ bpls a.bp -la
        double   T               3*{15, 16} = 0 / 200
        string   T/description   attr   = "Temperature from simulation"
        string   T/unit          attr   = "C"
        double   dT              3*{15, 16} = -53.1922 / 49.7861
        string   dT/description  attr   = "Temperature difference between two steps calculated in analysis"
  :::
  ::::

- [`pattern`{.docutils .literal .notranslate}]{.pre}, [`-e`{.docutils
  .literal .notranslate}]{.pre}

  Select which variables/attributes to list or dump. By default the
  pattern(s) are interpreted as shell file patterns.

  :::: {.highlight-bash .notranslate}
  ::: highlight
      $ bpls a.bp -la T*
        double   T               3*{15, 16} = 0 / 200
  :::
  ::::

  Multiple patterns can be defined in the command line.

  :::: {.highlight-bash .notranslate}
  ::: highlight
      $ bpls a.bp -la T/* dT/*
        string   T/description   attr   = "Temperature from simulation"
        string   T/unit          attr   = "C"
        string   dT/description  attr   = "Temperature difference between two steps calculated in analysis"
  :::
  ::::

  If the -e option is given (all) the pattern(s) will be interpreted as
  regular expressions.

  :::: {.highlight-bash .notranslate}
  ::: highlight
      $ bpls a.bp -la T.* -e
        double   T               3*{15, 16} = 0 / 200
        string   T/description   attr   = "Temperature from simulation"
        string   T/unit          attr   = "C"
  :::
  ::::

- [`-D`{.docutils .literal .notranslate}]{.pre}

  Print the decomposition of a variable. In the BP file, the data blocks
  written by different writers are stored separately and have their own
  size info and min/max statistics. This option is useful at code
  development to check if the output file is written the way intended.

  :::: {.highlight-bash .notranslate}
  ::: highlight
      $ bpls a.bp -l T -D
        double   T               3*{15, 16} = 0 / 200
          step 0:
            block 0: [ 0: 4,  0:15] = 3.54199e-14 / 200
            block 1: [ 5: 9,  0:15] = 58.3642 / 200
            block 2: [10:14,  0:15] = 0 / 200
          step 1:
            block 0: [ 0: 4,  0:15] = 31.4891 / 153.432
            block 1: [ 5: 9,  0:15] = 68.2107 / 180.184
            block 2: [10:14,  0:15] = 31.4891 / 161.699
          step 2:
            block 0: [ 0: 4,  0:15] = 48.0431 / 135.225
            block 1: [ 5: 9,  0:15] = 74.064 / 170.002
            block 2: [10:14,  0:15] = 48.0431 / 147.87
  :::
  ::::

  In this case we find 3 blocks per output step and 3 output steps. We
  can see that the variable [`T`{.docutils .literal .notranslate}]{.pre}
  was decomposed in the first (slow) dimension. In the above example,
  the [`T`{.docutils .literal .notranslate}]{.pre} variable in the
  simulation output ([`sim.bp`{.docutils .literal .notranslate}]{.pre})
  had 12 blocks per step, but the analysis code was running on 3
  processes, effectively reorganizing the data into fewer larger blocks.

- [`-d`{.docutils .literal .notranslate}]{.pre}

  Dump the data content of a variable. For pretty-printing, one should
  use the additional [`-n`{.docutils .literal .notranslate}]{.pre} and
  [`-f`{.docutils .literal .notranslate}]{.pre} options. For selecting
  only a subset of a variable, one should use the [`-s`{.docutils
  .literal .notranslate}]{.pre} and [`-c`{.docutils .literal
  .notranslate}]{.pre} options.

  By default, six values are printed per line and using C style
  [`-g`{.docutils .literal .notranslate}]{.pre} prints for floating
  point values.

  :::: {.highlight-bash .notranslate}
  ::: highlight
      $ bpls a.bp -d T
        double   T     3*{15, 16}
          (0, 0, 0)    124.925 124.296 139.024 95.2078 144.864 191.485
          (0, 0, 6)    139.024 140.814 124.925 109.035 110.825 58.3642
          (0, 0,12)    104.985 154.641 110.825 125.553 66.5603 65.9316
          ...
          (2,14, 4)    105.918 116.842 111.249 102.044 93.3121 84.5802
          (2,14,10)    75.3746 69.782 80.706 93.5492 94.7595 95.0709
  :::
  ::::

  For pretty-printing, use the additional [`-n`{.docutils .literal
  .notranslate}]{.pre} and [`-f`{.docutils .literal .notranslate}]{.pre}
  options.

  :::: {.highlight-bash .notranslate}
  ::: highlight
      $ bpls a.bp -d T -n 16 -f "%3.0f"
        double   T     3*{15, 16}
          (0, 0, 0)    125 124 139  95 145 191 139 141 125 109 111  58 105 155 111 126
          (0, 1, 0)     67  66  81  37  86 133  81  82  67  51  52   0  47  96  52  67
          (0, 2, 0)    133 133 148 104 153 200 148 149 133 118 119  67 114 163 119 134
          ...
          (2,13, 0)     98  98  96  96 115 132 124 109  97  86  71  63  79  98  97  95
          (2,14, 0)     96  96  93  93 106 117 111 102  93  85  75  70  81  94  95  95
  :::
  ::::

  For selecting a subset of a variable, use the [`-s`{.docutils .literal
  .notranslate}]{.pre} and [`-c`{.docutils .literal .notranslate}]{.pre}
  options. These options are N+1 dimensional for N-dimensional arrays
  with more than one steps. The first element of the options are used to
  select the starting step and the number of steps to print.

  The following example dumps a [`4x4`{.docutils .literal
  .notranslate}]{.pre} small subset from the center of the array, one
  step from the second (middle) step:

  :::: {.highlight-bash .notranslate}
  ::: highlight
      $ bpls a.bp -d T -s "1,6,7" -c "1,4,4" -n 4
        double   T     3*{15, 16}
          slice (1:1, 6:9, 7:10)
          (1,6, 7)    144.09 131.737 119.383 106.787
          (1,7, 7)    145.794 133.44 121.086 108.49
          (1,8, 7)    145.794 133.44 121.086 108.49
          (1,9, 7)    144.09 131.737 119.383 106.787
  :::
  ::::

- [`-y`{.docutils .literal .notranslate}]{.pre} [`--noindex`{.docutils
  .literal .notranslate}]{.pre}

  Data can be dumped in a format that is easier to import later into
  other tools, like Excel. The leading array indexes can be omitted by
  using this option. Non-data lines, like the variable and slice info,
  are printed with a starting [`;`{.docutils .literal
  .notranslate}]{.pre}.

  :::: {.highlight-bash .notranslate}
  ::: highlight
      $ bpls a.bp -d T -s "1,6,7" -c "1,4,4" -n 4 --noindex
        ; double   T     3*{15, 16}
        ;   slice (1:1, 6:9, 7:10)
        144.09 131.737 119.383 106.787
        145.794 133.44 121.086 108.49
        145.794 133.44 121.086 108.49
        144.09 131.737 119.383 106.787
  :::
  ::::

::::: {.admonition .note}
Note

HDF5 files can also be dumped with bpls if ADIOS was built with HDF5
support. Note that the HDF5 files do not contain min/max information for
the arrays and therefore bpls always prints 0 for them:

:::: {.highlight-bash .notranslate}
::: highlight
    $ bpls -l a.h5
      double   T     3*{15, 16} = 0 / 0
      double   dT    3*{15, 16} = 0 / 0
:::
::::
:::::
:::::::::

::::: {#adios-reorganize .section}
### adios_reorganize[](#adios-reorganize "Link to this heading"){.headerlink}

[`adios_reorganize`{.docutils .literal .notranslate}]{.pre} and
[`adios_reorganize_mpi`{.docutils .literal .notranslate}]{.pre} are
generic ADIOS tools to read in ADIOS streams and output the same data
into another ADIOS stream. The two tools are for serial and MPI
environments, respectively. They can be used for

- converting files between ADIOS BP and HDF5 format

- using separate compute nodes to stage I/O from/to disk to/from a large
  scale application

- reorganizing the data blocks for a different number of blocks

Let's assume we run the Heat Transfer tutorial example and produce the
output by

:::: {.highlight-bash .notranslate}
::: highlight
    $ mpirun -n 12 ./heatSimulation  sim.bp  3 4   5 4   3 1
    Process decomposition  : 3 x 4
    Array size per process : 5 x 4
    Number of output steps : 3
    Iterations per step    : 1

    $ bpls sim.bp
      double   T     3*{15, 16}
:::
::::

In our example, we have an array, [`T`{.docutils .literal
.notranslate}]{.pre}. It is a 2-dimensional [`double`{.docutils .literal
.notranslate}]{.pre} array, its global size is [`15x16`{.docutils
.literal .notranslate}]{.pre} and the file contains [`3`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`output`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`steps`{.docutils .literal .notranslate}]{.pre} of this
array. The array is composed of 12 separate blocks coming from the 12
producers in the application.

- Convert BP file to HDF5 file

  > <div>
  >
  > If ADIOS is built with HDF5 support, this tool can be used to
  > convert between the two file formats.
  >
  > :::: {.highlight-bash .notranslate}
  > ::: highlight
  >     $ mpirun -n 2 adios_reorganize_mpi sim.bp sim.h5 BPFile "" HDF5 "" 2 1
  >
  >     $ bpls sim.h5
  >       double   T     3*{15, 16}
  >
  >     $ h5ls -r sim.h5
  >     /                        Group
  >     /Step0                   Group
  >     /Step0/T                 Dataset {15, 16}
  >     /Step1                   Group
  >     /Step1/T                 Dataset {15, 16}
  >     /Step2                   Group
  >     /Step2/T                 Dataset {15, 16}
  > :::
  > ::::
  >
  > </div>

- Stage I/O through extra compute nodes

  > <div>
  >
  > If writing data to disk is a bottleneck to the application, it may
  > be worth to use extra nodes for receiving the data quickly from the
  > application and then write to disk while the application continues
  > computing. Similarly, data can be staged in from disk into extra
  > nodes and make it available for fast read-in for an application. One
  > can use one of the staging engines in ADIOS to perform this data
  > staging (SST, SSC, DataMan).
  >
  > Assuming that the heatSimulation is using SST instead of file I/O in
  > a run (set in its [`adios2.xml`{.docutils .literal
  > .notranslate}]{.pre} configuration file), staging to disk can be
  > done this way:
  >
  > :::: {.highlight-bash .notranslate}
  > ::: highlight
  >     Make sure adios2.xml sets SST for the simulation:
  >         <io name="SimulationOutput">
  >             <engine type="SST">
  >             </engine>
  >         </io>
  >
  >
  >     $ mpirun -n 12 ./heatSimulation  sim.bp  3 4   5 4   3 1 : \
  >              -n 2 adios_reorganize_mpi sim.bp staged.bp SST "" BPFile "" 2 1
  >
  >     $ bpls staged.bp
  >       double   T     3*{15, 16}
  > :::
  > ::::
  >
  > Data is staged to the extra 2 cores and those will write the data to
  > disk while the heatSimulation calculates the next step. Note, that
  > this staging can only be useful if the tool can write all data to
  > disk before the application produces the next output step.
  > Otherwise, it will still block the application for I/O.
  >
  > </div>

- Reorganizing the data blocks in file for a different number of blocks

  > <div>
  >
  > In the above example, the application writes the array from 12
  > processes, but then [`adios_reorganize_mpi`{.docutils .literal
  > .notranslate}]{.pre} reads the global arrays on 2 processes. The
  > output file on disk will therefore contain the array in 2 blocks.
  > This reorganization of the array may be useful if reading is too
  > slow for a dataset created by many-many processes. One may want to
  > reorganize a file written by tens or hundreds of thousands of
  > processes if one wants to read the content more than one time and
  > the read time proves to be a bottleneck in one's work flow.
  >
  > :::: {.highlight-bash .notranslate}
  > ::: highlight
  >     $ mpirun -n 12 ./heatSimulation  sim.bp  3 4   5 4   3 1
  >     $ bpls sim.bp -D
  >       double   T     3*{15, 16}
  >           step 0:
  >             block  0: [ 0: 4,  0: 3]
  >             block  1: [ 5: 9,  0: 3]
  >             block  2: [10:14,  0: 3]
  >             block  3: [ 0: 4,  4: 7]
  >             block  4: [ 5: 9,  4: 7]
  >             block  5: [10:14,  4: 7]
  >             block  6: [ 0: 4,  8:11]
  >             block  7: [ 5: 9,  8:11]
  >             block  8: [10:14,  8:11]
  >             block  9: [ 0: 4, 12:15]
  >             block 10: [ 5: 9, 12:15]
  >             block 11: [10:14, 12:15]
  >           step 1:
  >             block  0: [ 0: 4,  0: 3]
  >             block  1: [ 5: 9,  0: 3]
  >             block  2: [10:14,  0: 3]
  >             block  3: [ 0: 4,  4: 7]
  >             block  4: [ 5: 9,  4: 7]
  >             block  5: [10:14,  4: 7]
  >             block  6: [ 0: 4,  8:11]
  >             block  7: [ 5: 9,  8:11]
  >             block  8: [10:14,  8:11]
  >             block  9: [ 0: 4, 12:15]
  >             block 10: [ 5: 9, 12:15]
  >             block 11: [10:14, 12:15]
  >           step 2:
  >             block  0: [ 0: 4,  0: 3]
  >             block  1: [ 5: 9,  0: 3]
  >             block  2: [10:14,  0: 3]
  >             block  3: [ 0: 4,  4: 7]
  >             block  4: [ 5: 9,  4: 7]
  >             block  5: [10:14,  4: 7]
  >             block  6: [ 0: 4,  8:11]
  >             block  7: [ 5: 9,  8:11]
  >             block  8: [10:14,  8:11]
  >             block  9: [ 0: 4, 12:15]
  >             block 10: [ 5: 9, 12:15]
  >             block 11: [10:14, 12:15]
  >
  >
  >     $ mpirun -n 2 adios_reorganize_mpi sim.bp reorg.bp BPFile "" BPFile "" 2 1
  >     $ bpls reorg.bp -D
  >       double   T     3*{15, 16}
  >           step 0:
  >             block 0: [ 0: 6,  0:15]
  >             block 1: [ 7:14,  0:15]
  >           step 1:
  >             block 0: [ 0: 6,  0:15]
  >             block 1: [ 7:14,  0:15]
  >           step 2:
  >             block 0: [ 0: 6,  0:15]
  >             block 1: [ 7:14,  0:15]
  > :::
  > ::::
  >
  > </div>
:::::

::::: {#adios2-config .section}
### adios2-config[](#adios2-config "Link to this heading"){.headerlink}

adios2-config is provided to aid with non-CMake builds (*e.g.* manually
generated Makefile). Running the adios2-config command under
adios2-install-dir/bin/adios2-config will generate the following usage
information:

:::: {.highlight-bash .notranslate}
::: highlight
    ./adios2-config --help
    adios2-config (--help | [--c-flags] [--c-libs] [--cxx-flags] [--cxx-libs] [-fortran-flags] [--fortran-libs])
      --help           Display help information
      -c               Both compile and link flags for the C bindings
      --c-flags        Preprocessor and compile flags for the C bindings
      --c-libs         Linker flags for the C bindings
      -x               Both compile and link flags for the C++ bindings
      --cxx-flags      Preprocessor and compile flags for the C++ bindings
      --cxx-libs       Linker flags for the C++ bindings
      -f               Both compile and link flags for the F90 bindings
      --fortran-flags  Preprocessor and compile flags for the F90 bindings
      --fortran-libs   Linker flags for the F90 bindings
:::
::::

Please refer to the [[From non-CMake build systems]{.std
.std-ref}](#document-setting_up/setting_up#from-non-cmake-build-systems){.reference
.internal} for more information on how to use this command.
:::::

::::::::: {#sst-conn-tool-sst-network-connectivity-tool .section}
### sst_conn_tool : SST network connectivity tool[](#sst-conn-tool-sst-network-connectivity-tool "Link to this heading"){.headerlink}

The [`sst_conn_tool`{.docutils .literal .notranslate}]{.pre} utility
exposes some aspects of SST network connectivity parameters and activity
in order to allow debugging of SST connections.

In its simplest usage, it just lets you test an SST connection (between
two runs of the program) and tells you the network information its
trying, I.E. what IP address and port it determined to use for
listening, and if it's connecting somewhere what those parameters are.
For example, you'd first run sst_conn_tool in one window and its output
would look like this:

:::: {.highlight-bash .notranslate}
::: highlight
    bash-3.2$ bin/sst_conn_tool

            Sst writer is listening for TCP/IP connection at IP 192.168.1.17, port 26051

            Sst connection tool waiting for connection…
:::
::::

To try to connect from another window, you run sst_conn_tool with the -c
or ---connect option:

:::: {.highlight-bash .notranslate}
::: highlight
    bash-3.2$ bin/sst_conn_tool -c

            Sst reader at IP 192.168.1.17, listening UDP port 26050


            Attempting TCP/IP connection to writer at IP 192.168.1.17, port 26051

    Connection success, all is well!
    bash-3.2$
:::
::::

Here, it has found the contact information file, tried and succeeded in
making the connection and has indicated that all is well. In the first
window, we get a similar message about the success of the connection.

In the event that there is trouble with the connection, there is a "-i"
or "---info" option that will provide additional information about the
network configuration options. For example:

:::: {.highlight-bash .notranslate}
::: highlight
    bash-3.2$ bin/sst_conn_tool -i

            ADIOS2_IP_CONFIG best guess hostname is "sandy.local"
            ADIOS2_IP_CONFIG Possible interface lo0 : IPV4 127.0.0.1
            ADIOS2_IP_CONFIG Possible interface en0 : IPV4 192.168.1.56
            ADIOS2_IP_CONFIG Possible interface en5 : IPV4 192.168.1.17
            ADIOS2_IP_CONFIG best guess IP is "192.168.1.17"
            ADIOS2_IP_CONFIG default port range is "any"

            The following environment variables can impact ADIOS2_IP_CONFIG operation:
                    ADIOS2_IP               -  Publish the specified IP address for contact
                    ADIOS2_HOSTNAME         -  Publish the specified hostname for contact
                    ADIOS2_USE_HOSTNAME     -  Publish a hostname preferentially over IP address
                    ADIOS2_INTERFACE        -  Use the IP address associated with the specified network interface
                    ADIOS2_PORT_RANGE       -  Use a port within the specified range "low:high",
                                               or specify "any" to let the OS choose

            Sst writer is listening for TCP/IP connection at IP 192.168.1.17, port 26048

            Sst connection tool waiting for connection...
:::
::::

Full options for sst_conn_tool:

Operational Modes:

- 

  [`-l`{.docutils .literal .notranslate}]{.pre} [`--listen`{.docutils .literal .notranslate}]{.pre}

  :   Display connection parameters and wait for an SST connection
      (default)

- [`-c`{.docutils .literal .notranslate}]{.pre} [`--connect`{.docutils
  .literal .notranslate}]{.pre} Attempt a connection to an
  already-running instance of sst_conn_tool

Additional Options:

- 

  [`-i`{.docutils .literal .notranslate}]{.pre} [`--info`{.docutils .literal .notranslate}]{.pre}

  :   Display additional networking information for this host

- 

  [`-f`{.docutils .literal .notranslate}]{.pre} [`--file`{.docutils .literal .notranslate}]{.pre}

  :   Use file-based contact info sharing (default). The SST contact
      file is created in the current directory

- 

  [`-s`{.docutils .literal .notranslate}]{.pre} [`--screen`{.docutils .literal .notranslate}]{.pre}

  :   Use screen-based contact info sharing, SST contact info is
      displayed/entered via terminal

- 

  [`-h`{.docutils .literal .notranslate}]{.pre} [`--help`{.docutils .literal .notranslate}]{.pre}

  :   Display this message usage and options
:::::::::
::::::::::::::::::::::::

[]{#document-ecosystem/visualization}

:::::::::::::::::: {#visualizing-data .section}
## Visualizing Data[](#visualizing-data "Link to this heading"){.headerlink}

Certain ADIOS2 bp files can be recognized by third party visualization
tools. This section describes how to create an ADIOS2 bp file to
accomodate the visualization product requirements.

::::::::::::::::: {#using-vtk-and-paraview .section}
### Using VTK and Paraview[](#using-vtk-and-paraview "Link to this heading"){.headerlink}

ADIOS BP files can now be seamlessly integrated into the [Visualization
Toolkit](https://vtk.org/){.reference .external} and
[Paraview](https://www.paraview.org/){.reference .external}. Datasets
can be described with an additional attribute that conforms to the [VTK
XML data model
formats](https://vtk.org/wp-content/uploads/2015/04/file-formats.pdf){.reference
.external} as high-level descriptors that will allow interpretation of
ADIOS2 variables into a hierarchy understood by the VTK infrastructure.
This XML data format is saved in ADIOS2 as either an attribute or as an
additional [`vtk.xml`{.docutils .literal .notranslate}]{.pre} file
inside the [`file.bp.dir`{.docutils .literal .notranslate}]{.pre}
directory.

There are currently a number of limitations:

- It only works with MPI builds of VTK and Paraview

- Support only one block per ADIOS dataset

- Only supports BP Files, streams are not supported

- Currently working up to 3D (and linearized 1D) variables for scalars
  and vectors.

- Image Data, vti, is supported with ADIOS2 Global Array Variables only

- Unstructured Grid, vtu, is supported with ADIOS2 Local Arrays
  Variables only

Two VTK file types are supported:

1.  Image data (.vti)

2.  Unstructured Grid (.vtu)

The main idea is to populate the above XML format contents describing
the extent and the data arrays with ADIOS variables in the BP data set.
The result is a more-than-compact typical VTK data file since extra
information about the variable, such as dimensions and type, as they
already exist in the BP data set.

A typical VTK image data XML descriptor (.vti):

:::: {.highlight-xml .notranslate}
::: highlight
    <?xml version="1.0"?>
    <VTKFile type="ImageData">
      <ImageData WholeExtent="x1 x2 y1 y2 z1 z2" Origin="x0 y0 z0" Spacing="dx dy dz">
        <Piece Extent="x1 x2 y1 y2 z1 z2">
          <PointData>
            <DataArray Name="p1"/>
            <DataArray Name="p2"/>
          </PointData>
          <CellData>
            <DataArray Name="c1"/>
            <DataArray Name="c2"/>
          </CellData>
        </Piece>
      </ImageData>
    </VTKFile>
:::
::::

A typical VTK unstructured grid XML descriptor (.vtu):

:::: {.highlight-xml .notranslate}
::: highlight
    <?xml version="1.0"?>
    <VTKFile type="ImageData">
      <ImageData WholeExtent="x1 x2 y1 y2 z1 z2" Origin="x0 y0 z0" Spacing="dx dy dz">
        <Piece Extent="x1 x2 y1 y2 z1 z2">
          <PointData>
            <DataArray Name="p1"/>
            <DataArray Name="p2"/>
          </PointData>
          <CellData>
            <DataArray Name="c1"/>
            <DataArray Name="c2"/>
          </CellData>
        </Piece>
      </ImageData>
    </VTKFile>
:::
::::

In addition, VTK can interpret physical-time or output-step varying data
stored with ADIOS by reusing the special "TIME" tag. This is better
illustrated in the following section.

:::::::::::: {#saving-the-vtk-xml-data-model .section}
#### Saving the vtk.xml data model[](#saving-the-vtk-xml-data-model "Link to this heading"){.headerlink}

For the full source code of the following illustration example see the
[gray-scott adios2
tutorial](https://github.com/pnorbert/adiosvm/tree/master/Tutorial/gray-scott){.reference
.external}.

To incorporate the data model in a BP data file, the application has two
options:

1.  Adding a string attribute called "vtk.xml" in code. "TIME" is a
    special tag for adding physical time variables.

:::: {.highlight-c++ .notranslate}
::: highlight
    const std::string imageData = R"(
         <?xml version="1.0"?>
         <VTKFile type="ImageData" version="0.1" byte_order="LittleEndian">
           <ImageData WholeExtent=")" + extent + R"(" Origin="0 0 0" Spacing="1 1 1">
             <Piece Extent=")" + extent + R"(">
               <CellData Scalars="U">
                   <DataArray Name="U" />
                   <DataArray Name="V" />
                   <DataArray Name="TIME">
                     step
                   </DataArray>
               </CellData>
             </Piece>
           </ImageData>
         </VTKFile>)";

    io.DefineAttribute<std::string>("vtk.xml", imageData);
:::
::::

::: {.admonition .tip}
Tip

C++11 users should take advantage C++11 string literals
([`R"(`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`xml_here`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`)"`{.docutils
.literal .notranslate}]{.pre}) to simplify escaping characters in the
XML.
:::

The resulting bpls output should contain the "vtk.xml" attribute and the
variables in the model:

:::: {.highlight-bash .notranslate}
::: highlight
    > bpls gs.bp -lav
    File info:
      of variables:  3
      of attributes: 7
      statistics:    Min / Max

      double   Du       attr   = 0.2
      double   Dv       attr   = 0.1
      double   F        attr   = 0.02
      double   U        24*{48, 48, 48} = 0.107439 / 1.04324
      double   V        24*{48, 48, 48} = 0 / 0.672232
      double   dt       attr   = 1
      double   k        attr   = 0.048
      double   noise    attr   = 0.01
      int32_t  step     24*scalar = 0 / 575
      string   vtk.xml  attr   =
    <VTKFile type="ImageData" version="0.1" byte_order="LittleEndian">
      <ImageData WholeExtent="0 49 0 49 0 49" Origin="0 0 0" Spacing="1 1 1">
        <Piece Extent="0 49 0 49 0 49">
          <CellData Scalars="U">
            <DataArray Name="U" />
            <DataArray Name="V" />
            <DataArray Name="TIME">
              step
            </DataArray>
          </CellData>
        </Piece>
      </ImageData>
    </VTKFile>
:::
::::

2.  Saving a "vtk.xml" file inside the file.bp.dir to describe the data
    after is created

:::: {.highlight-default .notranslate}
::: highlight
    > cat gs.bp.dir/vtk.xml

      <?xml version="1.0"?>
      <VTKFile type="ImageData" version="0.1" byte_order="LittleEndian">
        <ImageData WholeExtent=")" + extent + R"(" Origin="0 0 0" Spacing="1 1 1">
          <Piece Extent=")" + extent + R"(">
            <CellData Scalars="U">
              <DataArray Name="U" />
              <DataArray Name="V" />
              <DataArray Name="TIME">
                step
              </DataArray>
            </CellData>
          </Piece>
        </ImageData>
      </VTKFile>
:::
::::

This BP file should be recognize by Paraview:

![](https://i.imgur.com/ap3l9Z5.png:alt:my-picture2)

Similarly, unstructured grid (.vtu) support can be added with the
limitations of using specific labels for the variable names setting the
"connectivity", "vertices", and cell "types".

The following example is taken from example 2 of the [MFEM product
examples website](https://mfem.org/examples/){.reference .external}
using ADIOS2:

The resulting bpls output for unstructured grid data types:

:::: {.highlight-bash .notranslate}
::: highlight
    File info:
      of variables:  6
      of attributes: 4
      statistics:    Min / Max

      uint32_t  NumOfElements       {4} = 1024 / 1024
      uint32_t  NumOfVertices       {4} = 1377 / 1377
      string    app                 attr   = "MFEM"
      uint64_t  connectivity        [4]*{1024, 9} = 0 / 1376
      uint32_t  dimension           attr   = 3
      string    glvis_mesh_version  attr   = "1.0"
      double    sol                 [4]*{1377, 3} = -0.201717 / 1.19304
      uint32_t  types               scalar = 11
      double    vertices            [4]*{1377, 3} = -1.19304 / 8.20172
      string    vtk.xml             attr   =
    <VTKFile type="UnstructuredGrid" version="0.1" byte_order="LittleEndian">
      <UnstructuredGrid>
        <Piece NumberOfPoints="NumOfVertices" NumberOfCells="NumOfElements">
          <Points>
            <DataArray Name="vertices" />
          </Points>
          <Cells>
            <DataArray Name="connectivity" />
            <DataArray Name="types" />
          </Cells>
          <PointData>
            <DataArray Name="sol" />
          </PointData>
        </Piece>
      </UnstructuredGrid>
    </VTKFile>
:::
::::

and resulting visualization in Paraview for different "cell" types:

![](https://i.imgur.com/ke1xiNh.png:alt:my-picture3)
::::::::::::
:::::::::::::::::
::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::: {.toctree-wrapper .compound}
[]{#document-faq/faq}

:::::::::::::::::: {#faq .section}
## FAQ[](#faq "Link to this heading"){.headerlink}

::: {#mpi-vs-non-mpi .section}
### MPI vs Non-MPI[](#mpi-vs-non-mpi "Link to this heading"){.headerlink}

1.  [[Can I use the same library for MPI and non-MPI code?]{.std
    .std-ref}](#can-i-use-the-same-library-for-mpi-and-non-mpi-code){.reference
    .internal}
:::

::: {#apis .section}
### APIs[](#apis "Link to this heading"){.headerlink}

1.  [[Can I use ADIOS 2 C++11 library with C++98 codes?]{.std
    .std-ref}](#can-i-use-adios-2-c-11-library-with-c-98-codes){.reference
    .internal}

2.  [[Why are C and Fortran APIs missing functionality?]{.std
    .std-ref}](#why-are-c-and-fortran-apis-missing-functionality){.reference
    .internal}

3.  [[C++11: Why are std::string arguments passed sometimes by value and
    sometimes by reference?]{.std
    .std-ref}](#c-11-why-are-std-string-arguments-passed-sometimes-by-value-and-sometimes-by-reference){.reference
    .internal}

4.  [[C++11: Should I pass adios2:: objects by value or by
    reference?]{.std
    .std-ref}](#c-11-should-i-pass-adios2-objects-by-value-or-by-reference){.reference
    .internal}

5.  [[Fortran: Can I pass slices and temporary arrays to
    adios2_put?]{.std
    .std-ref}](#fortran-can-i-pass-slices-and-temporary-arrays-to-adios2-put){.reference
    .internal}
:::

::: {#building-on-titan .section}
### Building on Titan[](#building-on-titan "Link to this heading"){.headerlink}

1.  [[My application uses PGI compilers on Titan, can I link ADIOS
    2?]{.std
    .std-ref}](#my-application-uses-pgi-compilers-on-titan-can-i-link-adios-2){.reference
    .internal}

2.  [[How do I enable the Python bindings on Titan?]{.std
    .std-ref}](#how-do-i-enable-the-python-bindings-on-titan){.reference
    .internal}
:::

::: {#building-and-running-on-fujitsu-fx100 .section}
### Building and Running on Fujitsu FX100[](#building-and-running-on-fujitsu-fx100 "Link to this heading"){.headerlink}

1.  [[How do I build ADIOS 2 on Fujitsu FX100?]{.std
    .std-ref}](#how-do-i-build-adios-2-on-fujitsu-fx100){.reference
    .internal}

2.  [[SST engine hangs on Fujitsu FX100. Why?]{.std
    .std-ref}](#sst-engine-hangs-on-fujitsu-fx100-why){.reference
    .internal}
:::

::::::::::::: {#faqs-answered .section}
### FAQs Answered[](#faqs-answered "Link to this heading"){.headerlink}

::: {#can-i-use-the-same-library-for-mpi-and-non-mpi-code .section}
#### Can I use the same library for MPI and non-MPI code?[](#can-i-use-the-same-library-for-mpi-and-non-mpi-code "Link to this heading"){.headerlink}

Short answer: Yes, since version 2.6.0.

Long answer: One build of ADIOS can be used by both serial and parallel
applications. Use the [`-s`{.docutils .literal .notranslate}]{.pre} and
[`-m`{.docutils .literal .notranslate}]{.pre} flags in the
[`adios2-config`{.docutils .literal .notranslate}]{.pre} command. By
default, or with the [`-m`{.docutils .literal .notranslate}]{.pre} flag,
the command gives the flags for a parallel build, which add
[`-DADIOS2_USE_MPI`{.docutils .literal .notranslate}]{.pre} to the
compilation flags and include extra libaries containing the MPI
implementations into the linker flags. The [`-s`{.docutils .literal
.notranslate}]{.pre} flag will omit these flags. For example, if ADIOS
is installed into /opt/adios2, the flags for a Fortran application will
look like these:

> <div>
>
> :::: {.highlight-bash .notranslate}
> ::: highlight
>     $ /opt/adios2/bin/adios2-config --fortran-flags
>     -DADIOS2_USE_MPI -I/opt/adios2/include/adios2/fortran
>     $ /opt/adios2/bin/adios2-config --fortran-flags -m
>     -DADIOS2_USE_MPI -I/opt/adios2/include/adios2/fortran
>     $ /opt/adios2/bin/adios2-config --fortran-flags -s
>     -I/opt/adios2/include/adios2/fortran
>
>     $ /opt/adios2/bin/adios2-config --fortran-libs
>     -Wl,-rpath,/opt/adios2/lib /opt/adios2/lib/libadios2_fortran_mpi.so.2.6.0 /opt/adios2/lib/libadios2_fortran.so.2.6.0 -Wl,-rpath-link,/opt/adios2/lib
>     $ /opt/adios2/bin/adios2-config --fortran-libs -s
>     -Wl,-rpath,/opt/adios2/lib /opt/adios2/lib/libadios2_fortran.so.2.6.0 -Wl,-rpath-link,/opt/adios2/lib
> :::
> ::::
>
> </div>

If using cmake, there are different targets to build parallel

> <div>
>
> :::: {.highlight-cmake .notranslate}
> ::: highlight
>     find_package(MPI REQUIRED)
>     find_package(ADIOS2 REQUIRED)
>     #...
>     add_library(my_library src1.cxx src2.cxx)
>     target_link_libraries(my_library PRIVATE adios2::cxx11_mpi MPI::MPI_CXX)
>     #...
>     add_library(my_f_library src1.F90 src2.F90)
>     target_link_libraries(my_f_library PRIVATE adios2::fortran_mpi adios2::fortran MPI::MPI_Fortran)
> :::
> ::::
>
> </div>

and serial applications:

> <div>
>
> :::: {.highlight-cmake .notranslate}
> ::: highlight
>     find_package(ADIOS2 REQUIRED)
>     #...
>     add_library(my_library src1.cxx src2.cxx)
>     target_link_libraries(my_library PRIVATE adios2::cxx11)
>     #...
>     add_library(my_f_library src1.F90 src2.F90)
>     target_link_libraries(my_f_library PRIVATE adios2::fortran)
> :::
> ::::
>
> </div>
:::

::: {#can-i-use-adios-2-c-11-library-with-c-98-codes .section}
#### Can I use ADIOS 2 C++11 library with C++98 codes?[](#can-i-use-adios-2-c-11-library-with-c-98-codes "Link to this heading"){.headerlink}

Use the [[C bindings]{.std
.std-ref}](#document-api_full/api_full#c-bindings){.reference
.internal}. C++11 is a brand new language standard and many new (and
old, *e.g.* [`std::string`{.docutils .literal .notranslate}]{.pre})
might cause ABI conflicts.
:::

::: {#why-are-c-and-fortran-apis-missing-functionality .section}
#### Why are C and Fortran APIs missing functionality?[](#why-are-c-and-fortran-apis-missing-functionality "Link to this heading"){.headerlink}

Because language intrinsics are NOT THE SAME. For example, C++ and
Python support key/value pair structures natively, *e.g.*
[`std::map`{.docutils .literal .notranslate}]{.pre} and dictionaries,
respectively. Fortran and C only support arrays natively. Use the right
language (tool) for the right task.
:::

::: {#c-11-why-are-std-string-arguments-passed-sometimes-by-value-and-sometimes-by-reference .section}
#### C++11: Why are std::string arguments passed sometimes by value and sometimes by reference?[](#c-11-why-are-std-string-arguments-passed-sometimes-by-value-and-sometimes-by-reference "Link to this heading"){.headerlink}

C++11, provides mechanisms to optimize copying small objects, rather
than passing by reference. The latter was always the rule for C++98.
When a string is passed by value, it's assumed that the name will be
short, \<= 15 characters, most of the time. While passing by reference
indicates that the string can be of any size. Check the [isocpp
guidelines on this
topic](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#f15-prefer-simple-and-conventional-ways-of-passing-information){.reference
.external} for more information.
:::

::: {#c-11-should-i-pass-adios2-objects-by-value-or-by-reference .section}
#### C++11: Should I pass adios2:: objects by value or by reference?[](#c-11-should-i-pass-adios2-objects-by-value-or-by-reference "Link to this heading"){.headerlink}

[`adios2::ADIOS`{.docutils .literal .notranslate}]{.pre}: always pass by
reference this is the only "large memory" object; all others: pass by
reference or value depending on your coding standards and requirements,
they are small objects that wrap around a pointer to an internal object
inside [`adios2::ADIOS`{.docutils .literal .notranslate}]{.pre}.
:::

::: {#fortran-can-i-pass-slices-and-temporary-arrays-to-adios2-put .section}
#### Fortran: Can I pass slices and temporary arrays to adios2_put?[](#fortran-can-i-pass-slices-and-temporary-arrays-to-adios2-put "Link to this heading"){.headerlink}

By definition the lifetime of a temporary is the scope of the function
is passed to. Therefore, you must use sync mode with
[`adios2_put`{.docutils .literal .notranslate}]{.pre}. Deferred mode
will save garbage data since the memory location of a temporary is
undefined after [`adios2_put`{.docutils .literal .notranslate}]{.pre},
not able to reach [`adios2_end_step`{.docutils .literal
.notranslate}]{.pre}, [`adios2_close`{.docutils .literal
.notranslate}]{.pre} or [`adios2_perform_puts`{.docutils .literal
.notranslate}]{.pre} where the memory is actually used.
:::

::: {#my-application-uses-pgi-compilers-on-titan-can-i-link-adios-2 .section}
#### My application uses PGI compilers on Titan, can I link ADIOS 2?[](#my-application-uses-pgi-compilers-on-titan-can-i-link-adios-2 "Link to this heading"){.headerlink}

Follow directions at [[Building on HPC Systems]{.std
.std-ref}](#document-setting_up/setting_up#building-on-hpc-systems){.reference
.internal} to setup support for PGI on Titan. PGI compilers depend on
GNU headers, but they must point to a version greater than gcc 4.8.1 to
support C++11 features. The gcc module doesn't need to be loaded,
though. Example:

> <div>
>
> :::: {.highlight-bash .notranslate}
> ::: highlight
>     $ module load gcc/7.2.0
>     $ makelocalrc $(dirname $(which pgc++)) -gcc $(which gcc) -gpp $(which g++) -g77 $(which gfortran) -o -net 1>${HOME}/.mypgirc 2>/dev/null
>     $ module unload gcc/7.2.0
> :::
> ::::
>
> </div>
:::

::: {#how-do-i-enable-the-python-bindings-on-titan .section}
#### How do I enable the Python bindings on Titan?[](#how-do-i-enable-the-python-bindings-on-titan "Link to this heading"){.headerlink}

The default ADIOS2 configuration on Titan builds a static library.
Python bindings require enabling the dynamic libraries and the Cray
dynamic environment variable. See [[Building on HPC Systems]{.std
.std-ref}](#document-setting_up/setting_up#building-on-hpc-systems){.reference
.internal} and [[Enabling the Python bindings]{.std
.std-ref}](#document-setting_up/setting_up#enabling-the-python-bindings){.reference
.internal}. For example:

> <div>
>
> :::: {.highlight-bash .notranslate}
> ::: highlight
>     [atkins3@titan-ext4 code]$ mkdir adios
>     [atkins3@titan-ext4 code]$ cd adios
>     [atkins3@titan-ext4 adios]$ git clone https://github.com/ornladios/adios2.git source
>     [atkins3@titan-ext4 adios]$ module swap PrgEnv-pgi PrgEnv-gnu
>     [atkins3@titan-ext4 adios]$ module load cmake3/3.11.3
>     [atkins3@titan-ext4 adios]$ module load python python_numpy python_mpi4py
>     [atkins3@titan-ext4 adios]$ export CRAYPE_LINK_TYPE=dynamic CC=cc CXX=CC FC=ftn
>     [atkins3@titan-ext4 adios]$ mkdir build
>     [atkins3@titan-ext4 build]$ cd build
>     [atkins3@titan-ext4 build]$ cmake ../source
>     -- The C compiler identification is GNU 6.3.0
>     -- The CXX compiler identification is GNU 6.3.0
>     -- Cray Programming Environment 2.5.13 C
>     -- Check for working C compiler: /opt/cray/craype/2.5.13/bin/cc
>     -- Check for working C compiler: /opt/cray/craype/2.5.13/bin/cc -- works
>     -- Detecting C compiler ABI info
>     -- Detecting C compiler ABI info - done
>     -- Detecting C compile features
>     -- Detecting C compile features - done
>     -- Cray Programming Environment 2.5.13 CXX
>     -- Check for working CXX compiler: /opt/cray/craype/2.5.13/bin/CC
>     -- Check for working CXX compiler: /opt/cray/craype/2.5.13/bin/CC -- works
>     ...
>     -- Found PythonInterp: /sw/titan/.swci/0-login/opt/spack/20180315/linux-suse_linux11-x86_64/gcc-4.3.4/python-2.7.9-v6ctjewwdx6k2qs7ublexz7gnx457jo5/bin/python2.7 (found version "2.7.9")
>     -- Found PythonLibs: /sw/titan/.swci/0-login/opt/spack/20180315/linux-suse_linux11-x86_64/gcc-4.3.4/python-2.7.9-v6ctjewwdx6k2qs7ublexz7gnx457jo5/lib/libpython2.7.so (found version "2.7.9")
>     -- Found PythonModule_numpy: /sw/xk6/python_numpy/1.7.1/python2.7.9_craylibsci_gnu4.9.0/lib64/python2.7/site-packages/numpy
>     -- Found PythonModule_mpi4py: /lustre/atlas/sw/xk7/python_mpi4py/2.0.0/cle5.2up04_python2.7.9/lib64/python2.7/site-packages/mpi4py
>     -- Found PythonFull: /sw/titan/.swci/0-login/opt/spack/20180315/linux-suse_linux11-x86_64/gcc-4.3.4/python-2.7.9-v6ctjewwdx6k2qs7ublexz7gnx457jo5/bin/python2.7  found components:  Interp Libs numpy mpi4py
>     ...
>     ADIOS2 build configuration:
>       ADIOS Version: 2.4.0
>       C++ Compiler : GNU 6.3.0 CrayPrgEnv
>         /opt/cray/craype/2.5.13/bin/CC
>
>       Fortran Compiler : GNU 6.3.0 CrayPrgEnv
>         /opt/cray/craype/2.5.13/bin/ftn
>
>       Installation prefix: /usr/local
>             bin: bin
>             lib: lib
>         include: include
>           cmake: lib/cmake/adios2
>          python: lib/python2.7/site-packages
>
>       Features:
>         Library Type: shared
>         Build Type:   Release
>         Testing: ON
>         Build Options:
>           BZip2    : ON
>           ZFP      : OFF
>           SZ       : OFF
>           MGARD    : OFF
>           MPI      : ON
>           DataMan  : ON
>           SST      : ON
>           ZeroMQ   : OFF
>           HDF5     : OFF
>           Python   : ON
>           Fortran  : ON
>           SysVShMem: ON
>           Endian_Reverse: OFF
>
>     -- Configuring done
>     -- Generating done
>     -- Build files have been written to: /ccs/home/atkins3/code/adios/build
> :::
> ::::
>
> </div>
:::

::: {#how-do-i-build-adios-2-on-fujitsu-fx100 .section}
#### How do I build ADIOS 2 on Fujitsu FX100?[](#how-do-i-build-adios-2-on-fujitsu-fx100 "Link to this heading"){.headerlink}

- Cross-compilation (building on the login node) is not recommended.
  Submit an interactive job and build on the compute nodes.

- Make sure CMake \>= 3.6 is installed on the compute nodes. If not, you
  need to build and install it from source since CMake does not provide
  SPARC V9 binaries.

- Use gcc instead of the Fujitsu compiler. We tested with gcc 6.3.0

- CMake fails to automatically find the correct MPI library on FX100. As
  a workaround, set CC, CXX, and FC to the corresponding MPI compiler
  wrappers:

  > <div>
  >
  > :::: {.highlight-bash .notranslate}
  > ::: highlight
  >     $ CC=mpigcc CXX=mpig++ FC=mpigfortran cmake  ..
  > :::
  > ::::
  >
  > </div>
:::

::: {#sst-engine-hangs-on-fujitsu-fx100-why .section}
#### SST engine hangs on Fujitsu FX100. Why?[](#sst-engine-hangs-on-fujitsu-fx100-why "Link to this heading"){.headerlink}

The communication thread of SST might have failed to start. FX100
requires users to set the maximum stack size manually when launching
POSIX threads. One way to do this is through ulimit (*e.g.*
[`ulimit`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`-s`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`1024`{.docutils .literal .notranslate}]{.pre}).
You can also set the stack size when submitting the job. Please contact
your system administrator for details.
:::
:::::::::::::
::::::::::::::::::

[]{#document-advice/advice}

::: {#advice .section}
## Advice[](#advice "Link to this heading"){.headerlink}

This list is similar to the Advice sections for each chapter in [The C++
Programming Language, Fourth Edition by Bjarne
Stroustrup](http://www.stroustrup.com/4th.html){.reference .external}
The goal is to provide specific advice and good practices about the use
of ADIOS2 in other projects.

1.  Use [`MPI_COMM_SELF`{.docutils .literal .notranslate}]{.pre} to run
    MPI compiled versions of ADIOS 2 in "serial" mode

2.  Use a runtime configuration file in the [`ADIOS`{.docutils .literal
    .notranslate}]{.pre} constructor or [`adios2_init`{.docutils
    .literal .notranslate}]{.pre} when targeting multiple engines

3.  Check object validity when developing (similar to
    [`fstream`{.docutils .literal .notranslate}]{.pre}):

    - C++: operator bool

      > <div>
      >
      > :::: {.highlight-c++ .notranslate}
      > ::: highlight
      >     if(var) engine.Put(var, data);
      > :::
      > ::::
      >
      > </div>

    - C: NULL pointer

      > <div>
      >
      > :::: {.highlight-c .notranslate}
      > ::: highlight
      >     if(var) adios2_put(engine, var, data, adios2_mode_deferred);
      > :::
      > ::::
      >
      > </div>

    - 

      Python: v2 [`__nonzero__`{.docutils .literal .notranslate}]{.pre} v3 [`__bool__`{.docutils .literal .notranslate}]{.pre}. Note: do not check for None object

      :   :::: {.highlight-python .notranslate}
          ::: highlight
              if(var) engine.Put(var, data);
          :::
          ::::

    - Fortran: [`type%valid`{.docutils .literal .notranslate}]{.pre}

      > <div>
      >
      > :::: {.highlight-fortran .notranslate}
      > ::: highlight
      >     if( adios%valid .eqv. .true. ) then
      >        adios2_declare_io(adios, io, "foo")
      >     end if
      > :::
      > ::::
      >
      > </div>

4.  C++11 and Python: use [`try-catch`{.docutils .literal
    .notranslate}]{.pre} ([`try-except`{.docutils .literal
    .notranslate}]{.pre} in Python) blocks to handle exceptions from
    ADIOS 2

5.  C++11: use fixed-width types ([`int8_t`{.docutils .literal
    .notranslate}]{.pre}, [`uint32_t`{.docutils .literal
    .notranslate}]{.pre}) for portability

6.  Define your data structure: set of variables and attributes before
    developing. Data hierarchies/models can be built on top of ADIOS 2.

7.  Read the documentation for [[Supported Engines]{.std
    .std-ref}](#document-engines/engines#supported-engines){.reference
    .internal} before targeting development for a particular engine

8.  MPI development: treat [`ADIOS`{.docutils .literal
    .notranslate}]{.pre} constructor/destructor
    ([`adios2_init`{.docutils .literal
    .notranslate}]{.pre}/[`adios2_finalize`{.docutils .literal
    .notranslate}]{.pre}) and Engine [`Open`{.docutils .literal
    .notranslate}]{.pre} and [`Close`{.docutils .literal
    .notranslate}]{.pre} always as collective functions. For the most
    part, ADIOS 2 API functionality is local, but other Engine functions
    might follow other rules, [[Supported Engines]{.std
    .std-ref}](#document-engines/engines#supported-engines){.reference
    .internal}.

9.  Use Remove functions carefully. They create dangling
    objects/pointers.

10. Thread-safety: treat ADIOS 2 as NOT thread-safe. Either use a mutex
    or only handle I/O from a master thread. ADIOS 2 is about
    performance, adding I/O serial algorithm operations into a parallel
    execution block may reduce parallel portions from Amdahl's Law.

11. Prefer the high-level Python and C++ APIs for simple tasks that do
    not require performance. The more familiar Write/Read overloads for
    File I/O return native data constructs ([`std::vector`{.docutils
    .literal .notranslate}]{.pre} and [`numpy`{.docutils .literal
    .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`arrays`{.docutils .literal .notranslate}]{.pre})
    immediately for a requested selection. [`open`{.docutils .literal
    .notranslate}]{.pre} only explores the metadata index.

12. C++: prefer templates to [`void*`{.docutils .literal
    .notranslate}]{.pre} to increase compile-time safety. Use
    [`IO::InquireVariableType("variableName")`{.docutils .literal
    .notranslate}]{.pre} and [`adios2::GetType<T>()`{.docutils .literal
    .notranslate}]{.pre} to cast upfront to a [`Variable<T>`{.docutils
    .literal .notranslate}]{.pre}. C++17 has [`std::any`{.docutils
    .literal .notranslate}]{.pre} as an alternative to
    [`void*`{.docutils .literal .notranslate}]{.pre}. ADIOS 2 follows
    closely the STL model.

13. Understand [`Put`{.docutils .literal .notranslate}]{.pre} and
    [`Get`{.docutils .literal .notranslate}]{.pre} memory contracts from
    [[Engine]{.std
    .std-ref}](#document-components/components#engine){.reference
    .internal}

14. Prefer Put/Get [`Deferred`{.docutils .literal .notranslate}]{.pre}
    mode, treat [`Sync`{.docutils .literal .notranslate}]{.pre} as a
    special mode

15. [`Put`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
    .notranslate}[`Span`{.docutils .literal .notranslate}]{.pre}: create
    all spans in a step before populating them. Spans follow the same
    iterator invalidation rules as [`std::vector`{.docutils .literal
    .notranslate}]{.pre}, so use [`span.data()`{.docutils .literal
    .notranslate}]{.pre} to always keep the span pointer up-to-date

16. Always populate data before calling [`Put`{.docutils .literal
    .notranslate}]{.pre} in deferred mode, and do not change it between
    [`Put`{.docutils .literal .notranslate}]{.pre} and
    [`EndStep`{.docutils .literal .notranslate}]{.pre}, or
    [`Close`{.docutils .literal .notranslate}]{.pre}

17. Never call [`PerformPuts`{.docutils .literal .notranslate}]{.pre}
    right before [`EndStep`{.docutils .literal .notranslate}]{.pre}.
    This was a code pattern that had no adverse effects with the BP3/4
    file engines and is present in some older code, but was never
    beneficial.

18. Use [`BeginStep`{.docutils .literal .notranslate}]{.pre} and
    [`EndStep`{.docutils .literal .notranslate}]{.pre} to write code
    that is portable across all ADIOS 2 Engine types: file and
    streaming.

19. Always use [`Close`{.docutils .literal .notranslate}]{.pre} for
    every call to [`Open`{.docutils .literal .notranslate}]{.pre}.

20. C, Fortran: always call [`adios2_finalize`{.docutils .literal
    .notranslate}]{.pre} for every call to [`adios2_init`{.docutils
    .literal .notranslate}]{.pre} to avoid memory leaks.

21. Reminder: C++, C, Python: Row-Major, while Fortran: Column-Major.
    ADIOS 2 will handle interoperability between ordering. Remember that
    [[bpls : Inspecting Data]{.std
    .std-ref}](#document-ecosystem/utilities#bpls-inspecting-data){.reference
    .internal} is always a Row-Major reader so Fortran reader need to
    swap dimensions seen in bpls. bpls: (slow, ...., fast) -\>
    Fortran(fast,...,slow).

22. Fortran API: use the type members ([`var%valid`{.docutils .literal
    .notranslate}]{.pre}, [`var%name`{.docutils .literal
    .notranslate}]{.pre}, etc.) to get extra type information.

23. Fortran C interoperability: Fortran bindings support the majority of
    applications using Fortran 90. We currently don't support the
    [`ISO_C_BINDING`{.docutils .literal .notranslate}]{.pre}
    interoperability module in Fortran 2003.

24. Always keep the [`IO`{.docutils .literal .notranslate}]{.pre} object
    self-contained keeping its own set of [`Variables`{.docutils
    .literal .notranslate}]{.pre}, [`Attributes`{.docutils .literal
    .notranslate}]{.pre} and [`Engines`{.docutils .literal
    .notranslate}]{.pre}. Do not combine Variables with multiple Engines
    or multiple modes, unless it's 100% guaranteed to be safe in your
    program avoiding Variable access conflicts.

25. Developers: explore the testing infrastructure
    [`ADIOS2/testing`{.docutils .literal .notranslate}]{.pre} in ADIOS 2
    as a starting point for using ADIOS 2 in your own testing
    environment.

26. Become a super-user of [[bpls : Inspecting Data]{.std
    .std-ref}](#document-ecosystem/utilities#bpls-inspecting-data){.reference
    .internal} to analyze datasets generated by ADIOS 2.
:::
::::::::::::::::::::

- [[Search Page]{.std .std-ref}](search.html){.reference .internal}
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
