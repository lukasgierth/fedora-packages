%global debug_package %{nil}

Name:       argonaut
# renovate: datasource=github-releases depName=darksworm/argonaut extractVersion=true
Version:    2.17.0
Release:    1%{?dist}
Summary:    Keyboard-first terminal UI for Argo CD. Browse apps, scope by clusters/namespaces/projects, stream live resource status, trigger syncs, inspect diffs, and roll back safely — all without leaving your terminal.
License:    GPL-3.0-or-later
URL:        https://github.com/darksworm/%{name}
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang

Requires: argocd
Recommends: git-delta

%description

%prep
%autosetup -n %{name}-%{version}

%build
export GOTOOLCHAIN=auto
go build \
    -ldflags "-X main.appVersion=%{version} -s -w" \
    -o _build/%{name} \
    ./cmd/app
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
