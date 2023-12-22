# libatomic_ops is used by libdrm, libdrm is used by wine and steam
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define _disable_ld_no_undefined 1

%define sname atomic_ops
%define major 1
%define libname %mklibname %{sname} %{major}
%define libgpl %mklibname %{sname}_gpl %{major}
%define devname %mklibname -d %{sname}
%define lib32name lib%{sname}%{major}
%define lib32gpl lib%{sname}_gpl%{major}
%define dev32name lib%{sname}-devel

Summary:	Multiplatform atomic memory operation library
Name:		libatomic_ops
Version:	7.8.2
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		https://github.com/ivmai/libatomic_ops
Source0:	https://github.com/ivmai/libatomic_ops/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
%if %{with compat32}
BuildRequires:	libc6
%endif

%description
Multiplatform atomic memory operation library.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{libgpl}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libgpl}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Multiplatform atomic memory operation library
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libgpl} = %{version}-%{release}

%description -n  %{devname}
Provides implementations for atomic memory update operations on a number of
architectures. This allows direct use of these in reasonably portable code.
Unlike earlier similar packages, this one explicitly considers memory barrier
semantics, and allows the construction of code that involves minimum overhead
across a variety of architectures.

It should be useful both for high performance multi-threaded code which can't
afford to use the standard locking primitives, or for code that has to access
shared data structures from signal handlers. For details, see README.md in
the distribution.

%if %{with compat32}
%package -n %{lib32name}
Summary:	Shared library for %{name} (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
This package contains the shared library for %{name}.

%package -n %{lib32gpl}
Summary:	Shared library for %{name} (32-bit)
Group:		System/Libraries

%description -n %{lib32gpl}
This package contains the shared library for %{name}.

%package -n %{dev32name}
Summary:	Multiplatform atomic memory operation library (32-bit)
Group:		System/Libraries
Provides:	%{name}-devel = %{version}
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{lib32gpl} = %{version}-%{release}

%description -n  %{dev32name}
Provides implementations for atomic memory update operations on a number of
architectures. This allows direct use of these in reasonably portable code.
Unlike earlier similar packages, this one explicitly considers memory barrier
semantics, and allows the construction of code that involves minimum overhead
across a variety of architectures.

It should be useful both for high performance multi-threaded code which can't
afford to use the standard locking primitives, or for code that has to access
shared data structures from signal handlers. For details, see README.md in
the distribution.
%endif

%prep
%autosetup -p1

%build
%if %{with compat32}
%cmake32 \
	-DBUILD_SHARED_LIBS=ON \
	-Denable_atomic_intrinsics=OFF \
	-G Ninja

%ninja_build
cd ..
%endif

%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-Denable_atomic_intrinsics=OFF \
	-G Ninja

%ninja_build

%install
%if %{with compat32}
%ninja_install -C build32
%endif
%ninja_install -C build

rm -rf %{buildroot}%{_docdir}/%{name}

%files -n %{libname}
%{_libdir}/libatomic_ops.so.%{major}*

%files -n %{libgpl}
%{_libdir}/libatomic_ops_gpl.so.%{major}*

%files -n  %{devname}
%doc COPYING LICENSE README.md
%{_includedir}/*.h
%dir %{_includedir}/%{sname}
%{_includedir}/%{sname}/*.h
%dir %{_includedir}/%{sname}/sysdeps
%{_includedir}/%{sname}/sysdeps/*.h
%dir %{_includedir}/%{sname}/sysdeps/gcc
%{_includedir}/%{sname}/sysdeps/gcc/*.h
%dir %{_includedir}/%{sname}/sysdeps/hpc
%{_includedir}/%{sname}/sysdeps/hpc/*.h
%dir %{_includedir}/%{sname}/sysdeps/ibmc
%{_includedir}/%{sname}/sysdeps/ibmc/*.h
%dir %{_includedir}/%{sname}/sysdeps/icc
%{_includedir}/%{sname}/sysdeps/icc/*.h
%dir %{_includedir}/%{sname}/sysdeps/msftc
%{_includedir}/%{sname}/sysdeps/msftc/*.h
%dir %{_includedir}/%{sname}/sysdeps/sunc
%{_includedir}/%{sname}/sysdeps/sunc/*.h
%dir %{_includedir}/%{sname}/sysdeps/armcc
%{_includedir}/%{sname}/sysdeps/armcc/*.h
%dir %{_includedir}/%{sname}/sysdeps/loadstore
%{_includedir}/%{sname}/sysdeps/loadstore/*.h
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%dir %{_libdir}/cmake/%{sname}
%{_libdir}/cmake/%{sname}/*.cmake

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libatomic_ops.so.%{major}*

%files -n %{lib32gpl}
%{_prefix}/lib/libatomic_ops_gpl.so.%{major}*

%files -n  %{dev32name}
%{_prefix}/lib/*.so
%{_prefix}/lib/pkgconfig/*
%dir %{_prefix}/lib/cmake/%{sname}
%{_prefix}/lib/cmake/%{sname}/*.cmake
%endif
