set(pyspatialite_sources
    cache.c
    connection.c
    cursor.c
    microprotocols.c
    module.c
    prepare_protocol.c
    row.c
    statement.c
    util.c
    )

set(binaries_directories ${PYSPATIALITE_BINARY_DIRECTORIES})

# iconv
if (USE_ICONV)
    find_package(ICONV REQUIRED)
    set_package_properties(ICONV PROPERTIES
        DESCRIPTION "String conversion library"
        URL "http://www.gnu.org/software/libiconv/"
        TYPE REQUIRED
        PURPOSE "Required for text conversions (also dependency for some libraries).")
    include_directories(${ICONV_INCLUDE_DIR})
    list(APPEND pyspatialite_libraries ${ICONV_LIBRARY})
    get_filename_component(iconv_binary_directories ${ICONV_INCLUDE_DIR}/../bin ABSOLUTE)
    list(APPEND binary_directories ${iconv_binary_directories})
endif (USE_ICONV)

# proj.4
if (USE_PROJ4)
    find_package(Proj REQUIRED)
    set_package_properties(Proj PROPERTIES
        DESCRIPTION "Cartographic Projections library"
        URL "https://trac.osgeo.org/proj/"
        TYPE REQUIRED
        PURPOSE "Required for all projection transformations.")
    include_directories(${PROJ_INCLUDE_DIR})
    list(APPEND pyspatialite_libraries ${PROJ_LIBRARY})
    get_filename_component(proj_binary_directories ${PROJ_INCLUDE_DIR}/../bin ABSOLUTE)
    list(APPEND binary_directories ${proj_binary_directories})
endif (USE_PROJ4)

find_package(Sqlite3 REQUIRED)
set_package_properties(Sqlite3 PROPERTIES
    DESCRIPTION "Software library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine."
    URL "http://www.sqlite.org/"
    TYPE REQUIRED
    PURPOSE "Enables queries from SQLite databases.")

include_directories(${SQLITE3_INCLUDE_DIR})
list(APPEND pyspatialite_libraries ${SQLITE3_LIBRARY})
get_filename_component(sqlite3_binary_directories ${SQLITE3_LIBRARY}/../../bin ABSOLUTE)
list(APPEND binary_directories ${sqlite3_binary_directories})

find_package(SPATIALITE REQUIRED)
set_package_properties(SPATIALITE PROPERTIES
    DESCRIPTION "Library extending the basic SQLite core in order to get a full fledged Spatial DBMS, really simple and lightweight, but mostly OGC-SFS compliant."
    URL "http://www.gaia-gis.it/gaia-sins/"
    TYPE RECOMMENDED
    PURPOSE "Enables spatial queries from SQLite databases.")

if (SPATIALITE_FOUND)
    include_directories(${SPATIALITE_INCLUDE_DIR})
    list(APPEND pyspatialite_libraries ${SPATIALITE_LIBRARY})
    get_filename_component(spatialite_binary_directories ${SPATIALITE_LIBRARY}/../../bin ABSOLUTE)
    list(APPEND binary_directories ${spatialite_binary_directories})
endif (SPATIALITE_FOUND)

#Python
if (PYTHONLIBS_FOUND)
    include_directories(${PYTHON_INCLUDE_DIRS})
    list(APPEND pyspatialite_libraries ${PYTHON_LIBRARIES})
else()
    message( FATAL_ERROR "PYTHON was not found" )
endif(PYTHONLIBS_FOUND)

add_definitions(-DNDEBUG=1 -DSQLITE_ENABLE_RTREE=1 -DMODULE_NAME="spatialite.dbapi2" -DVERSION="0.1")

# Create the pyspatialite library
add_library(pyspatialite SHARED ${pyspatialite_sources})

target_link_libraries(pyspatialite ${pyspatialite_libraries})

install(TARGETS pyspatialite RUNTIME DESTINATION "bin/${CMAKE_BUILD_TYPE}")
install(TARGETS pyspatialite ARCHIVE DESTINATION "lib/MSVC/${CMAKE_BUILD_TYPE}")

install(
    FILES ${CMAKE_INSTALL_PREFIX}/bin/${CMAKE_BUILD_TYPE}/pyspatialite${CMAKE_SHARED_LIBRARY_SUFFIX}
    DESTINATION "bin/${CMAKE_BUILD_TYPE}"
    RENAME _spatialite.pyd)

set(PYSPATIALITE_BINARY_DIRECTORIES ${binary_directories} ${CMAKE_CURRENT_BINARY_DIR} PARENT_SCOPE)