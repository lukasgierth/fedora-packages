%define debug_package %{nil}

Name:           kwin-dynamic-workspaces
# renovate: datasource=github-releases depName=maurges/dynamic_workspaces extractVersion=true
Version:        a06e723804398d672be74eba0cd4ccee062e1410
Release:        1%{?dist}
Summary:        A kwin script that creates and deletes desktops as you move windows on the last one
License:        BSD
URL:            https://github.com/maurges/dynamic_workspaces
Source0:        %{url}/archive/%{version}.tar.gz#/dynamic_workspaces-%{version}.tar.gz

Requires:       kwin

%description

%prep
%autosetup -n dynamic_workspaces-%{version}

%install
mkdir -p %{buildroot}%{_datadir}/kwin-wayland/scripts/dynamic_workspaces
cp metadata.json %{buildroot}%{_datadir}/kwin-wayland/scripts/dynamic_workspaces/
cp -r contents %{buildroot}%{_datadir}/kwin-wayland/scripts/dynamic_workspaces/

%files
%license LICENSE
%doc README.md
%{_datadir}/kwin-wayland/scripts/dynamic_workspaces

%changelog
%autochangelog
