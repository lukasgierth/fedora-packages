%global debug_package %{nil}

Name:    sysz
Version: 1.4.3
Release: %autorelease
Summary: A fzf terminal UI for systemctl
License: UNLICENSE
URL:     https://github.com/joehillen/%{name}
Source:  https://github.com/joehillen/%{name}/archive/refs/tags/%{version}.tar.gz

Requires: awk
Requires: bash > 4.3
Requires: fzf >= 0.27.1

%description
TODO

%prep
%autosetup -n %{name}-%{version}

%build

%install
install -Dpm 0755 sysz -t %{buildroot}%{_bindir}/

%files
%license UNLICENSE
%{_bindir}/sysz

%changelog
%autochangelog
