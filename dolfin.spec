Name:           dolfin
Version:        1.6.0
Release:        3.4
Summary:        An open source CFD software
License:        LGPL-3.0
Group:          Development/Libraries/C and C++
Url:            http://fenicsproject.org/
Source0:        %{name}-%{version}.tar.gz
Patch0:         dolfin-1.1.0-suitesparse.patch
BuildRequires:  Modules
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  eigen3-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  arpack-devel
BuildRequires:  parpack-openmpi-devel
BuildRequires:  hdf5-openmpi-devel
BuildRequires:  java-devel
BuildRequires:  lapack-devel
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  freetype2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libqt4-devel
BuildRequires:  libxml2-devel
BuildRequires:  openmpi-devel
BuildRequires:  pastix-openmpi-devel
BuildRequires:  petsc-openmpi-devel
BuildRequires:  pkg-config
BuildRequires:  ptscotch-openmpi-devel
BuildRequires:  libptscotch-parmetis-openmpi-devel
BuildRequires:  trlan-devel
BuildRequires:  python-FFC = %{version}
BuildRequires:  python-FIAT = %{version}
BuildRequires:  python-sympy
BuildRequires:  python-Sphinx
BuildRequires:  python-devel
BuildRequires:  python-instant = %{version}
BuildRequires:  python-numpy-devel
BuildRequires:  python-ply
BuildRequires:  python-ufl = %{version}
BuildRequires:  python-uflacs = %{version}
BuildRequires:  python-viper
BuildRequires:  scotch-devel
BuildRequires:  slepc-openmpi-devel
BuildRequires:  suitesparse-devel
BuildRequires:  swig >= 3.0
BuildRequires:  texlive-latex
BuildRequires:  ufc-devel
BuildRequires:  vtk-devel

%description
dolphin is an open source CFD software (FLOW solvER, literally)
written in C++. It is mainly devoted to the resolution of the
turbulent unsteady incompressible Navier-Stokes equations. 

%package openmpi
Summary:        Development and header files for %{name}
Group:          Development/Libraries/C and C++
Requires:       openmpi
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description openmpi
dolphin is an open source CFD software (FLOW solvER, literally)
written in C++. It is mainly devoted to the resolution of the
turbulent unsteady incompressible Navier-Stokes equations.

This package contains the dolfin binaries build with openmpi support.

%package openmpi-devel
Summary:        Development and header files for %{name}
Group:          Development/Libraries/C and C++
Provides:       pkgconfig(DOLFIN)
Requires:       boost-devel
Requires:       cmake
Requires:       cppunit-devel
Requires:       eigen3-devel
Requires:       lapack-devel
Requires:       libdolfin1_6-openmpi = %{version}
Requires:       libxml2-devel
Requires:       openmpi-devel
Requires:       pastix-openmpi-devel
Requires:       petsc-openmpi-devel
Requires:       ptscotch-openmpi-devel
Requires:       suitesparse-devel
Requires:       ufc-devel
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}

%description openmpi-devel
The %{name}-openmpi-devel package contains header files for developing
applications that use %{name}-openmpi.

%package -n libdolfin1_6-openmpi
Summary:        A package for solving large sparse systems of linear equations
Group:          System/Libraries
Provides:       libdolfin1_6 = %{version}
Obsoletes:      libdolfin1_6 < %{version}
Obsoletes:      libdolfin1_5 < %{version}
Obsoletes:      libdolfin1_4 < %{version}
Obsoletes:      libdolfin1_3 < %{version}

%description -n libdolfin1_6-openmpi
dolphin is an open source CFD software (FLOW solvER, literally)
written in C++. It is mainly devoted to the resolution of the
turbulent unsteady incompressible Navier-Stokes equations. 

%package -n python-dolfin_utils-openmpi
Summary:        A package for solving large sparse systems of linear equations
Group:          Development/Languages/Python
Provides:       python-dolfin_utils = %{version}
Obsoletes:      python-dolfin_utils < %{version}

%description -n python-dolfin_utils-openmpi
dolphin is an open source CFD software (FLOW solvER, literally)
written in C++. It is mainly devoted to the resolution of the
turbulent unsteady incompressible Navier-Stokes equations. 

%package -n python-dolfin-openmpi
Summary:        A package for solving large sparse systems of linear equations
Group:          Development/Languages/Python
Requires:       dolfin-openmpi-devel = %{version}
Requires:       python-FFC = %{version}
Requires:       python-FIAT = %{version}
Requires:       python-sympy
Requires:       python-dolfin_utils-openmpi
Requires:       python-instant = %{version}
Requires:       python-ply
Requires:       python-ufl = %{version}
Requires:       python-viper
Provides:       python-dolfin = %{version}
Obsoletes:      python-dolfin < %{version}

%description -n python-dolfin-openmpi
dolphin is an open source CFD software (FLOW solvER, literally)
written in C++. It is mainly devoted to the resolution of the
turbulent unsteady incompressible Navier-Stokes equations. 

This package contains the python-dolfin module build with openmpi support.

%package doc
Summary:        Documentation files for %{name}
Group:          Documentation/HTML

%description doc
The %{name}-doc package contains documentation files for developing
applications that use %{name}.


%prep
%setup -q
%patch0 -p1
mkdir openmpi

%build
export CXXFLAGS="%{optflags} -fpermissive"
%define slepc_ver %(rpm -q slepc-openmpi-devel --queryformat %%{VERSION})
%define petsc_ver %(rpm -q petsc-openmpi-devel --queryformat %%{VERSION})

cd openmpi
cmake  -DCMAKE_INSTALL_PREFIX=%{_libdir}/mpi/gcc/openmpi \
       -DDOLFIN_LIB_DIR:PATH="%_lib" \
       -DDOLFIN_PKGCONFIG_DIR:PATH="%_lib/pkgconfig" \
       -DDOLFIN_ENABLE_MPI:BOOL=ON \
       -DDOLFIN_ENABLE_PARMETIS:BOOL=OFF \
       -DDOLFIN_ENABLE_PASTIX:BOOL=ON \
       -DDOLFIN_ENABLE_SCOTCH:BOOL=ON \
       -DDOLFIN_ENABLE_TRILINOS:BOOL=OFF \
       -DDOLFIN_ENABLE_QT:BOOL=OFF \
       -DHDF5_C_COMPILER_EXECUTABLE=%{_libdir}/mpi/gcc/openmpi/bin/h5pcc \
       -DHDF5_CXX_COMPILER_EXECUTABLE=%{_libdir}/mpi/gcc/openmpi/bin/h5pcc \
       -DHDF5_Fortran_COMPILER_EXECUTABLE=%{_libdir}/mpi/gcc/openmpi/bin/h5pfc \
       -DHDF5_DIFF_EXECUTABLE=%{_libdir}/mpi/gcc/openmpi/bin/h5diff \
       -DSCOTCH_LIBRARY=%{_libdir}/mpi/gcc/openmpi/%_lib/libscotch.so \
       -DSCOTCH_INCLUDE_DIRS=%{_libdir}/mpi/gcc/openmpi/include \
       -DPTSCOTCHERR_LIBRARY=%{_libdir}/mpi/gcc/openmpi/%_lib/libptscotcherr.so \
       -DPTSCOTCH_LIBRARY=%{_libdir}/mpi/gcc/openmpi/%_lib/libptscotch.so \
       -DPARMETIS_DIR=%{_libdir}/mpi/gcc/openmpi \
       -DPARMETIS_LIBRARY=%{_libdir}/mpi/gcc/openmpi/%_lib/libparmetis.so \
       -DPETSC_DIR=%{_libdir}/mpi/gcc/openmpi/%_lib/petsc/%{petsc_ver}/linux-gnu-c-opt \
       -DSLEPC_DIR=%{_libdir}/mpi/gcc/openmpi/%_lib/slepc/%{slepc_ver}/linux-gnu-c-opt \
       -DARPACK_LIB="%{_libdir}/mpi/gcc/openmpi/%_lib/libparpack.so;%{_libdir}/libarpack.so" \
       -DDOLFIN_SKIP_BUILD_TESTS:BOOL=ON \
       ..
make -j1


%install
cd openmpi
make install DESTDIR=%{buildroot}
# remove RPM_BUILD_ROOT in some .pyc files
pushd %{buildroot}%{_libdir}/mpi/gcc/openmpi/lib/python%{py_ver}/site-packages/dolfin_utils
%py_compile .
popd
pushd %{buildroot}%{_libdir}/mpi/gcc/openmpi/%_lib/python%{py_ver}/site-packages/dolfin
%py_compile .
popd

%fdupes -s %{buildroot}%{_libdir}/mpi/gcc/openmpi/share/%{name}

export PYTHONPATH=%{buildroot}%{_libdir}/mpi/gcc/openmpi/lib/python%{py_ver}/site-packages:%{buildroot}%{_libdir}/mpi/gcc/openmpi/%_lib/python%{py_ver}/site-packages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}/mpi/gcc/openmpi/%{_lib}:%{_libdir}/mpi/gcc/openmpi/%{_lib}
python -c "import dolfin"
make doc
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -ar doc/sphinx-cpp/build/html %{buildroot}%{_docdir}/%{name}/cpp-html
cp -ar doc/sphinx-python/build/html %{buildroot}%{_docdir}/%{name}/python-html

%fdupes -s %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_docdir}/%{name}
cd ..

%post -n libdolfin1_6-openmpi -p /sbin/ldconfig

%postun -n libdolfin1_6-openmpi -p /sbin/ldconfig

%files openmpi
%{_libdir}/mpi/gcc/openmpi/bin/*
%{_libdir}/mpi/gcc/openmpi/share/man/man1/*

%files -n python-dolfin_utils-openmpi
%ifarch ia64 x86_64 ppc64
%dir %{_libdir}/mpi/gcc/openmpi/lib
%endif
%dir %{_libdir}/mpi/gcc/openmpi/lib/python%{py_ver}
%dir %{_libdir}/mpi/gcc/openmpi/lib/python%{py_ver}/site-packages
%{_libdir}/mpi/gcc/openmpi/lib/python%{py_ver}/site-packages/dolfin_utils

%files -n python-dolfin-openmpi
%dir %{_libdir}/mpi/gcc/openmpi/%_lib/python%{py_ver}
%dir %{_libdir}/mpi/gcc/openmpi/%_lib/python%{py_ver}/site-packages
%{_libdir}/mpi/gcc/openmpi/%_lib/python%{py_ver}/site-packages/dolfin
%{_libdir}/mpi/gcc/openmpi/%_lib/python%{py_ver}/site-packages/fenics

%files -n libdolfin1_6-openmpi
%doc AUTHORS ChangeLog COPYING COPYING.LESSER README.rst
%{_libdir}/mpi/gcc/openmpi/%_lib/*.so.*

%files openmpi-devel
%dir %{_libdir}/mpi/gcc/openmpi/lib
%dir %{_libdir}/mpi/gcc/openmpi/%_lib/pkgconfig
%{_libdir}/mpi/gcc/openmpi/include/*
%{_libdir}/mpi/gcc/openmpi/%_lib/*.so
%{_libdir}/mpi/gcc/openmpi/share/%{name}
%{_libdir}/mpi/gcc/openmpi/%_lib/pkgconfig/*.pc

%files doc
%{_docdir}/%{name}

%changelog
* Fri Tue Nov  6 2015 Alves Adrian <alvesadrian@fedoraproject.org> 1.6.0-1
- Initial build
