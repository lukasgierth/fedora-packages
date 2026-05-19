%global debug_package %{nil}

Name:    siomon
# renovate: datasource=github-releases depName=level1techs/siomon extractVersion=true
Version: 0.2.3
Release: 1%{?dist}
Summary: A comprehensive Linux hardware information and real-time sensor monitoring tool
License: MIT
URL:     https://github.com/level1techs/%{name}
Source:  %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release

%install
install -Dpm 0755 target/release/sio -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/sio

%changelog
%autochangelog
