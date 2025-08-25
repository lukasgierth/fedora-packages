%global debug_package %{nil}

Name:           oh-my-posh
# renovate: datasource=github-releases depName=JanDeDobbeleer/oh-my-posh
Version:        26.19.1
Release:        3%{?dist}
Summary:        The most customisable and low-latency cross platform/shell prompt renderer
License:        MIT
URL:            https://github.com/JanDeDobbeleer/oh-my-posh
Source:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: golang
BuildRequires: git-core

%package -n oh-my-posh-themes
Summary: Default themes for oh-my-posh
Requires: oh-my-posh
BuildArch: noarch

%description
Oh My Posh is a highly customisable and extensible cross shell prompt theme engine.

%description -n oh-my-posh-themes

%prep
%autosetup -n oh-my-posh-%{version}

%build
cd ./src/
go build \
    -trimpath \
    -buildmode=pie \
    -modcacherw \
    -ldflags "-linkmode=external -X main.version=v%{version} -s -w"

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/themes/
install -Dm 0755 src/src %{buildroot}%{_bindir}/oh-my-posh
install -Dm 0644 COPYING %{buildroot}%{_datadir}/licenses/oh-my-posh/COPYING
install -Dm 0644 themes/* %{buildroot}%{_datadir}/%{name}/themes/

%files
%{_bindir}/oh-my-posh
%license %{_datadir}/licenses/oh-my-posh/COPYING

%files -n oh-my-posh-themes
%{_datadir}/%{name}/themes/

%changelog
%autochangelog
