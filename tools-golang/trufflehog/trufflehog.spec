%global debug_package %{nil}

Name:       trufflehog
# renovate: datasource=github-releases depName=trufflesecurity/trufflehog extractVersion=true
Version:    3.92.5
Release:    1%{?dist}
Summary:    Find, verify, and analyze leaked credentials
License:    AGPL-3.0-only
URL:        https://github.com/trufflesecurity/trufflehog
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
    -o _build/%{name}
go-md2man -in README.md -out %{name}.1

%install
install -Dpm 0755 _build/%{name} -t %{buildroot}%{_bindir}
install -Dpm 0644 %{name}.1 -t %{buildroot}/%{_mandir}/man1/


%files
%license LICENSE
%doc README.md CONTRIBUTING.md docs/
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
%autochangelog
