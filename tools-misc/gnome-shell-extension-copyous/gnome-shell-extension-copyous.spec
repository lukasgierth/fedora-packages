%global debug_package %{nil}
%global uuid copyous@boerdereinar.dev

Name:           gnome-shell-extension-copyous
# renovate: datasource=github-releases depName=boerdereinar/copyous extractVersion=true
Version:        1.3.0
Release:        1%{?dist}
Summary:        Modern Clipboard Manager for GNOME
License:        GPL-3.0-or-later
URL:            https://github.com/boerdereinar/copyous
Source0:        %{url}/releases/download/v%{version}/%{uuid}.zip
Source1:        https://raw.githubusercontent.com/boerdereinar/copyous/refs/tags/v%{version}/LICENSE
Source2:        https://raw.githubusercontent.com/boerdereinar/copyous/refs/tags/v%{version}/README.md

Requires: gnome-shell

BuildArch: noarch

%description

%prep
%setup -c -T -a 0

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r -p * %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
cp %{SOURCE1} ./
cp %{SOURCE2} ./

%files
%license LICENSE
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}

%changelog
%autochangelog
