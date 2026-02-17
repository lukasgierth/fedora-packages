%define debug_package %{nil}

Name:           karousel
# renovate: datasource=github-releases depName=peterfajdiga/karousel extractVersion=true
Version:        0.15
Release:        1%{?dist}
Summary:        Scrollable tiling Kwin script
License:        GPL-3.0-or-later
URL:            https://github.com/peterfajdiga/%{name}
Source0:	    %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: npm
BuildRequires: typescript

Requires: kwin

%description

%prep
%autosetup -n %{name}-%{version}

%build
make build

%install
mkdir -p %{buildroot}%{_datadir}/kwin-wayland/scripts/%{name}
cp package/metadata.json %{buildroot}%{_datadir}/kwin-wayland/scripts/%{name}
cp -r package/contents %{buildroot}%{_datadir}/kwin-wayland/scripts/%{name}

%files
%license LICENSE
%doc README.md
%{_datadir}/kwin-wayland/scripts/%{name}

%changelog
%autochangelog
