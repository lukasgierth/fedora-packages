%global debug_package %{nil}

Name:       otel-tui
# renovate: datasource=github-releases depName=ymtdzzz/otel-tui extractVersion=true
Version:    0.7.0
Release:    1%{?dist}
Summary:    A terminal OpenTelemetry viewer inspired by otel-desktop-viewer
License:    Apache-2.0
URL:        https://github.com/ymtdzzz/otel-tui
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang >= 1.24.7

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
%doc README.md docs
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
%autochangelog
