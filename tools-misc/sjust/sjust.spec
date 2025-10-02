%global __os_install_post %{nil}
Name:    sjust
Version: 1.21
Release: 1%{?dist}
Summary: Helper based on just
License: GPLv3
Source1: justfile
Source2: sjust
Source3: sjust-fzf
Source4: system-update.desktop
Source5: system-update.svg
Source6: firmware-update.desktop
Source7: firmware-update.svg
# SVG
# downloaded from: https://www.svgrepo.com/svg/451874/software-update-urgent
# LICENSE: GPL
# downloaded from: https://www.svgrepo.com/download/164645/usb-cable

BuildArch: noarch

Requires: bash
Requires: coreutils
Requires: fish
Requires: fzf
Requires: gawk
Requires: just

%description

%prep

%build

%install
install -Dpm 0644 %{_sourcedir}/justfile %{buildroot}%{_datadir}/sjust/justfile
install -Dpm 0644 %{_sourcedir}/system-update.desktop %{buildroot}%{_datadir}/applications/system-update.desktop
install -Dpm 0644 %{_sourcedir}/system-update.svg %{buildroot}%{_datadir}/pixmaps/system-update.svg
install -Dpm 0644 %{_sourcedir}/firmware-update.desktop %{buildroot}%{_datadir}/applications/firmware-update.desktop
install -Dpm 0644 %{_sourcedir}/firmware-update.svg %{buildroot}%{_datadir}/pixmaps/firmware-update.svg
install -Dpm 0755 %{_sourcedir}/sjust %{buildroot}%{_bindir}/sjust
install -Dpm 0755 %{_sourcedir}/sjust-fzf %{buildroot}%{_bindir}/sjust-fzf

%files
%{_bindir}/sjust
%{_bindir}/sjust-fzf
%{_datadir}/applications/firmware-update.desktop
%{_datadir}/applications/system-update.desktop
%{_datadir}/pixmaps/firmware-update.svg
%{_datadir}/pixmaps/system-update.svg
%{_datadir}/sjust/justfile

%changelog
%autochangelog
