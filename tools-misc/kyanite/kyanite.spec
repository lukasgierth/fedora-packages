%define debug_package %{nil}

Name:           kyanite
# renovate: datasource=github-releases depName=MurderFromMars/Kyanite extractVersion=true
Version:        1.4.1
Release:        1%{?dist}
Summary:        Kyanite is a kwin extension designed to bring a fluid and minimalist dynamic workspace system to Plasma 6
License:        MIT
URL:            https://github.com/MurderFromMars/Kyanite
Source0:	    %{url}/archive/refs/tags/V%{version}.tar.gz

BuildArch: noarch

Requires: kwin

%description

%prep
%autosetup -n Kyanite-%{version}

%install
mkdir -p %{buildroot}%{_datadir}/kwin-wayland/scripts/kyanite
cp metadata.json %{buildroot}%{_datadir}/kwin-wayland/scripts/kyanite/
cp -r contents %{buildroot}%{_datadir}/kwin-wayland/scripts/kyanite/

%files
%license LICENSE
%doc README.md
%{_datadir}/kwin-wayland/scripts/kyanite

%changelog
%autochangelog
