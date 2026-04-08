%global debug_package %{nil}

Name:       gh-dash
# renovate: datasource=github-releases depName=dlvhdr/gh-dash extractVersion=true
Version:    4.23.2
Release:    1%{?dist}
Summary:    A rich terminal UI for GitHub that doesn't break your flow.
License:    MIT
URL:        https://github.com/dlvhdr/%{name}
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang

Requires: gh

%description

%prep
%autosetup -n %{name}-%{version}

%build
export GOTOOLCHAIN=auto
export BUILD_DATE=$(date --iso-8601)
export COMMIT=$(git rev-parse HEAD)
go build \
    -ldflags "-X github.com/dlvhdr/gh-dash/v4/cmd.Version=%{version} -X github.com/dlvhdr/gh-dash/v4/cmd.Date=$BUILD_DATE -X github.com/dlvhdr/gh-dash/v4/cmd.Commit=$COMMIT -s -w" \
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
