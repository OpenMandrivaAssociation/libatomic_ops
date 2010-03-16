%define rawname atomic_ops
# Can't use mklibname as the name should be the same on all arches
%define libname lib%{rawname}
%define libname_devel %mklibname -d %{rawname}

%define version 1.2
%define release %mkrel 5

Summary:   Multiplatform atomic memory operation library
Name:      %{libname}
Version:   %{version}
Release:   %{release}
License:   MIT/GPL
Group:     System/Libraries
Source:    lib%{rawname}-%{version}.tar.gz
Patch1:    01_s390_include.patch
Patch2:    02_mips.patch
Patch3:    libatomic_ops-1.2-installonce.patch
Patch4:    04_m68k-rediff.patch
Patch5:    libatomic_ops-1.2-ppc.patch
URL:       http://www.hpl.hp.com/research/linux/atomic_ops/
BuildRoot: %{_tmppath}/%{name}-buildroot

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

%files -n  %{libname_devel}
%defattr(-,root,root)
%{_includedir}/*.h
%dir %{_includedir}/%{rawname}
%{_includedir}/%{rawname}/*.h
%dir %{_includedir}/%{rawname}/sysdeps
%{_includedir}/%{rawname}/sysdeps/README
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
%{_libdir}/*.a
%dir %{_datadir}/%{libname}
%{_datadir}/%{libname}/*


%prep
%setup -q -n %{libname}-%{version}
%patch1 -p0
%patch2 -p1
%patch3 -p1 -b .installonce
%patch4 -p1
%patch5 -p1 -b .ppc

%build
autoreconf
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}
