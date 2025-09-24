%global debug_package %{nil}

Name:       lazysql
# renovate: datasource=github-releases depName=jorgerojas26/lazysql extractVersion=true
Version:    0.4.2
Release:    1%{?dist}
Summary:    A cross-platform TUI database management tool written in Go.
License:    MIT
URL:        https://github.com/jorgerojas26/%{name}
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang >= 1.23

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
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
%autochangelog
