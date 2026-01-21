%global debug_package %{nil}

Name:       golazo
# renovate: datasource=github-releases depName=0xjuanma/golazo extractVersion=true
Version:    0.15.0
Release:    1%{?dist}
Summary:    Golazo is a terminal app for keeping up with live football/soccer. Check scores, match events, and stats from major leagues without leaving your terminal.
License:    MIT
URL:        https://github.com/0xjuanma/golazo
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang >= 1.25

Requires: libnotify

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
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
%autochangelog
