Summary: The RoboCup Soccer Client Library
Name: librcsc
Version: 4.1.0
Release: 0
License: LGPL
Group: Development/Library
Source: %{name}-%{version}.tar.gz
#Patch:
URL: http://rctools.sourceforge.jp/
Packager: Hidehisa Akiyama <akky@users.sourceforge.jp>
BuildRoot: %{_tmppath}/%{name}-root

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: boost-devel >= 1.32

%description
librcsc is a base library of the soccer agent and/or the tool
program for the RoboCup soccer 2D simulation.

%package devel
Summary: The RoboCup Soccer Client Library Development Package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: boost-devel >= 1.32

%description devel
librcsc is a base library to develop a soccer agent and/or a tool
program for the RoboCup soccer 2D simulation.
Install librcsc-devel if you want to write your own program.

%prep
rm -rf %{buildroot}

%setup

#%patch -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf ${buildroot}

%makeinstall

# remove libtool .la file
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING.LESSER INSTALL NEWS README
%{_bindir}/*
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS COPYING.LESSER INSTALL NEWS README
%{_libdir}/lib*.so
%{_libdir}/*.a
%{_includedir}/rcsc

%changelog

* Wed Sep 27 2006 Hidehisa Akiyama <akky@users.sourceforge.jp>
-created initial version.
