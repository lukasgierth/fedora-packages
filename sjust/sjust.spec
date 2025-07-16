%global __os_install_post %{nil}
Name:    sjust
Version: 0.1
Release: %autorelease
Summary: Helper based on just
License: GPLv3
Source1: justfile
Source2: sjust

Requires: just

%description
TODO

%prep

%build

%install
install -Dpm 0755 %{_sourcedir}/sjust %{buildroot}%{_bindir}/sjust
install -Dpm 0644 %{_sourcedir}/justfile %{buildroot}/usr/share/sjust/justfile

%files
%{_bindir}/sjust
/usr/share/sjust/justfile

%changelog
%autochangelog
