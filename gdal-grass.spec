%define name gdal-grass
%define version 1.3.2
%define release %mkrel 1
%define grasspath %{_libdir}/grass60

Summary: 	GRASS plugin extension for the Geospatial Data Abstraction Library and OGR
Name:    	%name
Version: 	%version
Release: 	%release
Source0: 	http://www.gdal.org/dl/%{name}-%{version}.tar.bz2
Patch:		gdal-grass-1.3.1-fix-install-prefix.patch
License: 	MIT
Group:   	Sciences/Geosciences
URL:     	http://www.gdal.org/

BuildRequires: proj-devel, zlib-devel, gdal-devel >= 1.3.1, grass
Requires: gdal >= 1.3.1
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
This package contains the GRASS support (plugin) for
the GDAL/OGR libraries.

%prep
#%setup -q -n %{name}-1.3.1
%setup -q
%patch -p1 -b .destdir

%build
export LD_LIBRARY_PATH=%{grasspath}/%_lib
%configure \
  --with-grass=%{grasspath}  \
  --with-autoload=%{_libdir}/gdalplugins
%make

%install
rm -Rf %{buildroot}
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/gdalplugins/gdal_GRASS.so
%{_libdir}/gdalplugins/ogr_GRASS.so
%{_datadir}/gdal/grass/etc/datum.table
%{_datadir}/gdal/grass/etc/ellipse.table
%doc README

