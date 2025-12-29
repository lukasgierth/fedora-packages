%global debug_package %{nil}

Name:       lazyjournal
# renovate: datasource=github-releases depName=Lifailon/lazyjournal extractVersion=true
Version:    0.8.3
Release:    1%{?dist}
Summary:    A TUI for reading logs from journald, auditd, file system, Docker (including Swarm) containers, Podman and Kubernetes pods with support for output coloring and multiple filtering modes.
License:    MIT
URL:        https://github.com/Lifailon/%{name}
Source:     %{url}/archive/refs/tags/%{version}.tar.gz

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
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
%autochangelog
