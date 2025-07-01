%global __os_install_post %{nil}
Name:    ansel-bin
Version: 0.0.0+1996.gb51cfa3
Release: %autorelease
Summary: Ansel Photo Editor (based on darktable)
License: GPLv3
URL:     https://github.com/aurelienpierreeng/ansel
Source:  https://github.com/aurelienpierreeng/ansel/releases/download/v0.0.0/Ansel-%{version}-x86_64.AppImage
Source2: ansel.desktop
Source3: ansel.svg

Requires: fuse

%description
TODO

%prep

%build

%install
install -Dpm 0755 %{_sourcedir}/Ansel-%{version}-x86_64.AppImage %{buildroot}%{_bindir}/ansel
install -Dpm 0644 %{_sourcedir}/ansel.desktop %{buildroot}/usr/share/applications/ansel.desktop
install -Dpm 0644 %{_sourcedir}/ansel.svg %{buildroot}/usr/share/icons/ansel.svg

%files
%{_bindir}/ansel
/usr/share/applications/ansel.desktop
/usr/share/icons/ansel.svg

%changelog
%autochangelog
