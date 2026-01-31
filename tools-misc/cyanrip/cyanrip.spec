%global debug_package %{nil}
Name:           cyanrip
# renovate: datasource=github-releases depName=cyanreg/cyanrip extractVersion=true
Version:        0.9.3.1
Release:        1%{?dist}
Summary:        Fully featured CD ripping program
License:        LGPLv2.1+
URL:            https://github.com/cyanreg/%{name}
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
Buildrequires:  pkgconfig(libavcodec) >= 59.24.100
Buildrequires:  pkgconfig(libavfilter) >= 7.16.100
Buildrequires:  pkgconfig(libavformat) >= 58.13.100
Buildrequires:  pkgconfig(libavutil) >= 57.25.100
Buildrequires:  pkgconfig(libswresample) >= 4.5.100
BuildRequires:  pkgconfig(libmusicbrainz5) >= 5.1
BuildRequires:  pkgconfig(libcdio_paranoia) >= 10.2
BuildRequires:  pkgconfig(libcurl) >= 7.66.0

%description
Fully featured CD ripping program able to take out most of the tedium. Fully
accurate, has advanced features most rippers don't, yet has no bloat.

%prep
%autosetup

%build
%meson
%ninja_build -C %{_vpath_builddir}

%install
%ninja_install -C %{_vpath_builddir}

%files
%license LICENSE.md
%doc README.md Changelog.md
%{_bindir}/%{name}
