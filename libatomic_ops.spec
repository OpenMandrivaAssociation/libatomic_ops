#define snapshot_vendor  ivmai
#define snapshot         81be636
#define snapshot_version 7_2alpha6-128
%define debug_package	%nil

%define rawname atomic_ops
# Can't use mklibname as the name should be the same on all arches
%define libname lib%{rawname}
%define libname_devel %mklibname -d %{rawname}

%define prever alpha2

Name:      %{libname}
Version:   7.3
Release:   %mkrel 0.%{prever}.1
Summary:   Multiplatform atomic memory operation library
License:   MIT/GPL
Group:     System/Libraries
Source0:   http://www.hpl.hp.com/personal/Hans_Boehm/gc/gc_source/%{name}-%{version}%{prever}.tar.gz
URL:       http://www.hpl.hp.com/research/linux/atomic_ops/
Patch0:    libatomic_ops-automake-1.13.patch

%description
Multiplatform atomic memory operation library


%package -n %{libname_devel}
Summary:   Multiplatform atomic memory operation library
Group:     System/Libraries
# Cross-arch provides
Provides:  %{libname}-devel = %{version}

%description -n  %{libname_devel}
Provides implementations for atomic memory update operations on a number of
architectures. This allows direct use of these in reasonably portable code.
Unlike earlier similar packages, this one explicitly considers memory barrier
semantics, and allows the construction of code that involves minimum overhead
across a variety of architectures.

The package has been at least minimally tested on X86, Itanium, Alpha,
PA-RISC, PowerPC, and SPARC, with Linux, Microsoft Windows, HP/UX, Solaris
and MACOSX operating systems. Some implementations are more complete than
others.

It should be useful both for high performance multi-threaded code which can't
afford to use the standard locking primitives, or for code that has to access
shared data structures from signal handlers. For details, see README.txt in
the distribution.

The most recent version adds support for operations on data of different
sizes, and adds an optional library providing almost-lock-free stacks (see
Boehm, "An almost non-blocking stack", also here) and a signal-handler-safe
memory allocator based on it. See README_stack.txt and README_malloc.txt for
details.


%prep
#setup -q -n % {snapshot_vendor}-% {name}-% {snapshot}
%setup -q -n %{name}-%{version}%{prever}
%apply_patches

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n  %{libname_devel}
%{_includedir}/*.h
%dir %{_includedir}/%{rawname}
%{_includedir}/%{rawname}/*.h
%dir %{_includedir}/%{rawname}/sysdeps
#%{_includedir}/%{rawname}/sysdeps/README
%{_includedir}/%{rawname}/sysdeps/*.h
%dir %{_includedir}/%{rawname}/sysdeps/gcc
%{_includedir}/%{rawname}/sysdeps/gcc/*.h
%dir %{_includedir}/%{rawname}/sysdeps/hpc
%{_includedir}/%{rawname}/sysdeps/hpc/*.h
%dir %{_includedir}/%{rawname}/sysdeps/ibmc
%{_includedir}/%{rawname}/sysdeps/ibmc/*.h
%dir %{_includedir}/%{rawname}/sysdeps/icc
%{_includedir}/%{rawname}/sysdeps/icc/*.h
%dir %{_includedir}/%{rawname}/sysdeps/msftc
%{_includedir}/%{rawname}/sysdeps/msftc/*.h
%dir %{_includedir}/%{rawname}/sysdeps/sunc
%{_includedir}/%{rawname}/sysdeps/sunc/*.h
%dir %{_includedir}/%{rawname}/sysdeps/armcc
%{_includedir}/%{rawname}/sysdeps/armcc/*.h
%dir %{_datadir}/%{libname}
%{_datadir}/%{libname}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.a
