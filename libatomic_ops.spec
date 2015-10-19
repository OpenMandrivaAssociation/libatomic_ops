%define _disable_ld_no_undefined 1
#define debug_package	%nil

%define sname	atomic_ops
%define major	1
%define libname	%mklibname %{sname} %{major} 
%define libgpl	%mklibname %{sname}_gpl %{major} 
%define devname %mklibname -d %{sname}

Summary:	Multiplatform atomic memory operation library
Name:		libatomic_ops
Version:	7.4.2
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		http://www.hboehm.info/gc/
Source0:	http://www.ivmaisoft.com/_bin/atomic_ops/%{name}-%{version}.tar.gz

%description
Multiplatform atomic memory operation library

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
Provides:	%{name}-devel = %{version}
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
shared data structures from signal handlers. For details, see README.txt in
the distribution.

%prep
%setup -qn %{name}-%{version}
%apply_patches

%build
autoreconf -fi
%configure2_5x \
	--disable-static \
	--enable-shared
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libatomic_ops.so.%{major}*

%files -n %{libgpl}
%{_libdir}/libatomic_ops_gpl.so.%{major}*

%files -n  %{devname}
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
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

