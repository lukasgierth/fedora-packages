%global __os_install_post %{nil}
Name:    sjust
Version: 0.8
Release: %autorelease
Summary: Helper based on just
License: GPLv3
Source1: justfile
Source2: sjust
Source3: sjust-interactive

Requires: just
Requires: fzf
Requires: gawk
Requires: coreutils

%description

%prep

%build

%install
install -Dpm 0755 %{_sourcedir}/sjust %{buildroot}%{_bindir}/sjust
install -Dpm 0755 %{_sourcedir}/sjust-interactive %{buildroot}%{_bindir}/sjust-interactive
install -Dpm 0644 %{_sourcedir}/justfile %{buildroot}/usr/share/sjust/justfile

%files
%{_bindir}/sjust
%{_bindir}/sjust-interactive
/usr/share/sjust/justfile

%changelog
%autochangelog
