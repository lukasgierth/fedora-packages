%global debug_package %{nil}

Name:   	noctalia-shell
# renovate: datasource=github-releases depName=noctalia-dev/noctalia-shell extractVersion=true
Version:	4.4.3
Release:	1%{?dist}
Summary:	A sleek and minimal desktop shell thoughtfully crafted for Wayland, built with Quickshell.
License:	MIT
URL:		https://github.com/noctalia-dev/%{name}
Source0:	%{url}/releases/download/v%{version}/noctalia-v%{version}.tar.gz

BuildArch:	noarch

Requires:	brightnessctl
Requires:	dejavu-sans-fonts
Requires:	gpu-screen-recorder
Requires:	qt6-qtmultimedia
Requires:	quickshell

Recommends:	cava
Recommends:	cliphist
Recommends:	ddcutil
Recommends:	matugen
Recommends:	power-profiles-daemon
Recommends:	wlsunset

%description

%prep
# %autosetup -n noctalia-release -p1
%setup -q -n noctalia-release

%build

%install
install -d -m 0755 %{buildroot}/etc/xdg/quickshell/noctalia-shell
cp -r ./* %{buildroot}/etc/xdg/quickshell/noctalia-shell/

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/xdg/quickshell/noctalia-shell/

%changelog
%autochangelog
