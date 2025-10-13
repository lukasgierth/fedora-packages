%global debug_package %{nil}

Name:       nom
# renovate: datasource=github-releases depName=guyfedwards/nom extractVersion=true
Version:    2.18.0
Release:    1%{?dist}
Summary:    RSS reader for the terminal
License:    GPL-3.0
URL:        https://github.com/guyfedwards/nom
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
    cmd/nom/main.go
go-md2man -in README.md -out %{name}.1

%install
install -Dpm 0755 _build/%{name} -t %{buildroot}%{_bindir}
install -Dpm 0644 %{name}.1 -t %{buildroot}/%{_mandir}/man1/


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
%autochangelog
