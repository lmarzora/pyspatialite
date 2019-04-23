cmake_minimum_required(VERSION 2.8)

project(pyspatialite)
include(FeatureSummary)
include(FindPythonLibs)

set(CMAKE_INSTALL_PREFIX, "${CMAKE_CURRENT_BINARY_DIR}/../deployment" CACHE INTERNAL "Default installation path")

option(USE_PROJ4 "Compile with PROJ4 support" TRUE)
option(USE_GEOS "Compile with GEOS support" TRUE)
option(USE_GEOS_ADVANCED "Compile with GEOS advanced features" TRUE)
option(USE_ICONV "Compile with iconv support" TRUE)
option(USE_FREEXL "Compile with freexl suppport" FALSE)
option(USE_SPATIALITE_INIT_EXE "use spatialite_init_ex() instead of deprecated spatialite_init() method" FALSE)

set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake/Modules)

include_directories(${pyspatialite_source_dir})

add_subdirectory(src)