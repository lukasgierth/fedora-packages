%global debug_package %{nil}

Name:       sops
# renovate: datasource=github-releases depName=getsops/sops extractVersion=true
Version:    3.11.0
Release:    1%{?dist}
Summary:    Simple and flexible tool for managing secrets
License:    MPL-2.0
URL:        https://github.com/getsops/%{name}
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang >= 1.24

%description

%prep
%autosetup -n %{name}-%{version}

%build
go build \
    -ldflags "-X main.version=%{version} -s -w" \
    -o _build/%{name} \
	./cmd/sops

%install
install -Dpm 0755 _build/%{name} -t %{buildroot}%{_bindir}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
