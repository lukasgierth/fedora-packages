%global debug_package %{nil}
%global _missing_build_ids_terminate_build 0

Name:           act-cli
# renovate: datasource=github-releases depName=nektos/act
Version:        0.2.80
Release:        3%{?dist}
Summary:        Run your GitHub Actions locally
License:        MIT
URL:            https://github.com/nektos/act
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
# Patch:          0001-Downgrade-go-to-1.23.patch

BuildRequires:  git-core
BuildRequires:  golang
BuildRequires:  make

Requires:       (podman or moby or docker or docker-ce or docker-ce-cli or docker-ee)

%description
Run your GitHub Actions locally

%prep
%autosetup -n act-%{version}

%build
go mod tidy
go build \
    -trimpath \
    -buildmode=pie \
    -modcacherw \
    -ldflags "-linkmode=external -X main.version=v%{version}"

%install
install -Dm 0755 act %{buildroot}%{_bindir}/act-cli
install -Dm 0644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%files
%{_bindir}/act-cli
%license %{_datadir}/licenses/%{name}/LICENSE

%changelog
%autochangelog
