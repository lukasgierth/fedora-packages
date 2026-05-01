%global debug_package %{nil}

Name:       calicoctl
# renovate: datasource=github-releases depName=projectcalico/calico extractVersion=true
Version:    3.32.0
Release:    1%{?dist}
Summary:    Calico CLI
License:    Apache-2.0
URL:        https://github.com/projectcalico/calico
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang

%description

%prep
%autosetup -n calico-%{version}

%build
export GOTOOLCHAIN=auto
go build \
    -ldflags "-X github.com/projectcalico/calico/pkg/buildinfo.Version=%{version} -s -w" \
    -o _build/%{name} \
	./calicoctl/calicoctl
go-md2man -in README.md -out %{name}.1

%install
install -Dpm 0755 _build/%{name} -t %{buildroot}%{_bindir}
install -Dpm 0644 %{name}.1 -t %{buildroot}/%{_mandir}/man1/

%files
%license LICENSE.md
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
%autochangelog
