%global debug_package %{nil}

Name:       krew
# renovate: datasource=github-releases depName=kubernetes-sigs/krew extractVersion=true
Version:    0.4.5
Release:    1%{?dist}
Summary:    Find and install kubectl plugins
License:    Apache-2.0
URL:        https://github.com/kubernetes-sigs/%{name}
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang >= 1.25

%description

%prep
%autosetup -n %{name}-%{version}

%build
go build \
    -ldflags "-X main.version=%{version} -s -w" \
    -o _build/%{name} \
	./cmd/krew
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
