%define name gdal-grass
%define version 1.4.3
%define release %mkrel 2
%define grasspath %{_libdir}/grass62

Summary: 	GRASS plugin extension for the Geospatial Data Abstraction Library and OGR
Name:    	%name
Version: 	%version
Release: 	%release
Source0: 	http://download.osgeo.org/gdal/%{name}-%{version}.tar.gz
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
%{_datadir}/gdal/grass/
%doc README

