%global debug_package %{nil}

Name:       lazydocker
# renovate: datasource=github-releases depName=jesseduffield/lazydocker extractVersion=true
Version:    0.24.1
Release:    1%{?dist}
Summary:    The lazier way to manage everything docker
License:    MIT
URL:        https://github.com/jesseduffield/%{name}
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core >= 2.0
BuildRequires: go-md2man
BuildRequires: golang >= 1.19

Requires: (docker-ce or moby-engine)
Requires: (docker-ce-cli or docker-cli)
Suggests: (docker-compose-plugin or docker-compose)

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
%doc README.md docs/
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
%autochangelog
