%global __os_install_post %{nil}
Name:    flatpak-downgrade
Version: 0.1
Release: 1%{?dist}
Summary: Python script that lets you interactively downgrade and mask flatpak apps, written mostly by Gemini (LLM)
License: GPL-3.0-or-later
Source0: flatpak-downgrade

BuildArch: noarch

Requires: python
Requires: flatpak

%description

%prep

%build

%install
install -Dpm 0755 %{_sourcedir}/flatpak-downgrade %{buildroot}%{_bindir}/flatpak-downgrade

%files
%{_bindir}/flatpak-downgrade

%changelog
%autochangelog
