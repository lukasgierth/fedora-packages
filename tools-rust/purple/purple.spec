%global debug_package %{nil}

Name:    purple
# renovate: datasource=github-releases depName=erickochen/purple extractVersion=true
Version: 2.45.0
Release: 2%{?dist}
Summary: Terminal cockpit for your servers. Search, connect, transfer files, manage containers and run commands across hosts. Syncs from 16 cloud providers. Edits ~/.ssh/config directly.
License: MIT
URL:     https://github.com/erickochen/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust
BuildRequires: openssl-devel

Requires: openssl

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
