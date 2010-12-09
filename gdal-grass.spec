%define name gdal-grass
%define version 1.4.3
%define release %mkrel 8
%define grasspath %{_libdir}/grass64

Summary: 	GRASS plugin extension for the Geospatial Data Abstraction Library and OGR
Name:    	%name
Version: 	%version
Release: 	%release
Source0: 	http://download.osgeo.org/gdal/%{name}-%{version}.tar.gz
Patch:		gdal-grass-1.3.1-fix-install-prefix.patch
Patch1:		gdal-grass-1.4.3-ldflags.patch
License: 	MIT
Group:   	Sciences/Geosciences
URL:     	http://www.gdal.org/
BuildRequires:	gdal-devel >= 1.3.1, grass >= 6.4
Requires: gdal >= 1.3.1
Requires:	grass >= 6.4
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
This package contains the GRASS support (plugin) for
the GDAL/OGR libraries.

%prep
%setup -q
%patch -p1 -b .destdir
%patch1 -p0 -b .ldflags

%build
export LD_LIBRARY_PATH=%{grasspath}/%_lib
%configure2_5x \
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
