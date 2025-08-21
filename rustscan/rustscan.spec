%global debug_package %{nil}

Name:    RustScan
# renovate: datasource=github-releases depName=bee-san/RustScan
Version: 2.4.1
Release: %autorelease
Summary: The Modern Port Scanner. Find ports quickly (3 seconds at its fastest). Run scripts through our scripting engine (Python, Lua, Shell supported).
License: GPLv3
URL:     https://github.com/bee-san/%{name}
Source:  %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

Requires: nmap

%description

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release

%install
install -Dpm 0755 target/release/rustscan -t %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/rustscan

%changelog
%autochangelog
